"""Persistência, recuperação idempotente e suspensão sem contar tempo offline."""
from datetime import datetime, timedelta, timezone
import sys
from types import SimpleNamespace
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.launcher import Launcher
from checkpoint.statistics_periods import period_stats
from test_bugs_0134 import ui, sample


class Clock:
    def __init__(self):
        self.value = 1000.0
        self.wall = datetime(2026, 11, 21, 23, 59, 40, tzinfo=timezone.utc)
    def monotonic(self): return self.value
    def timestamp(self): return self.wall.isoformat()
    def advance(self, seconds):
        self.value += seconds
        self.wall += timedelta(seconds=seconds)


def tracked(library, monkeypatch):
    clock = Clock()
    process = SimpleNamespace(pid=812, poll=lambda: None)
    monkeypatch.setattr('checkpoint.launcher.subprocess.Popen', lambda *a, **k: process)
    game = library.save_game({'title': 'Jogo acompanhado', 'platform': 'PC'})
    launcher = Launcher(library, clock=clock.monotonic, timestamp=clock.timestamp)
    session = launcher.start_command(game, [sys.executable, '-c', 'pass'], True)
    return launcher, clock, game, session, process


def test_crash_recovers_only_persisted_prefix_once(library, monkeypatch):
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    clock.advance(10)
    launcher.poll()
    clock.advance(5)
    launcher.poll()
    assert library.sql.execute('SELECT duration_seconds FROM play_sessions').fetchone()[0] == 10
    clock.advance(100000)
    # Outra conexão representa a reabertura depois de um crash, sem interrupt/finish.
    reopened = Database(library.db.path)
    try:
        copy = Library(reopened)
        Launcher(copy, clock=clock.monotonic, timestamp=clock.timestamp)
        before = [tuple(row) for row in copy.sql.execute('SELECT * FROM play_sessions')]
        assert len(before) == 1
        assert copy.stats()['seconds'] == 10
        assert copy.sql.execute('SELECT ended_at FROM play_sessions').fetchone()[0] != clock.timestamp()
        Launcher(copy, clock=clock.monotonic, timestamp=clock.timestamp)
        assert [tuple(row) for row in copy.sql.execute('SELECT * FROM play_sessions')] == before
    finally:
        reopened.close()


def test_graceful_close_saves_last_seconds_without_killing_game(library, monkeypatch):
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    clock.advance(7)
    launcher.interrupt()
    assert not launcher.active
    assert process.poll() is None
    assert library.stats()['seconds'] == 7
    assert library.sql.execute('SELECT state FROM play_sessions').fetchone()[0] == 'finished'


def test_sleep_is_excluded_from_total_and_calendar(library, monkeypatch):
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    clock.advance(10)
    launcher.suspend()
    clock.advance(3600)
    launcher.resume()
    clock.advance(10)
    launcher.finish(session)
    assert library.stats()['seconds'] == 20
    stats = period_stats(library, 'all', clock.wall+timedelta(seconds=1), timezone.utc)
    assert stats['sessions'] == 1
    assert stats['daily'] == {'2026-11-21': 10, '2026-11-22': 10}


def test_large_unsampled_gap_is_not_assumed_to_be_play(library, monkeypatch):
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    clock.advance(10)
    launcher.poll()
    clock.advance(7200)
    launcher.poll()
    clock.advance(5)
    launcher.finish(session)
    assert library.stats()['seconds'] == 15
    assert library.setting(f'sessions.gap.{session}') is not None


def test_shutdown_query_does_not_finish_if_shutdown_is_cancelled(library, monkeypatch):
    from checkpoint.session_events import SessionEvents
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    events = SessionEvents(launcher)
    clock.advance(6)
    events.handle_code(0x11, 0)  # WM_QUERYENDSESSION
    events.handle_code(0x16, 0)  # WM_ENDSESSION cancelado
    assert session in launcher.active
    assert library.sql.execute('SELECT duration_seconds FROM play_sessions').fetchone()[0] == 6
    clock.advance(2)
    events.handle_code(0x16, 1)
    assert not launcher.active
    assert library.stats()['seconds'] == 8


def test_checkpoint_failure_is_retryable_without_losing_elapsed_time(library, monkeypatch):
    import sqlite3
    import pytest
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    real = library.sql
    class FailedWrite:
        def __enter__(self):
            real.__enter__()
            return self
        def __exit__(self, *args): return real.__exit__(*args)
        def execute(self, sql, *args):
            if sql.startswith('UPDATE play_sessions SET ended_at'):
                raise sqlite3.OperationalError('fixture: disco cheio')
            return real.execute(sql, *args)
    clock.advance(10)
    library.sql = FailedWrite()
    try:
        with pytest.raises(sqlite3.OperationalError): launcher.checkpoint()
    finally:
        library.sql = real
    assert real.execute('SELECT duration_seconds FROM play_sessions').fetchone()[0] == 0
    launcher.checkpoint()
    assert real.execute('SELECT duration_seconds FROM play_sessions').fetchone()[0] == 10
    clock.advance(1)
    launcher.finish(session)
    assert library.stats()['seconds'] == 11


def test_invalid_checkpoint_does_not_prevent_opening_or_invent_time(library):
    game = library.save_game({'title': 'Sessão antiga', 'platform': 'PC'})
    with library.sql:
        session = library.sql.execute("INSERT INTO play_sessions(game_id,started_at,pid) VALUES(?,'2026-11-21T00:00:00+00:00',812)", (game,)).lastrowid
        library.sql.execute('INSERT INTO settings(key,value) VALUES(?,?)', (f'sessions.checkpoint.{session}', '{invalid'))
    Launcher(library)
    assert library.sql.execute('SELECT state,duration_seconds FROM play_sessions').fetchone()[:] == ('interrupted', 0)
    assert library.stats()['seconds'] == 0


def test_busy_database_does_not_block_gui_for_general_timeout(library, monkeypatch):
    import sqlite3
    import time
    import pytest
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    other = sqlite3.connect(library.db.path)
    clock.advance(10)
    try:
        other.execute('BEGIN IMMEDIATE')
        started = time.perf_counter()
        with pytest.raises(sqlite3.OperationalError): launcher.checkpoint()
        assert time.perf_counter()-started < 0.5
    finally:
        other.rollback()
        other.close()
    launcher.checkpoint()
    assert library.sql.execute('PRAGMA busy_timeout').fetchone()[0] == 10000
    assert library.sql.execute('SELECT duration_seconds FROM play_sessions').fetchone()[0] == 10


def test_process_exit_retry_does_not_count_time_after_exit(library, monkeypatch):
    import sqlite3
    import pytest
    launcher, clock, game, session, process = tracked(library, monkeypatch)
    clock.advance(10)
    process.poll = lambda: 0
    other = sqlite3.connect(library.db.path)
    try:
        other.execute('BEGIN IMMEDIATE')
        with pytest.raises(sqlite3.OperationalError): launcher.poll()
    finally:
        other.rollback()
        other.close()
    clock.advance(5)
    assert launcher.poll() == [game]
    assert library.stats()['seconds'] == 10


def test_dismissal_is_per_session_persistent_and_manual_review_still_works(ui, app, monkeypatch):
    window, game = ui
    with window.library.sql:
        first = window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state) VALUES(?,'2026-11-21T10:00:00+00:00','interrupted')", (game,)).lastrowid
        second = window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state) VALUES(?,'2026-11-21T11:00:00+00:00','interrupted')", (game,)).lastrowid
    answers = iter([(0, False), (3, True)])
    monkeypatch.setattr('checkpoint.dialog_style.AppInputs.getInt', lambda *a, **k: next(answers))
    window.recover_sessions(automatic=True)
    assert window.library.setting(f'sessions.review_dismissed.{first}') is True
    assert window.library.sql.execute('SELECT state,duration_seconds FROM play_sessions WHERE id=?', (first,)).fetchone()[:] == ('interrupted', 0)
    assert window.library.sql.execute('SELECT duration_seconds FROM play_sessions WHERE id=?', (second,)).fetchone()[0] == 180
    from checkpoint.session_tracking import pending_reviews
    assert not pending_reviews(window.library)
    reopened = Database(window.library.db.path)
    try:
        assert not pending_reviews(Library(reopened))
    finally:
        reopened.close()
    monkeypatch.setattr('checkpoint.dialog_style.AppInputs.getInt', lambda *a, **k: (2, True))
    window.recover_sessions()
    assert window.library.stats()['seconds'] == 300
    assert not pending_reviews(window.library, include_dismissed=True)

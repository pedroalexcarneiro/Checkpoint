"""Checkpoints de sessões sem migração destrutiva nem duração offline presumida."""
from datetime import datetime
import json
import math


def _put(sql, key, value):
    sql.execute('INSERT INTO settings(key,value) VALUES(?,?) '
                'ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                (key, json.dumps(value)))


def valid_checkpoint(row, value):
    if not isinstance(value, dict) or value.get('version') != 1:
        return False
    if type(value.get('seconds')) is not int or value['seconds'] < 0:
        return False
    if (value.get('game_id') != row['game_id'] or value.get('started_at') != row['started_at']
            or value.get('ended_at') != row['ended_at']
            or value.get('seconds') != row['duration_seconds']):
        return False
    spans = value.get('spans')
    if not isinstance(spans, list) or not spans:
        return False
    total = 0
    for span in spans:
        if not isinstance(span, dict) or type(span.get('seconds')) is not int or span['seconds'] < 0:
            return False
        try:
            stamp = datetime.fromisoformat(span['start'].replace('Z', '+00:00'))
            if stamp.tzinfo is None:
                return False
        except (TypeError, ValueError, KeyError, AttributeError):
            return False
        total += span['seconds']
    return total == row['duration_seconds']


def checkpoint_index(library):
    result={}
    for key,value in library.sql.execute("SELECT key,value FROM settings WHERE key LIKE 'sessions.checkpoint.%'"):
        try:result[int(key.rsplit('.',1)[-1])]=json.loads(value)
        except (ValueError,TypeError):continue
    return result


def observed_spans(library, row, checkpoints=None):
    """Intervalos comprovados; registros legados mantêm sua apresentação anterior."""
    try:
        value = (checkpoints.get(row['id']) if checkpoints is not None else
                 library.setting(f'sessions.checkpoint.{row["id"]}', None))
    except (ValueError,TypeError):
        value = None
    if valid_checkpoint(row, value):
        return [(span['start'], span['seconds']) for span in value['spans']]
    return [(row['started_at'], row['duration_seconds'])]


def pending_reviews(library, *, include_dismissed=False):
    rows = library.sql.execute("SELECT s.*,g.title FROM play_sessions s JOIN games g "
        "ON g.id=s.game_id WHERE s.state='interrupted' AND g.deleted_at IS NULL ORDER BY s.id").fetchall()
    return [dict(row) for row in rows if include_dismissed or not
            library.setting(f'sessions.review_dismissed.{row["id"]}', False)]


class SessionTracker:
    interval = 10
    maximum_unsampled_gap = 30

    def __init__(self, library, clock, timestamp):
        self.library = library
        self.clock = clock
        self.timestamp = timestamp
        self.samples = {}
        self.suspended = False
        checkpoints=checkpoint_index(library)
        with library.sql:
            for row in library.sql.execute("SELECT * FROM play_sessions WHERE state='active'").fetchall():
                value = checkpoints.get(row['id'])
                if valid_checkpoint(row, value):
                    library.sql.execute("UPDATE play_sessions SET state='finished' WHERE id=?", (row['id'],))
                    _put(library.sql, f'sessions.recovered.{row["id"]}',
                         {'at': timestamp(), 'checkpoint': row['ended_at']})
                else:
                    library.sql.execute("UPDATE play_sessions SET state='interrupted' WHERE id=?", (row['id'],))

    def started(self, session, game_id, stamp, anchor):
        self.samples[session] = {'game_id': game_id, 'started_at': stamp, 'last': anchor,
            'last_saved': anchor, 'spans': [{'start': stamp, 'seconds': 0.0}]}

    def checkpoint(self, active, *, force=False, reason='heartbeat', only=None, terminal=()):
        current = self.clock()
        stamp = self.timestamp()
        writes = []
        for session, sample in list(self.samples.items()):
            if session not in active or (only is not None and session not in only):
                continue
            delta = max(0.0, current-sample['last'])
            gap = None
            if not self.suspended and not sample.get('ended',False):
                if delta > self.maximum_unsampled_gap:
                    # Falta de amostra não comprova jogo: nunca somar suspensão
                    # perdida, hibernação ou relógio monotônico descontinuado.
                    gap = {'at': stamp, 'seconds': int(delta)}
                    sample['gap'] = gap
                    sample['spans'].append({'start': stamp, 'seconds': 0.0})
                else:
                    sample['spans'][-1]['seconds'] += delta
            sample['last'] = current
            if force or current-sample['last_saved'] >= self.interval:
                seconds = max(0, math.floor(sum(span['seconds'] for span in sample['spans'])))
                spans = [{'start': span['start'], 'seconds': max(0, math.floor(span['seconds']))}
                         for span in sample['spans']]
                spans[-1]['seconds'] += seconds-sum(span['seconds'] for span in spans)
                value = {'version': 1, 'game_id': sample['game_id'], 'started_at': sample['started_at'],
                         'ended_at': sample.get('stopped_at',stamp), 'seconds': seconds, 'spans': spans, 'reason': reason}
                writes.append((session, sample, value, sample.get('gap')))
        if not writes:
            return
        # Um auxiliar de download/indexação pode estar gravando. O timer da GUI
        # não deve aguardar o timeout geral de 10 s; falha rápida permite retry.
        sql=self.library.sql
        timeout=sql.execute('PRAGMA busy_timeout').fetchone()[0]
        sql.execute('PRAGMA busy_timeout=25')
        try:
            with sql:
                for session, sample, value, gap in writes:
                    updated = sql.execute("UPDATE play_sessions SET ended_at=?,duration_seconds=? "
                        "WHERE id=? AND state='active'", (value['ended_at'], value['seconds'], session))
                    if updated.rowcount:
                        _put(sql, f'sessions.checkpoint.{session}', value)
                        if gap:
                            _put(sql, f'sessions.gap.{session}', gap)
                        if session in terminal:
                            sql.execute("UPDATE play_sessions SET state='finished' WHERE id=?",(session,))
        finally:
            sql.execute(f'PRAGMA busy_timeout={int(timeout)}')
        for session,sample,value,gap in writes:
            sample['last_saved'] = current
            sample.pop('gap',None)

    def suspend(self, active):
        if self.suspended:
            return
        self.checkpoint(active, force=True, reason='suspend')
        self.suspended = True

    def resume(self, active):
        if not self.suspended:
            return
        current = self.clock()
        stamp = self.timestamp()
        for session, sample in self.samples.items():
            if session in active:
                sample['last'] = current
                sample['spans'].append({'start': stamp, 'seconds': 0.0})
        self.suspended = False

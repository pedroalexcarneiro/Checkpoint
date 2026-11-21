"""Quadros distintos e publicação imediata, sem jogos/contas pessoais."""
from types import SimpleNamespace
import pytest
from PySide6.QtGui import QColor, QImage, QPixmap
from PySide6.QtWidgets import QTabWidget
from checkpoint.design_system import ArtworkButton
from checkpoint.game_capture import capture_game, WindowsCapture
from test_bugs_0134 import ui, sample


@pytest.mark.parametrize('tab', [0, 2])
def test_each_capture_appears_immediately_in_visible_memories(ui, app, monkeypatch, tab):
    window, identity = ui
    window.launcher.active[1] = (SimpleNamespace(pid=101, poll=lambda: None), 0, identity, True)
    class Frames:
        color = 'red'
        def foreground_pid(self): return 101
        def capture(self, pid):
            assert pid == 101
            frame = QPixmap(80, 40); frame.fill(QColor(self.color)); return frame
    frames = Frames()
    monkeypatch.setattr('checkpoint.game_capture.WindowsCapture', lambda: frames)
    window.navigate(3)
    window.pages[3].findChild(QTabWidget, 'memoryTabs').setCurrentIndex(tab)
    paths = []
    try:
        for color in ('red', 'blue'):
            frames.color = color
            window.capture_game_window()
            for _ in range(5): app.processEvents()
            from artwork_wait import wait_for_memory_artwork
            wait_for_memory_artwork(window)
            assert window.current_page == 3 and window.stack.currentWidget() is window.pages[3]
            tabs = window.pages[3].findChild(QTabWidget, 'memoryTabs')
            assert tabs.currentIndex() == tab
            previews = tabs.currentWidget().findChildren(ArtworkButton)
            assert len(previews) == len(paths)+1
            assert previews[0].pixmap.toImage().pixelColor(10, 10) == QColor(color)
            row = window.library.sql.execute('SELECT * FROM media_files ORDER BY id DESC LIMIT 1').fetchone()
            assert row['game_id'] == identity
            paths.append(row['path'])
        assert paths[0] != paths[1]
        assert QImage(paths[0]).pixelColor(10, 10) == QColor('red')
        assert QImage(paths[1]).pixelColor(10, 10) == QColor('blue')
    finally: window.launcher.active.clear()


def test_capture_backend_reads_fresh_client_frame_and_rejects_changed_target(app):
    backend = object.__new__(WindowsCapture)
    backend.handle = 123
    backend.foreground_pid = lambda: 42
    backend.client_rect = lambda: (10, 20, 80, 40)
    calls = []
    def grab(rect):
        calls.append(rect)
        result = QPixmap(80, 40); result.fill(QColor('red' if len(calls) == 1 else 'blue')); return result
    backend.grab_client = grab
    first, second = backend.capture(42), backend.capture(42)
    assert len(calls) == 2
    assert first.toImage().pixelColor(0, 0) != second.toImage().pixelColor(0, 0)
    def moved(rect):
        backend.client_rect = lambda: (11, 20, 80, 40)
        return first
    backend.grab_client = moved
    with pytest.raises(ValueError, match='mudou'): backend.capture(42)


def test_capture_failure_keeps_visible_memories_and_existing_media(ui, monkeypatch):
    window, identity = ui
    window.navigate(3); before = window.pages[3]
    window.launcher.active[1] = (SimpleNamespace(pid=101, poll=lambda: None), 0, identity, True)
    def failed(): raise ValueError('Janela indisponível')
    monkeypatch.setattr('checkpoint.game_capture.WindowsCapture', failed)
    # O guard real retorna None ao informar o erro; preserve esse contrato.
    def guard(callback):
        with pytest.raises(ValueError): callback()
        return None
    monkeypatch.setattr(window, 'guard', guard)
    try:
        window.capture_game_window()
        assert window.pages[3] is before
        assert window.library.sql.execute('SELECT count(*) FROM media_files').fetchone()[0] == 0
    finally: window.launcher.active.clear()


@pytest.mark.parametrize('title', ['Portal 2 — janela controlada', 'Hades — janela controlada'])
def test_two_actual_window_frames_in_isolated_process(folder, title):
    import os, subprocess, sys, json
    platform='windows' if sys.platform=='win32' else 'offscreen'
    result=subprocess.run([sys.executable,'-m','scripts.check_capture_frames',str(folder),title],
        env={**os.environ,'QT_QPA_PLATFORM':platform},capture_output=True,text=True,
        encoding='utf-8',errors='replace',timeout=20)
    assert result.returncode==0,result.stdout+result.stderr
    evidence=json.loads(result.stdout)
    assert evidence['native_windows']==(sys.platform=='win32')
    assert evidence['frames']==['red','blue']
    assert QImage(str(folder/'red.png')).pixelColor(10,10)==QColor('red')
    assert QImage(str(folder/'blue.png')).pixelColor(10,10)==QColor('blue')

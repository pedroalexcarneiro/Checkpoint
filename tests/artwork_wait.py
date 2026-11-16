"""Sincronização de capturas com as imagens realmente prontas, sem mudar pixels."""
from PySide6.QtCore import QElapsedTimer
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication


def wait_for_artwork(view):
    clock=QElapsedTimer();clock.start()
    while clock.elapsed()<2000:
        view.viewport().grab()
        QApplication.processEvents()
        if not view.art_cache.pending:
            return
        QTest.qWait(5)
    assert not view.art_cache.pending, 'A arte não terminou de carregar'

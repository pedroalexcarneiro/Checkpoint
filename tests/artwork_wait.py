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


def wait_for_memory_artwork(widget):
    """Aguardar trabalho real assíncrono mantendo as asserções de pixels intactas."""
    from checkpoint.memory_artwork import MemoryArtwork
    previews=widget.findChildren(MemoryArtwork)
    if isinstance(widget,MemoryArtwork):previews.append(widget)
    caches={preview.cache for preview in previews}
    clock=QElapsedTimer();clock.start()
    while clock.elapsed()<2000:
        widget.grab();QApplication.processEvents()
        if not any(cache.pending for cache in caches):
            widget.grab()
            return
        QTest.qWait(5)
    assert not any(cache.pending for cache in caches), 'Miniaturas não terminaram de carregar'

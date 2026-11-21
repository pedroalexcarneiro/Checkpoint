"""Miniaturas compartilhadas e limitadas; QImage no pool, QPixmap só na GUI."""
from PySide6.QtCore import Qt
from .artwork_cache import ArtworkCache
from .design_system import ArtworkButton


def memory_cache(window):
    cache = getattr(window, 'memory_art_cache', None)
    if cache is None:
        cache = ArtworkCache(24*1024*1024, asynchronous=True, parent=window)
        window.memory_art_cache = cache
    return cache


class MemoryArtwork(ArtworkButton):
    def __init__(self, path, caption, callback, cache, height=160, parent=None):
        # Não abrir o arquivo original no construtor de QWidget.
        super().__init__('', caption, callback, height, parent, background=False)
        self.source_path = path
        self.cache = cache
        self.cache.ready.connect(self.update)
        self.setAttribute(Qt.WA_OpaquePaintEvent, False)

    def paintEvent(self, event):
        ratio = self.devicePixelRatioF()
        self.pixmap = self.cache.load(self.source_path,
                                      max(1, round(self.width()*ratio)),
                                      max(1, round(self.height()*ratio)))
        super().paintEvent(event)

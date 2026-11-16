import threading

from PySide6.QtCore import QThread, QTimer
from PySide6.QtGui import QColor, QImage
from PySide6.QtTest import QTest


def wait_until(app, condition):
    for _ in range(200):
        app.processEvents()
        if condition():
            return
        QTest.qWait(5)
    assert condition()


def test_cold_images_decode_outside_gui_and_do_not_block_events(app, folder, monkeypatch):
    from checkpoint import artwork_cache

    original = artwork_cache._read_image
    release = threading.Event()
    entered = threading.Event()
    threads = []

    def slow_decode(*args):
        threads.append(QThread.currentThread())
        entered.set()
        assert release.wait(3)
        return original(*args)

    paths = []
    for name, color in [('Portal 2', 'red'), ('Hades', 'blue')]:
        image = QImage(300, 450, QImage.Format_RGB32)
        image.fill(QColor(color))
        path = folder / (name + '.png')
        assert image.save(str(path))
        paths.append(path)
    monkeypatch.setattr(artwork_cache, '_read_image', slow_decode)
    cache = artwork_cache.ArtworkCache(asynchronous=True)
    ticks = []
    try:
        for path in paths:
            assert cache.load(str(path), 100, 150).isNull()
        QTimer.singleShot(0, lambda: ticks.append(True))
        wait_until(app, lambda: entered.is_set() and bool(ticks))
        assert cache.pending and not cache.entries
        assert all(thread != app.thread() for thread in threads)
    finally:
        release.set()
        wait_until(app, lambda: not cache.pending)
    for path, color in zip(paths, ['red', 'blue']):
        pix = cache.load(str(path), 100, 150)
        assert (pix.width(), pix.height()) == (100, 150)
        assert pix.toImage().pixelColor(50, 75) == QColor(color)


def test_async_cache_bounds_queue_and_preserves_changed_image(app, folder, monkeypatch):
    from checkpoint import artwork_cache

    original = artwork_cache._read_image
    release = threading.Event()

    def slow_decode(*args):
        assert release.wait(3)
        return original(*args)

    monkeypatch.setattr(artwork_cache, '_read_image', slow_decode)
    cache = artwork_cache.ArtworkCache(max_bytes=80_000, asynchronous=True)
    paths = []
    try:
        for n in range(40):
            path = folder / f'{n}.png'
            image = QImage(160, 240, QImage.Format_RGB32)
            image.fill(QColor('red'))
            assert image.save(str(path))
            paths.append(path)
            cache.load(str(path), 100, 150)
        assert 0 < len(cache.pending) <= 24
    finally:
        release.set()
        wait_until(app, lambda: not cache.pending)
    assert cache.used_bytes <= 80_000
    image.fill(QColor('blue'))
    assert image.save(str(paths[-1]))
    cache.load(str(paths[-1]), 100, 150)
    wait_until(app, lambda: not cache.pending)
    result = cache.load(str(paths[-1]), 100, 150)
    assert result.toImage().pixelColor(50, 75) == QColor('blue')
    assert cache.used_bytes <= 80_000


def test_async_transparent_logo_matches_original_raster(app, folder):
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QPixmap,QRegion
    from checkpoint.artwork_cache import ArtworkCache

    for name,left in [('Portal 2', 14), ('Hades', 81)]:
        image=QImage(200,90,QImage.Format_ARGB32);image.fill(Qt.transparent)
        for y in range(13,63):
            for x in range(left,left+70):image.setPixelColor(x,y,QColor('#1cba70'))
        path=folder/(name+'.png');assert image.save(str(path))
        original=QPixmap.fromImage(image);bounds=QRegion(original.mask()).boundingRect()
        expected=original.copy(bounds).scaled(96,48,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        cache=ArtworkCache(asynchronous=True)
        cache.load(str(path),96,48,trim=True)
        wait_until(app,lambda:not cache.pending)
        assert cache.load(str(path),96,48,trim=True).toImage()==expected.toImage()

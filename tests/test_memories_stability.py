"""Carga progressiva, responsividade e reaproveitamento com mídia volumosa."""
import shutil
from threading import Event
from time import monotonic
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QColor
from PySide6.QtTest import QTest
from checkpoint.memory_artwork import MemoryArtwork
from test_bugs_0134 import ui, sample


def test_slow_decode_does_not_block_navigation_or_events(ui, app, folder, monkeypatch):
    window, identity = ui
    from checkpoint import artwork_cache
    path = folder/'original-4k.png'
    image = QImage(3840, 2160, QImage.Format_RGB32)
    image.fill(QColor('#387d9a'))
    assert image.save(str(path))
    for index in range(96):
        destination = folder/f'captura-{index}.png'
        shutil.copyfile(path, destination)
        window.library.add_media(identity, destination)
    entered, release, decode_resumed = Event(), Event(), Event()
    original = artwork_cache._read_image
    def slow(*args):
        entered.set()
        release.wait(5)
        decode_resumed.set()
        return original(*args)
    monkeypatch.setattr(artwork_cache, '_read_image', slow)
    pulses = []
    timer = QTimer()
    timer.setInterval(5)
    timer.timeout.connect(lambda: pulses.append(True))
    timer.start()
    try:
        window.navigate(3)
        page = window.pages[3]
        browser = window.memory_browser
        for _ in range(20):
            app.processEvents()
            if entered.is_set(): break
            QTest.qWait(5)
        assert entered.is_set()
        pulses.clear()
        deadline = monotonic()+1
        while len(pulses) < 3 and monotonic() < deadline:
            QTest.qWait(10)
        assert len(pulses) >= 3
        assert not decode_resumed.is_set()
        assert len(browser.states[0]['grid'].cards) == 24
        assert 0 < len(browser.cache.pending) <= 24
        window.navigate(1)
        window.navigate(3)
        assert window.pages[3] is page
        assert window.memory_browser is browser
    finally:
        release.set()
        timer.stop()
        deadline = monotonic()+5
        while window.memory_art_cache.pending and monotonic() < deadline:
            QTest.qWait(10)
    assert not window.memory_art_cache.pending
    assert window.memory_art_cache.used_bytes <= 24*1024*1024
    for preview in window.pages[3].findChildren(MemoryArtwork):
        if not preview.pixmap.isNull():
            assert preview.pixmap.width() <= 1000
            assert preview.pixmap.height() <= 320


def test_new_memory_updates_only_changed_cards_and_preserves_tab(ui, app):
    window, identity = ui
    window.library.add_diary(identity, 'Primeira nota')
    window.navigate(3)
    app.processEvents()
    browser = window.memory_browser
    tabs = browser.tabs
    tabs.setCurrentIndex(1)
    app.processEvents()
    before = browser.states[1]['grid'].cards[0]
    window.library.add_diary(identity, 'Segunda nota')
    window.memories()
    app.processEvents()
    assert browser.tabs is tabs and tabs.currentIndex() == 1
    assert browser.states[1]['grid'].cards[1] is before
    assert len(browser.states[1]['grid'].cards) == 2
    assert browser.states[2]['grid'] is None


def test_memory_filters_keep_identity_and_more_columns_use_available_width(ui, app):
    window, identity = ui
    other = window.library.save_game({'title': 'Outro jogo', 'platform': 'Nintendo 64'})
    for index in range(60):
        window.library.add_diary(identity if index % 2 else other, f'Nota {index}')
    window.navigate(3)
    browser = window.memory_browser
    counts = []
    for width in (1280, 1920, 1000, 1280):
        window.resize(width, 800)
        for _ in range(6): app.processEvents()
        grid = browser.states[0]['grid']
        counts.append(grid.columns)
        right = max(card.geometry().right() for card in grid.cards)
        assert grid.width()-right <= grid.grid.spacing()+4
        assert all(250 <= card.width() <= 336 for card in grid.cards)
    assert counts[1] > counts[0]
    browser.game_filter.setCurrentIndex(browser.game_filter.findData(other))
    assert all(card.memory_record['game_id'] == other for card in browser.states[0]['grid'].cards)
    assert window.library.setting('memories.game') == other


def test_game_selector_contains_only_games_with_memories_and_refreshes(ui, app, folder):
    window, diary_game = ui
    media_game = window.library.save_game({'title': 'Somente captura', 'platform': 'PC'})
    empty_game = window.library.save_game({'title': 'Sem memórias', 'platform': 'PC'})
    window.library.add_diary(diary_game, 'Diário registrado')
    path = folder/'foto.png'
    image = QImage(120, 80, QImage.Format_RGB32)
    image.fill(QColor('blue'))
    assert image.save(str(path))
    window.library.add_media(media_game, path)
    window.navigate(3)
    selector = window.memory_browser.game_filter
    values = [selector.itemData(index) for index in range(selector.count())]
    assert set(values) == {None, diary_game, media_game}
    assert empty_game not in values
    with window.library.sql:
        window.library.sql.execute('DELETE FROM diary_entries WHERE game_id=?', (diary_game,))
    window.memories()
    assert {selector.itemData(index) for index in range(selector.count())} == {None, media_game}

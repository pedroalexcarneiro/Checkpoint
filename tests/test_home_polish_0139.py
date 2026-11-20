"""Sessões reais e geometria do Início; dados isolados, sem contas."""
from datetime import datetime, timedelta, timezone
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from PySide6.QtTest import QTest
from checkpoint.home_components import GameStrip, RecentGameCard, RecentArtwork, SingleLineInfo
from test_bugs_0134 import ui, sample


def settle(app):
    for _ in range(12):
        app.processEvents()


def sessions(window, identity):
    other = window.library.save_game({'title': 'Hades — edição de teste', 'platform': 'PC'})
    now = datetime.now(timezone.utc)
    records = []
    with window.library.sql:
        for index, game_id in enumerate((identity, other, identity, other, identity)):
            start = now - timedelta(hours=index+1)
            row = window.library.sql.execute(
                "INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?, 'finished',?)",
                (game_id, start.isoformat(), (start+timedelta(minutes=10)).isoformat(), 600, index+40))
            records.append(row.lastrowid)
    return other, records


def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
    from checkpoint.home_data import recent_sessions
    w, identity = ui
    other, records = sessions(w, identity)
    before = [tuple(row) for row in w.library.sql.execute('SELECT * FROM play_sessions')]
    data = recent_sessions(w.library, limit=None)
    assert [r['session_id'] for r in data] == records
    assert [r['id'] for r in data] == [identity, other, identity, other, identity]
    assert [tuple(row) for row in w.library.sql.execute('SELECT * FROM play_sessions')] == before


def test_recent_cards_height_follows_content_and_button_fits(ui, app):
    w, identity = ui
    sessions(w, identity)
    for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
        w.resize(*size)
        w.navigate(0)
        settle(app)
        section = w.pages[0].findChild(QWidget, 'homeRecentSection')
        right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
        if size[0] >= 1280:
            assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
        strip = section.findChild(GameStrip)
        assert strip.tiles
        for tile in strip.tiles:
            play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
            assert play.width() >= play.sizeHint().width()
            labels = tile.findChildren(SingleLineInfo)
            gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
            assert all(0 <= gap <= 13 for gap in gaps)
            assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
        assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))


def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
    w, identity = ui
    sessions(w, identity)
    # Início passou a exibir jogos únicos por pedido posterior do dono.
    # Cinco jogos distintos mantêm a cobertura das setas sem repetir cards.
    with w.library.sql:
        for n in range(3):
            game=w.library.save_game({'title':f'Outro jogo de teste {n}','platform':'PC'})
            w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'finished',?)",
                (game,(datetime.now(timezone.utc)-timedelta(days=n+1)).isoformat(),200+n))
    w.resize(1280, 800)
    w.navigate(0)
    settle(app)
    strip = w.pages[0].findChild(GameStrip)
    before = [tile.session_id for tile in strip.tiles]
    assert strip.next.isEnabled() and not strip.previous.isEnabled()
    QTest.mouseClick(strip.next, Qt.LeftButton)
    settle(app)
    assert [tile.session_id for tile in strip.tiles] != before
    strip.setFocus()
    QTest.keyClick(strip, Qt.Key_Left)
    assert strip.offset == 0
    for _ in range(10):
        strip.next.click()
    assert not strip.next.isEnabled()
    assert strip.previous.name == 'chevron-left' and strip.next.name == 'chevron-right'
    assert strip.previous.size() == strip.next.size()


def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
    from PySide6.QtGui import QImage, QColor
    w, identity = ui
    path = folder / 'cover.png'
    image = QImage(200, 300, QImage.Format_RGB32)
    image.fill(QColor('#f0a030'))
    assert image.save(str(path))
    art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
    art.resize(200, 300)
    art.show()
    settle(app)
    try:
        pixels = art.grab().toImage()
        assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
        target = art.image_target()
        assert art.rect().contains(target.toAlignedRect())
        assert abs(target.width()/target.height() - 2/3) < .01
        assert pixels.pixelColor(100, 2).red() > 200
        assert pixels.pixelColor(2, 150).red() > 200
    finally:
        art.close()


def test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text(ui, app, folder):
    from PySide6.QtGui import QImage, QColor
    from checkpoint.home_components import HomeOfferRow, OfferThumbnail
    from checkpoint.ui_components import ElidedAction
    w, identity = ui
    path = folder / 'offer-cover.png'
    image = QImage(200, 300, QImage.Format_RGB32)
    image.fill(QColor('#f0a030'))
    assert image.save(str(path))
    game = {**w.library.get(identity), 'cover': str(path), 'quote': {'current_kind': 'retail', 'lowest': 3000}}
    row = HomeOfferRow(w, game)
    row.resize(400, row.sizeHint().height())
    row.show()
    settle(app)
    try:
        thumbnail = row.findChild(OfferThumbnail)
        title = row.findChild(ElidedAction)
        assert thumbnail.geometry().right() + 10 <= title.x()
        target = thumbnail.image_target()
        assert abs(target.width()/target.height()-2/3) < .01
        pixels = thumbnail.grab().toImage()
        for x, y in ((target.left(), target.top()), (target.right()-1, target.top()), (target.left(), target.bottom()-1), (target.right()-1, target.bottom()-1)):
            assert pixels.pixelColor(round(x), round(y)).name() != '#f0a030'
        for x, y in ((target.center().x(), target.top()+2), (target.center().x(), target.bottom()-3), (target.left()+2, target.center().y()), (target.right()-3, target.center().y())):
            assert pixels.pixelColor(round(x), round(y)).name() == '#f0a030'
    finally:
        row.close()


def test_restricted_cover_has_no_dark_letterbox(ui, app, folder):
    from PySide6.QtGui import QImage, QColor
    from checkpoint.design_system import CardSurface
    from checkpoint.home_components import RecentGameCard
    w, identity = ui
    path = folder / 'letterbox-cover.png'
    image = QImage(200, 300, QImage.Format_RGB32)
    image.fill(QColor('#f0a030'))
    assert image.save(str(path))
    game = {**w.library.get(identity), 'cover': str(path), 'last_played': datetime.now(timezone.utc).isoformat(), 'seconds': 0}
    tile = RecentGameCard(w, game)
    tile.resize(240, tile.sizeHint().height())
    tile.show()
    settle(app)
    try:
        art = tile.findChild(RecentArtwork)
        target = art.image_target()
        assert target.width() < art.width()
        pixels = tile.grab().toImage()
        from PySide6.QtCore import QPoint
        at = art.mapTo(tile, QPoint(1, art.height()//2))
        beside = QPoint(at.x()-3, at.y())
        a, b = pixels.pixelColor(at), pixels.pixelColor(beside)
        assert max(abs(x-y) for x,y in zip(a.getRgb()[:3], b.getRgb()[:3])) <= 2
    finally:
        tile.close()


def test_resizing_preserves_visible_session_focus_and_card(ui,app):
    w,identity=ui
    sessions(w,identity);w.resize(1280,800);w.navigate(0);settle(app)
    strip=w.pages[0].findChild(GameStrip)
    first=strip.tiles[0]
    play=next(b for b in first.findChildren(QPushButton) if b.property('homeContinue'))
    play.setFocus(Qt.TabFocusReason)
    for size in ((1920,1080),(1280,800)):
        w.resize(*size);settle(app)
        assert strip.tiles[0] is first and first.isVisibleTo(w)
        assert app.focusWidget() is play
        art=first.findChild(RecentArtwork)
        assert play.y()>art.geometry().bottom()

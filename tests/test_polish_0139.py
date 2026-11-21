"""Regressões geométricas e dados preservados da rodada 0.1.39."""
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QLabel, QWidget, QPushButton
from PySide6.QtTest import QTest
from PySide6.QtGui import QIcon
from test_bugs_0134 import ui, sample


def settle(app):
    for _ in range(10):
        app.processEvents()


def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
    from checkpoint.collection_views import WishGrid, WishLogo
    w, identity = ui
    other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
    extra = [w.library.save_game({'title': title, 'platform': 'PlayStation 5'}) for title in ('Hades', 'Hollow Knight')]
    with w.library.sql:
        for game_id in (identity, other, *extra):
            w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
    columns = []
    for size in ((1000, 700), (1280, 800), (1920, 1080)):
        w.resize(*size)
        w.navigate(2)
        settle(app)
        grid = w.pages[2].findChild(WishGrid)
        columns.append(grid.columns)
        for card in grid.cards:
            assert card.width() <= 238
            art = card.findChild(WishLogo)
            assert art.width() == art.height()
            assert card.rect().contains(art.geometry())
            viewport=w.wishlist_scroll.viewport()
            assert viewport.width()-1-card.mapTo(viewport,card.rect().topRight()).x()>=12
        assert w.wishlist_scroll.widget().width()<=w.wishlist_scroll.viewport().width()
    assert columns[0]==3 and columns[2] > columns[1]
    from checkpoint.collection_views import WishFilterCombo
    for name in ('wishlistPlatform','wishlistOrder'):
        combo=w.pages[2].findChild(WishFilterCombo,name)
        QTest.mouseClick(combo,Qt.LeftButton,pos=QPoint(combo.width()-12,combo.height()//2))
        assert combo.view().isVisible()
        combo.hidePopup()


def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
    from checkpoint.collection_views import build_memories
    from checkpoint.design_system import CardGrid
    w, identity = ui
    other = w.library.save_game({'title': 'Hades'})
    notes = ('Texto curto que deve permanecer íntegro.', 'Texto próprio de outra extensão para conferir o alinhamento superior dos cards de Diário na mesma linha da grade.')
    for game_id, note in zip((identity, other), notes):
        w.library.add_diary(game_id, note)
    before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
    w.navigate(3)
    settle(app)
    tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
    tabs.setCurrentIndex(1)
    settle(app)
    grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
    assert all(card.height() < 240 for card in grid.cards)
    assert len({card.y() for card in grid.cards}) == 1
    for card in grid.cards:
        label = card.findChild(QLabel, 'bodyText')
        assert label.alignment() & Qt.AlignLeft
        assert label.text() in notes
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')] == before


def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
    from checkpoint.settings_previews import CoverSizeChoices
    w, _ = ui
    w.navigate(5)
    choices = w.pages[5].findChild(CoverSizeChoices)
    choices.show()
    settle(app)
    choice = choices.group.button(70)
    QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
    assert choice.isChecked()
    assert not choice.keyboard_focus
    choices.group.button(90).setFocus(Qt.TabFocusReason)
    settle(app)
    assert choices.group.button(90).keyboard_focus
    QTest.keyClick(choices.group.button(90), Qt.Key_Right)
    assert choices.group.button(100).isChecked()


def test_black_is_neutral_and_other_themes_preserved():
    from checkpoint.theme import THEMES
    from PySide6.QtGui import QColor, QIcon
    black = THEMES['black'].colors
    for key in ('background', 'sidebar', 'surface', 'elevated', 'card', 'panel', 'input', 'button', 'border', 'border_subtle'):
        c = QColor(black[key])
        assert c.red() == c.green() == c.blue(), (key, black[key])
    # Pedido posterior: superfícies acompanham a cor, sem fundo azul fixo.
    assert THEMES['green'].colors['background'] != THEMES['purple'].colors['background']
    assert len(THEMES) == 9


def test_add_wish_icon_matches_primary_foreground(ui, app):
    from checkpoint.ui_components import action
    from checkpoint.theme import get_theme
    from PySide6.QtGui import QColor
    w, _ = ui
    button = action('+ Adicionar desejo', lambda: None, True)
    button.show()
    settle(app)
    try:
        for enabled, mode, foreground in ((True, QIcon.Normal, 'on_accent'), (False, QIcon.Disabled, 'disabled')):
            button.setEnabled(enabled)
            pix = button.icon().pixmap(20, 20, mode).toImage()
            expected = QColor(w.theme.colors[foreground])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
            assert opaque and all(max(abs(a-b) for a,b in zip(c.getRgb()[:3], expected.getRgb()[:3])) <= 1 for c in opaque)
    finally:
        button.close()


def test_library_scrollbar_has_stable_gutter(ui, app):
    w, identity = ui
    for n in range(30):
        w.library.save_game({'title': f'Outro jogo {n}'})
    w.navigate(1)
    w.view.setCurrentIndex(1)
    settle(app)
    view = w.game_list
    bar = view.verticalScrollBar()
    assert bar.maximum() > 0
    rect = view.visualItemRect(view.item(0))
    right = view.viewport().mapTo(view, rect.topRight()).x()
    assert 12 <= bar.mapTo(view, QPoint()).x() - right <= 24
    assert view.horizontalScrollBar().maximum() == 0


def test_saves_empty_has_one_compact_configuration_action(ui, app):
    w, identity = ui
    w.detail(identity)
    w.detail_tabs.setCurrentIndex(3)
    settle(app)
    tab = w.detail_tabs.currentWidget()
    buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
    assert len(buttons) == 1
    empty = tab.findChild(QWidget, 'traditionalSaves')
    assert empty and empty.height() < 170


def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
    w, identity = ui
    other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
    w.library.delete(identity)
    w.library.delete(other)
    before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
    w.navigate(5)
    settle(app)
    titles = [w.settings_tabs.tabText(i) for i in range(w.settings_tabs.count())]
    assert 'Emuladores' in titles and 'Lixeira' in titles
    w.settings_tabs.setCurrentIndex(titles.index('Lixeira'))
    tab = w.settings_tabs.currentWidget()
    restore = [b for b in tab.findChildren(QPushButton) if b.text() == 'Restaurar']
    assert len(restore) == 2
    assert any('Switch' in label.text() for label in tab.findChildren(QLabel))
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')] == before


def test_mixed_diary_preview_matches_capture_area(ui, app, folder):
    from checkpoint.collection_views import memory_card
    from checkpoint.design_system import ArtworkButton
    from PySide6.QtWidgets import QTextEdit
    from PySide6.QtGui import QImage
    w, identity = ui
    path = folder/'capture.png'
    picture = QImage(400, 240, QImage.Format_RGB32);picture.fill(0)
    assert picture.save(str(path))
    common = {'id': 1, 'game_id': identity, 'title': w.library.get(identity)['title'],
        'created_at': '2026-11-16T12:00:00+00:00', 'text': 'Minha nota curta.',
        'path': str(path), 'caption': ''}
    diary = memory_card(w, {**common, 'kind': 'diary'})
    media = memory_card(w, {**common, 'kind': 'image'})
    for widget in (diary, media):
        widget.resize(320, 320);widget.show()
    settle(app)
    try:
        note = diary.findChild(QTextEdit, 'memoryTextArea')
        art = media.findChild(ArtworkButton)
        assert note is not None and art is not None
        assert note.y() == art.y() and note.size() == art.size()
        assert note.toPlainText() == common['text'] and note.isReadOnly()
    finally:
        for widget in (diary, media):widget.close()

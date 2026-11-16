from PySide6.QtWidgets import QComboBox,QLabel
from checkpoint.collection_views import WishCard
from test_bugs_0134 import ui,sample


def test_wish_platform_dropdown_filters_families_without_changing_games(ui,app):
    w,_=ui;ids={}
    for platform in ('PC','Nintendo Switch','PlayStation 5','PlayStation 2','Xbox Series X/S','Game Boy Advance'):
        i=w.library.save_game({'title':'Desejo '+platform,'platform':platform});ids[platform]=i
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
    before=[tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
    w.navigate(2);app.processEvents()
    for key,expected in [('pc',{'PC'}),('switch',{'Nintendo Switch'}),('playstation',{'PlayStation 5','PlayStation 2'}),('xbox',{'Xbox Series X/S'})]:
        combo=w.pages[2].findChild(QComboBox,'wishlistPlatform');assert combo is not None
        combo.setCurrentIndex(combo.findData(key));app.processEvents()
        cards=w.pages[2].findChildren(WishCard)
        assert {c.game['platform'] for c in cards}==expected
        order=w.pages[2].findChild(QComboBox,'wishlistOrder')
        assert order.itemText(order.findData('name'))=='Alfabeticamente'
        assert w.library.setting('wishlist.platform_filter')==key
    w.navigate(1);w.navigate(2);app.processEvents()
    assert w.pages[2].findChild(QComboBox,'wishlistPlatform').currentData()=='xbox'
    combo=w.pages[2].findChild(QComboBox,'wishlistPlatform');combo.setCurrentIndex(combo.findData('all'));app.processEvents()
    assert len(w.pages[2].findChildren(WishCard))==6
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]==before


def test_empty_platform_filter_keeps_controls_and_clear_action(ui,app):
    w,i=ui
    with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
    w.navigate(2);app.processEvents();combo=w.pages[2].findChild(QComboBox,'wishlistPlatform')
    assert combo is not None
    combo.setCurrentIndex(combo.findData('switch'));app.processEvents()
    assert not w.pages[2].findChildren(WishCard)
    assert w.pages[2].findChild(QComboBox,'wishlistOrder') is not None
    assert any(l.text()=='Nenhum desejo nesta plataforma' for l in w.pages[2].findChildren(QLabel))

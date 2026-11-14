from PySide6.QtWidgets import QLabel
from test_bugs_0134 import ui,sample

def test_app_and_steam_times_are_separate(ui,app):
    w,i=ui
    with w.library.sql:
        w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,duration_seconds) VALUES(?,'2026-11-10','finished',3600)",(i,))
        w.library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES('76561198000000001',?,?,?,180,'2026-11-10')",(str(i),i,w.library.get(i)['title']))
    w.detail(i);app.processEvents()
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 1 h'
    assert w.detail_page.findChild(QLabel,'steamPlaytime').text()=='Steam: 3 h'
    assert not any('4 h' in label.text() for label in w.detail_page.findChildren(QLabel))

def test_wish_card_keeps_price_and_explains_no_price(ui,app):
    from checkpoint.prices import refresh_prices
    from checkpoint.collection_views import WishCard
    w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
    with w.library.sql:
        w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
        w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
    class Provider:
        value=2190
        def prices(self,*args,**kwargs):return {'current':self.value,'currency':'BRL'}
    provider=Provider();refresh_prices(w.library,i,provider);provider.value=None;refresh_prices(w.library,i,provider)
    w.wishlist();app.processEvents();card=w.pages[2].findChild(WishCard)
    assert any(label.text()=='R$ 21,90' for label in card.findChildren(QLabel))
    assert any(label.text()=='Último preço salvo' for label in card.findChildren(QLabel))
    w.library.set_setting(f'prices.ggdeals.{i}',{});w.wishlist();app.processEvents()
    card=w.pages[2].findChild(WishCard)
    assert any(label.text()=='Preços ainda não consultados.' for label in card.findChildren(QLabel))

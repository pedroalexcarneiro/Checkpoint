from PySide6.QtWidgets import QLabel,QComboBox
from checkpoint.price_view import price_summary
from checkpoint.window import MainWindow
from checkpoint.prices import wishlist_order,money
from checkpoint.price_queue import PriceQueue


def test_official_history_is_never_struck_out_or_used_as_discount(library,app):
    identity=library.save_game({'title':'Example'})
    library.set_setting(f'prices.ggdeals.{identity}',{'provider':'api','lowest':5990,'historical':1990,'current_kind':'retail','original':9990,'discount':40,'currency':'BRL'})
    frame=price_summary(library,library.get(identity));labels=frame.findChildren(QLabel)
    assert any(label.text()=='Menor histórico: R$ 19,90' for label in labels)
    assert any(label.text()=='Loja oficial' for label in labels)
    assert any(label.text()=='Sem ID da Steam para consulta' for label in labels)
    assert not any(label.font().strikeOut() or '%' in label.text() for label in labels)
    assert money(0)=='Indisponível' and money(None)=='Indisponível'


def test_price_order_places_missing_prices_last_and_respects_name(library):
    ids=[library.save_game({'title':title}) for title in ('Zulu','Beta','Alfa','Sem preço')]
    for identity,current in zip(ids,(5000,2000,2000,None)):
        library.set_setting(f'prices.ggdeals.{identity}',{'lowest':current})
    assert [game['title'] for game in wishlist_order(library,library.games())]==['Alfa','Beta','Sem preço','Zulu']
    assert [game['title'] for game in wishlist_order(library,library.games(),'price')]==['Alfa','Beta','Zulu','Sem preço']


def test_wishlist_and_detail_have_active_attribution_and_no_steam_queue(library,app):
    library.set_setting('prices.auto',False);library.set_setting('artwork.auto',False)
    identity=library.save_game({'title':'ROM'})
    with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
    library.set_setting('wishlist.order','discount')
    window=MainWindow(library);window.navigate(2)
    label=window.pages[2].findChild(QLabel,'ggdealsAttribution')
    assert label.openExternalLinks() and 'https://gg.deals/' in label.text() and 'Preços: GG.deals' in label.text()
    assert window.pages[2].findChild(QComboBox,'wishlistOrder').currentData()=='name'
    assert library.setting('wishlist.order')=='name'
    window.detail(identity)
    label=window.detail_page.findChild(QLabel,'ggdealsAttribution')
    assert label.openExternalLinks() and 'https://gg.deals/' in label.text()
    queue=PriceQueue(library,window);queue.submit([identity]);assert not queue.pending and queue.active is None
    window.close()


def test_foreign_currency_cache_never_renders_as_reais(library,app):
    from types import SimpleNamespace
    from checkpoint.price_view import comparison
    identity=library.save_game({'title':'Example'})
    library.set_setting(f'prices.ggdeals.{identity}',{'provider':'api','currency':'USD','lowest':6000,'retail':6000,'keyshop':5000,'historical':1900})
    game=library.get(identity)
    summary=price_summary(library,game);detail=comparison(SimpleNamespace(library=library),game)
    labels=summary.findChildren(QLabel)+detail.findChildren(QLabel)
    assert not any('R$' in label.text() for label in labels)

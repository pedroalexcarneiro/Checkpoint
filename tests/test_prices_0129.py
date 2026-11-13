from unittest.mock import Mock
import pytest
from PySide6.QtWidgets import QLabel,QComboBox
from checkpoint.integrations import IntegrationError
from checkpoint.integrations.ggdeals import parse_prices
from checkpoint.integrations.price_provider import GgDealsApiProvider
from checkpoint.prices import wishlist_order
from checkpoint.window import MainWindow
from checkpoint.collection_views import WishGrid,WishLogo
from checkpoint.price_view import price_summary

HTML='''<link rel="canonical" href="https://gg.deals/br/game/example/">
<script type="application/ld+json">{"offers":{"priceCurrency":"BRL"}}</script>
<section id="official-stores"><div class="game-list-item" data-shop-name="Loja">
<a class="shop-link" href="/br/redirect/example/">Loja</a>
<span class="price price-old">R$ 100,00</span><span class="price">R$ 60,00</span>
</div></section>'''

def test_original_price_and_discount_come_from_same_offer():
    quote=parse_prices(HTML)
    assert (quote['current'],quote['original'],quote['discount'],quote['currency'])==(6000,10000,40,'BRL')
    assert quote['stores']==quote['offers']
    quote=parse_prices(HTML.replace('<span class="price price-old">R$ 100,00</span>',''))
    assert quote['original'] is None and quote['discount'] is None
    with pytest.raises(IntegrationError):parse_prices(HTML.replace('R$ 60,00','R$ 0,00'))

def test_official_api_without_saved_key_never_calls_transport():
    fetch=Mock();provider=GgDealsApiProvider(fetch=fetch);assert not provider.enabled
    with pytest.raises(IntegrationError,match='não configurada'):provider.prices('42')
    fetch.assert_not_called()

def test_wishlist_name_price_sort_and_scroll_survive_refresh(library,app):
    library.set_setting('prices.auto',False);library.set_setting('artwork.auto',False)
    ids=[]
    for index in range(30):
        identity=library.save_game({'title':f'Jogo {index:02}'})
        with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
        ids.append(identity)
    library.set_setting(f'prices.ggdeals.{ids[-1]}',{'lowest':6000,'current':6000,'original':10000,'discount':40,'currency':'BRL'})
    ordered=wishlist_order(library,library.games())
    assert ordered[0]['id']==ids[0]
    assert wishlist_order(library,library.games(),'price')[0]['id']==ids[-1]
    assert wishlist_order(library,library.games(),'name')[0]['id']==ids[0]
    window=MainWindow(library);window.resize(1280,800);window.navigate(2);window.show()
    for _ in range(5):app.processEvents()
    combo=window.pages[2].findChild(QComboBox,'wishlistOrder');assert combo.currentData()=='name';combo.setCurrentIndex(1)
    for _ in range(5):app.processEvents()
    grid=window.pages[2].findChild(WishGrid,'wishlistGrid')
    assert grid.cards[0].game['id']==ids[-1]
    assert all(card.findChild(WishLogo).width()==card.findChild(WishLogo).height() for card in grid.cards)
    price=price_summary(library,library.get(ids[-1]));labels=price.findChildren(QLabel)
    assert any(label.text()=='-40%' for label in labels)
    assert any(label.text()=='R$ 100,00' and label.font().strikeOut() for label in labels)
    window.wishlist_scroll.verticalScrollBar().setValue(250)
    library.set_setting(f'prices.ggdeals.{ids[-2]}',{'lowest':2000,'discount':80,'original':10000})
    window.prices_updated(ids[-2])
    for _ in range(5):app.processEvents()
    assert window.wishlist_scroll.verticalScrollBar().value()==250
    assert window.pages[2].findChild(WishGrid,'wishlistGrid').cards[0].game['id']==ids[-2]
    combo=window.pages[2].findChild(QComboBox,'wishlistOrder');combo.setCurrentIndex(0)
    for _ in range(5):app.processEvents()
    assert window.pages[2].findChild(WishGrid,'wishlistGrid').cards[0].game['id']==ids[0]
    window.close()

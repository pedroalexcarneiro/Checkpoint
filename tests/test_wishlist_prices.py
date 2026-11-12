from unittest.mock import Mock
from pathlib import Path
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QComboBox
from gamevault.integrations import IntegrationError,MetadataResult
from gamevault.integrations.ggdeals import parse_prices,GgDealsProvider
from gamevault.prices import refresh_prices,snapshot,needs_update
from gamevault.game_import import save_import
from gamevault.window import MainWindow
from gamevault.ui_components import GameTile


HTML='''<html><link rel="canonical" href="https://gg.deals/br/game/example/">
<script type="application/ld+json">{"name":"Example","offers":{"priceCurrency":"BRL"}}</script>
<section id="official-stores"><div class="game-list-item" data-shop-name="Loja A" data-deal-value="8.00">
<a class="shop-link" href="/br/redirect/offer-a/?affiliate=original">Loja</a><span class="price">R$ 49,99</span></div></section>
<section id="keyshops"><div class="game-list-item" data-shop-name="Loja B"><a class="shop-link" href="/br/redirect/offer-b/">Loja</a><span class="price">R$ 30,50</span></div></section></html>'''


def test_prices_use_visible_brl_not_internal_dollar_values_and_keep_links():
    result=parse_prices(HTML)
    assert result['lowest']==3050 and result['retail']==4999 and result['keyshop']==3050
    assert result['offers'][1]['url']=='https://gg.deals/br/redirect/offer-a/?affiliate=original'
    assert result['offers'][0]['shop']=='Loja B'
    with pytest.raises(IntegrationError):parse_prices(HTML.replace('BRL','USD'))
    with pytest.raises(IntegrationError):parse_prices('<html>Challenge</html>')
    with pytest.raises(IntegrationError):GgDealsProvider(lambda url:HTML).prices(url='https://example.com/game/example/')


def test_prices_cache_failure_keeps_last_good_price(library):
    identity=save_import(library,{'title':'Example'},result=MetadataResult('steam','42','Example'))
    provider=GgDealsProvider(lambda url:HTML);refresh_prices(library,identity,provider)
    assert snapshot(library,identity)['lowest']==3050 and not needs_update(library,identity)
    broken=Mock();broken.prices.side_effect=IntegrationError('Offline');refresh_prices(library,identity,broken)
    result=snapshot(library,identity)
    assert result['state']=='unavailable' and result['lowest']==3050 and result['checked_at']


def test_wishlist_has_no_owned_status_and_is_excluded_from_owned_statistics(library,app):
    identity=library.save_game({'title':'Wish fixture','status':'Concluído','notes':'Keep notes'})
    window=MainWindow(library);window.add_wish(identity);window.navigate(2);window.show();app.processEvents()
    from gamevault.collection_views import SquareWishCard,WishLogo
    tile=window.pages[2].findChild(SquareWishCard)
    assert tile.accessibleDescription()=='Na lista de desejos' and tile.width()==tile.height()
    assert tile.findChild(WishLogo) is not None and tile.findChild(GameTile) is None
    assert library.stats()['total']==0 and library.stats()['statuses']['Concluído']==0
    window.detail(identity);app.processEvents()
    labels=[label.text() for label in window.detail_page.findChildren(QLabel)]
    assert '● Concluído' not in labels and 'Na lista de desejos' in labels
    window.remove_wish(identity)
    assert not library.is_owned(identity) and library.get(identity)['notes']=='Keep notes'
    window.acquire_wish(identity)
    assert library.is_owned(identity) and library.stats()['total']==1
    assert library.get(identity)['notes']=='Keep notes';window.close()


def test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips(library,app):
    from datetime import datetime,timezone,timedelta
    from gamevault.activity_heatmap import ActivityHeatmap
    identity=library.save_game({'title':'Daily fixture'})
    start=(datetime.now(timezone.utc)-timedelta(days=2)).replace(hour=23,minute=30,second=0,microsecond=0)
    with library.sql:library.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state) VALUES(?,?,?,?, 'finished')",(identity,start.isoformat(),(start+timedelta(hours=1)).isoformat(),3600))
    daily=library.stats()['daily'];assert sorted(daily.values())==[1800,1800]
    window=MainWindow(library);window.navigate(4);window.show();app.processEvents();chart=window.findChild(ActivityHeatmap)
    assert chart is not None and chart.values==daily and len(chart.cells)==365
    assert sum(seconds for rect,day,seconds in chart.cells)==3600
    assert chart.accessibleName()=='Horas de jogo por dia';window.close()




def test_wishlist_logos_titles_and_prices_share_fixed_alignment(library,app,folder):
    from PySide6.QtGui import QImage,QColor
    from gamevault.collection_views import SquareWishCard,WishLogo,WishTitle
    for index in range(4):
        logo=''
        if index<3:
            path=folder/f'logo-{index}.png';image=QImage(100+index*200,80,QImage.Format_RGB32);image.fill(QColor('blue'));image.save(str(path));logo=str(path)
        identity=library.save_game({'title':'A long title '*8 if index==3 else f'Game {index}','logo':logo})
        with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
    window=MainWindow(library);window.navigate(2);window.show()
    for _ in range(3):app.processEvents()
    cards=window.pages[2].findChildren(SquareWishCard);assert len(cards)==4
    assert all(card.width()==card.height() for card in cards)
    assert len({card.findChild(WishLogo).geometry().height() for card in cards})==1
    assert len({card.findChild(WishTitle).height() for card in cards})==1
    assert all(not title.wordWrap() and title.alignment()==Qt.AlignCenter for card in cards for title in card.findChildren(WishTitle))
    window.set_theme('blue');window.resize(1000,700)
    for _ in range(4):app.processEvents()
    assert all(not a.geometry().intersects(b.geometry()) for index,a in enumerate(cards) for b in cards[index+1:])
    assert all(card.width()==card.height() for card in cards)
    window.close()


def test_artwork_cache_rejects_gif(library,folder):
    import base64
    from gamevault.integrations.images import ImageCache
    gif=base64.b64decode('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7')
    with pytest.raises(IntegrationError,match='estática'):ImageCache(folder/'cache').store(gif)

from copy import deepcopy
import pytest
from checkpoint.prices import refresh_prices, selected_quote, snapshot
from checkpoint.integrations import IntegrationError
from PySide6.QtWidgets import QCheckBox,QLabel
from test_bugs_0134 import ui, sample


def configured(library,monkeypatch,title):
    identity=library.save_game({'title':title,'platform':'PC'})
    with library.sql:library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
    api={'provider':'api','url':'https://gg.deals/game/edition-one/','currency':'BRL',
        'current':3000,'lowest':3000,'retail':6000,'keyshop':3000,'historical':1000,
        'historical_retail':2000,'current_kind':'keyshop','original':None,'discount':None,'offers':[]}
    public={'url':'https://gg.deals/br/game/edition-one/','currency':'BRL','retail':6000,'keyshop':3000,
        'offers':[{'kind':'retail','cents':6000,'original':10000,'shop':'Loja oficial de teste','url':'https://gg.deals/br/redirect/official/','game_slug':'edition-one'},
                  {'kind':'keyshop','cents':3000,'original':10000,'shop':'Keys de teste','url':'https://gg.deals/br/redirect/keys/','game_slug':'edition-one'}]}
    calls=[];errors={}
    class Api:
        enabled=True
        def __init__(self,*args):pass
        def prices(self,identity,url=None):
            if errors.get('api'):raise IntegrationError('API indisponível')
            callback=errors.pop('after_api',None)
            if callback:callback()
            return deepcopy(api)
    class Public:
        def prices(self,identity,url=None):
            calls.append((identity,url))
            if errors.get('public'):raise IntegrationError('Erro de transporte que não deve ser salvo')
            return deepcopy(public)
    monkeypatch.setattr('checkpoint.integrations.price_provider.GgDealsApiProvider',Api)
    monkeypatch.setattr('checkpoint.integrations.ggdeals.GgDealsProvider',Public)
    monkeypatch.setattr('checkpoint.credentials.CredentialVault',lambda:object())
    library.set_setting('prices.offer_details',True)
    return identity,api,public,calls,errors


@pytest.mark.parametrize('title',['Portal 2','Hades'])
def test_optional_details_confirm_same_offer_without_changing_api_history(library,monkeypatch,title):
    identity,api,public,calls,errors=configured(library,monkeypatch,title)
    refresh_prices(library,identity)
    value=selected_quote(library,identity)
    assert value['lowest']==6000 and value['discount']==40 and value['original']==10000
    assert value['current_kind']=='retail' and value['historical']==1000
    assert value['selected_offer']['shop']=='Loja oficial de teste'
    assert len(calls)==1 and calls[0][0]==str(identity)
    library.set_setting('prices.include_keyshops',True)
    assert selected_quote(library,identity)['discount']==70
    assert selected_quote(library,identity)['lowest']==3000


@pytest.mark.parametrize('case',['edition','row_edition','currency','price','original','store','link','unavailable'])
def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
    identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
    if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
    elif case=='row_edition':public['offers'][0]['game_slug']='edition-one-ultimate'
    elif case=='currency':public['currency']='USD'
    elif case=='price':public['retail']=5900
    elif case=='original':public['offers'][0]['original']=6000
    elif case=='store':public['offers'][0]['kind']='keyshop'
    elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
    else:errors['public']=True
    refresh_prices(library,identity)
    value=selected_quote(library,identity)
    assert len(calls)==1
    assert value['lowest']==6000 and value['historical']==1000
    assert value['discount'] is None and value['original'] is None
    assert 'Erro de transporte' not in str(snapshot(library,identity))


def test_disabled_details_make_no_extra_request_and_api_failure_preserves_cache(library,monkeypatch):
    identity,api,public,calls,errors=configured(library,monkeypatch,'Hades')
    library.set_setting('prices.offer_details',False)
    refresh_prices(library,identity)
    assert calls==[] and selected_quote(library,identity)['discount'] is None
    library.set_setting('prices.offer_details',True);errors['api']=True
    refresh_prices(library,identity)
    assert calls==[] and selected_quote(library,identity)['lowest']==6000


def test_details_option_is_explicit_and_rechecks_without_discarding_cache(ui,app):
    window,identity=ui;window.navigate(5)
    control=window.pages[5].findChild(QCheckBox,'ggdealsOfferDetails')
    assert control is not None and not control.isChecked()
    key=f'prices.ggdeals.{identity}';cache={'retail':6000,'currency':'BRL','historical':2000}
    window.library.set_setting(key,cache)
    previous=window.library.setting('prices.config_version',0)
    control.setChecked(True)
    assert window.library.setting('prices.offer_details') is True
    assert window.library.setting('prices.config_version')>previous
    assert snapshot(window.library,identity)==cache
    window.settings()
    assert window.pages[5].findChild(QCheckBox,'ggdealsOfferDetails').isChecked()


def test_wish_detail_displays_confirmed_percentage_and_explains_missing_data(ui,app,monkeypatch):
    window,_=ui
    identity,api,public,calls,errors=configured(window.library,monkeypatch,'Portal 2')
    with window.library.sql:window.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
    refresh_prices(window.library,identity);window.detail(identity);app.processEvents()
    assert any(label.text()=='-40%' for label in window.detail_page.findChildren(QLabel,'priceDiscount'))
    errors['public']=True;refresh_prices(window.library,identity);window.detail(identity);app.processEvents()
    unknown=[label for label in window.detail_page.findChildren(QLabel) if label.text()=='Desconto: -']
    assert len(unknown)==1 and 'API preservado' in unknown[0].toolTip()
    assert selected_quote(window.library,identity)['lowest']==6000


def test_wishlist_opt_in_queues_refresh_and_displays_same_offer_discount(ui,monkeypatch):
    window,_=ui
    library=window.library
    identity,api,public,_,_=configured(library,monkeypatch,'God of War Ragnarök')
    api['retail']=public['retail']=14_230
    public['offers'][0].update(cents=14_230,original=24_990)
    library.set_setting('prices.offer_details',False)
    with library.sql:library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
    refresh_prices(library,identity)
    monkeypatch.setattr(window.price_queue,'submit',lambda ids:[refresh_prices(library,game_id) for game_id in ids])
    window.navigate(2)
    assert not window.pages[2].findChildren(QLabel,'priceDiscount')
    window.pages[2].findChild(QCheckBox,'wishlistOfferDetails').setChecked(True)
    window.wishlist()
    assert any(label.text()=='-43%' for label in window.pages[2].findChildren(QLabel,'priceDiscount'))
    assert selected_quote(library,identity)['historical']==1000


@pytest.mark.parametrize('slug',['portal-2','hades'])
def test_public_parser_reads_base_price_and_excludes_foreign_products(slug):
    from checkpoint.integrations.ggdeals import parse_prices
    html=f'''<link rel="canonical" href="https://gg.deals/game/{slug}/">
    <script type="application/ld+json">{{"offers":{{"priceCurrency":"BRL","lowPrice":"10.00"}}}}</script>
    <a class="game-header-price" href="#official-stores">R$ 10,00</a>
    <section id="official-stores">
      <div class="game-list-item" data-shop-name="Outra plataforma" data-game-name="{slug}-xbox">
        <span class="base-price">R$ 100,00</span><span class="price">R$ 10,00</span>
        <a class="shop-link" href="/br/redirect/other/">Loja</a></div>
      <div class="game-list-item" data-shop-name="Outra edição" data-game-name="{slug}-ultimate">
        <span class="price">R$ 40,00</span><a class="shop-link" href="/br/redirect/ultimate/">Loja</a></div>
      <div class="game-list-item" data-shop-name="Loja oficial" data-game-name="{slug}">
        <span class="base-price">R$ 100,00</span><span class="price">R$ 60,00</span>
        <a class="shop-link" href="/br/redirect/correct/">Loja</a></div>
    </section>'''
    value=parse_prices(html)
    assert value['retail']==6000 and value['lowest']==6000
    assert len(value['offers'])==1 and value['offers'][0]['original']==10000
    assert value['offers'][0]['game_slug']==slug and value['discount']==40
    assert value['excluded_minima']['retail']==1000


def test_api_price_matching_only_another_product_is_not_shown_as_this_edition(library,monkeypatch):
    identity,api,public,calls,errors=configured(library,monkeypatch,'Hades')
    public['retail']=8000;public['excluded_minima']={'retail':6000}
    public['offers'][0]['cents']=8000
    refresh_prices(library,identity)
    assert snapshot(library,identity)['retail']==6000
    value=selected_quote(library,identity)
    assert value['lowest'] is None and value['discount'] is None
    assert value['retail'] is None
    assert value['state']=='offer_unconfirmed' and 'edição' in value['message']


def test_enabling_details_during_a_request_does_not_mark_old_configuration_fresh(library,monkeypatch):
    from checkpoint.prices import invalidate_prices,needs_update
    identity,api,public,calls,errors=configured(library,monkeypatch,'Hades')
    library.set_setting('prices.offer_details',False)
    def changed():
        library.set_setting('prices.offer_details',True);invalidate_prices(library)
    errors['after_api']=changed
    refresh_prices(library,identity)
    assert calls==[] and needs_update(library,identity)
    refresh_prices(library,identity)
    assert len(calls)==1 and not needs_update(library,identity)

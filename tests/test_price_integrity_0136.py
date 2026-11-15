import pytest
from types import SimpleNamespace
from PySide6.QtWidgets import QLabel
from checkpoint.prices import selected_quote,refresh_prices,wishlist_order
from checkpoint.price_view import comparison

@pytest.mark.parametrize('title,platform',[('Zelda Phantom Hourglass','Nintendo DS'),('Metroid Dread','Nintendo Switch')])
def test_non_pc_never_uses_steam_cache_or_calls_pc_provider(library,title,platform):
    i=library.save_game({'title':title,'platform':platform})
    library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','42'));library.sql.commit()
    previous={'lowest':1200,'current_kind':'retail','currency':'BRL'};library.set_setting(f'prices.ggdeals.{i}',previous)
    class Provider:
        def prices(self,*a,**k):raise AssertionError('Não consultar preço PC para console')
    assert selected_quote(library,i).get('lowest') is None
    assert 'plataforma' in refresh_prices(library,i,Provider()).lower()
    assert library.setting(f'prices.ggdeals.{i}')['lowest']==1200
    assert library.sql.execute('SELECT external_id FROM external_identifiers').fetchone()[0]=='42'

@pytest.mark.parametrize('title',['Portal 2','Hades II'])
def test_discount_requires_same_offer_and_confirmed_context(library,title):
    i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)));library.sql.commit()
    quote={'lowest':6000,'retail':6000,'currency':'BRL','original':10000,'discount':40,'historical':1000,'current_kind':'retail','offers':[{'cents':6000,'original':10000,'kind':'retail','shop':'Loja','url':'https://gg.deals/br/redirect/store/'}]}
    library.set_setting(f'prices.ggdeals.{i}',quote)
    assert selected_quote(library,i).get('discount') is None
    quote['offer_context']={'platform':'PC','steam':str(i)};library.set_setting(f'prices.ggdeals.{i}',quote)
    assert selected_quote(library,i)['discount']==40
    quote['offers'][0]['cents']=7000;library.set_setting(f'prices.ggdeals.{i}',quote)
    assert selected_quote(library,i)['discount'] is None
    quote['offers'][0]['cents']=6000;quote['offers'][0]['original']=6000;library.set_setting(f'prices.ggdeals.{i}',quote)
    assert selected_quote(library,i)['discount'] is None


def test_discount_sort_and_keyshop_policy(library):
    ids=[]
    for n,title in enumerate(['Portal 2','Hades II','Sem oferta']):
        i=library.save_game({'title':title});ids.append(i)
        library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)))
        library.set_setting(f'prices.ggdeals.{i}',{'currency':'BRL','retail':6000,'keyshop':2000 if n else 4000,'offer_context':{'platform':'PC','steam':str(i)},'offers':[] if n==2 else [{'kind':'retail','cents':6000,'original':10000 if n==0 else 8000,'shop':'Oficial','url':'https://gg.deals/br/redirect/retail/'},{'kind':'keyshop','cents':2000 if n else 4000,'original':10000,'shop':'Keys','url':'https://gg.deals/br/redirect/keys/'}]})
    assert [g['id'] for g in wishlist_order(library,library.games(),'discount')]==ids
    library.set_setting('prices.include_keyshops',True)
    assert [g['id'] for g in wishlist_order(library,library.games(),'discount')]==[ids[1],ids[0],ids[2]]


def test_comparison_has_reason_instead_of_bare_unavailable(library,app):
    for title,platform in [('Portal 2','PC'),('Zelda','Nintendo DS')]:
        i=library.save_game({'title':title,'platform':platform});frame=comparison(SimpleNamespace(library=library),library.get(i))
        labels=[l.text() for l in frame.findChildren(QLabel)]
        assert '-' in labels and 'Indisponível' not in labels
        assert any('plataforma' in t.lower() or 'ID da Steam' in t for t in labels)


def test_discount_visible_only_for_offer_and_rounds_half_up(library,app):
    from checkpoint.price_view import price_summary
    i=library.save_game({'title':'Portal 2'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
    quote={'currency':'BRL','retail':9950,'offer_context':{'platform':'PC','steam':'620'},'offers':[{'kind':'retail','cents':9950,'original':10000,'shop':'Loja','url':'https://gg.deals/br/redirect/shop/'}]}
    library.set_setting(f'prices.ggdeals.{i}',quote)
    frame=price_summary(library,library.get(i));labels=frame.findChildren(QLabel)
    assert any(l.text()=='-1%' for l in labels)
    assert any(l.text()=='R$ 100,00' and l.font().strikeOut() for l in labels)
    assert selected_quote(library,i)['lowest']==9950
    quote['offer_context']['steam']='999';library.set_setting(f'prices.ggdeals.{i}',quote)
    assert selected_quote(library,i)['discount'] is None


def test_discount_follows_active_theme(library,app):
    from checkpoint.price_view import price_summary
    from checkpoint.theme import apply_theme,THEMES
    from PySide6.QtGui import QPalette
    i=library.save_game({'title':'Portal 2'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
    library.set_setting(f'prices.ggdeals.{i}',{'currency':'BRL','retail':6000,'offer_context':{'platform':'PC','steam':'620'},'offers':[{'kind':'retail','cents':6000,'original':10000,'shop':'Loja','url':'https://gg.deals/br/redirect/shop/'}]})
    frame=price_summary(library,library.get(i));frame.show()
    try:
        for key,theme in THEMES.items():
            apply_theme(app,key);app.processEvents()
            label=frame.findChild(QLabel,'priceDiscount')
            assert label.text()=='-40%'
            assert label.palette().color(QPalette.WindowText).name()==theme.colors['accent']
    finally:frame.close();apply_theme(app,'green')

@pytest.mark.parametrize('title',['Portal 2','Hades'])
def test_cached_quote_from_different_edition_is_not_shown(library,title):
    i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
    cached={'currency':'BRL','retail':6000,'offer_context':{'platform':'PC','steam':'620'}};library.set_setting(f'prices.ggdeals.{i}',cached)
    assert selected_quote(library,i)['lowest']==6000
    library.sql.execute("UPDATE external_identifiers SET external_id='999' WHERE game_id=? AND provider='steam'",(i,));library.sql.commit()
    quote=selected_quote(library,i)
    assert quote.get('lowest') is None and 'identidade' in quote.get('message','').lower()
    assert library.setting(f'prices.ggdeals.{i}')==cached


def test_price_store_and_original_do_not_mix_tied_offers(library,app):
    from checkpoint.price_view import price_summary
    i=library.save_game({'title':'Portal 2'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
    offers=[{'kind':'keyshop','cents':6000,'original':10000,'shop':'Chaves','url':'https://gg.deals/br/redirect/keys/'},
            {'kind':'retail','cents':6000,'original':None,'shop':'Oficial A','url':'https://gg.deals/br/redirect/a/'},
            {'kind':'retail','cents':6000,'original':10000,'shop':'Oficial B','url':'https://gg.deals/br/redirect/b/'}]
    library.set_setting(f'prices.ggdeals.{i}',{'currency':'BRL','retail':6000,'keyshop':6000,'offer_context':{'platform':'PC','steam':'620'},'offers':offers})
    frame=price_summary(library,library.get(i));labels=[l.text() for l in frame.findChildren(QLabel)]
    assert 'Loja oficial · Oficial A' in labels
    assert selected_quote(library,i).get('original') is None
    assert not any('%' in t for t in labels)

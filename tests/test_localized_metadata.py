from dataclasses import replace
from unittest.mock import Mock
from urllib.parse import parse_qs,urlsplit
import pytest
from gamevault.integrations import MetadataResult
from gamevault.integrations.descriptions import PortugueseDescriptions,localize_result
from gamevault.integrations.steam_store import SteamStoreProvider
from gamevault.game_import import save_import
from gamevault.enrichment import complete_game
from gamevault.description_provenance import current
from gamevault.dialogs import GameDialog
from gamevault.window import MainWindow
from PySide6.QtWidgets import QLabel


def wiki_page(title='Example',platform='Game Boy Advance',year='2004',pt='Exemplo'):
    return {'query':{'pages':{'1':{'title':title,'pageprops':{'wikibase-shortdesc':year+' video game'},
        'categories':[{'title':'Category:'+platform+' games'}],'langlinks':[{'lang':'pt','*':pt}]}}}}


def test_portuguese_description_requires_exact_game_platform_and_not_ambiguous():
    http=Mock();http.json.side_effect=[wiki_page(),{'query':{'pages':{'2':{'pageid':2,'title':'Exemplo','extract':'Um jogo de aventura.','pageprops':{}}}}}]
    found=PortugueseDescriptions(http).find('Example','Game Boy Advance','2004-11-04')
    assert found['text']=='Um jogo de aventura.' and found['source']=='https://pt.wikipedia.org/?curid=2'
    assert parse_qs(urlsplit(http.json.call_args_list[1].args[0]).query)['explaintext']==['1']
    for payload in [wiki_page(title='Example 2'),wiki_page(platform='PlayStation 2'),wiki_page(year='2024')]:
        http=Mock();http.json.return_value=payload
        assert PortugueseDescriptions(http).find('Example','Game Boy Advance','2004-11-04') is None
        assert http.json.call_count==1
    payload=wiki_page();payload['query']['pages']['3']={**payload['query']['pages']['1'],'langlinks':[{'lang':'pt','*':'Outro exemplo'}]}
    http=Mock();http.json.return_value=payload
    assert PortugueseDescriptions(http).find('Example','Game Boy Advance') is None


def test_localization_rejects_disambiguation_and_missing_translation():
    payload=wiki_page();payload['query']['pages']['1']['pageprops']['disambiguation']=''
    http=Mock();http.json.return_value=payload
    assert PortugueseDescriptions(http).find('Example','Game Boy Advance') is None
    payload=wiki_page();payload['query']['pages']['1']['langlinks']=[];http.json.return_value=payload
    assert PortugueseDescriptions(http).find('Example','Game Boy Advance') is None


def test_steam_requests_brazilian_and_parses_brazilian_release_date():
    http=Mock();http.json.return_value={'42':{'success':True,'data':{'steam_appid':42,'name':'Example',
        'short_description':'Uma aventura &amp; exploração.','release_date':{'date':'24/fev./2017'}}}}
    result=SteamStoreProvider(http).details('42')
    assert result.description=='Uma aventura & exploração.' and result.release_date=='2017-02-24'
    assert parse_qs(urlsplit(http.json.call_args.args[0]).query)['l']==['brazilian']
    SteamStoreProvider(http).search('Example')
    assert parse_qs(urlsplit(http.json.call_args.args[0]).query)['l']==['brazilian']


def test_rom_with_art_identity_gets_portuguese_description_and_attribution(library):
    identity=save_import(library,{'title':'Example','platform':'Game Boy Advance'},result=MetadataResult('steamgriddb','42','Example'))
    art=Mock(spec=['game_by_id']);art.game_by_id.return_value=MetadataResult('steamgriddb','42','Example')
    descriptions=Mock();descriptions.find.return_value={'text':'Uma aventura para Game Boy Advance.','source':'https://pt.wikipedia.org/?curid=2','language':'pt'}
    complete_game(library,identity,art_provider=art,descriptions=descriptions)
    game=library.get(identity)
    assert game['description']=='Uma aventura para Game Boy Advance.' and current(library,game)['language']=='pt'
    assert game['platform']=='Game Boy Advance'
    art.game_by_id.assert_called_once_with('42')


def test_localization_preserves_manual_text_and_replaces_exact_legacy_source(library):
    original=MetadataResult('rawg','42','Example',description='An adventure.',description_language='en',description_source='https://rawg.io/games/example')
    provider=Mock();provider.details.return_value=original
    descriptions=Mock();descriptions.find.return_value={'text':'Uma aventura.','source':'https://pt.wikipedia.org/?curid=2','language':'pt'}
    identity=save_import(library,{'title':'Example','platform':'Game Boy Advance','description':'An adventure.'},result=original)
    complete_game(library,identity,rawg_provider=provider,descriptions=descriptions)
    assert library.get(identity)['description']=='Uma aventura.'
    library.save_game({'title':'Example','description':'Minha descrição pessoal.'},identity)
    complete_game(library,identity,rawg_provider=provider,descriptions=descriptions)
    assert library.get(identity)['description']=='Minha descrição pessoal.' and current(library,library.get(identity))=={}


def test_release_date_roundtrip_and_information_always_visible(library,app):
    identity=library.save_game({'title':'Example','release_date':'2004-11-04','publisher':'Nintendo','source':'Google Drive'})
    dialog=GameDialog(game=library.get(identity),library=library)
    assert dialog.fields['release_date'].text()=='04/11/2004'
    dialog.fields['release_date'].setText('24/02/2017');assert dialog.data()['release_date']=='2017-02-24'
    dialog.fields['release_date'].setText('31/02/2017');dialog.validate();assert 'DD/MM/AAAA' in dialog.error.text();dialog.reject()
    window=MainWindow(library);window.detail(identity);window.show();app.processEvents()
    labels=[item.text() for item in window.detail_page.findChildren(QLabel) if item.isVisible()]
    assert '04/11/2004' in labels and 'Publicadora · Nintendo' in labels and 'Origem · Google Drive' in labels
    assert library.get(identity)['release_date']=='2004-11-04';window.close()


def test_legacy_steam_english_is_replaced_only_on_exact_source_match(library,folder):
    from urllib.parse import parse_qs,urlsplit
    from gamevault.integrations import IntegrationError
    def payload(url):
        language=parse_qs(urlsplit(url).query)['l'][0]
        return {'42':{'success':True,'data':{'steam_appid':42,'name':'Example',
            'short_description':'An adventure.' if language=='english' else 'Uma aventura.'}}}
    http=Mock();http.json.side_effect=payload
    provider=SteamStoreProvider(http);cache=Mock();cache.download.side_effect=IntegrationError('Offline')
    identity=save_import(library,{'title':'Example','description':'An adventure.'},result=MetadataResult('steam','42','Example'))
    complete_game(library,identity,steam_provider=provider,cache=cache)
    assert library.get(identity)['description']=='Uma aventura.'
    library.save_game({'title':'Example','description':'Meu texto.'},identity)
    complete_game(library,identity,steam_provider=provider,cache=cache)
    assert library.get(identity)['description']=='Meu texto.'


def test_enrichment_fetches_rom_description_even_when_all_art_exists(library,folder,app,monkeypatch):
    import json
    from gamevault.worker import execute_request
    identity=save_import(library,{'title':'Example','platform':'Game Boy Advance',
        'cover':'existing-cover','banner':'existing-banner','logo':'existing-logo'},result=MetadataResult('steamgriddb','42','Example'))
    result=MetadataResult('steamgriddb','42','Example',description='Uma aventura.',
        description_source='https://pt.wikipedia.org/?curid=2',description_language='pt')
    details=Mock(return_value=result);monkeypatch.setattr('gamevault.unified_catalog.selected_details',details)
    monkeypatch.setattr('gamevault.auto_artwork.obtain_artwork',lambda *args,**kwargs:'Preservado')
    request=folder/'request.json';response=folder/'response.json'
    request.write_text(json.dumps({'operation':'enrich','database':str(library.db.path.resolve()),
        'response':str(response.resolve()),'arguments':{'game_id':identity,'force':True}}),encoding='utf-8')
    assert execute_request(request)==0
    details.assert_called_once_with('steamgriddb','42','Game Boy Advance')
    game=library.get(identity)
    assert game['description']=='Uma aventura.' and game['cover']=='existing-cover'

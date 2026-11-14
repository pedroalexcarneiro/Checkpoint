import json
import secrets
import traceback
from unittest.mock import Mock
from urllib.error import HTTPError
from urllib.parse import parse_qs,urlsplit
import pytest
from checkpoint.integrations import IntegrationError
from checkpoint.integrations.ggdeals_api import GgDealsApiProvider,parse_api_prices,download_json
from checkpoint.prices import refresh_prices,snapshot,default_provider
from checkpoint.game_import import save_import
from checkpoint.integrations import MetadataResult


def response(**changes):
    prices={'currentRetail':'59.90','currentKeyshops':'45.00','historicalRetail':'20.00','historicalKeyshops':'15.00','currency':'BRL'}
    prices.update(changes)
    return {'success':True,'data':{'42':{'title':'Example','url':'https://gg.deals/game/example/?affiliate=original','prices':prices}}}


def test_api_parser_current_and_history_are_distinct_not_a_discount():
    result=parse_api_prices(response(),'42')
    assert (result['current'],result['current_kind'],result['historical'])==(4500,'keyshop',1500)
    assert result['original'] is None and result['discount'] is None
    assert result['url'].endswith('?affiliate=original')
    assert parse_api_prices(response(currentKeyshops=None),'42')['current_kind']=='retail'
    result=parse_api_prices(response(currentRetail=None,currentKeyshops=None),'42')
    assert result['current'] is None and result['historical']==1500
    assert parse_api_prices({'success':True,'data':{'42':None}},'42')['current'] is None
    assert parse_api_prices(response(currentRetail='0',currentKeyshops=None),'42')['current'] is None


@pytest.mark.parametrize('payload',[
    {},{'success':False,'data':{}},{'success':True,'data':{}},
    {'success':True,'data':{'42':{'prices':{}}}},
    response(currency='USD'),response(currentRetail='NaN'),response(currentRetail=59.9),response(currentRetail='-1'),response(currentRetail='1.001')])
def test_api_rejects_invalid_response_and_foreign_currency(payload):
    with pytest.raises(IntegrationError):parse_api_prices(payload,'42')


def test_api_missing_one_current_field_does_not_invent_zero():
    payload=response();del payload['data']['42']['prices']['currentRetail']
    assert parse_api_prices(payload,'42')['current']==4500


def test_transport_parameters_and_failures_never_reveal_in_memory_secret(caplog):
    value=secrets.token_urlsafe(32);vault=Mock();vault.get.return_value=value
    requests=[]
    def fetch(url):
        parameters=parse_qs(urlsplit(url).query)
        correct=parameters=={'ids':['42'],'key':[value],'region':['br']}
        assert correct,'Parâmetros da consulta incorretos'
        requests.append(urlsplit(url).path)
        return response()
    provider=GgDealsApiProvider(vault,fetch);assert provider.enabled
    assert provider.prices('42')['current']==4500
    assert requests==['/v1/prices/by-steam-app-id/']
    for error_type in (RuntimeError,ValueError):
        def broken(url):raise error_type(url)
        provider.fetch=broken
        with pytest.raises(IntegrationError) as captured:provider.prices('42')
        shown=''.join(traceback.format_exception(captured.type,captured.value,captured.tb))
        leaked=value in shown or value in caplog.text
        assert not leaked,'Uma credencial apareceu no erro ou no log'
    def limited(url):raise HTTPError(url,429,'',{},None)
    provider.fetch=limited
    with pytest.raises(IntegrationError,match='Limite de consultas') as captured:provider.prices('42')
    leaked=value in str(captured.value) or value in caplog.text
    assert not leaked,'Uma credencial apareceu no erro ou no log'


def test_api_reflected_secret_response_is_rejected_without_storage(library):
    value=secrets.token_urlsafe(32);vault=Mock();vault.get.return_value=value
    provider=GgDealsApiProvider(vault,lambda url:{'success':False,'message':value})
    identity=save_import(library,{'title':'Example'},result=MetadataResult('steam','42','Example'))
    refresh_prices(library,identity,provider)
    stored=json.dumps(snapshot(library,identity));leaked=value in stored
    assert not leaked,'Uma credencial apareceu no cache de preços'


def test_missing_steam_id_does_not_call_provider(library):
    identity=library.save_game({'title':'ROM'});provider=Mock()
    assert refresh_prices(library,identity,provider)=='Sem ID da Steam para consulta'
    provider.prices.assert_not_called()


def test_factory_selects_api_or_configured_public_fallback(library,monkeypatch):
    from checkpoint.integrations.ggdeals import GgDealsProvider
    vault=Mock();vault.get.return_value=None
    monkeypatch.setattr('checkpoint.credentials.CredentialVault',lambda:vault)
    assert isinstance(default_provider(library),GgDealsProvider)
    library.set_setting('prices.public_fallback',False)
    with pytest.raises(IntegrationError):default_provider(library)
    vault.get.return_value=secrets.token_urlsafe(32)
    assert isinstance(default_provider(library),GgDealsApiProvider)


def test_api_failure_keeps_previous_price_and_null_is_not_zero(library):
    identity=save_import(library,{'title':'Example'},result=MetadataResult('steam','42','Example'))
    library.set_setting(f'prices.ggdeals.{identity}',{'lowest':5900,'currency':'BRL','checked_at':'2026-01-01T00:00:00+00:00'})
    vault=Mock();vault.get.return_value=secrets.token_urlsafe(32)
    broken=GgDealsApiProvider(vault,lambda url:response(currency='USD'))
    refresh_prices(library,identity,broken)
    assert snapshot(library,identity)['lowest']==5900
    empty=GgDealsApiProvider(vault,lambda url:response(currentRetail=None,currentKeyshops=None))
    refresh_prices(library,identity,empty)
    assert snapshot(library,identity)['lowest']==5900
    assert snapshot(library,identity)['state']=='unavailable'

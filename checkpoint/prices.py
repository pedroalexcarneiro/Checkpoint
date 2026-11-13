"""Cache de uma hora, sem preços inventados nem consultas na thread da interface."""
from datetime import datetime,timezone
from .library import now
from .integrations import IntegrationError


def money(value):return 'Sem oferta' if value is None else 'R$ '+f'{value/100:,.2f}'.replace(',','X').replace('.',',').replace('X','.')


def snapshot(library,game_id):return library.setting(f'prices.ggdeals.{game_id}',{})


def needs_update(library,game_id):
    value=snapshot(library,game_id)
    if value.get('config_version',0)!=library.setting('prices.config_version',0):return True
    try:return (datetime.now(timezone.utc)-datetime.fromisoformat(value['attempted_at'])).total_seconds()>=3600
    except (KeyError,ValueError,TypeError):return True


def default_provider(library):
    from .integrations.price_provider import GgDealsApiProvider
    from .integrations.ggdeals import GgDealsProvider
    try:
        from .credentials import CredentialVault
        official=GgDealsApiProvider(CredentialVault())
        if official.enabled:return official
    except Exception:pass
    if library.setting('prices.public_fallback',True):return GgDealsProvider()
    raise IntegrationError('Configure a API GG.deals ou ative a consulta pela página pública em Conexões.')


def refresh_prices(library,game_id,provider=None):
    from .integrations.ggdeals import GgDealsProvider
    game=library.get(game_id)
    if not game:return 'Jogo indisponível.'
    identity=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game_id,)).fetchone()
    previous=snapshot(library,game_id);url=previous.get('url')
    if not identity:
        previous.update({'config_version':library.setting('prices.config_version',0),'attempted_at':now(),'state':'missing_steam_id','message':'Sem ID da Steam para consulta'})
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return 'Sem ID da Steam para consulta'
    try:
        result=(provider or default_provider(library)).prices(identity[0],url=url)
        current=result.get('current',result.get('lowest'))
        if result.get('currency')!='BRL' or (current is not None and (type(current) is not int or current<=0)):
            raise IntegrationError('Nenhuma oferta em reais disponível. Último preço salvo preservado.')
        result['lowest']=result['current']=current
        result.update({'config_version':library.setting('prices.config_version',0),'checked_at':now(),'attempted_at':now(),'state':'ready' if current is not None else 'unavailable'})
        library.set_setting(f'prices.ggdeals.{game_id}',result)
        return 'Preços GG.deals atualizados.'
    except IntegrationError as error:
        previous.update({'config_version':library.setting('prices.config_version',0),'attempted_at':now(),'state':'unavailable','message':str(error)})
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return str(error)


def wishlist_order(library,games,order='discount'):
    def key(game):
        value=snapshot(library,game['id'])
        discount=value.get('discount') if value.get('lowest',0) and value.get('lowest',0)>0 else None
        return (-(discount or 0),game['title'].casefold()) if order=='discount' else (game['title'].casefold(),)
    return sorted(games,key=key)


def invalidate_prices(library):
    current=library.setting('prices.config_version',0)
    library.set_setting('prices.config_version',current+1 if type(current) is int and current>=0 else 1)

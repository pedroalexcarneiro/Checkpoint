"""Cache de uma hora, sem preços inventados nem consultas na thread da interface."""
from datetime import datetime,timezone
from .library import now
from .integrations import IntegrationError


def money(value):return 'Sem oferta' if value is None else 'R$ '+f'{value/100:,.2f}'.replace(',','X').replace('.',',').replace('X','.')


def snapshot(library,game_id):return library.setting(f'prices.ggdeals.{game_id}',{})


def needs_update(library,game_id):
    value=snapshot(library,game_id)
    try:return (datetime.now(timezone.utc)-datetime.fromisoformat(value['attempted_at'])).total_seconds()>=3600
    except (KeyError,ValueError,TypeError):return True


def refresh_prices(library,game_id,provider=None):
    from .integrations.ggdeals import GgDealsProvider
    game=library.get(game_id)
    if not game:return 'Jogo indisponível.'
    identity=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game_id,)).fetchone()
    previous=snapshot(library,game_id);url=previous.get('url')
    try:
        result=(provider or GgDealsProvider()).prices(identity[0] if identity else None,url=url)
        current=result.get('current',result.get('lowest'))
        if result.get('currency')!='BRL' or not isinstance(current,int) or current<=0:
            raise IntegrationError('Nenhuma oferta em reais disponível. Último preço salvo preservado.')
        result['lowest']=result['current']=current
        result.update({'checked_at':now(),'attempted_at':now(),'state':'ready'})
        library.set_setting(f'prices.ggdeals.{game_id}',result)
        return 'Preços GG.deals atualizados.'
    except IntegrationError as error:
        previous.update({'attempted_at':now(),'state':'unavailable','message':str(error)})
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return str(error)


def wishlist_order(library,games,order='discount'):
    def key(game):
        value=snapshot(library,game['id'])
        discount=value.get('discount') if value.get('lowest',0) and value.get('lowest',0)>0 else None
        return (-(discount or 0),game['title'].casefold()) if order=='discount' else (game['title'].casefold(),)
    return sorted(games,key=key)

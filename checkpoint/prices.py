"""Cache de uma hora, sem preços inventados nem consultas na thread da interface."""
from datetime import datetime,timezone
from .library import now
from .integrations import IntegrationError


def money(value):return 'Indisponível' if type(value) is not int or value<=0 else 'R$ '+f'{value/100:,.2f}'.replace(',','X').replace('.',',').replace('X','.')


def snapshot(library,game_id):return library.setting(f'prices.ggdeals.{game_id}',{})


def platform_problem(game):
    platform=(game.get('platform') or '').strip().casefold()
    if platform not in ('pc','windows','linux','mac','macos','pc (windows)'):
        return 'Cobertura da plataforma/edição não confirmada nesta fonte.'
    return ''


def selected_quote(library,game_id):
    raw=snapshot(library,game_id);value=dict(raw)
    game=library.get(game_id) or {}
    problem=platform_problem(game)
    if problem:return {'message':problem,'state':'unsupported_platform'}
    if value.get('currency','BRL')!='BRL':return {'message':'Preço salvo em outra moeda. Consulte ofertas em reais.'}
    context=value.get('offer_context',{})
    steam=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game_id,)).fetchone()
    confirmed=bool(steam and context.get('steam')==steam[0] and context.get('platform')==game.get('platform'))
    if context and not confirmed:
        return {'lowest':None,'current':None,'original':None,'discount':None,'state':'identity_mismatch','message':'Identidade alterada. Consulte preços da edição atual.'}
    allowed=('retail','keyshop') if library.setting('prices.include_keyshops',False) else ('retail',)
    unconfirmed=value.get('unconfirmed_kinds') or []
    allowed=tuple(kind for kind in allowed if kind not in unconfirmed)
    for kind in unconfirmed:
        if kind in ('retail','keyshop'):value[kind]=None
    choices=[]
    def add(amount,kind):
        if kind in allowed and type(amount) is int and amount>0:choices.append((amount,kind))
    for kind in allowed:add(value.get(kind),kind)
    add(value.get('current',value.get('lowest')),value.get('current_kind'))
    for offer in value.get('offers',[]):add(offer.get('cents'),offer.get('kind'))
    amount,kind=min(choices,default=(None,None))
    value.update(lowest=amount,current=amount,current_kind=kind,original=None,discount=None)
    if kind and value.get('details_enabled') and 'detail_prices' in value and value['detail_prices'].get(kind)!=amount:
        value['details_state']='price_mismatch'
    # Um original só acompanha exatamente a oferta escolhida, nunca o histórico/agregado.
    offers=[o for o in value.get('offers',[]) if o.get('cents')==amount and o.get('kind')==kind]
    from urllib.parse import urlsplit
    value['selected_offer']=offers[0] if offers else {}
    for offer in offers[:1] if confirmed and value.get('currency')=='BRL' else []:
        original=offer.get('original');url=urlsplit(offer.get('url',''))
        if type(original) is int and original>amount and offer.get('shop') and url.scheme=='https' and url.netloc=='gg.deals' and url.path.startswith('/br/redirect/'):
            # Inteiro mais próximo; empate arredonda para cima. Nenhum 0% inventado.
            discount=((original-amount)*200+original)//(2*original)
            if discount>0:value.update(original=original,discount=discount,selected_offer=offer)
            break
    if amount is None and value.get('unconfirmed_kinds'):
        value.update(state='offer_unconfirmed',message='Preço da API sem confirmação para esta edição. Confira as ofertas.')
    if amount is None and (not value.get('message') or value.get('state')=='ready'):
        if allowed==('retail',) and ('retail' in value or value.get('state')=='ready'):
            value['message']='Consulta sem oferta em lojas oficiais.'
        elif raw.get('lowest'):
            value['message']='A origem do preço salvo não foi identificada. Consulte novamente.'
        elif value.get('state')=='ready':value['message']='Consulta sem ofertas disponíveis.'
    if amount is None and not value.get('message'):
        value['message']='Preços ainda não consultados.' if steam else 'Sem ID da Steam para consultar ofertas.'
    return value


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
        if official.enabled:
            if library.setting('prices.offer_details',False):
                from .price_enrichment import OfferDetailsProvider
                return OfferDetailsProvider(official,GgDealsProvider())
            return official
    except Exception:pass
    if library.setting('prices.public_fallback',True):return GgDealsProvider()
    raise IntegrationError('Configure a API GG.deals ou ative a consulta pela página pública em Conexões.')


def refresh_prices(library,game_id,provider=None):
    from .integrations.ggdeals import GgDealsProvider
    game=library.get(game_id)
    if not game:return 'Jogo indisponível.'
    identity=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game_id,)).fetchone()
    previous=snapshot(library,game_id);url=previous.get('url')
    config_version=library.setting('prices.config_version',0)
    problem=platform_problem(game)
    if problem:
        previous.update(state='unsupported_platform',message=problem,attempted_at=now())
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return problem
    context=previous.get('offer_context',{})
    if not identity or context.get('steam')!=identity[0] or context.get('platform')!=game['platform']:url=None
    if not identity:
        previous.update({'config_version':config_version,'attempted_at':now(),'state':'missing_steam_id','message':'Sem ID da Steam para consulta'})
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return 'Sem ID da Steam para consulta'
    try:
        result=(provider or default_provider(library)).prices(identity[0],url=url)
        current=result.get('current',result.get('lowest'))
        if result.get('currency')!='BRL' or type(current) is not int or current<=0:
            raise IntegrationError('Nenhuma oferta em reais disponível. Último preço salvo preservado.')
        result['lowest']=result['current']=current
        result['offer_context']={'platform':game['platform'],'steam':identity[0]}
        result.update({'config_version':config_version,'checked_at':now(),'attempted_at':now(),'state':'ready' if current is not None else 'unavailable'})
        library.set_setting(f'prices.ggdeals.{game_id}',result)
        return 'Preços GG.deals atualizados.'
    except IntegrationError as error:
        previous.update({'config_version':library.setting('prices.config_version',0),'attempted_at':now(),'state':'unavailable','message':str(error)})
        library.set_setting(f'prices.ggdeals.{game_id}',previous)
        return str(error)


def wishlist_order(library,games,order='name'):
    def key(game):
        value=selected_quote(library,game['id']);current=value.get('lowest')
        usable=type(current) is int and current>0 and value.get('currency','BRL')=='BRL'
        name=game['title'].casefold()
        if order=='discount':
            discount=value.get('discount')
            valid=usable and type(discount) is int and discount>0
            return (not valid,-discount if valid else 0,name,game['id'])
        return (not usable,current if usable else 0,name,game['id']) if order=='price' else (name,game['id'])
    return sorted(games,key=key)


def invalidate_prices(library):
    current=library.setting('prices.config_version',0)
    library.set_setting('prices.config_version',current+1 if type(current) is int and current>=0 else 1)

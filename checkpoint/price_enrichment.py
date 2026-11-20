"""Complemento opcional da API, sem trocar seus valores por outra oferta."""
from urllib.parse import urlsplit
from .integrations.ggdeals import game_url
from .integrations import IntegrationError


class OfferDetailsProvider:
    def __init__(self,api,public):
        self.api=api;self.public=public

    def prices(self,identity=None,url=None):
        base=self.api.prices(identity,url=url)
        result={**base,'details_enabled':True,'details_state':'unconfirmed'}
        if base.get('currency')!='BRL':return result
        try:canonical=game_url(base.get('url',''))
        except (IntegrationError,ValueError,TypeError):
            result['details_state']='identity_unconfirmed';return result
        try:
            details=self.public.prices(identity,url=canonical)
            if details.get('currency')!='BRL' or game_url(details.get('url',''))!=canonical:
                result['details_state']='identity_mismatch';return result
        except Exception:
            # Não propagar corpo/URL/erro do transporte e não perder a API válida.
            result['details_state']='unavailable';return result
        result['detail_prices']={kind:details.get(kind) for kind in ('retail','keyshop')}
        excluded=details.get('excluded_minima') or {}
        result['unconfirmed_kinds']=[kind for kind in ('retail','keyshop') if
            type(base.get(kind)) is int and excluded.get(kind)==base[kind] and details.get(kind)!=base[kind]]
        matched=[];offers=details.get('offers') or []
        if not isinstance(offers,list):return result
        for offer in offers:
            if not isinstance(offer,dict):continue
            if offer.get('game_slug')!=urlsplit(canonical).path.rstrip('/').split('/')[-1]:continue
            kind=offer.get('kind');amount=offer.get('cents');original=offer.get('original')
            if kind not in ('retail','keyshop') or type(amount) is not int or amount<=0 or amount!=base.get(kind) or details.get(kind)!=base.get(kind):continue
            if type(original) is not int or original<=amount or not isinstance(offer.get('shop'),str) or not offer['shop'].strip():continue
            try:link=urlsplit(offer.get('url',''))
            except (ValueError,TypeError):continue
            if link.scheme!='https' or link.netloc!='gg.deals' or not link.path.startswith('/br/redirect/'):continue
            matched.append({key:offer[key] for key in ('shop','cents','original','url','kind','drm','game_slug') if key in offer})
        if matched:
            result['offers']=matched;result['details_state']='verified'
        elif any(type(base.get(kind)) is int and base.get(kind)!=details.get(kind) for kind in ('retail','keyshop')):
            result['details_state']='price_mismatch'
        return result

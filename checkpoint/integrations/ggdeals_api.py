"""API oficial GG.deals. Segredos existem somente em memória durante a consulta."""
from decimal import Decimal,InvalidOperation
import json
from urllib.error import HTTPError
from urllib.parse import urlencode,urlsplit
from urllib.request import Request,build_opener,HTTPRedirectHandler
from . import IntegrationError
from .steam import app_id

API_URL='https://api.gg.deals/v1/prices/by-steam-app-id/'
INVALID='A API GG.deals retornou uma resposta inválida. Tente novamente.'


def price_cents(value):
    if value is None:return None
    if not isinstance(value,str):raise IntegrationError(INVALID)
    try:
        number=Decimal(value)
        if not number.is_finite() or number<0 or number>10_000_000 or number*100!=(number*100).to_integral_value():raise ValueError()
        return int(number*100) if number>0 else None
    except (InvalidOperation,ValueError,OverflowError):raise IntegrationError(INVALID) from None


def parse_api_prices(payload,identity):
    identity=app_id(identity)
    if not isinstance(payload,dict) or payload.get('success') is not True or not isinstance(payload.get('data'),dict) or identity not in payload['data']:
        raise IntegrationError(INVALID)
    game=payload['data'][identity]
    empty={'provider':'api','currency':'BRL','current':None,'lowest':None,'retail':None,'keyshop':None,'historical':None,'historical_retail':None,'historical_keyshop':None,'current_kind':None,'original':None,'discount':None,'stores':[],'offers':[],'url':f'https://gg.deals/br/steam/app/{identity}/','title':''}
    if game is None:return empty
    if not isinstance(game,dict) or not isinstance(game.get('prices'),dict):raise IntegrationError(INVALID)
    prices=game['prices']
    if prices.get('currency')!='BRL':raise IntegrationError('A API GG.deals não retornou preços em reais. Nenhuma conversão foi feita.')
    if not any(key in prices for key in ('currentRetail','currentKeyshops')):raise IntegrationError(INVALID)
    retail=price_cents(prices.get('currentRetail'));keyshop=price_cents(prices.get('currentKeyshops'))
    history_retail=price_cents(prices.get('historicalRetail'));history_keyshop=price_cents(prices.get('historicalKeyshops'))
    choices=[(value,kind) for value,kind in ((retail,'retail'),(keyshop,'keyshop')) if value is not None]
    current,kind=min(choices,key=lambda pair:pair[0]) if choices else (None,None)
    historical=min((value for value in (history_retail,history_keyshop) if value is not None),default=None)
    url=game.get('url',empty['url']);parsed=urlsplit(url) if isinstance(url,str) else None
    if not parsed or parsed.scheme!='https' or parsed.netloc!='gg.deals':raise IntegrationError(INVALID)
    title=game.get('title','')
    if not isinstance(title,str):raise IntegrationError(INVALID)
    return {**empty,'url':url,'title':title,'current':current,'lowest':current,'retail':retail,'keyshop':keyshop,'current_kind':kind,'historical':historical,'historical_retail':history_retail,'historical_keyshop':history_keyshop}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,request,fp,code,msg,headers,newurl):return None


def download_json(url):
    request=Request(url,headers={'Accept':'application/json','User-Agent':'Checkpoint/0.1.29'})
    # Não permite encaminhar a URL autenticada a um destino de redirecionamento.
    with build_opener(NoRedirect()).open(request,timeout=15) as response:
        data=response.read(1_000_001)
        if len(data)>1_000_000:raise IntegrationError(INVALID)
        return json.loads(data)


class GgDealsApiProvider:
    def __init__(self,vault=None,fetch=None):self.vault=vault;self.fetch=fetch or download_json
    @property
    def enabled(self):
        try:
            value=self.vault.get('ggdeals') if self.vault is not None else None
            return isinstance(value,str) and bool(value.strip())
        except Exception:return False
    def prices(self,identity=None,url=None):
        if identity is None:raise IntegrationError('Sem ID da Steam para consulta')
        identity=app_id(identity)
        try:value=self.vault.get('ggdeals') if self.vault is not None else None
        except Exception:raise IntegrationError('Não foi possível acessar a configuração GG.deals no cofre.') from None
        if not isinstance(value,str) or not value.strip():raise IntegrationError('API GG.deals não configurada.')
        request_url=API_URL+'?'+urlencode({'ids':identity,'key':value.strip(),'region':'br'})
        try:
            payload=self.fetch(request_url)
            # A resposta não pode refletir a credencial em nenhum campo persistido.
            if value.strip() in json.dumps(payload,ensure_ascii=False):raise IntegrationError(INVALID)
            return parse_api_prices(payload,identity)
        except HTTPError as error:
            code=error.code
            message='Limite de consultas GG.deals atingido. Tente novamente mais tarde.' if code==429 else 'A API GG.deals não pôde ser consultada. Confira a configuração e tente novamente.'
            raise IntegrationError(message) from None
        except Exception:
            # Nunca propaga URL, corpo de erro ou exceção do transporte/cofre.
            raise IntegrationError('Não foi possível obter os preços da API GG.deals. Confira a configuração e tente novamente.') from None

"""Preços da página pública BR do GG.deals; identidade por redirecionamento oficial."""
from html.parser import HTMLParser
from decimal import Decimal,InvalidOperation
from urllib.parse import urljoin,urlsplit
from urllib.request import Request,urlopen
import json
import re
from . import IntegrationError
from .steam import app_id


class Node:
    def __init__(self,tag='',attrs=(),parent=None):
        self.tag=tag;self.attrs=dict(attrs);self.parent=parent;self.children=[];self.data=[]
    def find(self,predicate):
        for node in self.children:
            if predicate(node):yield node
            yield from node.find(predicate)
    def has(self,name):return name in self.attrs.get('class','').split()
    def text(self):return ''.join(self.data)+''.join(node.text() for node in self.children)


class Page(HTMLParser):
    def __init__(self,content):
        super().__init__(convert_charrefs=True);self.root=Node();self.current=self.root;self.feed(content)
    def handle_starttag(self,tag,attrs):
        node=Node(tag,attrs,self.current);self.current.children.append(node)
        if tag not in {'img','input','br','hr','meta','link','source','wbr','area','base','embed','param','track','col'}:self.current=node
    def handle_startendtag(self,tag,attrs):self.current.children.append(Node(tag,attrs,self.current))
    def handle_endtag(self,tag):
        node=self.current
        while node.parent:
            if node.tag==tag:self.current=node.parent;return
            node=node.parent
    def handle_data(self,data):self.current.data.append(data)


def game_url(value):
    parsed=urlsplit(value)
    if parsed.scheme!='https' or parsed.netloc!='gg.deals' or not re.fullmatch(r'/(?:br/)?game/[a-z0-9-]+/',parsed.path):
        raise IntegrationError('Página GG.deals indisponível para esta edição.')
    return 'https://gg.deals/br/game/'+parsed.path.rstrip('/').split('/')[-1]+'/'


def cents(value):
    match=re.search(r'R\$\s*([\d.]+,\d{2})',value)
    if not match:return None
    try:return int(Decimal(match[1].replace('.','').replace(',','.'))*100)
    except (InvalidOperation,ValueError):return None


def parse_prices(content):
    page=Page(content).root
    canonical=next((node.attrs['href'] for node in page.find(lambda n:n.tag=='link' and n.attrs.get('rel')=='canonical' and 'href' in n.attrs)),None)
    if not canonical:raise IntegrationError('A página de preços não pôde ser identificada. Abra o GG.deals para conferir.')
    url=game_url(canonical);currency=None;title='';aggregate=None
    for node in page.find(lambda n:n.tag=='script' and n.attrs.get('type')=='application/ld+json'):
        try:payload=json.loads(node.text())
        except (ValueError,TypeError):continue
        if isinstance(payload,dict) and isinstance(payload.get('offers'),dict):
            currency=payload['offers'].get('priceCurrency');title=payload.get('name','')
            try:
                amount=Decimal(str(payload['offers'].get('lowPrice')))*100
                if amount.is_finite() and 0<amount<=1_000_000_000:aggregate=int(amount)
            except (InvalidOperation,ValueError):pass
    if currency!='BRL':raise IntegrationError('A fonte não retornou preços em reais. Nenhum valor foi convertido ou apresentado como BRL.')
    offers=[]
    for section in page.find(lambda n:n.tag=='section' and n.attrs.get('id') in ('official-stores','keyshops')):
        kind='retail' if section.attrs['id']=='official-stores' else 'keyshop'
        for row in section.find(lambda n:n.has('game-list-item') and n.attrs.get('data-shop-name')):
            price=next((cents(n.text()) for n in row.find(lambda n:n.has('price') and not n.has('price-old')) if cents(n.text()) is not None),None)
            link=next((n.attrs.get('href') for n in row.find(lambda n:n.tag=='a' and n.has('shop-link'))),None)
            if price is None or price<=0 or not link:continue
            link=urljoin('https://gg.deals',link);parsed=urlsplit(link)
            if parsed.scheme!='https' or parsed.netloc!='gg.deals' or not parsed.path.startswith('/br/redirect/'):continue
            drm=next((n.text().replace('DRM:','').strip() for n in row.find(lambda n:n.has('tag-drm'))),'')
            original=next((cents(n.text()) for n in row.find(lambda n:n.has('price-old')) if cents(n.text()) is not None),None)
            if original is not None and original<=price:original=None
            discount=round((original-price)*100/original) if original else None
            offers.append({'shop':row.attrs['data-shop-name'],'cents':price,'original':original,'discount':discount,'url':link,'kind':kind,'drm':drm})
    offers.sort(key=lambda row:row['cents'])
    minima={kind:min((row['cents'] for row in offers if row['kind']==kind),default=None) for kind in ('retail','keyshop')}
    for kind,anchor in [('retail','#official-stores'),('keyshop','#keyshops')]:
        for node in page.find(lambda n:n.tag=='a' and n.has('game-header-price') and n.attrs.get('href')==anchor):
            value=cents(node.text())
            if value is not None and value>0:minima[kind]=value;break
    valid=[value for value in minima.values() if value is not None]
    if aggregate is None and not valid:raise IntegrationError('Nenhuma oferta em reais foi carregada. Confira a página do GG.deals.')
    lowest=aggregate if aggregate is not None else min(valid)
    best=next((offer for offer in offers if offer['cents']==lowest),{})
    return {'current':lowest,'original':best.get('original'),'discount':best.get('discount'),'stores':offers,
        'url':url,'currency':'BRL','title':title,'offers':offers,
        'retail':minima['retail'],'keyshop':minima['keyshop'],
        'lowest':lowest}



from .price_provider import PriceProvider


class GgDealsProvider(PriceProvider):
    def __init__(self,fetch=None):self.fetch=fetch or self.download
    def download(self,url):
        try:
            request=Request(url,headers={'User-Agent':'Checkpoint/0.1 (+https://github.com/pedroalexcarneiro/Checkpoint)'})
            with urlopen(request,timeout=12) as response:
                if urlsplit(response.url).netloc!='gg.deals':raise IntegrationError('Destino GG.deals inesperado.')
                raw=response.read(8_000_001)
                if len(raw)>8_000_000:raise IntegrationError('Página de preços excedeu o limite.')
                return raw.decode('utf-8')
        except (OSError,UnicodeError):raise IntegrationError('GG.deals indisponível. Tente novamente mais tarde ou abra a página do jogo.') from None
    def prices(self,identity=None,url=None):
        if url:target=game_url(url)
        elif identity:target=f'https://gg.deals/br/steam/app/{app_id(identity)}/'
        else:raise IntegrationError('Este jogo ainda não tem uma página GG.deals confirmada.')
        return parse_prices(self.fetch(target))

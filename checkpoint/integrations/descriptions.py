"""Descrições PT por artigo exato e plataforma, sem identificar ROM por semelhança."""
from dataclasses import replace
from urllib.parse import urlencode
import re
from .http import HttpClient
from . import IntegrationError


class PortugueseDescriptions:
    def __init__(self,http=None):
        self.http=http or HttpClient(timeout=8,attempts=1)

    def find(self,title,platform,release_date=''):
        from ..automatic_catalog import normalized
        if not title.strip() or not platform:return None
        aliases={'pc':'windows','gba':'game boy advance','snes':'super nintendo entertainment system',
                 'super nintendo':'super nintendo entertainment system','nes':'nintendo entertainment system',
                 'playstation':'playstation','playstation 2':'playstation 2'}
        platform=aliases.get(normalized(platform),normalized(platform))
        variants=[title,title+' (video game)']
        if re.match(r'^\d{4}',release_date):variants.append(f'{title} ({release_date[:4]} video game)')
        payload=self.http.json('https://en.wikipedia.org/w/api.php?'+urlencode({
            'action':'query','format':'json','prop':'langlinks|pageprops|categories',
            'lllang':'pt','lllimit':1,'cllimit':100,'redirects':1,'titles':'|'.join(variants)}))
        matches=[]
        for page in payload.get('query',{}).get('pages',{}).values():
            props=page.get('pageprops',{})
            if 'missing' in page or 'disambiguation' in props:continue
            if normalized(page.get('title',''))!=normalized(title):continue
            summary=props.get('wikibase-shortdesc','')
            if not re.search(r'\bvideo game\b',summary,re.I):continue
            year=re.match(r'^(\d{4})\b',summary)
            if year and release_date and year[1]!=release_date[:4]:continue
            categories=[normalized(row.get('title','').removeprefix('Category:')) for row in page.get('categories',[])]
            if not any(value in (platform+' games',platform+' only games') for value in categories):continue
            links=[row['*'] for row in page.get('langlinks',[]) if row.get('lang')=='pt' and row.get('*')]
            if len(links)==1:matches.append(links[0])
        if len(set(matches))!=1:return None
        payload=self.http.json('https://pt.wikipedia.org/w/api.php?'+urlencode({
            'action':'query','format':'json','prop':'extracts|pageprops','exintro':1,
            'explaintext':1,'redirects':1,'titles':matches[0]}))
        pages=list(payload.get('query',{}).get('pages',{}).values())
        if len(pages)!=1:return None
        page=pages[0];description=(page.get('extract') or '').strip()
        if 'missing' in page or 'disambiguation' in page.get('pageprops',{}) or not description:return None
        if not str(page.get('pageid','')).isdigit():return None
        return {'text':description,'source':f"https://pt.wikipedia.org/?curid={page['pageid']}",
                'language':'pt','title':page['title']}


def localize_result(result,platform,provider=None):
    # Steam já solicita a ficha localizada; SteamGridDB não fornece descrições.
    if result.provider=='steam' and result.description:return result
    try:
        found=(provider or PortugueseDescriptions()).find(result.title,platform,result.release_date)
        if found:
            return replace(result,description=found['text'],description_source=found['source'],description_language=found['language'])
    except (IntegrationError,OSError,ValueError):pass
    return result

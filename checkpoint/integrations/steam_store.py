"""Ficha pública da loja Steam, identificada por AppID; não usa chave pessoal."""
import re
from html import unescape
from datetime import datetime
from urllib.parse import urlencode

from . import IntegrationError, MetadataResult
from .http import HttpClient
from .steam import app_id


class SteamStoreProvider:
    def __init__(self, http=None):
        self.http = http or HttpClient()

    def search(self, title):
        query = urlencode({'term': title, 'l': 'brazilian', 'cc': 'BR'})
        payload = self.http.json('https://store.steampowered.com/api/storesearch/?' + query)
        return [MetadataResult('steam', app_id(str(row['id'])), row['name'],platforms=('PC',))
                for row in payload.get('items', []) if row.get('type') == 'app']

    def details(self, identity, language='brazilian'):
        identity = app_id(identity)
        payload = self.http.json('https://store.steampowered.com/api/appdetails?' +
                                 urlencode({'appids': identity, 'l': language, 'cc': 'BR'}))
        entry = payload.get(identity, {})
        row = entry.get('data', {})
        if not entry.get('success') or str(row.get('steam_appid')) != identity or not row.get('name'):
            raise IntegrationError('Ficha indisponível na loja Steam para este AppID.')
        release = row.get('release_date') or {}
        date = ''
        if not release.get('coming_soon'):
            localized=release.get('date','').lower()
            for pt,en in [('fev','feb'),('abr','apr'),('mai','may'),('ago','aug'),('set','sep'),('out','oct'),('dez','dec')]:
                localized=re.sub(r'\b'+pt+r'\b',en,localized)
            localized=re.sub(r'\s+de\s+',' ',localized).replace('.','')
            for pattern in ('%d %b, %Y', '%b %d, %Y', '%d %b %Y', '%d/%m/%Y', '%d/%b/%Y', '%Y-%m-%d'):
                try:
                    date = datetime.strptime(localized, pattern).date().isoformat()
                    break
                except ValueError:
                    pass
        images = {'cover': f'https://cdn.akamai.steamstatic.com/steam/apps/{identity}/library_600x900.jpg',
                  'logo': f'https://cdn.akamai.steamstatic.com/steam/apps/{identity}/logo.png',
                  'banner': f'https://cdn.akamai.steamstatic.com/steam/apps/{identity}/library_hero.jpg'}
        alternatives={}
        if row.get('header_image'):
            alternatives['banner']=[row['header_image']]
        # Alguns jogos não publicam todos os formatos de arte. O cache valida cada resposta.
        return MetadataResult('steam', identity, row['name'],
                              description=unescape(re.sub('<[^>]+>', '', row.get('short_description') or row.get('detailed_description') or '')).strip(),
                              description_source=f'https://store.steampowered.com/app/{identity}/',
                              description_language='pt-BR' if language=='brazilian' else 'en',
                              release_date=date,
                              genres=tuple(item['description'] for item in row.get('genres', [])),
                              platforms=('PC',), images=images, image_candidates=alternatives,
                              developer=', '.join(row.get('developers') or []),
                              publisher=', '.join(row.get('publishers') or []))

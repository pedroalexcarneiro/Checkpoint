import json
from urllib.parse import urlencode
from . import MetadataResult,IntegrationError
from .http import HttpClient

class RawgProvider:
    def __init__(self,key,http=None):
        if not key: raise IntegrationError('Configure uma chave RAWG.')
        self.key = key; self.http = http or HttpClient()

    def search(self,title):
        if not title.strip(): return []
        payload = self.http.json('https://api.rawg.io/api/games?'+urlencode({'key':self.key,'search':title,'page_size':20}))
        return [MetadataResult('rawg',str(row['id']),row['name'],release_date=row.get('released') or '',
            genres=tuple(g['name'] for g in row.get('genres',[])),
            platforms=tuple(p['platform']['name'] for p in row.get('platforms') or []),
            images={'banner':row['background_image']} if row.get('background_image') else {}) for row in payload.get('results',[])]

    def details(self,external_id):
        if not str(external_id).isdigit(): raise ValueError('Identificador RAWG inválido.')
        row = self.http.json(f'https://api.rawg.io/api/games/{external_id}?'+urlencode({'key':self.key}))
        return MetadataResult('rawg',str(row['id']),row['name'],description=row.get('description_raw',''),
            release_date=row.get('released') or '',genres=tuple(g['name'] for g in row.get('genres',[])),
            platforms=tuple(p['platform']['name'] for p in row.get('platforms') or []),
            images={'banner':row['background_image']} if row.get('background_image') else {})

class SteamGridDbProvider:
    def __init__(self,key,http=None):
        if not key: raise IntegrationError('Configure uma chave SteamGridDB.')
        self.key = key; self.http = http or HttpClient()

    def search(self,title):
        from urllib.parse import quote
        payload = self.http.json('https://www.steamgriddb.com/api/v2/search/autocomplete/'+quote(title,safe=''),
                                 {'Authorization':'Bearer '+self.key})
        return [MetadataResult('steamgriddb',str(r['id']),r['name']) for r in payload.get('data',[])]

    def artworks(self,game_id,kind='cover'):
        if not str(game_id).isdigit(): raise ValueError('Identificador inválido.')
        resource = {'cover':'grids','banner':'heroes','logo':'logos'}[kind]
        query = '?dimensions=600x900' if kind=='cover' else ''
        payload = self.http.json(f'https://www.steamgriddb.com/api/v2/{resource}/game/{game_id}'+query,
                                 {'Authorization':'Bearer '+self.key})
        return [r['url'] for r in payload.get('data',[]) if not r.get('nsfw')]

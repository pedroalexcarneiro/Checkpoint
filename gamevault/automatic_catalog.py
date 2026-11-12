"""Identificação pelo nome, com plataforma e sem aplicar resultados ambíguos."""
from dataclasses import replace
from difflib import SequenceMatcher
import re
import unicodedata

from .integrations.metadata import RawgProvider, SteamGridDbProvider
from .integrations.steam_store import SteamStoreProvider


def normalized(title):
    title = re.sub(r'\([^)]*\)|\[[^]]*\]', ' ', title)
    title = ''.join(c for c in unicodedata.normalize('NFKD', title.casefold()) if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[a-z0-9]+', title))


def best_match(title, platform, results):
    query = normalized(title)
    ranked = []
    for result in results:
        if result.platforms and platform:
            requested = normalized(platform)
            aliases = {'gba': 'game boy advance', 'snes': 'super nintendo',
                       'nes': 'nintendo entertainment system', 'pc': 'pc'}
            requested = aliases.get(requested, requested)
            available = [aliases.get(normalized(p), normalized(p)) for p in result.platforms]
            if not any(requested in p or p in requested for p in available):
                continue
        name = normalized(result.title)
        # Nomes próximos de sequências não representam o mesmo jogo.
        sequel = r'\b(?:\d+|ii|iii|iv|vi|vii|viii|ix|xi|xii)\b'
        if re.findall(sequel, query) != re.findall(sequel, name):
            continue
        score = SequenceMatcher(None, query, name).ratio()
        if query == name:
            score = 1.0
        ranked.append((score, result))
    ranked.sort(key=lambda item: item[0], reverse=True)
    if not ranked or ranked[0][0] < .88:
        return None
    if len(ranked) > 1 and ranked[0][0] - ranked[1][0] < .06:
        return None
    return ranked[0][1]


def resolve_title(title, platform='', providers=None):
    if providers is None:
        from .credentials import CredentialVault
        providers = []
        if normalized(platform) in ('', 'pc', 'windows'):
            providers.append(SteamStoreProvider())
        # Credenciais já configuradas no app; nunca solicitar uma chave por jogo.
        for name, factory in (('rawg', RawgProvider), ('steamgriddb', SteamGridDbProvider)):
            try:
                key = CredentialVault().get(name)
                if key:
                    providers.append(factory(key))
            except Exception:
                continue
    matches = []
    for provider in providers:
        try:
            query = re.sub(r'\([^)]*\)|\[[^]]*\]', ' ', title).strip()
            match = best_match(title, platform, provider.search(query))
            if match:
                if hasattr(provider, 'details'):
                    details = provider.details(match.external_id)
                    if details.provider != match.provider or details.external_id != match.external_id:
                        continue
                    match = details
                matches.append(match)
                # AppID Steam já fornece ficha/imagens; SteamGridDB é complemento opcional.
                if match.provider == 'steam':
                    return match
        except Exception:
            continue
    if not matches:
        return None
    primary = next((item for item in matches if item.provider == 'rawg'), matches[0])
    # Somente combinar provedores que retornaram o mesmo título, sem fundir edições.
    identities = {item.provider: item.external_id for item in matches
                  if normalized(item.title) == normalized(primary.title)}
    return replace(primary, identifiers=identities)

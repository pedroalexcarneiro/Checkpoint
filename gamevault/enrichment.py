"""Completa somente campos vazios de identidades confirmadas, sem buscar por nome."""
import hashlib
from pathlib import Path
from urllib.parse import urlsplit

from .integrations import IntegrationError
from .integrations.images import ImageCache
from .integrations.steam_store import SteamStoreProvider
from .library import now



def replaceable_steam_header(library,game,identity):
    asset=library.sql.execute("SELECT * FROM artwork_assets WHERE game_id=? AND kind='banner'",(game['id'],)).fetchone()
    if not asset or asset['provider']!='steam' or asset['external_id']!=identity or asset['local_path']!=game['banner']:
        return False
    parsed=urlsplit(asset['source_url'])
    if not (parsed.hostname or '').endswith('.steamstatic.com') or not Path(parsed.path).name.lower().startswith('header'):
        return False
    try:return hashlib.sha256(Path(game['banner']).read_bytes()).hexdigest()==asset['sha256']
    except OSError:return False


def complete_game(library, game_id, steam_provider=None, rawg_provider=None, cache=None, descriptions=None, art_provider=None):
    live=steam_provider is None and rawg_provider is None and art_provider is None
    game = library.get(game_id)
    if not game:
        return 'Jogo indisponível; cadastro preservado.'
    identities = dict(library.sql.execute(
        'SELECT provider,external_id FROM external_identifiers WHERE game_id=?', (game_id,)))
    if not identities:
        return 'Ficha pendente: confirme o jogo no catálogo. Nenhuma associação por nome foi feita.'
    cache = cache or ImageCache(library.db.path.parent / 'images')
    sources = []
    if 'steam' in identities:
        sources.append(('steam', steam_provider or SteamStoreProvider()))
    if 'rawg' in identities:
        if rawg_provider is None:
            try:
                from .credentials import CredentialVault
                from .integrations.metadata import RawgProvider
                rawg_provider = RawgProvider(CredentialVault().get('rawg'))
            except Exception:
                pass
        if rawg_provider:
            sources.append(('rawg', rawg_provider))
    if not sources and 'steamgriddb' in identities:
        try:
            if art_provider is None:
                from .credentials import CredentialVault
                from .integrations.metadata import SteamGridDbProvider
                art_provider=SteamGridDbProvider(CredentialVault().get('steamgriddb'))
            sources.append(('steamgriddb',art_provider))
        except Exception:pass
    fields_saved = images_saved = failures = 0
    for source, provider in sources:
        try:
            result = provider.details(identities[source]) if hasattr(provider,'details') else provider.game_by_id(identities[source])
            if result.provider != source or result.external_id != identities[source]:
                raise IntegrationError('O provedor retornou outra identidade.')
            original_description=result.description
            if live or descriptions is not None:
                from .integrations.descriptions import localize_result
                result=localize_result(result,game['platform'],descriptions)
            from .description_provenance import current,record
            provenance=current(library,game)
            expected_description=''
            if game['description'] and result.description and result.description!=game['description']:
                if provenance and provenance.get('language')=='en':expected_description=game['description']
                elif source=='rawg' and original_description==game['description']:expected_description=game['description']
                elif source=='steam' and isinstance(provider,SteamStoreProvider):
                    # Legado sem proveniência: só substitui se ainda for exatamente o texto da fonte inglesa.
                    try:
                        english=provider.details(identities[source],language='english')
                        if english.description==game['description']:expected_description=game['description']
                    except IntegrationError:pass
            values = {'description': result.description, 'genre': ', '.join(result.genres),
                      'developer': result.developer, 'publisher': result.publisher,
                      'release_date': result.release_date}
            # Identidade e campo são conferidos no UPDATE para preservar edições concorrentes.
            with library.sql:
                for field, value in values.items():
                    if value:
                        cursor = library.sql.execute(
                            f"UPDATE games SET {field}=?,updated_at=? WHERE id=? AND {field}=? "
                            "AND deleted_at IS NULL AND EXISTS (SELECT 1 FROM external_identifiers "
                            "WHERE game_id=games.id AND provider=? AND external_id=?)",
                            (value, now(), game_id, expected_description if field=='description' else '', source, result.external_id))
                        fields_saved += cursor.rowcount
                record(library,game_id,result)
            for kind, url in result.images.items():
                if kind not in ('cover', 'banner', 'logo'):
                    continue
                current = library.get(game_id)
                if not current:continue
                upgrade=source=='steam' and kind=='banner' and 'library_hero' in url and bool(current[kind]) and replaceable_steam_header(library,current,result.external_id)
                if current[kind] and not upgrade:continue
                expected=current[kind]
                candidates=[url] if upgrade else [url,*result.image_candidates.get(kind,[])]
                try:
                    path=None
                    for candidate in candidates:
                        try:path=cache.download(candidate);url=candidate;break
                        except (IntegrationError,OSError,ValueError):continue
                    if not path:raise IntegrationError('Nenhuma imagem disponível para este tipo.')
                    digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
                    with library.sql:
                        cursor = library.sql.execute(
                            f"UPDATE games SET {kind}=?,updated_at=? WHERE id=? AND {kind}=? "
                            "AND deleted_at IS NULL AND EXISTS (SELECT 1 FROM external_identifiers "
                            "WHERE game_id=games.id AND provider=? AND external_id=?) "
                            "AND (?=0 OR EXISTS (SELECT 1 FROM artwork_assets WHERE game_id=games.id "
                            "AND kind='banner' AND provider='steam' AND local_path=?))",
                            (path, now(), game_id, expected, source, result.external_id, int(upgrade), expected))
                        if cursor.rowcount:
                            library.sql.execute('INSERT INTO artwork_assets VALUES(?,?,?,?,?,?,?,?) '
                                'ON CONFLICT(game_id,kind) DO UPDATE SET provider=excluded.provider,'
                                'external_id=excluded.external_id,source_url=excluded.source_url,'
                                'local_path=excluded.local_path,sha256=excluded.sha256,fetched_at=excluded.fetched_at',
                                (game_id, kind, source, result.external_id, url, path, digest, now()))
                            images_saved += 1
                except (IntegrationError, OSError, ValueError):
                    failures += 1
        except Exception:
            failures += 1
    if not sources:
        return 'Ficha pendente: fonte de descrição indisponível. Identidade e dados existentes preservados.'
    return f'Ficha: {fields_saved} campos e {images_saved} imagens preenchidos; {failures} consultas indisponíveis. Campos existentes preservados.'

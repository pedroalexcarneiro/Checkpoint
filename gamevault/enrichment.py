"""Completa somente campos vazios de identidades confirmadas, sem buscar por nome."""
import hashlib
from pathlib import Path

from .integrations import IntegrationError
from .integrations.images import ImageCache
from .integrations.steam_store import SteamStoreProvider
from .library import now


def complete_game(library, game_id, steam_provider=None, rawg_provider=None, cache=None):
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
    fields_saved = images_saved = failures = 0
    for source, provider in sources:
        try:
            result = provider.details(identities[source])
            if result.provider != source or result.external_id != identities[source]:
                raise IntegrationError('O provedor retornou outra identidade.')
            values = {'description': result.description, 'genre': ', '.join(result.genres),
                      'developer': result.developer, 'publisher': result.publisher,
                      'release_date': result.release_date}
            # Identidade e campo são conferidos no UPDATE para preservar edições concorrentes.
            with library.sql:
                for field, value in values.items():
                    if value:
                        cursor = library.sql.execute(
                            f"UPDATE games SET {field}=?,updated_at=? WHERE id=? AND {field}='' "
                            "AND deleted_at IS NULL AND EXISTS (SELECT 1 FROM external_identifiers "
                            "WHERE game_id=games.id AND provider=? AND external_id=?)",
                            (value, now(), game_id, source, result.external_id))
                        fields_saved += cursor.rowcount
            for kind, url in result.images.items():
                if kind not in ('cover', 'banner', 'logo'):
                    continue
                current = library.get(game_id)
                if not current or current[kind]:
                    continue
                try:
                    path = cache.download(url)
                    digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
                    with library.sql:
                        cursor = library.sql.execute(
                            f"UPDATE games SET {kind}=?,updated_at=? WHERE id=? AND {kind}='' "
                            "AND deleted_at IS NULL AND EXISTS (SELECT 1 FROM external_identifiers "
                            "WHERE game_id=games.id AND provider=? AND external_id=?)",
                            (path, now(), game_id, source, result.external_id))
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
        return 'Ficha pendente: selecione Steam ou RAWG no catálogo para obter dados detalhados.'
    return f'Ficha: {fields_saved} campos e {images_saved} imagens preenchidos; {failures} consultas indisponíveis. Campos existentes preservados.'

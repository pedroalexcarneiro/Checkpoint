from unittest.mock import Mock
import pytest
from gamevault.enrichment import complete_game
from gamevault.integrations import IntegrationError, MetadataResult
from gamevault.integrations.steam_store import SteamStoreProvider
from gamevault.game_import import save_import


class Cache:
    def __init__(self, folder):
        self.folder = folder
    def download(self, url):
        path = self.folder / (url.rsplit('/', 1)[-1] + '.png')
        path.write_bytes(b'image-content')
        return str(path)


def provider_result():
    return MetadataResult('steam', '304430', 'INSIDE', description='Description',
                          genres=('Adventure',), developer='Playdead', publisher='Playdead',
                          release_date='2016-07-07', images={'cover': 'https://example/cover',
                                                          'banner': 'https://example/banner'})


def test_steam_details_validate_appid_and_parse_fields():
    http = Mock()
    http.json.return_value = {'304430': {'success': True, 'data': {
        'steam_appid': 304430, 'name': 'INSIDE', 'short_description': '<b>Description</b>',
        'developers': ['Playdead'], 'publishers': ['Playdead'],
        'genres': [{'description': 'Adventure'}],
        'release_date': {'date': '7 Jul, 2016', 'coming_soon': False},
        'header_image': 'https://shared.akamai.steamstatic.com/header.jpg'}}}
    result = SteamStoreProvider(http).details('304430')
    assert result.developer == 'Playdead' and result.release_date == '2016-07-07'
    assert result.genres == ('Adventure',) and result.description == 'Description'
    assert '/304430/' in result.images['cover']
    assert 'key=' not in http.json.call_args.args[0]
    http.json.return_value['304430']['data']['steam_appid'] = 999
    with pytest.raises(IntegrationError): SteamStoreProvider(http).details('304430')
    with pytest.raises(ValueError): SteamStoreProvider(http).details('../bad')


def test_fill_missing_preserves_personal_values_and_tracks_images(library, folder):
    result = provider_result()
    identity = save_import(library, {'title': 'Meu título', 'developer': 'Minha escolha',
        'notes': 'Pessoal', 'status': 'Jogando', 'cover': 'manual.png'}, result=result)
    provider = Mock(); provider.details.return_value = result
    message = complete_game(library, identity, steam_provider=provider, cache=Cache(folder))
    game = library.get(identity)
    assert game['title'] == 'Meu título' and game['developer'] == 'Minha escolha'
    assert game['notes'] == 'Pessoal' and game['status'] == 'Jogando'
    assert game['genre'] == 'Adventure' and game['publisher'] == 'Playdead'
    assert game['cover'] == 'manual.png' and game['banner']
    asset = library.sql.execute('SELECT * FROM artwork_assets').fetchone()
    assert asset['provider'] == 'steam' and len(asset['sha256']) == 64
    assert '1 imagens' in message


def test_unknown_game_never_searches_by_name(library):
    identity = library.save_game({'title': 'Ambiguous'})
    provider = Mock()
    assert 'confirme' in complete_game(library, identity, steam_provider=provider)
    provider.details.assert_not_called()
    provider.search.assert_not_called()


def test_download_failure_keeps_metadata_and_game(library, folder):
    identity = save_import(library, {'title': 'INSIDE'}, result=provider_result())
    provider = Mock(); provider.details.return_value = provider_result()
    cache = Mock(); cache.download.side_effect = IntegrationError('Unavailable')
    assert '2 consultas indisponíveis' in complete_game(library, identity, steam_provider=provider, cache=cache)
    assert library.get(identity)['developer'] == 'Playdead'
    assert library.get(identity)['cover'] == ''


def test_concurrent_edit_during_download_is_preserved(library, folder):
    identity = save_import(library, {'title': 'INSIDE'}, result=provider_result())
    provider = Mock(); provider.details.return_value = provider_result()
    cache = Cache(folder)
    original = cache.download
    def download(url):
        with library.sql:
            library.sql.execute("UPDATE games SET cover='my-new-cover.png' WHERE id=?", (identity,))
        return original(url)
    cache.download = download
    complete_game(library, identity, steam_provider=provider, cache=cache)
    assert library.get(identity)['cover'] == 'my-new-cover.png'
    assert library.sql.execute("SELECT count(*) FROM artwork_assets WHERE kind='cover'").fetchone()[0] == 0


def test_wrong_identity_response_never_applied(library, folder):
    identity = save_import(library, {'title': 'INSIDE'}, result=provider_result())
    provider = Mock(); provider.details.return_value = MetadataResult('steam', '999', 'Other', developer='Wrong')
    complete_game(library, identity, steam_provider=provider, cache=Cache(folder))
    assert library.get(identity)['developer'] == ''


def test_rawg_confirmed_rom_uses_its_own_identity(library, folder):
    result = MetadataResult('rawg', '10', 'ROM', developer='Nintendo',
                            images={'cover': 'https://example/rom-cover', 'banner': 'https://example/rom-banner'})
    identity = save_import(library, {'title': 'ROM', 'platform': 'Game Boy Advance'}, result=result)
    provider = Mock(); provider.details.return_value = result
    complete_game(library, identity, rawg_provider=provider, cache=Cache(folder))
    provider.details.assert_called_once_with('10')
    assert library.get(identity)['developer'] == 'Nintendo'
    assert library.get(identity)['cover'] and library.get(identity)['banner']
    assert library.get(identity)['platform'] == 'Game Boy Advance'


def test_new_form_opens_catalog_on_save_and_can_save_offline(library, app, monkeypatch):
    from gamevault.dialogs import GameDialog
    from PySide6.QtWidgets import QDialog
    dialog = GameDialog(library=library)
    dialog.fields['title'].setText('INSIDE')
    called = []
    def choose():
        called.append(True); dialog.apply_catalog(provider_result())
    monkeypatch.setattr(dialog, 'lookup_catalog', choose)
    dialog.validate()
    assert called and dialog.result() == QDialog.Accepted
    assert dialog.data()['developer'] == 'Playdead'
    dialog.close()
    offline = GameDialog(library=library)
    offline.fields['title'].setText('Local game')
    offline.complete_on_save.setChecked(False)
    offline.validate()
    assert offline.result() == QDialog.Accepted
    offline.close()


def test_cancelled_identification_does_not_silently_save(library, app, monkeypatch):
    from gamevault.dialogs import GameDialog
    from PySide6.QtWidgets import QDialog
    dialog = GameDialog(library=library)
    dialog.fields['title'].setText('Unknown ROM')
    monkeypatch.setattr(dialog, 'lookup_catalog', lambda: None)
    dialog.validate()
    assert dialog.result() != QDialog.Accepted
    assert 'Confirme' in dialog.error.text()
    dialog.close()


def test_batch_cancellation_keeps_existing_library(library, app, monkeypatch):
    from gamevault.artwork_progress import ArtworkProgress
    identity = library.save_game({'title': 'Keep me'})
    obtain = Mock()
    monkeypatch.setattr('gamevault.auto_artwork.obtain_artwork', obtain)
    dialog = ArtworkProgress(library, [identity])
    dialog.cancel.click()
    dialog.exec()
    assert 'interrompida' in dialog.message
    assert library.get(identity)['title'] == 'Keep me'
    obtain.assert_not_called()

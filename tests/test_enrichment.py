from unittest.mock import Mock
import pytest
from checkpoint.enrichment import complete_game
from checkpoint.integrations import IntegrationError, MetadataResult
from checkpoint.integrations.steam_store import SteamStoreProvider
from checkpoint.game_import import save_import


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
    assert '1 imagem' in message


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


def test_form_saves_without_network_or_nested_loading_dialog(library, app, monkeypatch):
    from checkpoint.dialogs import GameDialog
    from PySide6.QtWidgets import QDialog
    nested=Mock(side_effect=AssertionError('Salvar não deve abrir outro loop modal'))
    monkeypatch.setattr(QDialog,'exec',nested)
    dialog=GameDialog(library=library)
    result=MetadataResult('steam','304430','INSIDE')
    dialog.apply_catalog(result);dialog.quick_add.show_result(result)
    assert dialog.complete_on_save.isChecked()
    dialog.validate()
    assert dialog.result()==QDialog.Accepted
    nested.assert_not_called()
    dialog.close()
    offline=GameDialog(library=library)
    result=MetadataResult('steam','1','Local game')
    offline.apply_catalog(result);offline.quick_add.show_result(result)
    offline.complete_on_save.setChecked(False)
    offline.validate()
    assert offline.result()==QDialog.Accepted
    offline.close()


def test_unknown_game_requires_selection(library, app):
    from checkpoint.dialogs import GameDialog
    from PySide6.QtWidgets import QDialog
    dialog=GameDialog(library=library)
    dialog.fields['title'].setText('Unknown ROM')
    dialog.validate()
    assert dialog.result()!=QDialog.Accepted
    assert not dialog.quick_add.save.isEnabled()
    assert dialog.error.text()
    assert dialog.catalog_result is None
    dialog.close()


def test_batch_cancellation_keeps_existing_library(library, app, monkeypatch):
    from checkpoint.artwork_progress import ArtworkProgress
    identity = library.save_game({'title': 'Keep me'})
    obtain = Mock()
    monkeypatch.setattr('checkpoint.worker.run_isolated', obtain)
    dialog = ArtworkProgress(library, [identity])
    dialog.cancel.click()
    dialog.exec()
    assert 'interrompida' in dialog.message
    assert library.get(identity)['title'] == 'Keep me'
    obtain.assert_not_called()


def steam_banner_result():
    return MetadataResult('steam','304430','INSIDE',
        images={'banner':'https://cdn.akamai.steamstatic.com/steam/apps/304430/library_hero.jpg'},
        image_candidates={'banner':['https://shared.akamai.steamstatic.com/steam/apps/304430/header.jpg']})


def automatic_header(library,folder):
    import hashlib
    path=folder/'header.png';path.write_bytes(b'original-header')
    identity=save_import(library,{'title':'INSIDE','banner':str(path)},result=provider_result())
    with library.sql:
        library.sql.execute('INSERT INTO artwork_assets VALUES(?,?,?,?,?,?,?,?)',
            (identity,'banner','steam','304430','https://shared.akamai.steamstatic.com/steam/apps/304430/header.jpg',str(path),hashlib.sha256(path.read_bytes()).hexdigest(),'2026-11-12'))
    return identity,path


def test_steam_header_is_fallback_after_library_hero(library,folder):
    identity=save_import(library,{'title':'INSIDE'},result=provider_result())
    provider=Mock();provider.details.return_value=steam_banner_result()
    cache=Cache(folder);original=cache.download;calls=[]
    def download(url):
        calls.append(url)
        if url.endswith('library_hero.jpg'):raise IntegrationError('Missing')
        return original(url)
    cache.download=download
    complete_game(library,identity,steam_provider=provider,cache=cache)
    assert calls[0].endswith('library_hero.jpg') and calls[1].endswith('header.jpg')
    assert library.get(identity)['banner']


def test_existing_automatic_header_upgrades_and_keeps_old_cache(library,folder):
    identity,old=automatic_header(library,folder)
    provider=Mock();provider.details.return_value=steam_banner_result()
    complete_game(library,identity,steam_provider=provider,cache=Cache(folder))
    assert library.get(identity)['banner']!=str(old) and old.read_bytes()==b'original-header'
    asset=library.sql.execute("SELECT * FROM artwork_assets WHERE game_id=? AND kind='banner'",(identity,)).fetchone()
    assert asset['source_url'].endswith('library_hero.jpg')


def test_missing_hero_does_not_replace_existing_header_with_another_header(library,folder):
    identity,old=automatic_header(library,folder)
    provider=Mock();provider.details.return_value=steam_banner_result()
    cache=Mock();cache.download.side_effect=IntegrationError('Missing')
    complete_game(library,identity,steam_provider=provider,cache=cache)
    cache.download.assert_called_once()
    assert cache.download.call_args.args[0].endswith('library_hero.jpg')
    assert library.get(identity)['banner']==str(old)


def test_modified_header_content_is_preserved_as_user_choice(library,folder):
    identity,old=automatic_header(library,folder);old.write_bytes(b'manually-modified')
    provider=Mock();provider.details.return_value=steam_banner_result();cache=Mock()
    complete_game(library,identity,steam_provider=provider,cache=cache)
    cache.download.assert_not_called()
    assert old.read_bytes()==b'manually-modified'


def test_manual_confirmation_during_header_download_wins(library,folder):
    identity,old=automatic_header(library,folder)
    provider=Mock();provider.details.return_value=steam_banner_result()
    cache=Cache(folder);download=cache.download
    def choose_manual(url):
        with library.sql:library.sql.execute("DELETE FROM artwork_assets WHERE game_id=? AND kind='banner'",(identity,))
        return download(url)
    cache.download=choose_manual
    complete_game(library,identity,steam_provider=provider,cache=cache)
    assert library.get(identity)['banner']==str(old)

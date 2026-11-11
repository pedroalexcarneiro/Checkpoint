from pathlib import Path
from unittest.mock import Mock
import pytest
from gamevault.auto_artwork import AutoArtwork,obtain_artwork
from gamevault.integrations import IntegrationError,MetadataResult
from gamevault.integrations.metadata import SteamGridDbProvider

class Provider:
    def __init__(self):self.calls=[]
    def artworks(self,external_id,kind):
        self.calls.append((external_id,kind));return ['https://cdn2.steamgriddb.com/'+kind+'.png']
    def game_from_steam(self,app_id):return MetadataResult('steamgriddb','42','Confirmed')
class Cache:
    def __init__(self,folder):self.folder=folder;self.calls=[]
    def download(self,url):
        self.calls.append(url);path=self.folder/url.rsplit('/',1)[-1];path.write_bytes(b'test-image');return str(path)


def configured(library,folder,**fields):
    game=library.save_game({'title':'Confirmed',**fields});provider=Provider();cache=Cache(folder)
    service=AutoArtwork(library,provider,cache,clock=lambda:100000)
    service.confirm_identity(game,'42')
    return game,provider,cache,service


def test_three_kinds_cached_with_provenance_and_no_redownload(library,folder):
    game,provider,cache,service=configured(library,folder)
    assert '3 artes' in service.obtain(game)
    assert all(library.get(game)[kind] for kind in ('cover','banner','logo'))
    rows=library.sql.execute('SELECT * FROM artwork_assets').fetchall()
    assert len(rows)==3 and all(len(row['sha256'])==64 for row in rows)
    assert 'já definidos' in service.obtain(game)
    assert len(cache.calls)==3


def test_unknown_identity_never_searches_or_guesses(library,folder):
    game=library.save_game({'title':'Ambiguous'});provider=Provider()
    assert 'aguardando identificação' in AutoArtwork(library,provider,Cache(folder)).obtain(game)
    assert provider.calls==[]


def test_preserves_manual_cover_and_fetches_other_kinds(library,folder):
    game,provider,cache,service=configured(library,folder,cover='manual.png')
    service.obtain(game)
    assert library.get(game)['cover']=='manual.png'
    assert [kind for _,kind in provider.calls]==['banner','logo']


def test_partial_failure_keeps_game_and_successful_art(library,folder):
    game,provider,cache,service=configured(library,folder)
    base=provider.artworks
    def broken(external_id,kind):
        if kind=='banner':raise IntegrationError('network')
        return base(external_id,kind)
    provider.artworks=broken
    assert '2 artes' in service.obtain(game)
    assert library.get(game)['banner']=='' and library.get(game)['cover']
    assert 'consulta recente' in service.obtain(game)


def test_changed_cover_during_download_is_not_overwritten(library,folder):
    game,provider,cache,service=configured(library,folder)
    base=cache.download
    def change(url):
        if url.endswith('cover.png'):
            item=library.get(game);item['cover']='user-new.png';library.save_game(item,game)
        return base(url)
    cache.download=change;service.obtain(game)
    assert library.get(game)['cover']=='user-new.png'
    assert library.sql.execute("SELECT count(*) FROM artwork_assets WHERE kind='cover'").fetchone()[0]==0


def test_identity_collision_is_rejected(library,folder):
    game,provider,cache,service=configured(library,folder)
    another=library.save_game({'title':'Another'})
    with pytest.raises(ValueError):service.confirm_identity(another,'42')
    assert service.identity(another) is None


def test_disabled_auto_and_manual_retry(library,folder):
    game,provider,cache,service=configured(library,folder)
    library.set_setting('artwork.auto',False)
    assert 'desativadas' in service.obtain(game) and provider.calls==[]
    assert '3 artes' in service.obtain(game,force=True)


def test_exact_steam_id_resolution_without_title_search(library,folder):
    game=library.save_game({'title':'Steam game'})
    with library.sql:library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(game,'steam','123'))
    service=AutoArtwork(library,Provider(),Cache(folder),clock=lambda:100000)
    assert '3 artes' in service.obtain(game)
    assert service.identity(game)[0]=='42'


def test_provider_steam_mapping_and_safe_art_ranking():
    http=Mock();http.json.return_value={'data':{'id':42,'name':'Game'}}
    provider=SteamGridDbProvider('test-key',http)
    assert provider.game_from_steam('123').external_id=='42'
    assert http.json.call_args.args[0].endswith('/games/steam/123')
    http.json.return_value={'data':[{'url':'safe-low','score':1},{'url':'nsfw','nsfw':True,'score':100},{'url':'safe-high','score':5},{'url':'animated','mime':'image/gif'}]}
    assert provider.artworks('42')==['safe-high','safe-low']
    with pytest.raises(ValueError):provider.game_from_steam('../bad')


def test_background_failure_does_not_raise_into_rom_operation(library,monkeypatch):
    monkeypatch.setattr(AutoArtwork,'obtain',Mock(side_effect=RuntimeError('secret')))
    assert 'preservados' in obtain_artwork(library,1)
    assert 'secret' not in obtain_artwork(library,1)


def test_missing_key_is_explicit_and_does_not_mutate_game(library,folder,monkeypatch):
    import gamevault.credentials
    game=library.save_game({'title':'Game'})
    service=AutoArtwork(library,cache=Cache(folder));service.confirm_identity(game,'42')
    vault=Mock();vault.get.return_value=None
    monkeypatch.setattr(gamevault.credentials,'CredentialVault',lambda:vault)
    assert 'Configure a chave' in service.obtain(game)
    assert library.get(game)['cover']==''


def test_identifying_dialog_has_automatic_action_and_preference(library,app):
    from gamevault.artwork_dialog import ArtworkDialog
    game=library.save_game({'title':'Game'})
    dialog=ArtworkDialog(library,library.get(game))
    assert dialog.identify.text().startswith('Confirmar jogo')
    dialog.auto.setChecked(False)
    assert library.setting('artwork.auto') is False
    dialog.close()


def test_confirmed_catalog_name_standardizes_display_title(library,folder):
    game,provider,cache,service=configured(library,folder)
    service.confirm_identity(game,'42','The Legend of Zelda: The Minish Cap')
    assert library.get(game)['title']=='The Legend of Zelda: The Minish Cap'

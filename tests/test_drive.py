import hashlib
import pytest
from gamevault.integrations.drive import DriveScanner,normalize_rom_name
from gamevault.integrations import IntegrationError

class FakeDrive:
    def __init__(self): self.downloads=0
    def start_token(self): return 'before-scan'
    def children(self,parent):
        return {'root':[{'id':'snes','name':'SNES','mimeType':'application/vnd.google-apps.folder'}],
            'snes':[{'id':'rom','name':'Game (USA).sfc','mimeType':'application/octet-stream','parents':['snes'],
                     'size':'3','md5Checksum':hashlib.md5(b'rom').hexdigest(),'modifiedTime':'2026-11-10'}]}[parent]
    def changes(self,token):
        return {'newStartPageToken':'after-scan','changes':[{'fileId':'rom','removed':True}]}
    def download(self,file_id,target): self.downloads+=1; target.write_bytes(b'rom')

def test_scan_never_downloads_and_keeps_versions(library,folder):
    client=FakeDrive(); scanner=DriveScanner(library,client)
    assert scanner.full_scan('root')==1
    assert client.downloads==0 and library.games()==[]
    file=dict(library.sql.execute('SELECT * FROM game_files').fetchone())
    assert file['platform']=='SNES' and file['original_name']=='Game (USA).sfc'
    assert library.setting('drive_scan')['token']=='before-scan'
    game=library.save_game({'title':'Game'})
    scanner.associate(file['id'],game)
    scanner.full_scan('root')
    assert library.sql.execute('SELECT count(*) FROM game_files').fetchone()[0]==1
    assert library.sql.execute('SELECT game_id FROM game_files').fetchone()[0]==game
    target=scanner.download(file['id'],folder/'downloads')
    assert target.read_bytes()==b'rom'
    with pytest.raises(ValueError): scanner.download(file['id'],folder/'downloads')
    scanner.incremental()
    assert target.exists()
    assert library.sql.execute('SELECT review_state FROM game_files').fetchone()[0]=='remote_removed'
    assert library.setting('drive_scan')['token']=='after-scan'

def test_failed_scan_does_not_advance_cursor(library):
    class Broken(FakeDrive):
        def children(self,parent): raise RuntimeError('network')
    with pytest.raises(RuntimeError): DriveScanner(library,Broken()).full_scan('root')
    assert library.setting('drive_scan') is None
    assert normalize_rom_name('Game_Name (USA) [Rev 1].sfc')=='Game Name'

def test_failed_download_not_available(library,folder):
    class Broken(FakeDrive):
        def download(self,file_id,target): target.write_bytes(b'bad')
    scanner=DriveScanner(library,Broken()); scanner.full_scan('root')
    file=library.sql.execute('SELECT id FROM game_files').fetchone()[0]
    with pytest.raises(IntegrationError): scanner.download(file,folder/'downloads')
    assert library.sql.execute('SELECT available FROM game_files').fetchone()[0]==0

def test_full_rescan_marks_missing_without_deleting_local(library,folder):
    client=FakeDrive(); scanner=DriveScanner(library,client); scanner.full_scan('root')
    row=library.sql.execute('SELECT id FROM game_files').fetchone()
    target=scanner.download(row['id'],folder/'downloads')
    client.children=lambda parent:[]
    scanner.full_scan('root')
    assert library.sql.execute('SELECT review_state FROM game_files').fetchone()[0]=='remote_missing'
    assert target.exists()


@pytest.mark.parametrize('path,expected', [
 ('/Nintendo Game Boy Advanced/Pokémon','Game Boy Advance'),
 ('/Super Nintendo (SNES)/Extras','SNES'),
 ('/  super_nintendo (snes) /Extras','SNES'),
 ('/Switch','Nintendo Switch'),
 ('/Nintendo DS/MelonDS','Nintendo DS'),
 ('/Temas',''),
 ('/Switch Games',''),
 ('/Nintendo DS/PSP',''),
 (r'C:\ROMs\Nintendo 3DS','Nintendo 3DS'),
])
def test_folder_platform_aliases(path,expected):
    from gamevault.integrations.drive import platform_for
    assert platform_for(path)==expected


def test_reclassification_preserves_existing_metadata(library):
    scanner=DriveScanner(library,None)
    scanner.record({'id':'gba','name':'Game.zip','mimeType':'application/octet-stream'},'/Nintendo Game Boy Advanced')
    library.sql.execute("UPDATE game_files SET platform='' WHERE drive_id='gba'")
    scanner.record({'id':'manual','name':'Other.zip','mimeType':'application/octet-stream'},'/Switch')
    library.sql.execute("UPDATE game_files SET platform='Personalizada' WHERE drive_id='manual'")
    library.sql.commit()
    before=[tuple(r) for r in library.sql.execute('SELECT id,drive_id,original_name,game_id,available FROM game_files ORDER BY id')]
    assert scanner.recognize_platforms()==1
    assert scanner.recognize_platforms()==0
    assert library.sql.execute("SELECT platform FROM game_files WHERE drive_id='gba'").fetchone()[0]=='Game Boy Advance'
    assert library.sql.execute("SELECT platform FROM game_files WHERE drive_id='manual'").fetchone()[0]=='Personalizada'
    assert [tuple(r) for r in library.sql.execute('SELECT id,drive_id,original_name,game_id,available FROM game_files ORDER BY id')]==before


def test_root_themes_are_not_roms(library):
    scanner=DriveScanner(library,None)
    assert scanner.record({'id':'theme','name':'Theme.zip','mimeType':'application/octet-stream'},'/Temas')==0
    assert library.sql.execute('SELECT count(*) FROM game_files').fetchone()[0]==0
    class WithThemes(FakeDrive):
        def children(self,parent):
            if parent=='root':
                return [{'id':'themes','name':'Temas','mimeType':'application/vnd.google-apps.folder'}]
            raise AssertionError('Não deve percorrer a pasta de temas')
    assert DriveScanner(library,WithThemes()).full_scan('root')==0

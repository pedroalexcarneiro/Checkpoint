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

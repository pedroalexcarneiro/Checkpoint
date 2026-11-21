"""Downloads verificáveis, nomes reconhecíveis e recuperação sem sobrescrita."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import sqlite3
import pytest
from checkpoint.integrations.drive import DriveScanner,GoogleDriveClient
from checkpoint.integrations import IntegrationError
from checkpoint.transfer_progress import TransferCancelled,TransferProgress
from checkpoint.transfer_files import windows_name


def indexed(library, name='Aventura com ação.NSP', content=b'ROM de teste'):
    scanner=DriveScanner(library,None)
    scanner.record({'id':'download-fixture','name':name,'size':str(len(content)),
                    'md5Checksum':hashlib.md5(content,usedforsecurity=False).hexdigest()},'/Switch')
    library.sql.commit()
    row=dict(library.sql.execute('SELECT * FROM game_files').fetchone())
    return scanner,row,content


def test_original_name_and_collisions_preserve_existing_file(library,folder):
    scanner,row,data=indexed(library)
    target=folder/'downloads';target.mkdir()
    existing=target/row['original_name'];existing.write_bytes(b'arquivo original')
    class Client:
        def download(self, identity, path):path.write_bytes(data)
    scanner.client=Client()
    downloaded=scanner.download(row['id'],target)
    assert downloaded.name=='Aventura com ação (2).NSP'
    assert existing.read_bytes()==b'arquivo original'
    assert downloaded.read_bytes()==data
    with pytest.raises(ValueError):scanner.download(row['id'],target)
    assert len(list(target.glob('*.NSP')))==2


@pytest.mark.parametrize('name', ['arquivo../teste:ação?.gba','CON.gba','CON.foo.gba','AUX.txt','Jogo grande '+('á'*260)+'.nsp'])
def test_windows_sanitization_keeps_extension_and_avoids_invalid_name(name):
    value=windows_name(name)
    assert not any(c in value for c in '<>:"/\\|?*')
    assert not value.endswith((' ','.'))
    assert len(value.encode('utf-16-le'))<=510
    assert Path(value).suffix==Path(name).suffix
    assert value.upper().split('.')[0] not in {'CON','AUX'}


def test_valid_long_name_is_preserved_and_collision_keeps_suffix(library,folder):
    from checkpoint.transfer_files import free_destination
    name='a'*246+'.nsp'
    assert windows_name(name)==name
    original=folder/name;original.write_bytes(b'original')
    alternate=free_destination(folder,name)
    assert alternate.name.endswith(' (2).nsp')
    assert len(alternate.name.encode('utf-16-le'))<=510


def test_sdk_reports_actual_bytes_and_cooperative_cancel(library,folder,monkeypatch):
    scanner,row,data=indexed(library,content=b'123456789')
    cancelled=[False];events=[]
    class SDK:
        def __init__(self, stream, request, **kwargs):self.stream=stream;self.part=0
        def next_chunk(self, **kwargs):
            self.stream.write(b'123');self.part+=1
            return SimpleNamespace(total_size=9),self.part==3
    monkeypatch.setattr('googleapiclient.http.MediaIoBaseDownload',SDK)
    service=SimpleNamespace(files=lambda:SimpleNamespace(get_media=lambda **kwargs:object()))
    client=GoogleDriveClient(service)
    def update(event):events.append(event);cancelled[0]=True
    path=folder/'cancelled.partial'
    with pytest.raises(TransferCancelled):client.download('download-fixture',path,progress=update,cancel=lambda:cancelled[0])
    assert path.read_bytes()==b'123'
    assert events[0]['received']==3 and events[0]['total']==9


def test_cancel_never_promotes_partial(library,folder):
    scanner,row,data=indexed(library)
    cancelled=[False]
    class Client:
        def download(self, identity, path, **kwargs):
            path.write_bytes(b'partial');cancelled[0]=True
    scanner.client=Client()
    with pytest.raises(TransferCancelled):scanner.download(row['id'],folder/'downloads',cancel=lambda:cancelled[0])
    assert library.sql.execute('SELECT available FROM game_files').fetchone()[0]==0
    assert list((folder/'downloads').glob('*.partial'))
    assert not list((folder/'downloads').glob('*.NSP'))


def test_completed_download_journal_recovers_after_database_failure(library,folder):
    scanner,row,data=indexed(library)
    calls=[]
    class Client:
        def download(self, identity, path):calls.append(identity);path.write_bytes(data)
    scanner.client=Client();real=library.sql
    class FailAvailability:
        def __enter__(self):real.__enter__();return self
        def __exit__(self,*args):return real.__exit__(*args)
        def execute(self,sql,*args):
            if sql.startswith('UPDATE game_files SET local_path'):
                raise sqlite3.OperationalError('fixture: falha na confirmação')
            return real.execute(sql,*args)
    library.sql=FailAvailability()
    try:
        with pytest.raises(sqlite3.OperationalError):scanner.download(row['id'],folder/'downloads')
    finally:library.sql=real
    assert len(calls)==1
    assert library.setting(f'downloads.pending.{row["id"]}')
    result=scanner.download(row['id'],folder/'downloads')
    assert result.read_bytes()==data
    assert len(calls)==1
    assert library.sql.execute('SELECT available FROM game_files').fetchone()[0]==1
    assert not library.setting(f'downloads.pending.{row["id"]}')


def test_unknown_size_has_no_invented_percentage(folder):
    progress=TransferProgress(folder/'progress.json')
    progress.report({'stage':'downloading','received':100,'total':None})
    assert progress.snapshot['percent'] is None
    assert progress.snapshot['eta_seconds'] is None


def test_remote_change_during_download_never_marks_old_revision_available(library,folder):
    scanner,row,old=indexed(library)
    updated='ROM da revisão atual'.encode('utf-8')
    class Client:
        def download(self,identity,path):
            path.write_bytes(old)
            scanner.record({'id':identity,'name':row['original_name'],'size':str(len(updated)),
                            'md5Checksum':hashlib.md5(updated,usedforsecurity=False).hexdigest()},'/Switch')
            library.sql.commit()
    scanner.client=Client()
    with pytest.raises(ValueError,match='índice da ROM mudou'):
        scanner.download(row['id'],folder)
    changed=library.sql.execute('SELECT * FROM game_files').fetchone()
    assert changed['size']==len(updated) and changed['available']==0
    original=folder/row['original_name'];assert original.read_bytes()==old
    scanner.client=SimpleNamespace(download=lambda identity,path:path.write_bytes(updated))
    result=scanner.download(row['id'],folder)
    assert result!=original and result.read_bytes()==updated and original.read_bytes()==old


def test_speed_and_eta_require_consistent_observed_progress(monkeypatch):
    clock=[0.0]
    monkeypatch.setattr('checkpoint.transfer_progress.time.monotonic',lambda:clock[0])
    progress=TransferProgress()
    progress.report({'stage':'downloading','received':0,'total':100})
    for received in (20,40,60):
        clock[0]+=2
        progress.report({'stage':'downloading','received':received,'total':100})
    assert progress.snapshot['percent']==60
    assert progress.snapshot['bytes_per_second']==10
    assert progress.snapshot['eta_seconds']==4
    clock[0]+=1
    progress.report({'stage':'downloading','received':99,'total':100})
    assert progress.snapshot['eta_seconds'] is None

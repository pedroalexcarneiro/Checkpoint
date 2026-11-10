import io
import hashlib
import zipfile
from pathlib import Path
import pytest
from gamevault.updates import select_update,GitHubUpdates,UpdateError
from gamevault.update_installer import extract_package,swap_install

def asset_release(tag='v0.1.4',preview=False):
    return {'tag_name':tag,'prerelease':preview,'assets':[{'name':'Checkpoint-'+tag[1:]+'-windows-x64.zip','state':'uploaded','id':1,'size':10,'digest':'sha256:'+'a'*64}]}

def test_versions_skip_old_drafts_previews_and_unverified_assets():
    candidates=[asset_release('v0.1.2'),asset_release('v0.1.4',True),asset_release('v0.1.3')]
    assert select_update(candidates,'0.1.2')['tag']=='v0.1.3'
    assert select_update(candidates,'0.1.3',True)['tag']=='v0.1.4'
    assert select_update(candidates,'0.1.4',True) is None
    candidate=asset_release(); candidate['assets'][0]['digest']=None
    assert select_update([candidate],'0.1.3') is None
    candidate=asset_release(); candidate['draft']=True
    assert select_update([candidate],'0.1.3') is None

def package(path,name='Checkpoint/Checkpoint.exe',content=b'new'):
    with zipfile.ZipFile(path,'w') as archive: archive.writestr(name,content)
    return path

def test_extract_and_swap_preserves_previous(folder):
    archive=package(folder/'package.zip')
    staged=extract_package(archive,folder/'staged')
    old=folder/'Checkpoint'; old.mkdir(); (old/'Checkpoint.exe').write_bytes(b'old')
    previous=swap_install(old,staged)
    assert (old/'Checkpoint.exe').read_bytes()==b'new'
    assert (previous/'Checkpoint.exe').read_bytes()==b'old'

@pytest.mark.parametrize('name',['../outside.exe','Checkpoint/../outside.exe','C:/outside.exe','Checkpoint/file.txt:ads','Checkpoint/CON.txt'])
def test_unsafe_archives_rejected(folder,name):
    archive=package(folder/'package.zip',name)
    with pytest.raises(ValueError): extract_package(archive,folder/'staged')
    assert not (folder/'outside.exe').exists()

def test_copy_failure_rolls_back(folder,monkeypatch):
    import gamevault.update_installer as module
    old=folder/'Checkpoint'; old.mkdir(); (old/'Checkpoint.exe').write_bytes(b'old')
    staged=folder/'staged'; staged.mkdir(); (staged/'Checkpoint.exe').write_bytes(b'new')
    def broken(source,target):
        Path(target).mkdir(); (Path(target)/'partial').write_bytes(b'x'); raise OSError('disk full')
    monkeypatch.setattr(module.shutil,'copytree',broken)
    with pytest.raises(OSError): swap_install(old,staged)
    assert (old/'Checkpoint.exe').read_bytes()==b'old'
    assert list(folder.glob('Checkpoint.failed-*'))

class Response:
    def __init__(self,code,data=b'',headers=None): self.status_code=code; self.data=data; self.headers=headers or {}; self.raw=io.BytesIO(data)
    def __enter__(self): return self
    def __exit__(self,*args): self.close()
    def close(self): pass
    def iter_content(self,size): yield self.data

def test_private_download_strips_token_on_cdn_and_verifies(folder,monkeypatch):
    import gamevault.updates as module
    data=package(folder/'source.zip').read_bytes(); calls=[]
    def get(url,**kwargs):
        calls.append((url,kwargs))
        if len(calls)==1: return Response(302,headers={'Location':'https://release-assets.githubusercontent.com/package'})
        return Response(200,data)
    monkeypatch.setattr(module.requests,'get',get)
    info={'asset_id':1,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    staged=GitHubUpdates('test-token').prepare(info,folder/'updates')
    assert (Path(staged)/'Checkpoint.exe').read_bytes()==b'new'
    assert calls[0][1]['headers']['Authorization']=='Bearer test-token'
    assert 'headers' not in calls[1][1]

def test_corrupt_download_never_extracts(folder,monkeypatch):
    import gamevault.updates as module
    monkeypatch.setattr(module.requests,'get',lambda *a,**k:Response(200,b'bad'))
    with pytest.raises(UpdateError): GitHubUpdates().prepare({'asset_id':1,'size':3,'sha256':'a'*64},folder/'updates')
    assert not list((folder/'updates').rglob('Checkpoint.exe'))
    assert not list((folder/'updates').rglob('*.partial'))

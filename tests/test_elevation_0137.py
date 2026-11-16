from pathlib import Path
import pytest


class Native:
    def __init__(self,admin=False,sid='owner',cancel=False):self.admin=admin;self.sid=sid;self.cancel=cancel;self.calls=[]
    def is_admin(self):return self.admin
    def user_sid(self):return self.sid
    def relaunch(self,exe,args,cwd):
        self.calls.append((exe,args,cwd))
        if self.cancel:
            from checkpoint.elevation import ElevationCancelled
            raise ElevationCancelled()


def test_uac_handoff_preserves_arguments_paths_and_original_identity(folder):
    from checkpoint.elevation import elevate_startup
    api=Native();data=folder/'Dados com acentuação';root=folder/'Perfil original'
    code=elevate_startup(['--data-dir',str(data),'--flag-com-espaço','Jogo Á'],executable='C:/Meu app/Checkpoint.exe',cwd=str(folder),local_root=root,api=api)
    assert code==0 and len(api.calls)==1
    exe,args,cwd=api.calls[0]
    assert exe=='C:/Meu app/Checkpoint.exe' and cwd==str(folder)
    assert args[:4]==['--data-dir',str(data.resolve()),'--flag-com-espaço','Jogo Á']
    assert args[args.index('--elevated-owner-sid')+1]=='owner'
    assert args[args.index('--elevated-data-root')+1]==str(root.resolve())
    assert not data.exists() and not root.exists()


def test_uac_cancel_and_other_account_never_retry_or_prepare_data(folder):
    from checkpoint.elevation import elevate_startup,ElevationCancelled
    api=Native(cancel=True)
    with pytest.raises(ElevationCancelled):elevate_startup([],executable='Checkpoint.exe',cwd=str(folder),local_root=folder,api=api)
    assert len(api.calls)==1
    for native in (Native(admin=True,sid='other'),Native(admin=False,sid='owner')):
        with pytest.raises(ValueError):elevate_startup([],executable='Checkpoint.exe',cwd=str(folder),local_root=folder,owner_sid='owner',api=native)
        assert native.calls==[]


def test_already_elevated_same_account_continues_without_new_prompt(folder):
    from checkpoint.elevation import elevate_startup
    api=Native(admin=True)
    assert elevate_startup([],executable='Checkpoint.exe',cwd=str(folder),local_root=folder,owner_sid='owner',api=api) is None
    assert not api.calls


@pytest.mark.parametrize('outcome',['handoff','cancel','different_account'])
def test_frozen_startup_handles_uac_before_opening_data(folder,outcome):
    import subprocess,sys,os
    code=r'''
import sys
from pathlib import Path
import checkpoint.app as entry
import checkpoint.elevation as elevation
import checkpoint.data_migration as migration
from PySide6.QtWidgets import QMessageBox
root=Path(sys.argv[1]);outcome=sys.argv[2];calls=[]
def forbidden(*args,**kwargs):raise AssertionError('Dados ou cofre abertos antes da decisão UAC')
migration.prepare_data_directory=forbidden
def handoff(*args,**kwargs):
    calls.append(kwargs)
    if outcome=='cancel':raise elevation.ElevationCancelled()
    if outcome=='different_account':raise ValueError('Conta diferente')
    return 0
elevation.elevate_startup=handoff
QMessageBox.information=lambda *args:None
QMessageBox.critical=lambda *args:None
sys.frozen=True;sys.platform='win32';sys.argv=['Checkpoint.exe','--data-dir',str(root)]
assert entry.main()==(2 if outcome=='different_account' else 0)
assert len(calls)==1 and not root.exists()
'''
    result=subprocess.run([sys.executable,'-c',code,str(folder/'dados-preservados'),outcome],cwd=Path(__file__).resolve().parents[1],env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
    assert result.returncode==0,result.stdout+result.stderr

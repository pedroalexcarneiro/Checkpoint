import os
from pathlib import Path
import subprocess
import sys
import pytest


@pytest.mark.parametrize('custom_directory',[False,True])
def test_frozen_user_variant_reaches_current_user_data_without_elevation(folder,custom_directory):
    code=r'''
import sys
from pathlib import Path
import checkpoint.app as entry
import checkpoint.elevation as elevation
import checkpoint.data_migration as migration
root=Path(sys.argv[1]);custom=sys.argv[2]=='True';seen=[]
class ReachedData(Exception):pass
def forbidden(*args,**kwargs):raise AssertionError('Variante de usuário tentou solicitar elevação')
def prepare(path,**kwargs):
    seen.append((path,kwargs));raise ReachedData()
elevation.elevate_startup=forbidden
migration.prepare_data_directory=prepare
sys.platform='win32';sys.frozen=True
sys.argv=['Checkpoint.exe']+(['--data-dir',str(root)] if custom else [])
try:entry.main(request_elevation=False)
except ReachedData:pass
else:raise AssertionError('A inicialização não chegou aos dados')
assert len(seen)==1 and seen[0][0]==(root if custom else None)
assert seen[0][1]['local_root'] is None
assert seen[0][1]['migrate_credentials'] is True
assert not root.exists()
'''
    result=subprocess.run([sys.executable,'-c',code,str(folder/'Dados do usuário'),str(custom_directory)],cwd=Path(__file__).resolve().parents[1],env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=20)
    assert result.returncode==0,result.stdout+result.stderr

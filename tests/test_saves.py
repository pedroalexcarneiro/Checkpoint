import hashlib
import json
import zipfile
import pytest
from gamevault.saves import SaveBackupService,digest

def test_backup_restore_preserves_previous_and_ignores_states(folder):
    source=folder/'saves'; source.mkdir(); (source/'game.sav').write_bytes(b'original')
    (source/'game.state').write_bytes(b'not a traditional save')
    service=SaveBackupService(folder/'backups')
    archive,checksum,manifest=service.create(source,['*.sav','*.state'])
    assert list(manifest)==['game.sav']
    (source/'game.sav').write_bytes(b'newer')
    recovery=service.restore(archive,source,checksum)
    assert (source/'game.sav').read_bytes()==b'original'
    with zipfile.ZipFile(recovery) as previous: assert previous.read('game.sav')==b'newer'
    with pytest.raises(ValueError): service.restore(archive,source,'invalid')

def test_rejects_traversal_and_broad_patterns(folder):
    source=folder/'saves'; source.mkdir(); (source/'a.sav').write_text('data')
    service=SaveBackupService(folder/'backups')
    with pytest.raises(ValueError): service.create(source,['*'])
    bad=folder/'bad.zip'; content=b'attack'
    with zipfile.ZipFile(bad,'w') as archive:
        archive.writestr('../escape.sav',content)
        archive.writestr('gamevault-manifest.json',json.dumps({'files':{'../escape.sav':hashlib.sha256(content).hexdigest()}}))
    with pytest.raises(ValueError): service.restore(bad,source,digest(bad))
    assert not (folder/'escape.sav').exists()

import pytest
from checkpoint.game_saves import GameSaveBackups,run_save_operation
from checkpoint.save_profiles import SaveProfiles

def test_game_backup_worker_history_restore_and_profile_versions(library,folder):
    game=library.save_game({'title':'Saves'})
    source=folder/'progress'; source.mkdir(); save=source/'game.sav'; save.write_bytes(b'first')
    SaveProfiles(library).configure(game,source,['*.sav'])
    library.set_setting('save_backups',str(folder/'versions'))
    result=run_save_operation(library.db.path,game)
    history=GameSaveBackups(library).history(game)
    assert len(history)==1 and history[0]['id']==result['id']
    SaveProfiles(library).configure(game,source,['*.sav'])
    assert len(GameSaveBackups(library).history(game))==1
    save.write_bytes(b'second')
    recovery=run_save_operation(library.db.path,game,result['id'])
    assert save.read_bytes()==b'first'
    from pathlib import Path
    assert Path(recovery).exists()
    other=library.save_game({'title':'Other'})
    with pytest.raises(ValueError): run_save_operation(library.db.path,other,result['id'])

def test_missing_profile_or_destination_is_explicit(library,folder):
    game=library.save_game({'title':'Saves'})
    with pytest.raises(ValueError): GameSaveBackups(library).create(game)
    SaveProfiles(library).configure(game,folder,['*.sav'])
    with pytest.raises(ValueError): GameSaveBackups(library).create(game)

def test_changing_save_does_not_publish_backup(folder,monkeypatch):
    import checkpoint.saves as module
    source=folder/'progress'; source.mkdir(); save=source/'game.sav'; save.write_bytes(b'first')
    service=module.SaveBackupService(folder/'versions')
    monkeypatch.setattr(module.time,'sleep',lambda seconds:save.write_bytes(b'changed'))
    with pytest.raises(ValueError): service.create(source,['*.sav'])
    assert not list((folder/'versions').glob('*.zip'))
    assert not list((folder/'versions').glob('*.partial'))

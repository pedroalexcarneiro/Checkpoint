import json
from contextlib import closing
import sqlite3
from pathlib import Path
import pytest
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.credentials import CredentialVault,SERVICE
from checkpoint.data_migration import prepare_data_directory,MigrationError,LEGACY_PRODUCT,LEGACY_DATABASE,DATABASE_NAME,LEGACY_PALETTE


class MemoryVault:
    def __init__(self):self.values={};self.writes=[]
    def get_password(self,service,name):return self.values.get((service,name))
    def set_password(self,service,name,value):self.values[service,name]=value;self.writes.append((service,name))


@pytest.fixture(autouse=True)
def isolated_vault(monkeypatch):
    # Nenhum teste acessa o cofre do sistema, inclusive no runner Windows.
    monkeypatch.setattr('checkpoint.credentials.CredentialVault',lambda:CredentialVault(MemoryVault()))


def old_library(root):
    directory=root/LEGACY_PRODUCT;directory.mkdir()
    db=Database(directory/LEGACY_DATABASE);lib=Library(db)
    art=directory/'images'/'manual.png';art.parent.mkdir();art.write_bytes(b'image fixture')
    identity=lib.save_game({'title':'Jogo preservado','notes':'Minha nota','cover':str(art),'status':'Jogando'})
    lib.add_diary(identity,'Minha memória');lib.set_setting('appearance.theme',LEGACY_PALETTE);lib.set_setting('other.preference',{'keep':True})
    return directory,db,lib,identity


def test_first_open_copies_complete_library_and_wal_snapshot(folder):
    old,db,lib,identity=old_library(folder)
    assert db.connection.execute('PRAGMA journal_mode').fetchone()[0]=='wal'
    (old/'extra.txt').write_text('Preservar arquivo adicional')
    try:
        with prepare_data_directory(local_root=folder) as session:
            assert session.directory==folder/'Checkpoint'
            with closing(sqlite3.connect(session.directory/DATABASE_NAME)) as copy:
                assert copy.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
                assert copy.execute('PRAGMA user_version').fetchone()[0]==4
                assert copy.execute('SELECT notes FROM games WHERE id=?',(identity,)).fetchone()[0]=='Minha nota'
                assert copy.execute('SELECT text FROM diary_entries').fetchone()[0]=='Minha memória'
                assert Path(copy.execute('SELECT cover FROM games').fetchone()[0]).read_bytes()==b'image fixture'
            assert (session.directory/'extra.txt').read_text()=='Preservar arquivo adicional'
            assert not (session.directory/LEGACY_DATABASE).exists()
            assert old.is_dir() and (old/LEGACY_DATABASE).exists() and lib.get(identity)['notes']=='Minha nota'
    finally:db.close()


def test_first_open_without_legacy_creates_only_new_directory(folder):
    with prepare_data_directory(local_root=folder) as session:
        assert session.directory==folder/'Checkpoint' and session.directory.is_dir()
        assert not (folder/LEGACY_PRODUCT).exists()


def test_existing_new_directory_is_not_overwritten(folder):
    old,db,_,_=old_library(folder);db.close()
    destination=folder/'Checkpoint';destination.mkdir();new_db=Database(destination/DATABASE_NAME);Library(new_db).save_game({'title':'Já estava aqui'});new_db.close()
    with prepare_data_directory(local_root=folder) as session:
        with closing(sqlite3.connect(session.directory/DATABASE_NAME)) as copy:assert copy.execute('SELECT title FROM games').fetchone()[0]=='Já estava aqui'
    assert (old/LEGACY_DATABASE).exists()


def test_integrity_failure_never_publishes_or_opens_copied_database(folder,monkeypatch,caplog):
    old,db,_,_=old_library(folder);db.close()
    def fail(connection):raise ValueError('conteudo-privado-que-nao-deve-aparecer')
    monkeypatch.setattr('checkpoint.data_migration.verify_database',fail)
    with pytest.raises(MigrationError) as error:prepare_data_directory(local_root=folder)
    assert str(old) in error.value.user_message()
    assert not (folder/'Checkpoint').exists() and (old/LEGACY_DATABASE).exists()
    assert 'conteudo-privado' not in caplog.text and str(folder) not in caplog.text
    assert not list(folder.glob('.checkpoint-migration-*'))


def test_credentials_copy_without_overwriting_or_logging_values(folder,caplog):
    backend=MemoryVault();dummy='credencial-ficticia-apenas-em-memoria'
    backend.values[LEGACY_PRODUCT,'steam']=dummy;backend.values[LEGACY_PRODUCT,'rawg']='anterior-ficticia';backend.values[SERVICE,'rawg']='nova-ficticia'
    with prepare_data_directory(local_root=folder,vault_factory=lambda:CredentialVault(backend)):
        assert backend.values[SERVICE,'steam']==dummy
        assert backend.values[SERVICE,'rawg']=='nova-ficticia'
        assert backend.values[LEGACY_PRODUCT,'steam']==dummy
    assert dummy not in caplog.text
    assert not any(dummy.encode() in file.read_bytes() for file in folder.rglob('*') if file.is_file())
    backend.writes.clear()
    with prepare_data_directory(local_root=folder,vault_factory=lambda:CredentialVault(backend)):pass
    assert backend.writes==[]


def test_legacy_light_preference_becomes_default_without_losing_others(folder):
    _,db,_,_=old_library(folder);db.close()
    with prepare_data_directory(local_root=folder) as session:
        with closing(sqlite3.connect(session.directory/DATABASE_NAME)) as copy:
            preferences={key:json.loads(value) for key,value in copy.execute('SELECT key,value FROM settings')}
            assert preferences['appearance.theme']=='green' and preferences['other.preference']=={'keep':True}


def test_instance_lock_also_prevents_concurrent_migration(folder):
    _,db,_,_=old_library(folder);db.close()
    with prepare_data_directory(local_root=folder):
        with pytest.raises(MigrationError):prepare_data_directory(local_root=folder)
    with prepare_data_directory(local_root=folder):pass


def test_explicit_directory_never_uses_real_localappdata(folder,monkeypatch):
    unrelated=folder/'unrelated';monkeypatch.setenv('LOCALAPPDATA',str(unrelated))
    with prepare_data_directory(folder/'isolated') as session:assert session.directory==folder/'isolated'
    assert not unrelated.exists()


def test_corrupt_source_and_empty_existing_destination_are_preserved(folder):
    old=folder/LEGACY_PRODUCT;old.mkdir();source=old/LEGACY_DATABASE;source.write_bytes(b'corrupt database fixture')
    with pytest.raises(MigrationError):prepare_data_directory(local_root=folder)
    assert source.read_bytes()==b'corrupt database fixture' and not (folder/'Checkpoint').exists()
    (folder/'Checkpoint').mkdir()
    with pytest.raises(MigrationError):prepare_data_directory(local_root=folder)
    assert source.read_bytes()==b'corrupt database fixture'


def test_vault_failure_preserves_source_without_logging_error_payload(folder,caplog):
    old,db,_,_=old_library(folder);db.close()
    def unavailable():raise RuntimeError('dado-privado-ficticio')
    with pytest.raises(MigrationError):prepare_data_directory(local_root=folder,vault_factory=unavailable)
    assert (old/LEGACY_DATABASE).exists() and not (folder/'Checkpoint').exists()
    assert 'dado-privado-ficticio' not in caplog.text


def test_running_legacy_instance_blocks_copy(folder):
    from PySide6.QtCore import QLockFile
    old,db,_,_=old_library(folder);db.close()
    lock=QLockFile(str(old/(LEGACY_PRODUCT.lower()+'.lock')));assert lock.tryLock(0)
    try:
        with pytest.raises(MigrationError):prepare_data_directory(local_root=folder)
        assert not (folder/'Checkpoint').exists()
    finally:lock.unlock()


def test_regular_files_with_similar_names_are_not_discarded(folder):
    old,db,_,_=old_library(folder);db.close()
    (old/'TokenAdventure.gba').write_bytes(b'arquivo de teste sem credenciais')
    with prepare_data_directory(local_root=folder) as session:
        assert (session.directory/'TokenAdventure.gba').read_bytes()==b'arquivo de teste sem credenciais'

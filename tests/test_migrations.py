import sqlite3
from contextlib import closing
import pytest
from gamevault.database import Database,MIGRATIONS

def test_upgrade_v1_keeps_user_data(folder):
    path=folder/'v1.sqlite'
    with closing(sqlite3.connect(path)) as sql:
        sql.executescript(MIGRATIONS[0]+"\nPRAGMA user_version=1; INSERT INTO games(title) VALUES('Original');")
    db=Database(path)
    assert db.connection.execute('PRAGMA user_version').fetchone()[0]==len(MIGRATIONS)
    assert db.connection.execute('SELECT title FROM games').fetchone()[0]=='Original'
    assert db.connection.execute('SELECT count(*) FROM rom_catalog').fetchone()[0]==0
    db.close()

def test_newer_schema_refused_without_mutation(folder):
    path=folder/'future.sqlite'
    with closing(sqlite3.connect(path)) as sql: sql.execute('PRAGMA user_version=999')
    with pytest.raises(RuntimeError): Database(path)
    with closing(sqlite3.connect(path)) as sql: assert sql.execute('PRAGMA user_version').fetchone()[0]==999

def test_failed_migration_rolls_back_all_ddl(folder,monkeypatch):
    import gamevault.database as module
    path=folder/'rollback.sqlite'
    db=Database(path); db.close()
    monkeypatch.setattr(module,'MIGRATIONS',MIGRATIONS+["CREATE TABLE should_rollback(id INTEGER); INVALID SQL;"])
    with pytest.raises(sqlite3.OperationalError): Database(path)
    with closing(sqlite3.connect(path)) as sql:
        assert sql.execute('PRAGMA user_version').fetchone()[0]==len(MIGRATIONS)
        assert sql.execute("SELECT count(*) FROM sqlite_master WHERE name='should_rollback'").fetchone()[0]==0


def test_upgrade_v2_preserves_covers_and_ids(folder):
    path=folder/'v2.sqlite'
    with closing(sqlite3.connect(path)) as sql:
        sql.executescript(''.join(MIGRATIONS[:2])+"PRAGMA user_version=2; INSERT INTO games(title,cover) VALUES('Original','my-cover.png'); INSERT INTO external_identifiers VALUES(1,'steam','10');")
    db=Database(path)
    assert db.connection.execute('SELECT cover FROM games').fetchone()[0]=='my-cover.png'
    assert db.connection.execute('SELECT external_id FROM external_identifiers').fetchone()[0]=='10'
    assert db.connection.execute('SELECT count(*) FROM artwork_assets').fetchone()[0]==0
    backups=list((folder/'backups').glob('before-migration-v2-to-v3-*.sqlite'))
    assert len(backups)==1
    with closing(sqlite3.connect(backups[0])) as backup:
        assert backup.execute('PRAGMA user_version').fetchone()[0]==2
        assert backup.execute('SELECT cover FROM games').fetchone()[0]=='my-cover.png'
    db.close()

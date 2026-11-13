import sqlite3
from contextlib import closing
import pytest
from checkpoint.database import Database,MIGRATIONS
from checkpoint.library import STATUSES

def test_crud_persistence_filters_and_recovery(library):
    game=library.save_game({'title':'  Metroid  ','platform':'SNES','genre':'Aventura','favorite':1,'rating':9})
    assert library.get(game)['title']=='Metroid'
    assert len(library.games(search='troid',platform='SNES',favorite=True))==1
    library.save_game({'title':'Metroid','status':'Concluído'},game)
    assert library.get(game)['completed_at']
    library.delete(game)
    assert library.games()==[] and library.get(game) is None
    library.restore(game)
    assert len(library.games())==1
    reopened=Database(library.db.path)
    assert reopened.connection.execute('PRAGMA user_version').fetchone()[0]==len(MIGRATIONS)
    assert reopened.connection.execute('SELECT count(*) FROM games').fetchone()[0]==1
    reopened.close()

def test_validation_sql_and_literal_search(library):
    for data in [{'title':' '},{'title':'X','status':'invalid'},{'title':'X','rating':11}]:
        with pytest.raises(ValueError): library.save_game(data)
    library.save_game({'title':"Robert'); DROP TABLE games;--"})
    library.save_game({'title':'100% diversão'})
    assert len(library.games(search='%'))==1
    assert len(library.games())==2

def test_diary_settings_and_stats(library):
    game=library.save_game({'title':'Jogo','status':'Jogando'})
    with pytest.raises(ValueError): library.add_diary(game,'  ')
    library.add_diary(game,'Primeiro chefe vencido')
    assert library.diary(game)[0]['text']=='Primeiro chefe vencido'
    library.set_setting('downloads','D:/ROMs')
    assert library.setting('downloads')=='D:/ROMs'
    with library.sql:
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,duration_seconds) VALUES(?,?,'finished',3600)",(game,'2026-11-10'))
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,duration_seconds) VALUES(?,?,'interrupted',999)",(game,'2026-11-10'))
    assert library.stats()['seconds']==3600
    library.delete(game)
    assert library.stats()['seconds']==0

def test_database_backup_and_foreign_keys(library,folder):
    library.save_game({'title':'Persistido'})
    backup=folder/'backup.sqlite'; library.db.backup(backup)
    with closing(sqlite3.connect(backup)) as sql:
        assert sql.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
        assert sql.execute('SELECT title FROM games').fetchone()[0]=='Persistido'
    with pytest.raises(ValueError): library.db.backup(library.db.path)
    with pytest.raises(sqlite3.IntegrityError), library.sql:
        library.sql.execute("INSERT INTO diary_entries(game_id,created_at,text) VALUES(999,'x','x')")

def test_filter_individual_genre_from_imported_metadata(library):
    library.save_game({'title':'Multi gênero','genre':'Ação, Aventura'})
    assert len(library.games(genre='Aventura'))==1
    assert library.games(genre='Avent')==[]

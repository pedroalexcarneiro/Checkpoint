import pytest
from zoneinfo import ZoneInfo
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_daily_local_preserves_raw_utc(library,title):
 i=library.save_game({'title':title});raw='2026-11-15T00:30:00+00:00'
 with library.sql:library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,?,600,'finished')",(i,raw))
 assert library.stats(display_timezone=ZoneInfo('America/Sao_Paulo'))['daily']=={'2026-11-14':600}
 assert library.sql.execute('SELECT started_at FROM play_sessions WHERE game_id=?',(i,)).fetchone()[0]==raw

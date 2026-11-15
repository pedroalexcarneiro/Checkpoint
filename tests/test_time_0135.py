import pytest
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_combined_time_without_join_multiplication(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i)
 with w.library.sql:
  for seconds in (1800,1800):w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,duration_seconds) VALUES(?,'2026-11-10','finished',?)",(i,seconds))
  for account in ('76561198000000001','76561198000000002'):
   w.library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES(?,?,?,?,180,'2026-11-10')",(account,str(i),i,title))
 w.detail(i);app.processEvents()
 assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 4h00min'
 assert not w.detail_page.findChildren(QLabel,'steamPlaytime')
 from checkpoint.playtime import total_seconds,format_time
 assert total_seconds(w.library,i)==14400
 assert format_time(0)=='0h00min' and format_time(8159)=='2h15min'

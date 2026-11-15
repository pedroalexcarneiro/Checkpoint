import pytest
from types import SimpleNamespace
from test_bugs_0134 import ui,sample
from PySide6.QtGui import QPixmap
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_capture_belongs_to_launched_game(ui,folder,monkeypatch,title):
 from checkpoint.game_capture import capture_game
 w,i=ui;w.library.save_game({'title':title},i)
 monkeypatch.setattr(w,'isActiveWindow',lambda:True)
 w.launcher.active[1]=(SimpleNamespace(pid=123,poll=lambda:None),0,i,True)
 class Adapter:
  def foreground_pid(self):return 123
  def capture(self,pid):
   assert pid==123
   pix=QPixmap(200,100);pix.fill();return pix
 try:
  p=capture_game(w,Adapter())
  row=w.library.sql.execute('SELECT * FROM media_files WHERE game_id=?',(i,)).fetchone()
  assert row['kind']=='image' and row['path']==str(p) and p.is_file()
  monkeypatch.setattr(w,'isActiveWindow',lambda:False)
  second=capture_game(w,Adapter())
  assert second.is_file() and second!=p
  assert w.library.sql.execute("SELECT count(*) FROM media_files WHERE game_id=?",(i,)).fetchone()[0]==2
  w.launcher.active.clear();monkeypatch.setattr(w,'isActiveWindow',lambda:True)
  with pytest.raises(ValueError,match='Checkpoint'):capture_game(w,Adapter())
 finally:w.launcher.active.clear()

import pytest
from types import SimpleNamespace
from test_bugs_0134 import ui,sample
from PySide6.QtGui import QPixmap
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_capture_belongs_to_launched_game(ui,folder,monkeypatch,title):
 from checkpoint.game_capture import capture_game
 w,i=ui;w.library.save_game({'title':title},i)
 monkeypatch.setattr(w,'isActiveWindow',lambda:True)
 w.launcher.active[1]=(SimpleNamespace(pid=123),0,i,True)
 class Adapter:
  def capture(self,pid):
   assert pid==123
   pix=QPixmap(200,100);pix.fill();return pix
 try:
  p=capture_game(w,Adapter())
  row=w.library.sql.execute('SELECT * FROM media_files WHERE game_id=?',(i,)).fetchone()
  assert row['kind']=='image' and row['path']==str(p) and p.is_file()
  monkeypatch.setattr(w,'isActiveWindow',lambda:False)
  assert capture_game(w,Adapter()) is None
  w.launcher.active.clear();monkeypatch.setattr(w,'isActiveWindow',lambda:True)
  with pytest.raises(ValueError,match='Checkpoint'):capture_game(w,Adapter())
 finally:w.launcher.active.clear()

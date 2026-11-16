from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QInputDialog,QPushButton,QMessageBox
import pytest

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_empty_memory_goes_to_game_tab(ui,app,monkeypatch,title):
 w,i=ui;w.library.save_game({'title':title},i)
 monkeypatch.setattr('checkpoint.dialog_style.AppInputs.getItem',lambda *a:(title,True))
 w.memories();app.processEvents()
 assert any('anotação' in t.text() and 'Memórias' in t.text() for t in w.pages[3].findChildren(QLabel))
 next(b for b in w.pages[3].findChildren(QPushButton) if b.text()=='Biblioteca').click()
 assert w.current_game==i and w.detail_tabs.currentIndex()==2

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_memory_card_geometry_and_title(ui,app,folder,title):
 from checkpoint.collection_views import memory_card
 from PySide6.QtGui import QImage
 w,i=ui
 image=QImage(100,50,QImage.Format_RGB32);image.fill(0);p=folder/'capture.png';image.save(str(p))
 common={'id':1,'game_id':i,'title':title,'created_at':'2026-11-10','text':'Anotação','caption':'','path':str(p)}
 cards=[memory_card(w,{**common,'kind':kind}) for kind in ('diary','image')]
 try:
  for c in cards:c.resize(320,c.sizeHint().height());c.show()
  app.processEvents()
  assert cards[0].minimumHeight()==cards[1].minimumHeight()>=300
  for c in cards:assert any(b.text()==title for b in c.findChildren(QPushButton))
 finally:
  for c in cards:c.close();c.deleteLater()

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_delete_memory_requires_confirmation(ui,folder,monkeypatch,title):
 w,i=ui;w.library.save_game({'title':title},i)
 w.library.add_diary(i,'Guardar isto')
 row=dict(w.library.sql.execute('SELECT * FROM diary_entries WHERE game_id=?',(i,)).fetchone())
 row.update(kind='diary',title=title)
 monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a:QMessageBox.No)
 w.delete_memory(row)
 assert len(w.library.diary(i))==1
 monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a:QMessageBox.Yes)
 w.delete_memory(row)
 assert not w.library.diary(i)
 p=folder/'external.png';p.write_bytes(b'fixture');w.library.add_media(i,p)
 media=dict(w.library.sql.execute('SELECT * FROM media_files WHERE game_id=?',(i,)).fetchone());media['title']=title
 w.delete_memory(media)
 assert p.exists() and not w.library.sql.execute('SELECT 1 FROM media_files WHERE game_id=?',(i,)).fetchone()

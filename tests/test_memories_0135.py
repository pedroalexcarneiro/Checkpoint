from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QInputDialog,QPushButton,QMessageBox
import pytest

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_empty_memory_goes_to_game_tab(ui,app,monkeypatch,title):
 w,i=ui;w.library.save_game({'title':title},i)
 monkeypatch.setattr(QInputDialog,'getItem',lambda *a:(title,True))
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

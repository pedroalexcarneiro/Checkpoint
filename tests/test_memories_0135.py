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

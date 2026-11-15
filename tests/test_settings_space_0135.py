import pytest
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QWidget,QLabel
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_appearance_uses_window_and_cover_preview(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i);w.resize(1920,1080);w.navigate(5)
 for _ in range(5):app.processEvents()
 content=w.findChild(QWidget,'mainContent')
 assert content.width()>w.width()-198-12
 previews=w.pages[5].findChildren(QWidget,'themePreview')
 assert len(previews)==9 and all(p.height()>=100 for p in previews)
 assert w.pages[5].findChild(QWidget,'coverSizePreview') is not None
 assert w.pages[5].findChild(QLabel,'coverSizeLabel').font().bold()

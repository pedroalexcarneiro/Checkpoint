import pytest
from PySide6.QtWidgets import QLabel,QWidget
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from test_bugs_0134 import ui,sample
from checkpoint.settings_previews import ThemePreview
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_mockup_extras_are_absent_and_theme_cards_work(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i);w.resize(1920,1080);w.navigate(5);app.processEvents()
 assert not w.theme_selector.isVisible()
 assert w.header_widget.width()<=1392
 content=w.findChild(QWidget,'mainContent');texts=[label.text() for label in content.findChildren(QLabel)]
 assert not {'Checkpoint','Biblioteca pessoal','9','2','3'}.intersection(texts)
 preview=next(p for p in w.pages[5].findChildren(ThemePreview) if p.theme.key=='pink')
 QTest.mouseClick(preview,Qt.LeftButton);app.processEvents()
 assert w.theme.key=='pink' and w.library.setting('appearance.theme')=='pink'

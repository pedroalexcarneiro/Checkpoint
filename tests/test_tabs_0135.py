import pytest
from test_bugs_0134 import ui,sample
from PySide6.QtCore import Qt,QPoint
from PySide6.QtTest import QTest
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_drag_does_not_select_tab_but_click_and_key_do(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i);w.detail(i);app.processEvents()
 tabs=w.detail_tabs;bar=tabs.tabBar();target=bar.tabRect(1).center()
 QTest.mousePress(bar,Qt.LeftButton,Qt.NoModifier,target)
 QTest.mouseMove(bar,target+QPoint(50,0))
 QTest.mouseRelease(bar,Qt.LeftButton,Qt.NoModifier,target+QPoint(50,0))
 assert tabs.currentIndex()==0
 QTest.mouseClick(bar,Qt.LeftButton,Qt.NoModifier,target)
 assert tabs.currentIndex()==1
 bar.setFocus();QTest.keyClick(bar,Qt.Key_Right)
 assert tabs.currentIndex()==2

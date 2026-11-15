import pytest
from PySide6.QtWidgets import QLabel,QPushButton
from test_bugs_0134 import ui,sample
@pytest.mark.parametrize('page,destination',[(0,'biblioteca'),(1,'biblioteca'),(2,'desejos')])
def test_empty_state_identifies_destination_and_keeps_action(ui,app,monkeypatch,page,destination):
 w,i=ui;w.library.delete(i);calls=[]
 monkeypatch.setattr(w,'add_library_game',lambda:calls.append('add'))
 monkeypatch.setattr(w,'add_game',lambda:calls.append('add'))
 w.navigate(page);app.processEvents()
 frame=w.pages[page].findChild(QLabel,'emptyDescription');assert frame is not None
 assert destination in frame.text() and len(frame.text())>20
 next(button for button in frame.parentWidget().findChildren(QPushButton) if 'Adicionar' in button.text()).click()
 assert calls==['add']

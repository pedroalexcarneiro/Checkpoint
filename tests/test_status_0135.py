import pytest
from PySide6.QtWidgets import QComboBox
from test_bugs_0134 import ui,sample
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_status_control_persists_all_choices(ui,app,title):
 from checkpoint.home_view import in_progress
 w,i=ui;w.library.save_game({'title':title},i);w.detail(i);app.processEvents()
 control=w.detail_page.findChild(QComboBox,'gameStatus')
 assert control is not None
 assert [control.itemText(n) for n in range(control.count())]==['Backlog','Jogando','Pausado','Concluído','Abandonado']
 for name in ('Jogando','Pausado','Concluído','Abandonado','Backlog'):
  control.setCurrentText(name)
  assert w.library.get(i)['status']==name
  assert (i in [g['id'] for g in in_progress(w.library)])==(name in ('Jogando','Pausado'))

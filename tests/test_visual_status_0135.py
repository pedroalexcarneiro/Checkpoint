import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox
from test_bugs_0134 import ui,sample
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_visual_c_five_statuses_highlight_current_without_rewriting_legacy(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i);w.detail(i);app.processEvents()
 combo=w.detail_page.findChild(QComboBox,'gameStatus')
 names=['Não iniciado','Jogando','Pausado','Concluído','Abandonado']
 assert [combo.itemText(n) for n in range(combo.count())]==names
 assert combo.currentText()=='Não iniciado' and w.library.get(i)['status']=='Não iniciado'
 for name in ('Não iniciado','Jogando','Pausado','Concluído','Abandonado'):
  combo.setCurrentText(name)
  for n in range(combo.count()):
   font=combo.itemData(n,Qt.FontRole)
   assert font is not None and font.bold()==(combo.itemText(n)==name)
  if name!='Não iniciado':assert w.library.get(i)['status']==name

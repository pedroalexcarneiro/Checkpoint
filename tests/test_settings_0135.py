from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QPushButton
from checkpoint.design_system import CardGrid

def test_cover_control_label_and_full_width(ui,app):
 w,i=ui
 for title in ('Zelda: A Link to the Past','Metroid Fusion'):w.library.save_game({'title':title})
 w.navigate(5);app.processEvents()
 label=w.pages[5].findChild(QLabel,'coverSizeLabel')
 assert label is not None and label.text()=='Tamanho das capas'
 assert w.pages[5].findChild(CardGrid,'connectionsGrid').maximumWidth()>1200

def test_connections_standard_buttons(ui,app):
 w,i=ui;w.navigate(5);app.processEvents()
 grid=w.pages[5].findChild(CardGrid,'connectionsGrid')
 buttons=[b for c in grid.cards for b in c.findChildren(QPushButton)]
 assert len(buttons)==4
 assert all(b.minimumWidth()==120 and b.minimumHeight()==36 for b in buttons)
 assert all(b.objectName()=='primary' for b in buttons)

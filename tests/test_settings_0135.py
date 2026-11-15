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

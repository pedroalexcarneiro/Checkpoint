import pytest
from PySide6.QtCore import Qt,QPoint
from PySide6.QtWidgets import QLabel,QPushButton,QToolButton
from PySide6.QtTest import QTest
from test_bugs_0134 import ui,sample
from checkpoint.metadata_state import display_source

@pytest.mark.parametrize('source',['rawg','steam','drive'])
def test_real_source_is_shown(ui,app,source):
    w,i=ui
    if source=='drive':w.library.sql.execute('INSERT INTO game_files(game_id,drive_id,original_name) VALUES(?,?,?)',(i,'source-rom','Example.gba'))
    else:w.library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,source,str(i)))
    w.library.sql.commit();w.detail(i);app.processEvents()
    expected={'rawg':'Busca','steam':'Steam','drive':'Drive'}[source]
    assert display_source(w.library,w.library.get(i))==expected
    assert any(label.text()=='Origem · '+expected for label in w.detail_page.findChildren(QLabel))

def test_zero_new_fields_is_not_reported_as_search_failure(ui,app):
    w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'developer':'Existente'},i)
    w.game_completed(i,'Não foi possível preencher a ficha automaticamente. Tente novamente.')
    assert 'Não foi possível preencher' not in w.statusBar().currentMessage()
    assert 'preservados' in w.statusBar().currentMessage()

def test_menu_edge_click_runs_only_named_action(ui,app,monkeypatch):
    w,i=ui;called=[]
    monkeypatch.setattr(w,'artworks',lambda game:called.append('art'))
    monkeypatch.setattr(w.completion_queue,'submit',lambda games,force=False:called.append(('complete',games,force)))
    w.detail(i);app.processEvents();w.move(500-w.width(),40)
    menu=next(b.menu() for b in w.detail_page.findChildren(QToolButton) if b.menu())
    menu.popup(w.mapToGlobal(QPoint(w.width()-1,w.height()-10)));app.processEvents()
    target=next(action for action in menu.actions() if action.text()=='Obter ficha e imagens faltantes')
    QTest.mouseClick(menu,Qt.LeftButton,pos=menu.actionGeometry(target).center());app.processEvents()
    assert called==[('complete',[i],True)]
    menu.hide()

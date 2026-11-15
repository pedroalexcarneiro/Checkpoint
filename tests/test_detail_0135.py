import pytest
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QPushButton
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_wish_detail_only_overview(ui,app,title):
 w,i=ui;w.library.save_game({'title':title},i)
 with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
 w.detail(i);app.processEvents()
 assert w.detail_tabs.count()==1
 assert w.detail_page.findChild(type(w.detail_tabs),'detailGallery') is None
 assert any(b.text()=='Adicionar à biblioteca' for b in w.detail_page.findChildren(QPushButton))
 assert not any(b.text()=='Configurar execução' for b in w.detail_page.findChildren(QPushButton))
 w.library.acquire(i);w.detail(i)
 assert w.detail_tabs.count()==4

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_no_description_explains_and_offers_actions(ui,app,title):
 from PySide6.QtWidgets import QLabel
 w,i=ui;w.library.save_game({'title':title,'banner':'arte-local.png'},i)
 w.detail(i);app.processEvents()
 assert any('texto descritivo' in label.text() for label in w.detail_page.findChildren(QLabel))
 buttons=[b.text() for b in w.detail_page.findChildren(QPushButton)]
 assert 'Pesquisar manualmente' in buttons and 'Editar ficha' in buttons

import pytest
from checkpoint.design_system import IconButton
from PySide6.QtGui import QColor
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('wish',[False,True])
def test_favorite_click_is_visible_persistent_and_reversible(ui,app,wish):
    w,i=ui;lib=w.library
    lib.save_game({'title':lib.get(i)['title'],'notes':'Nota preservada','description':'Descrição externa'},i)
    if wish:lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2)
    else:w.navigate(1)
    original=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
    w.detail(i);app.processEvents()
    def heart():return next(b for b in w.detail_page.findChildren(IconButton) if b.name=='heart')
    for enabled in [True,False]:
        heart().click();app.processEvents()
        assert lib.get(i)['favorite']==int(enabled)
        control=heart();assert control.isCheckable() and control.isChecked()==enabled
        center=control.grab().toImage().pixelColor(control.width()//2,control.height()//2)
        assert (center==QColor(w.theme.colors['accent']))==enabled
        assert control.toolTip()==('Retirar dos favoritos' if enabled else 'Marcar como favorito')
        w.detail(i);app.processEvents();assert heart().isChecked()==enabled
        assert lib.is_owned(i)==(not wish)
        assert lib.get(i)['notes']=='Nota preservada' and lib.get(i)['description']=='Descrição externa'
        assert [tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]==original
        from checkpoint.database import Database
        with_db=Database(lib.db.path)
        try:assert with_db.connection.execute('SELECT favorite FROM games WHERE id=?',(i,)).fetchone()[0]==int(enabled)
        finally:with_db.close()
        if enabled:
            w.navigate(1);w.library_tabs.setCurrentIndex(1);app.processEvents()
            assert w.gallery.count()==(0 if wish else 1)
            w.navigate(2 if wish else 1);w.detail(i);app.processEvents()
    w.navigate(1);w.library_tabs.setCurrentIndex(1);app.processEvents()
    assert w.gallery.count()==0

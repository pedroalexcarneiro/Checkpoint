import pytest
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QPushButton,QToolButton
from checkpoint.collection_views import WishCard,WishLogo
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('has_banner',[False,True])
def test_open_wish_stays_in_wishes_and_does_not_acquire(ui,app,folder,has_banner):
    w,i=ui;lib=w.library
    if has_banner:
        path=folder/'banner.png';im=QImage(1920,620,QImage.Format_RGB32);im.fill(QColor('blue'));im.save(str(path));lib.save_game({'title':lib.get(i)['title'],'banner':str(path)},i)
    lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
    before=lib.get(i);wishlist=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
    card=next(c for c in w.pages[2].findChildren(WishCard) if c.isVisible())
    card.findChild(WishLogo).click();app.processEvents()
    assert w.current_page==2 and w.nav_buttons[2].isChecked() and not w.nav_buttons[1].isChecked()
    assert not lib.is_owned(i) and lib.get(i)==before
    assert [tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]==wishlist
    assert w.detail_tabs.count()==1
    assert not any(b.text()=='Adicionar à biblioteca' for b in w.detail_page.findChildren(QPushButton))
    menu=next(b.menu() for b in w.detail_page.findChildren(QToolButton) if b.menu())
    assert 'Retirar dos desejos' in [a.text() for a in menu.actions()]
    assert 'Remover da biblioteca' not in [a.text() for a in menu.actions()]
    back=next(b for b in w.detail_page.findChildren(QPushButton) if b.isVisible() and b.accessibleName()=='Voltar aos desejos')
    back.click();app.processEvents()
    assert w.current_page==2 and w.stack.currentWidget()==w.pages[2]
    assert not lib.is_owned(i)

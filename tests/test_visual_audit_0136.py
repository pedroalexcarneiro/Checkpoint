from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QPushButton,QLabel
from checkpoint.design_system import CardGrid,IconButton
from checkpoint.collection_views import WishLogo
from test_bugs_0134 import ui,sample


def test_long_memory_titles_keep_delete_inside_card(ui,app):
    w,i=ui
    for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
        identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
    for size in [(1280,800),(1920,1080)]:
        w.resize(*size);w.navigate(3)
        for _ in range(5):app.processEvents()
        grids=w.pages[3].findChildren(CardGrid,'memoriesGrid')
        grid=next(g for g in grids if g.isVisible());assert len(grid.cards)==2
        for card in grid.cards:
            delete=card.findChild(IconButton)
            assert card.rect().contains(delete.geometry())
            title=card.findChild(QPushButton,'activityLink')
            assert title.geometry().right()<delete.geometry().left()
            assert title.toolTip() and title.accessibleName()


def test_wide_wishes_and_existing_identity_are_preserved(ui,app):
    w,i=ui
    for n in range(12):
        j=w.library.save_game({'title':f'Fixture visual {n}'})
        w.library.set_setting(f'collection.unowned.{j}',True);w.add_wish(j)
    columns=[]
    for size in [(1280,800),(1920,1080)]:
        w.resize(*size);w.navigate(2)
        for _ in range(5):app.processEvents()
        grid=w.pages[2].findChild(CardGrid,'wishlistGrid');columns.append(grid.columns)
        assert all(c.width()<=360 and c.findChild(WishLogo).width()==c.findChild(WishLogo).height() for c in grid.cards)
    assert columns[1]>columns[0]
    w.navigate(5);app.processEvents()
    assert w.brand.text()=='Checkpoint' and w.theme_selector.count()==9
    assert w.header_widget.width()<=1392

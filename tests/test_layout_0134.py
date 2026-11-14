from pathlib import Path
import pytest
from PySide6.QtCore import Qt,QRect
from PySide6.QtGui import QImage,QColor,QFontMetrics,QRegion
from PySide6.QtWidgets import QLabel,QPushButton
from test_bugs_0134 import ui,sample

def test_list_uses_fixed_logo_area_or_title(ui,app,folder):
    w,i=ui;image=QImage(240,80,QImage.Format_RGB32);image.fill(QColor('#18aa60'));logo=folder/'logo.png';assert image.save(str(logo))
    image.fill(QColor('#ff0000'));cover=folder/'cover.png';assert image.save(str(cover))
    w.library.save_game({'title':w.library.get(i)['title'],'logo':str(logo),'cover':str(cover)},i)
    w.view.setCurrentIndex(1);w.refresh_library();app.processEvents()
    assert w.table.columnWidth(0)==160 and w.table.item(0,1).text()==w.library.get(i)['title']
    assert w.table.item(0,0).icon().pixmap(140,48).toImage().pixelColor(70,24)==QColor('#18aa60')
    from checkpoint.list_art import list_icon
    game={**w.library.get(i),'logo':''};pix=list_icon(game,'#ffffff').pixmap(140,48)
    assert not QRegion(pix.mask()).boundingRect().isEmpty()
    assert all(pix.toImage().pixelColor(x,24)!=QColor('#ff0000') for x in range(140))

@pytest.mark.parametrize('width',[1280,1920])
def test_wishes_fill_columns_with_square_art(ui,app,width):
    from checkpoint.collection_views import WishGrid,WishLogo,WishCard
    w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
    with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
    w.resize(width,800);w.navigate(2)
    for _ in range(4):app.processEvents()
    grid=w.pages[2].findChild(WishGrid);card=grid.findChild(WishCard);art=card.findChild(WishLogo)
    assert art.width()==art.height() and card.width()>=280
    assert abs(grid.columns*card.width()+(grid.columns-1)*grid.grid.spacing()-grid.width())<grid.columns

def test_settings_paths_labels_grid_and_update_action(ui,app,folder,monkeypatch):
    from checkpoint.design_system import ThemeSwatch,CardGrid
    from checkpoint.theme import THEMES
    w,i=ui;called=[];monkeypatch.setattr(w,'updates',lambda:called.append(True))
    path=folder/'ROMs baixadas';w.library.set_setting('downloads',str(path));w.resize(1280,800);w.navigate(5);app.processEvents()
    swatches=w.pages[5].findChildren(ThemeSwatch)
    assert {s.toolTip() for s in swatches}=={theme.name for theme in THEMES.values()}
    captions=[label.text() for label in w.settings_tabs.widget(0).findChildren(QLabel)]
    assert all(theme.name in captions for theme in THEMES.values())
    w.settings_tabs.setCurrentIndex(1)
    for _ in range(3):app.processEvents()
    grid=w.pages[5].findChild(CardGrid,'connectionsGrid')
    assert grid.columns==2 and len(grid.cards)==4 and len({c.y() for c in grid.cards})==2
    w.settings_tabs.setCurrentIndex(2);app.processEvents()
    paths=[label.text() for label in w.settings_tabs.widget(2).findChildren(QLabel,'folderPath')]
    assert str(path.resolve()) in paths and 'Não definida' in paths
    w.settings_tabs.setCurrentIndex(3);app.processEvents()
    w.pages[5].findChild(QPushButton,'checkUpdates').click();assert called==[True]

def test_home_empty_text_and_files_action(ui,app):
    w,i=ui;w.resize(1280,800);w.navigate(0)
    for _ in range(3):app.processEvents()
    description=w.pages[0].findChild(QLabel,'emptyDescription')
    needed=QFontMetrics(description.font()).boundingRect(QRect(0,0,description.width(),10000),Qt.TextWordWrap,description.text()).height()
    assert description.height()>=needed
    w.detail(i);w.detail_tabs.setCurrentIndex(3);app.processEvents()
    buttons=w.detail_tabs.widget(3).findChildren(QPushButton)
    assert not any(button.text()=='Configurar execução' for button in buttons)
    assert any(button.text()=='Vincular ROM do Drive' for button in buttons)

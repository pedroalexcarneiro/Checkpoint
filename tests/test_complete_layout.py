from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QInputDialog,QLabel,QLineEdit
from gamevault.window import MainWindow
from gamevault.dialogs import GameDialog
from gamevault.design_system import CardGrid,IconButton,ThemeSwatch


def test_wishlist_uses_current_prices_and_removal_preserves_game(library,app,monkeypatch):
    identity=library.save_game({'title':'Wishlist fixture','notes':'Preserve'})
    with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,?)',(identity,5000))
    window=MainWindow(library);window.navigate(2);window.show();app.processEvents()
    assert len(window.pages[2].findChild(CardGrid,'wishlistGrid').cards)==1
    monkeypatch.setattr(QInputDialog,'getDouble',lambda *args:(39.9,True))
    window.add_wish(identity)
    assert library.sql.execute('SELECT target_cents FROM wishlist').fetchone()[0]==5000
    labels=[item.text() for item in window.pages[2].findChildren(QLabel)]
    assert 'Menor preço' in labels and 'Meta de preço' not in labels
    assert not library.is_owned(identity)
    window.pages[2].findChild(IconButton).click()
    assert library.sql.execute('SELECT count(*) FROM wishlist').fetchone()[0]==0
    assert library.get(identity)['notes']=='Preserve';window.close()


def test_memories_excludes_removed_games_and_filters_diary(library,app,tmp_path):
    visible=library.save_game({'title':'Visible'});removed=library.save_game({'title':'Removed'})
    library.add_diary(visible,'Visible memory');library.add_diary(removed,'Private removed memory');library.delete(removed)
    window=MainWindow(library);window.navigate(3);window.show();app.processEvents()
    from PySide6.QtWidgets import QTabWidget
    tabs=window.pages[3].findChild(QTabWidget,'memoryTabs')
    assert tabs.count()==3
    labels=[label.text() for label in tabs.currentWidget().findChildren(QLabel)]
    assert 'Visible memory' in labels and 'Private removed memory' not in labels
    tabs.setCurrentIndex(2);app.processEvents()
    assert not tabs.currentWidget().findChildren(CardGrid);window.close()


def test_editor_all_tabs_keep_values_and_manual_images(library,app,tmp_path):
    from PySide6.QtGui import QImage,QColor
    path=tmp_path/'manual.png';image=QImage(80,120,QImage.Format_RGB32);image.fill(QColor('red'));image.save(str(path))
    identity=library.save_game({'title':'Editor fixture','cover':str(path),'notes':'Keep notes','developer':'Keep studio','rating':8})
    dialog=GameDialog(game=library.get(identity),library=library);dialog.show()
    assert [dialog.editor_tabs.tabText(i) for i in range(4)]==['Ficha','Execução','Imagens','Pessoal']
    for index in range(4):dialog.editor_tabs.setCurrentIndex(index);app.processEvents()
    dialog.fields['notes'].setPlainText('New note');dialog.validate()
    data=dialog.data();assert data['developer']=='Keep studio' and data['rating']==8 and data['notes']=='New note'
    assert data['cover']==str(path) and path.is_file()


def test_favorite_action_keeps_detail_draft(library,app):
    identity=library.save_game({'title':'Favorite fixture'})
    window=MainWindow(library);window.detail(identity);window.detail_tabs.setCurrentIndex(2);window.detail_diary.setPlainText('Unsaved')
    window.toggle_favorite(identity)
    assert library.get(identity)['favorite']==1 and window.detail_diary.toPlainText()=='Unsaved'
    window.close()


def test_layout_header_and_library_fit_small_window(library,app):
    for index in range(16):library.save_game({'title':f'Layout fixture {index}'})
    window=MainWindow(library);window.resize(1000,700);window.show()
    for page in range(6):
        window.navigate(page)
        for _ in range(3):app.processEvents()
        assert window.width()==1000 and window.header_widget.height()==38
        assert window.heading.geometry().top()>=0 and window.heading.geometry().bottom()<window.header_widget.height()
    window.navigate(1);app.processEvents();grid=window.gallery
    first=[grid.visualItemRect(grid.item(i)) for i in range(grid.count()) if grid.visualItemRect(grid.item(i)).top()==0]
    assert len(first)>=4
    assert first[-1].right()<=grid.viewport().width();window.close()


def test_theme_swatches_and_profile_apply_without_losing_data(library,app):
    identity=library.save_game({'title':'Theme fixture'})
    window=MainWindow(library);window.navigate(5);window.show();app.processEvents()
    swatch=next(item for item in window.findChildren(ThemeSwatch) if item.theme.key=='purple');swatch.click()
    assert app.property('checkpointTheme')=='purple' and window.brand.theme.key=='purple'
    from gamevault.profile_dialog import ProfileDialog
    dialog=ProfileDialog(library,window);dialog.nickname.setText('Jogador');dialog.save();window.refresh_profile()
    assert library.setting('profile.name')=='Jogador' and window.profile_button.text()=='Jogador'
    assert library.get(identity)['title']=='Theme fixture';window.close()

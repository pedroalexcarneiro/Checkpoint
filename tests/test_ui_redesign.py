from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QLabel,QDialog
from gamevault.window import MainWindow
from gamevault.ui_components import Hero,GameTile
from gamevault.branding import app_icon
from gamevault.theme import get_theme
from gamevault.dialogs import GameDialog


def art(folder,name,color):
    path=folder/(name+'.png');image=QImage(160,120,QImage.Format_RGB32);image.fill(QColor(color));assert image.save(str(path));return str(path)


def test_game_detail_uses_banner_logo_tabs_and_preserves_files(library,folder,app):
    cover=art(folder,'cover','red');banner=art(folder,'banner','blue');logo=art(folder,'logo','white')
    game=library.save_game({'title':'Detail fixture','cover':cover,'banner':banner,'logo':logo})
    window=MainWindow(library);window.detail(game)
    assert [window.detail_tabs.tabText(i) for i in range(4)]==['Visão geral','Atividade','Memórias','Arquivos']
    assert len(window.detail_page.findChildren(Hero))==1
    assert all(label.pixmap().isNull() for label in window.detail_page.findChildren(QLabel))
    assert window.nav_buttons[1].isChecked()
    window.detail_tabs.setCurrentIndex(2);window.detail(game)
    assert window.detail_tabs.currentIndex()==2
    assert library.get(game)['cover']==cover and Path(cover).is_file()
    window.close()


def test_settings_are_compact_and_restore_selected_section(library,app,monkeypatch):
    window=MainWindow(library)
    monkeypatch.setattr(window,'integration_status',lambda provider:'Credencial salva · conexão não verificada')
    window.navigate(5)
    assert [window.settings_tabs.tabText(i) for i in range(4)]==['Aparência','Conexões','Downloads','Dados e backup']
    window.settings_tabs.setCurrentIndex(1)
    labels=[label.text() for label in window.settings_tabs.currentWidget().findChildren(QLabel)]
    assert labels.count('Configurado')==4 and 'Conectado' not in labels
    window.navigate(0);window.navigate(5)
    assert window.settings_tabs.currentIndex()==1
    window.close()


def test_library_shortcuts_density_and_theme_update(library,app):
    library.save_game({'title':'Favorite fixture','favorite':1})
    library.save_game({'title':'Playing fixture','status':'Jogando'})
    window=MainWindow(library);window.navigate(1)
    window.library_tabs.setCurrentIndex(1);assert window.gallery.count()==1
    window.library_tabs.setCurrentIndex(2);assert window.gallery.count()==1
    window.library_tabs.setCurrentIndex(0);assert window.gallery.count()==2
    window.set_density('compact');assert window.gallery.iconSize().width()<174
    window.set_theme('purple');assert window.brand.theme.key=='purple'
    assert not app_icon(get_theme('purple')).pixmap(16,16).isNull()
    window.close()


def test_add_sources_do_not_start_network_or_nested_loading(library,app):
    dialog=GameDialog(library=library)
    assert [dialog.source_tabs.tabText(i) for i in range(3)]==['Pesquisar jogo','ROM do Drive','Steam']
    dialog.source_tabs.setCurrentIndex(2);assert not dialog.steam_panel.isHidden()
    dialog.request_steam();assert dialog.steam_requested and dialog.result()==QDialog.Rejected
    dialog.close()


def test_home_tiles_are_full_height_and_open_real_game(library,app):
    identity=library.save_game({'title':'Fixture','status':'Jogando'})
    window=MainWindow(library);window.show();app.processEvents()
    tiles=window.pages[0].findChildren(GameTile)
    assert tiles and all(tile.height()>200 for tile in tiles)
    tiles[0].click();assert window.current_game==identity
    window.close()


def test_detail_refresh_preserves_diary_draft_and_save_clears_it(library,app):
    from PySide6.QtWidgets import QPushButton
    identity=library.save_game({'title':'Draft fixture'})
    window=MainWindow(library);window.detail(identity);window.detail_tabs.setCurrentIndex(2)
    window.detail_diary.setPlainText('Minha memória ainda não salva')
    window.detail(identity)
    assert window.detail_diary.toPlainText()=='Minha memória ainda não salva'
    button=next(b for b in window.detail_page.findChildren(QPushButton) if b.text()=='Salvar memória')
    button.click()
    assert library.diary(identity)[0]['text']=='Minha memória ainda não salva'
    assert window.detail_diary.toPlainText()==''
    window.close()

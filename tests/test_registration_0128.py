from unittest.mock import Mock
from PySide6.QtWidgets import QLabel,QPushButton,QDialog
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult
from checkpoint.game_import import save_import


def test_empty_tabs_search_and_empty_library_have_distinct_actions(library,app):
    window=MainWindow(library);window.navigate(1)
    def labels():return [x.text() for x in window.library_empty.findChildren(QLabel)]
    assert 'Biblioteca vazia' in labels()
    library.save_game({'title':'Meu jogo'});window.refresh_library()
    for index,caption in [(1,'Nenhum favorito ainda'),(2,'Nenhum jogo em andamento'),(3,'Nenhum jogo concluído ainda')]:
        window.library_tabs.setCurrentIndex(index);assert caption in labels()
    window.search.setText('inexistente');assert 'Nenhum resultado para esta busca' in labels()
    button=window.library_empty.findChild(QPushButton);assert button.text()=='Limpar filtros'
    button.click();assert not window.search.text() and window.library_tabs.currentIndex()==0
    assert window.gallery.count()==1;window.close()


def test_quick_add_requires_selection_and_has_exclusive_search_state(library,app):
    dialog=GameDialog(library=library,purpose='wish');quick=dialog.quick_add
    assert dialog.windowTitle()=='Adicionar desejo' and quick.save.text()=='Salvar desejo'
    assert not quick.save.isEnabled()
    quick.query.setText('zelda');quick.timer.stop()
    assert quick.state.text()=='Buscando…' and quick.preview.isHidden() and not quick.save.isEnabled()
    dialog.validate();assert dialog.result()!=QDialog.Accepted
    result=MetadataResult('steam','1','Zelda',platforms=('PC',),developer='Estúdio')
    dialog.apply_catalog(result);quick.show_result(result)
    assert quick.save.isEnabled() and not quick.confirmed.isHidden()
    quick.query.setText('outro');quick.timer.stop();assert not quick.save.isEnabled()
    dialog.close()


def test_wish_reusing_owned_identity_does_not_remove_game(library,app,monkeypatch):
    result=MetadataResult('steam','1','Meu jogo')
    identity=save_import(library,{'title':'Meu jogo','notes':'Preservar'},result=result)
    window=MainWindow(library);window.completion_queue.submit=Mock()
    class Selected:
        steam_requested=False;catalog_result=result;drive_file_id=None;complete_on_save=Mock(isChecked=lambda:False)
        def __init__(self,*args,**kwargs):assert kwargs['purpose']=='wish'
        def exec(self):return QDialog.Accepted
        def data(self):return {'title':'Meu jogo'}
        def should_complete(self):return False
    monkeypatch.setattr('checkpoint.window.GameDialog',Selected)
    window.navigate(2);window.add_game()
    assert library.is_owned(identity) and library.get(identity)['notes']=='Preservar'
    assert not library.setting(f'collection.unowned.{identity}',False)
    assert not library.sql.execute('SELECT 1 FROM wishlist WHERE game_id=?',(identity,)).fetchone()
    assert window.detail_page.findChild(QLabel,'wishNotice').text()=='Este jogo já está na sua biblioteca.'
    window.add_wish(identity);assert library.is_owned(identity);window.close()


def test_new_wish_has_visible_confirmation(library,app,monkeypatch):
    window=MainWindow(library);window.completion_queue.submit=Mock()
    result=MetadataResult('steam','2','Novo desejo')
    class Selected:
        steam_requested=False;catalog_result=result;drive_file_id=None;complete_on_save=Mock(isChecked=lambda:False)
        def __init__(self,*args,**kwargs):pass
        def exec(self):return QDialog.Accepted
        def data(self):return {'title':'Novo desejo'}
        def should_complete(self):return False
    monkeypatch.setattr('checkpoint.window.GameDialog',Selected)
    window.navigate(2);window.add_game();identity=window.current_game
    assert not library.is_owned(identity)
    assert window.detail_page.findChild(QLabel,'wishNotice').text()=='Adicionado à lista de desejos'
    window.close()


def test_selected_preview_does_not_overlap_other_result_link(library,app):
    dialog=GameDialog(library=library);result=MetadataResult('steam','1','Meu jogo',platforms=('PC',))
    dialog.apply_catalog(result);dialog.quick_add.candidates=[result];dialog.quick_add.show_result(result)
    dialog.show()
    for _ in range(4):app.processEvents()
    quick=dialog.quick_add
    assert quick.preview.geometry().bottom()<quick.other.geometry().top()
    assert quick.art.height()<=quick.preview.height()
    assert quick.save.geometry().bottom()<dialog.height()
    dialog.close()


def test_missing_cover_draws_full_title_instead_of_two_letters(library,app):
    from PySide6.QtCore import Qt,QRect
    from PySide6.QtGui import QFontMetrics
    from PySide6.QtWidgets import QStyleOptionViewItem
    title='ARK: Survival of the Fittest';library.save_game({'title':title})
    window=MainWindow(library);window.navigate(1)
    painter=Mock();painter.fontMetrics.return_value=QFontMetrics(app.font())
    option=QStyleOptionViewItem();option.rect=QRect(0,0,210,360)
    window.gallery.itemDelegate().paint(painter,option,window.gallery.model().index(0,0))
    drawn=[call.args[-1] for call in painter.drawText.call_args_list]
    assert title in drawn and 'AR' not in drawn;window.close()

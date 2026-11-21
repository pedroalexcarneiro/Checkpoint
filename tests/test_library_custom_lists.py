from PySide6.QtCore import Qt,QTimer
from PySide6.QtWidgets import QComboBox,QLineEdit,QListWidget,QPushButton

from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.library_lists import LibraryLists
from test_bugs_0134 import ui,sample


def test_list_filters_combine_in_both_views_and_persist(ui,folder):
    window,first=ui
    lib=window.library
    second=lib.save_game({'title':'Segundo jogo','platform':'Nintendo Switch','favorite':1})
    third=lib.save_game({'title':'Terceiro jogo','platform':'Nintendo Switch','favorite':1})
    lists=LibraryLists(lib)
    identity=lists.save(None,'Para jogar',[first,second])
    other=lists.save(None,'Sequências',[second,third])
    def ids():
        return [[view.item(i).data(Qt.UserRole) for i in range(view.count())]
                for view in (window.game_list,window.gallery)]
    window.navigate(1);window.update_custom_lists()
    window.select_custom_list(window.custom_lists.findData(identity))
    assert all(set(values)=={first,second} for values in ids())
    window.view.setCurrentIndex(1)
    window.library_tabs.setCurrentIndex(1)
    window.platform.setCurrentIndex(window.platform.findData('Nintendo Switch'))
    window.sort.setCurrentIndex(window.sort.findData('recent'))
    assert ids()==[[second],[second]]
    window.search.setText('Terceiro');window.refresh_library()
    assert ids()==[[],[]]
    empty=window.library_empty.findChild(QPushButton)
    assert empty.text()=='Limpar filtros'
    empty.click()
    assert all(set(values)=={first,second} for values in ids())
    rom=folder/'Segundo.nsp';rom.write_bytes(b'fixture')
    with lib.sql:lib.sql.execute('INSERT INTO game_files(game_id,original_name,local_path) VALUES(?,?,?)',(second,rom.name,str(rom)))
    lists.save(identity,'Renomeada',[first])
    assert second in lists.all()[other]['games']
    lists.remove(identity)
    assert lib.get(second) and lib.get(first) and rom.read_bytes()==b'fixture'
    assert lib.sql.execute('SELECT game_id FROM game_files').fetchone()[0]==second
    reopened=Database(lib.db.path)
    try:assert LibraryLists(Library(reopened)).all()=={other:{'name':'Sequências','games':[second,third]}}
    finally:reopened.close()


def test_new_list_manager_saves_checked_games_and_rejects_duplicate(ui,app):
    window,first=ui
    lib=window.library
    second=lib.save_game({'title':'Jogo B','platform':'Nintendo Switch'})
    def interact(dialog):
        name=dialog.findChild(QLineEdit)
        games=dialog.findChild(QListWidget)
        save=next(button for button in dialog.findChildren(QPushButton) if button.text()=='Salvar lista')
        name.setText('Fins de semana')
        for i in range(games.count()):
            item=games.item(i)
            if item.data(Qt.UserRole)==second:
                assert item.text()=='Jogo B'
                item.setCheckState(Qt.Checked)
        save.click()
        identity=dialog.findChild(QComboBox).currentData()
        assert LibraryLists(lib).all()[identity]['games']==[second]
        dialog.findChild(QComboBox).setCurrentIndex(0)
        name.setText('FINS DE SEMANA');save.click()
        assert len(LibraryLists(lib).all())==1
    issues=[]
    def run_dialog():
        dialog=app.activeModalWidget()
        try:interact(dialog)
        except BaseException as error:issues.append(error)
        finally:dialog.reject()
    window.navigate(1);QTimer.singleShot(0,run_dialog)
    window.select_custom_list(window.custom_lists.findData('create'))
    assert not issues,issues
    assert window.custom_lists.currentText()=='Fins de semana'
    assert window.game_list.count()==1 and window.game_list.item(0).data(Qt.UserRole)==second
    assert lib.get(first)

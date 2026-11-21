"""Listas lógicas da Biblioteca, persistidas pelas IDs dos jogos."""
from uuid import uuid4


SETTING='library.custom_lists'


class LibraryLists:
    def __init__(self,library):
        self.library=library

    def all(self):
        records=self.library.setting(SETTING,{})
        return records if isinstance(records,dict) else {}

    def save(self,identity,name,games):
        name=name.strip()
        if not name:raise ValueError('Informe um nome para a lista.')
        if name.casefold() in ('todos os jogos','criar lista…','gerenciar listas…'):
            raise ValueError('Escolha um nome diferente dos controles da Biblioteca.')
        records=self.all()
        if identity is not None and identity not in records:
            raise ValueError('Esta lista não existe mais.')
        if any(row['name'].casefold()==name.casefold() for key,row in records.items() if key!=identity):
            raise ValueError('Já existe uma lista com esse nome.')
        identity=identity or uuid4().hex
        records[identity]={'name':name,'games':sorted(set(games))}
        self.library.set_setting(SETTING,records)
        return identity

    def remove(self,identity):
        records=self.all()
        if identity in records:
            del records[identity]
            self.library.set_setting(SETTING,records)


def manage_lists(window,selected=None,*,create=False):
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QComboBox,QDialog,QFormLayout,QHBoxLayout,QLineEdit,QListWidget,QListWidgetItem,QVBoxLayout
    from .design_system import dialog_heading
    from .dialog_style import AppMessages,prepare_dialog
    from .ui_components import action,text

    lists=LibraryLists(window.library)
    dialog=prepare_dialog(QDialog(window))
    dialog.setWindowTitle('Listas da Biblioteca');dialog.resize(640,524)
    layout=QVBoxLayout(dialog)
    dialog_heading(layout,'Listas da Biblioteca',name='library')
    fields=QFormLayout()
    selection=QComboBox();selection.setAccessibleName('Lista da Biblioteca');fields.addRow('Lista',selection)
    name=QLineEdit();name.setAccessibleName('Nome da lista')
    name.setMaxLength(88);fields.addRow('Nome',name)
    layout.addLayout(fields)
    layout.addWidget(text('Jogos','cardTitle'))
    games=QListWidget();games.setAccessibleName('Jogos da lista');layout.addWidget(games,1)
    status=text('','muted');layout.addWidget(status)
    for game in window.library.owned_games():
        item=QListWidgetItem(game['title']);item.setData(Qt.UserRole,game['id'])
        if game['platform']:item.setToolTip(game['platform'])
        item.setFlags(item.flags()|Qt.ItemIsUserCheckable);item.setCheckState(Qt.Unchecked)
        games.addItem(item)
    last_selection=selected

    def load_selection():
        row=lists.all().get(selection.currentData(),{})
        name.setText(row.get('name',''))
        members=set(row.get('games',[]))
        for index in range(games.count()):
            item=games.item(index)
            item.setCheckState(Qt.Checked if item.data(Qt.UserRole) in members else Qt.Unchecked)
        remove_button.setEnabled(bool(row))
        status.clear()

    def populate(identity):
        selection.blockSignals(True);selection.clear();selection.addItem('Nova lista',None)
        for key,row in sorted(lists.all().items(),key=lambda entry:entry[1]['name'].casefold()):
            selection.addItem(row['name'],key)
        selection.setCurrentIndex(max(0,selection.findData(identity)));selection.blockSignals(False)
        load_selection()

    def save():
        nonlocal last_selection
        identity=selection.currentData()
        games_in_dialog={games.item(index).data(Qt.UserRole) for index in range(games.count())}
        existing=set(lists.all().get(identity,{}).get('games',[]))
        checked={games.item(index).data(Qt.UserRole) for index in range(games.count())
                 if games.item(index).checkState()==Qt.Checked}
        try:last_selection=lists.save(identity,name.text(),(existing-games_in_dialog)|checked)
        except ValueError as error:status.setText(str(error));return
        populate(last_selection);status.setText('Lista salva.')

    def remove():
        nonlocal last_selection
        identity=selection.currentData()
        if not identity:return
        if AppMessages.question(dialog,'Excluir lista',f'Excluir a lista “{selection.currentText()}”?')!=AppMessages.Yes:
            return
        lists.remove(identity)
        if last_selection==identity:last_selection=None
        populate(None);status.setText('Lista excluída.')

    buttons=QHBoxLayout()
    remove_button=action('Excluir lista',remove);buttons.addWidget(remove_button);buttons.addStretch()
    buttons.addWidget(action('Fechar',dialog.reject));buttons.addWidget(action('Salvar lista',save,True))
    layout.addLayout(buttons)
    selection.currentIndexChanged.connect(load_selection)
    populate(None if create else selected)
    if create:name.setFocus()
    dialog.exec()
    return last_selection

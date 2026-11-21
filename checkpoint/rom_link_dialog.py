"""A busca de Arquivos conhece o jogo; um clique vincula e inicia as etapas."""
from PySide6.QtCore import Qt,Slot
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QListWidget,QListWidgetItem,QInputDialog,QMessageBox
from .ui_components import text,action
from .rom_link import candidates
from .rom_link_worker import run_link


class RomLinkDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id;self.job=None;self.file_id=None;self.outcome=None
        from .transfers import manager_for
        self.manager=manager_for(library,parent);self.task=None;self.progress_card=None;self.monitor_closed=False
        self.manager.updated.connect(self.task_updated);self.manager.completed.connect(self.task_finished)
        from .dialog_style import prepare_dialog
        prepare_dialog(self)
        self.setWindowTitle('Vincular ROM do Drive');self.resize(720,500)
        game=library.get(game_id);self.platform=game['platform'];layout=QVBoxLayout(self)
        self.game_title=text('Vincular ROM a '+game['title'],'sectionTitle');layout.addWidget(self.game_title)
        self.query=QLineEdit();self.query.setPlaceholderText('Pesquisar ROM pelo título');self.query.setText(game['title']);layout.addWidget(self.query)
        self.results=QListWidget();self.results.setObjectName('romLinkResults');layout.addWidget(self.results,1)
        self.state=text('','muted');self.state.setObjectName('romLinkState');layout.addWidget(self.state)
        self.retry=action('Tentar novamente',self.start);self.retry.hide();layout.addWidget(self.retry,0,Qt.AlignLeft)
        self.correct=action('Escolher outra ficha',self.choose_game);self.correct.hide();layout.addWidget(self.correct,0,Qt.AlignLeft)
        self.register=action('Cadastrar edição',self.register_game);self.register.hide();layout.addWidget(self.register,0,Qt.AlignLeft)
        layout.addWidget(action('Fechar',self.reject),0,Qt.AlignRight)
        self.query.textChanged.connect(self.refresh);self.results.itemClicked.connect(self.chosen)
        self.refresh()

    def refresh(self):
        if self.task and self.task.active:return
        self.rows=candidates(self.library,self.query.text(),self.platform);self.results.clear()
        for file in self.rows:
            item=QListWidgetItem(file['original_name']+'\n'+(file['platform'] or 'Plataforma não identificada'))
            item.setData(Qt.UserRole,file['id']);self.results.addItem(item)
        self.state.setText('' if self.rows else 'Nenhuma ROM compatível. Ajuste o título ou atualize o índice nas Conexões.')

    def chosen(self,item):
        self.file_id=item.data(Qt.UserRole);self.start()

    def start(self):
        if (self.task and self.task.active) or self.file_id is None:return
        from .local_rom import identity_problem,title_needs_confirmation
        file=self.library.sql.execute('SELECT * FROM game_files WHERE id=?',(self.file_id,)).fetchone();game=self.library.get(self.game_id)
        if not file or not game:self.state.setText('ROM ou jogo indisponível. Atualize a seleção.');return
        problem=identity_problem(game,dict(file))
        if problem:
            self.state.setText(problem);self.correct.show();self.register.show();return
        if title_needs_confirmation(game,dict(file)) and QMessageBox.question(self,'Confirmar edição',file['original_name']+'\n'+file['platform']+'\nVincular a '+game['title']+'?')!=QMessageBox.Yes:return
        self.correct.hide();self.register.hide()
        self.outcome=None;self.query.setEnabled(False);self.results.setEnabled(False);self.retry.hide()
        try:self.task=self.manager.start(self.file_id,self.game_id,mode='link',worker=run_link)
        except ValueError as error:
            self.state.setText(str(error));self.query.setEnabled(True);self.results.setEnabled(True);return
        self.job=self.task.job;self.results.hide();self.state.hide()
        if self.progress_card:
            self.layout().removeWidget(self.progress_card);self.progress_card.deleteLater()
        from .transfer_view import TransferCard
        self.progress_card=TransferCard(self.manager,self.task,self,allow_retry=False)
        self.layout().insertWidget(self.layout().count()-1,self.progress_card)
        if not self.task.active:self.task_finished(self.task)

    def choose_game(self):
        games=self.library.owned_games();names=[f'{n+1}. '+g['title']+' · '+(g['platform'] or 'Plataforma não definida') for n,g in enumerate(games)]
        choice,ok=QInputDialog.getItem(self,'Escolher ficha','Jogo e edição:',names,0,False)
        if ok:
            game=games[names.index(choice)];self.game_id=game['id'];self.platform=game['platform'];self.file_id=None
            self.game_title.setText('Vincular ROM a '+game['title']);self.query.setText(game['title']);self.correct.hide();self.register.hide();self.refresh()

    def register_game(self):
        parent=self.parentWidget()
        while parent is not None and not hasattr(parent,'add_library_game'):parent=parent.parentWidget()
        if parent is None:self.state.setText('Cadastre a edição correta em Adicionar jogo antes de vincular.');return
        self.reject()
        origin=self.parentWidget()
        if isinstance(origin,QDialog):origin.reject()
        parent.add_library_game()

    @Slot(object)
    def task_updated(self,task):
        if self.task is not None and task.id==self.task.id:self.job=task.job

    @Slot(object)
    def task_finished(self,task):
        if self.task is None or task.id!=self.task.id:return
        self.outcome=task.outcome;self.state.setText(self.outcome.get('message',''))
        self.job=None;self.query.setEnabled(True);self.results.setEnabled(True)
        if self.monitor_closed:return
        if task.status=='completed' and not self.outcome.get('errors'):self.accept()
        else:
            self.results.show()
            self.retry.setText('Consultar novamente' if task.status=='partial' and self.outcome.get('link_state')=='linked' else 'Tentar novamente')
            self.retry.show()

    def reject(self):
        self.monitor_closed=True
        super().reject()
    def closeEvent(self,event):
        self.monitor_closed=True
        super().closeEvent(event)

from .dialog_style import AppMessages as QMessageBox
from .dialog_style import AppInputs as QInputDialog

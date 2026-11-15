"""A busca de Arquivos conhece o jogo; um clique vincula e inicia as etapas."""
from functools import partial
from PySide6.QtCore import Qt,Slot
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QListWidget,QListWidgetItem,QInputDialog,QMessageBox
from .ui_components import text,action
from .jobs import Job
from .rom_link import candidates
from .rom_link_worker import run_link


class RomLinkDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id;self.job=None;self.file_id=None;self.outcome=None
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
        if self.job:return
        self.rows=candidates(self.library,self.query.text(),self.platform);self.results.clear()
        for file in self.rows:
            item=QListWidgetItem(file['original_name']+'\n'+(file['platform'] or 'Plataforma não identificada'))
            item.setData(Qt.UserRole,file['id']);self.results.addItem(item)
        self.state.setText('' if self.rows else 'Nenhuma ROM compatível. Ajuste o título ou atualize o índice nas Conexões.')

    def chosen(self,item):
        self.file_id=item.data(Qt.UserRole);self.start()

    def start(self):
        if self.job or self.file_id is None:return
        from .local_rom import identity_problem,title_needs_confirmation
        file=self.library.sql.execute('SELECT * FROM game_files WHERE id=?',(self.file_id,)).fetchone();game=self.library.get(self.game_id)
        if not file or not game:self.state.setText('ROM ou jogo indisponível. Atualize a seleção.');return
        problem=identity_problem(game,dict(file))
        if problem:
            self.state.setText(problem);self.correct.show();self.register.show();return
        if title_needs_confirmation(game,dict(file)) and QMessageBox.question(self,'Confirmar edição',file['original_name']+'\n'+file['platform']+'\nVincular a '+game['title']+'?')!=QMessageBox.Yes:return
        self.correct.hide();self.register.hide()
        self.outcome=None;self.query.setEnabled(False);self.results.setEnabled(False);self.retry.hide()
        self.state.setText('Vinculando ROM, verificando o arquivo e consultando a ficha…')
        self.job=Job(partial(run_link,self.library.db.path,self.file_id,self.game_id),self)
        self.job.succeeded.connect(self.completed);self.job.failed.connect(self.failed);self.job.finished.connect(self.finished_job);self.job.start()

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
    def completed(self,result):self.outcome=result;self.state.setText(result['message'])
    @Slot(str)
    def failed(self,message):self.outcome={'errors':[message],'message':message};self.state.setText(message)
    @Slot()
    def finished_job(self):
        self.job.deleteLater();self.job=None;self.query.setEnabled(True);self.results.setEnabled(True)
        if self.outcome and not self.outcome['errors']:self.accept()
        else:
            if not self.outcome:self.state.setText('A operação foi interrompida. Tente novamente.')
            self.retry.show()

    def reject(self):
        if self.job:self.state.setText('Aguarde a operação terminar antes de fechar.');return
        super().reject()
    def closeEvent(self,event):
        if self.job:event.ignore();return
        super().closeEvent(event)

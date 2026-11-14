"""A busca de Arquivos conhece o jogo; um clique vincula e inicia as etapas."""
from functools import partial
from PySide6.QtCore import Qt,Slot
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QListWidget,QListWidgetItem
from .ui_components import text,action
from .jobs import Job
from .rom_link import candidates
from .rom_link_worker import run_link


class RomLinkDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id;self.job=None;self.file_id=None;self.outcome=None
        self.setWindowTitle('Vincular ROM do Drive');self.resize(720,500)
        game=library.get(game_id);self.platform=game['platform'];layout=QVBoxLayout(self)
        layout.addWidget(text('Vincular ROM a '+game['title'],'sectionTitle'))
        layout.addWidget(text('Escolha uma ROM. O download, a verificação e a busca da ficha serão iniciados automaticamente.','muted'))
        self.query=QLineEdit();self.query.setPlaceholderText('Pesquisar ROM pelo título');self.query.setText(game['title']);layout.addWidget(self.query)
        self.results=QListWidget();self.results.setObjectName('romLinkResults');layout.addWidget(self.results,1)
        self.state=text('','muted');self.state.setObjectName('romLinkState');layout.addWidget(self.state)
        self.retry=action('Tentar novamente',self.start);self.retry.hide();layout.addWidget(self.retry,0,Qt.AlignLeft)
        layout.addWidget(action('Fechar',self.reject),0,Qt.AlignRight)
        self.query.textChanged.connect(self.refresh);self.results.itemClicked.connect(self.chosen)
        self.refresh()

    def refresh(self):
        if self.job:return
        self.rows=candidates(self.library,self.query.text(),self.platform);self.results.clear()
        for file in self.rows:
            item=QListWidgetItem(file['original_name']+'\n'+(file['platform'] or 'Plataforma não identificada'))
            item.setData(Qt.UserRole,file['id']);self.results.addItem(item)
        self.state.setText('Até 3 versões; USA/Europe e revisão mais recente primeiro.' if self.rows else 'Nenhuma ROM compatível. Ajuste o título ou atualize o índice nas Conexões.')

    def chosen(self,item):
        self.file_id=item.data(Qt.UserRole);self.start()

    def start(self):
        if self.job or self.file_id is None:return
        self.outcome=None;self.query.setEnabled(False);self.results.setEnabled(False);self.retry.hide()
        self.state.setText('Vinculando ROM, verificando o arquivo e consultando a ficha…')
        self.job=Job(partial(run_link,self.library.db.path,self.file_id,self.game_id),self)
        self.job.succeeded.connect(self.completed);self.job.failed.connect(self.failed);self.job.finished.connect(self.finished_job);self.job.start()

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

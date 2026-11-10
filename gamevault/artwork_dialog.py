from pathlib import Path
from PySide6.QtWidgets import QDialog,QVBoxLayout,QPushButton,QListWidget,QLabel,QComboBox
from .credentials import CredentialVault
from .integrations.metadata import SteamGridDbProvider
from .integrations.images import ImageCache
from .jobs import Job

class ArtworkDialog(QDialog):
    def __init__(self,library,game,parent=None):
        super().__init__(parent); self.library=library; self.game=game; self.jobs=[]; self.results=[]; self.urls=[]
        self.setWindowTitle('Selecionar arte · SteamGridDB'); self.resize(700,600)
        layout=QVBoxLayout(self); layout.addWidget(QLabel('Escolha o jogo, o tipo de arte e depois a imagem. Imagens são armazenadas no cache local.'))
        self.search=QPushButton('Pesquisar '+game['title']); self.search.clicked.connect(self.lookup); layout.addWidget(self.search)
        self.games=QListWidget(); layout.addWidget(self.games)
        self.kind=QComboBox(); self.kind.addItem('Capa vertical','cover'); self.kind.addItem('Banner','banner'); self.kind.addItem('Logo transparente','logo'); layout.addWidget(self.kind)
        self.load=QPushButton('Listar artes do jogo selecionado'); self.load.clicked.connect(self.load_arts); layout.addWidget(self.load)
        self.art=QListWidget(); layout.addWidget(self.art)
        self.apply=QPushButton('Baixar e usar arte selecionada'); self.apply.clicked.connect(self.apply_art); layout.addWidget(self.apply)
        self.state=QLabel('Requer chave SteamGridDB. A seleção é sempre manual.'); self.state.setWordWrap(True); layout.addWidget(self.state)
    def provider(self): return SteamGridDbProvider(CredentialVault().get('steamgriddb'))
    def run(self,work,success):
        for item in [self.search,self.load,self.apply,self.kind]: item.setEnabled(False)
        job=Job(work,self); self.jobs.append(job); job.succeeded.connect(success); job.failed.connect(self.state.setText)
        job.finished.connect(lambda:self.finished_job(job)); self.state.setText('Consultando…'); job.start()
    def finished_job(self,job):
        self.jobs.remove(job); job.deleteLater()
        for item in [self.search,self.load,self.apply,self.kind]: item.setEnabled(True)
    def lookup(self): self.run(lambda:self.provider().search(self.game['title']),self.show_games)
    def show_games(self,results):
        self.results=results; self.games.clear()
        for result in results: self.games.addItem(result.title)
        self.state.setText('Selecione o jogo correto.')
    def load_arts(self):
        index=self.games.currentRow()
        if index<0: return
        game_id=self.results[index].external_id; kind=self.kind.currentData(); self.loaded_kind=kind
        self.run(lambda:self.provider().artworks(game_id,kind),self.show_arts)
    def show_arts(self,urls):
        self.urls=urls; self.art.clear()
        for index,url in enumerate(urls): self.art.addItem(f'Arte {index+1} · '+url.rsplit('/',1)[-1])
        self.state.setText(f'{len(urls)} artes disponíveis. A imagem será exibida para confirmação após o download.')
    def apply_art(self):
        index=self.art.currentRow()
        if index<0: return
        url=self.urls[index]; directory=self.library.db.path.parent/'images'
        self.run(lambda:ImageCache(directory).download(url),self.confirm)
    def confirm(self,path):
        from .dialogs import ImageDialog
        from PySide6.QtWidgets import QMessageBox
        ImageDialog(path,self).exec()
        if QMessageBox.question(self,'Aplicar arte','Usar esta arte no jogo?')==QMessageBox.Yes:
            game=self.library.get(self.game['id']); game[self.loaded_kind]=path
            self.library.save_game(game,game['id']); self.state.setText('Arte salva no cache local.')
    def reject(self):
        if self.jobs: self.state.setText('Aguarde a consulta terminar.'); return
        super().reject()

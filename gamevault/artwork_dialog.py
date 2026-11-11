from pathlib import Path
from PySide6.QtWidgets import QDialog,QVBoxLayout,QPushButton,QListWidget,QLabel,QComboBox,QFileDialog,QCheckBox,QMessageBox,QInputDialog
from .credentials import CredentialVault
from .integrations.metadata import SteamGridDbProvider
from .integrations.images import ImageCache
from .jobs import Job

class ArtworkDialog(QDialog):
    def __init__(self,library,game,parent=None):
        super().__init__(parent); self.library=library; self.game=game; self.jobs=[]; self.results=[]; self.urls=[]
        self.setWindowTitle('Selecionar arte · SteamGridDB'); self.resize(700,600)
        layout=QVBoxLayout(self); layout.addWidget(QLabel('Escolha o jogo, o tipo de arte e depois a imagem. Imagens são armazenadas no cache local.'))
        local=QPushButton('Escolher imagem local (sem chave de API)');local.clicked.connect(self.local_art);layout.addWidget(local)
        self.local=local
        self.search=QPushButton('Pesquisar '+game['title']); self.search.clicked.connect(self.lookup); layout.addWidget(self.search)
        self.games=QListWidget(); layout.addWidget(self.games)
        self.kind=QComboBox(); self.kind.addItem('Capa vertical','cover'); self.kind.addItem('Banner','banner'); self.kind.addItem('Logo transparente','logo'); layout.addWidget(self.kind)
        self.load=QPushButton('Listar artes do jogo selecionado'); self.load.clicked.connect(self.load_arts); layout.addWidget(self.load)
        self.art=QListWidget(); layout.addWidget(self.art)
        self.apply=QPushButton('Baixar e usar arte selecionada'); self.apply.clicked.connect(self.apply_art); layout.addWidget(self.apply)
        self.identify=QPushButton('Confirmar jogo selecionado e obter capa, banner e logo');self.identify.clicked.connect(self.confirm_game);layout.addWidget(self.identify)
        self.missing=QPushButton('Obter artes faltantes do jogo já identificado');self.missing.clicked.connect(self.obtain_missing);layout.addWidget(self.missing)
        self.steam=QPushButton('Identificar pelo AppID Steam');self.steam.clicked.connect(self.identify_steam);layout.addWidget(self.steam)
        self.auto=QCheckBox('Obter artes faltantes automaticamente ao criar, associar ou baixar');self.auto.setChecked(library.setting('artwork.auto',True));self.auto.toggled.connect(lambda value:library.set_setting('artwork.auto',value));layout.addWidget(self.auto)
        self.state=QLabel('Confirme o jogo uma vez. Artes faltantes serão obtidas por tipo, sem substituir escolhas existentes. Requer chave SteamGridDB.'); self.state.setWordWrap(True); layout.addWidget(self.state)
    def confirm_game(self):
        index=self.games.currentRow()
        if index<0: self.state.setText('Pesquise e selecione o jogo correto primeiro.');return
        result=self.results[index]
        if QMessageBox.question(self,'Confirmar identidade',f'Associar {self.game["title"]} ao jogo {result.title} do SteamGridDB e obter as artes faltantes?')!=QMessageBox.Yes: return
        from .auto_artwork import AutoArtwork
        try: AutoArtwork(self.library).confirm_identity(self.game['id'],result.external_id,result.title)
        except ValueError as error: self.state.setText(str(error));return
        self.obtain_missing()
    def identify_steam(self):
        app_id,ok=QInputDialog.getText(self,'Identificar jogo Steam','AppID numérico da página do jogo na Steam:')
        if not ok: return
        app_id=app_id.strip()
        if not app_id.isdigit() or int(app_id)<=0: self.state.setText('Informe um AppID válido.');return
        def confirm(result):
            if QMessageBox.question(self,'Confirmar jogo Steam',f'AppID {app_id}: {result.title}. Associar ao cadastro {self.game["title"]}?')!=QMessageBox.Yes: return
            from .auto_artwork import AutoArtwork
            conflict=self.library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',('steam',app_id)).fetchone()
            if conflict and conflict[0]!=self.game['id']: self.state.setText('AppID já associado a outro cadastro.');return
            try:
                AutoArtwork(self.library).confirm_identity(self.game['id'],result.external_id,result.title)
                with self.library.sql:
                    self.library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?) ON CONFLICT(game_id,provider) DO UPDATE SET external_id=excluded.external_id',(self.game['id'],'steam',app_id))
                from PySide6.QtCore import QTimer
                QTimer.singleShot(0,self.obtain_missing)
            except ValueError as error: self.state.setText(str(error))
        self.run(lambda:self.provider().game_from_steam(app_id),confirm)
    def obtain_missing(self):
        path=self.library.db.path;game_id=self.game['id']
        def work():
            from .database import Database
            from .library import Library
            from .auto_artwork import obtain_artwork
            db=Database(path)
            try: return obtain_artwork(Library(db),game_id,force=True)
            finally: db.close()
        self.run(work,self.state.setText)
    def local_art(self):
        path,_=QFileDialog.getOpenFileName(self,'Selecionar imagem','','Imagens (*.png *.jpg *.jpeg *.webp *.bmp)')
        if not path: return
        self.loaded_kind=self.kind.currentData()
        def store():
            with open(path,'rb') as stream: return ImageCache(self.library.db.path.parent/'images').store(stream.read(25_000_001))
        self.run(store,self.confirm)
    def provider(self): return SteamGridDbProvider(CredentialVault().get('steamgriddb'))
    def run(self,work,success):
        for item in [self.search,self.load,self.apply,self.kind,self.local,self.identify,self.missing,self.steam,self.auto]: item.setEnabled(False)
        job=Job(work,self); self.jobs.append(job); job.succeeded.connect(success); job.failed.connect(self.state.setText)
        job.finished.connect(lambda:self.finished_job(job)); self.state.setText('Consultando…'); job.start()
    def finished_job(self,job):
        self.jobs.remove(job); job.deleteLater()
        for item in [self.search,self.load,self.apply,self.kind,self.local,self.identify,self.missing,self.steam,self.auto]: item.setEnabled(not self.jobs)
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

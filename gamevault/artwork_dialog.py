from pathlib import Path
from PySide6.QtWidgets import QDialog,QVBoxLayout,QPushButton,QListWidget,QLabel,QComboBox,QFileDialog,QCheckBox,QMessageBox,QInputDialog
from .credentials import CredentialVault
from .integrations.metadata import SteamGridDbProvider
from .integrations.images import ImageCache
from .jobs import Job

class ArtworkDialog(QDialog):
    def __init__(self,library,game,parent=None):
        super().__init__(parent); self.library=library; self.game=game; self.jobs=[]; self.results=[]; self.urls=[]
        self.setWindowTitle('Imagens do jogo');self.resize(960,720)
        from PySide6.QtCore import Qt
        from PySide6.QtGui import QPixmap
        from PySide6.QtWidgets import QWidget,QHBoxLayout
        from .design_system import dialog_heading,AdaptiveColumns
        from .settings_view import disclosure
        layout=QVBoxLayout(self);dialog_heading(layout,'Imagens do jogo',game['title'],'memories')
        row=QHBoxLayout();self.kind=QComboBox();self.kind.addItem('Capa vertical','cover');self.kind.addItem('Banner','banner');self.kind.addItem('Logo transparente','logo');row.addWidget(self.kind);row.addStretch()
        self.local=QPushButton('Escolher imagem local');self.local.clicked.connect(self.local_art);row.addWidget(self.local);layout.addLayout(row)
        preview=QWidget();left=QVBoxLayout(preview);left.setContentsMargins(0,0,0,0);self.current_preview=QLabel();self.current_preview.setAlignment(Qt.AlignCenter);self.current_preview.setMinimumSize(240,280);left.addWidget(self.current_preview,1);caption=QLabel('Imagem atual · original preservado');caption.setObjectName('caption');left.addWidget(caption)
        catalog=QWidget();right=QVBoxLayout(catalog);right.setContentsMargins(0,0,0,0);self.search=QPushButton('Pesquisar jogo no catálogo');self.search.clicked.connect(self.lookup);right.addWidget(self.search)
        self.games=QListWidget();self.games.setMaximumHeight(100);right.addWidget(self.games)
        self.load=QPushButton('Ver opções de imagens');self.load.clicked.connect(self.load_arts);right.addWidget(self.load)
        self.art=QListWidget();right.addWidget(self.art,1)
        self.apply=QPushButton('Conferir imagem selecionada');self.apply.setObjectName('primary');self.apply.clicked.connect(self.apply_art);right.addWidget(self.apply)
        layout.addWidget(AdaptiveColumns(preview,catalog,(1,1),breakpoint=700),1)
        advanced=QWidget();inside=QVBoxLayout(advanced);self.identify=QPushButton('Confirmar jogo e obter imagens');self.identify.clicked.connect(self.confirm_game);inside.addWidget(self.identify)
        self.missing=QPushButton('Obter imagens faltantes');self.missing.clicked.connect(self.obtain_missing);inside.addWidget(self.missing)
        self.steam=QPushButton('Identificar pelo AppID Steam');self.steam.clicked.connect(self.identify_steam);inside.addWidget(self.steam)
        self.auto=QCheckBox('Completar imagens automaticamente');self.auto.setChecked(library.setting('artwork.auto',True));self.auto.toggled.connect(lambda value:library.set_setting('artwork.auto',value));inside.addWidget(self.auto);disclosure('Identificação e automação',advanced,layout)
        self.state=QLabel('Escolha uma imagem local ou pesquise opções no catálogo configurado.');self.state.setWordWrap(True);self.state.setObjectName('muted');layout.addWidget(self.state)
        self.kind.currentIndexChanged.connect(self.show_current);self.show_current()

    def show_current(self,*args):
        from PySide6.QtCore import Qt
        from PySide6.QtGui import QPixmap
        game=self.library.get(self.game['id']) or self.game;pix=QPixmap(game.get(self.kind.currentData()) or '')
        if pix.isNull():self.current_preview.clear();self.current_preview.setText('Nenhuma imagem definida')
        else:self.current_preview.setPixmap(pix.scaled(340,320,Qt.KeepAspectRatio,Qt.SmoothTransformation))

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
        for index,url in enumerate(urls): self.art.addItem(f'Opção {index+1}')
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
            self.library.save_game(game,game['id'])
            with self.library.sql:self.library.sql.execute('DELETE FROM artwork_assets WHERE game_id=? AND kind=?',(game['id'],self.loaded_kind))
            self.state.setText('Arte salva no cache local.');self.show_current()
    def reject(self):
        if self.jobs: self.state.setText('Aguarde a consulta terminar.'); return
        super().reject()

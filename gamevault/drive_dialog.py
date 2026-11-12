from pathlib import Path
import unicodedata
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize,Slot,Qt
from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QListWidgetItem,QComboBox,QMessageBox,QFileDialog,QInputDialog
from .jobs import Job
from .database import Database
from .library import Library
from .credentials import CredentialVault
from .integrations.drive import DriveScanner,GoogleDriveClient

class DriveDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent); self.library=library; self.jobs=[]; self.files=[]; self.pending_artwork=None
        self.setWindowTitle('Google Drive · ROMs'); self.resize(860,650)
        layout=QVBoxLayout(self)
        layout.addWidget(QLabel('Varredura de metadados. Nenhum arquivo é baixado durante o scanner.'))
        self.root=QLineEdit(); self.root.setPlaceholderText('ID da pasta principal do Drive')
        state=library.setting('drive_scan',{}); self.root.setText(state.get('root','')); layout.addWidget(self.root)
        self.controls=[]
        actions=QHBoxLayout()
        for title,callback in [('Testar conexão',self.test_connection),('Autenticar',self.authenticate),('Varredura inicial',lambda:self.scan(False)),('Atualizar alterações',lambda:self.scan(True))]:
            item=QPushButton(title); item.clicked.connect(callback); actions.addWidget(item); self.controls.append(item)
        layout.addLayout(actions)
        filters=QHBoxLayout()
        self.search=QLineEdit();self.search.setObjectName('romSearch');self.search.setPlaceholderText('Pesquisar ROM, jogo associado ou pasta');self.search.setClearButtonEnabled(True)
        self.platform_filter=QComboBox();self.platform_filter.setObjectName('romPlatformFilter')
        filters.addWidget(self.search,2);filters.addWidget(self.platform_filter,1);layout.addLayout(filters)
        self.result_count=QLabel();layout.addWidget(self.result_count)
        self.search.textChanged.connect(lambda text:self.refresh())
        self.platform_filter.currentIndexChanged.connect(lambda index:self.refresh())
        self.list=QListWidget(); self.list.setIconSize(QSize(42,56)); layout.addWidget(self.list)
        actions=QHBoxLayout()
        for title,callback in [('Associar a um jogo',self.associate),('Baixar e adicionar à biblioteca',self.download)]:
            item=QPushButton(title); item.clicked.connect(callback); actions.addWidget(item); self.controls.append(item)
        layout.addLayout(actions)
        more=QHBoxLayout()
        for title,callback in [('Pastas e plataformas',self.folder_platforms),('Criar jogo desta ROM',self.create_game),('Capa do jogo',self.game_art)]:
            item=QPushButton(title);item.clicked.connect(callback);more.addWidget(item);self.controls.append(item)
        layout.addLayout(more)
        catalog=QHBoxLayout()
        for title,callback in [('Reconhecer plataformas',self.recognize_platforms),('Importar catálogo DAT',self.import_dat),('Consultar MD5 no catálogo',self.check_catalog)]:
            item=QPushButton(title); item.clicked.connect(callback); catalog.addWidget(item); self.controls.append(item)
        layout.addLayout(catalog)
        self.state=QLabel('Não autenticado nesta janela. Credenciais são mantidas no cofre do Windows.'); self.state.setWordWrap(True); self.state.setTextFormat(Qt.PlainText); layout.addWidget(self.state)
        self.refresh()

    def refresh(self):
        selected=self.selected()
        selected_id=selected['id'] if selected else None
        files=[dict(r) for r in self.library.sql.execute('SELECT f.*,g.title,g.cover FROM game_files f LEFT JOIN games g ON g.id=f.game_id WHERE f.drive_id IS NOT NULL ORDER BY f.original_name')]
        chosen=self.platform_filter.currentData() if self.platform_filter.count() else ''
        self.platform_filter.blockSignals(True);self.platform_filter.clear();self.platform_filter.addItem('Todas as plataformas','')
        for platform in sorted({file['platform'] for file in files if file['platform']}): self.platform_filter.addItem(platform,platform)
        self.platform_filter.addItem('Plataforma não identificada',None)
        index=self.platform_filter.findData(chosen)
        self.platform_filter.setCurrentIndex(max(0,index));self.platform_filter.blockSignals(False)
        platform=self.platform_filter.currentData()
        def fold(value):
            return ''.join(char for char in unicodedata.normalize('NFKD',value.casefold()) if not unicodedata.combining(char))
        query=fold(self.search.text().strip())
        self.files=[file for file in files
                    if (platform=='' or (not file['platform'] if platform is None else file['platform']==platform))
                    and (not query or any(query in fold(file.get(key) or '') for key in ('original_name','title','folder_path')))]
        self.list.clear()
        for index,file in enumerate(self.files):
            item=QListWidgetItem(file['original_name']+' · '+(file['platform'] or 'Revisar plataforma')+' · '+(file['title'] or 'Sem associação')+' · '+file['review_state'])
            if file['cover']: item.setIcon(QIcon(file['cover']))
            self.list.addItem(item)
            if file['id']==selected_id: self.list.setCurrentRow(index)
        self.result_count.setText(f'{len(self.files)} de {len(files)} ROMs' if self.files else f'Nenhuma ROM encontrada · {len(files)} no índice. Limpe a pesquisa ou ajuste a plataforma.')

    def run(self,operation):
        if self.jobs:return
        path=self.library.db.path
        def work():
            db=Database(path)
            try: return operation(Library(db))
            finally: db.close()
        for control in self.controls: control.setEnabled(False)
        job=Job(work,self); self.jobs.append(job)
        job.succeeded.connect(self.completed); job.failed.connect(self.state.setText)
        job.finished.connect(self.finished_job); self.state.setText('Processando…'); job.start()

    @Slot(object)
    def completed(self,result):
        if isinstance(result,dict):
            self.state.setText(result['message'])
            self.pending_artwork=result.get('game_id')
        else:self.state.setText(str(result))
        self.refresh()
    @Slot()
    def finished_job(self):
        job=self.sender()
        if job not in self.jobs:return
        self.jobs.remove(job); job.deleteLater()
        for control in self.controls: control.setEnabled(True)
        if self.pending_artwork:
            game_id=self.pending_artwork;self.pending_artwork=None
            self.queue_artwork(game_id,'ROM baixada e verificada. ')

    def client(self,interactive=False,client_json=None):
        return GoogleDriveClient.authenticate(client_json,CredentialVault(),interactive)
    def test_connection(self):
        from .integrations.network import probe_google_connection
        self.run(lambda lib: probe_google_connection())
    def authenticate(self):
        path,_=QFileDialog.getOpenFileName(self,'OAuth Desktop client do Google Cloud','','JSON (*.json)')
        if path: self.run(lambda lib: 'Autenticado. Pronto para varrer.' if self.client(True,path) else '')
    def scan(self,incremental):
        root=self.root.text().strip()
        if not incremental and self.library.setting('drive_scan',{}).get('root',root)!=root:
            QMessageBox.warning(self,'Pasta','Trocar a raiz de uma coleção existente ainda não é suportado. Use um diretório de dados separado.'); return
        def operation(lib):
            scanner=DriveScanner(lib,self.client())
            count=scanner.incremental() if incremental else scanner.full_scan(root)
            return f'{count} registros processados. Nenhuma ROM foi baixada.'
        self.run(operation)
    def selected(self):
        index=self.list.currentRow()
        return self.files[index] if 0<=index<len(self.files) else None
    def folder_platforms(self):
        from .folder_platform_dialog import FolderPlatformDialog
        FolderPlatformDialog(self.library,self).exec();self.refresh()
    def create_game(self):
        file=self.selected()
        if not file:self.state.setText('Selecione uma ROM primeiro.');return
        from .dialogs import GameDialog
        from .game_import import save_import
        from .artwork_progress import ArtworkProgress
        dialog=GameDialog(self,library=self.library);dialog.load_drive_file(file)
        if dialog.exec()==QDialog.Accepted:
            try:
                game_id=save_import(self.library,dialog.data(),dialog.drive_file_id,dialog.catalog_result)
                progress=ArtworkProgress(self.library,game_id,self);progress.exec()
                self.refresh();self.state.setText('Jogo salvo. '+progress.message)
            except ValueError as error:self.state.setText(str(error))
    def game_art(self):
        file=self.selected()
        if not file or not file['game_id']:
            self.state.setText('Crie ou associe o jogo primeiro para selecionar sua capa.');return
        from .artwork_dialog import ArtworkDialog
        ArtworkDialog(self.library,self.library.get(file['game_id']),self).exec();self.refresh()
    def associate(self):
        file=self.selected(); games=self.library.games()
        if not file: self.state.setText('Selecione uma ROM primeiro.'); return
        if not games: self.state.setText('Crie o primeiro jogo usando Criar jogo desta ROM.'); return
        choices=[str(g['id'])+' · '+g['title'] for g in games]
        choice,ok=QInputDialog.getItem(self,'Revisão manual','Associar este arquivo ao jogo:',choices,0,False)
        if ok:
            game_id=games[choices.index(choice)]['id']
            DriveScanner(self.library,None).associate(file['id'],game_id); self.refresh()
            self.queue_artwork(game_id,'ROM associada ao jogo.')
    def queue_artwork(self,game_id,message):
        from .worker import run_isolated
        self.run(lambda lib: message+' '+run_isolated('enrich',lib.db.path,game_id=game_id))
    def download(self):
        file=self.selected()
        if not file: return
        directory=self.library.setting('downloads')
        if not directory:
            QMessageBox.information(self,'Downloads','Configure a pasta de downloads primeiro.'); return
        from .worker import run_isolated
        self.run(lambda lib:run_isolated('download',lib.db.path,file_id=file['id'],directory=directory))
    def recognize_platforms(self):
        self.run(lambda lib: f'{DriveScanner(lib,None).recognize_platforms()} plataformas reconhecidas. Nenhuma ROM foi baixada.')
    def import_dat(self):
        path,_=QFileDialog.getOpenFileName(self,'Catálogo DAT Logiqx','','DAT/XML (*.dat *.xml)')
        if not path: return
        platform,ok=QInputDialog.getText(self,'Plataforma','Nome exato da plataforma (ex.: SNES):')
        if not ok: return
        def operation(lib):
            from .rom_catalog import RomCatalog
            return str(RomCatalog(lib).import_dat(path,platform))+' ROMs indexadas no catálogo.'
        self.run(operation)
    def check_catalog(self):
        from .rom_catalog import RomCatalog
        file=self.selected()
        if not file: return
        matches=RomCatalog(self.library).candidates(file)
        if not matches:
            self.state.setText('Nenhuma correspondência exata de MD5, tamanho e plataforma. Nenhuma associação foi feita.'); return
        self.state.setText('Correspondências exatas: '+', '.join(m['title'] for m in matches)+'. Use a associação manual para vincular à biblioteca.')
    def reject(self):
        if self.jobs:
            self.state.setText('Aguarde a operação terminar antes de fechar.'); return
        super().reject()

    def closeEvent(self,event):
        if self.jobs:
            self.state.setText('Aguarde a operação terminar antes de fechar.');event.ignore();return
        super().closeEvent(event)

    def accept(self):
        if self.jobs:
            self.state.setText('Aguarde a operação terminar antes de fechar.');return
        super().accept()

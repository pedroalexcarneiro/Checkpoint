from pathlib import Path
from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QMessageBox,QFileDialog,QInputDialog
from .jobs import Job
from .database import Database
from .library import Library
from .credentials import CredentialVault
from .integrations.drive import DriveScanner,GoogleDriveClient

class DriveDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent); self.library=library; self.jobs=[]; self.files=[]
        self.setWindowTitle('Google Drive · ROMs'); self.resize(860,650)
        layout=QVBoxLayout(self)
        layout.addWidget(QLabel('Varredura de metadados. Nenhum arquivo é baixado durante o scanner.'))
        self.root=QLineEdit(); self.root.setPlaceholderText('ID da pasta principal do Drive')
        state=library.setting('drive_scan',{}); self.root.setText(state.get('root','')); layout.addWidget(self.root)
        self.controls=[]
        actions=QHBoxLayout()
        for title,callback in [('Autenticar',self.authenticate),('Varredura inicial',lambda:self.scan(False)),('Atualizar alterações',lambda:self.scan(True))]:
            item=QPushButton(title); item.clicked.connect(callback); actions.addWidget(item); self.controls.append(item)
        layout.addLayout(actions)
        self.list=QListWidget(); layout.addWidget(self.list)
        actions=QHBoxLayout()
        for title,callback in [('Associar a um jogo',self.associate),('Baixar versão selecionada',self.download)]:
            item=QPushButton(title); item.clicked.connect(callback); actions.addWidget(item); self.controls.append(item)
        layout.addLayout(actions)
        catalog=QHBoxLayout()
        for title,callback in [('Importar catálogo DAT',self.import_dat),('Consultar MD5 no catálogo',self.check_catalog)]:
            item=QPushButton(title); item.clicked.connect(callback); catalog.addWidget(item); self.controls.append(item)
        layout.addLayout(catalog)
        self.state=QLabel('Não autenticado nesta janela. Credenciais são mantidas no cofre do Windows.'); self.state.setWordWrap(True); layout.addWidget(self.state)
        self.refresh()

    def refresh(self):
        self.files=[dict(r) for r in self.library.sql.execute('SELECT f.*,g.title FROM game_files f LEFT JOIN games g ON g.id=f.game_id ORDER BY f.original_name')]
        self.list.clear()
        for file in self.files:
            self.list.addItem(file['original_name']+' · '+(file['platform'] or 'Revisar plataforma')+' · '+(file['title'] or 'Sem associação')+' · '+file['review_state'])

    def run(self,operation):
        path=self.library.db.path
        def work():
            db=Database(path)
            try: return operation(Library(db))
            finally: db.close()
        for control in self.controls: control.setEnabled(False)
        job=Job(work,self); self.jobs.append(job)
        job.succeeded.connect(lambda result:self.completed(result)); job.failed.connect(self.state.setText)
        job.finished.connect(lambda:self.finished_job(job)); self.state.setText('Processando…'); job.start()

    def completed(self,result): self.state.setText(str(result)); self.refresh()
    def finished_job(self,job):
        self.jobs.remove(job); job.deleteLater()
        for control in self.controls: control.setEnabled(True)
    def client(self,interactive=False,client_json=None):
        return GoogleDriveClient.authenticate(client_json,CredentialVault(),interactive)
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
        return self.files[index] if index>=0 else None
    def associate(self):
        file=self.selected(); games=self.library.games()
        if not file or not games: return
        choices=[str(g['id'])+' · '+g['title'] for g in games]
        choice,ok=QInputDialog.getItem(self,'Revisão manual','Associar este arquivo ao jogo:',choices,0,False)
        if ok:
            DriveScanner(self.library,None).associate(file['id'],games[choices.index(choice)]['id']); self.refresh()
    def download(self):
        file=self.selected()
        if not file: return
        directory=self.library.setting('downloads')
        if not directory:
            QMessageBox.information(self,'Downloads','Configure a pasta de downloads primeiro.'); return
        self.run(lambda lib:str(DriveScanner(lib,self.client()).download(file['id'],directory)))
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

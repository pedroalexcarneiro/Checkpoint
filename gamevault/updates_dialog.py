import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from uuid import uuid4
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
from . import __version__
from .credentials import CredentialVault
from .jobs import Job
from .updates import GitHubUpdates,UpdateError

class UpdatesDialog(QDialog):
    def __init__(self,data_directory,parent=None):
        super().__init__(parent); self.data_directory=Path(data_directory).resolve(); self.jobs=[]; self.update=None; self.staged=None; self.approved=False
        self.setWindowTitle('Atualizações'); self.resize(620,410)
        layout=QVBoxLayout(self); layout.addWidget(QLabel('Checkpoint '+__version__+' · pedroalexcarneiro/Checkpoint'))
        self.preview=QCheckBox('Incluir versões de desenvolvimento'); self.preview.setChecked(True); layout.addWidget(self.preview)
        self.token=QLineEdit(); self.token.setEchoMode(QLineEdit.Password); self.token.setPlaceholderText('Token GitHub com acesso de leitura ao repositório privado'); layout.addWidget(self.token)
        self.save=QPushButton('Salvar credencial no cofre do Windows'); self.save.clicked.connect(self.save_token); layout.addWidget(self.save)
        self.check=QPushButton('Verificar atualizações'); self.check.clicked.connect(self.check_updates); layout.addWidget(self.check)
        self.download=QPushButton('Baixar e verificar'); self.download.setEnabled(False); self.download.clicked.connect(self.prepare); layout.addWidget(self.download)
        self.install=QPushButton('Aplicar atualização e reiniciar'); self.install.setEnabled(False); self.install.clicked.connect(self.install_update); layout.addWidget(self.install)
        self.state=QLabel('A credencial é necessária para o repositório privado. Permissão mínima: Contents, somente leitura.'); self.state.setWordWrap(True); layout.addWidget(self.state)
    def client(self):
        token=CredentialVault().get('github-updates')
        if not token: raise UpdateError('Nenhuma credencial salva. Cole o token e clique em Salvar credencial antes de verificar.')
        return GitHubUpdates(token)
    def save_token(self):
        if not self.token.text().strip(): return
        try:
            CredentialVault().set('github-updates',self.token.text().strip()); self.token.clear(); self.state.setText('Credencial salva. Acesso ainda não verificado.')
        except Exception: self.state.setText('Não foi possível salvar a credencial no cofre do Windows.')
    def run(self,work,callback):
        for control in [self.save,self.check,self.download,self.install,self.preview]: control.setEnabled(False)
        job=Job(work,self); self.jobs.append(job); job.succeeded.connect(callback); job.failed.connect(self.state.setText)
        job.finished.connect(lambda:self.job_finished(job)); job.start()
    def job_finished(self,job):
        self.jobs.remove(job); job.deleteLater()
        self.save.setEnabled(True); self.check.setEnabled(True); self.preview.setEnabled(True)
        self.download.setEnabled(self.update is not None); self.install.setEnabled(self.staged is not None and getattr(sys,'frozen',False))
    def check_updates(self):
        if self.token.text().strip():
            self.state.setText('Clique em Salvar credencial antes de verificar atualizações.'); return
        self.update=None; self.staged=None; previews=self.preview.isChecked(); self.state.setText('Consultando versões…')
        self.run(lambda:self.client().check(__version__,previews),self.checked)
    def checked(self,update):
        self.update=update; self.state.setText('Nova versão: '+update['tag'] if update else 'Nenhuma versão mais recente com pacote verificável foi encontrada.')
    def prepare(self):
        update=dict(self.update); self.state.setText('Baixando e verificando o pacote…')
        self.run(lambda:self.client().prepare(update,self.data_directory/'updates'),self.prepared)
    def prepared(self,path):
        self.staged=path; self.state.setText('Pacote verificado. Aplicar fechará o aplicativo e preservará a pasta da versão anterior.')
    def install_update(self):
        if self.jobs or not self.staged or not getattr(sys,'frozen',False): return
        installation=Path(sys.executable).resolve().parent
        if installation.name!='Checkpoint' or self.data_directory==installation or installation in self.data_directory.parents:
            self.state.setText('Use a pasta portátil Checkpoint e mantenha o diretório de dados fora da instalação.'); return
        helper=installation/'CheckpointUpdater'/'CheckpointUpdater.exe'
        if not helper.is_file(): self.state.setText('Atualizador auxiliar ausente nesta instalação.'); return
        if QMessageBox.question(self,'Atualizar','Aplicar a versão verificada e reiniciar o Checkpoint?')!=QMessageBox.Yes: return
        try:
            directory=Path(self.staged).parent.parent
            helper_directory=directory/('updater-'+uuid4().hex); shutil.copytree(helper.parent,helper_directory)
            copied=helper_directory/'CheckpointUpdater.exe'
            plan=directory/'install.json'; plan.write_text(json.dumps({'pid':os.getpid(),'installation':str(installation),'staged':self.staged,'data_directory':str(self.data_directory)}),encoding='utf-8')
            subprocess.Popen([str(copied),'--plan',str(plan)],shell=False,creationflags=subprocess.CREATE_NO_WINDOW)
            self.approved=True; self.accept()
        except OSError: self.state.setText('Não foi possível iniciar o atualizador. A versão instalada foi preservada.')
    def reject(self):
        if self.jobs: self.state.setText('Aguarde a operação terminar antes de fechar.'); return
        super().reject()

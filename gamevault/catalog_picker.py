from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QComboBox,QPushButton,QListWidget
from .credentials import CredentialVault
from .integrations.metadata import SteamGridDbProvider,RawgProvider
from .jobs import Job
from .integrations.steam_store import SteamStoreProvider


class CatalogPicker(QDialog):
    def __init__(self,title,parent=None):
        super().__init__(parent);self.selected_result=None;self.results=[];self.jobs=[]
        self.setWindowTitle('Confirmar título no catálogo');self.resize(650,500)
        layout=QVBoxLayout(self)
        help=QLabel('Escolha a edição correta. O título exibido virá do catálogo; o nome original da ROM será preservado. Steam fornece ficha e imagens sem chave. RAWG cobre outros jogos com chave própria; SteamGridDB complementa artes.')
        help.setWordWrap(True);layout.addWidget(help)
        row=QHBoxLayout();self.provider=QComboBox();self.provider.addItem('Steam · ficha e imagens (sem chave)','steam');self.provider.addItem('SteamGridDB · título e artes','steamgriddb');self.provider.addItem('RAWG · ficha do jogo','rawg');row.addWidget(self.provider)
        self.query=QLineEdit(title);row.addWidget(self.query,1);layout.addLayout(row)
        self.search=QPushButton('Pesquisar');self.search.clicked.connect(self.lookup);layout.addWidget(self.search)
        self.list=QListWidget();layout.addWidget(self.list)
        self.use=QPushButton('Usar título e dados do resultado selecionado');self.use.clicked.connect(self.choose);layout.addWidget(self.use)
        self.state=QLabel('Nenhum jogo é associado automaticamente por semelhança de nome.');self.state.setWordWrap(True);layout.addWidget(self.state)
    def source(self):
        key=self.provider.currentData()
        if key=='steam':return SteamStoreProvider()
        secret=CredentialVault().get(key)
        return SteamGridDbProvider(secret) if key=='steamgriddb' else RawgProvider(secret)
    def run(self,action,success):
        for control in (self.provider,self.search,self.use,self.query,self.list):control.setEnabled(False)
        job=Job(action,self);self.jobs.append(job);job.succeeded.connect(success);job.failed.connect(self.state.setText)
        job.finished.connect(lambda:self.finished_job(job));self.state.setText('Consultando catálogo…');job.start()
    def finished_job(self,job):
        self.jobs.remove(job);job.deleteLater()
        for control in (self.provider,self.search,self.use,self.query,self.list):control.setEnabled(True)
        if getattr(self,'_accept_when_finished',False):self.accept()
    def lookup(self):
        title=self.query.text().strip()
        if not title:return
        source=self.provider.currentData()
        def fetch():
            if source=='steam':return SteamStoreProvider().search(title)
            secret=CredentialVault().get(source)
            provider=SteamGridDbProvider(secret) if source=='steamgriddb' else RawgProvider(secret)
            return provider.search(title)
        self.run(fetch,self.show_results)
    def show_results(self,results):
        self.results=results;self.list.clear()
        for result in results:self.list.addItem(result.title+(' · '+result.release_date if result.release_date else ''))
        self.state.setText(f'{len(results)} resultados. Confirme o jogo e a edição corretos.')
    def choose(self):
        index=self.list.currentRow()
        if index<0:self.state.setText('Selecione um resultado.');return
        selected=self.results[index]
        if selected.provider=='steam':
            self.run(lambda:SteamStoreProvider().details(selected.external_id),self.complete)
        elif selected.provider=='rawg':
            self.run(lambda:RawgProvider(CredentialVault().get('rawg')).details(selected.external_id),self.complete)
        else:self.complete(selected)
    def complete(self,result):
        self.selected_result=result
        if not self.jobs:self.accept()
        else:self._accept_when_finished=True
    def reject(self):
        if self.jobs:self.state.setText('Aguarde a consulta terminar.');return
        super().reject()

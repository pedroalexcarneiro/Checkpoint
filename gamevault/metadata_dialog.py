from .locale import date_display
from pathlib import Path
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QListWidgetItem,QMessageBox,QComboBox
from PySide6.QtCore import Qt
from .jobs import Job
from .credentials import CredentialVault
from .integrations.metadata import RawgProvider
from .integrations.images import ImageCache

class MetadataDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent); self.library = library; self.jobs = []; self.results = []; self.imported_id = None
        self.setWindowTitle('Pesquisar metadados · RAWG'); self.resize(680,560)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('RAWG · selecione explicitamente o resultado correto.'))
        self.query = QLineEdit(); self.query.setPlaceholderText('Nome do jogo'); layout.addWidget(self.query)
        self.search_button = QPushButton('Pesquisar'); self.search_button.clicked.connect(self.search); layout.addWidget(self.search_button)
        self.list = QListWidget(); layout.addWidget(self.list)
        self.platform = QLineEdit('PC'); self.platform.setPlaceholderText('Plataforma da sua cópia'); layout.addWidget(self.platform)
        self.state = QLabel('Requer chave RAWG nas configurações.'); self.state.setWordWrap(True); layout.addWidget(self.state)
        self.import_button = QPushButton('Importar resultado selecionado'); self.import_button.clicked.connect(self.import_selected); layout.addWidget(self.import_button)

        from .design_system import dialog_heading
        dialog_heading(layout,'Metadados','Pesquisa manual e identificação de jogos.','search')

    def run_job(self,work,success):
        self.search_button.setEnabled(False); self.import_button.setEnabled(False)
        job = Job(work,self); self.jobs.append(job)
        job.succeeded.connect(success); job.failed.connect(self.failure)
        job.finished.connect(lambda:self.done_job(job)); job.start()

    def done_job(self,job):
        self.jobs.remove(job); job.deleteLater(); self.search_button.setEnabled(True); self.import_button.setEnabled(True)

    def failure(self,message): self.state.setText(message)

    def provider(self):
        return RawgProvider(CredentialVault().get('rawg'))

    def search(self):
        title = self.query.text().strip()
        if not title: return
        self.state.setText('Pesquisando…')
        self.run_job(lambda:self.provider().search(title),self.show_results)

    def show_results(self,results):
        self.results = results; self.list.clear()
        for result in results: self.list.addItem(result.title+' · '+(date_display(result.release_date) or 'Data desconhecida'))
        self.state.setText(f'{len(results)} resultados. Escolha a edição correta antes de importar.')

    def import_selected(self):
        index = self.list.currentRow()
        if index<0: self.state.setText('Selecione um resultado.'); return
        selected = self.results[index]; self.state.setText('Obtendo os detalhes…')
        def fetch():
            result = self.provider().details(selected.external_id)
            return result
        self.run_job(fetch,self.save_result)

    def save_result(self,result):
        existing = self.library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(result.provider,result.external_id)).fetchone()
        if existing:
            self.state.setText('Este resultado já está cadastrado, inclusive se estiver na lixeira.'); return
        try:
            with self.library.sql:
                # save_game usa uma transação própria; inserção do identificador deve permanecer atômica.
                cursor = self.library.sql.execute('INSERT INTO games(title,description,release_date,genre,platform,source) VALUES(?,?,?,?,?,?)',
                    (result.title,result.description,result.release_date,', '.join(result.genres),self.platform.text().strip() or 'PC','RAWG'))
                game_id = cursor.lastrowid
                self.library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(game_id,result.provider,result.external_id))
            self.imported_id = game_id; self.accept()
        except Exception:
            self.state.setText('Não foi possível salvar os metadados.')

    def reject(self):
        if self.jobs:
            self.state.setText('Aguarde a consulta terminar antes de fechar.'); return
        super().reject()

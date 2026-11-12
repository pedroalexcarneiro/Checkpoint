from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

from .integrations import MetadataResult
from .jobs import Job
from .worker import run_isolated


class AutomaticLookup(QDialog):
    def __init__(self, library, title, platform, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Adicionando jogo')
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.path, self.title, self.platform = library.db.path, title, platform
        self.selected_result = None
        self.job = None
        layout = QVBoxLayout(self)
        self.state = QLabel('Buscando ficha e imagens pelo nome do jogo…')
        self.state.setTextFormat(Qt.PlainText)
        layout.addWidget(self.state)
        QTimer.singleShot(0, self.start)

    def start(self):
        self.job = Job(lambda: run_isolated('resolve', self.path, title=self.title, platform=self.platform), self)
        self.job.succeeded.connect(self.found)
        self.job.failed.connect(self.state.setText)
        self.job.finished.connect(self.finished_job)
        self.job.start()

    def found(self, result):
        if result:
            self.selected_result = MetadataResult(**result)

    def finished_job(self):
        self.job.deleteLater()
        self.job = None
        self.accept()

    def reject(self):
        if self.job:
            self.state.setText('Aguarde a consulta terminar. O cadastro será salvo mesmo sem resultado.')
            return
        super().reject()

    def closeEvent(self, event):
        if self.job:
            self.reject()
            event.ignore()
            return
        super().closeEvent(event)

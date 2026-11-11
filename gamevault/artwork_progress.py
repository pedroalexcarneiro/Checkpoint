from PySide6.QtWidgets import QDialog,QVBoxLayout,QLabel
from PySide6.QtCore import QTimer
from .jobs import Job


class ArtworkProgress(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.setWindowTitle('Obtendo artes do jogo');self.resize(500,110)
        self.message='';self.job=None;self.path=library.db.path;self.game_id=game_id
        layout=QVBoxLayout(self);self.state=QLabel('Obtendo capa, banner e logo disponíveis…');self.state.setWordWrap(True);layout.addWidget(self.state)
        QTimer.singleShot(0,self.start)
    def start(self):
        def work():
            from .database import Database
            from .library import Library
            from .auto_artwork import obtain_artwork
            db=Database(self.path)
            try:return obtain_artwork(Library(db),self.game_id)
            finally:db.close()
        self.job=Job(work,self);self.job.succeeded.connect(self.result_ready);self.job.failed.connect(self.result_ready);self.job.finished.connect(self.finish_job);self.job.start()
    def result_ready(self,message):self.message=message
    def finish_job(self):self.job.deleteLater();self.job=None;self.accept()
    def reject(self):
        if self.job:self.state.setText('Aguarde a consulta terminar. O jogo já foi salvo.');return
        super().reject()

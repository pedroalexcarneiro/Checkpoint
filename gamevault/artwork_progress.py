from threading import Event
from PySide6.QtWidgets import QDialog,QVBoxLayout,QLabel,QPushButton
from PySide6.QtCore import QTimer,Signal,Qt
from .jobs import Job


class ArtworkProgress(QDialog):
    progress=Signal(str)
    def __init__(self,library,game_id,parent=None,force=False):
        super().__init__(parent);self.setWindowTitle('Completando ficha e imagens');self.resize(500,110);self.setAttribute(Qt.WA_QuitOnClose,False)
        self.force=force;self.message='';self.job=None;self.path=library.db.path;self.game_id=game_id;self.game_ids=list(game_id) if isinstance(game_id,(list,tuple)) else [game_id]
        layout=QVBoxLayout(self);self.state=QLabel('Obtendo ficha, capa, banner e logo disponíveis…');self.state.setWordWrap(True);self.state.setTextFormat(Qt.PlainText);layout.addWidget(self.state)
        self.stop=Event();self.progress.connect(self.state.setText)
        self.cancel=QPushButton('Parar após o jogo atual');self.cancel.clicked.connect(self.stop.set);layout.addWidget(self.cancel)
        QTimer.singleShot(0,self.start)
    def start(self):
        def work():
            from .database import Database
            from .library import Library
            from .worker import run_isolated
            db=Database(self.path)
            try:
                lib=Library(db)
                messages=[]
                for index,identity in enumerate(self.game_ids):
                    if self.stop.is_set():
                        messages.append('Consulta interrompida. Jogos e resultados já salvos foram preservados.');break
                    game=lib.get(identity)
                    self.progress.emit(f'{index+1}/{len(self.game_ids)} · '+(game['title'] if game else 'Jogo indisponível'))
                    try:result=run_isolated('enrich',self.path,game_id=identity,force=self.force)
                    except Exception as error:result=str(error) if isinstance(error,RuntimeError) else 'Consulta interrompida; cadastro preservado.'
                    messages.append((game['title']+': ' if game else '')+result)
                return '\n'.join(messages)
            finally:db.close()
        self.job=Job(work,self);self.job.succeeded.connect(self.result_ready);self.job.failed.connect(self.result_ready);self.job.finished.connect(self.finish_job);self.job.start()
    def result_ready(self,message):self.message=message
    def finish_job(self):self.job.deleteLater();self.job=None;self.accept()
    def reject(self):
        if self.job:
            self.stop.set();self.state.setText('Interrompendo após o jogo atual. O cadastro já foi salvo.');return
        super().reject()
    def closeEvent(self,event):
        if self.job:
            self.reject();event.ignore();return
        super().closeEvent(event)

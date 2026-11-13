"""Consultas sequenciais em auxiliares; respeita 10 redirecionamentos por minuto."""
from collections import deque
from functools import partial
from PySide6.QtCore import QObject,QTimer,Slot,Signal
from .jobs import Job
from .worker import run_isolated
from .prices import needs_update


class PriceQueue(QObject):
    updated=Signal(int)
    def __init__(self,library,parent):
        super().__init__(parent);self.library=library;self.pending=deque();self.active=None
        self.timer=QTimer(self);self.timer.setSingleShot(True);self.timer.setInterval(6500);self.timer.timeout.connect(self.start_next)
    def submit(self,ids):
        known=set(self.pending)
        if self.active:known.add(self.active.property('gameId'))
        for identity in ids:
            if not self.library.sql.execute("SELECT 1 FROM external_identifiers WHERE game_id=? AND provider='steam'",(identity,)).fetchone() and not self.library.setting(f'prices.ggdeals.{identity}',{}).get('url'):continue
            if identity not in known and needs_update(self.library,identity):self.pending.append(identity);known.add(identity)
        if not self.active and not self.timer.isActive():self.timer.start(0)
    @Slot()
    def start_next(self):
        if self.active or not self.pending:return
        identity=self.pending.popleft();job=Job(partial(run_isolated,'prices',self.library.db.path,game_id=identity),self);self.active=job;job.setProperty('gameId',identity)
        job.succeeded.connect(self.completed);job.failed.connect(self.failed);job.finished.connect(self.finished);job.start()
    @Slot(object)
    def completed(self,result):self.updated.emit(self.active.property('gameId'))
    @Slot(str)
    def failed(self,message):
        from .library import now
        from .prices import snapshot
        identity=self.active.property('gameId');previous=snapshot(self.library,identity);previous.update({'config_version':self.library.setting('prices.config_version',0),'attempted_at':now(),'state':'unavailable','message':'A consulta de preços não foi concluída.'});self.library.set_setting(f'prices.ggdeals.{identity}',previous);self.updated.emit(identity)
    @Slot()
    def finished(self):
        self.active.deleteLater();self.active=None
        if self.pending:self.timer.start(6500)
    def stop(self):self.pending.clear();self.timer.stop()

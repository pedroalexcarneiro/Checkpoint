"""Fila de enriquecimento da biblioteca, sem loops modais dentro de Salvar."""
from collections import deque
from functools import partial

from PySide6.QtCore import QObject, Signal, Slot

from .jobs import Job
from .worker import run_isolated


class CompletionQueue(QObject):
    updated = Signal(int, str)
    busy_changed = Signal(int)

    def __init__(self, database, parent=None):
        super().__init__(parent)
        self.database = database
        self.pending = deque()
        self.active = None

    def submit(self, game_ids, force=False):
        existing = {item[0] for item in self.pending}
        if self.active:
            existing.add(self.active.property('gameId'))
        for game_id in game_ids:
            if game_id not in existing:
                self.pending.append((game_id, force))
                existing.add(game_id)
        self.start_next()

    def start_next(self):
        if self.active is None and self.pending:
            game_id, force = self.pending.popleft()
            self.active = Job(partial(run_isolated, 'enrich', self.database,
                                      game_id=game_id, force=force), self)
            self.active.setProperty('gameId', game_id)
            self.active.succeeded.connect(self.completed)
            self.active.failed.connect(self.failed)
            self.active.finished.connect(self.finished_job)
            self.active.start()
        self.busy_changed.emit(len(self.pending) + int(self.active is not None))

    @Slot(object)
    def completed(self, message):
        self.updated.emit(self.sender().property('gameId'), str(message))

    @Slot(str)
    def failed(self, message):
        self.updated.emit(self.sender().property('gameId'), message)

    @Slot()
    def finished_job(self):
        self.active.deleteLater()
        self.active = None
        self.start_next()

    @Slot()
    def cancel_pending(self):
        self.pending.clear()
        self.busy_changed.emit(int(self.active is not None))

import time
from PySide6.QtTest import QTest
from checkpoint.completion_queue import CompletionQueue
from checkpoint.integrations import IntegrationError


def wait(queue):
    deadline=time.monotonic()+3
    while queue.active and time.monotonic()<deadline:QTest.qWait(10)
    assert queue.active is None


def test_queue_is_serial_and_continues_after_failure(library,app,monkeypatch):
    calls=[];messages=[];counts=[]
    def run(operation,database,**args):
        calls.append(args['game_id'])
        if args['game_id']==1:raise IntegrationError('Consulta indisponível; jogo preservado.')
        return 'done'
    monkeypatch.setattr('checkpoint.completion_queue.run_isolated',run)
    queue=CompletionQueue(library.db.path)
    queue.updated.connect(lambda identity,message:messages.append((identity,message)))
    queue.busy_changed.connect(counts.append)
    queue.submit([1,1,2])
    wait(queue)
    assert calls==[1,2]
    assert messages==[(1,'Consulta indisponível; jogo preservado.'),(2,'done')]
    assert counts[-1]==0


def test_cancel_drops_pending_games_without_destroying_running_job(library,app,monkeypatch):
    calls=[]
    def run(operation,database,**args):
        calls.append(args['game_id']);time.sleep(.02);return 'done'
    monkeypatch.setattr('checkpoint.completion_queue.run_isolated',run)
    queue=CompletionQueue(library.db.path)
    queue.submit([1,2,3])
    queue.cancel_pending()
    wait(queue)
    assert calls==[1] and not queue.pending

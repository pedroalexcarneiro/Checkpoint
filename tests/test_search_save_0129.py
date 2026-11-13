from dataclasses import asdict
from threading import Event
from PySide6.QtWidgets import QDialog
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult
from checkpoint.game_import import save_import
import time
from PySide6.QtTest import QTest

def wait(app,predicate):
    deadline=time.monotonic()+4
    while not predicate() and time.monotonic()<deadline:app.processEvents();QTest.qWait(10)
    assert predicate()


def test_accept_during_selected_details_waits_and_saves_full_record(library,app,monkeypatch):
    selected=MetadataResult('rawg','7','Example',platforms=('PC',))
    full=MetadataResult('rawg','7','Example',platforms=('PC',),developer='Estúdio',publisher='Editora',description='Descrição completa')
    entered=Event();release=Event()
    def worker(operation,*args,**kwargs):
        entered.set();release.wait(3)
        return {'result':asdict(full),'preview':{}}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    parent=QDialog();dialog=GameDialog(parent,library=library);dialog.show();quick=dialog.quick_add
    quick.candidates=[selected];quick.choose(0);wait(app,entered.is_set)
    dialog.validate()
    try:
        assert dialog.isVisible() and not quick.save.isEnabled()
    finally:
        release.set();wait(app,lambda:not quick.jobs)
    assert dialog.result()==QDialog.Accepted
    identity=save_import(library,dialog.data(),result=dialog.catalog_result)
    game=library.get(identity)
    assert (game['developer'],game['publisher'],game['description'])==('Estúdio','Editora','Descrição completa')
    assert game['source']=='Busca'
    parent.close()

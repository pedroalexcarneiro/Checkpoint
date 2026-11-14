"""Regressões gerais: dois cadastros distintos, sem contas ou rede reais."""
import pytest
from PySide6.QtCore import Qt,QCoreApplication,QEvent
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QLabel
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult

@pytest.fixture(params=[('Aurora','Estúdio Norte',680),('Horizonte','Oficina Sul',1100)])
def sample(request):return request.param

@pytest.fixture
def ui(app,library,folder,monkeypatch,sample):
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *args:None)
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    title,developer,width=sample
    identity=library.save_game({'title':title,'platform':'PC'})
    window=MainWindow(library);window.resize(width+300,800);window.show();app.processEvents()
    yield window,identity
    window.close();window.deleteLater();QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)

def test_selected_drive_result_is_not_not_found(ui,app,sample,monkeypatch):
    window,identity=ui;title,developer,width=sample
    d=GameDialog(window,library=window.library);q=d.quick_add
    d.source_tabs.setCurrentIndex(1);q.timer.stop();d.drive_file_id=identity
    result=MetadataResult('rawg',str(identity),title,developer=developer)
    d.apply_catalog(result);q.show_result(result);q.save.setEnabled(False);q.show_missing_metadata()
    d.resize(width,760);d.show();app.processEvents()
    try:
        assert 'Não encontramos' not in q.state.text()
        assert not q.metadata_unavailable and q.save.isEnabled()
        assert not q.state.geometry().intersects(q.preview.geometry())
        monkeypatch.setattr(q,'lookup',lambda:None)
        q.manual_search();d.apply_catalog(result);q.show_result(result);q.save.setEnabled(False);q.show_missing_metadata()
        assert 'Não encontramos' not in q.state.text() and d.drive_file_id==identity
    finally:d.reject();d.deleteLater();QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)

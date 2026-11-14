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

@pytest.mark.parametrize('field,value',[('description','Um mundo para explorar.'),('cover','imagem-local.png'),('price',2490)])
def test_any_metadata_prevents_empty_notice(ui,app,field,value):
    w,i=ui
    w.library.sql.execute("INSERT INTO game_files(game_id,drive_id,original_name) VALUES(?,?,?)",(i,'fixture-rom','arquivo.nds'));w.library.sql.commit()
    if field=='price':w.library.set_setting(f'prices.ggdeals.{i}',{'lowest':value,'currency':'BRL'})
    else:w.library.save_game({'title':w.library.get(i)['title'],field:value},i)
    w.detail(i);app.processEvents()
    assert not w.detail_page.findChildren(QLabel,'metadataNotice')
    assert not any('A ficha ainda está incompleta' in label.text() for label in w.detail_page.findChildren(QLabel))

def test_price_keeps_last_valid_or_explains_absence(ui):
    from checkpoint.prices import refresh_prices,snapshot
    from checkpoint.price_view import price_summary
    w,i=ui;key=f'prices.ggdeals.{i}'
    w.library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)));w.library.sql.commit()
    class Provider:
        value=1900+i*100
        def prices(self,*args,**kwargs):return {'current':self.value,'currency':'BRL'}
    p=Provider();refresh_prices(w.library,i,p);previous=snapshot(w.library,i)['lowest']
    p.value=None;refresh_prices(w.library,i,p)
    assert snapshot(w.library,i)['lowest']==previous
    frame=price_summary(w.library,w.library.get(i))
    assert any('R$' in label.text() for label in frame.findChildren(QLabel))
    w.library.set_setting(key,{})
    frame=price_summary(w.library,w.library.get(i))
    assert not any(label.text()=='Indisponível' for label in frame.findChildren(QLabel))

def test_artwork_close_refreshes_library_without_restart(ui,folder,monkeypatch):
    from checkpoint.artwork_dialog import ArtworkDialog
    w,i=ui
    image=QImage(120,180,QImage.Format_RGB32);image.fill(QColor('#da4848'));p=folder/'chosen.png';assert image.save(str(p))
    def choose(d):
        w.library.save_game({'title':d.game['title'],'cover':str(p)},i)
        return d.DialogCode.Accepted
    monkeypatch.setattr(ArtworkDialog,'exec',choose)
    w.refresh_library();w.artworks(i)
    row=next(w.gallery.item(n) for n in range(w.gallery.count()) if w.gallery.item(n).data(Qt.UserRole)==i)
    assert row.data(Qt.UserRole+1)['cover']==str(p)

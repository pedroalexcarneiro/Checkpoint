from dataclasses import asdict
from threading import Event
import time
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from checkpoint.dialogs import GameDialog
from checkpoint.window import MainWindow
from checkpoint.integrations import MetadataResult
from checkpoint.unified_catalog import search_titles,selected_details


def wait(app,predicate):
    deadline=time.monotonic()+4
    while not predicate() and time.monotonic()<deadline:app.processEvents();QTest.qWait(10)
    assert predicate()


class Provider:
    def __init__(self,result):self.result=result;self.queries=[]
    def search(self,title):self.queries.append(title);return [self.result]
    def details(self,identity):return self.result


def test_unified_catalog_combines_details_without_provider_selection():
    steam=Provider(MetadataResult('steam','42','Example',platforms=('PC',),images={'cover':'steam-cover'}))
    rawg=Provider(MetadataResult('rawg','9','Example',platforms=('PC',),developer='Studio',description='Description'))
    result=selected_details('steam','42','PC',{'steam':steam,'rawg':rawg})
    assert result.developer=='Studio' and result.description=='Description'
    assert result.identifiers=={'steam':'42','rawg':'9'} and result.images['cover']=='steam-cover'
    assert rawg.queries==['Example']


def test_console_search_does_not_match_pc_edition():
    steam=Provider(MetadataResult('steam','1','Example',platforms=('PC',)))
    console=Provider(MetadataResult('rawg','2','Example',platforms=('Nintendo DS',)))
    result=search_titles('Example','Nintendo DS',{'steam':steam,'rawg':console})
    assert steam.queries==[] and len(result['results'])==1 and result['results'][0]['external_id']=='2'


def test_search_failure_keeps_other_sources_usable():
    class Broken:
        def search(self,title):raise RuntimeError('Unavailable')
    result=search_titles('Example',sources={'steam':Broken(),'rawg':Provider(MetadataResult('rawg','3','Example'))})
    assert len(result['results'])==1 and result['unavailable']==1


def test_search_prefills_form_and_can_save_without_advanced_step(library,app,monkeypatch):
    result=MetadataResult('steam','42','Example',platforms=('PC',),developer='Studio',description='Full description')
    def worker(operation,database,**kwargs):
        if operation=='catalog_search':return {'results':[asdict(result)],'unavailable':0}
        return {'result':asdict(result),'preview':{}}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    window=MainWindow(library);dialog=GameDialog(window,library=library);dialog.show()
    dialog.fields['title'].setText('Example');QTest.keyClick(dialog.quick_add.query,Qt.Key_Return)
    assert dialog.isVisible()
    wait(app,lambda:not dialog.quick_add.jobs)
    assert dialog.catalog_result.external_id=='42'
    assert dialog.data()['developer']=='Studio' and dialog.data()['platform']=='PC'
    assert not dialog.form_scroll.isVisible() and dialog.source_tabs.isVisible()
    dialog.validate();assert dialog.result()==QDialog.Accepted;window.close()


def test_stale_lookup_cannot_overwrite_new_query(library,app,monkeypatch):
    blocked=Event();started=Event()
    def worker(operation,database,**kwargs):
        title=kwargs.get('title','Old' if kwargs.get('identity')=='1' else 'New')
        result=MetadataResult('steam','1' if title=='Old' else '2',title,platforms=('PC',),developer=title+' studio')
        if operation=='catalog_search':return {'results':[asdict(result)],'unavailable':0}
        if kwargs['identity']=='1':started.set();blocked.wait(3)
        return {'result':asdict(result),'preview':{}}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    window=MainWindow(library);dialog=GameDialog(window,library=library);dialog.show()
    dialog.fields['title'].setText('Old');dialog.quick_add.lookup();wait(app,started.is_set)
    dialog.fields['title'].setText('New');dialog.quick_add.lookup();blocked.set()
    wait(app,lambda:not dialog.quick_add.jobs)
    assert dialog.data()['title']=='New' and dialog.data()['developer']=='New studio'
    assert dialog.catalog_result.external_id=='2'
    dialog.reject();window.close()


def test_drive_choice_preserves_original_and_searches_platform(library,app,monkeypatch):
    from checkpoint.integrations.drive import DriveScanner
    DriveScanner(library,None).record({'id':'rom','name':'Example (USA).gba'},'/GBA');library.sql.commit()
    calls=[]
    def worker(operation,database,**kwargs):calls.append((operation,kwargs));return {'results':[],'unavailable':0}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    window=MainWindow(library);dialog=GameDialog(window,library=library);dialog.show()
    file=dict(library.sql.execute('SELECT * FROM game_files').fetchone());dialog.load_drive_file(file)
    wait(app,lambda:not dialog.quick_add.jobs)
    assert dialog.drive_file_id==file['id'] and dialog.data()['platform']=='Game Boy Advance'
    assert calls[0][1]['platform']=='Game Boy Advance'
    assert not dialog.drive_group.isVisible()
    assert library.sql.execute('SELECT original_name FROM game_files').fetchone()[0]=='Example (USA).gba'
    dialog.reject();window.close()


def test_same_title_across_sources_is_one_result_not_a_provider_choice():
    steam=Provider(MetadataResult('steam','42','Example',platforms=('PC',)))
    rawg=Provider(MetadataResult('rawg','9','Example',platforms=('PC','Nintendo Switch')))
    art=Provider(MetadataResult('steamgriddb','8','Example'))
    result=search_titles('Example',sources={'steam':steam,'rawg':rawg,'steamgriddb':art})
    assert len(result['results'])==1
    assert result['results'][0]['identifiers']=={'steam':'42','rawg':'9','steamgriddb':'8'}
    assert set(result['results'][0]['platforms'])=={'PC','Nintendo Switch'}


def test_standalone_dialog_finishes_query_before_destruction(folder):
    import os,subprocess,sys
    script=r"""
import time,sys
from pathlib import Path
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.dialogs import GameDialog
import checkpoint.quick_add as quick
app=QApplication([]);app.setQuitOnLastWindowClosed(False)
db=Database(Path(sys.argv[1])/'standalone.sqlite')
def query(*args,**kwargs):time.sleep(.08);return {'results':[],'unavailable':0}
quick.run_isolated=query
dialog=GameDialog(library=Library(db));dialog.show();dialog.fields['title'].setText('Example');dialog.quick_add.lookup();dialog.reject()
def verify():
 if dialog.quick_add.jobs:QTimer.singleShot(10,verify);return
 assert not dialog.isVisible();app.exit(0)
QTimer.singleShot(10,verify);QTimer.singleShot(3000,lambda:app.exit(5))
result=app.exec();db.close();raise SystemExit(result)
"""
    result=subprocess.run([sys.executable,'-X','faulthandler','-c',script,str(folder.resolve())],env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,timeout=8)
    assert result.returncode==0,result.stdout+'\n'+result.stderr


def test_source_change_rejects_inflight_catalog_and_steam_uses_import(library,app,monkeypatch):
    blocked=Event();started=Event()
    def worker(operation,database,**kwargs):
        started.set();blocked.wait(3)
        return {'results':[asdict(MetadataResult('steam','42','Old',platforms=('PC',)))],'unavailable':0}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    window=MainWindow(library);dialog=GameDialog(window,library=library);dialog.show()
    quick=dialog.quick_add;quick.query.setText('Old');quick.lookup();wait(app,started.is_set)
    dialog.source_tabs.setCurrentIndex(2);blocked.set();wait(app,lambda:not quick.jobs)
    assert dialog.catalog_result is None and quick.candidates==[]
    assert quick.steam_panel.isVisible() and not quick.save.isVisible()
    assert quick.query.isHidden() and not dialog.steam_requested
    dialog.source_tabs.setCurrentIndex(1);app.processEvents()
    assert quick.results.isVisible() and quick.drive_manage.isVisible()
    assert quick.save.isVisible() and quick.timer.isActive() is False
    dialog.reject();window.close()


def test_drive_source_displays_versions_and_preserves_original(library,app,monkeypatch):
    from checkpoint.integrations.drive import DriveScanner
    for region in ('USA','Europe'):
        DriveScanner(library,None).record({'id':region,'name':f'Example ({region}).gba'},'/GBA')
    library.sql.commit();calls=[]
    def worker(operation,database,**kwargs):
        calls.append(kwargs);return {'results':[],'unavailable':0}
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',worker)
    window=MainWindow(library);dialog=GameDialog(window,library=library);dialog.show()
    dialog.source_tabs.setCurrentIndex(1);quick=dialog.quick_add;quick.query.setText('Example');app.processEvents()
    assert quick.results.count()==2 and calls==[] and dialog.drive_file_id is None
    assert 'Europe' in quick.results.item(0).text() and 'USA' in quick.results.item(1).text()
    quick.results.setCurrentRow(1);wait(app,lambda:not quick.jobs)
    assert calls[0]['platform']=='Game Boy Advance'
    assert library.sql.execute('SELECT original_name FROM game_files WHERE id=?',(dialog.drive_file_id,)).fetchone()[0]=='Example (USA).gba'
    assert dialog.data()['source']=='Google Drive'
    quick.save.click();assert dialog.result()==QDialog.Accepted;window.close()

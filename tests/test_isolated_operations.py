from dataclasses import asdict
import json
import sys
import threading
import time
from pathlib import Path
from unittest.mock import Mock

import pytest
from PySide6.QtTest import QTest

from checkpoint.integrations import IntegrationError, MetadataResult
from checkpoint.integrations.drive import DriveScanner
from checkpoint.worker import run_isolated
from checkpoint.automatic_catalog import best_match, resolve_title
from checkpoint.game_import import save_import, complete_identity


TRANSFER = b'isolated transfer fixture'
DOWNLOAD_SCRIPT = '''
import sys
from pathlib import Path
from checkpoint.worker import execute_request
import checkpoint.credentials
from checkpoint.integrations.drive import GoogleDriveClient
class Client:
 def download(self,file_id,target):target.write_bytes(b'isolated transfer fixture')
checkpoint.credentials.CredentialVault=lambda:None
GoogleDriveClient.authenticate=classmethod(lambda cls,*args:Client())
raise SystemExit(execute_request(Path(sys.argv[1])))
'''


def command(script):
    return lambda request: [sys.executable, '-X', 'faulthandler', '-c', script, str(request)]


def add_file(library):
    DriveScanner(library,None).record({'id':'downloadfixture','name':'Example (USA).gba','size':str(len(TRANSFER))},'/GBA')
    library.sql.commit()
    return library.sql.execute('SELECT id FROM game_files').fetchone()[0]


def test_real_worker_entry_does_not_open_gui_or_require_credentials(library):
    assert run_isolated('ping',library.db.path)=={'worker':'ok','schema':4}
    assert library.sql.execute('pragma integrity_check').fetchone()[0]=='ok'
    assert not list((library.db.path.parent/'jobs').iterdir())


def test_abrupt_child_exit_is_reported_without_terminating_parent(library):
    with pytest.raises(IntegrationError,match='continua aberto'):
        run_isolated('enrich',library.db.path,game_id=1,command_factory=command('import os; os._exit(139)'))
    assert library.sql.execute('pragma integrity_check').fetchone()[0]=='ok'


def test_real_transfer_child_adds_library_preserves_original_and_local_file(library,folder):
    identity=add_file(library)
    result=run_isolated('download',library.db.path,file_id=identity,directory=str(folder/'downloads'),
                        command_factory=command(DOWNLOAD_SCRIPT))
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(identity,)).fetchone()
    assert Path(row['local_path']).read_bytes()==TRANSFER and row['available']==1
    assert row['original_name']=='Example (USA).gba'
    assert row['game_id']==result['game_id']
    assert library.get(result['game_id'])['title']=='Example'
    assert library.get(result['game_id'])['platform']=='Game Boy Advance'


def test_drive_ui_survives_art_child_failure_after_real_transfer(library,folder,app,monkeypatch):
    import checkpoint.worker as worker
    from checkpoint.drive_dialog import DriveDialog
    library.set_setting('downloads',str(folder/'downloads'))
    identity=add_file(library)
    original=worker.run_isolated
    called=[];main=threading.get_ident()
    def isolated(operation,path,**arguments):
        assert threading.get_ident()!=main
        called.append(operation)
        script=DOWNLOAD_SCRIPT if operation=='download' else 'import os; os._exit(139)'
        return original(operation,path,command_factory=command(script),**arguments)
    monkeypatch.setattr(worker,'run_isolated',isolated)
    dialog=DriveDialog(library)
    dialog.list.setCurrentRow(0)
    dialog.show()
    dialog.download()
    dialog.close()  # A live worker must prevent destruction of its QThread.
    assert dialog.isVisible()
    deadline=time.monotonic()+15
    while dialog.jobs and time.monotonic()<deadline:QTest.qWait(10)
    assert not dialog.jobs
    assert called==['download','enrich']
    assert 'continua aberto' in dialog.state.text()
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(identity,)).fetchone()
    assert row['available']==1 and Path(row['local_path']).read_bytes()==TRANSFER
    assert library.get(row['game_id'])
    assert all(control.isEnabled() for control in dialog.controls)
    dialog.close()


def test_platform_and_ambiguous_matches_do_not_silently_choose_wrong_edition():
    original=MetadataResult('rawg','1','Example',platforms=('Game Boy Advance',))
    remake=MetadataResult('rawg','2','Example',platforms=('PlayStation 5',))
    assert best_match('Example','GBA',[remake,original])==original
    assert best_match('Example','',[original,remake]) is None
    assert best_match('Completely different','GBA',[original]) is None


def test_automatic_title_lookup_combines_same_title_sources_without_manual_picker():
    rawg=Mock();rawg.search.return_value=[MetadataResult('rawg','1','Example')]
    rawg.details.return_value=MetadataResult('rawg','1','Example',developer='Studio')
    class Artwork:
        def search(self,title):return [MetadataResult('steamgriddb','2','Example')]
    result=resolve_title('Example (USA)','GBA',[rawg,Artwork()])
    assert result.developer=='Studio'
    assert result.identifiers=={'rawg':'1','steamgriddb':'2'}
    rawg.details.assert_called_once_with('1')


def test_conflicting_combined_identities_roll_back_import(library):
    one=save_import(library,{'title':'First'},result=MetadataResult('rawg','1','First'))
    two=save_import(library,{'title':'Second'},result=MetadataResult('steamgriddb','2','Second'))
    with pytest.raises(ValueError):
        save_import(library,{'title':'Merged'},result=MetadataResult('rawg','1','Merged',identifiers={'steamgriddb':'2'}))
    assert len(library.games())==2
    assert library.get(one)['title']=='First' and library.get(two)['title']=='Second'


def test_binding_automatic_result_keeps_personal_fields(library):
    game=library.save_game({'title':'Personal title','developer':'Personal developer','notes':'keep'})
    complete_identity(library,game,MetadataResult('rawg','1','Catalog title',developer='Catalog developer',publisher='Publisher',identifiers={'steamgriddb':'2'}))
    row=library.get(game)
    assert row['title']=='Personal title' and row['developer']=='Personal developer' and row['notes']=='keep'
    assert row['publisher']=='Publisher'
    assert dict(library.sql.execute('SELECT provider,external_id FROM external_identifiers'))=={'rawg':'1','steamgriddb':'2'}


def test_new_game_form_keeps_optional_configuration_collapsed(library,app):
    from checkpoint.dialogs import GameDialog
    dialog=GameDialog(library=library)
    assert dialog.quick_add.query is dialog.fields['title']
    assert dialog.form_scroll.isHidden() and dialog.advanced.isHidden()
    assert dialog.fields['developer'].isVisibleTo(dialog) is False
    editor=GameDialog(game={'title':'Example'},library=library)
    assert editor.editor_tabs.count()==4
    assert editor.fields['developer'].isVisibleTo(editor)
    editor.close();dialog.close()


def test_transfer_child_exit_preserves_partial_without_publishing_corrupt_rom(library,folder):
    identity=add_file(library)
    crashing=DOWNLOAD_SCRIPT.replace("target.write_bytes(b'isolated transfer fixture')", "target.write_bytes(b'partial'); __import__('os')._exit(139)")
    with pytest.raises(IntegrationError,match='continua aberto'):
        run_isolated('download',library.db.path,file_id=identity,directory=str(folder/'downloads'),
                     command_factory=command(crashing))
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(identity,)).fetchone()
    assert row['available']==0 and not row['local_path']
    partials=list((folder/'downloads').glob('*.partial'))
    assert len(partials)==1 and partials[0].read_bytes()==b'partial'
    assert library.sql.execute('pragma integrity_check').fetchone()[0]=='ok'


def test_main_window_close_waits_for_child_operation(library,app,monkeypatch):
    from threading import Event
    from PySide6.QtWidgets import QMessageBox
    from checkpoint.jobs import Job
    from checkpoint.window import MainWindow
    window=MainWindow(library);window.show()
    release=Event()
    job=Job(lambda:release.wait(3),window)
    notices=[]
    monkeypatch.setattr(QMessageBox,'information',lambda *args:notices.append(args[2]))
    job.start()
    window.close()
    assert notices and window.isVisible()
    release.set()
    assert job.wait(3000)
    window.close()


def test_automatic_name_does_not_confuse_sequels():
    result=MetadataResult('steamgriddb','3','Example 3')
    assert best_match('Example 2','',[result]) is None
    assert best_match('Example','',[result]) is None

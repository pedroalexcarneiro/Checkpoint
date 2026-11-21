"""Fila independente de modal, cancelamento e etapas reais de arquivo/vínculo."""
from pathlib import Path
from threading import Event
from time import monotonic
import hashlib
from PySide6.QtTest import QTest
from checkpoint.integrations.drive import DriveScanner
from checkpoint.transfer_progress import TransferProgress
from checkpoint.transfers import TransferManager
from checkpoint.rom_link import complete_link
from test_bugs_0134 import ui,sample


def wait_for(predicate,seconds=8):
    deadline=monotonic()+seconds
    while not predicate() and monotonic()<deadline:QTest.qWait(5)
    assert predicate(),'A operação não finalizou dentro do limite de teste'


def record(library,identity,name,data=b'fixture ROM',game=None):
    scanner=DriveScanner(library,None)
    scanner.record({'id':identity,'name':name,'size':str(len(data)),
        'md5Checksum':hashlib.md5(data,usedforsecurity=False).hexdigest()},'/Nintendo Switch')
    library.sql.commit()
    row=library.sql.execute('SELECT id FROM game_files WHERE drive_id=?',(identity,)).fetchone()[0]
    if game is not None:
        from checkpoint.rom_link import bind
        bind(library,row,game)
    return row


def test_real_isolated_download_worker_reuses_verified_file_offline(app,library,folder):
    data=b'programa de teste legal'
    file_id=record(library,'offline-fixture','Arquivo local verificado.nsp',data)
    source=folder/'Arquivo local verificado.nsp';source.write_bytes(data)
    with library.sql:library.sql.execute('UPDATE game_files SET available=1,local_path=? WHERE id=?',(str(source),file_id))
    manager=TransferManager(library)
    try:
        task=manager.start(file_id)
        wait_for(lambda:not manager.busy)
        assert task.status=='completed',task.outcome
        assert task.outcome['download_state']=='downloaded'
        assert task.outcome['link_state']=='not_requested'
        assert source.read_bytes()==data and library.games()==[]
    finally:
        manager.timer.stop();manager.deleteLater()


def test_close_monitor_keeps_task_and_app_navigation_available(ui,app,monkeypatch):
    window,game=ui
    title=window.library.get(game)['title']
    window.library.save_game({'title':title,'platform':'Nintendo Switch'},game)
    file_id=record(window.library,'background-fixture',title+'.nsp')
    entered,release=Event(),Event()
    def work(database,file_id,game_id,**options):
        context=TransferProgress(options['progress_path'],options['cancel_path'],options['owner'])
        context.report({'stage':'downloading','received':25,'total':100})
        entered.set()
        while not release.wait(.01):
            if context.cancelled():
                return {'download_state':'cancelled','cancelled':True,'link_state':'not_completed',
                        'metadata_state':'not_started','errors':[],'message':'Cancelado em teste controlado.'}
        return {'download_state':'downloaded','link_state':'linked','metadata_state':'completed','errors':[],'message':'Concluído em fixture.'}
    monkeypatch.setattr('checkpoint.rom_link_dialog.run_link',work)
    dialog=window.link_drive_rom(game)
    try:
        assert not dialog.isModal()
        dialog.chosen(dialog.results.item(0))
        task=dialog.task
        wait_for(entered.is_set)
        duplicate=window.download_manager.start(file_id,game,mode='link')
        assert duplicate is task
        dialog.reject()
        window.navigate(3)
        QTest.qWait(30)
        assert window.current_page==3 and window.download_manager.busy
        window.open_downloads()
        wait_for(lambda:task.progress.get('received')==25)
        from checkpoint.transfer_view import TransferList
        panel=window.pages[5].findChild(TransferList)
        assert panel.cards[task.id].bar.value()==25
        window.download_manager.cancel(task.id)
        wait_for(lambda:not window.download_manager.busy)
        assert task.status=='cancelled'
        assert window.current_page==5
    finally:
        release.set()
        if window.download_manager.busy:
            window.download_manager.cancel_all();wait_for(lambda:not window.download_manager.busy)


def test_queue_cancel_does_not_start_second_download(app,library):
    one=record(library,'queue-one','Primeiro.nsp')
    two=record(library,'queue-two','Segundo.nsp')
    entered,release=Event(),Event();calls=[]
    def work(database,file_id,**options):
        calls.append(file_id);entered.set();release.wait(5)
        return {'download_state':'downloaded','message':'Fixture de fila','errors':[]}
    manager=TransferManager(library)
    try:
        first=manager.start(one,worker=work)
        second=manager.start(two,worker=work)
        wait_for(entered.is_set)
        assert first.job is not None and second.job is None
        manager.cancel(second.id)
        release.set();wait_for(lambda:not manager.busy)
        assert calls==[one] and second.status=='cancelled'
        assert not any(row[0] for row in library.sql.execute('SELECT available FROM game_files'))
    finally:
        release.set()
        if manager.busy:manager.cancel_all();wait_for(lambda:not manager.busy)
        manager.timer.stop();manager.deleteLater()


def test_cancel_before_new_file_verified_preserves_old_link(library,folder):
    game=library.save_game({'title':'Aventura','platform':'Nintendo Switch'})
    old_data=b'old ROM';new_data=b'new ROM'
    new=record(library,'candidate-new','Aventura.nsp',new_data)
    old=record(library,'candidate-old','Aventura (USA).nsp',old_data,game)
    original=folder/'original.nsp';original.write_bytes(old_data)
    with library.sql:library.sql.execute('UPDATE game_files SET available=1,local_path=? WHERE id=?',(str(original),old))
    cancel=folder/'cancel'
    class Client:
        def download(self,identity,target,**options):target.write_bytes(b'partial');cancel.touch()
    result=complete_link(library,new,game,client=Client(),sources={},progress_path=folder/'progress.json',cancel_path=cancel)
    assert result['cancelled'] and result['link_state']=='not_completed'
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(old,)).fetchone()[0]==game
    assert library.sql.execute('SELECT game_id,available FROM game_files WHERE id=?',(new,)).fetchone()[:]==(None,0)
    assert original.read_bytes()==old_data


def test_metadata_failure_does_not_falsify_download_failure(library,folder):
    data=b'new ROM'
    game=library.save_game({'title':'Aventura','platform':'Nintendo Switch'})
    file_id=record(library,'valid-new','Aventura.nsp',data)
    class Client:
        def download(self,identity,target,**options):target.write_bytes(data)
    class Empty:
        def search(self,title):return []
    result=complete_link(library,file_id,game,client=Client(),sources={'rawg':Empty()},
                         progress_path=folder/'progress.json',cancel_path=folder/'cancel')
    assert result['download_state']=='downloaded' and result['link_state']=='linked'
    assert result['metadata_state']=='pending' and result['errors']
    assert result['transfer_state']=='completed' and result['verification_state']=='completed'
    row=library.sql.execute('SELECT game_id,available,local_path FROM game_files WHERE id=?',(file_id,)).fetchone()
    assert row['game_id']==game and row['available']==1
    assert Path(row['local_path']).read_bytes()==data


def test_close_app_offers_back_then_waits_for_cooperative_cancellation(ui,app,monkeypatch):
    from PySide6.QtWidgets import QMessageBox
    window,game=ui
    file_id=record(window.library,'close-fixture','Fechamento.nsp')
    entered,release=Event(),Event()
    def work(database,file_id,**options):
        context=TransferProgress(options['progress_path'],options['cancel_path'],options['owner'])
        entered.set()
        while not release.wait(.01):
            if context.cancelled():return {'download_state':'cancelled','cancelled':True,'message':'Cancelado.'}
        return {'download_state':'cancelled','cancelled':True,'message':'Cancelado.'}
    try:
        task=window.download_manager.start(file_id,worker=work)
        wait_for(entered.is_set)
        monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a,**k:QMessageBox.No)
        assert window.close() is False
        assert task.active and window.isVisible()
        monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a,**k:QMessageBox.Yes)
        window.close()
        wait_for(lambda:not window.download_manager.busy)
        wait_for(lambda:not window.isVisible())
        assert task.status=='cancelled'
    finally:
        release.set()
        if window.download_manager.busy:
            window.download_manager.cancel_all();wait_for(lambda:not window.download_manager.busy)


def test_checksum_failure_keeps_transport_and_verification_separate(library,folder):
    from checkpoint.transfer_download import download_only
    data=b'good ROM'
    file_id=record(library,'checksum-only','Integridade.nsp',data)
    class Corrupted:
        def download(self,identity,target,**options):target.write_bytes(b'bad! ROM')
    result=download_only(library,file_id,client=Corrupted(),directory=folder/'downloads',
                         progress_path=folder/'progress.json')
    assert result['download_state']=='failed'
    assert result['transfer_state']=='completed'
    assert result['verification_state']=='failed'
    assert 'MD5' in result['message']
    assert library.sql.execute('SELECT available FROM game_files WHERE id=?',(file_id,)).fetchone()[0]==0
    assert not list((folder/'downloads').glob('*.nsp'))
    assert list((folder/'downloads').glob('*.partial'))


def test_restart_keeps_interrupted_transfer_without_starting_worker(app,library):
    from checkpoint.transfers import Transfer
    task=Transfer('a'*32,1,None,'Arquivo.nsp','Arquivo',status='running',progress={'received':12})
    library.set_setting('downloads.transfers',[task.record()])
    manager=TransferManager(library)
    try:
        restored=manager.tasks[task.id]
        assert restored.status=='interrupted' and restored.job is None
        assert not manager.busy
        assert 'reinicia' in restored.outcome['message']
    finally:manager.deleteLater()


def test_owner_identity_prevents_orphan_continuing_after_pid_reuse(folder,monkeypatch):
    import pytest
    from checkpoint import process_liveness
    from checkpoint.transfer_progress import TransferCancelled
    owner=process_liveness.current_owner()
    assert process_liveness.owner_alive(owner)
    context=TransferProgress(folder/'progress.json',owner=owner)
    monkeypatch.setattr(process_liveness,'process_token',lambda pid:'a different process')
    with pytest.raises(TransferCancelled):context.check()


def test_confirmed_windows_shutdown_requests_cancel_without_modal(ui,app,monkeypatch):
    window,game=ui
    file_id=record(window.library,'shutdown-fixture','Desligamento.nsp')
    entered,release=Event(),Event()
    def work(database,file_id,**options):
        context=TransferProgress(options['progress_path'],options['cancel_path'],options['owner'])
        entered.set()
        while not release.wait(.01):
            if context.cancelled():return {'download_state':'cancelled','cancelled':True,'message':'Cancelado.'}
        return {'download_state':'cancelled','cancelled':True,'message':'Cancelado.'}
    def forbidden(*args,**kwargs):raise AssertionError('Desligamento confirmado não deve abrir confirmação')
    monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',forbidden)
    monkeypatch.setattr('checkpoint.dialog_style.AppMessages.information',forbidden)
    try:
        task=window.download_manager.start(file_id,worker=work)
        wait_for(entered.is_set)
        window.session_events.handle_code(0x16,1)
        assert window.system_shutdown and task.cancel_requested
        window.close()
        wait_for(lambda:not window.download_manager.busy)
    finally:
        release.set()
        if window.download_manager.busy:
            window.download_manager.cancel_all();wait_for(lambda:not window.download_manager.busy)

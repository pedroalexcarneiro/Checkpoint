"""Recuperação manual real e política de fonte dos dados de ROMs."""
import json
from pathlib import Path
import sys
import time
from unittest.mock import Mock
from PySide6.QtCore import Qt, QTimer
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QPushButton
from checkpoint.integrations import MetadataResult
from checkpoint.integrations.drive import DriveScanner
from checkpoint.game_import import save_import
from checkpoint.enrichment import complete_game
from scripts.drive_search_flow_support import EMERALD, ROM_NAME, save_via_drive


def test_drive_enrichment_uses_text_but_not_rawg_images(library):
    DriveScanner(library,None).record({'id':'policy-rom','name':ROM_NAME},'/Roms/GBA')
    library.sql.commit()
    file_id=library.sql.execute('SELECT id FROM game_files').fetchone()[0]
    identity=save_import(library,{'title':'Pokemon Emerald','source':'Google Drive'},file_id,
                         MetadataResult('rawg','11','Pokemon Emerald'))
    provider=Mock();provider.details.return_value=MetadataResult('rawg','11','Pokemon Emerald',
        developer='Game Freak',publisher='Nintendo',description='Hoenn',images={'cover':'rawg-image'})
    cache=Mock()
    complete_game(library,identity,rawg_provider=provider,cache=cache)
    game=library.get(identity)
    assert (game['developer'],game['publisher'],game['description'],game['source'])==('Game Freak','Nintendo','Hoenn','Busca')
    assert not game['cover']
    cache.download.assert_not_called()


def test_manual_search_recovers_existing_rom_without_duplicate(app,library,folder,monkeypatch):
    root=folder/'manual-source'
    window,game,file_id,_=save_via_drive(app,library,root,no_results=True)
    (root/'source.json').write_text(json.dumps(EMERALD),encoding='utf-8')
    (root/'details.release').touch()
    from checkpoint.worker import run_isolated
    from checkpoint.jobs import Job
    from checkpoint.credentials import CredentialVault
    support=str(Path('scripts/drive_search_flow_support.py').resolve())
    def isolated(operation,database,**arguments):
        bootstrap="import runpy,sys; m=runpy.run_path(sys.argv[1]); sys.exit(m['drive_worker'](sys.argv[2],sys.argv[3]))"
        return run_isolated(operation,database,command_factory=lambda request:[sys.executable,'-X','faulthandler','-c',bootstrap,support,str(request),str(root)],**arguments)
    monkeypatch.setattr(CredentialVault,'get',lambda *args:None)
    monkeypatch.setattr('checkpoint.quick_add.run_isolated',isolated)
    monkeypatch.setattr('checkpoint.completion_queue.run_isolated',isolated)
    state={'stage':'open','dialog':None,'error':None}
    timer=QTimer();timer.setInterval(10);deadline=time.monotonic()+25
    def tick():
        try:
            assert time.monotonic()<deadline
            dialog=app.activeModalWidget()
            if state['stage']=='open' and dialog and hasattr(dialog,'quick_add'):
                state['dialog']=dialog
                dialog.quick_add.query.selectAll();QTest.keyClicks(dialog.quick_add.query,'Pokemon Emerald')
                QTest.keyClick(dialog.quick_add.query,Qt.Key_Return);state['stage']='choose'
            elif state['stage']=='choose' and dialog.quick_add.results.isVisible() and dialog.quick_add.candidates:
                results=dialog.quick_add.results
                QTest.mouseClick(results.viewport(),Qt.LeftButton,pos=results.visualItemRect(results.item(0)).center())
                state['stage']='save'
            elif state['stage']=='save' and dialog.quick_add.save.isEnabled():
                timer.stop();QTest.mouseClick(dialog.quick_add.save,Qt.LeftButton);state['stage']='saved'
        except BaseException as error:
            state['error']=error;timer.stop()
            if state['dialog']:state['dialog'].reject()
    try:
        button=next(button for button in window.detail_page.findChildren(QPushButton) if button.text()=='Pesquisar manualmente')
        timer.timeout.connect(tick);timer.start();QTest.mouseClick(button,Qt.LeftButton);timer.stop()
        deadline=time.monotonic()+25
        while (any(job.isRunning() for job in window.findChildren(Job)) or window.completion_queue.active or
               (state['dialog'] and state['dialog'].quick_add.jobs)):
            assert time.monotonic()<deadline
            app.processEvents();QTest.qWait(10)
        if state['error']:raise state['error']
        assert state['stage']=='saved'
        assert len(library.games())==1
        updated=library.get(game['id'])
        assert updated['developer']=='Game Freak' and updated['publisher']=='Nintendo'
        assert updated['description']==EMERALD['description'] and updated['source']=='Busca'
        assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file_id,)).fetchone()[0]==game['id']
    finally:
        window.close();app.processEvents()

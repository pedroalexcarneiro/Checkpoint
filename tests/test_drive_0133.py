"""Fluxo por cliques: o catálogo controlado responde apenas ao nome No-Intro limpo."""
import time
import os
import tempfile
from unittest.mock import patch
import pytest
from PySide6.QtCore import Qt,QTimer,QCoreApplication,QEvent
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QLabel
from checkpoint.integrations.drive import rom_identity,DriveScanner
from checkpoint.integrations import MetadataResult
from checkpoint.window import MainWindow
from checkpoint.jobs import Job

NAMES=[
 ('Legend of Zelda, The - Spirit Tracks (USA) (Rev 1).nds','The Legend of Zelda: Spirit Tracks','Nintendo DS'),
 ('Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip','Yu-Gi-Oh! - Ultimate Masters 2006','Game Boy Advance'),
 ('Zelda (Game & Watch).zip','Zelda (Game & Watch)',''),
 ('Mother 3 [!].gba','Mother 3','Game Boy Advance'),
 ('Legend of Zelda, The - The Minish Cap (USA).gba','The Legend of Zelda: The Minish Cap','Game Boy Advance'),
 ('Little Mermaid, The (USA).nes','The Little Mermaid','NES'),
 ('Amazing Spider-Man, The (USA).gb','The Amazing Spider-Man','Game Boy'),
 ('Legend of Zelda, The - Oracle of Ages (USA, Australia).gbc','The Legend of Zelda: Oracle of Ages','Game Boy Color'),
 ('Legend of Zelda, The - A Link to the Past (USA).sfc','The Legend of Zelda: A Link to the Past','SNES'),
 ('Incredible Hulk, The (Europe).md.zip','The Incredible Hulk','Mega Drive'),
]
@pytest.mark.parametrize('name,title,platform',NAMES)
def test_no_intro_identity(name,title,platform):assert rom_identity(name)==(title,platform)


def drive_flow(app,library,folder,*,missing=False,capture=False):
    import checkpoint.quick_add as quick
    rom=NAMES[0][0];expected=NAMES[0][1];seen=[];errors=[];state={}
    DriveScanner(library,None).record({'id':'controlled-spirit','name':rom},'/ROMs/NDS');library.sql.commit()
    library.set_setting('prices.auto',False);library.set_setting('artwork.auto',False)
    def worker(operation,database,**args):
        if operation=='catalog_search':
            seen.append(args['title'])
            if args['title']!=expected or missing:return {'results':[]}
            return {'results':[MetadataResult('rawg',str(i),expected+suffix,platforms=('Nintendo DS',)).__dict__ for i,suffix in [(1,''),(2,' (outra edição)')]]}
        result=MetadataResult('rawg','1',expected,platforms=('Nintendo DS',),developer='Nintendo EAD',publisher='Nintendo',description='Descrição da fonte controlada.')
        return {'result':result.__dict__}
    with patch('checkpoint.credentials.CredentialVault.get',return_value=None),patch.object(quick,'run_isolated',worker):
        window=MainWindow(library);window.show();app.processEvents()
        timer=QTimer();timer.setInterval(10);deadline=time.monotonic()+8
        def tick():
            try:
                assert time.monotonic()<deadline,'Fluxo não concluiu'
                d=app.activeModalWidget()
                if not d or not hasattr(d,'quick_add'):return
                q=d.quick_add;state['dialog']=d
                if 'stage' not in state:
                    QTest.mouseClick(q.sources,Qt.LeftButton,pos=q.sources.tabRect(1).center());QTest.keyClicks(q.query,'Spirit');state['stage']='rom'
                elif state['stage']=='rom' and q.results.count():
                    QTest.mouseClick(q.results.viewport(),Qt.LeftButton,pos=q.results.visualItemRect(q.results.item(0)).center());state['stage']='catalog'
                elif state['stage']=='catalog' and seen and not q.jobs:
                    assert seen==[expected],f'Pesquisa enviada: {seen!r}; esperada: {expected!r}'
                    if missing:
                        assert q.results.isHidden();assert q.manual.isVisible() and q.drive_manage.isVisible()
                        assert q.state.text()=='Não encontramos dados para este jogo. Pesquise manualmente.'
                        assert not library.games()
                    else:
                        assert q.results.isVisible() and q.results.count()==2
                        QTest.mouseClick(q.results.viewport(),Qt.LeftButton,pos=q.results.visualItemRect(q.results.item(0)).center())
                    state['stage']='save'
                elif state['stage']=='save' and not q.jobs and q.save.isEnabled():
                    if capture:
                        from pathlib import Path
                        out=(Path(os.environ.get('CHECKPOINT_TEST_ROOT', tempfile.gettempdir())) / 'checkpoint-0133-evidence');out.mkdir(exist_ok=True)
                        assert d.grab().save(str(out/('drive-sem-resultado.png' if missing else 'drive-resultados.png')))
                    timer.stop();QTest.mouseClick(q.save,Qt.LeftButton)
            except BaseException as exc:
                errors.append(exc);timer.stop();d.reject()
        timer.timeout.connect(tick);timer.start();QTest.mouseClick(window.add_button,Qt.LeftButton);timer.stop()
        while any(j.isRunning() for j in window.findChildren(Job)) or window.completion_queue.active or window.completion_queue.pending:
            app.processEvents();QTest.qWait(10)
        try:
            if errors:raise errors[0]
            game=library.games()[0];game=library.get(game['id'])
            assert game['title']==expected
            assert library.sql.execute('SELECT game_id FROM game_files').fetchone()[0]==game['id']
            if not missing:
                assert game['developer']=='Nintendo EAD' and game['publisher']=='Nintendo' and game['description']
                assert game['source']=='Busca'
            else:
                window.detail(game['id']);app.processEvents()
                heading=window.detail_page.findChild(QLabel,'gameDetailTitle');assert heading and heading.text()==expected
                assert any(label.text()=='Não encontramos dados para este jogo. Pesquise manualmente.' for label in window.detail_page.findChildren(QLabel))
        finally:
            window.close();window.deleteLater();QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)


def test_drive_normalized_search_click_flow(app,library,folder):drive_flow(app,library,folder,capture=True)
def test_drive_no_results_is_explicit_and_link_survives(app,library,folder):drive_flow(app,library,folder,missing=True,capture=True)


def test_articles_and_subtitle_separator():
    assert rom_identity('Journey, A - Home (USA).nes')[0]=='A Journey: Home'
    assert rom_identity('Story, An: Home (Europe).gba')[0]=='An Story: Home'
    assert rom_identity('Adventure, The (USA).nes')[0]=='The Adventure'

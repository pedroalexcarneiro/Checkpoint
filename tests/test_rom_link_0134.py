import hashlib
import time
import pytest
from PySide6.QtCore import Qt,QCoreApplication,QEvent
from PySide6.QtGui import QImage,QColor
from PySide6.QtTest import QTest
from checkpoint.integrations import MetadataResult,IntegrationError
from checkpoint.integrations.drive import DriveScanner
from checkpoint.rom_link import candidates,bind,complete_link

@pytest.fixture(params=[('The Legend of Zelda: A Link to the Past','Legend of Zelda, The - A Link to the Past','SNES','.sfc'),('Metroid Fusion','Metroid Fusion','Game Boy Advance','.gba')])
def rom(request,library,folder):
    title,stem,platform,extension=request.param
    game=library.save_game({'title':title,'platform':platform})
    content=b'controlled-rom';scanner=DriveScanner(library,None)
    for index,tag in enumerate(('(USA)','(USA) (Rev 2)','(Europe) (Rev 3)','(Japan)')):
        scanner.record({'id':'rom'+str(index),'name':stem+' '+tag+extension,'size':str(len(content)),'md5Checksum':hashlib.md5(content,usedforsecurity=False).hexdigest()},'/ROMs/'+platform)
    library.sql.commit();preferred=candidates(library,title,platform)[0]
    image=QImage(240,360,QImage.Format_RGB32);image.fill(QColor('#a54b8f'));path=folder/'source.png';assert image.save(str(path))
    result=MetadataResult('rawg',str(game),title,platforms=(platform,),developer='Estúdio controlado',publisher='Publicadora controlada',description='Aventura da fonte controlada.',release_date='2001-01-01',identifiers={'steamgriddb':str(game)})
    class Provider:
        def search(self,query):return [result]
        def details(self,identity):return result
        def artworks(self,identity,kind):return ['https://cdn.steamgriddb.com/'+kind+'.png']
    class Cache:
        def download(self,url):return str(path)
    class Client:
        def download(self,identity,target):target.write_bytes(content)
    return game,preferred,Provider(),Cache(),Client()

def perform(library,rom,**kwargs):
    game,file,provider,cache,client=rom
    return complete_link(library,file['id'],game,client=client,sources={'rawg':provider},art_provider=provider,cache=cache,**kwargs)

def test_exact_rom_ranking_and_unique_replacement(library,rom):
    game,file,*_=rom;g=library.get(game);rows=candidates(library,g['title'],g['platform'])
    assert len(rows)==3 and rows[0]['original_name'].endswith('(USA) (Rev 2)'+rows[0]['extension'])
    bind(library,rows[0]['id'],game);bind(library,rows[1]['id'],game)
    assert [r[0] for r in library.sql.execute('SELECT id FROM game_files WHERE game_id=?',(game,))]==[rows[1]['id']]
    other=library.save_game({'title':'Outro jogo'});bind(library,rows[2]['id'],other)
    with pytest.raises(ValueError):bind(library,rows[2]['id'],game)
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(rows[1]['id'],)).fetchone()[0]==game

def test_rom_pipeline_download_text_and_art(library,rom):
    outcome=perform(library,rom);game,file,*_=rom;g=library.get(game)
    assert outcome['errors']==[] and all(g[key] for key in ('developer','publisher','description','release_date','cover','banner','logo'))
    assert g['source']=='Busca'
    row=library.sql.execute('SELECT * FROM game_files WHERE game_id=?',(game,)).fetchone()
    from checkpoint.rom_link import verify
    assert row['id']==file['id'] and verify(dict(row))
    assert perform(library,rom)['errors']==[] # Reutiliza e verifica o arquivo, sem sobrescrever.

def test_missing_catalog_keeps_link_and_cause(library,rom):
    game,file,provider,cache,client=rom
    provider.search=lambda query:[]
    outcome=perform(library,rom)
    assert 'nenhum resultado exato' in outcome['message']
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file['id'],)).fetchone()[0]==game
    assert library.setting(f'rom.link.{game}')['errors']

def test_files_dialog_click_runs_and_finishes(app,library,rom,monkeypatch):
    from checkpoint.database import Database
    from checkpoint.library import Library
    from checkpoint.rom_link_dialog import RomLinkDialog
    def worker(database,file_id,game_id):
        db=Database(database)
        try:return perform(Library(db),rom)
        finally:db.close()
    monkeypatch.setattr('checkpoint.rom_link_dialog.run_link',worker)
    d=RomLinkDialog(library,rom[0]);d.show();app.processEvents()
    QTest.mouseClick(d.results.viewport(),Qt.LeftButton,pos=d.results.visualItemRect(d.results.item(0)).center())
    deadline=time.monotonic()+10
    while d.job:
        assert time.monotonic()<deadline
        app.processEvents();QTest.qWait(5)
    assert d.result()==d.DialogCode.Accepted and not d.isVisible()
    assert library.get(rom[0])['description'] and d.outcome['errors']==[]
    d.deleteLater();QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)

def test_failed_link_exposes_cause_and_retry(app,library,rom,monkeypatch):
    from checkpoint.rom_link_dialog import RomLinkDialog
    def unavailable(*args):raise IntegrationError('Conexão indisponível (fonte controlada).')
    monkeypatch.setattr('checkpoint.rom_link_dialog.run_link',unavailable)
    d=RomLinkDialog(library,rom[0]);d.show();app.processEvents()
    QTest.mouseClick(d.results.viewport(),Qt.LeftButton,pos=d.results.visualItemRect(d.results.item(0)).center())
    deadline=time.monotonic()+5
    while d.job:
        assert time.monotonic()<deadline
        app.processEvents();QTest.qWait(5)
    assert d.isVisible() and d.retry.isVisible() and d.query.isEnabled()
    assert d.state.text()==d.outcome['message']=='Conexão indisponível (fonte controlada).'
    assert 'Processando' not in d.state.text()
    d.reject();d.deleteLater();QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)

def test_existing_add_and_manager_also_replace_unique_link(library,rom):
    from checkpoint.trash_import import save_with_prompt
    game,file,provider,*_=rom;assert perform(library,rom)['errors']==[]
    rows=candidates(library,library.get(game)['title'],library.get(game)['platform'])
    result=provider.details(str(game))
    assert save_with_prompt(None,library,library.get(game),rows[1]['id'],result)==game
    assert [r[0] for r in library.sql.execute('SELECT id FROM game_files WHERE game_id=?',(game,))]==[rows[1]['id']]
    DriveScanner(library,None).associate(rows[2]['id'],game)
    assert [r[0] for r in library.sql.execute('SELECT id FROM game_files WHERE game_id=?',(game,))]==[rows[2]['id']]
    assert library.sql.execute('SELECT count(*) FROM rom_versions').fetchone()[0]==3

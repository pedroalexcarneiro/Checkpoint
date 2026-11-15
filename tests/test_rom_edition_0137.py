import pytest
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from checkpoint.integrations.drive import DriveScanner
from checkpoint.rom_link import complete_link


@pytest.mark.parametrize('platform',['','Nintendo 64'])
def test_drive_worker_rejects_distinct_ocarina_edition_before_binding(library,platform):
    game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time','platform':platform,'description':'Manter original'})
    DriveScanner(library,None).record({'id':'edition-3d','name':'The Legend of Zelda - Ocarina of Time 3D.3ds'},'/Nintendo 3DS');library.sql.commit()
    file=library.sql.execute('SELECT * FROM game_files').fetchone();before=library.get(game)
    class NoDownload:
        def download(self,*args):pytest.fail('Não baixar uma edição divergente')
    with pytest.raises(ValueError):complete_link(library,file['id'],game,client=NoDownload(),sources={})
    assert library.get(game)==before
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file['id'],)).fetchone()[0] is None


def test_drive_sheet_shows_divergence_without_starting_job(library,app,monkeypatch):
    from checkpoint.rom_link_dialog import RomLinkDialog
    game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time','platform':''})
    DriveScanner(library,None).record({'id':'edition-3d','name':'The Legend of Zelda - Ocarina of Time 3D.3ds'},'/Nintendo 3DS');library.sql.commit()
    called=[];monkeypatch.setattr('checkpoint.rom_link_dialog.run_link',lambda *a:called.append(a) or {'errors':[],'message':'fixture'})
    dialog=RomLinkDialog(library,game);dialog.show();app.processEvents();assert dialog.results.count()==1
    dialog.chosen(dialog.results.item(0));QTest.qWait(30);app.processEvents()
    assert not called and dialog.job is None
    assert 'edição' in dialog.state.text().lower() and dialog.correct.isVisible()
    dialog.reject()

import pytest
from gamevault.game_import import save_import
from gamevault.integrations import MetadataResult
from gamevault.integrations.drive import DriveScanner


def rom(library,file_id='rom',name='Zelda - the Minish Cap (USA).gba'):
    DriveScanner(library,None).record({'id':file_id,'name':name},'/GBA');library.sql.commit()
    return library.sql.execute('SELECT id FROM game_files WHERE drive_id=?',(file_id,)).fetchone()[0]


def test_catalog_title_is_separate_from_original_rom_name(library):
    file_id=rom(library)
    result=MetadataResult('steamgriddb','42','The Legend of Zelda: The Minish Cap')
    game_id=save_import(library,{'title':result.title,'platform':'Game Boy Advance','source':'Google Drive'},file_id,result)
    assert library.get(game_id)['title']==result.title
    assert library.sql.execute('SELECT original_name FROM game_files').fetchone()[0]=='Zelda - the Minish Cap (USA).gba'
    assert library.sql.execute('SELECT game_id FROM game_files').fetchone()[0]==game_id
    assert library.sql.execute('SELECT external_id FROM external_identifiers').fetchone()[0]=='42'


def test_second_version_reuses_confirmed_identity(library):
    result=MetadataResult('steamgriddb','42','Canonical title')
    first=save_import(library,{'title':result.title},rom(library,'usa'),result)
    data=library.get(first);data['notes']='personal';data['cover']='custom.png';library.save_game(data,first)
    second=save_import(library,{'title':result.title},rom(library,'europe'),result)
    assert first==second and len(library.games())==1
    assert library.get(first)['notes']=='personal' and library.get(first)['cover']=='custom.png'
    assert library.sql.execute('SELECT count(*) FROM rom_versions').fetchone()[0]==2


def test_wrong_existing_link_is_not_silently_replaced(library):
    file_id=rom(library)
    first=save_import(library,{'title':'Existing'},file_id,MetadataResult('steamgriddb','1','Existing'))
    other=save_import(library,{'title':'Other'},None,MetadataResult('steamgriddb','2','Other'))
    with pytest.raises(ValueError):save_import(library,{'title':'Other'},file_id,MetadataResult('steamgriddb','2','Other'))
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file_id,)).fetchone()[0]==first
    assert len(library.games())==2


def test_failed_import_does_not_create_orphan(library):
    with pytest.raises(ValueError):save_import(library,{'title':'Missing'},999)
    assert library.games()==[]


def test_add_form_drive_search_and_metadata_prefill(library,app):
    from gamevault.dialogs import GameDialog
    file_id=rom(library)
    dialog=GameDialog(library=library)
    dialog.drive_query.setText('minish');assert len(dialog.drive_results)==1
    dialog.drive_list.setCurrentRow(0);dialog.choose_drive()
    assert dialog.drive_file_id==file_id
    assert dialog.fields['platform'].text()=='Game Boy Advance'
    result=MetadataResult('rawg','123','The Legend of Zelda: The Minish Cap',description='Description',genres=('Adventure',),developer='Nintendo',publisher='Nintendo',release_date='2004-11-04')
    dialog.apply_catalog(result)
    assert dialog.data()['title']==result.title and dialog.data()['developer']=='Nintendo'
    assert dialog.fields['description'].toPlainText()=='Description'
    new_id=rom(library,'different','Another.gba')
    file=dict(library.sql.execute('SELECT * FROM game_files WHERE id=?',(new_id,)).fetchone())
    dialog.load_drive_file(file)
    assert dialog.catalog_result is None and dialog.data()['description']==''
    dialog.close()


def test_fit_preserves_entire_vertical_art(app):
    from PySide6.QtGui import QPixmap,QImage,QColor,QPainter
    from gamevault.artwork_render import fit_artwork
    original=QImage(120,180,QImage.Format_RGB32);original.fill(QColor('green'))
    painter=QPainter(original);painter.fillRect(0,0,120,10,QColor('red'));painter.fillRect(0,170,120,10,QColor('blue'));painter.end()
    fitted=fit_artwork(QPixmap.fromImage(original),174,232,'#202020').toImage()
    assert fitted.width()==174 and fitted.height()==232
    assert fitted.pixelColor(87,2).red()>200
    assert fitted.pixelColor(87,229).blue()>200
    assert fitted.pixelColor(0,116)==QColor('#202020')


def test_artwork_progress_finishes_and_closes(library,app,monkeypatch):
    from gamevault.artwork_progress import ArtworkProgress
    from PySide6.QtWidgets import QDialog
    from PySide6.QtCore import QTimer
    import gamevault.auto_artwork
    game=library.save_game({'title':'Test'})
    monkeypatch.setattr('gamevault.worker.run_isolated',lambda *args,**kwargs:'done safely')
    dialog=ArtworkProgress(library,game)
    QTimer.singleShot(5000,lambda:dialog.accept() if dialog.isVisible() else None)
    assert dialog.exec()==QDialog.Accepted
    assert dialog.job is None and dialog.message=='Test: done safely'


def test_catalog_selection_closes_with_confirmed_result(app):
    from gamevault.catalog_picker import CatalogPicker
    from PySide6.QtWidgets import QDialog
    dialog=CatalogPicker('Zelda')
    result=MetadataResult('steamgriddb','42','The Legend of Zelda: The Minish Cap')
    dialog.show_results([result]);dialog.list.setCurrentRow(0);dialog.choose()
    assert dialog.selected_result==result and dialog.result()==QDialog.Accepted
    dialog.close()

import pytest
from checkpoint.integrations.drive import DriveScanner,platform_for


def seed(library):
    library.set_setting('drive_scan',{'root':'root','token':'cursor','folders':{'root':'','custom':'/Minha coleção','child':'/Minha coleção/Especial','other':'/Outros'}})
    scanner=DriveScanner(library,None)
    for file_id,parent,path in [('one','custom','/Minha coleção'),('two','child','/Minha coleção/Especial'),('three','other','/Outros')]:
        scanner.record({'id':file_id,'name':'Game.zip','parents':[parent]},path)
    library.sql.commit()
    return scanner


def test_persistent_rules_inherit_and_specific_override(library):
    scanner=seed(library)
    assert scanner.set_folder_platform('custom','PlayStation 2')==2
    assert scanner.set_folder_platform('child','GameCube')==1
    assert scanner.resolve_platform('/Minha coleção/Extra')=='PlayStation 2'
    assert DriveScanner(library,None).resolve_platform('/Minha coleção/Especial')=='GameCube'
    scanner.set_folder_platform('custom','PlayStation')
    assert scanner.resolve_platform('/Minha coleção/Especial')=='GameCube'
    assert scanner.resolve_platform('/Minha coleção diferente')==''
    scanner.set_folder_platform('child',None)
    assert scanner.resolve_platform('/Minha coleção/Especial')=='PlayStation'
    assert library.sql.execute("SELECT platform FROM game_files WHERE drive_id='three'").fetchone()[0]==''
    assert library.setting('drive_scan')['token']=='cursor'


def test_rule_applies_to_new_files_and_renamed_folder_id(library):
    scanner=seed(library);scanner.set_folder_platform('custom','PS2 personalizado')
    scanner.folders['custom']='/Renomeada'
    scanner.record({'id':'new','name':'New.iso','parents':['custom']},'/Renomeada')
    assert library.sql.execute("SELECT platform FROM game_files WHERE drive_id='new'").fetchone()[0]=='PS2 personalizado'


def test_bad_rules_leave_saved_data_unchanged(library):
    scanner=seed(library)
    with pytest.raises(ValueError): scanner.set_folder_platform('missing','PS2')
    with pytest.raises(ValueError): scanner.set_folder_platform('custom','  ')
    assert library.setting('drive_folder_platforms') is None


@pytest.mark.parametrize('folder,platform',[('PS1','PlayStation'),('PSX','PlayStation'),('PS2','PlayStation 2'),('Nintendo GameCube','GameCube'),('NGC','GameCube'),('Nintendo Wii','Wii')])
def test_new_console_aliases(folder,platform):
    assert platform_for('/'+folder)==platform


def test_create_confirmed_game_and_link_version(library):
    scanner=seed(library)
    file_id=library.sql.execute("SELECT id FROM game_files WHERE drive_id='one'").fetchone()[0]
    scanner.set_folder_platform('custom','PlayStation 2')
    game_id=scanner.create_game(file_id,'Confirmed title')
    assert library.get(game_id)['platform']=='PlayStation 2'
    assert library.get(game_id)['cover']==''
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file_id,)).fetchone()[0]==game_id
    assert library.sql.execute('SELECT count(*) FROM rom_versions WHERE file_id=?',(file_id,)).fetchone()[0]==1
    with pytest.raises(ValueError): scanner.create_game(file_id,'Duplicate')
    assert len(library.games())==1


def test_folder_dialog_saves_rule_and_gallery_has_cover_icons(library,app,folder):
    from checkpoint.folder_platform_dialog import FolderPlatformDialog
    from PySide6.QtGui import QImage,QColor
    from checkpoint.window import MainWindow
    seed(library)
    dialog=FolderPlatformDialog(library)
    dialog.folder.setCurrentIndex(dialog.folder.findData('custom'));dialog.platform.setCurrentText('PlayStation 2');dialog.apply()
    assert library.setting('drive_folder_platforms')['custom']=='PlayStation 2'
    image=QImage(30,40,QImage.Format_RGB32);image.fill(QColor('blue'));path=folder/'cover.png';image.save(str(path))
    library.save_game({'title':'Has cover','cover':str(path)})
    window=MainWindow(library);window.refresh_library()
    assert not window.table.item(0,0).icon().isNull()
    window.close();dialog.close()

import json
import sys
from PySide6.QtWidgets import QPushButton, QMessageBox
from checkpoint.database import Database
from checkpoint.library import Library
from test_bugs_0134 import ui, sample


def add_profile(lib, name, platform='CHIP-8'):
    with lib.sql:
        emulator = lib.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)', (name,sys.executable)).lastrowid
        return lib.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',
            (emulator,platform,json.dumps(['{rom}']),'.ch8' if platform=='CHIP-8' else '.z64')).lastrowid


def test_profiles_normalize_extensions_and_reject_invalid_before_writing(library,app,monkeypatch):
    from checkpoint.emulator_dialog import EmulatorProfiles
    from checkpoint.local_rom import compatible_profiles
    messages=[]
    monkeypatch.setattr('checkpoint.dialog_style.AppMessages.warning',lambda *args:messages.append(args[-1]))
    editor=EmulatorProfiles(library)
    editor.name.setText('Emulador de teste');editor.platform.setText('Switch');editor.executable.setText(sys.executable)
    editor.extensions.setText(' NSP, .XCI, nsp, ./teste ')
    editor.save()
    assert 'Extensão inválida' in messages[-1]
    assert library.sql.execute('SELECT count(*) FROM emulators').fetchone()[0]==0
    editor.extensions.setText(' NSP, .XCI, nsp, ');editor.save()
    row=library.sql.execute('SELECT * FROM emulator_profiles').fetchone()
    assert (row['platform'],row['extensions'])==('Nintendo Switch','.nsp, .xci')
    for extension in ('.NSP','xci'):
        assert [profile['id'] for profile in compatible_profiles(library,'Switch',extension)]==[row['id']]
    assert not compatible_profiles(library,'Switch','.zip')
    assert not compatible_profiles(library,'','.nsp')
    editor.close()


def test_metadata_platform_aliases_and_unknown_are_visible_without_rewriting_legacy(ui,app,folder):
    from types import SimpleNamespace
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QLabel
    from checkpoint.local_rom import validate_path
    from checkpoint.metadata_dialog import MetadataDialog
    window,legacy=ui
    saved=window.library.get(legacy)
    for entered,expected in (('', ''),('N64','Nintendo 64'),('pc','PC'),('Switch','Nintendo Switch')):
        dialog=MetadataDialog(window.library)
        assert not dialog.platform.text()
        dialog.platform.setText(entered)
        result=SimpleNamespace(provider='rawg',external_id='fixture-'+entered,title=f'Teste {entered or "sem plataforma"}',
                               description='',release_date='',genres=[])
        dialog.save_result(result)
        game=dialog.imported_id
        assert window.library.get(game)['platform']==expected
        window.refresh_library()
        index=window.platform.findText(expected or 'Não identificada')
        assert index>0
        window.platform.setCurrentIndex(index)
        assert game in [window.game_list.item(n).data(Qt.UserRole) for n in range(window.game_list.count())]
        if not expected:
            window.detail(game)
            assert any(label.text()=='Não identificada' for label in window.detail_page.findChildren(QLabel))
            assert any(button.text()=='Definir plataforma' for button in window.detail_page.findChildren(QPushButton))
    assert window.library.get(legacy)==saved
    rom=folder/'Jogo acentuado.Z64';rom.write_bytes(b'exemplo')
    assert validate_path(rom)['platform']=='Nintendo 64'
    archive=folder/'Desconhecido.zip';archive.write_bytes(b'exemplo')
    assert not validate_path(archive)['platform']


def test_profile_edit_keeps_id_and_remove_preserves_files_and_used_profile(ui, app, folder, monkeypatch):
    from checkpoint.emulator_dialog import EmulatorProfiles
    w, identity = ui
    a = add_profile(w.library,'Primeiro');b = add_profile(w.library,'Segundo')
    path = folder/'Programa Á.ch8';path.write_bytes(bytes.fromhex('00e01200'))
    with w.library.sql:
        file_id=w.library.sql.execute('INSERT INTO game_files(game_id,original_name,local_path,platform,extension) VALUES(?,?,?,?,?)',
            (identity,path.name,str(path),'CHIP-8','.ch8')).lastrowid
        w.library.sql.execute('INSERT INTO rom_versions(file_id,profile_id) VALUES(?,?)',(file_id,a))
    editor = EmulatorProfiles(w.library);editor.show();app.processEvents()
    try:
        editor.list.setCurrentRow(0);editor.name.setText('Nome editado');editor.save()
        assert w.library.sql.execute('SELECT name FROM emulators ORDER BY id').fetchone()[0]=='Nome editado'
        assert [r[0] for r in w.library.sql.execute('SELECT id FROM emulator_profiles ORDER BY id')]==[a,b]
        editor.list.setCurrentRow(0);editor.remove()
        assert 'usado' in editor.state.text()
        assert w.library.sql.execute('SELECT profile_id FROM rom_versions').fetchone()[0]==a
        editor.list.setCurrentRow(1)
        monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *args:QMessageBox.No)
        editor.remove()
        assert w.library.sql.execute('SELECT 1 FROM emulator_profiles WHERE id=?',(b,)).fetchone()
        monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *args:QMessageBox.Yes)
        editor.remove()
        assert not w.library.sql.execute('SELECT 1 FROM emulator_profiles WHERE id=?',(b,)).fetchone()
        assert path.read_bytes()==bytes.fromhex('00e01200')
        assert w.library.sql.execute('SELECT profile_id FROM rom_versions').fetchone()[0]==a
    finally:editor.close()


def test_execution_profile_filters_preserves_on_cancel_and_survives_reopen(ui, app, folder):
    from checkpoint.execution_dialog import ExecutionProfileDialog
    w, identity = ui
    a=add_profile(w.library,'Perfil A');b=add_profile(w.library,'Perfil B');bad=add_profile(w.library,'Incompatível','N64')
    path=folder/'Programa Á.ch8';path.write_bytes(bytes.fromhex('00e01200'))
    with w.library.sql:
        file_id=w.library.sql.execute('INSERT INTO game_files(game_id,original_name,local_path,platform,extension) VALUES(?,?,?,?,?)',
            (identity,path.name,str(path),'CHIP-8','.ch8')).lastrowid
        w.library.sql.execute("INSERT INTO rom_versions(file_id,profile_id,region,revision) VALUES(?,?,'USA','1')",(file_id,a))
    original=w.library.get(identity)
    dialog=ExecutionProfileDialog(w.library,identity,w)
    assert {dialog.profile.itemData(n) for n in range(dialog.profile.count())}=={None,a,b}
    dialog.profile.setCurrentIndex(dialog.profile.findData(b));dialog.reject()
    assert w.library.sql.execute('SELECT profile_id FROM rom_versions').fetchone()[0]==a
    dialog=ExecutionProfileDialog(w.library,identity,w)
    dialog.profile.setCurrentIndex(dialog.profile.findData(b));dialog.save()
    row=w.library.sql.execute('SELECT * FROM rom_versions').fetchone()
    assert row['profile_id']==b and row['region']=='USA' and row['revision']=='1'
    assert w.library.get(identity)==original and path.exists()
    reopened=Database(w.library.db.path)
    try:assert Library(reopened).sql.execute('SELECT profile_id FROM rom_versions').fetchone()[0]==b
    finally:reopened.close()


def test_trash_restores_only_chosen_homonym_and_keeps_navigation(ui, app):
    w, identity=ui
    other=w.library.save_game({'title':w.library.get(identity)['title'],'platform':'Switch','notes':'Preservar'})
    for game_id in (identity,other):w.library.delete(game_id)
    original=[tuple(r) for r in w.library.sql.execute('SELECT * FROM games WHERE id=?',(other,))]
    w.navigate(5)
    index=next(i for i in range(w.settings_tabs.count()) if w.settings_tabs.tabText(i)=='Lixeira')
    w.settings_tabs.setCurrentIndex(index);app.processEvents()
    buttons=[b for b in w.settings_tabs.currentWidget().findChildren(QPushButton) if b.text()=='Restaurar']
    buttons[0].click();app.processEvents()
    assert w.library.get(identity) is not None and w.library.get(other) is None
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM games WHERE id=?',(other,))]==original
    assert w.settings_tabs.tabText(w.settings_tabs.currentIndex())=='Lixeira'
    assert w.library.sql.execute('PRAGMA integrity_check').fetchone()[0]=='ok'


def test_trash_unknown_date_does_not_invent_timestamp(ui,app):
    from checkpoint.trash_view import deletion_label
    from PySide6.QtWidgets import QLabel
    w,identity=ui
    for value in (None,'','data ausente'):
        assert deletion_label(value)=='Data não registrada'
    with w.library.sql:w.library.sql.execute("UPDATE games SET deleted_at='' WHERE id=?",(identity,))
    w.navigate(5)
    index=next(i for i in range(w.settings_tabs.count()) if w.settings_tabs.tabText(i)=='Lixeira')
    w.settings_tabs.setCurrentIndex(index);app.processEvents()
    assert any(label.full_text=='Data não registrada' for label in w.settings_tabs.currentWidget().findChildren(QLabel,'trashDeletedAt'))
    assert w.library.sql.execute('SELECT deleted_at FROM games WHERE id=?',(identity,)).fetchone()[0]==''

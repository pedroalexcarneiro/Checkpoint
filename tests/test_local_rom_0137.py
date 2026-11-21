"""Programas CHIP-8 próprios; execução controlada não homologa emulador do dono."""
import json
import sys
from pathlib import Path
import pytest
from checkpoint.launcher import Launcher,EmulatorCommand
from checkpoint.database import Database
from checkpoint.library import Library


@pytest.fixture(params=[('Programa Á',bytes.fromhex('00e01200')),('Programa Bê',bytes.fromhex('00e0600170011204'))])
def local_rom(library,folder,request):
    title,content=request.param;root=folder/'ROMs com espaço';root.mkdir();path=root/(title+'.ch8');path.write_bytes(content)
    game=library.save_game({'title':title,'platform':'CHIP-8','description':'Metadados preservados'})
    code="from pathlib import Path;import sys;p=Path(sys.argv[1]);b=p.read_bytes();assert len(b)%2==0 and b[:2]==bytes.fromhex('00e0');ops=[int.from_bytes(b[n:n+2],'big') for n in range(0,len(b),2)];assert all(op==0x00e0 or op>>12 in (1,6,7) for op in ops);p.with_suffix('.execution').write_text(str(p),encoding='utf-8')"
    with library.sql:
        emulator=library.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)',('CHIP-8 controlado',sys.executable)).lastrowid
        profile=library.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',(emulator,'CHIP-8',json.dumps(['-c',code,'{rom}']),'.ch8')).lastrowid
    return game,path,profile,content


def test_bind_launch_and_reopen_local_rom_without_drive(library,local_rom,monkeypatch):
    from checkpoint.local_rom import bind_local,compatible_profiles
    game,path,profile,content=local_rom
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *a:pytest.fail('Não acessar cofre'))
    monkeypatch.setattr('checkpoint.integrations.drive.GoogleDriveClient.authenticate',lambda *a,**k:pytest.fail('Não autenticar Drive'))
    before=library.get(game);file_id=bind_local(library,game,path,'CHIP-8',profile)
    row=dict(library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone())
    assert row['drive_id'] is None and row['available'] and Path(row['local_path'])==path
    assert library.get(game)==before and path.read_bytes()==content
    chosen=compatible_profiles(library,'CHIP-8','.ch8')[0]
    launcher=Launcher(library);command=EmulatorCommand.build(chosen['executable'],chosen['arguments_json'],row['local_path'])
    session=launcher.start_command(game,command,True);launcher.active[session][0].wait(timeout=5)
    assert launcher.poll()==[game]
    stored=library.sql.execute('SELECT * FROM play_sessions WHERE id=?',(session,)).fetchone()
    assert stored['state']=='finished' and stored['ended_at'] and stored['pid']>0
    assert path.with_suffix('.execution').read_text(encoding='utf-8')==str(path)
    reopened=Database(library.db.path)
    try:
        assert Library(reopened).get(game)==before
        assert reopened.connection.execute('SELECT profile_id FROM rom_versions WHERE file_id=?',(file_id,)).fetchone()[0]==profile
    finally:reopened.close()


def test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic(library,local_rom):
    from checkpoint.local_rom import bind_local
    game,path,profile,content=local_rom;first=bind_local(library,game,path,'CHIP-8',profile)
    second=path.with_name(path.stem+' (USA).ch8');second.write_bytes(content)
    bind_local(library,game,second,'CHIP-8',profile)
    assert path.read_bytes()==content and second.read_bytes()==content
    assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(first,)).fetchone()[0] is None
    before=[tuple(r) for r in library.sql.execute('SELECT * FROM game_files')]
    with pytest.raises(ValueError):bind_local(library,game,path.with_name('ausente.ch8'),'CHIP-8',profile)
    with pytest.raises(ValueError):bind_local(library,game,path,'Nintendo DS',profile)
    assert [tuple(r) for r in library.sql.execute('SELECT * FROM game_files')]==before


def test_local_link_requires_explicit_profile_capability_and_read_access(library,local_rom,monkeypatch):
    from checkpoint.local_rom import bind_local,compatible_profiles
    game,path,profile,_=local_rom
    assert not compatible_profiles(library,'CHIP-8','.zip')
    with library.sql:library.sql.execute("UPDATE emulator_profiles SET extensions='' WHERE id=?",(profile,))
    with pytest.raises(ValueError):bind_local(library,game,path,'CHIP-8',profile)
    with library.sql:library.sql.execute("UPDATE emulator_profiles SET extensions='.ch8' WHERE id=?",(profile,))
    original=Path.open
    def deny(self,*args,**kwargs):
        if self==path:raise PermissionError('controlled unreadable')
        return original(self,*args,**kwargs)
    monkeypatch.setattr(Path,'open',deny)
    with pytest.raises(ValueError,match='ler'):bind_local(library,game,path,'CHIP-8',profile)
    assert library.sql.execute('SELECT count(*) FROM game_files').fetchone()[0]==0


def test_distinct_ocarina_platform_and_edition_are_not_equivalent(library,folder):
    from checkpoint.local_rom import identity_problem
    game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time','platform':'Nintendo 64'})
    file={'original_name':'The Legend of Zelda - Ocarina of Time 3D.3ds','platform':'Nintendo 3DS'}
    assert identity_problem(library.get(game),file)
    file['platform']='Nintendo 64'
    assert 'edição' in identity_problem(library.get(game),file).lower()


def test_cancel_local_dialog_does_not_change_link(library,local_rom,app):
    from checkpoint.local_rom import bind_local
    from checkpoint.local_rom_dialog import LocalRomDialog
    game,path,profile,_=local_rom;bind_local(library,game,path,'CHIP-8',profile)
    before=[tuple(r) for r in library.sql.execute('SELECT * FROM game_files')]
    dialog=LocalRomDialog(library,game);dialog.select_path(path);dialog.reject()
    assert [tuple(r) for r in library.sql.execute('SELECT * FROM game_files')]==before


def test_play_missing_local_file_offers_relocation_without_session(library,local_rom,app,monkeypatch):
    from checkpoint.local_rom import bind_local
    from checkpoint.window import MainWindow
    from PySide6.QtWidgets import QMessageBox
    game,path,profile,_=local_rom;bind_local(library,game,path,'CHIP-8',profile)
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    w=MainWindow(library);before=library.get(game);path.unlink();calls=[]
    monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a:QMessageBox.Yes)
    monkeypatch.setattr(w,'choose_local_rom',lambda identity:calls.append(identity))
    try:
        w.start_game(library.get(game));assert calls==[game] and not w.launcher.active
        assert library.get(game)==before and library.sql.execute('SELECT count(*) FROM play_sessions').fetchone()[0]==0
        assert library.sql.execute('SELECT count(*) FROM game_files WHERE game_id=?',(game,)).fetchone()[0]==1
    finally:w.close()


def test_local_confirm_button_persists_only_after_click(library,local_rom,app):
    from checkpoint.local_rom_dialog import LocalRomDialog
    from PySide6.QtCore import Qt
    from PySide6.QtTest import QTest
    game,path,profile,_=local_rom;dialog=LocalRomDialog(library,game);dialog.select_path(path);dialog.show();app.processEvents()
    assert dialog.confirm.isEnabled() and library.sql.execute('SELECT count(*) FROM game_files').fetchone()[0]==0
    QTest.mouseClick(dialog.confirm,Qt.LeftButton);app.processEvents()
    assert dialog.result()==dialog.DialogCode.Accepted
    assert library.sql.execute('SELECT local_path FROM game_files WHERE game_id=?',(game,)).fetchone()[0]==str(path)
def test_rom_source_actions_are_on_one_row(app,library):
    from PySide6.QtWidgets import QPushButton
    from checkpoint.local_rom_dialog import RomSourceDialog
    game=library.save_game({'title':'Pokémon FireRed Version'})
    dialog=RomSourceDialog(library,game)
    dialog.show();app.processEvents()
    try:
        names=('Escolher ROM local','Vincular ROM do Drive','Cancelar')
        buttons={button.text():button for button in dialog.findChildren(QPushButton)}
        local,drive,cancel=[buttons[name] for name in names]
        assert local.y()==drive.y()==cancel.y()
        assert local.geometry().right()<drive.x()<drive.geometry().right()<cancel.x()
        assert cancel.geometry().right()<dialog.width()
    finally:dialog.close();dialog.deleteLater()

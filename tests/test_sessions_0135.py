import pytest,sys
from checkpoint.window import MainWindow
from PySide6.QtWidgets import QMessageBox,QInputDialog
@pytest.mark.parametrize('title,platform,extension',[('Zelda: A Link to the Past','SNES','.sfc'),('Metroid Fusion','GBA','.gba')])
def test_rom_session_finishes_after_real_process_exit(app,library,folder,monkeypatch,title,platform,extension):
 monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *a:None)
 library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
 game=library.save_game({'title':title,'platform':platform})
 rom=folder/('jogo'+extension);rom.write_bytes(b'x')
 with library.sql:
  e=library.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)',('Python teste',sys.executable)).lastrowid
  library.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',(e,platform,'["-c","pass", "{rom}"]',extension))
  f=library.sql.execute('INSERT INTO game_files(game_id,original_name,platform,extension,local_path,available) VALUES(?,?,?,?,?,1)',(game,rom.name,platform,extension,str(rom))).lastrowid
  library.sql.execute('INSERT INTO rom_versions(file_id) VALUES(?)',(f,))
 monkeypatch.setattr('checkpoint.dialog_style.AppInputs.getItem',lambda *a:('Python teste',True))
 monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *a:QMessageBox.Yes)
 w=MainWindow(library)
 try:
  w.launch_rom(game,dict(library.sql.execute('SELECT * FROM game_files WHERE id=?',(f,)).fetchone()))
  session=next(iter(w.launcher.active));w.launcher.active[session][0].wait(timeout=10)
  assert w.launcher.poll()==[game]
  assert not w.launcher.active
  assert library.sql.execute('SELECT state FROM play_sessions WHERE id=?',(session,)).fetchone()[0]=='finished'
 finally:w.close();w.deleteLater()

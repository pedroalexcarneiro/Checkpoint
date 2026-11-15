"""Comandos de ROM originados pela ação principal, em dois jogos."""
import sys
import pytest
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('title,platform,extension',[
 ('Zelda: A Link to the Past','SNES','.sfc'),('Metroid Fusion','GBA','.gba')])
def test_main_play_routes_linked_rom(ui,folder,monkeypatch,title,platform,extension):
 w,i=ui
 w.library.save_game({'title':title,'platform':platform,'executable':sys.executable},i)
 rom=folder/('ROM com espaço'+extension);rom.write_bytes(b'fixture')
 with w.library.sql:
  w.library.sql.execute('INSERT INTO game_files(game_id,original_name,platform,extension,available,local_path) VALUES(?,?,?,?,1,?)',(i,rom.name,platform,extension,str(rom)))
 calls=[];monkeypatch.setattr(w,'launch_rom',lambda game,file:calls.append((game,file)))
 monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
 w.start_game(w.library.get(i))
 assert len(calls)==1 and calls[0][0]==i and calls[0][1]['local_path']==str(rom)

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_rom_launch_monitors_emulator_exit(ui,folder,monkeypatch,title):
 from PySide6.QtWidgets import QInputDialog,QMessageBox
 w,i=ui;platform,extension=('Game Boy Advance','.gba') if title=='Metroid Fusion' else ('SNES','.sfc')
 w.library.save_game({'title':title,'platform':platform},i)
 rom=folder/('jogo'+extension);rom.write_bytes(b'x')
 with w.library.sql:
  emulator=w.library.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)',('Teste',sys.executable)).lastrowid
  w.library.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,extensions) VALUES(?,?,?)',(emulator,platform,extension))
  file=w.library.sql.execute('INSERT INTO game_files(game_id,original_name,platform,local_path,available) VALUES(?,?,?,?,1)',(i,rom.name,platform,str(rom))).lastrowid
  w.library.sql.execute('INSERT INTO rom_versions(file_id) VALUES(?)',(file,))
 monkeypatch.setattr(QInputDialog,'getItem',lambda *a:('Teste',True))
 monkeypatch.setattr(QMessageBox,'question',lambda *a:QMessageBox.Yes)
 commands=[];monkeypatch.setattr(w.launcher,'start_command',lambda *args:commands.append(args))
 w.launch_rom(i,dict(w.library.sql.execute('SELECT * FROM game_files WHERE id=?',(file,)).fetchone()))
 assert commands[0][2] is True

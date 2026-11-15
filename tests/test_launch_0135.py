"""Comandos de ROM originados pela ação principal, em dois jogos."""
import sys
import pytest
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('title,platform,extension',[
 ('Zelda: A Link to the Past','SNES','.sfc'),('Metroid Fusion','GBA','.gba')])
def test_main_play_routes_linked_rom(ui,folder,monkeypatch,title,platform,extension):
 w,i=ui
 w.library.save_game({'title':title,'executable':sys.executable},i)
 rom=folder/('ROM com espaço'+extension);rom.write_bytes(b'fixture')
 with w.library.sql:
  w.library.sql.execute('INSERT INTO game_files(game_id,original_name,platform,extension,available,local_path) VALUES(?,?,?,?,1,?)',(i,rom.name,platform,extension,str(rom)))
 calls=[];monkeypatch.setattr(w,'launch_rom',lambda game,file:calls.append((game,file)))
 monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
 w.start_game(w.library.get(i))
 assert len(calls)==1 and calls[0][0]==i and calls[0][1]['local_path']==str(rom)

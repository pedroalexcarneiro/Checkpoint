import json
import sys
import time
from pathlib import Path
import pytest
from gamevault.launcher import Launcher,EmulatorCommand
from gamevault.integrations.metadata import RawgProvider

def test_metadata_requires_selection_and_parses_without_network():
    class Http:
        def json(self,url):
            return {'results':[{'id':42,'name':'Game','released':None,'platforms':None,'genres':[]}]}
    results=RawgProvider('test-key',Http()).search('Game')
    assert len(results)==1 and results[0].external_id=='42' and results[0].platforms==()

def test_emulator_arguments_no_shell(folder):
    rom=folder/'game with spaces.sfc'; rom.write_bytes(b'x')
    command=EmulatorCommand.build(sys.executable,json.dumps(['--fullscreen','{rom}']),rom)
    assert command==[sys.executable,'--fullscreen',str(rom.resolve())]
    with pytest.raises(ValueError): EmulatorCommand.build(sys.executable,'["--fullscreen"]',rom)

def test_sessions_recover_without_inventing_duration(library):
    game=library.save_game({'title':'Jogo'})
    with library.sql:
        session=library.sql.execute("INSERT INTO play_sessions(game_id,started_at) VALUES(?,'2026-11-10')",(game,)).lastrowid
    launcher=Launcher(library)
    assert library.sql.execute('SELECT state FROM play_sessions').fetchone()[0]=='interrupted'
    assert library.stats()['seconds']==0
    launcher.resolve(session,120)
    assert library.stats()['seconds']==120
    with pytest.raises(ValueError): launcher.start(library.get(game))

def test_spawn_and_poll_actual_process(library):
    launcher=Launcher(library)
    game=library.save_game({'title':'Processo de teste'})
    session=launcher.start_command(game,[sys.executable,'-c','pass'],True)
    launcher.active[session][0].wait(timeout=10)
    assert launcher.poll()==[game]
    assert library.sql.execute('SELECT state FROM play_sessions WHERE id=?',(session,)).fetchone()[0]=='finished'
    assert not launcher.active

def test_emulator_exit_does_not_infer_rom_session_end(library):
    launcher=Launcher(library)
    game=library.save_game({'title':'Emulador de teste'})
    session=launcher.start_command(game,[sys.executable,'-c','pass'],False)
    launcher.active[session][0].wait(timeout=10)
    assert launcher.poll()==[] and session in launcher.active
    launcher.finish(session)
    assert library.stats()['sessions']==1

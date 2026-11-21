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


def test_play_button_closes_only_its_tracked_session_and_saves_after_exit(app,library,folder,monkeypatch):
    from PySide6.QtWidgets import QPushButton
    from checkpoint.home_components import LastPlayedBanner
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    game=library.save_game({'title':'Jogo de teste','executable':sys.executable})
    stop=folder/'close-request'
    child='from pathlib import Path; import sys, time\nwhile not Path(sys.argv[1]).exists(): time.sleep(.02)'
    window=MainWindow(library)
    monkeypatch.setattr(window.launcher,'start',lambda selected:window.launcher.start_command(
        selected['id'],[sys.executable,'-c',child,str(stop)],True))
    requests=[]
    def request(process):
        requests.append(process.pid)
        stop.touch()
        return True
    monkeypatch.setattr('checkpoint.process_liveness.request_game_close',request)
    def button(title):
        return next(b for b in window.detail_page.findChildren(QPushButton) if b.text()==title)
    try:
        window.detail(game);button('Jogar').click()
        session=window.launcher.active_session(game)
        process=window.launcher.active[session][0]
        assert not window.launcher.request_close(session+1,game)
        window.navigate(0)
        assert window.pages[0].findChild(LastPlayedBanner).play_button.text()=='Finalizar'
        window.detail(game);button('Finalizar').click()
        assert requests==[process.pid]
        assert window.status_toast.label.text()=='Confirme na tela do jogo'
        assert library.sql.execute('SELECT state FROM play_sessions WHERE id=?',(session,)).fetchone()[0]=='active'
        process.wait(timeout=5);window.poll_sessions();assert button('Jogar')
        assert library.sql.execute('SELECT state FROM play_sessions WHERE id=?',(session,)).fetchone()[0]=='finished'
    finally:
        stop.touch()
        if window.launcher.active:
            window.launcher.active[session][0].wait(timeout=5);window.poll_sessions()
        window.close();window.deleteLater()

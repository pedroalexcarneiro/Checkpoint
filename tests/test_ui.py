import os
from pathlib import Path
import pytest
from PySide6.QtCore import Qt,QBuffer,QIODevice
from PySide6.QtGui import QFontDatabase,QImage
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication,QDialog,QLineEdit
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.theme import DARK
from checkpoint.integrations.images import ImageCache
from checkpoint.integrations import IntegrationError


def test_navigate_and_game_detail_with_real_database(app,library,folder):
    window=MainWindow(library); window.show(); app.processEvents()
    for index in range(6):
        window.navigate(index); app.processEvents()
        assert window.stack.currentIndex()==index
    game=library.save_game({'title':'Teste automatizado','platform':'PC','status':'Jogando'})
    library.add_diary(game,'Memória de teste')
    window.navigate(1); window.search.setText('automatizado'); app.processEvents()
    assert window.gallery.count()==1
    window.view.setCurrentIndex(1); assert window.table.rowCount()==1
    window.detail(game); app.processEvents()
    assert window.current_game==game
    window.navigate(0); app.processEvents()
    assert window.grab().save(str(folder/'render.png'))
    window.close()

def test_game_form_validation_and_round_trip(app):
    dialog=GameDialog(); dialog.validate()
    assert dialog.result()!=QDialog.Accepted
    QTest.keyClicks(dialog.fields['title'],'Game name')
    dialog.fields['release_date'].setText('2026-99-50'); dialog.validate()
    assert dialog.result()!=QDialog.Accepted
    dialog.fields['release_date'].setText('2026-11-10'); dialog.fields['rating'].setValue(8)
    dialog.validate(); assert dialog.result()==QDialog.Accepted
    assert dialog.data()['title']=='Game name' and dialog.data()['rating']==8
    edit=GameDialog(game=dialog.data()); assert edit.data()==dialog.data()


def test_game_form_file_buttons_keep_their_field(app,folder,monkeypatch):
    from PySide6.QtWidgets import QPushButton,QFileDialog
    selected=folder/'selected.png'
    image=QImage(10,10,QImage.Format_RGB32); image.fill(Qt.green); assert image.save(str(selected))
    filters=[]
    def choose(parent,title,directory,file_filter):
        filters.append(file_filter)
        return str(selected),''
    monkeypatch.setattr(QFileDialog,'getOpenFileName',choose)
    dialog=GameDialog()
    try:
        buttons={button.property('gameField'):button for button in dialog.findChildren(QPushButton) if button.property('gameField')}
        assert set(buttons)=={'cover','banner','logo','executable'}
        for key,button in buttons.items():
            before={name:dialog.fields[name].text() for name in buttons}
            button.click()
            assert dialog.fields[key].text()==str(selected)
            assert all(dialog.fields[name].text()==value for name,value in before.items() if name!=key)
            assert ('Executáveis' if key=='executable' else 'Imagens') in filters[-1]
    finally:
        dialog.close()


def test_parentless_game_form_process_exits_cleanly(folder):
    # A falha nativa anterior ocorria após pytest anunciar sucesso, no shutdown.
    # Verificar o retorno do processo filho detecta o crash sem mascará-lo.
    import os
    import subprocess
    import sys
    code='''
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.dialogs import GameDialog
app=QApplication([])
db=Database(Path(sys.argv[1])/'shutdown.sqlite')
def open_and_close():
    dialog=GameDialog(library=Library(db))
    dialog.close()
for _ in range(3):
    open_and_close()
db.close()
print('form lifecycle complete',flush=True)
'''
    result=subprocess.run([sys.executable,'-X','faulthandler','-c',code,str(folder)],
        env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,timeout=15)
    assert result.returncode==0,result.stdout+'\n'+result.stderr
    assert 'form lifecycle complete' in result.stdout

def test_image_cache_validates_and_deduplicates(app,folder):
    cache=ImageCache(folder/'images')
    with pytest.raises(IntegrationError): cache.store(b'not image')
    image=QImage(30,40,QImage.Format_RGB32); image.fill(Qt.darkGreen)
    buffer=QBuffer(); buffer.open(QIODevice.WriteOnly); image.save(buffer,'PNG'); data=bytes(buffer.data())
    path=cache.store(data)
    assert cache.store(data)==path
    with pytest.raises(IntegrationError): cache.download('http://127.0.0.1/image.png')

def test_session_end_triggers_background_game_backup(app,library,folder):
    import sys
    from checkpoint.save_profiles import SaveProfiles
    from checkpoint.game_saves import GameSaveBackups
    game=library.save_game({'title':'Background saves'})
    source=folder/'progress'; source.mkdir(); (source/'game.sav').write_bytes(b'progress')
    SaveProfiles(library).configure(game,source,['*.sav'])
    library.set_setting('save_backups',str(folder/'backups'))
    library.set_setting('auto_save_'+str(game),True)
    window=MainWindow(library)
    session=window.launcher.start_command(game,[sys.executable,'-c','pass'],False)
    window.launcher.active[session][0].wait(timeout=10)
    window.end_session(session,game)
    assert game in window.save_jobs
    from PySide6.QtCore import QEventLoop,QTimer
    loop=QEventLoop(); timeout=QTimer(); timeout.setSingleShot(True)
    timeout.timeout.connect(loop.quit)
    window.save_jobs[game].finished.connect(loop.quit)
    timeout.start(15000); loop.exec(); timeout.stop()
    assert not window.save_jobs
    assert len(GameSaveBackups(library).history(game))==1
    assert library.stats()['sessions']==1
    window.close()

def test_updates_dialog_starts_without_network_or_credentials(app,folder):
    from checkpoint.updates_dialog import UpdatesDialog
    dialog=UpdatesDialog(folder)
    assert not dialog.download.isEnabled() and not dialog.install.isEnabled()
    assert dialog.token.text()==''
    dialog.reject()

def test_updates_require_saving_typed_credential_before_network(app,folder):
    from checkpoint.updates_dialog import UpdatesDialog
    dialog=UpdatesDialog(folder); dialog.token.setText('test-not-saved')
    dialog.check_updates()
    assert not dialog.jobs
    assert 'Salvar credencial' in dialog.state.text()
    dialog.reject()

import os
from pathlib import Path
import pytest
from PySide6.QtCore import Qt,QBuffer,QIODevice
from PySide6.QtGui import QFontDatabase,QImage
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication,QDialog,QLineEdit
from gamevault.window import MainWindow
from gamevault.dialogs import GameDialog
from gamevault.theme import DARK
from gamevault.integrations.images import ImageCache
from gamevault.integrations import IntegrationError

@pytest.fixture(scope='session')
def app():
    application=QApplication.instance() or QApplication([])
    font=Path('C:/Windows/Fonts/segoeui.ttf')
    if font.exists(): QFontDatabase.addApplicationFont(str(font))
    application.setStyle('Fusion'); application.setStyleSheet(DARK)
    yield application

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
    from gamevault.save_profiles import SaveProfiles
    from gamevault.game_saves import GameSaveBackups
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
    from gamevault.updates_dialog import UpdatesDialog
    dialog=UpdatesDialog(folder)
    assert not dialog.download.isEnabled() and not dialog.install.isEnabled()
    assert dialog.token.text()==''
    dialog.reject()

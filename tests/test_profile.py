from pathlib import Path
from PySide6.QtGui import QImage,QColor
from checkpoint.profile_dialog import ProfileDialog
from checkpoint.window import MainWindow


def test_nickname_and_photo_are_local_persistent_and_preserve_original(library,app,tmp_path,monkeypatch):
    image=QImage(160,100,QImage.Format_RGB32);image.fill(QColor('red'))
    original=tmp_path/'photo.png';image.save(str(original));content=original.read_bytes()
    monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(original),''))
    dialog=ProfileDialog(library);dialog.nickname.setText('MeuNick');dialog.choose_photo()
    assert library.setting('profile.avatar','')==''
    dialog.save()
    cached=Path(library.setting('profile.avatar'))
    assert cached.is_file() and cached!=original and original.read_bytes()==content
    window=MainWindow(library);assert window.profile_button.text()=='MeuNick'
    assert not window.profile_button.icon().isNull()
    assert window.profile_button.icon().pixmap(28,28).toImage().pixelColor(14,14).red()>240
    window.set_theme('purple');assert window.profile_button.text()=='MeuNick'
    window.close()
    reopened=MainWindow(library);assert reopened.profile_button.text()=='MeuNick';reopened.close()


def test_profile_cancel_and_remove_photo_keep_saved_name(library,app):
    library.set_setting('profile.name','Nick')
    dialog=ProfileDialog(library);dialog.nickname.setText('Não salvar');dialog.reject()
    assert library.setting('profile.name')=='Nick'
    dialog=ProfileDialog(library);dialog.clear_photo();dialog.save()
    assert library.setting('profile.name')=='Nick' and library.setting('profile.avatar')==''

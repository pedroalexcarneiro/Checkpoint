from pathlib import Path
import pytest
from PySide6.QtGui import QImage,QColor,QPainter
from checkpoint.profile_dialog import ProfileDialog


@pytest.mark.parametrize('shape',[(400,200),(200,400),(24,16)])
def test_crop_zoom_cancel_and_persistence_keep_original(library,app,folder,monkeypatch,shape):
    image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('red'));p=QPainter(image);p.fillRect(shape[0]//2,0,shape[0]//2,shape[1],QColor('blue'));p.end()
    path=folder/'Foto com espaço e acentuação.png';assert image.save(str(path));before=path.read_bytes()
    monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(path),''))
    dialog=ProfileDialog(library);dialog.choose_photo()
    assert hasattr(dialog,'crop')
    dialog.zoom.setValue(200);dialog.crop.set_center(.75,.5)
    assert library.setting('profile.avatar','')==''
    dialog.reject();assert library.setting('profile.avatar','')=='' and path.read_bytes()==before
    saved=ProfileDialog(library);saved.choose_photo();saved.zoom.setValue(200);saved.crop.set_center(.75,.5);saved.save()
    avatar=Path(library.setting('profile.avatar'));result=QImage(str(avatar))
    assert result.width()==result.height()==256
    assert result.pixelColor(128,128).blue()>200
    assert path.read_bytes()==before and Path(library.setting('profile.avatar_original')).read_bytes()==before
    reopened=ProfileDialog(library);assert reopened.zoom.value()==200
    assert reopened.crop.render_avatar()==result
    previous=library.setting('profile.avatar');reopened.zoom.setValue(300);reopened.reject()
    assert library.setting('profile.avatar')==previous


def test_invalid_profile_photo_keeps_existing_selection(library,app,folder,monkeypatch):
    path=folder/'invalid.png';path.write_bytes(b'not an image')
    monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(path),''))
    library.set_setting('profile.avatar','anterior.png');dialog=ProfileDialog(library);dialog.choose_photo()
    assert dialog.error.text() and dialog.selected is None
    dialog.reject();assert library.setting('profile.avatar')=='anterior.png'


def test_photo_orientation_and_drag_are_applied_without_modifying_source(library,app,folder):
    import struct
    from PySide6.QtCore import Qt,QPoint
    from PySide6.QtTest import QTest
    image=QImage(80,40,QImage.Format_RGB32);image.fill(QColor('red'))
    path=folder/'oriented.jpg';assert image.save(str(path),'JPEG')
    data=path.read_bytes();exif=b'Exif\0\0'+b'II'+struct.pack('<HIH',42,8,1)+struct.pack('<HHI',274,3,1)+struct.pack('<H',6)+b'\0\0'+struct.pack('<I',0)
    data=data[:2]+b'\xff\xe1'+struct.pack('>H',len(exif)+2)+exif+data[2:];path.write_bytes(data)
    dialog=ProfileDialog(library);assert dialog.select_photo(path)
    assert dialog.crop.source.width()==40 and dialog.crop.source.height()==80
    dialog.show();dialog.zoom.setValue(200);app.processEvents();before=dialog.crop.state()
    QTest.mousePress(dialog.crop,Qt.LeftButton,Qt.NoModifier,QPoint(120,120))
    QTest.mouseMove(dialog.crop,QPoint(80,100));QTest.mouseRelease(dialog.crop,Qt.LeftButton,Qt.NoModifier,QPoint(80,100))
    assert dialog.crop.state()!=before
    dialog.save();assert path.read_bytes()==data
    assert QImage(library.setting('profile.avatar')).size().width()==256

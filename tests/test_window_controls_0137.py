from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
from test_bugs_0134 import ui,sample


def test_window_controls_use_regular_window_close_and_restore(ui,app,monkeypatch):
    w,_=ui
    bar=w.findChild(type(w.menuWidget()),'windowControls')
    assert bar is not None
    called=[]
    with monkeypatch.context() as patch:
        patch.setattr(w,'close',lambda:called.append('close'))
        bar.close_button.click();assert called==['close']
    bar.maximize.click();app.processEvents();assert w.isMaximized()
    assert bar.maximize.accessibleName()=='Restaurar'
    bar.maximize.click();app.processEvents();assert not w.isMaximized()
    assert bar.maximize.accessibleName()=='Maximizar'
    assert bar.minimize.accessibleName()=='Minimizar'
    assert all(b.focusPolicy()==Qt.StrongFocus for b in (bar.minimize,bar.maximize,bar.close_button))
    bar.close_button.click();app.processEvents()
    assert not w.isVisible() and w.capture_shortcut.identity is None
    if w.capture_shortcut.local is not None:assert not w.capture_shortcut.local.isEnabled()


def test_native_hit_regions_preserve_resize_and_caption_controls():
    from checkpoint.window_controls import border_hit
    assert border_hit(1,1,1280,800,8)==13
    assert border_hit(1279,799,1280,800,8)==17
    assert border_hit(400,1,1280,800,8)==12
    assert border_hit(400,100,1280,800,8) is None

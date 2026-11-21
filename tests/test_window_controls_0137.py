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


def test_status_toast_slides_inside_window_without_expanding_status_bar(ui,app):
    window,_=ui
    toast=window.status_toast
    root=window.centralWidget()
    initial=root.size()
    bar=window.statusBar()
    bar.showMessage('Confirme na tela do jogo')
    assert toast.isVisible() and toast.x()<0
    assert bar.currentMessage()==toast.label.text() and not bar.isVisible()
    toast.animation.setCurrentTime(toast.animation.duration())
    assert toast.x()==18 and toast.geometry().bottom()==root.height()-19
    assert root.size()==initial
    window.resize(1200,780);app.processEvents()
    assert toast.geometry().bottom()==root.height()-19
    bar.clearMessage()
    toast.animation.setCurrentTime(toast.animation.duration()//2)
    assert -toast.width()<toast.x()<18
    toast.animation.setCurrentTime(toast.animation.duration())
    assert toast.isHidden()


def test_repeated_restore_keeps_current_detail_geometry_and_download(ui,app):
    from uuid import uuid4
    from checkpoint.transfers import Transfer
    w,identity=ui
    w.resize(1280,800);w.detail(identity);w.detail_tabs.setCurrentIndex(3)
    task=Transfer(uuid4().hex,1,identity,'Arquivo de teste.nsp',w.library.get(identity)['title'],status='running',
                  progress={'stage':'downloading','received':40,'total':100})
    w.download_manager.tasks[task.id]=task;w.download_manager.updated.emit(task)
    def settle():
        for _ in range(12):app.processEvents()
    settle()
    expected=w.detail_page.geometry()
    try:
        from checkpoint.transfer_view import TransferList
        for _ in range(3):
            w.menuWidget().minimize.click();settle();assert w.isMinimized()
            w.showNormal();settle()
            assert not w.isMinimized() and w.current_game==identity
            assert w.stack.currentWidget() is w.detail_page and w.detail_tabs.currentIndex()==3
            assert w.detail_page.geometry()==expected
            panel=w.detail_page.findChild(TransferList,'gameTransfers')
            assert panel.cards[task.id].bar.value()==40
            assert w.menuWidget().isVisible() and w.grab().size()==w.size()*w.devicePixelRatioF()
        w.showMaximized();settle();assert w.isMaximized()
        w.showNormal();settle()
        assert w.detail_page.geometry()==expected and w.download_manager.busy
    finally:
        w.download_manager.tasks.clear()

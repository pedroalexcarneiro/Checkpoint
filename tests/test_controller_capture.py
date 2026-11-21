from PySide6.QtCore import QTimer
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QComboBox,QPushButton

from checkpoint.controller_capture import ControllerCapture,PREFERENCE
from checkpoint.switch_controller import CAPTURE_MASK,SwitchDevice
from test_bugs_0134 import ui,sample


class ControllerFixture:
    def __init__(self):
        self.states=[0,0,None,None]
        self.reads=0

    def buttons(self,slot):
        self.reads+=1
        return self.states[slot]


SWITCH_ID='switch:'+'a'*64


class SwitchFixture:
    def __init__(self):
        self.states={SWITCH_ID:SwitchDevice('Switch Pro · USB',9,0)}
        self.reads=0

    def devices(self):
        self.reads+=1
        return self.states


def wait_for_read(backend):
    reads=backend.reads
    for _ in range(100):
        QTest.qWait(10)
        if backend.reads>reads:return
    raise AssertionError('O diálogo não consultou o controle.')


def test_controller_chord_fires_once_and_requires_release_after_reconnect(ui,monkeypatch):
    window,_=ui
    backend=ControllerFixture()
    window.library.set_setting(PREFERENCE,{'slot':1,'buttons':0x1100})
    monitor=ControllerCapture(window,backend);monitor.timer.stop()
    fired=[]
    monkeypatch.setattr(window,'capture_game_window',lambda:fired.append('capture'))
    window.launcher.active[1]=object()
    try:
        # Outro dispositivo pode receber os mesmos botões e permanece fora do vínculo.
        backend.states[0]=0x1100
        for buttons in (0,0x0100,0x1100,0x1100,0x0100,0x1100):
            backend.states[1]=buttons;monitor.poll()
        assert fired==['capture']
        for buttons in (None,0x1100,0x1100,0,0x1100):
            backend.states[1]=buttons;monitor.poll()
        assert fired==['capture','capture']
        window.launcher.active.clear()
        for buttons in (0,0x1100):
            backend.states[1]=buttons;monitor.poll()
        assert fired==['capture','capture']
    finally:
        window.launcher.active.clear();monitor.deleteLater()


def test_controller_dialog_learns_and_persists_pressed_buttons(ui,app):
    window,_=ui
    backend=ControllerFixture()
    monitor=ControllerCapture(window,backend)
    issues=[]
    def configure():
        dialog=app.activeModalWidget()
        try:
            buttons={button.text():button for button in dialog.findChildren(QPushButton)}
            device=dialog.findChild(QComboBox,'captureControllerDevice')
            command=dialog.findChild(QComboBox,'captureControllerCommand')
            device.setCurrentIndex(1)
            assert command.font()==device.font()
            assert command.geometry().top()-device.geometry().bottom()>=12
            assert command.x()==device.x() and command.height()==device.height()
            footer=[buttons[name].geometry() for name in ('Desativar','Gravar comando','Cancelar','Salvar')]
            assert len({(button.y(),button.height()) for button in footer})==1
            assert all(left.right()<right.left() for left,right in zip(footer,footer[1:]))
            assert all(dialog.rect().contains(button) for button in footer)
            command.setCurrentIndex(command.findData(0x1000))
            assert command.currentText()=='A' and buttons['Salvar'].isEnabled()
            buttons['Gravar comando'].click()
            wait_for_read(backend)
            backend.states[1]=0x1100
            wait_for_read(backend)
            backend.states[1]=0
            wait_for_read(backend)
            assert command.currentText()=='LB + A'
            assert buttons['Salvar'].isEnabled()
            buttons['Salvar'].click()
        except BaseException as error:
            issues.append(error);dialog.reject()
    try:
        QTimer.singleShot(0,configure)
        monitor.configure()
        assert not issues,issues
        assert window.library.setting(PREFERENCE)=={'slot':1,'buttons':0x1100}
        assert monitor.slot==1 and monitor.mask==0x1100 and monitor.timer.isActive()
    finally:monitor.timer.stop();monitor.deleteLater()


def test_switch_capture_persists_and_ignores_held_button_at_reconnect(ui,monkeypatch):
    window,_=ui
    backend=SwitchFixture()
    window.library.set_setting(PREFERENCE,{'device':SWITCH_ID,'buttons':CAPTURE_MASK})
    monitor=ControllerCapture(window,ControllerFixture(),switch_backend=backend);monitor.timer.stop()
    fired=[]
    monkeypatch.setattr(window,'capture_game_window',lambda:fired.append('capture'))
    window.launcher.active[1]=object()
    try:
        assert monitor.device==SWITCH_ID and monitor.mask==CAPTURE_MASK
        for instance,buttons in ((9,0),(9,CAPTURE_MASK|0x1000),(9,CAPTURE_MASK),
                                 (10,CAPTURE_MASK),(10,CAPTURE_MASK),(10,0),(10,CAPTURE_MASK)):
            backend.states[SWITCH_ID]=SwitchDevice('Switch Pro · sem fio',instance,buttons)
            monitor.poll()
        assert fired==['capture','capture']
        assert window.library.setting(PREFERENCE)=={'device':SWITCH_ID,'buttons':CAPTURE_MASK}
    finally:
        window.launcher.active.clear();monitor.deleteLater()


def test_switch_dialog_learns_dedicated_capture_button(ui,app):
    window,_=ui
    backend=SwitchFixture()
    monitor=ControllerCapture(window,ControllerFixture(),switch_backend=backend)
    issues=[]
    def configure():
        dialog=app.activeModalWidget()
        try:
            device=dialog.findChild(QComboBox,'captureControllerDevice')
            command=dialog.findChild(QComboBox,'captureControllerCommand')
            buttons={button.text():button for button in dialog.findChildren(QPushButton)}
            assert command.findData(CAPTURE_MASK)==-1
            device.setCurrentIndex(device.findData(SWITCH_ID))
            assert device.currentText()=='Switch Pro · USB'
            assert command.itemText(command.findData(CAPTURE_MASK))=='Captura'
            buttons['Gravar comando'].click()
            wait_for_read(backend)
            backend.states[SWITCH_ID]=SwitchDevice('Switch Pro · USB',9,CAPTURE_MASK)
            wait_for_read(backend)
            backend.states[SWITCH_ID]=SwitchDevice('Switch Pro · USB',9,0)
            wait_for_read(backend)
            assert command.currentText()=='Captura'
            assert buttons['Salvar'].isEnabled()
            buttons['Salvar'].click()
        except BaseException as error:
            issues.append(error);dialog.reject()
    try:
        QTimer.singleShot(0,configure)
        monitor.configure()
        assert not issues,issues
        assert window.library.setting(PREFERENCE)=={'device':SWITCH_ID,'buttons':CAPTURE_MASK}
    finally:monitor.timer.stop();monitor.deleteLater()

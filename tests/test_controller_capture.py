from PySide6.QtCore import QTimer
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QComboBox,QPushButton

from checkpoint.controller_capture import ControllerCapture,PREFERENCE
from test_bugs_0134 import ui,sample


class ControllerFixture:
    def __init__(self):self.states=[0,0,None,None]
    def buttons(self,slot):return self.states[slot]


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
            command.setCurrentIndex(command.findData(0x1000))
            assert command.currentText()=='A' and buttons['Salvar'].isEnabled()
            buttons['Gravar comando'].click()
            QTest.qWait(70)
            backend.states[1]=0x1100
            QTest.qWait(70)
            backend.states[1]=0
            QTest.qWait(70)
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

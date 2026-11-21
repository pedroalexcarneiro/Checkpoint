"""Atalho de captura para controles XInput e Switch Pro."""
import re
import sys
from PySide6.QtCore import QObject,QTimer
from .switch_controller import CAPTURE_MASK,SDL_DLL,SwitchControllers


BUTTONS={0x0001:'↑',0x0002:'↓',0x0004:'←',0x0008:'→',0x0010:'Menu',0x0020:'Visão',
         0x0040:'LS',0x0080:'RS',0x0100:'LB',0x0200:'RB',0x1000:'A',0x2000:'B',
         0x4000:'X',0x8000:'Y'}
SUPPORTED=sum(BUTTONS)
SWITCH_BUTTONS={**BUTTONS,0x0010:'+',0x0020:'−',0x0100:'L',0x0200:'R',CAPTURE_MASK:'Captura'}
PREFERENCE='capture.xinput'


def button_labels(device):
    return SWITCH_BUTTONS if isinstance(device,str) else BUTTONS


def button_names(mask,device=None):
    return ' + '.join(name for bit,name in button_labels(device).items() if mask&bit)


class XInput:
    def __init__(self):
        if sys.platform!='win32':raise OSError('XInput disponível no Windows.')
        import ctypes
        from ctypes import wintypes
        class Gamepad(ctypes.Structure):
            _fields_=[('buttons',wintypes.WORD),('left_trigger',ctypes.c_ubyte),('right_trigger',ctypes.c_ubyte),
                      ('left_x',ctypes.c_short),('left_y',ctypes.c_short),
                      ('right_x',ctypes.c_short),('right_y',ctypes.c_short)]
        class State(ctypes.Structure):
            _fields_=[('packet',wintypes.DWORD),('gamepad',Gamepad)]
        for name in ('xinput1_4','xinput9_1_0'):
            try:self.dll=ctypes.WinDLL(name,winmode=0x800);break
            except OSError:continue
        else:raise OSError('O Windows não forneceu XInput.')
        self.read=self.dll.XInputGetState
        self.read.argtypes=[wintypes.DWORD,ctypes.POINTER(State)]
        self.read.restype=wintypes.DWORD
        self.state=State();self.out=ctypes.byref(self.state)

    def buttons(self,slot):
        if self.read(slot,self.out)!=0:return None
        return self.state.gamepad.buttons&SUPPORTED


class ButtonEdge:
    def __init__(self):
        self.armed=False

    def update(self,state,mask,*,exact=True):
        if state is None:self.armed=False;return False
        if not state&mask:self.armed=True;return False
        if self.armed and state&mask==mask:
            self.armed=False
            return not exact or state==mask
        return False


class ControllerCapture(QObject):
    def __init__(self,window,backend=None,*,switch_backend=None):
        super().__init__(window)
        self.window=window;self.backend=backend;self.edge=ButtonEdge()
        self.switch_backend=switch_backend
        self.switch_injected=switch_backend is not None
        self.switch_available=self.switch_injected or (backend is None and sys.platform=='win32' and SDL_DLL.is_file())
        if self.backend is None:
            try:self.backend=XInput()
            except OSError:pass
        self.timer=QTimer(self);self.timer.setInterval(50);self.timer.timeout.connect(self.poll)
        self.load()

    @property
    def available(self):
        return self.backend is not None or self.switch_available

    def open_switch(self):
        if self.switch_backend is None and self.switch_available:
            try:self.switch_backend=SwitchControllers.windows()
            except (OSError,AttributeError):self.switch_available=False

    def devices(self):
        devices={}
        if self.backend:
            for slot in range(4):
                buttons=self.backend.buttons(slot)
                suffix=' · desconectado' if buttons is None else ''
                devices[slot]=(f'Controle {slot+1} · XInput'+suffix,buttons)
        if self.switch_backend:
            physical=self.switch_backend.devices()
            names=[state.name for state in physical.values()]
            for number,(device,state) in enumerate(sorted(physical.items()),1):
                name=f'{state.name} ({number})' if names.count(state.name)>1 else state.name
                devices[device]=(name,state.buttons)
        return devices

    def load(self):
        value=self.window.library.setting(PREFERENCE,{})
        slot=value.get('slot') if isinstance(value,dict) else None
        mask=value.get('buttons') if isinstance(value,dict) else None
        device=value.get('device') if isinstance(value,dict) else None
        self.slot=slot if type(slot) is int and 0<=slot<4 else None
        self.device=device if isinstance(device,str) and re.fullmatch(r'switch:[a-f0-9]{64}',device) else self.slot
        allowed=SUPPORTED|CAPTURE_MASK if isinstance(self.device,str) else SUPPORTED
        self.mask=mask if type(mask) is int and 0<mask<=allowed and not mask&~allowed else 0
        self.edge=ButtonEdge()
        self.switch_instance=None
        self.timer.stop()
        if isinstance(self.device,str) and self.mask:
            self.open_switch()
            if self.switch_backend:self.timer.start()
        else:
            if self.switch_backend and not self.switch_injected:
                self.switch_backend.close()
                self.switch_backend=None
            if self.backend and self.slot is not None and self.mask:self.timer.start()

    def poll(self):
        if isinstance(self.device,str):
            device=self.switch_backend.devices().get(self.device)
            instance=device.instance if device else None
            if instance!=self.switch_instance:self.edge=ButtonEdge()
            self.switch_instance=instance
            state=device.buttons if device else None
        else:state=self.backend.buttons(self.slot)
        pressed=self.edge.update(state,self.mask,exact=self.mask!=CAPTURE_MASK)
        if pressed and self.window.launcher.active:self.window.capture_game_window()

    def configure(self):
        self.timer.stop()
        self.open_switch()
        try:configure_controller(self)
        finally:self.load()

    def close(self):
        self.timer.stop()
        if self.switch_backend:self.switch_backend.close()


def configure_controller(controller):
    from PySide6.QtCore import QSignalBlocker
    from PySide6.QtGui import QPainter
    from PySide6.QtWidgets import QComboBox,QDialog,QGridLayout,QHBoxLayout,QVBoxLayout
    from .design_system import colors,dialog_heading
    from .dialog_style import prepare_dialog
    from .icons import lucide_icon
    from .ui_components import action,text

    class CaptureSelector(QComboBox):
        def __init__(self):
            super().__init__();self.setMinimumHeight(36)
            self.setStyleSheet('QComboBox::down-arrow { image: none; }')

        def paintEvent(self,event):
            super().paintEvent(event)
            painter=QPainter(self)
            arrow=lucide_icon('chevron',colors()['muted'],18).pixmap(18,18)
            painter.drawPixmap(self.width()-25,(self.height()-18)//2,arrow)

    dialog=prepare_dialog(QDialog(controller.window))
    dialog.setWindowTitle('Captura pelo controle');dialog.resize(520,310)
    layout=QVBoxLayout(dialog)
    dialog_heading(layout,'Captura pelo controle',name='memories')
    inputs=QGridLayout();inputs.setHorizontalSpacing(16);inputs.setVerticalSpacing(0)
    inputs.setRowMinimumHeight(1,12);inputs.setColumnStretch(1,1);layout.addLayout(inputs)
    device=CaptureSelector();device.setObjectName('captureControllerDevice');device.setAccessibleName('Controle')
    inputs.addWidget(text('Controle'),0,0);inputs.addWidget(device,0,1)
    shown_devices=None
    def display_devices(states):
        nonlocal shown_devices
        selected=device.currentData() if shown_devices is not None else controller.device
        entries={key:name for key,(name,_) in states.items()}
        if isinstance(selected,str) and selected not in entries:entries[selected]='Switch Pro · desconectado'
        if not entries:entries[None]='Nenhum controle detectado'
        if entries==shown_devices:return False
        previous=device.currentData()
        with QSignalBlocker(device):
            device.clear()
            for identity,name in entries.items():device.addItem(name,identity)
            if selected not in entries:
                selected=next((key for key,(_,pressed) in states.items() if pressed is not None),next(iter(entries)))
            device.setCurrentIndex(device.findData(selected))
        shown_devices=entries
        return device.currentData()!=previous
    display_devices(controller.devices())

    command=CaptureSelector();command.setObjectName('captureControllerCommand');command.setAccessibleName('Comando')
    def select_command(mask):
        index=command.findData(mask)
        if index<0:
            command.addItem(button_names(mask,device.currentData()),mask)
            index=command.count()-1
        command.setCurrentIndex(index)
    def reset_commands(mask):
        with QSignalBlocker(command):
            command.clear()
            command.addItem('Selecionar botão ou combinação',0)
            if device.currentData() is not None:
                for bit,label in button_labels(device.currentData()).items():command.addItem(label,bit)
            select_command(mask)
    reset_commands(controller.mask if device.currentData()==controller.device else 0)
    command.setEnabled(device.currentData() is not None)
    inputs.addWidget(text('Comando'),2,0);inputs.addWidget(command,2,1)
    state=text('','muted');state.hide();layout.addWidget(state)
    warning=text('Escolha uma combinação que o jogo não use. O comando continua chegando ao jogo.','muted')
    layout.addWidget(warning)
    learning=False;neutral=False;peak=0

    def learn():
        nonlocal learning,neutral,peak
        learning=True;neutral=False;peak=0
        state.setText('Solte os botões e pressione o comando. Depois solte para confirmar.')
        state.show()
        command.setEnabled(False)
        save_button.setEnabled(False)

    def clear_device():
        nonlocal learning,neutral,peak
        learning=False;neutral=False;peak=0
        command.setEnabled(device.currentData() is not None);reset_commands(0)
        save_button.setEnabled(False)

    def tick():
        nonlocal neutral,peak,learning
        states=controller.devices()
        if display_devices(states):clear_device()
        pressed=states.get(device.currentData(),('',None))[1]
        learn_button.setEnabled(pressed is not None)
        if pressed is None:
            state.setText('Conecte um controle XInput ou um Switch Pro por USB ou Bluetooth.')
            neutral=False;peak=0
        elif learning and not neutral and pressed==0:
            neutral=True
            state.setText('Pressione e solte o comando.')
        elif learning and neutral:
            if pressed.bit_count()>peak.bit_count():peak=pressed
            if pressed==0 and peak:
                learning=False
                command.setEnabled(True);select_command(peak);state.clear();save_button.setEnabled(True)
        elif not learning:
            state.clear()
        state.setVisible(bool(state.text()))

    def save():
        mask=command.currentData()
        selected=device.currentData()
        if not mask or selected is None:return
        key='device' if isinstance(selected,str) else 'slot'
        controller.window.library.set_setting(PREFERENCE,{key:selected,'buttons':mask})
        dialog.accept()

    def disable():
        controller.window.library.set_setting(PREFERENCE,{})
        dialog.accept()

    layout.addStretch()
    buttons=QHBoxLayout();buttons.setSpacing(8)
    buttons.addWidget(action('Desativar',disable))
    learn_button=action('Gravar comando',learn);buttons.addWidget(learn_button)
    buttons.addStretch()
    buttons.addWidget(action('Cancelar',dialog.reject))
    save_button=action('Salvar',save,True);save_button.setEnabled(bool(command.currentData()));buttons.addWidget(save_button);layout.addLayout(buttons)
    command.currentIndexChanged.connect(lambda:save_button.setEnabled(bool(command.currentData()) and not learning))
    device.currentIndexChanged.connect(clear_device)
    timer=QTimer(dialog);timer.setInterval(50);timer.timeout.connect(tick);timer.start();tick()
    dialog.exec();timer.stop()

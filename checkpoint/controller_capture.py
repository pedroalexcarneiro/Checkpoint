"""Atalho de captura para botões digitais expostos pelo XInput."""
import sys
from PySide6.QtCore import QObject,QTimer,Qt


BUTTONS={0x0001:'↑',0x0002:'↓',0x0004:'←',0x0008:'→',0x0010:'Menu',0x0020:'Visão',
         0x0040:'LS',0x0080:'RS',0x0100:'LB',0x0200:'RB',0x1000:'A',0x2000:'B',
         0x4000:'X',0x8000:'Y'}
SUPPORTED=sum(BUTTONS)
PREFERENCE='capture.xinput'


def button_names(mask):
    return ' + '.join(name for bit,name in BUTTONS.items() if mask&bit)


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

    def update(self,state,mask):
        if state is None:self.armed=False;return False
        if not state&mask:self.armed=True;return False
        if self.armed and state&mask==mask:
            self.armed=False
            return state==mask
        return False


class ControllerCapture(QObject):
    def __init__(self,window,backend=None):
        super().__init__(window)
        self.window=window;self.backend=backend;self.edge=ButtonEdge()
        if self.backend is None:
            try:self.backend=XInput()
            except OSError:pass
        self.timer=QTimer(self);self.timer.setInterval(50);self.timer.timeout.connect(self.poll)
        self.load()

    def load(self):
        value=self.window.library.setting(PREFERENCE,{})
        slot=value.get('slot') if isinstance(value,dict) else None
        mask=value.get('buttons') if isinstance(value,dict) else None
        self.slot=slot if type(slot) is int and 0<=slot<4 else None
        self.mask=mask if type(mask) is int and 0<mask<=SUPPORTED and not mask&~SUPPORTED else 0
        self.edge=ButtonEdge()
        self.timer.stop()
        if self.backend and self.slot is not None and self.mask:self.timer.start()

    def poll(self):
        state=self.backend.buttons(self.slot)
        if self.edge.update(state,self.mask) and self.window.launcher.active:self.window.capture_game_window()

    def configure(self):
        self.timer.stop()
        try:configure_controller(self)
        finally:self.load()


def configure_controller(controller):
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
    dialog.setWindowTitle('Captura pelo controle');dialog.resize(520,354)
    layout=QVBoxLayout(dialog)
    dialog_heading(layout,'Captura pelo controle',name='memories')
    inputs=QGridLayout();inputs.setHorizontalSpacing(16);inputs.setVerticalSpacing(0)
    inputs.setRowMinimumHeight(1,12);inputs.setColumnStretch(1,1);layout.addLayout(inputs)
    device=CaptureSelector();device.setObjectName('captureControllerDevice');device.setAccessibleName('Dispositivo XInput')
    for index in range(4):device.addItem(f'Controle {index+1}',index)
    device.setCurrentIndex(controller.slot if controller.slot is not None else 0)
    inputs.addWidget(text('Dispositivo XInput'),0,0);inputs.addWidget(device,0,1)
    command=CaptureSelector();command.setObjectName('captureControllerCommand');command.setAccessibleName('Comando')
    command.addItem('Selecionar botão ou combinação',0)
    for bit,label in BUTTONS.items():command.addItem(label,bit)
    def select_command(mask):
        index=command.findData(mask)
        if index<0:
            command.addItem(button_names(mask),mask)
            index=command.count()-1
        command.setCurrentIndex(index)
    select_command(controller.mask)
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
        command.setEnabled(True);command.setCurrentIndex(0)
        save_button.setEnabled(False)

    def tick():
        nonlocal neutral,peak,learning
        slots=[controller.backend.buttons(index) for index in range(4)]
        for index,buttons in enumerate(slots):
            label=f'Controle {index+1}'+(' · desconectado' if buttons is None else '')
            if device.itemText(index)!=label:device.setItemText(index,label)
        pressed=slots[device.currentData()]
        learn_button.setEnabled(pressed is not None)
        if pressed is None:
            state.setText('Conecte um controle reconhecido como XInput pelo Windows.')
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
        if not mask:return
        controller.window.library.set_setting(PREFERENCE,{'slot':device.currentData(),'buttons':mask})
        dialog.accept()

    def disable():
        controller.window.library.set_setting(PREFERENCE,{})
        dialog.accept()

    learn_button=action('Gravar comando',learn);layout.addWidget(learn_button,0,Qt.AlignLeft)
    layout.addStretch()
    buttons=QHBoxLayout();buttons.addWidget(action('Desativar',disable));buttons.addStretch()
    buttons.addWidget(action('Cancelar',dialog.reject))
    save_button=action('Salvar',save,True);save_button.setEnabled(bool(command.currentData()));buttons.addWidget(save_button);layout.addLayout(buttons)
    command.currentIndexChanged.connect(lambda:save_button.setEnabled(bool(command.currentData()) and not learning))
    device.currentIndexChanged.connect(clear_device)
    timer=QTimer(dialog);timer.setInterval(50);timer.timeout.connect(tick);timer.start();tick()
    dialog.exec();timer.stop()

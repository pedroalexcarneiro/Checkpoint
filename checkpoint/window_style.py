"""Cor nativa da barra de título Windows, preservando os controles do sistema."""
import sys


def titlebar_theme(window,dark):
    if sys.platform!='win32':return False
    try:
        import ctypes
        value=ctypes.c_int(bool(dark))
        function=ctypes.windll.dwmapi.DwmSetWindowAttribute
        function.argtypes=[ctypes.c_void_p,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint]
        for attribute in (20,19):
            if function(int(window.winId()),attribute,ctypes.byref(value),ctypes.sizeof(value))==0:return True
    except (OSError,AttributeError):pass
    return False


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QHBoxLayout,QLabel,QPushButton

class DialogTitleBar(QWidget):
    """Uma única barra de título e fechamento, com arraste do diálogo."""
    def __init__(self,dialog):
        super().__init__(dialog);self.dialog=dialog;self.drag_offset=None;self.setObjectName('dialogTitleBar')
        row=QHBoxLayout(self);row.setContentsMargins(0,0,0,0)
        label=QLabel(dialog.add_title);label.setObjectName('pageTitle');label.setAttribute(Qt.WA_TransparentForMouseEvents);row.addWidget(label,1)
        from .design_system import colors
        from .ui_components import nav_icon
        close=QPushButton();close.setIcon(nav_icon('close',colors()['text'],18));close.setObjectName('quiet');close.setFixedSize(30,30);close.setAccessibleName('Fechar');close.clicked.connect(dialog.reject);row.addWidget(close)
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            handle=self.dialog.windowHandle()
            if handle and handle.startSystemMove():event.accept();return
            self.drag_offset=event.globalPosition().toPoint()-self.dialog.pos();event.accept()
        else:super().mousePressEvent(event)
    def mouseMoveEvent(self,event):
        if self.drag_offset is not None and event.buttons() & Qt.LeftButton:
            self.dialog.move(event.globalPosition().toPoint()-self.drag_offset);event.accept()
        else:super().mouseMoveEvent(event)
    def mouseReleaseEvent(self,event):self.drag_offset=None;super().mouseReleaseEvent(event)

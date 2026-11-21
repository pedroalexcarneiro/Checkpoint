"""Controles integrados, sem marca duplicada, usando ações normais da janela."""
from PySide6.QtCore import Qt,QEvent,QRectF
from PySide6.QtGui import QPainter,QColor,QPen
from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout
from .design_system import colors


def border_hit(x,y,width,height,grip):
    left=x<grip;right=x>=width-grip;top=y<grip;bottom=y>=height-grip
    if top and left:return 13
    if top and right:return 14
    if bottom and left:return 16
    if bottom and right:return 17
    if left:return 10
    if right:return 11
    if top:return 12
    if bottom:return 15
    return None


class WindowButton(QPushButton):
    def __init__(self,kind,callback,parent):
        super().__init__(parent);self.kind=kind;self.restored=False;self.clicked.connect(callback)
        self.setFixedSize(42,32);self.setFocusPolicy(Qt.StrongFocus);self.setObjectName('window'+kind.title())
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors();hover=self.underMouse() or self.hasFocus()
        if hover:p.fillRect(self.rect(),QColor('#c42b1c' if self.kind=='close' else c['selected']))
        p.setPen(QPen(QColor('#ffffff' if hover and self.kind=='close' else c['text']),1.3));x=self.width()/2;y=self.height()/2
        if self.kind=='minimize':p.drawLine(round(x-5),round(y+3),round(x+5),round(y+3))
        elif self.kind=='close':
            p.drawLine(round(x-5),round(y-5),round(x+5),round(y+5));p.drawLine(round(x+5),round(y-5),round(x-5),round(y+5))
        else:
            p.setBrush(Qt.NoBrush)
            if self.restored:p.drawRect(QRectF(x-3,y-6,9,8))
            p.setBrush(QColor(c['selected'] if hover else c['background']));p.drawRect(QRectF(x-5,y-4,9,8))
        p.end()
    def enterEvent(self,event):super().enterEvent(event);self.update()
    def leaveEvent(self,event):super().leaveEvent(event);self.update()


class WindowControls(QWidget):
    def __init__(self,window):
        super().__init__(window);self.host=window;self.drag=None;self.setObjectName('windowControls');self.setFixedHeight(32)
        row=QHBoxLayout(self);row.setContentsMargins(0,0,0,0);row.setSpacing(0);row.addStretch()
        self.minimize=WindowButton('minimize',self.minimize_window,self)
        self.maximize=WindowButton('maximize',self.toggle_maximized,self)
        self.close_button=WindowButton('close',lambda:window.close(),self)
        self.minimize.setAccessibleName('Minimizar');self.minimize.setToolTip('Minimizar');self.close_button.setAccessibleName('Fechar');self.close_button.setToolTip('Fechar')
        for control in (self.minimize,self.maximize,self.close_button):row.addWidget(control)
        self.sync_state();window.installEventFilter(self)
    def minimize_window(self):
        frame=getattr(self.host,'integrated_frame',None)
        if frame and frame.api is not None and frame.applied and not frame.failed:
            frame.api.minimize(int(self.host.winId()))
        else:
            self.host.showMinimized()
    def sync_state(self):
        value=self.host.isMaximized();self.maximize.restored=value
        name='Restaurar' if value else 'Maximizar';self.maximize.setAccessibleName(name);self.maximize.setToolTip(name);self.maximize.update()
    def toggle_maximized(self):
        if self.host.isMaximized():self.host.showNormal()
        else:self.host.showMaximized()
        self.sync_state()
    def eventFilter(self,watched,event):
        if event.type() in (QEvent.WindowStateChange,QEvent.PaletteChange):self.sync_state();self.update()
        return super().eventFilter(watched,event)
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            handle=self.host.windowHandle()
            if handle and handle.startSystemMove():event.accept();return
            self.drag=event.globalPosition().toPoint()-self.host.pos();event.accept()
        else:super().mousePressEvent(event)
    def mouseMoveEvent(self,event):
        if self.drag is not None and event.buttons()&Qt.LeftButton:self.host.move(event.globalPosition().toPoint()-self.drag);event.accept()
        else:super().mouseMoveEvent(event)
    def mouseReleaseEvent(self,event):self.drag=None;super().mouseReleaseEvent(event)
    def mouseDoubleClickEvent(self,event):
        if event.button()==Qt.LeftButton:self.toggle_maximized();event.accept()
        else:super().mouseDoubleClickEvent(event)

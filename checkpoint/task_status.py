from .locale import count_text
from .icons import lucide_icon
"""Indicador compacto; nenhuma barra expansível na janela principal."""
from PySide6.QtCore import QEvent,QEasingCurve,Qt,QTimer,QRectF,QVariantAnimation
from PySide6.QtGui import QPainter,QPen,QColor
from PySide6.QtWidgets import QFrame,QStatusBar,QStyle,QStyleOption,QStylePainter,QWidget,QHBoxLayout,QLabel,QToolButton


class OperationStatusBar(QStatusBar):
    def paintEvent(self,event):
        painter=QStylePainter(self)
        option=QStyleOption()
        option.initFrom(self)
        painter.drawPrimitive(QStyle.PE_PanelStatusBar,option)
        painter.end()


class StatusToast(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.setObjectName('statusToast')
        self.setProperty('component','card')
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.label=QLabel()
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        row=QHBoxLayout(self)
        row.setContentsMargins(16,12,16,12)
        row.addWidget(self.label)
        self.progress=0.0
        self.animation=QVariantAnimation(self)
        self.animation.valueChanged.connect(self.reposition)
        self.animation.finished.connect(self.finish)
        parent.installEventFilter(self)
        self.hide()

    def set_message(self,message):
        if not message and self.isHidden():
            return
        if message:
            self.label.setText(message)
            self.setAccessibleName(message)
            self.setFixedWidth(max(200,min(360,self.label.fontMetrics().horizontalAdvance(message)+36)))
            self.adjustSize()
            self.reposition(self.progress)
            self.show()
            self.raise_()
        self.animation.stop()
        self.animation.setDuration(240 if message else 200)
        self.animation.setEasingCurve(QEasingCurve.OutCubic if message else QEasingCurve.InCubic)
        self.animation.setStartValue(self.progress)
        self.animation.setEndValue(1.0 if message else 0.0)
        self.animation.start()

    def reposition(self,progress):
        self.progress=progress
        x=round((self.width()+18)*progress-self.width())
        self.move(x,self.parentWidget().height()-self.height()-18)

    def finish(self):
        if self.progress==0:
            self.hide()

    def eventFilter(self,watched,event):
        if watched is self.parentWidget() and event.type()==QEvent.Resize:
            self.reposition(self.progress)
        return super().eventFilter(watched,event)


class BusyIndicator(QWidget):
    def __init__(self,theme,parent=None):
        super().__init__(parent);self.theme=theme;self.angle=0;self.setFixedSize(16,16)
        self.timer=QTimer(self);self.timer.setInterval(50);self.timer.timeout.connect(self.tick)
    def tick(self):self.angle=(self.angle+24)%360;self.update()
    def showEvent(self,event):super().showEvent(event);self.timer.start()
    def hideEvent(self,event):self.timer.stop();super().hideEvent(event)
    def paintEvent(self,event):
        from .ui_components import nav_icon
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);p.translate(8,8);p.rotate(self.angle);p.drawPixmap(-8,-8,nav_icon('busy',self.theme.colors['accent'],16).pixmap(16,16));p.end()


class TaskStatus(QWidget):
    def __init__(self,theme,stop,parent=None):
        super().__init__(parent);self.setObjectName('taskStatus');self.setFixedHeight(28);self.setMaximumWidth(380)
        row=QHBoxLayout(self);row.setContentsMargins(8,0,4,0);row.setSpacing(8)
        self.spinner=BusyIndicator(theme);row.addWidget(self.spinner)
        self.message=QLabel();self.message.setObjectName('caption');self.message.setMinimumWidth(0);row.addWidget(self.message)
        self.stop=QToolButton();self.stop.setIcon(lucide_icon('close',theme.colors['text'],16));self.stop.setFixedSize(24,24);self.stop.setToolTip('Parar consultas pendentes após o jogo atual');self.stop.setAccessibleName('Parar consultas pendentes');self.stop.clicked.connect(stop);row.addWidget(self.stop)
        self.hide()
    def set_count(self,count):
        self.message.setText('Imagens em segundo plano' if count==1 else 'Imagens em segundo plano · '+count_text(count,'jogo'))
        self.setVisible(count>0)

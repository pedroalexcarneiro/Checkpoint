"""Indicador compacto; nenhuma barra expansível na janela principal."""
from PySide6.QtCore import Qt,QTimer,QRectF
from PySide6.QtGui import QPainter,QPen,QColor
from PySide6.QtWidgets import QWidget,QHBoxLayout,QLabel,QToolButton


class BusyIndicator(QWidget):
    def __init__(self,theme,parent=None):
        super().__init__(parent);self.theme=theme;self.angle=0;self.setFixedSize(16,16)
        self.timer=QTimer(self);self.timer.setInterval(50);self.timer.timeout.connect(self.tick)
    def tick(self):self.angle=(self.angle+24)%360;self.update()
    def showEvent(self,event):super().showEvent(event);self.timer.start()
    def hideEvent(self,event):self.timer.stop();super().hideEvent(event)
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);p.setPen(QPen(QColor(self.theme.colors['accent']),2,Qt.SolidLine,Qt.RoundCap));p.drawArc(QRectF(2,2,12,12),self.angle*16,250*16);p.end()


class TaskStatus(QWidget):
    def __init__(self,theme,stop,parent=None):
        super().__init__(parent);self.setObjectName('taskStatus');self.setFixedHeight(28);self.setMaximumWidth(380)
        row=QHBoxLayout(self);row.setContentsMargins(8,0,4,0);row.setSpacing(8)
        self.spinner=BusyIndicator(theme);row.addWidget(self.spinner)
        self.message=QLabel();self.message.setObjectName('caption');self.message.setMinimumWidth(0);row.addWidget(self.message)
        self.stop=QToolButton();self.stop.setText('×');self.stop.setFixedSize(24,24);self.stop.setToolTip('Parar consultas pendentes após o jogo atual');self.stop.setAccessibleName('Parar consultas pendentes');self.stop.clicked.connect(stop);row.addWidget(self.stop)
        self.hide()
    def set_count(self,count):
        self.message.setText('Buscando ficha e imagens' if count==1 else f'Buscando ficha e imagens · {count} jogos')
        self.setVisible(count>0)

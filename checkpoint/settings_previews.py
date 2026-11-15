"""Prévias funcionais de aparência, usando as paletas reais do aplicativo."""
from PySide6.QtCore import Qt,QRectF
from PySide6.QtGui import QPainter,QColor,QPen
from PySide6.QtWidgets import QWidget,QApplication,QSizePolicy
from .design_system import ThemeSwatch,colors


class ThemePreview(ThemeSwatch):
    def __init__(self,theme,callback):
        super().__init__(theme,callback);self.setObjectName('themePreview')
        self.setMinimumSize(0,112);self.setMaximumSize(16777215,112);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=self.theme.colors
        chosen=QApplication.instance().property('checkpointTheme')==self.theme.key
        bounds=QRectF(self.rect().adjusted(2,2,-2,-2))
        p.setPen(QPen(QColor(colors()['accent'] if chosen else colors()['border']),2 if chosen else 1));p.setBrush(QColor(c['surface']));p.drawRoundedRect(bounds,9,9)
        p.setPen(Qt.NoPen);p.setBrush(QColor(c['elevated']));p.drawRoundedRect(QRectF(12,12,60,self.height()-24),5,5)
        for row in range(4):
            p.setBrush(QColor(c['accent'] if row==1 else c['muted']));p.drawRoundedRect(QRectF(20,22+row*16,42,6),2,2)
        p.setBrush(QColor(c['panel']));p.drawRoundedRect(QRectF(84,14,max(1,self.width()-98),30),4,4)
        width=max(1,(self.width()-110)/3)
        for column in range(3):
            x=84+column*(width+6);p.setBrush(QColor(c['elevated']));p.drawRoundedRect(QRectF(x,54,width,40),4,4)
            p.setBrush(QColor(c['accent']));p.drawRect(QRectF(x,91,width,3))
        p.end()


class CoverSizePreview(QWidget):
    def __init__(self,percent):
        super().__init__();self.percent=percent;self.setObjectName('coverSizePreview');self.setFixedSize(260,150)
        self.setAccessibleName('Prévia do tamanho das capas')
    def set_percent(self,value):self.percent=value;self.update()
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors()
        for index,height in enumerate((68,98,126)):
            height=round(height*(.85+self.percent/100*.15));width=round(height*2/3);x=15+index*80;y=140-height
            p.setBrush(QColor(c['panel']));p.setPen(QPen(QColor(c['accent'] if index==1 else c['border']),1));p.drawRoundedRect(QRectF(x,y,width,height),5,5)
            p.setPen(QColor(c['accent'] if index==1 else c['muted']));p.drawText(QRectF(x,y,width,height),Qt.AlignCenter,'Capa')
        p.end()

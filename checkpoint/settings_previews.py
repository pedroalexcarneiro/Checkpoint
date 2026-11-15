"""Prévias funcionais de aparência, usando as paletas reais do aplicativo."""
from PySide6.QtCore import Qt,QRectF
from PySide6.QtGui import QPainter,QColor,QPen
from PySide6.QtWidgets import QWidget,QApplication,QSizePolicy,QAbstractButton
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


class CoverChoice(QAbstractButton):
    def __init__(self,value,index,owner):
        super().__init__(owner);self.value=value;self.index=index;self.owner=owner
        self.setObjectName('coverChoice');self.setCheckable(True);self.setFocusPolicy(Qt.StrongFocus)
        self.setAccessibleName(str(value)+'%');self.setToolTip(str(value)+'%');self.setMinimumWidth(44)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed);self.setFixedHeight(228)
    def artwork_rect(self):
        height=min(176,max(24,(self.width()-16)*1.5))*(self.value/150)
        width=height*2/3
        return QRectF((self.width()-width)/2,188-height,width,height)
    def paintEvent(self,event):
        from .theme import get_theme
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors();green=get_theme('green').colors['accent']
        p.setBrush(QColor(c['panel']));p.setPen(QPen(QColor(green if self.isChecked() else c['border']),2 if self.isChecked() else 1))
        p.drawRoundedRect(self.artwork_rect(),6,6)
        p.setPen(QColor(green if self.isChecked() else c['text']));p.drawText(QRectF(0,198,self.width(),24),Qt.AlignCenter,str(self.value)+'%')
        if self.hasFocus():
            p.setBrush(Qt.NoBrush);p.setPen(QPen(QColor(c['text']),1,Qt.DashLine));p.drawRoundedRect(QRectF(self.rect().adjusted(3,3,-3,-3)),6,6)
        p.end()
    def keyPressEvent(self,event):
        if event.key() in (Qt.Key_Left,Qt.Key_Right,Qt.Key_Up,Qt.Key_Down):
            offset=-1 if event.key() in (Qt.Key_Left,Qt.Key_Up) else 1
            target=self.owner.buttons[(self.index+offset)%5];target.setFocus();target.click();event.accept();return
        if event.key() in (Qt.Key_Return,Qt.Key_Enter):self.click();event.accept();return
        super().keyPressEvent(event)


class CoverSizeChoices(QWidget):
    def __init__(self,percent,callback):
        from PySide6.QtWidgets import QHBoxLayout,QButtonGroup
        from .card_layout import COVER_CHOICES,nearest_cover_choice
        super().__init__();self.setObjectName('coverSizePreview');self.setAccessibleName('Tamanho das capas')
        row=QHBoxLayout(self);row.setContentsMargins(0,0,0,0);row.setSpacing(8)
        self.group=QButtonGroup(self);self.group.setExclusive(True);self.buttons=[]
        self.percent=nearest_cover_choice(percent)
        for index,value in enumerate(COVER_CHOICES):
            button=CoverChoice(value,index,self);self.buttons.append(button);self.group.addButton(button,value);row.addWidget(button,1)
            button.setChecked(value==self.percent)
        self.group.idClicked.connect(self.choose);self.callback=callback
    def choose(self,value):
        self.percent=value;self.group.button(value).setChecked(True);self.callback(value)
    def active_index(self):
        from .card_layout import COVER_CHOICES
        return COVER_CHOICES.index(self.percent)
    def cover_rects(self):
        from PySide6.QtCore import QPointF
        return [b.artwork_rect().translated(QPointF(b.pos())) for b in self.buttons]

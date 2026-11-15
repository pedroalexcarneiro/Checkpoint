"""Estado do jogo como controle único, com ponto, rótulo e menu nativo."""
from PySide6.QtCore import Qt,QRectF,QSize
from PySide6.QtGui import QPainter,QColor,QPen,QFont
from PySide6.QtWidgets import QComboBox,QLabel,QSizePolicy
from .design_system import colors
from .icons import lucide_icon


class StatusControl(QComboBox):
    def __init__(self,parent=None):
        super().__init__(parent);self.setObjectName('gameStatus');self.setAccessibleName('Status do jogo')
        self.setFixedHeight(40);self.setMinimumWidth(176);self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setStyleSheet('QComboBox#gameStatus { padding: 0px 34px 0px 40px; font-weight: 600; }')
        self.dot=QLabel('●',self);self.dot.setObjectName('gameStatusDot');self.dot.setFixedSize(12,18)
        self.dot.setAlignment(Qt.AlignCenter);self.dot.setAttribute(Qt.WA_TransparentForMouseEvents)
        self._dot_color=None

    def sizeHint(self):
        width=max((self.fontMetrics().horizontalAdvance(self.itemText(i)) for i in range(self.count())),default=0)
        return QSize(max(176,width+76),40)

    def resizeEvent(self,event):
        self.dot.move(16,(self.height()-self.dot.height())//2)
        super().resizeEvent(event)

    def paintEvent(self,event):
        c=colors()
        if self._dot_color!=c['accent']:
            self._dot_color=c['accent'];self.dot.setStyleSheet('color: '+c['accent']+'; font-size: 12px; background: transparent; border: none;')
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        p.setBrush(QColor(c['selected']));p.setPen(QPen(QColor(c['accent']),2 if self.hasFocus() else 1))
        p.drawRoundedRect(QRectF(self.rect()).adjusted(.5,.5,-.5,-.5),8,8)
        font=QFont(self.font());font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor(c['accent']))
        p.drawText(QRectF(40,0,max(0,self.width()-76),self.height()),Qt.AlignLeft|Qt.AlignVCenter,self.currentText())
        p.drawPixmap(self.width()-31,(self.height()-18)//2,lucide_icon('chevron',c['accent'],18).pixmap(18,18));p.end()

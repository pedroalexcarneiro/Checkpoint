from PySide6.QtCore import Qt, QSize, QRectF, QPointF
from PySide6.QtGui import QPixmap, QPainter, QColor, QLinearGradient, QFont, QIcon, QPen, QPolygonF, QRegion, QPainterPath
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QTabWidget, QSizePolicy


def text(value, kind=None):
    label = QLabel(str(value)); label.setWordWrap(True); label.setTextFormat(Qt.PlainText)
    if kind: label.setObjectName(kind)
    return label


def action(title, callback, primary=False):
    button = QPushButton(title); button.clicked.connect(callback)
    if primary: button.setObjectName('primary')
    return button


def card():
    frame = QFrame(); frame.setObjectName('panel')
    layout = QVBoxLayout(frame); layout.setContentsMargins(20, 18, 20, 18); layout.setSpacing(12)
    return frame, layout


def nav_icon(name, color):
    pixmap = QPixmap(24, 24); pixmap.fill(Qt.transparent)
    p = QPainter(pixmap); p.setRenderHint(QPainter.Antialiasing)
    p.setPen(QPen(QColor(color), 1.7, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
    if name == 'home':
        p.drawPolyline(QPolygonF([QPointF(x,y) for x,y in ((3,11),(12,3),(21,11))]))
        p.drawRoundedRect(QRectF(6,10,12,11),2,2)
    elif name == 'library':
        for x in (4,13):
            for y in (4,13): p.drawRoundedRect(QRectF(x,y,7,7),1.2,1.2)
    elif name == 'stats':
        for x,y in ((5,13),(11,7),(17,3)):p.drawRoundedRect(QRectF(x,y,3,19-y),1,1)
    elif name == 'memories':
        p.drawRoundedRect(QRectF(3,4,18,16),2,2); p.drawLine(5,17,10,11);p.drawLine(10,11,14,15);p.drawLine(14,15,18,10)
    elif name == 'settings':
        import math
        points=[]
        for i in range(48):
            radius=10 if i%8 in (0,1,6,7) else 8
            angle=i*math.pi/24
            points.append(QPointF(12+radius*math.cos(angle),12+radius*math.sin(angle)))
        p.drawPolygon(QPolygonF(points));p.drawEllipse(QRectF(8.5,8.5,7,7))
    elif name == 'wish':
        path=QPainterPath(QPointF(12,21));path.cubicTo(8,17,2,13,2,8);path.cubicTo(2,2,9,1,12,6);path.cubicTo(15,1,22,2,22,8);path.cubicTo(22,13,16,17,12,21);p.drawPath(path)
    p.end();return QIcon(pixmap)


class Hero(QWidget):
    def __init__(self, game, theme, parent=None):
        super().__init__(parent); self.game = game; self.theme = theme
        self.banner = QPixmap(game.get('banner') or '')
        self.logo = QPixmap(game.get('logo') or '')
        if not self.logo.isNull() and self.logo.hasAlphaChannel():
            bounds=QRegion(self.logo.mask()).boundingRect()
            if not bounds.isEmpty():self.logo=self.logo.copy(bounds)
        self.setObjectName('gameHero');self._hero_height=0
        self.content = QVBoxLayout(self);self.content.setContentsMargins(30,26,30,24)
        self.content.addStretch()

    def set_theme(self, theme):self.theme = theme;self.update()

    def resizeEvent(self,event):
        super().resizeEvent(event)
        ratio=self.banner.width()/self.banner.height() if not self.banner.isNull() else 4.5
        height=max(1,round(event.size().width()/ratio)) if not self.banner.isNull() else 220
        if height!=self._hero_height:self._hero_height=height;self.setFixedHeight(height)

    def paintEvent(self, event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        rect=self.rect();clip=QPainterPath();clip.addRoundedRect(QRectF(rect),10,10);p.setClipPath(clip)
        p.fillRect(rect,QColor('#15191e'))
        if not self.banner.isNull():
            p.drawPixmap(rect,self.banner)  # O quadro acompanha a proporção original.
        shade=QLinearGradient(0,0,self.width()*.7,0)
        shade.setColorAt(0,QColor(9,12,17,210));shade.setColorAt(.65,QColor(9,12,17,65));shade.setColorAt(1,QColor(9,12,17,0));p.fillRect(rect,shade)
        if not self.logo.isNull():
            logo=self.logo.scaled(min(290,self.width()-56),max(30,min(95,self.height()//3)),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(28,28,logo)
        else:
            p.setPen(QColor('#ffffff'));font=QFont('Segoe UI');font.setPixelSize(30);font.setWeight(QFont.Bold);p.setFont(font)
            p.drawText(QRectF(28,26,min(self.width()-56,560),100),Qt.TextWordWrap,self.game['title'])
        if self.height()>240:
            font=QFont('Segoe UI');font.setPixelSize(14);p.setFont(font);p.setPen(QColor('#d1d5db'))
            p.drawText(QRectF(28,140,min(420,self.width()-56),30),Qt.AlignVCenter,' · '.join(value for value in (self.game.get('platform'),self.game.get('status')) if value))
        p.end()


class GameTile(QPushButton):
    """Mesmo desenho e posições em todos os DPI; sem layout dentro do botão."""
    def __init__(self, game, callback, width=148, parent=None):
        super().__init__(parent);self.setObjectName('gameTile');self.setFixedWidth(width)
        self.game=game;self.callback=callback;self.game_id=game['id'];self.pixmap=QPixmap(game.get('cover') or '')
        self.art_height=round(width*1.5);self.setFixedHeight(self.art_height+58)
        self.setAccessibleName(game['title']);self.setAccessibleDescription(game.get('status') or '');self.setToolTip(game['title'])
        self.clicked.connect(self.open_game)

    def paintEvent(self,event):
        from .theme import get_theme
        from PySide6.QtWidgets import QApplication
        colors=get_theme(QApplication.instance().property('checkpointTheme')).colors
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        art=QRectF(0,0,self.width(),self.art_height)
        if not self.pixmap.isNull():
            pix=self.pixmap.scaled(art.size().toSize(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.save();clip=QPainterPath();clip.addRoundedRect(QRectF((self.width()-pix.width())//2,self.art_height-pix.height(),pix.width(),pix.height()),7,7);p.setClipPath(clip)
            p.drawPixmap((self.width()-pix.width())//2,self.art_height-pix.height(),pix)
            p.restore()
        else:
            p.fillRect(art,QColor(colors['panel']));p.setPen(QColor(colors['muted']));font=QFont('Segoe UI');font.setPixelSize(24);p.setFont(font);p.drawText(art,Qt.AlignCenter,self.game['title'][:2].upper())
        font=QFont('Segoe UI');font.setPixelSize(14);font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor(colors['text']))
        p.drawText(QRectF(0,self.art_height+10,self.width(),20),Qt.AlignVCenter,p.fontMetrics().elidedText(self.game['title'],Qt.ElideRight,self.width()))
        font.setPixelSize(12);font.setWeight(QFont.Normal);p.setFont(font);p.setPen(QColor(colors['muted']))
        p.drawText(QRectF(0,self.art_height+33,self.width(),18),Qt.AlignVCenter,self.game.get('status') or '')
        if self.hasFocus():p.setPen(QPen(QColor(colors['accent']),1));p.setBrush(Qt.NoBrush);p.drawRoundedRect(self.rect().adjusted(1,1,-1,-1),7,7)
        p.end()

    def open_game(self):self.callback(self.game_id)


class CurrentPageTabs(QTabWidget):
    """Uma aba longa não estica as outras páginas da ficha."""
    def __init__(self,parent=None):
        super().__init__(parent);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.currentChanged.connect(self.page_changed)

    def sizeHint(self):
        page=self.currentWidget()
        if page is None:return super().sizeHint()
        return QSize(page.sizeHint().width(),page.sizeHint().height()+self.tabBar().sizeHint().height()+8)

    def minimumSizeHint(self):return QSize(0,self.sizeHint().height())

    def page_changed(self,index):self.updateGeometry()


def service_icon(provider):
    pixmap=QPixmap(48,48);pixmap.fill(Qt.transparent)
    p=QPainter(pixmap);p.setRenderHint(QPainter.Antialiasing);p.setPen(Qt.NoPen)
    backgrounds={'Steam':'#152b49','Google Drive':'#202933','SteamGridDB':'#204659','RAWG':'#191b20'}
    p.setBrush(QColor(backgrounds.get(provider,'#25323c')));p.drawRoundedRect(QRectF(0,0,48,48),10,10)
    if provider=='Steam':
        p.setPen(QPen(QColor('#ffffff'),3,Qt.SolidLine,Qt.RoundCap));p.drawLine(15,32,31,17)
        p.drawEllipse(QRectF(24,9,14,14));p.drawEllipse(QRectF(8,26,12,12));p.drawLine(4,26,12,31)
    elif provider=='Google Drive':
        for color,points in [('#34a853',[(21,8),(28,8),(15,31),(8,31)]),('#fbbc04',[(28,8),(40,31),(32,31),(21,12)]),('#4285f4',[(8,31),(15,24),(36,24),(40,31),(36,38),(12,38)])]:
            p.setBrush(QColor(color));p.drawPolygon(QPolygonF([QPointF(x,y) for x,y in points]))
    else:
        p.setPen(QColor('#ffffff'));font=QFont('Segoe UI');font.setPixelSize(16 if provider=='SteamGridDB' else 20);font.setWeight(QFont.Bold);p.setFont(font)
        p.drawText(QRectF(0,0,48,48),Qt.AlignCenter,'SG' if provider=='SteamGridDB' else 'R')
    p.end();return pixmap

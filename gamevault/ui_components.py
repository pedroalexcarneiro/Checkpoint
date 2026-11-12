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
        p.drawEllipse(QRectF(4,4,16,16));p.drawEllipse(QRectF(9,9,6,6))
        for x,y,a,b in ((12,1,12,4),(12,20,12,23),(1,12,4,12),(20,12,23,12)):p.drawLine(x,y,a,b)
    else:
        p.drawRoundedRect(QRectF(6,3,12,18),2,2);p.drawLine(9,9,15,9);p.drawLine(9,13,15,13)
    p.end();return QIcon(pixmap)


class Hero(QWidget):
    def __init__(self, game, theme, parent=None):
        super().__init__(parent); self.game = game; self.theme = theme
        self.banner = QPixmap(game.get('banner') or '')
        self.logo = QPixmap(game.get('logo') or '')
        if not self.logo.isNull() and self.logo.hasAlphaChannel():
            bounds=QRegion(self.logo.mask()).boundingRect()
            if not bounds.isEmpty():self.logo=self.logo.copy(bounds)
        self.setObjectName('gameHero');self.setMinimumHeight(250);self.setMaximumHeight(370);self._hero_height=0
        self.content = QVBoxLayout(self);self.content.setContentsMargins(30,26,30,24)
        self.content.addStretch()

    def set_theme(self, theme):self.theme = theme;self.update()

    def resizeEvent(self,event):
        super().resizeEvent(event)
        ratio=self.banner.width()/self.banner.height() if not self.banner.isNull() else 3.5
        height=max(250,min(370,round(event.size().width()/max(2.8,ratio))))
        if height!=self._hero_height:self._hero_height=height;self.setFixedHeight(height)

    def paintEvent(self, event):
        p = QPainter(self); p.setRenderHint(QPainter.Antialiasing)
        rect = self.rect();clip=QPainterPath();clip.addRoundedRect(QRectF(rect),14,14);p.setClipPath(clip)
        p.fillRect(rect,QColor('#15191e'))
        if not self.banner.isNull():
            background=self.banner.scaled(48,24,Qt.IgnoreAspectRatio,Qt.SmoothTransformation).scaled(self.size(),Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
            p.drawPixmap((self.width()-background.width())//2,(self.height()-background.height())//2,background)
            foreground=self.banner.scaled(self.size()-QSize(24,24),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap((self.width()-foreground.width())//2,(self.height()-foreground.height())//2,foreground)
        shade=QLinearGradient(0,0,self.width(),0)
        shade.setColorAt(0,QColor(9,12,17,230));shade.setColorAt(.52,QColor(9,12,17,90));shade.setColorAt(1,QColor(9,12,17,15))
        p.fillRect(rect,shade)
        if not self.logo.isNull():
            logo=self.logo.scaled(min(330,self.width()-60),100,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(30,38,logo)
        else:
            p.setPen(QColor('#ffffff'));font=QFont('Segoe UI',25);font.setWeight(QFont.Bold);p.setFont(font)
            p.drawText(QRectF(30,30,min(self.width()-60,560),105),Qt.TextWordWrap,self.game['title'])
        font=QFont('Segoe UI');font.setPixelSize(14);p.setFont(font);p.setPen(QColor('#d1d5db'))
        p.drawText(QRectF(30,151,min(420,self.width()-60),30),Qt.AlignVCenter,' · '.join(value for value in (self.game.get('platform'),self.game.get('status')) if value))
        p.end()


class GameTile(QPushButton):
    def __init__(self, game, callback, width=148, parent=None):
        super().__init__(parent);self.setObjectName('gameTile');self.setFixedWidth(width)
        self.setAccessibleName(game['title']);self.setToolTip(game['title'])
        layout=QVBoxLayout(self);layout.setContentsMargins(4,4,4,8);layout.setSpacing(7)
        art=QLabel();art.setAlignment(Qt.AlignCenter);art.setFixedSize(width-8,int((width-8)*4/3));art.setObjectName('tileArt');self.setFixedHeight(art.height()+66)
        pix=QPixmap(game.get('cover') or '')
        if not pix.isNull():art.setPixmap(pix.scaled(art.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:art.setText(game['title'][:2].upper())
        layout.addWidget(art)
        title=text(game['title']);title.setMaximumHeight(38);layout.addWidget(title)
        status=text(game.get('status') or game.get('platform') or '', 'muted');layout.addWidget(status)
        for label in (art,title,status):label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.callback=callback;self.game_id=game['id'];self.clicked.connect(self.open_game)

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

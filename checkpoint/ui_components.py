from PySide6.QtCore import Qt, QSize, QRectF, QPointF
from PySide6.QtGui import QPixmap, QPainter, QColor, QLinearGradient, QFont, QIcon, QPen, QPolygonF, QRegion, QPainterPath
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QTabWidget, QSizePolicy


def text(value, kind=None):
    label = QLabel(str(value)); label.setWordWrap(True); label.setTextFormat(Qt.PlainText)
    if kind: label.setObjectName(kind)
    return label


class TwoLineLabel(QLabel):
    """Resumo legível no feed; texto completo permanece na dica e na ficha."""
    def __init__(self,value,parent=None):
        super().__init__(parent);self.full_text=value;self.setObjectName('muted')
        self.setTextFormat(Qt.PlainText);self.setAlignment(Qt.AlignTop);self.setToolTip(value);self.setFixedHeight(36)
    def resizeEvent(self,event):
        super().resizeEvent(event);metrics=self.fontMetrics();words=self.full_text.split();line=''
        while words and metrics.horizontalAdvance((line+' '+words[0]).strip())<=self.width():line=(line+' '+words.pop(0)).strip()
        self.setText(line+('\n'+metrics.elidedText(' '.join(words),Qt.ElideRight,self.width()) if words else ''))


def action(title, callback, primary=False):
    button = QPushButton(title); button.clicked.connect(callback)
    if primary: button.setObjectName('primary')
    return button


def card():
    frame = QFrame(); frame.setObjectName('panel')
    layout = QVBoxLayout(frame); layout.setContentsMargins(18, 16, 18, 16); layout.setSpacing(10)
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
    elif name in ('wish','heart'):
        path=QPainterPath(QPointF(12,21));path.cubicTo(8,17,2,13,2,8);path.cubicTo(2,2,9,1,12,6);path.cubicTo(15,1,22,2,22,8);path.cubicTo(22,13,16,17,12,21);p.drawPath(path)
    elif name=='clock':
        p.drawEllipse(QRectF(3,3,18,18));p.drawLine(12,6,12,12);p.drawLine(12,12,16,14)
    elif name=='user':
        p.drawEllipse(QRectF(8,3,8,8));path=QPainterPath(QPointF(4,21));path.cubicTo(4,10,20,10,20,21);p.drawPath(path)
    elif name=='search':
        p.drawEllipse(QRectF(3,3,13,13));p.drawLine(15,15,21,21)
    elif name=='folder':
        path=QPainterPath(QPointF(3,7));path.lineTo(3,4);path.lineTo(10,4);path.lineTo(12,7);path.lineTo(21,7);path.lineTo(21,20);path.lineTo(3,20);path.closeSubpath();p.drawPath(path)
    elif name=='download':
        p.drawLine(12,3,12,16);p.drawLine(7,11,12,16);p.drawLine(12,16,17,11);p.drawPolyline(QPolygonF([QPointF(4,17),QPointF(4,21),QPointF(20,21),QPointF(20,17)]))
    elif name=='trophy':
        p.drawPolyline(QPolygonF([QPointF(7,3),QPointF(17,3),QPointF(16,12),QPointF(12,16),QPointF(8,12),QPointF(7,3)]));p.drawPolyline(QPolygonF([QPointF(7,5),QPointF(3,5),QPointF(4,11),QPointF(8,12)]));p.drawPolyline(QPolygonF([QPointF(17,5),QPointF(21,5),QPointF(20,11),QPointF(16,12)]));p.drawLine(12,16,12,21);p.drawLine(8,21,16,21)
    elif name=='trash':
        p.drawLine(4,6,20,6);p.drawPolyline(QPolygonF([QPointF(6,6),QPointF(7,21),QPointF(17,21),QPointF(18,6)]));p.drawRoundedRect(QRectF(9,2,6,4),1,1);p.drawLine(10,10,10,17);p.drawLine(14,10,14,17)
    elif name=='play':
        p.drawPolygon(QPolygonF([QPointF(8,4),QPointF(20,12),QPointF(8,20)]))
    elif name=='list':
        for y in (6,12,18):p.drawLine(8,y,21,y);p.drawPoint(3,y)
    elif name=='filter':
        for y,x in ((6,8),(12,16),(18,10)):
            p.drawLine(3,y,21,y);p.drawEllipse(QRectF(x-2,y-2,4,4))
    elif name=='plus':p.drawLine(12,4,12,20);p.drawLine(4,12,20,12)
    else:
        p.drawRoundedRect(QRectF(4,3,16,18),2,2);p.drawLine(8,9,16,9);p.drawLine(8,14,16,14)
    p.end();return QIcon(pixmap)


class Hero(QWidget):
    def __init__(self, game, theme, parent=None):
        super().__init__(parent); self.game = game; self.theme = theme
        self.detail_mode=False
        self.banner = QPixmap(game.get('banner') or '')
        self.logo = QPixmap(game.get('logo') or '')
        if not self.logo.isNull() and self.logo.hasAlphaChannel():
            bounds=QRegion(self.logo.mask()).boundingRect()
            if not bounds.isEmpty():self.logo=self.logo.copy(bounds)
        self.setObjectName('gameHero');self._hero_height=0
        self.content = QVBoxLayout(self);self.content.setContentsMargins(26,12,26,18)
        self.content.addStretch()

    def set_theme(self, theme):self.theme = theme;self.update()

    def resizeEvent(self,event):
        super().resizeEvent(event)
        ratio=self.banner.width()/self.banner.height() if not self.banner.isNull() else 4.5
        height=max(220,min(300,round(event.size().width()/4)))
        if height!=self._hero_height:self._hero_height=height;self.setFixedHeight(height)

    def paintEvent(self, event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        rect=self.rect();clip=QPainterPath();clip.addRoundedRect(QRectF(rect),10,10);p.setClipPath(clip)
        p.fillRect(rect,QColor('#15191e'))
        if not self.banner.isNull():
            pix=self.banner.scaled(rect.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            image_left=rect.right()-pix.width()+1
            p.drawPixmap(image_left,(rect.height()-pix.height())//2,pix)
            if image_left>0:
                edge=QLinearGradient(image_left,0,image_left+100,0)
                edge.setColorAt(0,QColor('#15191e'));edge.setColorAt(1,QColor(21,25,30,0))
                p.fillRect(QRectF(image_left,0,100,self.height()),edge)
        shade=QLinearGradient(0,0,self.width()*.7,0)
        shade.setColorAt(0,QColor(9,12,17,210));shade.setColorAt(.65,QColor(9,12,17,65));shade.setColorAt(1,QColor(9,12,17,0));p.fillRect(rect,shade)
        x=26;top=62 if self.detail_mode else 22
        identity_height=min(100,max(60,self.height()*.34))
        if not self.logo.isNull():
            logo=self.logo.scaled(min(300 if self.detail_mode else 245,self.width()-52),round(identity_height),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(x,top,logo)
        else:
            p.setPen(QColor('#ffffff'));font=QFont('Segoe UI');font.setPixelSize(28);font.setWeight(QFont.DemiBold);p.setFont(font)
            p.drawText(QRectF(x,top,min(self.width()-52,360),identity_height),Qt.AlignLeft|Qt.AlignVCenter|Qt.TextWordWrap,self.game['title'])
        if not self.detail_mode and self.game.get('description'):
            font=QFont('Segoe UI');font.setPixelSize(13);p.setFont(font);p.setPen(QColor('#f0f1f3'))
            width=round(min(340,self.width()*.46));words=self.game['description'].replace('\n',' ').split()
            y=round(top+identity_height+12);available=self.height()-y-64
            for index in range(min(3,max(0,available//17))):
                line=''
                while words and p.fontMetrics().horizontalAdvance((line+' '+words[0]).strip())<=width:line=(line+' '+words.pop(0)).strip()
                if not line:break
                if index==min(3,max(0,available//17))-1 and words:line=p.fontMetrics().elidedText(line+' '+' '.join(words),Qt.ElideRight,width)
                p.drawText(QRectF(x,y+index*17,width,17),Qt.AlignVCenter,line)
        p.end()


class GameTile(QPushButton):
    """Mesmo desenho e posições em todos os DPI; sem layout dentro do botão."""
    def __init__(self, game, callback, width=148, parent=None):
        super().__init__(parent);self.setObjectName('gameTile');self.setFixedWidth(width)
        self.game=game;self.callback=callback;self.game_id=game['id'];self.pixmap=QPixmap(game.get('cover') or '')
        self.set_tile_width(width)
        self.setAccessibleName(game['title']);self.setAccessibleDescription(game.get('status') or '');self.setToolTip(game['title'])
        self.clicked.connect(self.open_game)

    def set_tile_width(self,width):
        self.setFixedWidth(width);self.art_height=round(width*1.5);self.setFixedHeight(self.art_height+48)

    def paintEvent(self,event):
        from .theme import get_theme
        from PySide6.QtWidgets import QApplication
        colors=get_theme(QApplication.instance().property('checkpointTheme')).colors
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        art=QRectF(0,0,self.width(),self.art_height)
        if not self.pixmap.isNull():
            pix=self.pixmap.scaled(art.size().toSize(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.save();clip=QPainterPath();clip.addRoundedRect(QRectF((self.width()-pix.width())//2,(self.art_height-pix.height())//2,pix.width(),pix.height()),7,7);p.setClipPath(clip)
            p.drawPixmap((self.width()-pix.width())//2,(self.art_height-pix.height())//2,pix)
            p.restore()
        else:
            p.fillRect(art,QColor(colors['panel']));p.setPen(QColor(colors['muted']));font=QFont('Segoe UI');font.setPixelSize(13);p.setFont(font);p.drawText(art.adjusted(10,10,-10,-10),Qt.AlignCenter|Qt.TextWordWrap,self.game['title'])
        font=QFont('Segoe UI');font.setPixelSize(14);font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor(colors['text']))
        p.drawText(QRectF(0,self.art_height+5,self.width(),20),Qt.AlignVCenter,p.fontMetrics().elidedText(self.game['title'],Qt.ElideRight,self.width()))
        font.setPixelSize(12);font.setWeight(QFont.Normal);p.setFont(font);p.setPen(QColor(colors['muted']))
        p.drawText(QRectF(0,self.art_height+25,self.width(),18),Qt.AlignVCenter,' · '.join(filter(None,[self.game.get('status'),f"{self.game['seconds']/3600:.0f} h" if self.game.get('seconds') else ''])))
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
    if provider in ('Steam','Google Drive'):
        from pathlib import Path
        source=Path(__file__).resolve().parent/'assets'/'services'/('steam.ico' if provider=='Steam' else 'google-drive.png')
        official=QIcon(str(source)).pixmap(48,48) if provider=='Steam' else QPixmap(str(source)).scaled(36,36,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        p.drawPixmap((48-official.width())//2,(48-official.height())//2,official)
    else:
        p.setPen(QColor('#ffffff'));font=QFont('Segoe UI');font.setPixelSize(16 if provider=='SteamGridDB' else 20);font.setWeight(QFont.Bold);p.setFont(font)
        p.drawText(QRectF(0,0,48,48),Qt.AlignCenter,'SG' if provider=='SteamGridDB' else 'R')
    p.end();return pixmap


class ResponsiveToolbar(QWidget):
    """Filtros ao lado das abas; segunda linha quando a janela é estreita."""
    def __init__(self,left,right,parent=None):
        super().__init__(parent)
        from PySide6.QtWidgets import QBoxLayout,QLayout
        self.left=left;self.right=right;self.row=QBoxLayout(QBoxLayout.LeftToRight,self)
        self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(10);self.row.setSizeConstraint(QLayout.SetNoConstraint)
        self.row.addWidget(left);self.row.addStretch();self.row.addWidget(right)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
    def minimumSizeHint(self):return QSize(0,self.sizeHint().height())
    def resizeEvent(self,event):
        from PySide6.QtWidgets import QBoxLayout
        width=self.left.sizeHint().width()+self.right.sizeHint().width()+20
        direction=QBoxLayout.LeftToRight if self.width()>=width else QBoxLayout.TopToBottom
        if self.row.direction()!=direction:self.row.setDirection(direction);self.updateGeometry()
        super().resizeEvent(event)


def relative_date(value):
    from datetime import datetime,timezone
    try:
        date=datetime.fromisoformat(value.replace('Z','+00:00'))
        if date.tzinfo is None:date=date.replace(tzinfo=timezone.utc)
        seconds=max(0,(datetime.now(timezone.utc)-date).total_seconds())
        if seconds<60:return 'agora'
        if seconds<3600:return f'há {int(seconds//60)} min'
        if seconds<86400:return f'há {int(seconds//3600)} h'
        if seconds<172800:return 'ontem'
        return date.strftime('%d/%m/%Y')
    except (ValueError,AttributeError):return str(value or '')[:10]

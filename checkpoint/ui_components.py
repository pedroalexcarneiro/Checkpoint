from PySide6.QtCore import Qt, QSize, QRectF, QPointF
from PySide6.QtGui import QPixmap, QPainter, QColor, QLinearGradient, QFont, QIcon, QPen, QPolygonF, QRegion, QPainterPath
from .visual_tokens import SPACE,TYPE,RADIUS
from .cover_art import CoverArtwork,paint_art,cover_pixmap
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
    symbols={'←':('back','Voltar'),'…':('more','Mais opções'),'⋯':('more','Mais opções'),'×':('close','Fechar')}
    symbol=symbols.get(title)
    caption='' if symbol else title[2:] if title.startswith('+ ') else title
    button = QPushButton(caption); button.clicked.connect(callback)
    if symbol or title.startswith('+ '):
        from .theme import get_theme
        from PySide6.QtWidgets import QApplication
        color=get_theme(QApplication.instance().property('checkpointTheme')).colors['text']
        button.setIcon(nav_icon(symbol[0] if symbol else 'plus',color,20));button.setIconSize(QSize(20,20))
        if symbol:button.setAccessibleName(symbol[1])
    button.setProperty('variant','primary' if primary else 'secondary')
    button.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed);button.setMinimumHeight(40)
    if primary: button.setObjectName('primary')
    return button


def card():
    from .design_system import CardSurface
    from .visual_tokens import SPACE
    frame = CardSurface()
    layout = QVBoxLayout(frame); layout.setContentsMargins(*([SPACE['lg']]*4)); layout.setSpacing(SPACE['sm'])
    return frame, layout


def nav_icon(name,color,size=24):
    from .icons import lucide_icon
    return lucide_icon(name,color,size)


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
        self.content = QVBoxLayout(self);self.content.setContentsMargins(SPACE['xl'],SPACE['md'],SPACE['xl'],SPACE['lg'])
        self.content.addStretch()

    def set_theme(self, theme):self.theme = theme;self.update()

    def resizeEvent(self,event):
        super().resizeEvent(event)
        ratio=self.banner.width()/self.banner.height() if not self.banner.isNull() else 4.5
        height=(200 if getattr(self,'compact',False) else max(240,min(300,round(event.size().width()/4)))) if self.detail_mode else max(300,min(360,round(event.size().width()/3.5)))
        if height!=self._hero_height:self._hero_height=height;self.setFixedHeight(height)
        self.content.setGeometry(self.rect())

    def paintEvent(self, event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        rect=self.rect();clip=QPainterPath();clip.addRoundedRect(QRectF(rect),RADIUS['card'],RADIUS['card']);p.setClipPath(clip)
        p.fillRect(rect,QColor(self.theme.colors['elevated']))
        if not self.banner.isNull():
            pix=self.banner.scaled(rect.size(),Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
            image_left=rect.right()-pix.width()+1
            p.drawPixmap(image_left,(rect.height()-pix.height())//2,pix)
            if image_left>0:
                edge=QLinearGradient(image_left,0,image_left+100,0)
                edge.setColorAt(0,QColor('#15191e'));edge.setColorAt(1,QColor(21,25,30,0))
                p.fillRect(QRectF(image_left,0,100,self.height()),edge)
        shade=QLinearGradient(0,0,self.width()*.7,0)
        shade.setColorAt(0,QColor(9,12,17,245));shade.setColorAt(.65,QColor(9,12,17,185));shade.setColorAt(1,QColor(9,12,17,0));p.fillRect(rect,shade)
        x=SPACE['xl'];top=64 if self.detail_mode else 56
        if not self.detail_mode:
            font=QFont('Segoe UI');font.setPixelSize(TYPE['caption']);font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor('#e4edf2'))
            p.drawText(QRectF(x,20,self.width()-2*x,20),Qt.AlignVCenter,' · '.join(filter(None,(self.game.get('platform'),self.game.get('status')))))
        identity_height=min(100,max(60,self.height()*.34))
        if not self.logo.isNull():
            logo=self.logo.scaled(min(300 if self.detail_mode else 245,self.width()-52),round(identity_height),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(x,top,logo)
        elif not (self.detail_mode and getattr(self,'compact',False)):
            p.setPen(QColor('#ffffff'));font=QFont('Segoe UI');font.setPixelSize(TYPE['display']);font.setWeight(QFont.DemiBold);p.setFont(font)
            p.drawText(QRectF(x,top,min(self.width()-52,360),identity_height),Qt.AlignLeft|Qt.AlignVCenter|Qt.TextWordWrap,self.game['title'])
        if not self.detail_mode and self.game.get('description'):
            font=QFont('Segoe UI');font.setPixelSize(13);p.setFont(font);p.setPen(QColor('#f0f1f3'))
            width=round(min(340,self.width()*.46));words=self.game['description'].replace('\n',' ').split()
            y=round(top+identity_height+12);available=self.height()-y-64
            for index in range(min(2,max(0,available//20))):
                line=''
                while words and p.fontMetrics().horizontalAdvance((line+' '+words[0]).strip())<=width:line=(line+' '+words.pop(0)).strip()
                if not line:break
                if index==min(2,max(0,available//20))-1 and words:line=p.fontMetrics().elidedText(line+' '+' '.join(words),Qt.ElideRight,width)
                p.drawText(QRectF(x,y+index*20,width,20),Qt.AlignVCenter,line)
        p.end()


class GameTile(CoverArtwork):
    """Mesmo desenho e posições em todos os DPI; sem layout dentro do botão."""
    def __init__(self, game, callback, width=148, parent=None):
        super().__init__(parent);self.setObjectName('gameTile');self.setFixedWidth(width)
        self.game=game;self.callback=callback;self.game_id=game['id'];self.pixmap=cover_pixmap(game)
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
        paint_art(p,art,self.pixmap,self.game['title'],colors,self.hasFocus() or self.underMouse(),fill=True)
        font=QFont('Segoe UI');font.setPixelSize(14);font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor(colors['text']))
        p.drawText(QRectF(0,self.art_height+5,self.width(),20),Qt.AlignVCenter,p.fontMetrics().elidedText(self.game['title'],Qt.ElideRight,self.width()))
        font.setPixelSize(12);font.setWeight(QFont.Normal);p.setFont(font);p.setPen(QColor(colors['muted']))
        p.drawText(QRectF(0,self.art_height+25,self.width(),18),Qt.AlignVCenter,' · '.join(filter(None,[self.game.get('status'),f"{self.game['seconds']/3600:.0f} h" if self.game.get('seconds') else ''])))
        if self.hasFocus():p.setPen(QPen(QColor(colors['accent']),1));p.setBrush(Qt.NoBrush);p.drawRoundedRect(self.rect().adjusted(1,1,-1,-1),RADIUS['card'],RADIUS['card'])
        p.end()

    def open_game(self):self.callback(self.game_id)


class CurrentPageTabs(QTabWidget):
    """Uma aba longa não estica as outras páginas da ficha."""
    def __init__(self,parent=None):
        super().__init__(parent);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
        self.currentChanged.connect(self.page_changed)

    def sizeHint(self):
        page=self.currentWidget()
        if page is None:return super().sizeHint()
        return QSize(page.sizeHint().width(),self.heightForWidth(max(1,self.width())))

    def minimumSizeHint(self):return QSize(0,self.heightForWidth(max(1,self.width())))

    def resizeEvent(self,event):
        super().resizeEvent(event)
        if event.oldSize().width()!=event.size().width():self.updateGeometry()

    def heightForWidth(self,width):
        page=self.currentWidget()
        if page is None:return super().heightForWidth(width)
        height=page.heightForWidth(width) if page.hasHeightForWidth() else page.sizeHint().height()
        return max(0,height)+self.tabBar().sizeHint().height()+8

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


class ProfileButton(QPushButton):
    def __init__(self,title,callback,parent=None):
        super().__init__(title,parent);self.clicked.connect(callback)
    def paintEvent(self,event):
        super().paintEvent(event)
        from .design_system import colors
        p=QPainter(self);p.setPen(QPen(QColor(colors()['muted']),1.6,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin));x=self.width()-15;y=self.height()/2
        p.drawPolyline(QPolygonF([QPointF(x-3,y-2),QPointF(x,y+1),QPointF(x+3,y-2)]));p.end()

"""Componentes comuns da interface: superfícies, arte, estados e composição."""
from PySide6.QtCore import Qt,QSize,QRectF
from PySide6.QtGui import QPainter,QPainterPath,QPixmap,QColor,QPen,QFont
from PySide6.QtWidgets import (QWidget,QFrame,QVBoxLayout,QHBoxLayout,QBoxLayout,
    QGridLayout,QLayout,QSizePolicy,QLabel,QPushButton,QScrollArea,QApplication)
from .theme import get_theme
from .visual_tokens import SPACE,TYPE,RADIUS,HEIGHT
from .smooth_scroll import SmoothScrollArea


def colors():return get_theme(QApplication.instance().property('checkpointTheme')).colors


def icon(name,size=20,accent=False):
    from .ui_components import nav_icon
    return nav_icon(name,colors()['accent' if accent else 'muted']).pixmap(size,size)


class Badge(QLabel):
    def __init__(self,name,size=40,parent=None):
        super().__init__(parent);self.name=name;self.setObjectName('iconBadge');self.setFixedSize(size,size);self.setAlignment(Qt.AlignCenter)
    def paintEvent(self,event):
        super().paintEvent(event);p=QPainter(self)
        if self.name in ('Steam','Google Drive'):
            from .ui_components import service_icon
            pix=service_icon(self.name).scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        else:pix=icon(self.name,min(24,self.width()-14),True)
        p.drawPixmap((self.width()-pix.width())//2,(self.height()-pix.height())//2,pix);p.end()


class IconButton(QPushButton):
    def __init__(self,name,tooltip,callback,parent=None):
        super().__init__(parent);self.name=name;self.setObjectName('iconButton');self.setFixedSize(34,34);self.setToolTip(tooltip);self.setAccessibleName(tooltip);self.clicked.connect(callback)
    def paintEvent(self,event):
        super().paintEvent(event);p=QPainter(self);pix=icon(self.name);p.drawPixmap((self.width()-pix.width())//2,(self.height()-pix.height())//2,pix);p.end()


class CardSurface(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent);self.setObjectName('panel');self.setProperty('component','card')
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)


class StatusChip(QLabel):
    def __init__(self,status,parent=None):
        super().__init__(status,parent);self.setObjectName('statusChip')
        self.setProperty('active',status in ('Jogando','Concluído','Disponível no Drive'))
        self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)


class SectionHeader(QWidget):
    def __init__(self,title,description='',callback=None,button='Ver tudo',parent=None):
        super().__init__(parent)
        from .ui_components import text,action
        row=QHBoxLayout(self);row.setContentsMargins(0,0,0,0);row.setSpacing(SPACE['md'])
        words=QVBoxLayout();words.setSpacing(SPACE['xxs']);words.addWidget(text(title,'sectionTitle'))
        if description:words.addWidget(text(description,'muted'))
        row.addLayout(words,1)
        if callback:
            control=action(button,callback);control.setProperty('variant','ghost');row.addWidget(control)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)


class ActionCard(CardSurface):
    def __init__(self,name,title,description,callback,button,parent=None):
        super().__init__(parent)
        from .ui_components import text,action
        layout=QVBoxLayout(self);layout.setContentsMargins(*([SPACE['lg']]*4));layout.setSpacing(SPACE['sm'])
        layout.addWidget(Badge(name,40));layout.addWidget(text(title,'cardTitle'))
        layout.addWidget(text(description,'secondary'));layout.addWidget(action(button,callback),0,Qt.AlignLeft)


def empty_state(name,title,description,callback=None,button='Adicionar jogo'):
    from .ui_components import text,action
    descriptions={'library':'Reúna seus jogos, escolha o próximo e acompanhe sua jornada.',
                  'wish':'Guarde os jogos que você quer jogar e acompanhe as ofertas.',
                  'memories':'Capturas e anotações dos seus jogos ficam reunidas aqui.',
                  'stats':'Jogue para começar a acompanhar seu tempo e suas conquistas.'}
    frame=CardSurface();frame.setObjectName('emptyState');frame.setProperty('emptyState',True)
    frame.setMinimumHeight(240);frame.setMaximumHeight(300)
    inside=QVBoxLayout(frame);inside.setContentsMargins(*([SPACE['lg']]*4));inside.setSpacing(SPACE['sm'])
    inside.addWidget(Badge(name,48),0,Qt.AlignHCenter)
    label=text(title,'sectionTitle');label.setAlignment(Qt.AlignCenter);inside.addWidget(label)
    label=text(description or descriptions.get(name,'Explore sua biblioteca para começar.'),'emptyDescription')
    label.setAlignment(Qt.AlignCenter);label.setMaximumWidth(480);inside.addWidget(label,0,Qt.AlignHCenter)
    if callback:inside.addWidget(action(button,callback,True),0,Qt.AlignHCenter)
    return frame


def page_scroll(outer,reserve_scrollbar=False):
    scroll=SmoothScrollArea();
    if reserve_scrollbar:
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn);scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.setWidgetResizable(True);scroll.setFrameShape(QFrame.NoFrame)
    body=QWidget();inside=QVBoxLayout(body);inside.setContentsMargins(0,0,4,8);inside.setSpacing(20)
    scroll.setWidget(body);outer.addWidget(scroll);inside.scroll_area=scroll;return inside


class AdaptiveColumns(QWidget):
    def __init__(self,left,right,ratio=(3,2),breakpoint=800,parent=None):
        super().__init__(parent);self.breakpoint=breakpoint;self.ratio=ratio
        self.row=QBoxLayout(QBoxLayout.LeftToRight,self);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(22);self.row.setSizeConstraint(QLayout.SetNoConstraint)
        self.row.addWidget(left,ratio[0]);self.row.addWidget(right,ratio[1]);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
    def minimumSizeHint(self):return QSize(0,self.sizeHint().height())
    def resizeEvent(self,event):
        direction=QBoxLayout.TopToBottom if self.width()<self.breakpoint else QBoxLayout.LeftToRight
        if self.row.direction()!=direction:self.row.setDirection(direction);self.updateGeometry()
        super().resizeEvent(event)


class CardGrid(QWidget):
    def __init__(self,target=300,parent=None,max_columns=None):
        super().__init__(parent);self.target=target;self.max_columns=max_columns;self.cards=[];self.columns=0
        self.grid=QGridLayout(self);self.grid.setContentsMargins(0,0,0,0);self.grid.setSpacing(SPACE['lg']);self.grid.setAlignment(Qt.AlignTop)
    def add_card(self,widget):self.cards.append(widget);self.reflow()
    def reflow(self):
        columns=max(1,self.width()//self.target)
        if self.max_columns:columns=min(columns,self.max_columns)
        width=max(1,(self.width()-max(0,columns-1)*self.grid.spacing())//columns)
        for widget in self.cards:
            if hasattr(widget,'set_tile_width'):widget.set_tile_width(width)
            else:widget.setFixedWidth(width)
        if columns==self.columns and self.grid.count()==len(self.cards):return
        self.columns=columns
        while self.grid.count():self.grid.takeAt(0)
        for index,widget in enumerate(self.cards):self.grid.addWidget(widget,index//columns,index%columns)
    def resizeEvent(self,event):self.reflow();super().resizeEvent(event)


class ArtworkButton(QPushButton):
    def __init__(self,path,caption,callback,height=130,parent=None):
        super().__init__(parent);self.pixmap=QPixmap(path);self.setObjectName('artworkButton');self.setFixedHeight(height);self.setMinimumWidth(100)
        self.setAccessibleName(caption);self.setToolTip(caption);self.clicked.connect(callback)
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);path=QPainterPath();path.addRoundedRect(QRectF(self.rect().adjusted(1,1,-1,-1)),8,8);p.setClipPath(path)
        p.fillRect(self.rect(),QColor(colors()['input']))
        if not self.pixmap.isNull():
            pix=self.pixmap.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation);p.drawPixmap((self.width()-pix.width())//2,(self.height()-pix.height())//2,pix)
        else:p.drawPixmap(self.width()//2-12,self.height()//2-12,icon('memories',24))
        p.setClipping(False)
        if self.underMouse() or self.hasFocus():p.setPen(QPen(QColor(colors()['accent']),2));p.setBrush(Qt.NoBrush);p.drawRoundedRect(QRectF(self.rect().adjusted(1,1,-1,-1)),8,8)
        p.end()


class ThemeSwatch(QPushButton):
    def __init__(self,theme,callback,parent=None):
        super().__init__(parent);self.theme=theme;self.setFixedSize(42,42);self.setToolTip(theme.name);self.setAccessibleName('Tema '+theme.name);self.clicked.connect(callback)
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);chosen=QApplication.instance().property('checkpointTheme')==self.theme.key
        p.setPen(QPen(QColor(colors()['accent'] if chosen else colors()['border']),2 if chosen else 1));p.setBrush(QColor(self.theme.colors['accent']));p.drawRoundedRect(QRectF(3,3,36,36),9,9)
        if chosen:
            p.setPen(QPen(QColor(self.theme.colors['on_accent']),2.2,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin));p.drawLine(14,21,19,26);p.drawLine(19,26,28,16)
        p.end()


def dialog_heading(layout,title,description='',name='settings'):
    from .ui_components import text
    layout.setContentsMargins(24,22,24,22);layout.setSpacing(16)
    from .window_style import titlebar_theme
    if layout.parentWidget():titlebar_theme(layout.parentWidget().window(),True)
    frame=QWidget();frame.setObjectName('dialogHeading');row=QHBoxLayout(frame);row.setContentsMargins(0,0,0,8);row.setSpacing(14);row.addWidget(Badge(name,44),0,Qt.AlignTop)
    words=QVBoxLayout();words.setSpacing(4);words.addWidget(text(title,'sectionTitle'))
    row.addLayout(words,1);layout.insertWidget(0,frame);return frame

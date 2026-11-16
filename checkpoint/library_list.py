"""Lista de cards horizontais: logo, nome, tempo e favorito, sem tabela."""
from PySide6.QtCore import Qt,QRect,QRectF,QSize,Signal
from PySide6.QtGui import QPainter,QColor,QPen,QFont,QPixmap
from PySide6.QtWidgets import QListWidget,QStyledItemDelegate,QStyle
from .smooth_scroll import SmoothScrollMixin
from .design_system import colors
from .icons import lucide_icon


class ListDelegate(QStyledItemDelegate):
    def sizeHint(self,option,index):return QSize(320,84)
    def paint(self,painter,option,index):
        p=painter;p.save();p.setRenderHint(QPainter.Antialiasing);p.setRenderHint(QPainter.SmoothPixmapTransform)
        c=colors();bounds=option.rect.adjusted(0,0,-1,-10);game=index.data(Qt.UserRole+1) or {}
        active=bool(option.state & (QStyle.State_Selected|QStyle.State_MouseOver))
        p.setBrush(QColor(c['selected'] if active else c['panel']));p.setPen(QPen(QColor(c['accent'] if active else c['border']),1))
        p.drawRoundedRect(QRectF(bounds).adjusted(.5,.5,-.5,-.5),9,9)
        logo_area=QRect(bounds.left()+14,bounds.center().y()-24,96,48)
        logo=self.parent().art_cache.load(game.get('logo'),logo_area.width(),logo_area.height(),trim=True)
        if logo.isNull():logo=lucide_icon('library',c['muted'],24).pixmap(24,24)
        p.drawPixmap(logo_area.center().x()-logo.width()//2,logo_area.center().y()-logo.height()//2,logo)
        heart=self.parent().heart_rect(option.rect)
        p.drawPixmap(heart.topLeft(),lucide_icon('heart',c['accent'] if game.get('favorite') else c['muted'],28,filled=bool(game.get('favorite'))).pixmap(28,28))
        font=QFont(option.font);font.setPixelSize(16);font.setWeight(QFont.DemiBold);p.setFont(font);p.setPen(QColor(c['text']))
        value=index.data(Qt.UserRole+2) or '0h00min';time_width=p.fontMetrics().horizontalAdvance(value)+4
        time_rect=QRect(heart.left()-time_width-22,bounds.top(),time_width,bounds.height())
        p.drawText(time_rect,Qt.AlignRight|Qt.AlignVCenter,value)
        font.setPixelSize(15);p.setFont(font)
        title_rect=QRect(logo_area.right()+16,bounds.top(),max(0,time_rect.left()-logo_area.right()-30),bounds.height())
        p.drawText(title_rect,Qt.AlignLeft|Qt.AlignVCenter,p.fontMetrics().elidedText(game.get('title',''),Qt.ElideRight,title_rect.width()))
        p.restore()


class LibraryList(SmoothScrollMixin,QListWidget):
    favorite_requested=Signal(int)
    def __init__(self,parent=None):
        super().__init__(parent);self.enable_smooth_scroll();self.setObjectName('libraryList')
        from .artwork_cache import ArtworkCache
        self.art_cache=ArtworkCache(max_bytes=8*1024*1024,asynchronous=True,parent=self)
        self.setUniformItemSizes(True);self.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);self.setFrameShape(self.Shape.NoFrame)
        self.setStyleSheet('QListWidget#libraryList { background: transparent; border: none; }')
        self.setMouseTracking(True);self.setItemDelegate(ListDelegate(self));self.setSpacing(0)
        self.setAccessibleName('Jogos da biblioteca');self.setAccessibleDescription('Enter abre a ficha; Espaço marca ou retira dos favoritos.')
        from .artwork_prefetch import ArtworkPrefetch
        self.art_prefetch=ArtworkPrefetch(self,covers=False)
    @staticmethod
    def heart_rect(rect):
        return QRect(rect.right()-46,rect.top()+(rect.height()-10-28)//2,28,28)
    def mouseReleaseEvent(self,event):
        item=self.itemAt(event.position().toPoint())
        if event.button()==Qt.LeftButton and item and self.heart_rect(self.visualItemRect(item)).contains(event.position().toPoint()):
            self.favorite_requested.emit(item.data(Qt.UserRole));event.accept();return
        super().mouseReleaseEvent(event)
    def keyPressEvent(self,event):
        item=self.currentItem()
        if event.key()==Qt.Key_Space and item:
            self.favorite_requested.emit(item.data(Qt.UserRole));event.accept();return
        super().keyPressEvent(event)

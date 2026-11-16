"""Cards da biblioteca desenhados com hierarquia própria e grade responsiva."""
from .cover_art import CoverArtwork,cover_pixmap
from .visual_tokens import TYPE,SPACE
from PySide6.QtCore import Qt,QSize,QRectF
from PySide6.QtGui import QPainter,QColor,QFont,QPen,QLinearGradient,QPainterPath
from PySide6.QtWidgets import QListWidget,QStyledItemDelegate,QStyle


class CoverDelegate(QStyledItemDelegate):
    art_component=CoverArtwork
    def sizeHint(self,option,index):return self.parent().gridSize()

    def paint(self,painter,option,index):
        painter.save();painter.setRenderHint(QPainter.Antialiasing)
        colors=self.parent().theme.colors
        hovered=bool(option.state & QStyle.State_MouseOver)
        selected=bool(option.state & QStyle.State_Selected)
        painter.setPen(QPen(QColor(colors['accent']),1) if selected else Qt.NoPen)
        painter.setBrush(QColor(colors['selected']) if hovered or selected else Qt.NoBrush)
        # O foco envolve somente a arte, sem pintar um card atrás do título.
        art=self.parent().art_rect(option.rect)
        game=index.data(Qt.UserRole+1) or {}
        icon=index.data(Qt.DecorationRole);image_rect=art
        pix=self.parent().art_cache.cover(game,art.size().toSize())
        CoverArtwork.paint_art(painter,art,pix,game.get('title','Jogo sem imagem'),colors,selected or hovered,fill=False)
        font=QFont('Segoe UI');font.setPixelSize(14);font.setWeight(QFont.DemiBold);painter.setFont(font);painter.setPen(QColor(colors['text']))
        title=game.get('title') or index.data(Qt.DisplayRole).split('\n')[0]
        painter.drawText(QRectF(image_rect.x(),image_rect.bottom()+6,image_rect.width(),23),Qt.AlignLeft|Qt.AlignVCenter,painter.fontMetrics().elidedText(title,Qt.ElideRight,int(image_rect.width())))
        font.setPixelSize(12);font.setWeight(QFont.Normal);painter.setFont(font)
        from .library import display_status
        status=display_status(game.get('status',''));active=status=='Jogando'
        painter.setPen(Qt.NoPen);painter.setBrush(QColor(colors['accent'] if active else colors['muted']))
        # Status sem marcador duplicado.
        painter.setPen(QColor(colors['muted']));painter.drawText(QRectF(image_rect.x(),image_rect.bottom()+26,image_rect.width(),20),Qt.AlignVCenter,status)
        painter.restore()


from .smooth_scroll import SmoothScrollMixin


class CoverGrid(SmoothScrollMixin,QListWidget):
    def __init__(self,theme,parent=None):
        super().__init__(parent);self.enable_smooth_scroll();self.setVerticalScrollMode(QListWidget.ScrollPerPixel);self.theme=theme;self.cover_percent=100;self.last_grid=None;self.art_ratio=1.5;self.card_gap=SPACE['lg']
        self.setProperty('cardComponent','coverCard')
        from .artwork_cache import ArtworkCache
        self.art_cache=ArtworkCache(asynchronous=True,parent=self);self.setUniformItemSizes(True)
        self.setItemDelegate(CoverDelegate(self));self.setMouseTracking(True)
        self.setViewMode(QListWidget.IconMode);self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static);self.setSpacing(0);self.setWordWrap(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        from .artwork_prefetch import ArtworkPrefetch
        self.art_prefetch=ArtworkPrefetch(self,covers=True)

    def set_cover_size(self,percent):
        if self.cover_percent==percent and self.last_grid is not None:return
        self.cover_percent=percent;self.update_grid()

    def art_rect(self,item_rect):
        occupied=self.columns*self.gridSize().width()-self.card_gap
        margin=max(0,(self.viewport().width()-occupied)/2)
        rect=QRectF(item_rect).adjusted(margin,0,margin-self.card_gap,-self.card_gap)
        return QRectF(rect.x()+2,rect.y()+2,max(1,rect.width()-4),max(1,rect.width()-4)*self.art_ratio)

    def update_grid(self):
        self.art_ratio=1.5
        from .card_layout import card_metrics
        metrics=card_metrics(self.viewport().width(),self.cover_percent)
        self.columns=metrics.columns;self.card_gap=metrics.gap
        cell=metrics.width
        size=QSize(cell+metrics.gap,round((cell-4)*self.art_ratio)+54+metrics.gap)
        self.setIconSize(QSize(max(1,cell),max(1,round(cell*self.art_ratio))))
        if self.last_grid!=size:self.last_grid=size;self.setGridSize(size)
        self.viewport().update()

    def resizeEvent(self,event):super().resizeEvent(event);self.update_grid()

"""Cards da biblioteca desenhados com hierarquia própria e grade responsiva."""
from PySide6.QtCore import Qt,QSize,QRectF
from PySide6.QtGui import QPainter,QColor,QFont,QPen,QLinearGradient,QPainterPath
from PySide6.QtWidgets import QListWidget,QStyledItemDelegate,QStyle


class CoverDelegate(QStyledItemDelegate):
    def sizeHint(self,option,index):return self.parent().gridSize()

    def paint(self,painter,option,index):
        painter.save();painter.setRenderHint(QPainter.Antialiasing)
        colors=self.parent().theme.colors
        rect=QRectF(option.rect).adjusted(0,0,-16,-8)
        hovered=bool(option.state & QStyle.State_MouseOver)
        selected=bool(option.state & QStyle.State_Selected)
        painter.setPen(QPen(QColor(colors['accent']),1) if selected else Qt.NoPen)
        painter.setBrush(QColor(colors['selected']) if hovered or selected else Qt.NoBrush)
        # O foco envolve somente a arte, sem pintar um card atrás do título.
        art=QRectF(rect.x()+2,rect.y()+2,rect.width()-4,(rect.width()-4)*self.parent().art_ratio)
        game=index.data(Qt.UserRole+1) or {}
        icon=index.data(Qt.DecorationRole);image_rect=art
        if game.get('cover') and icon and not icon.isNull():
            # O recorte suave acompanha a própria imagem, sem moldura lateral.
            bounds=art
            pix=icon.pixmap(bounds.size().toSize()).scaled(bounds.size().toSize(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            image_rect=QRectF(bounds.x(),bounds.y(),pix.width(),pix.height())
            painter.save();clip=QPainterPath();clip.addRoundedRect(image_rect,7,7);painter.setClipPath(clip)
            painter.drawPixmap(round(image_rect.x()),round(image_rect.y()),pix)
            painter.restore()
        else:
            painter.fillRect(art,QColor(colors['panel']))
            painter.setPen(QColor(colors['accent']));font=QFont('Segoe UI');font.setPixelSize(15);font.setWeight(QFont.DemiBold);painter.setFont(font)
            painter.drawText(art.adjusted(14,14,-14,-14),Qt.AlignCenter|Qt.TextWordWrap,game.get('title') or 'Jogo sem imagem')
        font=QFont('Segoe UI');font.setPixelSize(14);font.setWeight(QFont.DemiBold);painter.setFont(font);painter.setPen(QColor(colors['text']))
        title=game.get('title') or index.data(Qt.DisplayRole).split('\n')[0]
        painter.drawText(QRectF(image_rect.x(),image_rect.bottom()+6,image_rect.width(),23),Qt.AlignLeft|Qt.AlignVCenter,painter.fontMetrics().elidedText(title,Qt.ElideRight,int(image_rect.width())))
        font.setPixelSize(12);font.setWeight(QFont.Normal);painter.setFont(font)
        if hovered or selected:
            painter.setPen(QPen(QColor(colors['accent']),2 if selected else 1));painter.setBrush(Qt.NoBrush);painter.drawRoundedRect(image_rect,7,7)
        status=game.get('status','');active=status=='Jogando'
        painter.setPen(Qt.NoPen);painter.setBrush(QColor(colors['accent'] if active else colors['muted']))
        # Status sem marcador duplicado.
        painter.setPen(QColor(colors['muted']));painter.drawText(QRectF(image_rect.x(),image_rect.bottom()+26,image_rect.width(),20),Qt.AlignVCenter,status)
        painter.restore()


class CoverGrid(QListWidget):
    def __init__(self,theme,parent=None):
        super().__init__(parent);self.theme=theme;self.compact=False;self.last_grid=None;self.art_ratio=1.5
        self.setItemDelegate(CoverDelegate(self));self.setMouseTracking(True)
        self.setViewMode(QListWidget.IconMode);self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static);self.setSpacing(0);self.setWordWrap(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def set_density(self,compact):
        self.compact=compact;self.update_grid()

    def update_grid(self):
        self.art_ratio=1.5
        width=max(4,self.viewport().width()-16)
        cell=max(1,width//4)
        size=QSize(cell,round((cell-20)*self.art_ratio)+54)
        if self.last_grid!=size:self.last_grid=size;self.setGridSize(size)
        self.viewport().update()

    def resizeEvent(self,event):super().resizeEvent(event);self.update_grid()

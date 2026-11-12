"""Cards da biblioteca desenhados com hierarquia própria e grade responsiva."""
from PySide6.QtCore import Qt,QSize,QRectF
from PySide6.QtGui import QPainter,QColor,QFont,QPen,QLinearGradient,QPainterPath
from PySide6.QtWidgets import QListWidget,QStyledItemDelegate,QStyle


class CoverDelegate(QStyledItemDelegate):
    def sizeHint(self,option,index):return self.parent().gridSize()

    def paint(self,painter,option,index):
        painter.save();painter.setRenderHint(QPainter.Antialiasing)
        colors=self.parent().theme.colors
        rect=QRectF(option.rect).adjusted(3,3,-15,-15)
        hovered=bool(option.state & QStyle.State_MouseOver)
        selected=bool(option.state & QStyle.State_Selected)
        painter.setPen(QPen(QColor(colors['accent']),1) if selected else Qt.NoPen)
        painter.setBrush(QColor(colors['selected']) if hovered or selected else Qt.NoBrush)
        if hovered or selected:painter.drawRoundedRect(rect,9,9)
        art=QRectF(rect.x()+2,rect.y()+2,rect.width()-4,(rect.width()-4)*1.5)
        game=index.data(Qt.UserRole+1) or {}
        icon=index.data(Qt.DecorationRole)
        if game.get('cover') and icon and not icon.isNull():
            # O recorte suave acompanha a própria imagem, sem moldura lateral.
            bounds=art
            pix=icon.pixmap(bounds.size().toSize()).scaled(bounds.size().toSize(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            image_rect=QRectF(bounds.center().x()-pix.width()/2,bounds.bottom()-pix.height(),pix.width(),pix.height())
            painter.save();clip=QPainterPath();clip.addRoundedRect(image_rect,7,7);painter.setClipPath(clip)
            painter.drawPixmap(int(bounds.center().x()-pix.width()/2),int(bounds.bottom()-pix.height()),pix)
            painter.restore()
        else:
            painter.fillRect(art,QColor(colors['panel']))
            painter.setPen(QColor(colors['accent']));font=QFont('Segoe UI');font.setPixelSize(34);font.setWeight(QFont.Light);painter.setFont(font)
            painter.drawText(art,Qt.AlignCenter,(game.get('title') or '?')[:2].upper())
        font=QFont('Segoe UI');font.setPixelSize(15);font.setWeight(QFont.DemiBold);painter.setFont(font);painter.setPen(QColor(colors['text']))
        title=game.get('title') or index.data(Qt.DisplayRole).split('\n')[0]
        painter.drawText(QRectF(art.x(),art.bottom()+12,art.width(),23),Qt.AlignLeft|Qt.AlignVCenter,painter.fontMetrics().elidedText(title,Qt.ElideRight,int(art.width())))
        font.setPixelSize(12);font.setWeight(QFont.Normal);painter.setFont(font)
        status=game.get('status','');active=status=='Jogando'
        painter.setPen(Qt.NoPen);painter.setBrush(QColor(colors['accent'] if active else colors['muted']))
        painter.drawEllipse(QRectF(art.x(),art.bottom()+42,5,5))
        painter.setPen(QColor(colors['muted']));painter.drawText(QRectF(art.x()+12,art.bottom()+34,art.width()-12,23),Qt.AlignVCenter,status)
        painter.restore()


class CoverGrid(QListWidget):
    def __init__(self,theme,parent=None):
        super().__init__(parent);self.theme=theme;self.compact=False;self.last_grid=None
        self.setItemDelegate(CoverDelegate(self));self.setMouseTracking(True)
        self.setViewMode(QListWidget.IconMode);self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static);self.setSpacing(0);self.setWordWrap(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def set_density(self,compact):
        self.compact=compact;self.update_grid()

    def update_grid(self):
        width=max(1,self.viewport().width()-32);target=174 if self.compact else 218
        columns=max(1,width//target);cell=max(100,width//columns)
        size=QSize(cell,round((cell-22)*1.5)+82)
        if self.last_grid!=size:self.last_grid=size;self.setGridSize(size)
        self.viewport().update()

    def resizeEvent(self,event):super().resizeEvent(event);self.update_grid()

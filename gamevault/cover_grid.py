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
        painter.setPen(QPen(QColor(colors['accent'] if selected else colors['border']),1) if hovered or selected else Qt.NoPen)
        painter.setBrush(QColor(colors['selected'] if selected else colors['panel'] if hovered else colors['background']))
        painter.drawRoundedRect(rect,11,11)
        art=QRectF(rect.x()+5,rect.y()+5,rect.width()-10,(rect.width()-10)*4/3)
        path=QPainterPath();path.addRoundedRect(art,8,8)
        gradient=QLinearGradient(art.topLeft(),art.bottomRight());gradient.setColorAt(0,QColor(colors['selected']));gradient.setColorAt(1,QColor(colors['panel']))
        painter.fillPath(path,gradient)
        game=index.data(Qt.UserRole+1) or {}
        icon=index.data(Qt.DecorationRole)
        if game.get('cover') and icon and not icon.isNull():
            # A margem mantém toda a imagem dentro do quadro, inclusive os cantos.
            bounds=art.adjusted(3,3,-3,-3)
            pix=icon.pixmap(bounds.size().toSize()).scaled(bounds.size().toSize(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            painter.drawPixmap(int(bounds.center().x()-pix.width()/2),int(bounds.center().y()-pix.height()/2),pix)
        else:
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
        size=QSize(cell,int((cell-28)*4/3)+88)
        if self.last_grid!=size:self.last_grid=size;self.setGridSize(size)
        self.viewport().update()

    def resizeEvent(self,event):super().resizeEvent(event);self.update_grid()

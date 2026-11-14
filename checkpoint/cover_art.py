"""Arte contida e alinhada: mesmo componente em capas, desejos e resultados."""
from PySide6.QtCore import Qt,QRectF
from PySide6.QtGui import QPainterPath,QColor,QPen,QFont,QPixmap
from PySide6.QtWidgets import QPushButton
from .visual_tokens import RADIUS,TYPE


def paint_art(painter,bounds,pixmap,title,colors,selected=False,padding=0,fill=False):
    painter.save();clip=QPainterPath();clip.addRoundedRect(bounds,RADIUS['card'],RADIUS['card'])
    painter.setClipPath(clip);painter.fillRect(bounds,QColor(colors['surface']))
    if pixmap and not pixmap.isNull():
        area=bounds.adjusted(padding,padding,-padding,-padding)
        scaled=pixmap.scaled(area.size().toSize(),Qt.KeepAspectRatioByExpanding if fill else Qt.KeepAspectRatio,Qt.SmoothTransformation)
        painter.drawPixmap(round(area.center().x()-scaled.width()/2),round(area.center().y()-scaled.height()/2),scaled)
    else:
        painter.fillRect(bounds,QColor(colors['elevated']))
        font=QFont('Segoe UI');font.setPixelSize(TYPE['body']);font.setWeight(QFont.DemiBold)
        painter.setFont(font);painter.setPen(QColor(colors['secondary']))
        if bounds.width()<80:
            from .ui_components import nav_icon
            icon=nav_icon('library',colors['muted']).pixmap(24,24)
            painter.drawPixmap(round(bounds.center().x()-12),round(bounds.center().y()-12),icon)
        else:painter.drawText(bounds.adjusted(12,12,-12,-12),Qt.AlignCenter|Qt.TextWordWrap,title)
    painter.setClipping(False);painter.setBrush(Qt.NoBrush)
    painter.setPen(QPen(QColor(colors['accent'] if selected else colors['border_subtle']),2 if selected else 1))
    painter.drawRoundedRect(bounds.adjusted(1,1,-1,-1),RADIUS['card'],RADIUS['card']);painter.restore()


class CoverArtwork(QPushButton):
    paint_art=staticmethod(paint_art)
    def __init__(self,parent=None):
        super().__init__(parent);self.setProperty('component','coverCard')

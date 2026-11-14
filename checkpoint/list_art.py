"""Miniatura de largura fixa: logo contida ou título, sem capa na lista."""
from PySide6.QtCore import Qt,QRectF
from PySide6.QtGui import QPixmap,QPainter,QIcon,QColor,QFont


def list_icon(game,color):
    pix=QPixmap(140,48);pix.fill(Qt.transparent);p=QPainter(pix)
    logo=QPixmap(game.get('logo') or '')
    if logo.isNull():
        font=QFont('Segoe UI');font.setPixelSize(12);p.setFont(font);p.setPen(QColor(color))
        p.drawText(pix.rect().adjusted(4,4,-4,-4),Qt.AlignCenter|Qt.TextWordWrap,game['title'])
    else:
        logo=logo.scaled(132,40,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        p.drawPixmap((140-logo.width())//2,(48-logo.height())//2,logo)
    p.end();return QIcon(pix)

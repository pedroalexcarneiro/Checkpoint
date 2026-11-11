from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap,QPainter,QColor


def fit_artwork(pixmap,width,height,background):
    canvas=QPixmap(width,height);canvas.fill(QColor(background))
    if not pixmap.isNull():
        scaled=pixmap.scaled(width,height,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        painter=QPainter(canvas);painter.drawPixmap((width-scaled.width())//2,(height-scaled.height())//2,scaled);painter.end()
    return canvas

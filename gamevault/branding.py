"""Identidade intervalo: C// e checkpo//nt, desenhados em vetor pelo Qt."""
from PySide6.QtCore import Qt, QRectF, QSize, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QFontMetricsF, QIcon, QPixmap
from PySide6.QtWidgets import QWidget


def draw_symbol(painter, rect, foreground, accent):
    painter.save()
    painter.translate(rect.x(), rect.y())
    painter.scale(rect.width()/44, rect.height()/36)
    painter.setPen(QPen(QColor(foreground), 4.4, Qt.SolidLine, Qt.RoundCap))
    painter.drawArc(QRectF(3, 5, 24, 26), 47*16, 266*16)
    painter.setPen(QPen(QColor(accent), 4.2, Qt.SolidLine, Qt.RoundCap))
    for x in (30, 38):
        painter.drawLine(x, 28, x+5, 8)
    painter.restore()


def app_icon(theme):
    icon = QIcon()
    for size in (16, 24, 32, 48, 64, 128, 256):
        pixmap = QPixmap(size, size); pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap); painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen); painter.setBrush(QColor(theme.colors['sidebar']))
        painter.drawRoundedRect(QRectF(0, 0, size, size), size*.2, size*.2)
        draw_symbol(painter, QRectF(size*.12, size*.2, size*.76, size*.61),
                    theme.colors['text'], theme.colors['accent'])
        painter.end(); icon.addPixmap(pixmap)
    return icon


class BrandWidget(QWidget):
    symbol_gap = 18  # Seis pixels extras em relação ao espaçamento inicial.

    def __init__(self, theme, parent=None):
        super().__init__(parent); self.theme = theme
        self.setAccessibleName('Checkpoint'); self.setMinimumHeight(56)
        self.setMinimumWidth(206)

    def sizeHint(self): return QSize(212, 56)

    def set_theme(self, theme):
        self.theme = theme; self.update()

    def paintEvent(self, event):
        p = QPainter(self); p.setRenderHint(QPainter.Antialiasing)
        colors = self.theme.colors
        draw_symbol(p, QRectF(0, 12, 34, 30), colors['text'], colors['accent'])
        font = QFont('Segoe UI', 15); font.setWeight(QFont.DemiBold)
        p.setFont(font); p.setPen(QColor(colors['text']))
        metrics = QFontMetricsF(font); baseline = (self.height()+metrics.ascent()-metrics.descent())/2
        x = 34+self.symbol_gap
        p.drawText(QRectF(x, 0, 140, self.height()), Qt.AlignVCenter, 'checkpo')
        x += metrics.horizontalAdvance('checkpo')+3
        height = metrics.xHeight()
        p.setPen(QPen(QColor(colors['accent']), 2.6, Qt.SolidLine, Qt.RoundCap))
        for offset in (0, 6):
            p.drawLine(QPointF(x+offset, baseline-1), QPointF(x+offset+3, baseline-height+1))
        p.setPen(QColor(colors['text']))
        p.drawText(QRectF(x+12, 0, 40, self.height()), Qt.AlignVCenter, 'nt')
        p.end()

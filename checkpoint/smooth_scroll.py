"""Rolagem por pixel; animação restrita à barra, sem repintar a grade inteira."""
from PySide6.QtCore import QPropertyAnimation,QEasingCurve,QAbstractAnimation,Qt
from PySide6.QtWidgets import QScrollArea

class SmoothScrollMixin:
    def enable_smooth_scroll(self):
        self.scroll_animation=QPropertyAnimation(self.verticalScrollBar(),b'value',self)
        self.scroll_animation.setDuration(180)
        self.scroll_animation.setEasingCurve(QEasingCurve.OutCubic)
    def wheelEvent(self,event):
        if event.modifiers() & Qt.ControlModifier:
            return super().wheelEvent(event)
        delta=event.pixelDelta().y() or event.angleDelta().y()/120*72
        if not delta:return super().wheelEvent(event)
        bar=self.verticalScrollBar();animation=self.scroll_animation
        target=animation.endValue() if animation.state()==QAbstractAnimation.Running else bar.value()
        target=max(bar.minimum(),min(bar.maximum(),round(target-delta)))
        animation.stop();animation.setStartValue(bar.value());animation.setEndValue(target);animation.start();event.accept()

class SmoothScrollArea(SmoothScrollMixin,QScrollArea):
    def __init__(self,parent=None):
        super().__init__(parent);self.enable_smooth_scroll()
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

"""Rolagem por pixel; animação restrita à barra, sem repintar a grade inteira."""
from PySide6.QtCore import QEvent,QPropertyAnimation,QEasingCurve,QAbstractAnimation,QSize,Qt
from PySide6.QtWidgets import QFrame,QHBoxLayout,QScrollArea,QSizePolicy,QWidget

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
        bar=self.verticalScrollBar();bar.setEnabled(bar.maximum()>bar.minimum())
        bar.rangeChanged.connect(lambda minimum,maximum:bar.setEnabled(maximum>minimum))


class HorizontalCardScroll(QScrollArea):
    """Uma faixa de cards recortada pelo viewport, com navegação por posição."""
    def __init__(self,card_width,spacing,*,center=False,page_scroll=None):
        super().__init__()
        self.stride=card_width+spacing
        self.page_scroll=page_scroll
        self.body=QWidget()
        self.setFrameShape(QFrame.NoFrame)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.row=QHBoxLayout(self.body)
        self.row.setContentsMargins(0,0,0,0)
        self.row.setSpacing(spacing)
        self.row.setAlignment((Qt.AlignHCenter if center else Qt.AlignLeft)|Qt.AlignTop)
        self.setWidget(self.body)
        self.body.installEventFilter(self)
        self.animation=QPropertyAnimation(self.horizontalScrollBar(),b'value',self)
        self.animation.setDuration(220)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    def sizeHint(self):
        return QSize(0,self.body.sizeHint().height())

    def minimumSizeHint(self):
        return self.sizeHint()

    def eventFilter(self,watched,event):
        if watched is self.body and event.type()==QEvent.LayoutRequest:
            self.updateGeometry()
        return super().eventFilter(watched,event)

    def destination(self):
        bar=self.horizontalScrollBar()
        if self.animation.state()==QAbstractAnimation.Running:
            return min(bar.maximum(),self.animation.endValue())
        return bar.value()

    def scroll_to(self,value,animate=True):
        bar=self.horizontalScrollBar()
        target=max(0,min(bar.maximum(),value))
        self.animation.stop()
        if animate and bar.value()!=target:
            self.animation.setStartValue(bar.value())
            self.animation.setEndValue(target)
            self.animation.start()
        else:
            bar.setValue(target)

    def step(self,direction):
        position=self.destination()
        index=position//self.stride+1 if direction>0 else (position-1)//self.stride
        self.scroll_to(index*self.stride)

    def bind_arrows(self,previous,next_button):
        bar=self.horizontalScrollBar()
        def update(*_):
            maximum=bar.maximum()
            previous.setVisible(maximum>0)
            next_button.setVisible(maximum>0)
            previous.setEnabled(bar.value()>0)
            next_button.setEnabled(bar.value()<maximum)
        bar.valueChanged.connect(update)
        bar.rangeChanged.connect(update)
        update()

    def wheelEvent(self,event):
        pixels=event.pixelDelta()
        angle=event.angleDelta()
        if event.modifiers() & Qt.ShiftModifier:
            delta=pixels.x() or pixels.y() or round((angle.x() or angle.y())/120*72)
        elif abs(pixels.x())>abs(pixels.y()) or abs(angle.x())>abs(angle.y()):
            delta=pixels.x() or round(angle.x()/120*72)
        else:
            if self.page_scroll is not None:
                return self.page_scroll.wheelEvent(event)
            event.ignore()
            return
        if delta and self.horizontalScrollBar().maximum()>0:
            self.scroll_to(self.destination()-delta,animate=pixels.isNull())
            event.accept()
        else:
            event.ignore()

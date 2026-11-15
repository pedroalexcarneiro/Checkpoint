"""Recorte quadrado não destrutivo com arrasto e zoom para avatar local."""
from math import isfinite
from PySide6.QtCore import Qt,QRectF,QSize,Signal
from PySide6.QtGui import QImage,QPainter,QPainterPath,QColor,QPen
from PySide6.QtWidgets import QWidget
from .design_system import colors


class AvatarCrop(QWidget):
    changed=Signal()
    def __init__(self,parent=None):
        super().__init__(parent);self.source=QImage();self.zoom=1.;self.center_x=.5;self.center_y=.5;self.drag=None
        self.setFixedSize(240,240);self.setObjectName('avatarCrop');self.setFocusPolicy(Qt.StrongFocus);self.setCursor(Qt.OpenHandCursor)
        self.setAccessibleName('Recorte da foto');self.setAccessibleDescription('Setas reposicionam a imagem; controle Zoom amplia o recorte.')
    def set_source(self,image,state=None):
        self.source=image;state=state if isinstance(state,dict) else {}
        self.zoom=self.number(state.get('zoom',1),1,4,1)
        self.center_x=self.number(state.get('x',.5),0,1,.5);self.center_y=self.number(state.get('y',.5),0,1,.5)
        self.clamp();self.update();self.changed.emit()
    @staticmethod
    def number(value,low,high,default):
        try:value=float(value)
        except (ValueError,TypeError):return default
        return max(low,min(high,value)) if isfinite(value) else default
    def state(self):return {'zoom':self.zoom,'x':self.center_x,'y':self.center_y}
    def crop_rect(self):
        if self.source.isNull():return QRectF()
        side=min(self.source.width(),self.source.height())/self.zoom
        return QRectF(self.center_x*self.source.width()-side/2,self.center_y*self.source.height()-side/2,side,side)
    def clamp(self):
        if self.source.isNull():return
        half=min(self.source.width(),self.source.height())/self.zoom/2
        self.center_x=max(half/self.source.width(),min(1-half/self.source.width(),self.center_x))
        self.center_y=max(half/self.source.height(),min(1-half/self.source.height(),self.center_y))
    def set_center(self,x,y):
        self.center_x=self.number(x,0,1,.5);self.center_y=self.number(y,0,1,.5);self.clamp();self.update();self.changed.emit()
    def set_zoom(self,percent):
        self.zoom=self.number(percent/100,1,4,1);self.clamp();self.update();self.changed.emit()
    def render_avatar(self):
        if self.source.isNull():return QImage()
        result=QImage(256,256,QImage.Format_ARGB32);result.fill(Qt.transparent)
        p=QPainter(result);p.setRenderHint(QPainter.SmoothPixmapTransform);p.drawImage(QRectF(result.rect()),self.source,self.crop_rect());p.end();return result
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);p.setRenderHint(QPainter.SmoothPixmapTransform);c=colors();p.fillRect(self.rect(),QColor(c['input']))
        if not self.source.isNull():p.drawImage(QRectF(self.rect()),self.source,self.crop_rect())
        outside=QPainterPath();outside.addRect(QRectF(self.rect()));outside.addEllipse(QRectF(self.rect()).adjusted(2,2,-2,-2));outside.setFillRule(Qt.OddEvenFill)
        p.fillPath(outside,QColor(0,0,0,140));p.setBrush(Qt.NoBrush);p.setPen(QPen(QColor(c['accent']),2));p.drawEllipse(QRectF(self.rect()).adjusted(2,2,-2,-2));p.end()
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton and not self.source.isNull():self.drag=event.position();self.setCursor(Qt.ClosedHandCursor);event.accept()
        else:super().mousePressEvent(event)
    def mouseMoveEvent(self,event):
        if self.drag is not None:
            delta=event.position()-self.drag;self.drag=event.position();side=self.crop_rect().width()
            self.set_center(self.center_x-delta.x()*side/self.width()/self.source.width(),self.center_y-delta.y()*side/self.height()/self.source.height());event.accept()
        else:super().mouseMoveEvent(event)
    def mouseReleaseEvent(self,event):self.drag=None;self.setCursor(Qt.OpenHandCursor);super().mouseReleaseEvent(event)
    def keyPressEvent(self,event):
        steps={Qt.Key_Left:(-.02,0),Qt.Key_Right:(.02,0),Qt.Key_Up:(0,-.02),Qt.Key_Down:(0,.02)}
        if event.key() in steps:
            x,y=steps[event.key()];self.set_center(self.center_x+x,self.center_y+y);event.accept()
        else:super().keyPressEvent(event)

"""Menu contido na janela, inclusive quando ela atravessa os limites da tela."""
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QMenu


class WindowMenu(QMenu):
    def showEvent(self,event):
        super().showEvent(event)
        window=self.parentWidget().window()
        self.setMaximumSize(window.size())
        point=window.mapFromGlobal(self.pos())
        x=max(0,min(point.x(),window.width()-self.width()))
        y=max(0,min(point.y(),window.height()-self.height()))
        self.move(window.mapToGlobal(QPoint(x,y)))

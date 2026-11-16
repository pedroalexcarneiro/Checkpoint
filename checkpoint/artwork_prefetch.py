"""Antecipação limitada de arte perto da área visível da Biblioteca."""
import math
from PySide6.QtCore import QObject,QEvent,QTimer,Qt


class ArtworkPrefetch(QObject):
    def __init__(self,view,*,covers):
        super().__init__(view);self.view=view;self.covers=covers
        self.timer=QTimer(self);self.timer.setSingleShot(True);self.timer.setInterval(0)
        self.timer.timeout.connect(self.load_nearby)
        view.verticalScrollBar().valueChanged.connect(self.schedule)
        for signal in (view.model().rowsInserted,view.model().modelReset,view.model().dataChanged):signal.connect(self.schedule)
        view.viewport().installEventFilter(self)
        view.art_cache.ready.connect(view.viewport().update)
    def schedule(self,*args):
        if not self.timer.isActive():self.timer.start()
    def eventFilter(self,watched,event):
        if event.type() in (QEvent.Resize,QEvent.Show):self.schedule()
        return False
    def load_nearby(self):
        view=self.view
        if not view.isVisible() or not view.count():return
        columns=max(1,getattr(view,'columns',1)) if self.covers else 1
        height=max(1,view.gridSize().height()) if self.covers else 84
        first_row=max(0,view.verticalScrollBar().value()//height)
        visible_rows=math.ceil(view.viewport().height()/height)+1
        # Priorizar as linhas visíveis; depois uma linha abaixo e uma acima.
        rows=list(range(first_row,first_row+visible_rows+1))
        if first_row:rows.append(first_row-1)
        for row in rows:
            for index in range(row*columns,min(view.count(),(row+1)*columns)):
                item=view.item(index);game=item.data(Qt.UserRole+1) or {}
                if self.covers:
                    size=view.art_rect(view.visualItemRect(item)).size().toSize()
                    view.art_cache.cover(game,size,prefetch=True)
                else:view.art_cache.load(game.get('logo'),96,48,trim=True,prefetch=True)

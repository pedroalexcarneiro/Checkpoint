"""Atividade por período: barras, mês em calendário e heatmap compacto."""
from calendar import monthrange
from datetime import datetime,timedelta
from PySide6.QtCore import Qt,QRectF,QSize
from PySide6.QtGui import QPainter,QColor,QFont,QPen
from PySide6.QtWidgets import QWidget,QToolTip
from .activity_heatmap import ActivityHeatmap,MONTHS
from .design_system import colors
from .playtime import format_time
from .theme import blend


class PeriodChart(ActivityHeatmap):
    def __init__(self,*args,**kwargs):
        self.period='12m';self.hours=[]
        super().__init__(*args,**kwargs);self.setObjectName('periodActivityChart')
    def set_period(self,period,hours=None):
        self.period=period;self.hours=hours or [];self.fit_height();self.update()
    def months(self):
        first,last=self.interval();cursor=first.replace(day=1);result=[]
        while cursor<=last:
            result.append(cursor);cursor=(cursor.replace(day=28)+timedelta(days=4)).replace(day=1)
        return result
    def cell_size(self,columns=31):return ActivityHeatmap.cell_size(self,columns)
    def desired_height(self):
        if self.period in ('daily','weekly'):return 190
        if self.period=='monthly':
            first,last=self.interval();rows=(monthrange(first.year,first.month)[1]+first.weekday()+6)//7
            return 54+rows*(min(40,max(20,(self.width()-20)//7-6))+6)
        first,last=self.interval();columns=(last-(first-timedelta(days=first.weekday()))).days//7+1
        return 28+7*(self.cell_size(columns)+3)+42
    def fit_height(self):
        height=self.desired_height()
        if self.height()!=height:self.setFixedHeight(height)
        self.height_changed.emit(height)
    def sizeHint(self):return QSize(740,self.desired_height())
    def resizeEvent(self,event):self.fit_height();QWidget.resizeEvent(self,event)
    def paintEvent(self,event):
        if self.period not in ('daily','weekly','monthly'):
            ActivityHeatmap.paintEvent(self,event);return
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors();font=QFont(self.font());font.setPixelSize(11);p.setFont(font);self.cells=[]
        if self.period in ('daily','weekly'):self.paint_bars(p,c)
        else:self.paint_calendar(p,c)
        p.end()
    def paint_bars(self,p,c):
        first,last=self.interval()
        if self.period=='daily':
            entries=[(r['label'],r['seconds'],r['start']) for r in self.hours]
            if not entries:entries=[(f'{n:02}h',0,first) for n in range(24)]
        else:
            monday=first-timedelta(days=first.weekday());names=('Seg','Ter','Qua','Qui','Sex','Sáb','Dom')
            entries=[(names[n],self.values.get((monday+timedelta(days=n)).isoformat(),0),monday+timedelta(days=n)) for n in range(7)]
        left=12;available=max(1,self.width()-24);slot=available/max(1,len(entries));bar=min(44,max(3,slot*.58));bottom=145;scale=max(3600,max((e[1] for e in entries),default=0))
        p.setPen(QColor(c['border']));p.drawLine(left,bottom,self.width()-12,bottom)
        for n,(label,seconds,stamp) in enumerate(entries):
            x=left+n*slot+(slot-bar)/2;height=110*seconds/scale
            hit=QRectF(left+n*slot,10,slot,164);self.cells.append((hit,stamp,seconds))
            p.setPen(Qt.NoPen);p.setBrush(QColor(c['accent'] if seconds else c['button']))
            p.drawRoundedRect(QRectF(x,bottom-max(3,height),bar,max(3,height)),3,3)
            p.setPen(QColor(c['muted']))
            if self.period=='weekly' or n%3==0:p.drawText(QRectF(left+n*slot,151,slot,20),Qt.AlignCenter,label)
            if seconds and self.period=='weekly':p.drawText(QRectF(left+n*slot,max(4,bottom-height-22),slot,20),Qt.AlignCenter,format_time(seconds))
        p.setPen(QColor(c['muted']));p.drawText(QRectF(12,174,self.width()-24,16),Qt.AlignLeft,format_time(sum(e[1] for e in entries)))
    def paint_calendar(self,p,c):
        first,last=self.interval();cell=min(40,max(20,(self.width()-20)//7-6));stride=cell+6;left=max(0,(self.width()-7*stride+6)/2);top=26
        shades=[blend(c['panel'],c['text'],.055),blend(c['panel'],c['accent'],.24),blend(c['panel'],c['accent'],.46),blend(c['panel'],c['accent'],.72),c['accent']]
        p.setPen(QColor(c['muted']))
        for n,name in enumerate(('Seg','Ter','Qua','Qui','Sex','Sáb','Dom')):p.drawText(QRectF(left+n*stride,0,cell,20),Qt.AlignCenter,name)
        for number in range(1,monthrange(first.year,first.month)[1]+1):
            day=first.replace(day=number);offset=number-1+first.weekday();row,column=divmod(offset,7)
            seconds=self.values.get(day.isoformat(),0);level=0 if seconds<=0 else 1 if seconds<1800 else 2 if seconds<3600 else 3 if seconds<10800 else 4
            rect=QRectF(left+column*stride,top+row*stride,cell,cell)
            if day<=last:self.cells.append((rect,day,seconds))
            p.setPen(QPen(QColor(c['border']),.4));p.setBrush(QColor(shades[level]));p.drawRoundedRect(rect,4,4)
            p.setPen(QColor(c['muted'] if day>last else c['text']));p.drawText(rect,Qt.AlignCenter,str(number))
        p.setPen(QColor(c['muted']));total=sum(s for day,s in self.values.items() if first.isoformat()<=day<=last.isoformat())
        p.drawText(QRectF(left,self.height()-22,max(1,self.width()-left),20),Qt.AlignLeft,format_time(total) if total else 'Nenhuma sessão neste período')
    def mouseMoveEvent(self,event):
        for rect,stamp,seconds in self.cells:
            if rect.contains(event.position()):
                label=stamp.astimezone().strftime('%d/%m/%Y %H:%M %z') if isinstance(stamp,datetime) else stamp.strftime('%d/%m/%Y')
                QToolTip.showText(event.globalPosition().toPoint(),label+' · '+format_time(seconds),self);break
        else:QToolTip.hideText()
        QWidget.mouseMoveEvent(self,event)

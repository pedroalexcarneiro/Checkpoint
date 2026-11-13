"""Calendário de horas reais, em células diárias como um gráfico de contribuições."""
from datetime import date,datetime,timedelta,timezone
from PySide6.QtCore import Qt,QRectF,QSize
from PySide6.QtGui import QPainter,QColor,QFont,QPen
from PySide6.QtWidgets import QWidget,QToolTip
from .design_system import colors
from .theme import blend
from .locale import count_text,date_display

MONTHS=('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez')


class ActivityHeatmap(QWidget):
    def __init__(self,values,theme,parent=None):
        super().__init__(parent);self.theme=theme;self.year=None;self.cells=[];self.setMinimumHeight(166);self.setMouseTracking(True);self.set_values(values)
    def sizeHint(self):return QSize(740,166)
    def cell_size(self,columns):return max(3,min(20,(self.width()-34)//columns-3))
    def resizeEvent(self,event):
        first,last=self.interval();start=first-timedelta(days=first.weekday());columns=(last-start).days//7+1
        height=28+7*(self.cell_size(columns)+3)+42
        if self.height()!=height:self.setFixedHeight(height)
        super().resizeEvent(event)
    def set_values(self,values):
        self.values=values;self.setAccessibleName('Horas de jogo por dia')
        self.setAccessibleDescription('; '.join(date_display(day)+': '+f'{seconds/3600:.1f} h'.replace('.',',') for day,seconds in values.items()) or 'Nenhuma sessão registrada');self.update()
    def set_year(self,year):self.year=year;self.update()
    def interval(self):
        today=datetime.now(timezone.utc).date()
        if self.year is None:return today-timedelta(days=364),today
        return date(self.year,1,1),min(today,date(self.year,12,31))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors();font=QFont('Segoe UI');font.setPixelSize(11);p.setFont(font)
        first,last=self.interval();start=first-timedelta(days=first.weekday());columns=(last-start).days//7+1
        gap=3;cell=self.cell_size(columns);stride=cell+gap;left=32;top=28
        shades=[blend(c['panel'],c['text'],.055),blend(c['panel'],c['accent'],.24),blend(c['panel'],c['accent'],.46),blend(c['panel'],c['accent'],.72),c['accent']]
        self.cells=[];months=set()
        for column in range(columns):
            monday=start+timedelta(weeks=column)
            month=(monday.year,monday.month)
            if month not in months:
                months.add(month);p.setPen(QColor(c['muted']));p.drawText(QRectF(left+column*stride,4,36,18),Qt.AlignLeft,MONTHS[monday.month-1])
            for weekday in range(7):
                day=monday+timedelta(days=weekday)
                if not first<=day<=last:continue
                seconds=self.values.get(day.isoformat(),0)
                level=0 if seconds<=0 else 1 if seconds<1800 else 2 if seconds<3600 else 3 if seconds<10800 else 4
                rect=QRectF(left+column*stride,top+weekday*stride,cell,cell)
                p.setPen(QPen(QColor(c['border']),.4));p.setBrush(QColor(shades[level]));p.drawRoundedRect(rect,2,2);self.cells.append((rect,day,seconds))
        p.setPen(QColor(c['muted']))
        for weekday,label in ((0,'Seg'),(2,'Qua'),(4,'Sex')):p.drawText(QRectF(0,top+weekday*stride-1,26,cell+4),Qt.AlignRight|Qt.AlignVCenter,label)
        bottom=top+7*stride+14;total=sum(seconds for day,seconds in self.values.items() if first.isoformat()<=day<=last.isoformat());days=sum(seconds>0 for day,seconds in self.values.items() if first.isoformat()<=day<=last.isoformat())
        summary=f'{total/3600:.1f} h em '.replace('.',',')+count_text(days,'dia de jogo','dias de jogo') if total else 'Nenhuma sessão neste período'
        p.drawText(QRectF(left,bottom,max(1,self.width()-200),20),Qt.AlignVCenter,summary)
        x=self.width()-164;p.drawText(QRectF(x-39,bottom,38,20),Qt.AlignVCenter,'Menos')
        for index,color in enumerate(shades):p.setPen(Qt.NoPen);p.setBrush(QColor(color));p.drawRoundedRect(QRectF(x+index*14,bottom+4,10,10),2,2)
        p.setPen(QColor(c['muted']));p.drawText(QRectF(x+76,bottom,36,20),Qt.AlignVCenter,'Mais');p.end()
    def mouseMoveEvent(self,event):
        for rect,day,seconds in self.cells:
            if rect.contains(event.position()):
                minutes=int(seconds//60);QToolTip.showText(event.globalPosition().toPoint(),f'{day:%d/%m/%Y} · {minutes//60} h {minutes%60:02d} min',self);break
        else:QToolTip.hideText()
        super().mouseMoveEvent(event)

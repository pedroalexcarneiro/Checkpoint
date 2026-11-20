"""Calendário de horas reais, em células diárias como um gráfico de contribuições."""
from datetime import date,datetime,timedelta,timezone
from PySide6.QtCore import Qt,QRectF,QSize,Signal
from PySide6.QtGui import QPainter,QColor,QFont,QPen,QFontMetrics
from PySide6.QtWidgets import QWidget,QToolTip
from .design_system import colors
from .theme import blend
from .locale import count_text,date_display
from .playtime import format_time

MONTHS=('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez')


class ActivityHeatmap(QWidget):
    height_changed=Signal(int)
    def __init__(self,values,theme,parent=None,display_timezone=timezone.utc):
        super().__init__(parent);self.display_timezone=display_timezone;self.theme=theme;self.year=None;self.period_interval=None;self.cells=[];self.setMinimumHeight(166);self.setMouseTracking(True);self.set_values(values)
    def sizeHint(self):return QSize(740,166)
    def cell_size(self,columns):return max(3,min(getattr(self,'cell_limit',20),(self.width()-34)//columns-3))
    def chart_font(self):
        font=QFont('Segoe UI');font.setPixelSize(11);return font
    def summary(self):
        first,last=self.interval()
        values=[seconds for day,seconds in self.values.items() if first.isoformat()<=day<=last.isoformat()]
        total=sum(values);days=sum(seconds>0 for seconds in values)
        return format_time(total)+' em '+count_text(days,'dia de jogo','dias de jogo') if total else 'Nenhuma sessão neste período'
    def footer_layout(self):
        first,last=self.interval();columns=(last-(first-timedelta(days=first.weekday()))).days//7+1
        bottom=28+7*(self.cell_size(columns)+3)+14
        metrics=QFontMetrics(self.chart_font());available=max(1,self.width()-40)
        legend_width=metrics.horizontalAdvance('Menos')+10+66+10+metrics.horizontalAdvance('Mais')
        summary_width=metrics.horizontalAdvance(self.summary())+2
        separate=summary_width+16+legend_width>available
        group_left=max(32,(self.width()-summary_width-16-legend_width)/2)
        summary=QRectF(32 if separate else group_left,bottom,available if separate else summary_width,20)
        legend=QRectF(32 if separate else summary.right()+16,bottom+24 if separate else bottom,legend_width,20)
        return summary,legend
    def heatmap_height(self):
        summary,legend=self.footer_layout();return int(max(summary.bottom(),legend.bottom())+8)
    def resizeEvent(self,event):
        height=self.heatmap_height()
        if self.height()!=height:self.setFixedHeight(height)
        self.height_changed.emit(height)
        super().resizeEvent(event)
    def set_values(self,values):
        self.values=values;self.setAccessibleName('Horas de jogo por dia')
        self.setAccessibleDescription('; '.join(date_display(day)+': '+format_time(seconds) for day,seconds in values.items()) or 'Nenhuma sessão registrada');self.update()
    def set_year(self,year):self.year=year;self.update()
    def set_interval(self,first,last):
        self.period_interval=(first,last);self.updateGeometry();self.update()
    def interval(self):
        if self.period_interval is not None:return self.period_interval
        today=(datetime.now() if self.display_timezone=='local' else datetime.now(self.display_timezone)).date()
        if self.year is None:return today-timedelta(days=364),today
        return date(self.year,1,1),min(today,date(self.year,12,31))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);c=colors();p.setFont(self.chart_font())
        first,last=self.interval();start=first-timedelta(days=first.weekday());columns=(last-start).days//7+1
        gap=3;cell=self.cell_size(columns);stride=cell+gap;left=max(32,(self.width()-columns*stride+32)/2);top=28
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
        for weekday,label in ((0,'Seg'),(2,'Qua'),(4,'Sex')):p.drawText(QRectF(left-32,top+weekday*stride-1,26,cell+4),Qt.AlignRight|Qt.AlignVCenter,label)
        summary,legend=self.footer_layout()
        p.drawText(summary,Qt.AlignVCenter,self.summary())
        metrics=QFontMetrics(self.chart_font());less=metrics.horizontalAdvance('Menos');bottom=legend.top();x=legend.left()+less+10
        p.drawText(QRectF(legend.left(),bottom,less,20),Qt.AlignVCenter,'Menos')
        for index,color in enumerate(shades):p.setPen(Qt.NoPen);p.setBrush(QColor(color));p.drawRoundedRect(QRectF(x+index*14,bottom+4,10,10),2,2)
        p.setPen(QColor(c['muted']));p.drawText(QRectF(x+76,bottom,metrics.horizontalAdvance('Mais'),20),Qt.AlignVCenter,'Mais');p.end()
    def mouseMoveEvent(self,event):
        for rect,day,seconds in self.cells:
            if rect.contains(event.position()):
                minutes=int(seconds//60);QToolTip.showText(event.globalPosition().toPoint(),f'{day:%d/%m/%Y} · '+format_time(seconds),self);break
        else:QToolTip.hideText()
        super().mouseMoveEvent(event)

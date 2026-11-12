"""Painel de estatísticas com números e gráficos derivados da biblioteca real."""
from PySide6.QtCore import Qt,QRectF,QPointF
from PySide6.QtGui import QPainter,QPen,QColor,QFont
from PySide6.QtWidgets import QWidget,QScrollArea,QVBoxLayout,QHBoxLayout,QGridLayout,QComboBox
from .ui_components import text,card,action
from .theme import blend


class TimeChart(QWidget):
    def __init__(self,values,theme,parent=None):
        super().__init__(parent);self.values=values;self.theme=theme;self.setMinimumHeight(204)
        self.setAccessibleName('Tempo registrado por período')
        self.setAccessibleDescription('; '.join(f'{key}: {value/3600:.1f} horas' for key,value in values.items()) or 'Nenhuma sessão registrada')
    def set_values(self,values):self.values=values;self.update()
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);colors=self.theme.colors
        font=QFont('Segoe UI');font.setPixelSize(12);p.setFont(font)
        if not self.values:
            p.setPen(QColor(colors['muted']));p.drawText(self.rect(),Qt.AlignCenter,'Seu tempo de jogo aparecerá aqui');p.end();return
        values=list(self.values.items())[-8:];peak=max(max(value for _,value in values),1)
        area=QRectF(16,22,self.width()-32,self.height()-54);width=area.width()/len(values)
        p.setPen(QPen(QColor(colors['border']),1));p.drawLine(area.bottomLeft(),area.bottomRight())
        for index,(date,value) in enumerate(values):
            height=max(2,value/peak*(area.height()-24));bar=QRectF(area.x()+index*width+width*.23,area.bottom()-height,width*.54,height)
            p.setPen(Qt.NoPen);p.setBrush(QColor(colors['accent']));p.drawRoundedRect(bar,4,4)
            p.setPen(QColor(colors['muted']));p.drawText(QRectF(area.x()+index*width,area.bottom()+9,width,24),Qt.AlignCenter,date[5:])
            p.drawText(QRectF(area.x()+index*width,bar.top()-24,width,20),Qt.AlignCenter,f'{value/3600:.1f} h')
        p.end()


class StatusRing(QWidget):
    def __init__(self,statuses,theme,parent=None):
        super().__init__(parent);self.statuses=statuses;self.theme=theme;self.setFixedSize(168,168)
        self.setAccessibleName('Distribuição dos jogos por status');self.setAccessibleDescription('; '.join(f'{name}: {value}' for name,value in statuses.items()))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);colors=self.theme.colors;rect=QRectF(14,14,140,140);total=sum(self.statuses.values())
        p.setPen(QPen(QColor(colors['button']),17));p.drawEllipse(rect)
        start=90*16
        for index,value in enumerate(self.statuses.values()):
            if not value or not total:continue
            span=round(value/total*360*16);color=blend(colors['accent'],colors['panel'],index*.13)
            p.setPen(QPen(QColor(color),17,Qt.SolidLine,Qt.FlatCap));p.drawArc(rect,start,-span);start-=span
        p.setPen(QColor(colors['text']));font=QFont('Segoe UI');font.setPixelSize(28);font.setWeight(QFont.DemiBold);p.setFont(font);p.drawText(self.rect(),Qt.AlignCenter,str(total));p.end()


def metric(title,value,subtitle=''):
    frame,inside=card();inside.addWidget(text(title,'muted'));inside.addWidget(text(value,'metricValue'))
    if subtitle:inside.addWidget(text(subtitle,'caption'))
    return frame


def build_statistics(window):
    outer=window.clear_page(4);scroll=QScrollArea();scroll.setWidgetResizable(True);body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(20)
    stats=window.library.stats();row=QHBoxLayout();row.setSpacing(16)
    for title,value,subtitle in [('Jogos',str(stats['total']),'Na biblioteca'),('Tempo registrado',f"{stats['seconds']/3600:.1f} h",'Sessões locais confirmadas'),('Sessões',str(stats['sessions']),f"Média de {stats['average']/60:.0f} min"),('Concluídos',str(stats['statuses']['Concluído']),'Jogos finalizados')]:row.addWidget(metric(title,value,subtitle))
    layout.addLayout(row)
    charts=QHBoxLayout();charts.setSpacing(20)
    frame,inside=card();heading=QHBoxLayout();heading.addWidget(text('Tempo de jogo','sectionTitle'));heading.addStretch();period=QComboBox();period.addItems(['Semanas','Meses']);heading.addWidget(period);inside.addLayout(heading)
    chart=TimeChart(stats['weekly'],window.theme);period.currentIndexChanged.connect(lambda index:chart.set_values(stats['monthly'] if index else stats['weekly']));inside.addWidget(chart);inside.addWidget(text('Períodos em UTC · horas Steam não são somadas às sessões locais','caption'));charts.addWidget(frame,3)
    frame,inside=card();inside.addWidget(text('Sua coleção','sectionTitle'));distribution=QHBoxLayout();distribution.addWidget(StatusRing(stats['statuses'],window.theme))
    legend=QVBoxLayout()
    for name,value in stats['statuses'].items():
        line=QHBoxLayout();line.addWidget(text(name,'muted'));line.addStretch();line.addWidget(text(str(value)));legend.addLayout(line)
    distribution.addLayout(legend,1);inside.addLayout(distribution);charts.addWidget(frame,2);layout.addLayout(charts)
    bottom=QHBoxLayout();bottom.setSpacing(20)
    frame,inside=card();inside.addWidget(text('Mais jogados','sectionTitle'))
    if not stats['top']:inside.addWidget(text('Registre uma sessão para começar seu histórico.','muted'))
    for game in stats['top'][:5]:
        line=QHBoxLayout();b=action(game['title'],lambda checked=False,identity=game['id']:window.detail(identity));b.setObjectName('quiet');line.addWidget(b,1);line.addWidget(text(f"{game['seconds']/3600:.1f} h",'muted'));inside.addLayout(line)
    inside.addStretch();bottom.addWidget(frame,3)
    frame,inside=card();inside.addWidget(text('Plataformas','sectionTitle'))
    if not stats['platforms']:inside.addWidget(text('Nenhuma plataforma registrada.','muted'))
    for platform,count in sorted(stats['platforms'].items(),key=lambda pair:pair[1],reverse=True)[:6]:
        line=QHBoxLayout();line.addWidget(text(platform or 'Não definida'));line.addStretch();line.addWidget(text(f'{count} jogos','muted'));inside.addLayout(line)
    inside.addStretch();bottom.addWidget(frame,2);layout.addLayout(bottom)
    extra=QWidget();inside=QVBoxLayout(extra)
    for title,values in [('Gêneros',stats['genres']),('Conclusões por mês',stats['completions'])]:
        inside.addWidget(text(title,'cardTitle'))
        if not values:inside.addWidget(text('Sem registros.','muted'))
        for name,value in values.items():inside.addWidget(text(f'{name} · {value}','muted'))
    from .settings_view import disclosure
    disclosure('Mais estatísticas',extra,layout);layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

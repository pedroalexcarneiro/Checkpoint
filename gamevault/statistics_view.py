"""Painel de estatísticas com números e gráficos derivados da biblioteca real."""
from PySide6.QtCore import Qt,QRectF,QPointF
from PySide6.QtGui import QPainter,QPen,QColor,QFont,QPainterPath,QLinearGradient
from PySide6.QtWidgets import QWidget,QScrollArea,QVBoxLayout,QHBoxLayout,QGridLayout,QComboBox,QProgressBar
from .ui_components import text,card,action
from .theme import blend
from .design_system import AdaptiveColumns,colors as current_colors,Badge,CardGrid


from .activity_heatmap import ActivityHeatmap as TimeChart


class StatusRing(QWidget):
    """Distribuição em barras; nome mantido por compatibilidade com ferramentas."""
    def __init__(self,statuses,theme,parent=None):
        super().__init__(parent);self.statuses=statuses;self.theme=theme;self.setMinimumHeight(204)
        self.setAccessibleName('Distribuição dos jogos por status');self.setAccessibleDescription('; '.join(f'{name}: {value}' for name,value in statuses.items()))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);colors=current_colors();font=QFont('Segoe UI');font.setPixelSize(12);p.setFont(font)
        total=sum(self.statuses.values());track=max(1,self.width()-4)
        for index,(name,value) in enumerate(self.statuses.items()):
            y=index*34;p.setPen(QColor(colors['muted']));p.drawText(QRectF(0,y,track-32,19),Qt.AlignLeft|Qt.AlignVCenter,name)
            p.setPen(QColor(colors['text']));p.drawText(QRectF(track-32,y,32,19),Qt.AlignRight|Qt.AlignVCenter,str(value))
            p.setPen(Qt.NoPen);p.setBrush(QColor(colors['button']));p.drawRoundedRect(QRectF(0,y+23,track,4),2,2)
            if value and total:
                p.setBrush(QColor(colors['accent']));p.drawRoundedRect(QRectF(0,y+23,max(4,track*value/total),4),2,2)
        p.end()


def metric(title,value,subtitle=''):
    frame,inside=card();row=QHBoxLayout();row.addWidget(text(title,'muted'),1);row.addWidget(Badge('library' if title=='Jogos' else 'trophy' if title=='Concluídos' else 'clock',32));inside.addLayout(row);inside.addWidget(text(value,'metricValue'))
    if subtitle:inside.addWidget(text(subtitle,'caption'))
    return frame


def build_statistics(window):
    outer=window.clear_page(4);scroll=QScrollArea();scroll.setWidgetResizable(True);body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(20)
    stats=window.library.stats();row=CardGrid(180,max_columns=4);row.setObjectName('statisticsMetrics')
    for title,value,subtitle in [('Jogos',str(stats['total']),'Na biblioteca'),('Tempo registrado',f"{stats['seconds']/3600:.1f} h".replace('.',','),'Sessões locais confirmadas'),('Sessões',str(stats['sessions']),f"Média de {stats['average']/60:.0f} min"),('Concluídos',str(stats['statuses']['Concluído']),'Jogos finalizados')]:row.add_card(metric(title,value,subtitle))
    layout.addWidget(row)
    charts_left=None;charts_right=None
    frame,inside=card();heading=QHBoxLayout();heading.addWidget(text('Seu ritmo de jogo','sectionTitle'));heading.addStretch();period=QComboBox();period.addItem('Últimos 12 meses',None)
    from datetime import datetime,timezone
    years={int(day[:4]) for day in stats['daily']}|{datetime.now(timezone.utc).year}
    for year in sorted(years,reverse=True):period.addItem(str(year),year)
    heading.addWidget(period);inside.addLayout(heading)
    chart=TimeChart(stats['daily'],window.theme);period.currentIndexChanged.connect(lambda index:chart.set_year(period.itemData(index)));inside.addWidget(chart)
    layout.addWidget(frame)
    bottom_left=None;bottom_right=None
    frame,inside=card();inside.addWidget(text('Mais jogados','sectionTitle'))
    if not stats['top']:inside.addWidget(text('Registre uma sessão para começar seu histórico.','muted'))
    for game in stats['top'][:5]:
        line=QHBoxLayout();b=action(game['title'],lambda checked=False,identity=game['id']:window.detail(identity));b.setObjectName('quiet');line.addWidget(b,1);line.addWidget(text(f"{game['seconds']/3600:.1f} h".replace('.',','),'muted'));inside.addLayout(line)
    inside.addStretch();bottom_left=frame
    frame,inside=card();inside.addWidget(text('Sua coleção','sectionTitle'));inside.addWidget(StatusRing(stats['statuses'],window.theme));inside.addStretch();layout.addWidget(AdaptiveColumns(frame,bottom_left,(3,2),breakpoint=640))
    frame,inside=card();inside.addWidget(text('Plataformas','sectionTitle'))
    if not stats['platforms']:inside.addWidget(text('Nenhuma plataforma registrada.','muted'))
    for platform,count in sorted(stats['platforms'].items(),key=lambda pair:pair[1],reverse=True)[:6]:
        line=QHBoxLayout();line.addWidget(text(platform or 'Não definida'));line.addStretch();line.addWidget(text(f'{count} jogos','muted'));inside.addLayout(line)
        bar=QProgressBar();bar.setRange(0,max(stats['total'],1));bar.setValue(count);bar.setTextVisible(False);bar.setFixedHeight(4);inside.addWidget(bar)
    inside.addStretch();layout.addWidget(frame)
    extra=QWidget();inside=QVBoxLayout(extra)
    for title,values in [('Gêneros',stats['genres']),('Conclusões por mês',stats['completions'])]:
        inside.addWidget(text(title,'cardTitle'))
        if not values:inside.addWidget(text('Sem registros.','muted'))
        for name,value in values.items():
            if title=='Conclusões por mês' and len(name)==7:name=name[5:7]+'/'+name[:4]
            inside.addWidget(text(f'{name} · {value}','muted'))
    from .settings_view import disclosure
    disclosure('Mais estatísticas',extra,layout);layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

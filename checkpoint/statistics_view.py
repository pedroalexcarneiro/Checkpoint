from .smooth_scroll import SmoothScrollArea
from .locale import count_text
"""Painel de estatísticas com números e gráficos derivados da biblioteca real."""
from PySide6.QtCore import Qt,QRectF,QPointF
from PySide6.QtGui import QPainter,QPen,QColor,QFont,QPainterPath,QLinearGradient
from PySide6.QtWidgets import QWidget,QScrollArea,QVBoxLayout,QHBoxLayout,QGridLayout,QComboBox,QProgressBar,QPushButton,QLabel
from .ui_components import text,card,action
from .theme import blend
from .design_system import AdaptiveColumns,colors as current_colors,Badge,CardGrid


from .activity_heatmap import ActivityHeatmap as TimeChart


class HeatmapViewport(SmoothScrollArea):
    def __init__(self,chart):
        super().__init__();self.setObjectName('heatmapViewport');self.setFrameShape(self.Shape.NoFrame)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff);self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded);self.setWidgetResizable(True);self.setWidget(chart)
        chart.height_changed.connect(self.fit_height);self.horizontalScrollBar().rangeChanged.connect(self.fit_height)
        self.setFixedHeight(chart.sizeHint().height())
    def fit_height(self,*args):
        extra=self.horizontalScrollBar().sizeHint().height() if self.horizontalScrollBar().maximum()>0 else 0
        height=self.widget().height()+extra+2*self.frameWidth()
        if self.height()!=height:self.setFixedHeight(height)


class StatusRing(QWidget):
    """Distribuição em barras; nome mantido por compatibilidade com ferramentas."""
    def __init__(self,statuses,theme,parent=None):
        super().__init__(parent);self.statuses=dict(statuses);self.statuses['Não iniciado']=self.statuses.get('Não iniciado',0)+self.statuses.pop('Backlog',0);self.theme=theme;self.setMinimumHeight(204)
        self.setAccessibleName('Distribuição dos jogos por status');self.setAccessibleDescription('; '.join(f'{name}: {value}' for name,value in self.statuses.items()))
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


class GameNameButton(QPushButton):
    def __init__(self,title,callback):
        super().__init__();self.full_title=title;self.setObjectName('quiet');self.setToolTip(title);self.setAccessibleName(title);self.setMinimumWidth(0)
        from PySide6.QtWidgets import QSizePolicy
        self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed);self.clicked.connect(callback)
    def resizeEvent(self,event):
        super().resizeEvent(event);self.setText(self.fontMetrics().elidedText(self.full_title,Qt.ElideRight,max(0,self.width()-8)))


def metric(title,value,subtitle=''):
    frame,inside=card();frame.setMinimumHeight(158)
    from PySide6.QtWidgets import QSizePolicy
    frame.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    heading=text(title,'muted');heading.setMinimumHeight(36)
    row=QHBoxLayout();row.addWidget(heading,1);row.addWidget(Badge('library' if 'coleção' in title else 'clock',32));inside.addLayout(row)
    value_label=text(value,'metricValue');value_label.setMinimumHeight(40);value_label.setToolTip(value);inside.addWidget(value_label)
    caption=text(subtitle,'caption');caption.setMinimumHeight(18);inside.addWidget(caption)
    return frame


def render_statistics(window,layout,selected):
    from .playtime import collection_times,format_time
    from .statistics_periods import period_stats
    stats=window.library.stats(display_timezone='local');temporal=period_stats(window.library,selected)
    times=collection_times(window.library)
    row=CardGrid(220,max_columns=3);row.setObjectName('statisticsMetrics')
    for title,value in [('Tempo no período',format_time(temporal['seconds'])),('Sessões no período',str(temporal['sessions'])),('Média por sessão',format_time(temporal['average']))]:row.add_card(metric(title,value))
    layout.addWidget(row)
    frame,inside=card();inside.addWidget(text('Seu ritmo de jogo','sectionTitle'))
    chart=TimeChart(temporal['daily'],window.theme,display_timezone='local');chart.set_interval(*temporal['dates'])
    from datetime import timedelta
    first,last=temporal['dates'];columns=(last-(first-timedelta(days=first.weekday()))).days//7+1
    chart.setMinimumWidth(36+columns*6)
    scroller=HeatmapViewport(chart);inside.addWidget(scroller)
    layout.addWidget(frame)
    frame,inside=card();inside.addWidget(text('Mais jogados no período','sectionTitle'))
    if not temporal['top']:inside.addWidget(text('Sem sessões neste período.','muted'))
    for game in temporal['top'][:5]:
        game_row=QWidget();game_row.setObjectName('statisticsGameRow');line=QHBoxLayout(game_row);line.setContentsMargins(0,4,0,4);line.setSpacing(16)
        logo=QLabel();logo.setObjectName('statisticsGameLogo');logo.setFixedSize(140,48);logo.setAlignment(Qt.AlignCenter)
        stored=window.library.get(game['id'])
        from PySide6.QtGui import QPixmap
        from .list_art import list_icon
        if not QPixmap(stored.get('logo') or '').isNull():logo.setPixmap(list_icon(stored,window.theme.colors['text']).pixmap(140,48))
        elif not QPixmap(stored.get('cover') or '').isNull():logo.setPixmap(QPixmap(stored['cover']).scaled(132,40,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            from .ui_components import nav_icon
            logo.setPixmap(nav_icon('library',window.theme.colors['muted'],32).pixmap(32,32))
        line.addWidget(logo)
        b=GameNameButton(game['title'],lambda checked=False,identity=game['id']:window.detail(identity));b.setObjectName('statisticsGameName');line.addWidget(b,1)
        value=text(format_time(game['seconds']),'muted');value.setObjectName('statisticsGameTime');value.setStyleSheet('font-size: 16px; font-weight: 600; color: '+window.theme.colors['text']+';');value.setWordWrap(False);value.setAlignment(Qt.AlignRight|Qt.AlignVCenter);line.addWidget(value);inside.addWidget(game_row)
    inside.addStretch();layout.addWidget(frame)
    layout.addWidget(text('Coleção atual','sectionTitle'))
    row=CardGrid(220,max_columns=3);row.setObjectName('collectionMetrics')
    for title,value in [('Jogos da coleção',str(stats['total'])),('Concluídos da coleção',str(stats['statuses']['Concluído'])),('Tempo total · app + Steam',format_time(sum(times.values())))]:row.add_card(metric(title,value))
    layout.addWidget(row)
    frame,inside=card();inside.addWidget(text('Status da coleção','sectionTitle'));inside.addWidget(StatusRing(stats['statuses'],window.theme));layout.addWidget(frame)
    frame,inside=card();inside.addWidget(text('Plataformas da coleção','sectionTitle'))
    if not stats['platforms']:inside.addWidget(text('Nenhuma plataforma registrada.','muted'))
    for platform,count in sorted(stats['platforms'].items(),key=lambda pair:pair[1],reverse=True)[:6]:
        line=QHBoxLayout();line.addWidget(text(platform or 'Não definida'));line.addStretch();line.addWidget(text(count_text(count,'jogo'),'muted'));inside.addLayout(line)
        bar=QProgressBar();bar.setRange(0,max(stats['total'],1));bar.setValue(count);bar.setTextVisible(False);bar.setFixedHeight(4);inside.addWidget(bar)
    layout.addWidget(frame)
    extra=QWidget();inside=QVBoxLayout(extra)
    for title,values in [('Gêneros da coleção',stats['genres']),('Conclusões no período',temporal['completions'])]:
        inside.addWidget(text(title,'cardTitle'))
        if not values:inside.addWidget(text('Sem registros neste período.' if title=='Conclusões no período' else 'Sem gêneros registrados.','muted'))
        for name,value in values.items():
            if title=='Conclusões no período' and len(name)==7:name=name[5:7]+'/'+name[:4]
            inside.addWidget(text(f'{name} · {value}','muted'))
    layout.addWidget(extra)
    layout.addStretch()


def build_statistics(window):
    from .statistics_periods import PERIODS
    outer=window.clear_page(4);scroll=SmoothScrollArea();scroll.setWidgetResizable(True);body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(20)
    header=QHBoxLayout();header.addWidget(text('Período','cardTitle'));header.addStretch();period=QComboBox();period.setObjectName('statisticsPeriod')
    for name,key in PERIODS:period.addItem(name,key)
    selected=window.library.setting('statistics.period','12m')
    period.setCurrentIndex(max(0,period.findData(selected)));header.addWidget(period);layout.addLayout(header)
    content=QWidget();inside=QVBoxLayout(content);inside.setContentsMargins(0,0,0,0);inside.setSpacing(20);layout.addWidget(content)
    def render():
        while inside.count():
            item=inside.takeAt(0)
            if item.widget():
                widget=item.widget();widget.hide();widget.setParent(None);widget.deleteLater()
        key=period.currentData();window.library.set_setting('statistics.period',key);render_statistics(window,inside,key)
    period.currentIndexChanged.connect(render);render();scroll.setWidget(body);outer.addWidget(scroll)

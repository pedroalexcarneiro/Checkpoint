"""Cards e navegação do Início, com ações separadas e conteúdo local."""
from PySide6.QtCore import Qt,QRectF,QSize
from PySide6.QtGui import QPainter,QPainterPath,QColor,QPixmap
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QSizePolicy,QDialog,QScrollArea,QBoxLayout
from .design_system import CardSurface,IconButton,SectionHeader,ArtworkButton,colors
from .ui_components import Hero,text,action,ElidedAction
from .playtime import format_time
from .library import display_status
from .locale import datetime_display


class SingleLineInfo(QLabel):
    def __init__(self,value,kind='caption',tooltip=None):
        super().__init__();self.full_text=value;self.setObjectName(kind);self.setWordWrap(False)
        self.setMinimumWidth(0);self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed)
        self.setFixedHeight(20);self.setToolTip(tooltip or value);self.setAccessibleName(tooltip or value)
    def resizeEvent(self,event):
        super().resizeEvent(event);self.setText(self.fontMetrics().elidedText(self.full_text,Qt.ElideRight,self.width()))


def last_played_text(value):
    from datetime import datetime,timedelta
    from .statistics_periods import instant
    stamp=instant(value).astimezone();today=datetime.now().astimezone().date()
    day='hoje' if stamp.date()==today else 'ontem' if stamp.date()==today-timedelta(days=1) else stamp.strftime('%d/%m')
    return 'Última vez: '+day+', '+stamp.strftime('%H:%M')


class RecentArtwork(QPushButton):
    """Capa inteira; banner é alternativa somente quando não há capa."""
    def __init__(self,game,window):
        super().__init__();self.game=game;self.host_window=window;self.art_kind='cover'
        self.pixmap=QPixmap(game.get('cover') or '')
        if self.pixmap.isNull():self.art_kind='banner';self.pixmap=QPixmap(game.get('banner') or '')
        self.logo=QPixmap(game.get('logo') or '')
        self.setObjectName('recentGameArtwork');self.setFocusPolicy(Qt.StrongFocus);self.setCursor(Qt.PointingHandCursor)
        self.setAccessibleName('Abrir ficha de '+game['title']);self.setMinimumWidth(0)
        self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed)
        self.clicked.connect(lambda:window.detail(game['id']))
    def image_target(self):
        if self.pixmap.isNull():return QRectF()
        from PySide6.QtCore import QSizeF
        size=QSizeF(self.pixmap.size()).scaled(QSizeF(self.size()),Qt.KeepAspectRatio)
        return QRectF((self.width()-size.width())/2,(self.height()-size.height())/2,size.width(),size.height())
    def resizeEvent(self,event):
        super().resizeEvent(event)
        height=round(self.width()*self.pixmap.height()/self.pixmap.width()) if not self.pixmap.isNull() else 180
        if self.height()!=height:self.setFixedHeight(max(1,height))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);p.setRenderHint(QPainter.SmoothPixmapTransform)
        p.fillRect(self.rect(),QColor(colors()['input']))
        if not self.pixmap.isNull():p.drawPixmap(self.image_target(),self.pixmap,QRectF(self.pixmap.rect()))
        elif self.logo.isNull():p.setPen(QColor(colors()['text']));p.drawText(self.rect(),Qt.AlignCenter|Qt.TextWordWrap,self.game['title'])
        if not self.logo.isNull() and (self.art_kind!='cover' or self.pixmap.isNull()):
            logo=self.logo.scaled(max(1,self.width()-24),48,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(12,12,logo)
        p.end()


class RecentGameCard(CardSurface):
    def __init__(self,window,game):
        super().__init__();self.game_id=game['id'];self.setObjectName('recentGameCard');self.setMinimumWidth(0)
        self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Preferred)
        inside=QVBoxLayout(self);inside.setContentsMargins(12,12,12,12);inside.setSpacing(10)
        inside.addWidget(RecentArtwork(game,window))
        row=QHBoxLayout();row.setSpacing(8)
        def continue_game():
            if game.get('executable') or window.library.sql.execute('SELECT 1 FROM game_files WHERE game_id=?',(game['id'],)).fetchone():window.start_game(game)
            else:window.edit_game(game['id'])
        play=action('Continuar jogando',continue_game,True);play.setProperty('homeContinue',True);play.setMinimumWidth(0);play.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        row.addWidget(play,1);inside.addLayout(row)
        title_row=QHBoxLayout();title_row.setSpacing(4)
        title=ElidedAction(game['title'],lambda:window.detail(game['id']));title.setObjectName('activityLink');title_row.addWidget(title,1)
        title_row.addWidget(IconButton('files','Abrir ficha de '+game['title'],lambda:window.detail(game['id'])));inside.addLayout(title_row)
        inside.addWidget(SingleLineInfo(display_status(game.get('status')),'muted'))
        inside.addWidget(SingleLineInfo(last_played_text(game['last_played']),tooltip='Última vez: '+datetime_display(game['last_played'])))
        inside.addWidget(SingleLineInfo('Tempo total: '+format_time(game['seconds'])))


class OfferBanner(RecentArtwork):
    def __init__(self,game,window):
        super().__init__({**game,'cover':'','logo':''},window)
        self.setObjectName('homeOfferBanner')


class GameStrip(QWidget):
    """Três cards por página, com navegação horizontal sem cortar as capas."""
    def __init__(self,window,games,maximum=3):
        super().__init__();self.setMinimumWidth(0);self.setObjectName('recentGames')
        self.host_window=window;self.games=games;self.maximum=maximum;self.offset=0;self.setFocusPolicy(Qt.StrongFocus)
        layout=QVBoxLayout(self);layout.setContentsMargins(0,0,0,0);layout.setSpacing(8)
        controls=QHBoxLayout();controls.addStretch()
        self.previous=IconButton('back','Jogos anteriores',lambda:self.move_by(-1));controls.addWidget(self.previous)
        self.next=IconButton('chevron-right','Próximos jogos',lambda:self.move_by(1));controls.addWidget(self.next);layout.addLayout(controls)
        self.body=QWidget();self.row=QHBoxLayout(self.body);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(12);layout.addWidget(self.body)
        self.render()
    def render(self):
        while self.row.count():
            item=self.row.takeAt(0)
            if item.widget():item.widget().hide();item.widget().deleteLater()
        self.tiles=[RecentGameCard(self.host_window,game) for game in self.games[self.offset:self.offset+self.maximum]]
        for tile in self.tiles:self.row.addWidget(tile,1)
        self.previous.setEnabled(self.offset>0);self.next.setEnabled(self.offset+self.maximum<len(self.games))
    def move_by(self,step):
        self.offset=max(0,min(max(0,len(self.games)-self.maximum),self.offset+step));self.render()
    def keyPressEvent(self,event):
        if event.key() in (Qt.Key_Left,Qt.Key_Right):self.move_by(-1 if event.key()==Qt.Key_Left else 1);event.accept()
        else:super().keyPressEvent(event)


def open_memory(window,record):
    if record['kind']!='diary':window.show_media(record);return
    from PySide6.QtWidgets import QTextEdit
    dialog=QDialog(window);dialog.setWindowTitle('Memória de '+record['title']);dialog.resize(520,400)
    layout=QVBoxLayout(dialog);layout.addWidget(text(record['title'],'sectionTitle'))
    content=QTextEdit();content.setReadOnly(True);content.setPlainText(record['text']);layout.addWidget(content)
    layout.addWidget(text(datetime_display(record['created_at']),'caption'))
    def open_game():dialog.accept();window.detail(record['game_id']);window.detail_tabs.setCurrentIndex(2)
    layout.addWidget(action('Abrir jogo',open_game));layout.addWidget(action('Fechar',dialog.reject));dialog.exec()


class MemoryCarousel(CardSurface):
    def __init__(self,window,records):
        super().__init__();self.host_window=window;self.records=records;self.offset=0;self.visible_count=3;self.setObjectName('homeMemories')
        self.setFocusPolicy(Qt.StrongFocus);self.setMinimumWidth(0)
        layout=QVBoxLayout(self);layout.setContentsMargins(16,16,16,16);layout.setSpacing(14)
        head=QHBoxLayout();head.addWidget(text('Memórias recentes','sectionTitle'),1)
        head.addWidget(action('Ver todas',lambda:window.navigate(3)))
        self.previous=IconButton('back','Memórias anteriores',lambda:self.move_by(-1));head.addWidget(self.previous)
        self.next=IconButton('chevron-right','Próximas memórias',lambda:self.move_by(1));head.addWidget(self.next);layout.addLayout(head)
        self.body=QWidget();self.row=QHBoxLayout(self.body);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(14);layout.addWidget(self.body)
        self.render()
    def render(self):
        while self.row.count():
            item=self.row.takeAt(0)
            if item.widget():item.widget().hide();item.widget().deleteLater()
        if not self.records:
            self.row.addWidget(action('Adicionar memória',self.host_window.first_memory,True))
        for record in self.records[self.offset:self.offset+self.visible_count]:
            frame=CardSurface();frame.setObjectName('homeMemoryCard');frame.setMinimumWidth(0);frame.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Preferred)
            inside=QVBoxLayout(frame);inside.setContentsMargins(12,12,12,12);inside.setSpacing(8)
            callback=lambda checked=False,r=record:open_memory(self.host_window,r)
            if record['kind']=='diary':
                preview=QPushButton();preview.setObjectName('memoryTextPreview');preview.setFixedHeight(114)
                preview.setAccessibleName(record['text']);preview.setToolTip(record['text']);preview.clicked.connect(callback)
                words=QVBoxLayout(preview);words.setContentsMargins(10,10,10,10)
                label=text(record['text'],'bodyText');label.setAttribute(Qt.WA_TransparentForMouseEvents);label.setMaximumHeight(90);words.addWidget(label)
            else:preview=ArtworkButton(record['path'],record.get('caption') or 'Abrir captura',callback,height=114)
            inside.addWidget(preview)
            title=ElidedAction(record['title'],callback);title.setObjectName('activityLink');inside.addWidget(title)
            inside.addWidget(text('Diário' if record['kind']=='diary' else 'Vídeo' if record['kind']=='video' else 'Captura','caption'))
            inside.addWidget(text(datetime_display(record['created_at']),'caption'));self.row.addWidget(frame,1)
        self.previous.setEnabled(self.offset>0);self.next.setEnabled(self.offset+self.visible_count<len(self.records))
    def move_by(self,step):
        self.offset=max(0,min(max(0,len(self.records)-self.visible_count),self.offset+step));self.render()
    def keyPressEvent(self,event):
        if event.key() in (Qt.Key_Left,Qt.Key_Right):self.move_by(-1 if event.key()==Qt.Key_Left else 1);event.accept()
        else:super().keyPressEvent(event)
    def resizeEvent(self,event):
        count=3 if self.width()>=740 else 2 if self.width()>=480 else 1
        if count!=self.visible_count:
            self.visible_count=count;self.offset=min(self.offset,max(0,len(self.records)-count));self.render()
        super().resizeEvent(event)


def show_execution_history(window):
    from .home_data import execution_history
    dialog=QDialog(window);dialog.setWindowTitle('Histórico de execuções');dialog.resize(650,500)
    layout=QVBoxLayout(dialog);scroll=QScrollArea();scroll.setWidgetResizable(True);scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    body=QWidget();inside=QVBoxLayout(body)
    for record in execution_history(window.library):
        frame=CardSurface();row=QHBoxLayout(frame)
        def open_game(checked=False,identity=record['game_id']):dialog.accept();window.detail(identity)
        row.addWidget(ElidedAction(record['game']['title'],open_game),1)
        row.addWidget(text(datetime_display(record['started_at']),'caption'))
        row.addWidget(text({'active':'Em andamento','finished':'Concluída','interrupted':'Revisar sessão'}[record['state']],'caption'))
        inside.addWidget(frame)
    if not inside.count():inside.addWidget(text('Nenhuma execução registrada.','muted'))
    inside.addStretch();scroll.setWidget(body);layout.addWidget(scroll)
    layout.addWidget(action('Fechar',dialog.reject),0,Qt.AlignRight);dialog.exec()

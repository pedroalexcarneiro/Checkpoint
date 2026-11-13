"""Composição do início: hero, continuidade e atividade lado a lado."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea,QWidget,QVBoxLayout,QHBoxLayout,QSizePolicy,QLabel
from .ui_components import Hero,GameTile,text,action,card,nav_icon,relative_date,TwoLineLabel


def activity(window,layout):
    layout.addWidget(text('Sua atividade','sectionTitle'))
    events=[]
    queries=[("SELECT g.id,g.title,d.created_at AS time,d.text AS message FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') ORDER BY d.created_at DESC LIMIT 3",'Memória'),
             ("SELECT g.id,g.title,a.unlocked_at AS time,a.title AS message FROM achievements a JOIN games g ON g.id=a.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') ORDER BY a.unlocked_at DESC LIMIT 3",'Marco'),
             ("SELECT g.id,g.title,s.started_at AS time,s.duration_seconds AS message FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') AND s.state='finished' ORDER BY s.started_at DESC LIMIT 3",'Sessão')]
    for query,kind in queries:
        events.extend((dict(row),kind) for row in window.library.sql.execute(query) if window.library.is_owned(row['id']))
    events.sort(key=lambda item:item[0]['time'] or '',reverse=True)
    if not events:
        frame,inside=card();inside.addWidget(text('Nenhuma atividade recente.','muted'));layout.addWidget(frame)
    for event,kind in events[:2]:
        frame,inside=card();frame.setObjectName('activityCard');inside.setContentsMargins(12,10,12,10)
        contents=QHBoxLayout();contents.setSpacing(14)
        badge=QLabel();badge.setFixedSize(36,36);badge.setObjectName('activityBadge')
        badge.setPixmap(nav_icon('memories' if kind=='Memória' else 'trophy' if kind=='Marco' else 'clock',window.theme.colors['accent']).pixmap(22,22));badge.setAlignment(Qt.AlignCenter);contents.addWidget(badge,0,Qt.AlignTop)
        words=QVBoxLayout();words.setSpacing(4)
        top=QHBoxLayout();top.addWidget(text({'Memória':'Diário de jogo','Marco':'Conquista desbloqueada','Sessão':'Sessão concluída'}[kind],'activityKind'));top.addStretch();top.addWidget(text(relative_date(event['time']),'caption'));words.addLayout(top)
        link=action(event['title'],lambda checked=False,identity=event['id']:window.detail(identity));link.setObjectName('activityLink');link.setToolTip(event['title']);words.addWidget(link)
        message=f"{int(event['message'])//60} min registrados" if kind=='Sessão' else str(event['message'])
        words.addWidget(TwoLineLabel(message));contents.addLayout(words,1);inside.addLayout(contents)
        layout.addWidget(frame)
    layout.addStretch()


class GameStrip(QScrollArea):
    """Quatro capas se ajustam à coluna sem esconder a atividade pessoal."""
    def __init__(self,window,games,maximum):
        super().__init__();self.setWidgetResizable(True);self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tiles=QWidget();self.row=QHBoxLayout(tiles);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(12);self.row.setAlignment(Qt.AlignTop)
        self.tiles=[GameTile(game,window.detail,width=100) for game in games[:maximum]]
        for tile in self.tiles:self.row.addWidget(tile)
        self.row.addStretch();self.setWidget(tiles);self.setFixedHeight(190)
    def resizeEvent(self,event):
        super().resizeEvent(event)
        width=max(64,min(150,(self.viewport().width()-max(0,len(self.tiles)-1)*12)//max(1,len(self.tiles))))
        for tile in self.tiles:tile.set_tile_width(width)
        self.setFixedHeight(max((tile.height() for tile in self.tiles),default=0)+4)


def game_strip(window,layout,title,games,maximum=4):
    layout.addWidget(text(title,'sectionTitle'))
    layout.addWidget(GameStrip(window,games,maximum))


def build_home(window):
    outer=window.clear_page(0);scroll=QScrollArea();scroll.setWidgetResizable(True)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(16)
    games=window.library.owned_games(sort='recent')
    if not games:
        from .design_system import empty_state
        layout.addWidget(empty_state('library','Sua biblioteca começa aqui','Pesquise um jogo pelo nome para adicionar ficha e imagens à sua coleção.',window.add_game,'Adicionar jogo'))
        activity(window,layout)
    else:
        playing=[game for game in games if game['status']=='Jogando']
        featured=(playing or [game for game in games if game['favorite']] or games)[0]
        hero=Hero(featured,window.theme);hero.setMinimumHeight(0)
        buttons=QHBoxLayout()
        if featured['executable']:play=action('▶ Continuar jogando' if featured['status']=='Jogando' else '▶ Jogar',lambda:window.start_game(featured),True)
        else:play=action('Ver jogo',lambda:window.detail(featured['id']),True)
        buttons.addWidget(play);buttons.addStretch();hero.content.addLayout(buttons);layout.addWidget(hero)
        continuing=[dict(row) for row in window.library.sql.execute("SELECT g.*,MAX(s.started_at) AS last_played,SUM(CASE WHEN s.state='finished' THEN s.duration_seconds ELSE 0 END) AS seconds FROM games g JOIN play_sessions s ON s.game_id=g.id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') GROUP BY g.id ORDER BY last_played DESC LIMIT 6")] or playing
        continuing=[game for game in continuing if window.library.is_owned(game['id'])]
        from .design_system import AdaptiveColumns
        left=QWidget();left.setObjectName('homeContinuation');left.setMinimumWidth(280);left_layout=QVBoxLayout(left);left_layout.setContentsMargins(0,0,0,0);left_layout.setSpacing(14)
        game_strip(window,left_layout,'Continuar jogando' if continuing else 'Sua biblioteca',continuing or games)
        left_layout.addStretch()
        left.setMaximumWidth(720)
        right=QWidget();right.setObjectName('homeActivity');right.setMinimumWidth(240);right_layout=QVBoxLayout(right);right_layout.setContentsMargins(0,0,0,0);right_layout.setSpacing(12);activity(window,right_layout)
        layout.addWidget(AdaptiveColumns(left,right,(3,2),breakpoint=640))
    interrupted=window.library.sql.execute("SELECT count(*) FROM play_sessions WHERE state='interrupted'").fetchone()[0]
    if interrupted:layout.addWidget(action(f'{interrupted} sessões para revisar',window.recover_sessions))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

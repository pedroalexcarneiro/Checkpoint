from .visual_tokens import SPACE
from .design_system import SectionHeader,ActionCard,CardGrid
from .locale import count_text
"""Composição do início: hero, continuidade e atividade lado a lado."""
from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import QScrollArea,QWidget,QVBoxLayout,QHBoxLayout,QSizePolicy,QLabel,QLayout
from .ui_components import Hero,GameTile,text,action,card,nav_icon,relative_date,TwoLineLabel


def activity(window,layout):
    layout.addWidget(SectionHeader('Sua atividade','Conquistas, sessões e memórias recentes.'))
    events=[]
    queries=[("SELECT g.id,g.title,d.created_at AS time,d.text AS message FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') ORDER BY d.created_at DESC LIMIT 3",'Memória'),
             ("SELECT g.id,g.title,a.unlocked_at AS time,a.title AS message FROM achievements a JOIN games g ON g.id=a.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') ORDER BY a.unlocked_at DESC LIMIT 3",'Marco'),
             ("SELECT g.id,g.title,s.started_at AS time,s.duration_seconds AS message FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM wishlist w WHERE w.game_id=g.id) AND NOT EXISTS (SELECT 1 FROM settings t WHERE t.key='collection.unowned.'||g.id AND t.value='true') AND s.state='finished' ORDER BY s.started_at DESC LIMIT 3",'Sessão')]
    for query,kind in queries:
        events.extend((dict(row),kind) for row in window.library.sql.execute(query) if window.library.is_owned(row['id']))
    events.sort(key=lambda item:item[0]['time'] or '',reverse=True)
    if not events:
        layout.addWidget(ActionCard('clock','Sua história começa ao jogar','Suas sessões, conquistas e anotações aparecerão aqui.',lambda:window.navigate(1),'Abrir biblioteca'))
    selected=[]
    for preferred in ('Marco','Memória'):
        match=next((item for item in events if item[1]==preferred),None)
        if match:selected.append(match)
    for item in events:
        if len(selected)>=2:break
        if item not in selected:selected.append(item)
    for event,kind in selected:
        frame,inside=card();frame.setObjectName('activityCard');inside.setContentsMargins(*([SPACE['md']]*4))
        contents=QHBoxLayout();contents.setSpacing(14)
        badge=QLabel();badge.setFixedSize(36,36);badge.setObjectName('activityBadge')
        badge.setPixmap(nav_icon('memories' if kind=='Memória' else 'trophy' if kind=='Marco' else 'clock',window.theme.colors['accent']).pixmap(22,22));badge.setAlignment(Qt.AlignCenter);contents.addWidget(badge,0,Qt.AlignTop)
        words=QVBoxLayout();words.setSpacing(4)
        top=QHBoxLayout();top.addWidget(text({'Memória':'Diário de jogo','Marco':'Conquista desbloqueada','Sessão':'Sessão concluída'}[kind],'activityKind'));top.addStretch();top.addWidget(text(relative_date(event['time']),'caption'));words.addLayout(top)
        link=action(event['title'],lambda checked=False,identity=event['id']:window.detail(identity));link.setObjectName('activityLink');link.setToolTip(event['title']);link.setMinimumWidth(0);link.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed);words.addWidget(link)
        message=f"{int(event['message'])//60} min registrados" if kind=='Sessão' else str(event['message'])
        words.addWidget(TwoLineLabel(message));contents.addLayout(words,1);inside.addLayout(contents)
        layout.addWidget(frame)
    layout.addStretch()


class GameStrip(QScrollArea):
    """Quatro capas se ajustam à coluna sem esconder a atividade pessoal."""
    def __init__(self,window,games,maximum):
        super().__init__();self.setWidgetResizable(True);self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff);self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tiles=QWidget();self.row=QHBoxLayout(tiles);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(12);self.row.setAlignment(Qt.AlignTop);self.row.setSizeConstraint(QLayout.SetNoConstraint);self.setMinimumWidth(0)
        self.tiles=[GameTile(game,window.detail,width=100) for game in games[:maximum]]
        for tile in self.tiles:self.row.addWidget(tile)
        self.row.addStretch();self.setWidget(tiles);self.setFixedHeight(190)
    def minimumSizeHint(self):return QSize(0,0)
    def resizeEvent(self,event):
        super().resizeEvent(event)
        width=max(1,min(150,(self.viewport().width()-max(0,len(self.tiles)-1)*12)//max(1,len(self.tiles))))
        for tile in self.tiles:tile.set_tile_width(width)
        self.setFixedHeight(max((tile.height() for tile in self.tiles),default=0)+4)


def game_strip(window,layout,title,games,maximum=4):
    layout.addWidget(SectionHeader(title,'Retome de onde você parou.',lambda:window.navigate(1)))
    layout.addWidget(GameStrip(window,games,maximum))


def in_progress(library):
    sessions={row['game_id']:dict(row) for row in library.sql.execute("SELECT game_id,MAX(started_at) AS last_played,SUM(CASE WHEN state='finished' THEN duration_seconds ELSE 0 END) AS seconds FROM play_sessions GROUP BY game_id")}
    games=[{**game,**sessions.get(game['id'],{})} for game in library.owned_games() if game['status'] in ('Jogando','Pausado')]
    return sorted(games,key=lambda game:game.get('last_played') or game.get('updated_at') or game['created_at'],reverse=True)


def build_home(window):
    outer=window.clear_page(0);scroll=QScrollArea();scroll.setWidgetResizable(True);scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(SPACE['lg'])
    games=window.library.owned_games(sort='recent')
    if not games:
        from .design_system import empty_state
        layout.addWidget(empty_state('library','Sua biblioteca começa aqui','Adicione um jogo para reunir capas, progresso e memórias em um só lugar.',window.add_library_game,'Adicionar jogo'))
        activity(window,layout)
    else:
        continuing=in_progress(window.library)
        featured=continuing[0] if continuing else None
        if featured:
            hero=Hero(featured,window.theme);hero.setMinimumHeight(0)
            buttons=QHBoxLayout()
            play=action('Continuar jogando',lambda:window.start_game(featured) if featured['executable'] else window.detail(featured['id']),True)
            play.setObjectName('primary');play.setAccessibleName('Continuar jogando')
            buttons.addWidget(play);buttons.addStretch();hero.content.addLayout(buttons);layout.addWidget(hero)
        else:
            from .design_system import empty_state
            layout.addWidget(empty_state('library','Escolha seu próximo jogo','Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui.',lambda:window.navigate(1),'Abrir biblioteca'))
        from .design_system import AdaptiveColumns
        left=QWidget();left.setObjectName('homeContinuation');left.setMinimumWidth(280);left_layout=QVBoxLayout(left);left_layout.setContentsMargins(0,0,0,0);left_layout.setSpacing(14)
        if continuing:game_strip(window,left_layout,'Continuar jogando',continuing)
        else:
            left_layout.addWidget(SectionHeader('Na sua biblioteca','Jogos prontos para a sua próxima escolha.'))
            previews=CardGrid(150,max_columns=4)
            for game in games[:4]:previews.add_card(GameTile(game,window.detail,width=132))
            left_layout.addWidget(previews)
        left_layout.addStretch()
        left.setMaximumWidth(780)
        right=QWidget();right.setObjectName('homeActivity');right.setMinimumWidth(240);right_layout=QVBoxLayout(right);right_layout.setContentsMargins(0,0,0,0);right_layout.setSpacing(12);activity(window,right_layout)
        layout.addWidget(AdaptiveColumns(left,right,(3,2),breakpoint=640))
    interrupted=window.library.sql.execute("SELECT count(*) FROM play_sessions WHERE state='interrupted'").fetchone()[0]
    if interrupted:layout.addWidget(action(count_text(interrupted,'sessão para revisar','sessões para revisar'),window.recover_sessions))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

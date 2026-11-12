"""Composição do início: hero, continuidade e atividade lado a lado."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea,QWidget,QVBoxLayout,QHBoxLayout,QSizePolicy,QLabel
from .ui_components import Hero,GameTile,text,action,card,nav_icon


def activity(window,layout):
    layout.addWidget(text('Sua atividade','sectionTitle'))
    events=[]
    queries=[("SELECT g.id,g.title,d.created_at AS time,d.text AS message FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL ORDER BY d.created_at DESC LIMIT 3",'Memória'),
             ("SELECT g.id,g.title,a.unlocked_at AS time,a.title AS message FROM achievements a JOIN games g ON g.id=a.game_id WHERE g.deleted_at IS NULL ORDER BY a.unlocked_at DESC LIMIT 3",'Marco'),
             ("SELECT g.id,g.title,s.started_at AS time,s.duration_seconds AS message FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE g.deleted_at IS NULL AND s.state='finished' ORDER BY s.started_at DESC LIMIT 3",'Sessão')]
    for query,kind in queries:
        events.extend((dict(row),kind) for row in window.library.sql.execute(query))
    events.sort(key=lambda item:item[0]['time'] or '',reverse=True)
    if not events:
        frame,inside=card();inside.addWidget(text('Seu histórico começa ao jogar','cardTitle'));inside.addWidget(text('Sessões, conquistas e memórias ficam reunidas aqui.','muted'));layout.addWidget(frame)
    for event,kind in events[:2]:
        frame,inside=card();frame.setObjectName('activityCard')
        contents=QHBoxLayout();contents.setSpacing(14)
        badge=QLabel();badge.setFixedSize(36,36);badge.setObjectName('activityBadge')
        badge.setPixmap(nav_icon('memories' if kind=='Memória' else 'stats',window.theme.colors['accent']).pixmap(22,22));badge.setAlignment(Qt.AlignCenter);contents.addWidget(badge,0,Qt.AlignTop)
        words=QVBoxLayout();words.setSpacing(4)
        top=QHBoxLayout();top.addWidget(text(kind,'activityKind'));top.addStretch();top.addWidget(text((event['time'] or '')[:10],'caption'));words.addLayout(top)
        link=action(event['title'],lambda checked=False,identity=event['id']:window.detail(identity));link.setObjectName('activityLink');words.addWidget(link)
        message=f"{int(event['message'])//60} min registrados" if kind=='Sessão' else str(event['message'])
        words.addWidget(text(message[:115],'muted'));contents.addLayout(words,1);inside.addLayout(contents)
        layout.addWidget(frame)
    layout.addStretch()


def game_strip(window,layout,title,games,maximum=4):
    heading=QHBoxLayout();caption=text(title,'sectionTitle');caption.setMinimumWidth(250);heading.addWidget(caption);heading.addStretch()
    link=action('Ver tudo  ›',lambda:window.navigate(1));link.setObjectName('quiet');heading.addWidget(link);layout.addLayout(heading)
    strip=QScrollArea();strip.setWidgetResizable(True);strip.setFixedHeight(282);strip.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    tiles=QWidget();row=QHBoxLayout(tiles);row.setContentsMargins(0,0,0,0);row.setSpacing(16);row.setAlignment(Qt.AlignTop)
    for game in games[:maximum]:row.addWidget(GameTile(game,window.detail,width=140))
    row.addStretch();strip.setWidget(tiles);layout.addWidget(strip)


def build_home(window):
    outer=window.clear_page(0);scroll=QScrollArea();scroll.setWidgetResizable(True)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(22)
    games=window.library.games(sort='recent')
    if not games:
        frame,inside=card();inside.addWidget(text('Sua próxima história começa aqui','sectionTitle'))
        inside.addWidget(text('Adicione um jogo para montar sua biblioteca.','muted'));inside.addWidget(action('+ Adicionar jogo',window.add_game,True));layout.addWidget(frame)
        activity(window,layout)
    else:
        playing=[game for game in games if game['status']=='Jogando']
        featured=(playing or [game for game in games if game['favorite']] or games)[0]
        hero=Hero(featured,window.theme);hero.setMinimumHeight(0)
        buttons=QHBoxLayout()
        if featured['executable']:play=action('▶ Continuar jogando' if featured['status']=='Jogando' else '▶ Jogar',lambda:window.start_game(featured),True)
        else:play=action('Ver jogo',lambda:window.detail(featured['id']),True)
        buttons.addWidget(play);buttons.addStretch();hero.content.addLayout(buttons);layout.addWidget(hero)
        continuing=[dict(row) for row in window.library.sql.execute("SELECT g.*,MAX(s.started_at) AS last_played FROM games g JOIN play_sessions s ON s.game_id=g.id WHERE g.deleted_at IS NULL GROUP BY g.id ORDER BY last_played DESC LIMIT 6")] or playing
        content=QHBoxLayout();content.setSpacing(26)
        left=QWidget();left.setObjectName('homeContinuation');left.setMinimumWidth(270);left_layout=QVBoxLayout(left);left_layout.setContentsMargins(0,0,0,0);left_layout.setSpacing(14)
        game_strip(window,left_layout,'Continuar jogando' if continuing else 'Sua biblioteca',continuing or games)
        left_layout.addStretch()
        right=QWidget();right.setObjectName('homeActivity');right.setMinimumWidth(270);right.setMaximumWidth(340);right_layout=QVBoxLayout(right);right_layout.setContentsMargins(0,0,0,0);right_layout.setSpacing(12);activity(window,right_layout)
        content.addWidget(left,2);content.addWidget(right,1);layout.addLayout(content)
        game_strip(window,layout,'Adicionados recentemente',games,6)
    interrupted=window.library.sql.execute("SELECT count(*) FROM play_sessions WHERE state='interrupted'").fetchone()[0]
    if interrupted:layout.addWidget(action(f'{interrupted} sessões para revisar',window.recover_sessions))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

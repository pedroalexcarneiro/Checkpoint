"""Início pessoal: destaque, continuidade e atividade da própria biblioteca."""
from PySide6.QtWidgets import QScrollArea,QWidget,QVBoxLayout,QHBoxLayout
from .ui_components import Hero,GameTile,text,action,card


def build_home(window):
    outer=window.clear_page(0)
    scroll=QScrollArea();scroll.setWidgetResizable(True)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(22)
    games=window.library.games(sort='recent')
    if not games:
        frame,inside=card();inside.addWidget(text('Sua biblioteca começa aqui','sectionTitle'))
        inside.addWidget(text('Adicione um jogo, escolha uma ROM do Drive ou importe sua biblioteca Steam.','muted'))
        inside.addWidget(action('+ Adicionar jogo',window.add_game,True));layout.addWidget(frame)
    else:
        playing=[g for g in games if g['status']=='Jogando']
        featured=(playing or [g for g in games if g['favorite']] or games)[0]
        hero=Hero(featured,window.theme)
        row=QHBoxLayout();row.addWidget(action('Abrir jogo',lambda:window.detail(featured['id']),True));row.addStretch()
        hero.content.addLayout(row);layout.addWidget(hero)
        continuing=[dict(r) for r in window.library.sql.execute("SELECT g.*,MAX(s.started_at) AS last_played FROM games g JOIN play_sessions s ON s.game_id=g.id WHERE g.deleted_at IS NULL GROUP BY g.id ORDER BY last_played DESC LIMIT 6")]
        if not continuing:continuing=playing
        sections=[]
        if continuing:sections.append(('Continuar jogando',continuing[:6]))
        sections.append(('Adicionados recentemente',games[:6]))
        for title,items in sections:
            header=QHBoxLayout();caption=text(title,'sectionTitle');caption.setMinimumWidth(260);header.addWidget(caption);header.addStretch()
            header.addWidget(action('Ver biblioteca',lambda:window.navigate(1)));layout.addLayout(header)
            strip=QScrollArea();strip.setWidgetResizable(True);strip.setMinimumHeight(260);strip.setMaximumHeight(290)
            tiles=QWidget();row=QHBoxLayout(tiles);row.setContentsMargins(0,0,0,0);row.setSpacing(14)
            for game in items:row.addWidget(GameTile(game,window.detail))
            row.addStretch();strip.setWidget(tiles);layout.addWidget(strip)
    layout.addWidget(text('Sua atividade','sectionTitle'))
    events=[]
    queries=[("SELECT g.id,g.title,d.created_at AS time,d.text AS message FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL ORDER BY d.created_at DESC LIMIT 4",'Memória'),
             ("SELECT g.id,g.title,a.unlocked_at AS time,a.title AS message FROM achievements a JOIN games g ON g.id=a.game_id WHERE g.deleted_at IS NULL ORDER BY a.unlocked_at DESC LIMIT 4",'Marco'),
             ("SELECT g.id,g.title,s.started_at AS time,s.duration_seconds AS message FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE g.deleted_at IS NULL AND s.state='finished' ORDER BY s.started_at DESC LIMIT 4",'Sessão')]
    for query,kind in queries:
        for event in window.library.sql.execute(query):events.append((dict(event),kind))
    events.sort(key=lambda item:item[0]['time'] or '',reverse=True)
    if not events:layout.addWidget(text('Suas sessões, memórias e marcos aparecerão aqui.','muted'))
    for event,kind in events[:5]:
        frame,inside=card();row=QHBoxLayout();row.addWidget(text(kind+' · '+event['title'],'sectionTitle'));row.addStretch();row.addWidget(text((event['time'] or '')[:10],'muted'));inside.addLayout(row)
        message=f"{int(event['message'])//60} min registrados" if kind=='Sessão' else str(event['message'])
        inside.addWidget(text(message[:240]));inside.addWidget(action('Abrir jogo',lambda checked=False,identity=event['id']:window.detail(identity)));layout.addWidget(frame)
    interrupted=window.library.sql.execute("SELECT count(*) FROM play_sessions WHERE state='interrupted'").fetchone()[0]
    if interrupted:layout.addWidget(action(f'{interrupted} sessões para revisar',window.recover_sessions))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

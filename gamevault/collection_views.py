"""Desejos e memórias na mesma linguagem visual da biblioteca."""
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QTabWidget
from .ui_components import text,action,card,GameTile,relative_date
from .design_system import CardGrid,page_scroll,empty_state,IconButton,ArtworkButton,Badge


def build_wishlist(window):
    outer=window.clear_page(2);inside=page_scroll(outer)
    rows=[dict(row) for row in window.library.sql.execute('SELECT g.*,w.target_cents FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL ORDER BY g.title COLLATE NOCASE')]
    if not rows:
        inside.addWidget(empty_state('wish','Sua lista de desejos','Guarde os jogos que você quer jogar e defina suas metas de preço.',lambda:window.navigate(1),'Explorar biblioteca'));inside.addStretch();return
    top=QHBoxLayout();top.addWidget(text(f'{len(rows)} jogos','muted'));top.addStretch();top.addWidget(text('Metas pessoais · sem consulta automática de preços','caption'));inside.addLayout(top)
    grid=CardGrid(240);grid.setObjectName('wishlistGrid')
    for game in rows:
        panel,body=card();panel.setObjectName('panel');tile=GameTile(game,window.detail,width=156);body.addWidget(tile,0,Qt.AlignHCenter)
        line=QHBoxLayout();line.addWidget(text('Meta de preço','muted'));line.addStretch();line.addWidget(text(f"R$ {game['target_cents']/100:.2f}".replace('.',','),'cardTitle'));body.addLayout(line)
        line=QHBoxLayout();edit=action('Alterar meta',lambda checked=False,g=game['id']:window.add_wish(g));edit.setObjectName('quiet');line.addWidget(edit);line.addStretch();line.addWidget(IconButton('trash','Retirar dos desejos',lambda checked=False,g=game['id']:window.remove_wish(g)));body.addLayout(line);grid.add_card(panel)
    inside.addWidget(grid);inside.addStretch()


def memory_card(window,record):
    panel,inside=card();head=QHBoxLayout();head.addWidget(Badge('memories' if record['kind']=='diary' else 'play' if record['kind']=='video' else 'memories',32))
    title=action(record['title'],lambda checked=False,g=record['game_id']:window.detail(g));title.setObjectName('activityLink');head.addWidget(title,1);inside.addLayout(head)
    if record['kind']=='diary':
        content=text(record['text'],'bodyText');content.setMaximumHeight(130);inside.addWidget(content);inside.addStretch()
    else:
        inside.addWidget(ArtworkButton(record['path'],record['caption'] or Path(record['path']).name,lambda checked=False,m=record:window.show_media(m),height=160))
        if record['caption']:inside.addWidget(text(record['caption'],'muted'))
    bottom=QHBoxLayout();bottom.addWidget(text('Diário' if record['kind']=='diary' else 'Vídeo' if record['kind']=='video' else 'Captura','caption'));bottom.addStretch();bottom.addWidget(text(relative_date(record['created_at']),'caption'));inside.addLayout(bottom)
    return panel


def build_memories(window):
    outer=window.clear_page(3)
    records=[{**dict(row),'kind':'diary'} for row in window.library.sql.execute('SELECT d.*,g.title FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL')]
    records.extend(dict(row) for row in window.library.sql.execute('SELECT m.*,g.title FROM media_files m JOIN games g ON g.id=m.game_id WHERE g.deleted_at IS NULL'))
    records.sort(key=lambda row:row['created_at'],reverse=True)
    tabs=QTabWidget();tabs.setObjectName('memoryTabs')
    for name,kind in [('Tudo',None),('Diário','diary'),('Capturas e vídeos','media')]:
        page=QWidget();layout=QVBoxLayout(page);layout.setContentsMargins(0,16,0,0);inside=page_scroll(layout)
        selected=[row for row in records if kind is None or (row['kind']=='diary')==(kind=='diary')]
        if selected:
            grid=CardGrid(320);grid.setObjectName('memoriesGrid')
            for record in selected:grid.add_card(memory_card(window,record))
            inside.addWidget(grid)
        else:inside.addWidget(empty_state('memories','Guarde suas experiências','Adicione memórias, capturas e vídeos na ficha de cada jogo.',lambda:window.navigate(1),'Escolher jogo'))
        inside.addStretch();tabs.addTab(page,name)
    outer.addWidget(tabs)

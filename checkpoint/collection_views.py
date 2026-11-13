"""Desejos e memórias na mesma linguagem visual da biblioteca."""
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QHBoxLayout,QTabWidget,QFrame,QSizePolicy,QPushButton
from .ui_components import text,action,card,GameTile,relative_date
from .design_system import CardGrid,page_scroll,empty_state,IconButton,ArtworkButton,Badge


class WishLogo(QPushButton):
    def __init__(self,game):
        super().__init__();self.setObjectName('wishLogo');self.game=game;self.setFixedSize(180,270);self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed);self.setAccessibleName(game['title'])
        from PySide6.QtGui import QPixmap
        self.pixmap=QPixmap(game.get('logo') or '')
        if not self.pixmap.isNull() and self.pixmap.hasAlphaChannel():
            from PySide6.QtGui import QRegion
            bounds=QRegion(self.pixmap.mask()).boundingRect()
            if not bounds.isEmpty():self.pixmap=self.pixmap.copy(bounds)
    def paintEvent(self,event):
        from PySide6.QtGui import QPainter,QFont,QColor
        from PySide6.QtCore import QRectF
        from .design_system import colors
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        if not self.pixmap.isNull():
            pix=self.pixmap.scaled(max(1,self.width()-32),max(1,self.height()-24),Qt.KeepAspectRatio,Qt.SmoothTransformation);p.drawPixmap((self.width()-pix.width())//2,(self.height()-pix.height())//2,pix)
        else:
            font=QFont('Segoe UI');font.setPixelSize(12);font.setWeight(QFont.Normal);p.setFont(font);p.setPen(QColor(colors()['muted']));p.drawText(QRectF(self.rect()),Qt.AlignCenter,'Sem logo disponível')
        p.end()


class WishTitle(QLabel):
    def __init__(self,title):
        super().__init__();self.title=title;self.setObjectName('cardTitle');self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed);self.setMinimumWidth(0);self.setFixedHeight(20);self.setAlignment(Qt.AlignLeft|Qt.AlignVCenter);self.setToolTip(title);self.setWordWrap(False)
    def resizeEvent(self,event):
        super().resizeEvent(event);self.setText(self.fontMetrics().elidedText(self.title,Qt.ElideRight,self.width()))


class WishCard(QFrame):
    def __init__(self,game):
        super().__init__();self.game=game;self.setObjectName('panel');self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed);self.setAccessibleName(game['title']);self.setAccessibleDescription('Na lista de desejos')


class WishGrid(CardGrid):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        from PySide6.QtWidgets import QLayout
        self.grid.setSizeConstraint(QLayout.SetNoConstraint)
    def minimumSizeHint(self):
        from PySide6.QtCore import QSize
        return QSize(0,0)
    def reflow(self):
        self.columns=4
        spacing=self.grid.spacing();width=max(1,(self.width()-spacing*3)//4)
        art_width=max(1,width-24);art_height=round(art_width*1.5);height=art_height+146
        while self.grid.count():self.grid.takeAt(0)
        for column in range(4):self.grid.setColumnStretch(column,1)
        for index,card in enumerate(self.cards):
            card.setFixedSize(width,height)
            logo=card.findChild(WishLogo)
            if logo:logo.setFixedSize(art_width,art_height)
            self.grid.addWidget(card,index//4,index%4)
        rows=(len(self.cards)+3)//4
        self.setFixedHeight(rows*height+max(0,rows-1)*spacing)


def build_wishlist(window):
    outer=window.clear_page(2);inside=page_scroll(outer,reserve_scrollbar=True)
    rows=[dict(row) for row in window.library.sql.execute('SELECT g.*,w.target_cents FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL ORDER BY g.title COLLATE NOCASE')]
    if not rows:
        inside.addWidget(empty_state('wish','Nenhum desejo','',window.add_game,'Adicionar desejo'));inside.addStretch();return
    from .locale import count_text
    top=QHBoxLayout();top.addWidget(text(count_text(len(rows),'jogo'),'muted'));top.addStretch();top.addWidget(action('+ Adicionar desejo',window.add_game,True));inside.addLayout(top)
    grid=WishGrid(260);grid.setObjectName('wishlistGrid')
    from .price_view import price_summary,source_link
    for game in rows:
        panel=WishCard(game);body=QVBoxLayout(panel);body.setContentsMargins(12,12,12,12);body.setSpacing(6)
        logo=WishLogo(game);logo.clicked.connect(lambda checked=False,g=game['id']:window.detail(g));body.addWidget(logo,0,Qt.AlignHCenter)
        body.addWidget(WishTitle(game['title']))
        body.addWidget(price_summary(window.library,game))
        line=QHBoxLayout();line.setSpacing(4);line.addWidget(source_link(window.library,game));line.addStretch();line.addWidget(IconButton('plus','Adicionar à biblioteca',lambda checked=False,g=game['id']:window.acquire_wish(g)));line.addWidget(IconButton('trash','Retirar dos desejos',lambda checked=False,g=game['id']:window.remove_wish(g)));
        body.addLayout(line)
        for control in panel.findChildren(IconButton):control.setFixedSize(28,28)
        grid.add_card(panel)
    inside.addWidget(grid);inside.addStretch()
    if window.isVisible() and window.library.setting('artwork.auto',True):
        requested=getattr(window,'wish_logos_requested',set())
        missing=[game['id'] for game in rows if not game['logo'] and game['id'] not in requested and window.library.sql.execute('SELECT 1 FROM external_identifiers WHERE game_id=?',(game['id'],)).fetchone()]
        window.wish_logos_requested=requested|set(missing)
        if missing:window.completion_queue.submit(missing)
    if window.isVisible() and window.library.setting('prices.auto',True):window.price_queue.submit([game['id'] for game in rows])


def memory_card(window,record):
    panel,inside=card();head=QHBoxLayout();head.addWidget(Badge('memories' if record['kind']=='diary' else 'play' if record['kind']=='video' else 'memories',32))
    title=action(record['title'],lambda checked=False,g=record['game_id']:window.detail(g));title.setObjectName('activityLink');head.addWidget(title,1);inside.addLayout(head)
    if record['kind']=='diary':
        content=text(record['text'],'bodyText');content.setToolTip(record['text']);inside.addWidget(content);inside.addStretch()
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
        else:inside.addWidget(empty_state('memories','Nenhuma memória','',lambda:window.navigate(1),'Biblioteca'))
        inside.addStretch();tabs.addTab(page,name)
    outer.addWidget(tabs)

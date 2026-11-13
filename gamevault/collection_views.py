"""Desejos e memórias na mesma linguagem visual da biblioteca."""
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QHBoxLayout,QTabWidget,QFrame,QSizePolicy,QPushButton
from .ui_components import text,action,card,GameTile,relative_date
from .design_system import CardGrid,page_scroll,empty_state,IconButton,ArtworkButton,Badge


class WishLogo(QPushButton):
    def __init__(self,game):
        super().__init__();self.setObjectName('wishLogo');self.game=game;self.setMinimumHeight(72);self.setAccessibleName(game['title'])
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
            pix=self.pixmap.scaled(max(1,self.width()-12),max(1,self.height()-12),Qt.KeepAspectRatio,Qt.SmoothTransformation);p.drawPixmap((self.width()-pix.width())//2,(self.height()-pix.height())//2,pix)
        else:
            font=QFont('Segoe UI');font.setPixelSize(13);font.setWeight(QFont.Normal);p.setFont(font);p.setPen(QColor(colors()['text']));p.drawText(QRectF(self.rect()),Qt.AlignCenter,'Logo indisponível')
        p.end()


class WishTitle(QLabel):
    def __init__(self,title):
        super().__init__();self.title=title;self.setObjectName('caption');self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed);self.setMinimumWidth(0);self.setFixedHeight(20);self.setAlignment(Qt.AlignCenter);self.setToolTip(title);self.setWordWrap(False)
    def resizeEvent(self,event):
        super().resizeEvent(event);self.setText(self.fontMetrics().elidedText(self.title,Qt.ElideRight,self.width()))


class SquareWishCard(QFrame):
    def __init__(self,game):
        super().__init__();self.game=game;self.setObjectName('panel');self.setMinimumWidth(232);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed);self.setAccessibleName(game['title']);self.setAccessibleDescription('Na lista de desejos')
    def resizeEvent(self,event):
        super().resizeEvent(event)
        if self.height()!=self.width():self.setFixedHeight(self.width())


class WishGrid(CardGrid):
    def reflow(self):
        super().reflow()
        if not self.cards:return
        columns=max(1,self.columns);spacing=self.grid.spacing();height=(self.width()-spacing*(columns-1)+columns-1)//columns
        for row in range(self.grid.rowCount()):self.grid.setRowMinimumHeight(row,0)
        for card in self.cards:card.setFixedHeight(height)
        rows=(len(self.cards)+columns-1)//columns
        for row in range(rows):self.grid.setRowMinimumHeight(row,height)
        self.setMinimumHeight(rows*height+max(0,rows-1)*spacing);self.grid.invalidate()


def build_wishlist(window):
    outer=window.clear_page(2);inside=page_scroll(outer)
    rows=[dict(row) for row in window.library.sql.execute('SELECT g.*,w.target_cents FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL ORDER BY g.title COLLATE NOCASE')]
    if not rows:
        inside.addWidget(empty_state('wish','Sua lista de desejos','Guarde os jogos que você quer jogar.',window.add_game,'Adicionar desejo'));inside.addStretch();return
    top=QHBoxLayout();top.addWidget(text(f'{len(rows)} jogos','muted'));top.addStretch();top.addWidget(text('Menores preços atuais','caption'));inside.addLayout(top)
    grid=WishGrid(260);grid.setObjectName('wishlistGrid')
    from .price_view import price_summary,source_link
    for game in rows:
        panel=SquareWishCard(game);body=QVBoxLayout(panel);body.setContentsMargins(16,12,16,12);body.setSpacing(6)
        logo=WishLogo(game);logo.clicked.connect(lambda checked=False,g=game['id']:window.detail(g));body.addWidget(logo,1)
        body.addWidget(WishTitle(game['title']))
        body.addWidget(price_summary(window.library,game))
        line=QHBoxLayout();line.setSpacing(8);line.addWidget(source_link(window.library,game));line.addStretch();line.addWidget(IconButton('plus','Adicionar à biblioteca',lambda checked=False,g=game['id']:window.acquire_wish(g)));line.addWidget(IconButton('trash','Retirar dos desejos',lambda checked=False,g=game['id']:window.remove_wish(g)));body.addLayout(line);grid.add_card(panel)
    inside.addWidget(grid);inside.addStretch()
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
        else:inside.addWidget(empty_state('memories','Guarde suas experiências','Adicione memórias, capturas e vídeos na ficha de cada jogo.',lambda:window.navigate(1),'Escolher jogo'))
        inside.addStretch();tabs.addTab(page,name)
    outer.addWidget(tabs)

"""Desejos e memórias na mesma linguagem visual da biblioteca."""
from pathlib import Path
from .cover_art import CoverArtwork
from .visual_tokens import SPACE
from .design_system import CardSurface
from PySide6.QtCore import Qt,QSize,QTimer
from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QHBoxLayout,QBoxLayout,QTabWidget,QFrame,QSizePolicy,QPushButton,QComboBox
from .ui_components import text,action,card,GameTile,relative_date
from .design_system import CardGrid,page_scroll,empty_state,IconButton,ArtworkButton,Badge


class WishLogo(CoverArtwork):
    def __init__(self,game):
        super().__init__();self.setObjectName('wishLogo');self.game=game;self.setFixedSize(180,180);self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed);self.setAccessibleName(game['title'])
        from PySide6.QtGui import QPixmap
        self.pixmap=QPixmap(game.get('logo') or '');self.is_logo=not self.pixmap.isNull()
        if not self.is_logo:self.pixmap=QPixmap(game.get('cover') or '')
        if self.is_logo and self.pixmap.hasAlphaChannel():
            from PySide6.QtGui import QRegion
            bounds=QRegion(self.pixmap.mask()).boundingRect()
            if not bounds.isEmpty():self.pixmap=self.pixmap.copy(bounds)
    def paintEvent(self,event):
        from PySide6.QtGui import QPainter,QFont,QColor
        from PySide6.QtCore import QRectF
        from .design_system import colors
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing)
        CoverArtwork.paint_art(p,QRectF(self.rect()),self.pixmap,self.game['title'],colors(),self.hasFocus() or self.underMouse(),padding=SPACE['md'] if self.is_logo else 0)
        p.end()


class WishTitle(QLabel):
    def __init__(self,title):
        super().__init__();self.title=title;self.setObjectName('cardTitle');self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed);self.setMinimumWidth(0);self.setFixedHeight(20);self.setAlignment(Qt.AlignLeft|Qt.AlignVCenter);self.setToolTip(title);self.setWordWrap(False)
    def resizeEvent(self,event):
        super().resizeEvent(event);self.setText(self.fontMetrics().elidedText(self.title,Qt.ElideRight,self.width()))


class WishCard(CardSurface):
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
        from .card_layout import card_metrics
        metrics=card_metrics(self.width(),getattr(self,'cover_percent',100))
        self.columns=metrics.columns;spacing=metrics.gap;self.grid.setSpacing(spacing);width=metrics.width
        art_width=max(1,width-2*SPACE['md']);art_height=art_width;compact=width<200;height=art_height+(304 if compact else 272)
        while self.grid.count():self.grid.takeAt(0)
        self.grid.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        for column in range(self.grid.columnCount()):self.grid.setColumnStretch(column,0)
        for index,card in enumerate(self.cards):
            card.setFixedSize(width,height)
            if hasattr(card,'footer'):card.footer.setDirection(QBoxLayout.TopToBottom if compact else QBoxLayout.LeftToRight)
            logo=card.findChild(WishLogo)
            if logo:logo.setFixedSize(art_width,art_height)
            self.grid.addWidget(card,index//self.columns,index%self.columns)
        rows=(len(self.cards)+self.columns-1)//self.columns
        self.setFixedHeight(rows*height+max(0,rows-1)*spacing)


def build_wishlist(window):
    old=getattr(window,'wishlist_scroll',None)
    position=old.verticalScrollBar().value() if old else 0
    outer=window.clear_page(2);inside=page_scroll(outer,reserve_scrollbar=True);window.wishlist_scroll=inside.scroll_area
    scroll=window.wishlist_scroll
    bar=scroll.verticalScrollBar()
    restored=False
    def restore_position(*args):
        nonlocal restored
        if not restored and bar.maximum()>0:
            restored=True;bar.rangeChanged.disconnect(restore_position);bar.setValue(min(position,bar.maximum()))
    bar.rangeChanged.connect(restore_position)
    QTimer.singleShot(0,scroll,restore_position)
    rows=[dict(row) for row in window.library.sql.execute('SELECT g.*,w.target_cents FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL ORDER BY g.title COLLATE NOCASE')]
    if not rows:
        inside.addWidget(empty_state('wish','Nenhum desejo','Salve os jogos que você quer jogar para acompanhar suas ofertas.',window.add_game,'Adicionar desejo'));inside.addStretch();return
    from .locale import count_text
    top=QHBoxLayout();top.addWidget(text(count_text(len(rows),'jogo'),'muted'));top.addStretch();top.addWidget(action('+ Adicionar desejo',window.add_game,True));inside.addLayout(top)
    from .card_layout import cover_size
    from .prices import wishlist_order
    selected_order=window.library.setting('wishlist.order','name')
    if selected_order not in ('name','price'):selected_order='name';window.library.set_setting('wishlist.order',selected_order)
    order=QComboBox();order.setObjectName('wishlistOrder');order.addItem('Nome A–Z','name');order.addItem('Menor preço atual','price');order.setCurrentIndex(max(0,order.findData(selected_order)))
    from .price_view import attribution_link
    top.insertWidget(1,attribution_link())
    def change_order(index):
        window.library.set_setting('wishlist.order',order.itemData(index));window.wishlist()
    order.currentIndexChanged.connect(change_order);top.insertWidget(1,order)
    rows=wishlist_order(window.library,rows,order.currentData())
    grid=WishGrid(260);grid.cover_percent=cover_size(window.library);grid.setObjectName('wishlistGrid');grid.setProperty('cardComponent','coverCard')
    from .price_view import price_summary,source_link
    for game in rows:
        panel=WishCard(game);body=QVBoxLayout(panel);body.setContentsMargins(*([SPACE['md']]*4));body.setSpacing(SPACE['sm'])
        logo=WishLogo(game);logo.clicked.connect(lambda checked=False,g=game['id']:window.detail(g));body.addWidget(logo,0,Qt.AlignHCenter)
        body.addWidget(WishTitle(game['title']))
        body.addWidget(price_summary(window.library,game))
        line=QBoxLayout(QBoxLayout.LeftToRight);line.setSpacing(4)
        offers=source_link(window.library,game);line.addWidget(offers,1)
        controls=QWidget();controls.setFixedSize(60,28);buttons=QHBoxLayout(controls);buttons.setContentsMargins(0,0,0,0);buttons.setSpacing(4)
        buttons.addWidget(IconButton('plus','Adicionar à biblioteca',lambda checked=False,g=game['id']:window.acquire_wish(g)))
        buttons.addWidget(IconButton('trash','Retirar dos desejos',lambda checked=False,g=game['id']:window.remove_wish(g)))
        line.addWidget(controls,0,Qt.AlignRight);panel.footer=line;body.addLayout(line)
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

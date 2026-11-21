"""Desejos e memórias na mesma linguagem visual da biblioteca."""
from pathlib import Path
from .cover_art import CoverArtwork
from .visual_tokens import SPACE
from .design_system import CardSurface,colors
from PySide6.QtCore import Qt,QSize,QTimer
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QHBoxLayout,QBoxLayout,QTabWidget,QFrame,QSizePolicy,QPushButton,QComboBox,QCheckBox
from .ui_components import text,action,card,GameTile,relative_date,ElidedAction
from .design_system import CardGrid,page_scroll,empty_state,IconButton,ArtworkButton,Badge
from .icons import lucide_icon


class WishFilterCombo(QComboBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('QComboBox::down-arrow { image: none; }')
        self.currentTextChanged.connect(self.setToolTip)

    def paintEvent(self,event):
        super().paintEvent(event)
        painter=QPainter(self)
        arrow=lucide_icon('chevron',colors()['muted'],16).pixmap(16,16)
        painter.drawPixmap(self.width()-24,(self.height()-16)//2,arrow)
        painter.end()


class WishLogo(CoverArtwork):
    def __init__(self,game):
        super().__init__();self.setObjectName('wishLogo');self.game=game;self.setFixedSize(180,180);self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed);self.setAccessibleName(game['title'])
        from PySide6.QtGui import QPixmap
        self.pixmap=QPixmap(game.get('logo') or '');self.is_logo=not self.pixmap.isNull()
        if not self.is_logo:self.pixmap=QPixmap(game.get('cover') or '')
        if self.pixmap.isNull():self.pixmap=QPixmap(game.get('banner') or '')
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
        spacing=metrics.gap;self.grid.setSpacing(spacing)
        self.columns=max(1,(self.width()+spacing)//(220+spacing))
        width=min(238,max(1,(self.width()-spacing*(self.columns-1))//self.columns))
        art_width=max(1,width-2*SPACE['md']);art_height=art_width;compact=width<200
        while self.grid.count():self.grid.takeAt(0)
        self.grid.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        for column in range(self.grid.columnCount()):self.grid.setColumnStretch(column,0)
        heights=[]
        for card in self.cards:
            if hasattr(card,'footer'):card.footer.setDirection(QBoxLayout.TopToBottom if compact else QBoxLayout.LeftToRight)
            logo=card.findChild(WishLogo)
            if logo:logo.setFixedSize(art_width,art_height)
            if hasattr(card,'price_block'):
                block=card.price_block;block.ensurePolished();amount=block.layout().totalHeightForWidth(art_width)
                block.setFixedHeight(max(32,amount if amount>=0 else block.layout().sizeHint().height()))
            card.layout().invalidate();needed=card.layout().totalHeightForWidth(width)
            heights.append(needed if needed>=0 else card.layout().sizeHint().height())
        height=max(heights,default=0)
        for index,card in enumerate(self.cards):
            card.setFixedSize(width,height)
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
        inside.addWidget(empty_state('wish','Nenhum desejo','Adicione um jogo aos desejos.',window.add_game,'Adicionar desejo'));inside.addStretch();return
    from .locale import count_text
    top=QHBoxLayout();top.addWidget(text(count_text(len(rows),'jogo'),'muted'));top.addStretch();top.addWidget(action('+ Adicionar desejo',window.add_game,True));inside.addLayout(top)
    from .wish_platforms import options,selected
    filters=QHBoxLayout();filters.setSpacing(10);platform=WishFilterCombo();platform.setObjectName('wishlistPlatform');platform.setAccessibleName('Plataforma dos desejos')
    platform.setMaximumWidth(118)
    choices=options(rows)
    for caption,key in choices:platform.addItem(caption,key)
    saved=window.library.setting('wishlist.platform_filter','all')
    platform.setCurrentIndex(max(0,platform.findData(saved)));filters.addWidget(platform)
    def change_platform(index):
        window.library.set_setting('wishlist.platform_filter',platform.itemData(index));window.wishlist()
    platform.currentIndexChanged.connect(change_platform)
    rows=selected(rows,platform.currentData());top.itemAt(0).widget().setText(count_text(len(rows),'jogo'))
    inside.addLayout(filters)
    from .card_layout import cover_size
    from .prices import set_offer_details,wishlist_order
    selected_order=window.library.setting('wishlist.order','name')
    if selected_order not in ('name','price','discount'):selected_order='name';window.library.set_setting('wishlist.order',selected_order)
    order=WishFilterCombo();order.setObjectName('wishlistOrder');order.addItem('Alfabeticamente','name');order.addItem('Menor preço','price');order.addItem('Maior desconto','discount');order.setCurrentIndex(max(0,order.findData(selected_order)))
    order.setMaximumWidth(174)
    from .price_view import attribution_link
    filters.addWidget(attribution_link())
    def change_order(index):
        window.library.set_setting('wishlist.order',order.itemData(index));window.wishlist()
    order.currentIndexChanged.connect(change_order);filters.insertWidget(1,order)
    keyshops=QCheckBox('Incluir keyshops');keyshops.setObjectName('includeKeyshops');keyshops.setChecked(window.library.setting('prices.include_keyshops',False))
    def include_keyshops(value):
        window.library.set_setting('prices.include_keyshops',value);window.wishlist()
    keyshops.toggled.connect(include_keyshops);filters.insertWidget(2,keyshops);filters.addStretch()
    discounts=QCheckBox('Completar descontos')
    discounts.setObjectName('wishlistOfferDetails')
    discounts.setChecked(window.library.setting('prices.offer_details',False))
    def complete_discounts(value):
        set_offer_details(window.library,value)
        if value:window.price_queue.submit([game['id'] for game in rows])
    discounts.toggled.connect(complete_discounts);filters.insertWidget(3,discounts)
    if not rows:
        def clear_platform():window.library.set_setting('wishlist.platform_filter','all');window.wishlist()
        inside.addWidget(empty_state('wish','Nenhum desejo nesta plataforma','Escolha outra plataforma ou limpe o filtro.',clear_platform,'Todas'));inside.addStretch();return
    rows=wishlist_order(window.library,rows,order.currentData())
    grid=WishGrid(260);grid.cover_percent=cover_size(window.library);grid.setObjectName('wishlistGrid');grid.setProperty('cardComponent','coverCard')
    from .price_view import price_summary,source_link
    for game in rows:
        panel=WishCard(game);body=QVBoxLayout(panel);body.setContentsMargins(*([SPACE['md']]*4));body.setSpacing(SPACE['sm'])
        logo=WishLogo(game);logo.clicked.connect(lambda checked=False,g=game['id']:window.detail(g));body.addWidget(logo,0,Qt.AlignHCenter)
        body.addWidget(WishTitle(game['title']))
        panel.price_block=price_summary(window.library,game);body.addWidget(panel.price_block)
        line=QBoxLayout(QBoxLayout.LeftToRight);line.setSpacing(4)
        offers=source_link(window.library,game);offers.setFixedHeight(28);line.addWidget(offers,1)
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


def memory_card(window,record,diary_only=False,thumbnail_cache=None):
    panel,inside=card();panel.setMinimumHeight(0 if diary_only else 320)
    panel.setProperty('diaryOnly',diary_only);inside.setContentsMargins(16,16,16,16);inside.setSpacing(12)
    head=QHBoxLayout();head.setSpacing(10);head.addWidget(Badge('memories' if record['kind']=='diary' else 'play' if record['kind']=='video' else 'memories',32))
    title=ElidedAction(record['title'],lambda checked=False,g=record['game_id']:window.detail(g));title.setObjectName('activityLink');head.addWidget(title,1);head.addWidget(IconButton('trash','Apagar memória',lambda checked=False,r=record:window.delete_memory(r)));inside.addLayout(head)
    if record['kind']=='diary':
        if diary_only:
            content=text(record['text'],'bodyText');content.setAlignment(Qt.AlignLeft|Qt.AlignTop)
            content.setToolTip(record['text']);inside.addWidget(content,0,Qt.AlignTop)
        else:
            from PySide6.QtWidgets import QTextEdit
            from .design_system import colors
            content=QTextEdit();content.setObjectName('memoryTextArea');content.setReadOnly(True)
            content.setPlainText(record['text']);content.setFixedHeight(160)
            content.setStyleSheet('QTextEdit#memoryTextArea { background: '+colors()['input']+'; border: none; border-radius: 12px; padding: 10px; font-size: 14px; }')
            content.setAccessibleName('Anotação de '+record['title']);inside.addWidget(content);inside.addStretch()
    elif record.get('missing'):
        inside.addWidget(text('Arquivo movido ou removido.','muted'));inside.addStretch()
    else:
        callback=lambda checked=False,m=record:window.show_media(m)
        caption=record['caption'] or Path(record['path']).name
        if thumbnail_cache is None:
            preview=ArtworkButton(record['path'],caption,callback,height=160,background=False)
        else:
            from .memory_artwork import MemoryArtwork
            preview=MemoryArtwork(record['path'],caption,callback,thumbnail_cache)
        inside.addWidget(preview)
        if record['caption']:inside.addWidget(text(record['caption'],'muted'))
        inside.addStretch()
    bottom=QHBoxLayout();bottom.addWidget(text('Diário' if record['kind']=='diary' else 'Vídeo' if record['kind']=='video' else 'Captura','caption'));bottom.addStretch();bottom.addWidget(text(relative_date(record['created_at']),'caption'));inside.addLayout(bottom)
    return panel


class MemoryGrid(CardGrid):
    def reflow(self):
        gap=self.grid.spacing()
        columns=max(1,(self.width()+gap)//(280+gap))
        width=min(336,max(1,(self.width()-gap*(columns-1))//columns))
        if len(self.cards)<columns:width=min(320,width)
        for column in range(max(columns,self.columns)):
            self.grid.setColumnStretch(column,0)
            self.grid.setColumnMinimumWidth(column,width if column<columns else 0)
        self.grid.setAlignment(Qt.AlignTop|(Qt.AlignHCenter if len(self.cards)>=columns else Qt.AlignLeft))
        while self.grid.count():self.grid.takeAt(0)
        for index,panel in enumerate(self.cards):
            panel.setFixedWidth(width);self.grid.addWidget(panel,index//columns,index%columns,Qt.AlignTop|Qt.AlignLeft)
        self.columns=columns


def build_memories(window):
    from .memory_view import MemoryBrowser
    browser=getattr(window,'memory_browser',None)
    if browser is None:
        outer=window.clear_page(3)
        browser=window.memory_browser=MemoryBrowser(window)
        outer.addWidget(browser)
    else:browser.refresh()

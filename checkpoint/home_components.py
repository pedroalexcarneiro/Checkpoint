"""Cards e navegação do Início, com ações separadas e conteúdo local."""
from math import sqrt

from PySide6.QtCore import Qt,QRectF,QSize,QSizeF
from PySide6.QtGui import QPainter,QPainterPath,QColor,QPixmap,QLinearGradient,QRadialGradient,QTransform,QBrush,QRegion,QFont,QPen
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QSizePolicy,QDialog,QScrollArea,QBoxLayout,QLayout
from .design_system import CardSurface,IconButton,SectionHeader,ArtworkButton,colors
from .ui_components import text,action,ElidedAction
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


def continue_game(window,game):
    if game.get('executable') or window.library.sql.execute('SELECT 1 FROM game_files WHERE game_id=?',(game['id'],)).fetchone():
        window.start_game(game)
    else:
        window.edit_game(game['id'])


class LastPlayedBanner(QPushButton):
    """A arte conserva todo o quadro; continuar tem uma ação independente."""
    def __init__(self,window,game):
        super().__init__();self.game_id=game['id'];self.title=game['title']
        self.banner=QPixmap(game.get('banner') or '')
        self.logo=QPixmap(game.get('logo') or '')
        self.transition_color=QColor('#131923')
        if not self.banner.isNull():
            edge=self.banner.copy(0,0,max(1,self.banner.width()//12),self.banner.height())
            tone=edge.scaled(1,1,Qt.IgnoreAspectRatio,Qt.SmoothTransformation).toImage().pixelColor(0,0)
            if tone.alpha():
                self.transition_color=tone.darker(220)
                self.transition_color.setAlpha(255)
        if not self.logo.isNull() and self.logo.hasAlphaChannel():
            bounds=QRegion(self.logo.mask()).boundingRect()
            if not bounds.isEmpty():self.logo=self.logo.copy(bounds)
        self.setObjectName('homeLastPlayed');self.setCursor(Qt.PointingHandCursor)
        self.setAccessibleName('Abrir ficha de '+self.title);self.setFocusPolicy(Qt.StrongFocus)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed);self.setFixedHeight(164)
        self.clicked.connect(lambda:window.detail(self.game_id))
        layout=QVBoxLayout(self);layout.setContentsMargins(24,16,24,20);layout.addStretch()
        self.play_button=action('Continuar',lambda:continue_game(window,game),True)
        self.play_button.setProperty('homeContinue',True)
        layout.addWidget(self.play_button,0,Qt.AlignLeft)

    def resizeEvent(self,event):
        super().resizeEvent(event)
        height=round(self.width()*.16)
        if not self.banner.isNull():
            height=max(height,round(self.width()*.65*self.banner.height()/self.banner.width())+10)
        self.setFixedHeight(max(154,min(390,height)))

    def identity_width(self):
        if self.banner.isNull():return max(160,min(400,self.width()-48))
        return max(120,min(300,round(self.width()*.26)))

    def banner_target(self):
        if self.banner.isNull():return QRectF()
        gutter=5
        available=QSizeF(max(1,self.width()-self.identity_width()-24-gutter),self.height()-2*gutter)
        size=QSizeF(self.banner.size()).scaled(available,Qt.KeepAspectRatio)
        return QRectF(self.width()-gutter-size.width(),(self.height()-size.height())/2,size.width(),size.height())

    def paint_banner(self,painter,target):
        width,height=self.banner.width(),self.banner.height()
        background=QLinearGradient(0,0,target.left(),0)
        background.setColorAt(0,QColor('#0d1119'))
        background.setColorAt(1,self.transition_color)
        painter.fillRect(self.rect(),background)
        # Os pixels externos completam o contorno sem alterar a proporção da imagem.
        columns=((target.left(),target.width(),0,width),
                 (target.right(),self.width()-target.right(),width-1,1))
        rows=((0,target.top(),0,1),
              (target.top(),target.height(),0,height),
              (target.bottom(),self.height()-target.bottom(),height-1,1))
        for x,tile_width,source_x,source_width in columns:
            for y,tile_height,source_y,source_height in rows:
                painter.drawPixmap(QRectF(x,y,tile_width,tile_height),self.banner,
                                   QRectF(source_x,source_y,source_width,source_height))
        # A elipse toca a borda da arte no meio da faixa e recua no topo e na base.
        radius_x=target.width()*.61
        curve_depth=min(54,self.height()*.27,target.width()*.12)
        corner_offset=sqrt(1-(1-curve_depth/radius_x)**2)
        radius_y=self.height()/(2*corner_offset)
        feather=min(82,target.width()*.18)
        clear_stop=1-feather/radius_x
        center_x=target.left()+radius_x
        transparent=QColor(self.transition_color);transparent.setAlpha(0)
        fade=QRadialGradient(0,0,1)
        fade.setColorAt(clear_stop,transparent)
        fade.setColorAt(1,self.transition_color)
        brush=QBrush(fade)
        brush.setTransform(QTransform().translate(center_x,self.height()/2).scale(radius_x,radius_y))
        clear_at_corner=center_x-radius_x*sqrt(clear_stop**2-corner_offset**2)
        blend_left=target.left()-2
        painter.fillRect(QRectF(blend_left,0,clear_at_corner-blend_left,self.height()),brush)

    def paintEvent(self,event):
        from .visual_tokens import RADIUS
        bounds=QRectF(self.rect()).adjusted(.5,.5,-.5,-.5)
        radius=RADIUS['card'];contour=QPainterPath();contour.addRoundedRect(bounds,radius,radius)
        painter=QPainter(self);painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setClipPath(contour)
        target=self.banner_target()
        if not self.banner.isNull():
            self.paint_banner(painter,target)
        else:
            background=QLinearGradient(0,0,self.width(),0)
            background.setColorAt(0,QColor('#0d1119'))
            background.setColorAt(1,QColor(colors()['elevated']))
            painter.fillRect(bounds,background)
        area=QRectF(24,16,self.identity_width(),max(20,self.play_button.y()-24))
        if not self.logo.isNull():
            size=QSizeF(self.logo.size()).scaled(area.size(),Qt.KeepAspectRatio)
            target=QRectF(area.x(),area.center().y()-size.height()/2,size.width(),size.height())
            painter.drawPixmap(target,self.logo,QRectF(self.logo.rect()))
        else:
            font=QFont(self.font());font.setPixelSize(24 if self.width()>=600 else 18);font.setBold(True)
            painter.setFont(font);painter.setPen(QColor('#f4f8fd'))
            painter.drawText(area,Qt.AlignVCenter|Qt.AlignLeft|Qt.TextWordWrap,
                             painter.fontMetrics().elidedText(self.title,Qt.ElideRight,round(area.width()*2)))
        painter.setClipping(False)
        painter.setPen(QPen(QColor(colors()['accent'] if self.hasFocus() else colors()['border']),1))
        painter.drawPath(contour)


class RecentArtwork(QPushButton):
    """Capa inteira; banner é alternativa somente quando não há capa."""
    def __init__(self,game,window,maximum_height=None):
        super().__init__();self.game=game;self.host_window=window;self.art_kind='cover'
        self.pixmap=QPixmap(game.get('cover') or '')
        if self.pixmap.isNull():self.art_kind='banner';self.pixmap=QPixmap(game.get('banner') or '')
        self.logo=QPixmap(game.get('logo') or '')
        self.maximum_art_height=maximum_height
        self.setObjectName('recentGameArtwork');self.setFocusPolicy(Qt.StrongFocus);self.setCursor(Qt.PointingHandCursor)
        self.setAccessibleName('Abrir ficha de '+game['title']);self.setMinimumWidth(0)
        self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed)
        if self.pixmap.isNull():self.setFixedHeight(180)
        self.clicked.connect(lambda:window.detail(game['id']))
    def image_target(self):
        if self.pixmap.isNull():return QRectF()
        from PySide6.QtCore import QSizeF
        size=QSizeF(self.pixmap.size()).scaled(QSizeF(self.size()),Qt.KeepAspectRatio)
        return QRectF((self.width()-size.width())/2,(self.height()-size.height())/2,size.width(),size.height())
    def resizeEvent(self,event):
        super().resizeEvent(event)
        height=round(self.width()*self.pixmap.height()/self.pixmap.width()) if not self.pixmap.isNull() else 180
        if self.maximum_art_height is not None:height=min(height,self.maximum_art_height)
        if self.height()!=height:self.setFixedHeight(max(1,height))
    def paintEvent(self,event):
        p=QPainter(self);p.setRenderHint(QPainter.Antialiasing);p.setRenderHint(QPainter.SmoothPixmapTransform)
        from .visual_tokens import RADIUS
        bounds=QRectF(self.rect());clip=QPainterPath();clip.addRoundedRect(bounds,RADIUS['card'],RADIUS['card'])
        p.setClipPath(clip)
        if self.pixmap.isNull():p.fillRect(self.rect(),QColor(colors()['input']))
        if not self.pixmap.isNull():
            target=self.image_target();art_clip=QPainterPath();art_clip.addRoundedRect(target,RADIUS['card'],RADIUS['card'])
            p.setClipPath(art_clip,Qt.IntersectClip)
            p.drawPixmap(target,self.pixmap,QRectF(self.pixmap.rect()))
        elif self.logo.isNull():p.setPen(QColor(colors()['text']));p.drawText(self.rect(),Qt.AlignCenter|Qt.TextWordWrap,self.game['title'])
        if not self.logo.isNull() and (self.art_kind!='cover' or self.pixmap.isNull()):
            logo=self.logo.scaled(max(1,self.width()-24),48,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            p.drawPixmap(12,12,logo)
        p.end()


class RecentGameCard(CardSurface):
    def __init__(self,window,game):
        super().__init__();self.game_id=game['id'];self.session_id=game.get('session_id');self.setObjectName('recentGameCard');self.setMinimumWidth(0)
        self.open_detail=lambda:window.detail(self.game_id)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)
        inside=QVBoxLayout(self);inside.setContentsMargins(8,12,8,12);inside.setSpacing(10)
        inside.setAlignment(Qt.AlignTop)
        inside.addWidget(RecentArtwork(game,window,maximum_height=230))
        play=action('Continuar',lambda:continue_game(window,game),True);play.setProperty('homeContinue',True);play.ensurePolished()
        play.setMinimumWidth(play.sizeHint().width());play.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        inside.addWidget(play)
        title=ElidedAction(game['title'],self.open_detail);title.setObjectName('activityLink');inside.addWidget(title)
        inside.addWidget(SingleLineInfo(display_status(game.get('status')),'muted'))
        inside.addWidget(SingleLineInfo(last_played_text(game['last_played']),tooltip='Última vez: '+datetime_display(game['last_played'])))
        inside.addWidget(SingleLineInfo('Tempo total: '+format_time(game['seconds'])))

    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton and self.rect().contains(event.position().toPoint()):
            self.open_detail();event.accept()
        else:super().mouseReleaseEvent(event)


class OfferBanner(RecentArtwork):
    def __init__(self,game,window):
        super().__init__({**game,'cover':'','logo':''},window)
        self.setObjectName('homeOfferBanner')
        self.steam_identity=None
        if window.isVisible() and window.library.setting('artwork.auto',True):
            from .offer_art import OfferArt,steam_header_identity
            self.steam_identity=steam_header_identity(window.library,game)
            if self.steam_identity:
                if not hasattr(window,'offer_art'):
                    window.offer_art=OfferArt(window.library.db.path.parent,window)
                window.offer_art.available.connect(self.header_available)
                cached=window.offer_art.request(self.steam_identity)
                if cached:self.header_available(self.steam_identity,cached)

    def header_available(self,identity,path):
        if identity!=self.steam_identity:return
        pixmap=QPixmap(path)
        if pixmap.isNull():return
        self.pixmap=pixmap
        self.setFixedHeight(min(42,max(1,round(self.width()*pixmap.height()/pixmap.width()))))
        self.update()
    def sizeHint(self):return QSize(136,40)
    def resizeEvent(self,event):
        if self.pixmap.isNull():
            QPushButton.resizeEvent(self,event)
            self.setFixedHeight(40)
        else:super().resizeEvent(event)


class HomeSectionHeader(QWidget):
    """Título e ação mudam de linha antes de disputar espaço."""
    def __init__(self,title,callback,button):
        super().__init__();self.setMinimumWidth(0)
        self.row=QBoxLayout(QBoxLayout.LeftToRight,self);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(10)
        self.row.setSizeConstraint(QLayout.SetNoConstraint)
        self.title=text(title,'sectionTitle');self.title.setWordWrap(False)
        self.row.addWidget(self.title,1)
        self.control=None
        if callback is not None:
            self.control=action(button,callback);self.control.setProperty('variant','ghost');self.row.addWidget(self.control)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
    def minimumSizeHint(self):return QSize(0,self.sizeHint().height())
    def resizeEvent(self,event):
        super().resizeEvent(event)
        if self.control is None:return
        required=self.title.sizeHint().width()+self.control.sizeHint().width()+self.row.spacing()
        direction=QBoxLayout.TopToBottom if self.width()<required else QBoxLayout.LeftToRight
        if self.row.direction()!=direction:
            self.row.setDirection(direction)
            self.row.setAlignment(self.control,Qt.AlignLeft if direction==QBoxLayout.TopToBottom else Qt.AlignRight)
            self.updateGeometry()


class HomeOfferRow(QWidget):
    def __init__(self,window,game,show_platform=False):
        super().__init__();self.setObjectName('homeOfferRow');self.setMinimumWidth(0)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
        row=QHBoxLayout(self);row.setContentsMargins(0,6,0,6);row.setSpacing(12)
        self.banner=OfferBanner(game,window);self.banner.setFixedWidth(112);self.banner.maximum_art_height=42
        self.banner.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        row.addWidget(self.banner,0,Qt.AlignVCenter)
        words=QVBoxLayout();words.setContentsMargins(0,0,0,0);words.setSpacing(4)
        title=ElidedAction(game['title'],lambda:window.detail(game['id']));title.setObjectName('activityLink');words.addWidget(title)
        quote=game['quote'];offer=quote.get('selected_offer',{})
        origin={'retail':'Loja oficial','keyshop':'Keyshop'}[quote['current_kind']]
        identity=(game.get('platform','')+' · ') if show_platform else ''
        words.addWidget(SingleLineInfo(identity+origin+(' · '+offer['shop'] if offer.get('shop') else ''),'caption'))
        row.addLayout(words,1)
        prices=QVBoxLayout();prices.setSpacing(2)
        from .prices import money
        if quote.get('original') and quote.get('discount'):
            reduction=QHBoxLayout();reduction.setContentsMargins(0,0,0,0);reduction.setSpacing(6)
            original=text(money(quote['original']),'caption');original.setObjectName('homeOfferOriginal');original.setWordWrap(False)
            font=original.font();font.setStrikeOut(True);original.setFont(font);reduction.addWidget(original)
            discount=text('-'+str(quote['discount'])+'%','priceDiscount');discount.setObjectName('homeOfferDiscount');discount.setWordWrap(False)
            discount.setStyleSheet('color: '+window.theme.colors['accent']+'; font-weight: 600;')
            reduction.addWidget(discount);prices.addLayout(reduction)
        from .price_view import source_link
        price=source_link(window.library,game,money(quote['lowest']));price.setProperty('homeOfferPrice',True)
        price.setStyleSheet('color: '+window.theme.colors['accent']+'; font-weight: 600; text-align: right;')
        prices.addWidget(price,0,Qt.AlignRight);row.addLayout(prices)

    def resizeEvent(self,event):
        super().resizeEvent(event)
        self.banner.setFixedWidth(max(64,min(112,event.size().width()-192)))


class GameStrip(QWidget):
    """Quantidade visível acompanha a largura mínima dos controles."""
    def __init__(self,window,games,maximum=8,*,header=None):
        super().__init__();self.setMinimumWidth(0);self.setObjectName('recentGames')
        self.host_window=window;self.games=games;self.maximum=maximum;self.offset=0;self.setFocusPolicy(Qt.StrongFocus)
        self.minimum_tile_width=170
        self.visible_count=max(1,min(maximum,(self.width()+12)//(self.minimum_tile_width+12)))
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
        layout=QVBoxLayout(self);layout.setContentsMargins(0,0,0,0);layout.setSpacing(8)
        if header is None:header=HomeSectionHeader('Últimas sessões',None,'');layout.addWidget(header)
        self.previous=IconButton('chevron-left','Sessões anteriores',lambda:self.move_by(-1));header.row.addWidget(self.previous)
        self.next=IconButton('chevron-right','Próximas sessões',lambda:self.move_by(1));header.row.addWidget(self.next)
        self.body=QWidget();self.body.setMinimumWidth(0)
        self.row=QHBoxLayout(self.body);self.row.setSizeConstraint(QLayout.SetNoConstraint)
        self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(12);layout.addWidget(self.body)
        self.render()
    def minimumSizeHint(self):return QSize(0,super().minimumSizeHint().height())
    def render(self):
        previous={(tile.session_id,tile.game_id):tile for tile in getattr(self,'tiles',[])}
        while self.row.count():
            self.row.takeAt(0)
        self.tiles=[]
        for game in self.games[self.offset:self.offset+self.visible_count]:
            tile=previous.pop((game.get('session_id'),game['id']),None)
            if tile is None:tile=RecentGameCard(self.host_window,game)
            self.tiles.append(tile)
        for tile in previous.values():
            tile.hide();tile.setParent(None);tile.deleteLater()
        for tile in self.tiles:
            tile.setFixedWidth(self.minimum_tile_width);self.row.addWidget(tile,0,Qt.AlignTop)
        self.row.addStretch()
        show_controls=len(self.games)>self.visible_count
        self.previous.setVisible(show_controls);self.next.setVisible(show_controls)
        self.previous.setEnabled(self.offset>0);self.next.setEnabled(self.offset+self.visible_count<len(self.games))
        self.updateGeometry()
    def move_by(self,step):
        self.offset=max(0,min(max(0,len(self.games)-self.visible_count),self.offset+step));self.render()
    def resizeEvent(self,event):
        count=max(1,min(self.maximum,(self.width()+12)//(self.minimum_tile_width+12)))
        if count!=self.visible_count:
            self.visible_count=count;self.offset=min(self.offset,max(0,len(self.games)-count));self.render()
        super().resizeEvent(event)
    def keyPressEvent(self,event):
        if event.key() in (Qt.Key_Left,Qt.Key_Right):self.move_by(-1 if event.key()==Qt.Key_Left else 1);event.accept()
        else:super().keyPressEvent(event)


def open_memory(window,record):
    if record['kind']!='diary':window.show_media(record);return
    from PySide6.QtWidgets import QTextEdit
    from .dialog_style import prepare_dialog
    dialog=prepare_dialog(QDialog(window));dialog.setWindowTitle('Memória de '+record['title']);dialog.resize(520,400)
    layout=QVBoxLayout(dialog);layout.addWidget(text(record['title'],'sectionTitle'))
    content=QTextEdit();content.setReadOnly(True);content.setPlainText(record['text']);layout.addWidget(content)
    layout.addWidget(text(datetime_display(record['created_at']),'caption'))
    def open_game():dialog.accept();window.detail(record['game_id']);window.detail_tabs.setCurrentIndex(2)
    layout.addWidget(action('Abrir jogo',open_game));layout.addWidget(action('Fechar',dialog.reject));dialog.exec()


class MemoryCarousel(CardSurface):
    def __init__(self,window,records):
        super().__init__();self.host_window=window;self.records=records;self.offset=0;self.visible_count=3;self.setObjectName('homeMemories')
        self.setFocusPolicy(Qt.StrongFocus);self.setMinimumWidth(0);self.card_width=300;self.cards=[]
        layout=QVBoxLayout(self);layout.setContentsMargins(16,16,16,16);layout.setSpacing(14)
        head=QHBoxLayout();head.addWidget(text('Memórias recentes','sectionTitle'),1)
        head.addWidget(action('Ver todas',lambda:window.navigate(3)))
        self.previous=IconButton('chevron-left','Memórias anteriores',lambda:self.move_by(-1));head.addWidget(self.previous)
        self.next=IconButton('chevron-right','Próximas memórias',lambda:self.move_by(1));head.addWidget(self.next);layout.addLayout(head)
        self.body=QWidget();self.body.setMinimumWidth(0);self.row=QHBoxLayout(self.body);self.row.setSizeConstraint(QLayout.SetNoConstraint);self.row.setContentsMargins(0,0,0,0);self.row.setSpacing(14);layout.addWidget(self.body)
        self.render()
    def minimumSizeHint(self):return QSize(0,self.sizeHint().height())
    def render(self):
        self.cards=[]
        while self.row.count():
            item=self.row.takeAt(0)
            if item.widget():
                widget=item.widget();widget.hide();widget.setParent(None);widget.deleteLater()
        if not self.records:
            self.row.addWidget(action('Adicionar memória',self.host_window.first_memory,True))
        for record in self.records[self.offset:self.offset+self.visible_count]:
            frame=CardSurface();frame.setObjectName('homeMemoryCard');frame.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred)
            inside=QVBoxLayout(frame);inside.setContentsMargins(12,12,12,12);inside.setSpacing(8)
            callback=lambda checked=False,r=record:open_memory(self.host_window,r)
            if record['kind']=='diary':
                preview=QPushButton();preview.setObjectName('memoryTextPreview');preview.setFixedHeight(160)
                preview.setAccessibleName(record['text']);preview.setToolTip(record['text']);preview.clicked.connect(callback)
                words=QVBoxLayout(preview);words.setContentsMargins(10,10,10,10)
                label=text(record['text'],'bodyText');label.setAlignment(Qt.AlignTop|Qt.AlignLeft)
                label.setAttribute(Qt.WA_TransparentForMouseEvents);label.setMaximumHeight(136);words.addWidget(label,0,Qt.AlignTop);words.setAlignment(Qt.AlignTop)
            else:
                from .memory_artwork import MemoryArtwork,memory_cache
                preview=MemoryArtwork(record['path'],record.get('caption') or 'Abrir captura',callback,memory_cache(self.host_window))
            inside.addWidget(preview)
            title=ElidedAction(record['title'],callback);title.setObjectName('activityLink');inside.addWidget(title)
            inside.addWidget(text('Diário' if record['kind']=='diary' else 'Vídeo' if record['kind']=='video' else 'Captura','caption'))
            inside.addWidget(text(datetime_display(record['created_at']),'caption'));frame.setFixedWidth(min(self.card_width,max(1,self.width()-32)));self.cards.append(frame);self.row.addWidget(frame);frame.show()
        self.row.addStretch()
        self.previous.setEnabled(self.offset>0);self.next.setEnabled(self.offset+self.visible_count<len(self.records))
    def move_by(self,step):
        self.offset=max(0,min(max(0,len(self.records)-self.visible_count),self.offset+step));self.render()
    def keyPressEvent(self,event):
        if event.key() in (Qt.Key_Left,Qt.Key_Right):self.move_by(-1 if event.key()==Qt.Key_Left else 1);event.accept()
        else:super().keyPressEvent(event)
    def resizeEvent(self,event):
        count=max(1,min(8,(self.width()-32+14)//(self.card_width+14)))
        if count!=self.visible_count:
            self.visible_count=count;self.offset=min(self.offset,max(0,len(self.records)-count));self.render()
        for frame in self.cards:frame.setFixedWidth(min(self.card_width,max(1,self.width()-32)))
        super().resizeEvent(event)


def show_execution_history(window):
    from .home_data import execution_history
    from .dialog_style import prepare_dialog
    dialog=prepare_dialog(QDialog(window));dialog.setWindowTitle('Histórico de execuções');dialog.resize(650,500)
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

"""Cards de resultado: pintura apenas; seleção e consulta permanecem no QuickAdd."""
import weakref
from PySide6.QtCore import Qt,QSize,QRectF
from PySide6.QtGui import QFont,QPixmap,QColor,QPainterPath,QPen,QPainter
from PySide6.QtWidgets import QStyledItemDelegate,QStyle
from .cover_art import CoverArtwork
from .theme import get_theme
from .visual_tokens import SPACE,TYPE,RADIUS


class CatalogResultDelegate(QStyledItemDelegate):
    def __init__(self,quick,parent=None):
        super().__init__(parent);self.quick_ref=weakref.ref(quick)
    def sizeHint(self,option,index):return QSize(0,96)
    def paint(self,painter,option,index):
        quick=self.quick_ref()
        if quick is None:return
        from PySide6.QtWidgets import QApplication
        from .integrations.drive import normalize_rom_name
        colors=get_theme(QApplication.instance().property('checkpointTheme')).colors
        row=index.row();pix=QPixmap();original=''
        if row<len(quick.local):
            record=quick.local[row];title=normalize_rom_name(record['original_name'])
            platform=record.get('platform') or 'Plataforma a revisar'
            status='Baixada' if record.get('available') else 'Vinculada' if record.get('game_id') else 'Disponível no Drive'
            original=record['original_name']
            if not record.get('available') and record.get('review_state') in ('remote_removed','remote_missing','outside_root'):status='Indisponível'
            if record.get('game_id'):
                game=quick.library.get(record['game_id']) or {};pix=QPixmap(game.get('cover') or '')
        elif row-len(quick.local)<len(quick.candidates):
            result=quick.candidates[row-len(quick.local)];title=result.title
            platform=' / '.join(result.platforms[:2]) or 'Plataforma não informada'
            status={'rawg':'RAWG','steam':'Steam','steamgriddb':'SteamGridDB'}.get(result.provider,'Catálogo')
            original=result.developer or 'Selecione para carregar a ficha e as imagens.'
            match=quick.library.sql.execute('SELECT g.cover FROM games g JOIN external_identifiers e ON e.game_id=g.id WHERE e.provider=? AND e.external_id=?',(result.provider,result.external_id)).fetchone()
            if match:pix=QPixmap(match[0] or '')
        else:
            title=index.data(Qt.DisplayRole) or '';platform='';status='';original=''
        selected=bool(option.state & QStyle.State_Selected)
        painter.save();painter.setRenderHint(QPainter.Antialiasing);rect=QRectF(option.rect).adjusted(0,0,-1,-SPACE['xxs'])
        painter.setClipRect(rect);painter.setPen(QPen(QColor(colors['accent'] if selected else colors['border_subtle']),1))
        painter.setBrush(QColor(colors['selected'] if selected else colors['card']))
        painter.drawRoundedRect(rect,RADIUS['card'],RADIUS['card'])
        art=QRectF(rect.left()+SPACE['sm'],rect.top()+SPACE['sm'],48,68)
        CoverArtwork.paint_art(painter,art,pix,'Sem capa',colors,False)
        left=art.right()+SPACE['md'];width=max(1,rect.right()-left-SPACE['md'])
        font=QFont('Segoe UI');font.setPixelSize(TYPE['body']);font.setWeight(QFont.DemiBold)
        painter.setFont(font);painter.setPen(QColor(colors['text']))
        painter.drawText(QRectF(left,rect.top()+12,width-24,24),Qt.AlignVCenter,painter.fontMetrics().elidedText(title,Qt.ElideRight,int(width-24)))
        if selected:
            painter.setPen(QColor(colors['accent']));painter.drawText(QRectF(rect.right()-32,rect.top()+12,24,24),Qt.AlignCenter,'✓')
        font.setPixelSize(TYPE['caption']);font.setWeight(QFont.Normal);painter.setFont(font)
        badge_width=min(width/2,painter.fontMetrics().horizontalAdvance(status)+16)
        badge=QRectF(rect.right()-SPACE['sm']-badge_width,rect.top()+40,badge_width,22)
        painter.setBrush(QColor(colors['surface']));painter.setPen(Qt.NoPen);painter.drawRoundedRect(badge,RADIUS['button'],RADIUS['button'])
        painter.setPen(QColor(colors['secondary']));painter.drawText(badge,Qt.AlignCenter,status)
        painter.setPen(QColor(colors['accent']));painter.drawText(QRectF(left,rect.top()+40,max(0,width-badge_width-12),22),Qt.AlignVCenter,painter.fontMetrics().elidedText(platform,Qt.ElideRight,int(max(0,width-badge_width-12))))
        painter.setPen(QColor(colors['muted']));painter.drawText(QRectF(left,rect.top()+66,width,18),Qt.AlignVCenter,painter.fontMetrics().elidedText(original,Qt.ElideRight,int(width)))
        painter.restore()


from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QFrame,QVBoxLayout


class ResultEmptyOverlay(QFrame):
    """Estado desenhado sobre a lista vazia; não intercepta eventos de seleção."""
    def __init__(self,quick):
        super().__init__(quick.results.viewport());self.quick_ref=weakref.ref(quick)
        self.setObjectName('resultEmptyState');self.setAttribute(Qt.WA_TransparentForMouseEvents)
        from .ui_components import text
        from .design_system import Badge
        layout=QVBoxLayout(self);layout.setContentsMargins(*([SPACE['md']]*4));layout.setSpacing(SPACE['xs'])
        layout.addWidget(Badge('folder',32),0,Qt.AlignHCenter)
        title=text('Nenhuma ROM no índice','cardTitle');title.setAlignment(Qt.AlignCenter);layout.addWidget(title)
        description=text('Atualize o índice do Drive ou pesquise um jogo na primeira aba.','emptyDescription')
        description.setAlignment(Qt.AlignCenter);layout.addWidget(description)
        quick.results.viewport().installEventFilter(self)
        quick.sources.currentChanged.connect(self.sync)
        quick.results.model().rowsInserted.connect(self.sync)
        quick.results.model().rowsRemoved.connect(self.sync)
        quick.results.model().modelReset.connect(self.sync)
        self.sync()
    def sync(self,*args):
        quick=self.quick_ref()
        if quick is None:return
        self.setGeometry(quick.results.viewport().rect())
        self.setVisible(quick.sources.currentIndex()==1 and quick.results.count()==0)
    def eventFilter(self,watched,event):
        if event.type()==QEvent.Resize:self.sync()
        return False

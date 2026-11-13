"""Comparação em reais e atribuição/link permanente para a página GG.deals."""
from urllib.parse import urlencode
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QSizePolicy
from PySide6.QtGui import QFont,QFontMetrics
from .ui_components import text,action,card
from .prices import snapshot,money
from .visual_tokens import SPACE,TYPE
from .locale import datetime_display,date_display


def source_url(library,game):
    value=snapshot(library,game['id'])
    if value.get('url'):return value['url']
    steam=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone()
    return f'https://gg.deals/br/steam/app/{steam[0]}/' if steam else 'https://gg.deals/br/games/?'+urlencode({'title':game['title']})


def source_link(library,game,label='Ver ofertas ↗'):
    url=source_url(library,game);link=action(label,lambda:QDesktopServices.openUrl(QUrl(url)));link.setObjectName('quiet');link.setToolTip(url);return link


def attribution_link():
    label=QLabel('<a href="https://gg.deals/">Preços: GG.deals</a>');label.setObjectName('ggdealsAttribution');label.setTextFormat(Qt.RichText);label.setTextInteractionFlags(Qt.TextBrowserInteraction);label.setOpenExternalLinks(True);label.setAccessibleName('Preços: GG.deals');return label


def has_steam_id(library,game):
    return library.sql.execute("SELECT 1 FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone() is not None


def display_snapshot(library,game):
    value=snapshot(library,game['id'])
    return value if value.get('currency','BRL')=='BRL' else {}


class PriceAmount(QLabel):
    def __init__(self,value):
        super().__init__(value);self.setObjectName('priceValue');self.setFixedHeight(32)
        self.setMinimumWidth(0);self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed)
    def resizeEvent(self,event):
        super().resizeEvent(event);font=QFont(self.font());size=24
        font.setPixelSize(size)
        while size>16 and QFontMetrics(font).horizontalAdvance(self.text())>self.width():
            size-=1;font.setPixelSize(size)
        self.setStyleSheet('font-size: '+str(size)+'px; font-weight: 600;')


def price_summary(library,game):
    value=display_snapshot(library,game);frame=QWidget();frame.setFixedHeight(132);row=QVBoxLayout(frame);row.setContentsMargins(0,0,0,0);row.setSpacing(SPACE['xxs'])
    current=value.get('lowest');usable=type(current) is int and current>0 and value.get('currency','BRL')=='BRL'
    stale=value.get('state') in ('unavailable','missing_steam_id') and usable
    label=text('Último preço salvo' if stale else 'Menor preço atual','caption');label.setWordWrap(False);row.addWidget(label)
    amount=PriceAmount(money(current) if usable else 'Indisponível');row.addWidget(amount)
    kind={'retail':'Loja oficial','keyshop':'Keyshop'}.get(value.get('current_kind'))
    if kind and usable:
        offers=[offer for offer in value.get('offers',[]) if offer.get('cents')==current]
        shop=offers[0].get('shop','') if offers else ''
        label=text(kind+(' · '+shop if shop else ''),'secondary');label.setToolTip(label.text());row.addWidget(label)
    original=value.get('original');discount=value.get('discount')
    if value.get('provider')!='api' and usable and type(original) is int and original>current and discount:
        detail=QHBoxLayout();before=text(money(original),'caption');font=before.font();font.setStrikeOut(True);before.setFont(font);detail.addWidget(before)
        badge=text('-'+str(discount)+'%','discountBadge');detail.addWidget(badge);detail.addStretch();row.addLayout(detail)
    historical=value.get('historical')
    if type(historical) is int and historical>0:row.addWidget(text('Menor histórico: '+money(historical),'caption'))
    if not has_steam_id(library,game):row.addWidget(text('Sem ID da Steam para consulta','caption'))
    row.addStretch()
    if value.get('checked_at'):
        stamp='Última consulta: '+datetime_display(value['checked_at']);frame.setToolTip(stamp);frame.setAccessibleDescription(stamp)
    return frame


def comparison(window,game):
    value=display_snapshot(window.library,game);frame,inside=card();head=QHBoxLayout();head.addWidget(text('Últimos preços consultados' if value.get('state') in ('unavailable','missing_steam_id') else 'Preços atuais','sectionTitle'));head.addStretch();head.addWidget(source_link(window.library,game,'Abrir comparação ↗'));inside.addLayout(head);inside.addWidget(attribution_link(),0,Qt.AlignLeft)
    if not has_steam_id(window.library,game):inside.addWidget(text('Sem ID da Steam para consulta','caption'))
    if type(value.get('historical')) is int and value['historical']>0:inside.addWidget(text('Menor histórico: '+money(value['historical']),'muted'))
    for kind,title,key,anchor in [('retail','Lojas oficiais','retail','official-stores'),('keyshop','Lojas de chaves','keyshop','keyshops')]:
        row=QHBoxLayout();row.addWidget(text(title,'cardTitle'));row.addStretch();row.addWidget(text(money(value.get(key)),'cardTitle'));inside.addLayout(row)
        offers=[offer for offer in value.get('offers',[]) if offer['kind']==kind]
        for offer in offers[:8]:
            row=QHBoxLayout();row.addWidget(text(offer['shop']+(' · '+offer['drm'] if offer.get('drm') else ''),'muted'),1)
            link=action(money(offer['cents'])+' ↗',lambda checked=False,url=offer['url']:QDesktopServices.openUrl(QUrl(url)));link.setObjectName('quiet');row.addWidget(link);inside.addLayout(row)
    if value.get('checked_at'):inside.addWidget(text('Consultado em '+datetime_display(value['checked_at'])+' · BRL','caption'))
    if value.get('state')=='unavailable':inside.addWidget(text('Consulta indisponível agora. Abra a comparação para conferir as ofertas completas.','muted'))
    elif not value:inside.addWidget(text('As ofertas serão consultadas quando a página deste jogo estiver identificada.','muted'))
    inside.addWidget(source_link(window.library,game,'Ver todas as ofertas ↗'),0,Qt.AlignLeft)
    return frame

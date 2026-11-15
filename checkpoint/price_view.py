"""Comparação em reais e atribuição/link permanente para a página GG.deals."""
from urllib.parse import urlencode
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QSizePolicy
from PySide6.QtGui import QFont,QFontMetrics
from .ui_components import text,action,card
from .prices import snapshot,money,selected_quote
from .visual_tokens import SPACE,TYPE
from .locale import datetime_display,date_display


def source_url(library,game):
    value=snapshot(library,game['id'])
    from .prices import platform_problem
    if platform_problem(game):return 'https://gg.deals/br/games/?'+urlencode({'title':game['title']+' '+game.get('platform','')})
    if value.get('url') and selected_quote(library,game['id']).get('state')!='identity_mismatch':return value['url']
    steam=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone()
    return f'https://gg.deals/br/steam/app/{steam[0]}/' if steam else 'https://gg.deals/br/games/?'+urlencode({'title':game['title']})


def source_link(library,game,label='Ver ofertas ↗'):
    url=source_url(library,game);link=action(label,lambda:QDesktopServices.openUrl(QUrl(url)));link.setObjectName('quiet');link.setToolTip(url);return link


def attribution_link():
    label=QLabel('<a href="https://gg.deals/">Preços: GG.deals</a>');label.setObjectName('ggdealsAttribution');label.setTextFormat(Qt.RichText);label.setTextInteractionFlags(Qt.TextBrowserInteraction);label.setOpenExternalLinks(True);label.setAccessibleName('Preços: GG.deals');return label


def has_steam_id(library,game):
    return library.sql.execute("SELECT 1 FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone() is not None


def display_snapshot(library,game):
    return selected_quote(library,game['id'])


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
    amount=PriceAmount(money(current) if usable else '-');row.addWidget(amount)
    if not usable:row.addWidget(text(value.get('message') or ('Preços ainda não consultados.' if has_steam_id(library,game) else 'Sem ID da Steam para consultar ofertas.'),'caption'))
    kind={'retail':'Loja oficial','keyshop':'Keyshop'}.get(value.get('current_kind'))
    if kind and usable:
        shop=value.get('selected_offer',{}).get('shop','')
        label=text(kind+(' · '+shop if shop else ''),'secondary');label.setToolTip(label.text());row.addWidget(label)
    if usable and value.get('original') and value.get('discount'):
        discount=QHBoxLayout();original=text(money(value['original']),'caption');font=original.font();font.setStrikeOut(True);original.setFont(font);discount.addWidget(original);discount.addWidget(text('-'+str(value['discount'])+'%','priceDiscount'));discount.addStretch();row.addLayout(discount)
    historical=value.get('historical')
    if type(historical) is int and historical>0:row.addWidget(text('Menor histórico: '+money(historical),'caption'))
    if not has_steam_id(library,game) and usable:row.addWidget(text('Sem ID da Steam para consulta','caption'))
    row.addStretch()
    if value.get('checked_at'):
        stamp='Última consulta: '+datetime_display(value['checked_at']);frame.setToolTip(stamp);frame.setAccessibleDescription(stamp)
    return frame


def comparison(window,game):
    value=display_snapshot(window.library,game);frame,inside=card();head=QHBoxLayout();head.addWidget(text('Últimos preços consultados' if value.get('state') in ('unavailable','missing_steam_id') else 'Preços atuais','sectionTitle'));head.addStretch();head.addWidget(source_link(window.library,game,'Abrir comparação ↗'));inside.addLayout(head);inside.addWidget(attribution_link(),0,Qt.AlignLeft)
    inside.addWidget(price_summary(window.library,game))
    kinds=[('retail','Lojas oficiais')]
    if window.library.setting('prices.include_keyshops',False):kinds.append(('keyshop','Lojas de chaves'))
    for kind,title in kinds:
        amount=value.get(kind)
        if type(amount) is not int or amount<=0:continue
        row=QHBoxLayout();row.addWidget(text(title,'cardTitle'));row.addStretch();row.addWidget(text(money(amount),'cardTitle'));inside.addLayout(row)
        offers=[offer for offer in value.get('offers',[]) if offer.get('kind')==kind]
        for offer in offers[:8]:
            row=QHBoxLayout();row.addWidget(text(offer['shop']+(' · '+offer['drm'] if offer.get('drm') else ''),'muted'),1)
            link=action(money(offer['cents'])+' ↗',lambda checked=False,url=offer['url']:QDesktopServices.openUrl(QUrl(url)));link.setObjectName('quiet');row.addWidget(link);inside.addLayout(row)
    if value.get('checked_at'):inside.addWidget(text('Consultado em '+datetime_display(value['checked_at'])+' · BRL','caption'))
    if value.get('state')=='unavailable' and value.get('lowest'):inside.addWidget(text(value.get('message') or 'Falha na consulta. Último preço salvo preservado.','muted'))
    inside.addWidget(source_link(window.library,game,'Ver todas as ofertas ↗'),0,Qt.AlignLeft)
    return frame

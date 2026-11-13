"""Comparação em reais e atribuição/link permanente para a página GG.deals."""
from urllib.parse import urlencode
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout
from .ui_components import text,action,card
from .prices import snapshot,money
from .locale import datetime_display,date_display


def source_url(library,game):
    value=snapshot(library,game['id'])
    if value.get('url'):return value['url']
    steam=library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone()
    return f'https://gg.deals/br/steam/app/{steam[0]}/' if steam else 'https://gg.deals/br/games/?'+urlencode({'title':game['title']})


def source_link(library,game,label='Ver ofertas ↗'):
    url=source_url(library,game);link=action(label,lambda:QDesktopServices.openUrl(QUrl(url)));link.setObjectName('quiet');link.setToolTip(url);return link


def price_summary(library,game):
    value=snapshot(library,game['id']);frame=QWidget();frame.setFixedHeight(66);row=QVBoxLayout(frame);row.setContentsMargins(0,0,0,0);row.setSpacing(2)
    label=text('Último preço salvo' if value.get('state')=='unavailable' and value.get('lowest') is not None else 'Menor preço atual','caption');label.setWordWrap(False);row.addWidget(label)
    current=value.get('lowest');usable=isinstance(current,int) and current>0
    prices=QHBoxLayout();prices.setSpacing(5)
    amount=text(money(current) if usable else 'Indisponível','cardTitle');amount.setWordWrap(False);prices.addWidget(amount);prices.addStretch();row.addLayout(prices)
    original=value.get('original');discount=value.get('discount')
    if usable and isinstance(original,int) and original>current and discount:
        detail=QHBoxLayout();before=text(money(original),'caption');font=before.font();font.setStrikeOut(True);before.setFont(font);detail.addWidget(before)
        badge=text('-'+str(discount)+'%','selectedCheck');detail.addWidget(badge);detail.addStretch();row.addLayout(detail)
    if value.get('checked_at'):
        stamp='Última consulta: '+datetime_display(value['checked_at']);frame.setToolTip(stamp);frame.setAccessibleDescription(stamp)
    return frame


def comparison(window,game):
    value=snapshot(window.library,game['id']);frame,inside=card();head=QHBoxLayout();head.addWidget(text('Últimos preços consultados' if value.get('state')=='unavailable' else 'Preços atuais','sectionTitle'));head.addStretch();head.addWidget(source_link(window.library,game,'Abrir comparação ↗'));inside.addLayout(head)
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

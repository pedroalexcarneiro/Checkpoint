from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QLabel,QPushButton
from checkpoint.collection_views import WishCard
from test_bugs_0134 import ui,sample


def test_offer_link_follows_discount_without_large_fixed_gap(ui,app):
    w,i=ui
    with w.library.sql:
        w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
    w.library.set_setting(f'prices.ggdeals.{i}',{'state':'ready','currency':'BRL','retail':3000,'offer_context':{'platform':'PC','steam':str(i)},'offers':[{'cents':3000,'original':6000,'kind':'retail','shop':'Loja teste','url':'https://gg.deals/br/redirect/test/'}]})
    for size in ((1280,800),(1920,1080)):
        w.resize(*size);w.navigate(2)
        for _ in range(7):app.processEvents()
        card=w.pages[2].findChild(WishCard)
        discount=card.findChild(QLabel,'priceDiscount')
        link=next(b for b in card.findChildren(QPushButton) if b.text().startswith('Ver ofertas'))
        bottom=discount.mapTo(card,discount.rect().bottomLeft()).y();top=link.mapTo(card,QPoint()).y()
        assert 0<=top-bottom<=28
        assert card.rect().contains(link.geometry().translated(link.parentWidget().mapTo(card,QPoint())))

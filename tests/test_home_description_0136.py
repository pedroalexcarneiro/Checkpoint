from checkpoint.ui_components import Hero
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QPushButton


def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
    w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
    w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
    w.navigate(0);app.processEvents();hero=w.pages[0].findChild(Hero)
    assert hero and hero.findChildren(QPushButton)
    before=hero.grab().toImage();hero.game={**hero.game,'description':''};hero.update();app.processEvents()
    assert before==hero.grab().toImage()
    assert w.library.get(i)['description']==description
    w.detail(i);app.processEvents()
    assert any(l.text()==description for l in w.detail_page.findChildren(QLabel))

from checkpoint.home_components import LastPlayedBanner
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel


def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
    w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
    w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
    from datetime import datetime,timezone
    with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(i,datetime.now(timezone.utc).isoformat()))
    w.navigate(0);app.processEvents();hero=w.pages[0].findChild(LastPlayedBanner)
    assert hero and hero.play_button
    for _ in range(6):app.processEvents()
    assert w.library.get(i)['description']==description
    hero.clearFocus();before=hero.grab().toImage()
    w.library.save_game({'title':game['title'],'description':''},i)
    w.navigate(0)
    for _ in range(6):app.processEvents()
    new_hero=w.pages[0].findChild(LastPlayedBanner);new_hero.clearFocus()
    assert before==new_hero.grab().toImage()
    w.library.save_game({'title':game['title'],'description':description},i)
    w.detail(i);app.processEvents()
    assert any(l.text()==description for l in w.detail_page.findChildren(QLabel))

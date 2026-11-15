from datetime import datetime,timedelta,timezone
from PySide6.QtCore import Qt,QPoint
from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QComboBox
from PySide6.QtTest import QTest
from checkpoint.home_components import RecentArtwork,RecentGameCard,MemoryCarousel
from test_bugs_0134 import ui,sample


def seed_recent(w,i):
    j=w.library.save_game({'title':'Segundo jogo','platform':'GBA','status':'Concluído'})
    start=datetime.now(timezone.utc)-timedelta(hours=2)
    with w.library.sql:
        for identity in (i,j):
            w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?, 'finished',?)",(identity,start.isoformat(),(start+timedelta(minutes=30)).isoformat(),1800,100+identity))
    return j


def test_home_actions_are_distinct_and_week_opens_correct_period(ui,app,monkeypatch):
    w,i=ui;j=seed_recent(w,i);calls=[]
    monkeypatch.setattr(w,'detail',lambda identity:calls.append(('detail',identity)))
    monkeypatch.setattr(w,'edit_game',lambda identity:calls.append(('setup',identity)))
    w.navigate(0);app.processEvents()
    cards=w.pages[0].findChildren(RecentGameCard);assert {c.game_id for c in cards}=={i,j}
    first=next(c for c in cards if c.game_id==i)
    QTest.mouseClick(first.findChild(RecentArtwork),Qt.LeftButton);assert calls==[('detail',i)]
    play=next(b for b in first.findChildren(QPushButton) if b.property('homeContinue'))
    play.click();assert calls==[('detail',i),('setup',i)]
    button=next(b for b in w.pages[0].findChildren(QPushButton) if b.text()=='Ver estatísticas')
    button.click();assert w.current_page==4
    assert w.pages[4].findChild(QComboBox,'statisticsPeriod').currentData()=='weekly'


def test_home_columns_share_base_and_art_is_contained(ui,app):
    w,i=ui;seed_recent(w,i)
    for size in ((1280,800),(1920,1080),(1000,700)):
        w.resize(*size);w.navigate(0)
        for _ in range(8):app.processEvents()
        page=w.pages[0];left=page.findChild(QWidget,'homeRecentSection');offers=page.findChild(QWidget,'homeWishOffers')
        if size[0]>=1280:
            a=left.mapTo(page,left.rect().bottomLeft()).y();b=offers.mapTo(page,offers.rect().bottomLeft()).y()
            assert abs(a-b)<=2
        for art in page.findChildren(RecentArtwork):
            if not art.pixmap.isNull():assert art.rect().contains(art.image_target().toAlignedRect())
        assert any(l.text()=='Ofertas' for l in page.findChildren(QLabel))
        assert not any(l.text()=='Ofertas dos desejos' for l in page.findChildren(QLabel))
        from checkpoint.home_components import SingleLineInfo
        for card in page.findChildren(RecentGameCard):
            info=card.findChildren(SingleLineInfo);assert len(info)==3
            assert all(not label.wordWrap() and '\n' not in label.text() for label in info)
            assert info[0].full_text in ('Não iniciado','Jogando','Pausado','Concluído','Abandonado')
            assert info[1].full_text.startswith('Última vez:') and info[1].toolTip()
            assert info[2].full_text.startswith('Tempo total:')


def test_memory_carousel_bounds_keyboard_and_no_data_changes(ui,app):
    w,i=ui
    for n in range(6):w.library.add_diary(i,f'Nota própria {n}')
    before=[tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
    w.navigate(0);app.processEvents();carousel=w.pages[0].findChild(MemoryCarousel)
    assert not carousel.previous.isEnabled() and carousel.next.isEnabled()
    carousel.setFocus();QTest.keyClick(carousel,Qt.Key_Right);assert carousel.offset==1
    for _ in range(10):carousel.next.click()
    assert not carousel.next.isEnabled()
    for _ in range(10):carousel.previous.click()
    assert carousel.offset==0 and not carousel.previous.isEnabled()
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]==before


def test_status_change_does_not_create_recent_card(ui,app):
    w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'status':'Jogando'},i)
    w.navigate(0);app.processEvents()
    assert not w.pages[0].findChildren(RecentGameCard)
    assert any(l.text()=='Nenhuma execução registrada' for l in w.pages[0].findChildren(QLabel))


def test_three_recent_games_carousel_preserves_every_cover_edge(ui,app,folder):
    from PySide6.QtGui import QImage,QColor,QPainter
    from checkpoint.home_components import GameStrip
    w,i=ui;identities=[i]
    for title in ('Hades','Celeste','Metroid Fusion'):
        identities.append(w.library.save_game({'title':title,'platform':'PC'}))
    for n,identity in enumerate(identities):
        image=QImage(200,300,QImage.Format_RGB32);image.fill(QColor('blue'));p=QPainter(image)
        p.fillRect(0,0,200,12,QColor('yellow'));p.fillRect(0,288,200,12,QColor('magenta'))
        p.fillRect(0,12,12,276,QColor('cyan'));p.fillRect(188,12,12,276,QColor('red'));p.end()
        path=folder/f'cover-{n}.png';assert image.save(str(path))
        w.library.save_game({'title':w.library.get(identity)['title'],'cover':str(path)},identity)
        with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'finished',?)",(identity,(datetime.now(timezone.utc)-timedelta(hours=n+1)).isoformat(),100+n))
    for size in ((1280,800),(1920,1080)):
        w.resize(*size);w.navigate(0)
        for _ in range(8):app.processEvents()
        strip=w.pages[0].findChild(GameStrip);assert len(strip.tiles)==3
        assert not strip.previous.isEnabled() and strip.next.isEnabled()
        for card in strip.tiles:
            art=card.findChild(RecentArtwork);target=art.image_target()
            assert abs(target.width()-art.width())<=1 and abs(target.height()-art.height())<=1
            frame=art.grab().toImage();x=art.width()//2;y=art.height()//2
            top=frame.pixelColor(x,1);bottom=frame.pixelColor(x,art.height()-2)
            left=frame.pixelColor(1,y);right=frame.pixelColor(art.width()-2,y)
            assert top.red()>top.blue() and top.green()>top.blue()
            assert bottom.red()>bottom.green() and bottom.blue()>bottom.green()
            assert left.blue()>left.red() and left.green()>left.red()
            assert right.red()>right.green() and right.red()>right.blue()
        strip.setFocus();QTest.keyClick(strip,Qt.Key_Right);app.processEvents()
        assert strip.offset==1 and not strip.next.isEnabled()
        assert [c.game_id for c in strip.tiles]==identities[1:]


def test_offers_show_only_same_offer_original_discount_and_current(ui,app):
    from checkpoint.home_data import wish_offers
    w,i=ui
    with w.library.sql:
        w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam','620')",(i,))
    w.library.set_setting(f'prices.ggdeals.{i}',{'state':'ready','retail':3000,'currency':'BRL',
        'offer_context':{'steam':'620','platform':'PC'},'offers':[{'cents':3000,'original':6000,'kind':'retail','shop':'Loja teste','url':'https://gg.deals/br/redirect/test/'}]})
    w.navigate(0);app.processEvents();frame=w.pages[0].findChild(QWidget,'homeWishOffers')
    assert frame.findChild(QLabel,'homeOfferOriginal').text()=='R$ 60,00'
    assert frame.findChild(QLabel,'homeOfferOriginal').font().strikeOut()
    assert frame.findChild(QLabel,'homeOfferDiscount').text()=='-50%'
    assert not frame.findChildren(QWidget,'homeOfferLogo')
    assert not any(label.text().startswith('PC') for label in frame.findChildren(QLabel))
    assert wish_offers(w.library)[0]['quote']['lowest']==3000


def test_offer_banner_uses_entire_banner_instead_of_cover(ui,app,folder):
    from checkpoint.home_components import OfferBanner
    from PySide6.QtGui import QImage,QColor,QPainter
    w,i=ui;image=QImage(1200,320,QImage.Format_RGB32);image.fill(QColor('blue'));p=QPainter(image)
    p.fillRect(0,0,1200,20,QColor('yellow'));p.fillRect(0,300,1200,20,QColor('magenta'))
    p.fillRect(0,20,20,280,QColor('cyan'));p.fillRect(1180,20,20,280,QColor('red'));p.end()
    path=folder/'banner.png';assert image.save(str(path))
    art=OfferBanner({**w.library.get(i),'banner':str(path),'cover':'capa-que-nao-deve-ser-usada.png'},w);art.show()
    try:
        for width in (300,480,680,300):
            art.resize(width,art.height())
            for _ in range(6):app.processEvents()
            assert abs(art.width()/art.height()-1200/320)<.03
            frame=art.grab().toImage();x=art.width()//2;y=art.height()//2
            assert frame.pixelColor(x,1).green()>200 and frame.pixelColor(x,1).red()>200
            assert frame.pixelColor(x,art.height()-2).blue()>200 and frame.pixelColor(x,art.height()-2).red()>200
            assert frame.pixelColor(1,y).green()>200 and frame.pixelColor(1,y).blue()>200
            assert frame.pixelColor(art.width()-2,y).red()>200 and frame.pixelColor(art.width()-2,y).green()<20
    finally:art.close()

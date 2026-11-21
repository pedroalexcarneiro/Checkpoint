from datetime import datetime,timedelta,timezone
from PySide6.QtCore import Qt,QPoint
from PySide6.QtWidgets import QWidget,QPushButton,QLabel
from PySide6.QtTest import QTest
from checkpoint.home_components import LastPlayedBanner,RecentArtwork,RecentGameCard,MemoryCarousel
from test_bugs_0134 import ui,sample


def seed_recent(w,i):
    j=w.library.save_game({'title':'Segundo jogo','platform':'GBA','status':'Concluído'})
    start=datetime.now(timezone.utc)-timedelta(hours=2)
    with w.library.sql:
        for identity in (i,j):
            w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?, 'finished',?)",(identity,start.isoformat(),(start+timedelta(minutes=30)).isoformat(),1800,100+identity))
    return j


def test_home_actions_are_distinct_and_week_summary_has_no_second_heading_line(ui,app,monkeypatch):
    w,i=ui;j=seed_recent(w,i);calls=[]
    monkeypatch.setattr(w,'detail',lambda identity:calls.append(('detail',identity)))
    monkeypatch.setattr(w,'edit_game',lambda identity:calls.append(('setup',identity)))
    w.navigate(0);app.processEvents()
    banner=w.pages[0].findChild(LastPlayedBanner);assert banner.game_id==j
    cards=w.pages[0].findChildren(RecentGameCard);assert {c.game_id for c in cards}=={i}
    first=next(c for c in cards if c.game_id==i)
    QTest.mouseClick(first.findChild(RecentArtwork),Qt.LeftButton);assert calls==[('detail',i)]
    play=next(b for b in first.findChildren(QPushButton) if b.property('homeContinue'))
    play.click();assert calls==[('detail',i),('setup',i)]
    QTest.mouseClick(banner,Qt.LeftButton);assert calls[-1]==('detail',j)
    QTest.mouseClick(banner.play_button,Qt.LeftButton)
    assert calls==[('detail',i),('setup',i),('detail',j),('setup',j)]
    summary=w.pages[0].findChild(QWidget,'homeWeekSummary')
    assert not summary.findChildren(QPushButton)
    w.nav_buttons[4].click();assert w.current_page==4


def test_home_columns_align_top_and_art_is_contained(ui,app):
    w,i=ui;seed_recent(w,i)
    for size in ((1280,800),(1920,1080),(1000,700)):
        w.resize(*size);w.navigate(0)
        for _ in range(8):app.processEvents()
        page=w.pages[0];left=page.findChild(QWidget,'homeRecentSection');offers=page.findChild(QWidget,'homeWishOffers')
        summary=page.findChild(QWidget,'homeWeekSummary')
        left_origin=left.mapTo(page,QPoint());summary_origin=summary.mapTo(page,QPoint())
        offers_origin=offers.mapTo(page,QPoint())
        assert abs(left_origin.y()-summary_origin.y())<=2
        assert left_origin.x()+left.width()<summary_origin.x()==offers_origin.x()
        assert summary_origin.y()+summary.height()<offers_origin.y()
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
    track=carousel.track;bar=track.horizontalScrollBar();cards=carousel.cards.copy()
    viewport=track.viewport()
    assert any(card.mapTo(viewport,QPoint()).x()<viewport.width()<card.mapTo(viewport,QPoint()).x()+card.width() for card in cards)
    carousel.setFocus();QTest.keyClick(carousel,Qt.Key_Right)
    assert track.destination()==track.stride
    track.animation.setCurrentTime(track.animation.duration()//2)
    assert 0<bar.value()<track.stride and carousel.cards==cards
    track.animation.setCurrentTime(track.animation.duration())
    for _ in range(10):carousel.next.click()
    track.animation.setCurrentTime(track.animation.duration())
    assert not carousel.next.isEnabled()
    for _ in range(10):carousel.previous.click()
    track.animation.setCurrentTime(track.animation.duration())
    assert bar.value()==0 and not carousel.previous.isEnabled()
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]==before


def test_recent_memories_fill_panel_with_two_centered_standard_cards(ui,app):
    from PySide6.QtWidgets import QScrollArea
    w,game=ui
    for note in ('Primeira nota','Segunda nota'):w.library.add_diary(game,note)
    w.resize(1280,800);w.navigate(0)
    for _ in range(8):app.processEvents()
    page=w.pages[0];carousel=page.findChild(MemoryCarousel)
    assert [card.width() for card in carousel.cards]==[300,300]
    body=page.findChild(QScrollArea,'homeScroll').widget()
    assert carousel.width()==body.width()-body.layout().contentsMargins().right()
    assert carousel.mapTo(page,QPoint()).x()==page.findChild(QWidget,'homeRecentSection').mapTo(page,QPoint()).x()
    first,last=carousel.cards
    assert abs(first.x()-(carousel.track.body.width()-last.geometry().right()-1))<=1
    assert not carousel.previous.isVisible() and not carousel.next.isVisible()


def test_memory_track_keeps_vertical_wheel_and_loads_more_without_replacing_cards(ui,app):
    from PySide6.QtCore import QPointF
    from PySide6.QtGui import QWheelEvent
    from checkpoint.smooth_scroll import SmoothScrollArea

    window,game=ui
    for number in range(26):window.library.add_diary(game,f'Nota {number}')
    window.resize(1000,700);window.navigate(0)
    for _ in range(8):app.processEvents()
    page=window.pages[0]
    home=page.findChild(SmoothScrollArea,'homeScroll')
    carousel=page.findChild(MemoryCarousel)
    track=carousel.track
    assert len(carousel.cards)==24
    first=carousel.cards[0]
    home.verticalScrollBar().setValue(0)
    for delta,scroll in ((QPoint(0,-120),home.scroll_animation),(QPoint(-120,0),track.animation)):
        event=QWheelEvent(QPointF(10,10),QPointF(10,10),QPoint(),delta,
                          Qt.NoButton,Qt.NoModifier,Qt.NoScrollPhase,False)
        app.sendEvent(track.viewport(),event)
        assert event.isAccepted() and scroll.endValue()>0
        scroll.setCurrentTime(scroll.duration())
    track.scroll_to(track.horizontalScrollBar().maximum(),animate=False)
    for _ in range(8):app.processEvents()
    assert len(carousel.cards)==26 and carousel.cards[0] is first


def test_status_change_does_not_create_recent_card(ui,app):
    w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'status':'Jogando'},i)
    w.navigate(0);app.processEvents()
    assert not w.pages[0].findChildren(RecentGameCard)
    assert any(l.text()=='Nenhuma execução registrada' for l in w.pages[0].findChildren(QLabel))


def test_three_recent_games_carousel_preserves_every_cover_edge(ui,app,folder):
    from PySide6.QtGui import QImage,QColor,QPainter
    from checkpoint.home_components import GameStrip
    w,i=ui;identities=[i]
    for title in ('Hades','Celeste','Metroid Fusion','Portal','Metroid','Edição A','Edição B','Edição C','Edição D','Edição E','Edição F'):
        identities.append(w.library.save_game({'title':title,'platform':'PC'}))
    for n,identity in enumerate(identities):
        image=QImage(200,300,QImage.Format_RGB32);image.fill(QColor('blue'));p=QPainter(image)
        p.fillRect(0,0,200,12,QColor('yellow'));p.fillRect(0,288,200,12,QColor('magenta'))
        p.fillRect(0,12,12,276,QColor('cyan'));p.fillRect(188,12,12,276,QColor('red'));p.end()
        path=folder/f'cover-{n}.png';assert image.save(str(path))
        w.library.save_game({'title':w.library.get(identity)['title'],'cover':str(path)},identity)
        with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'finished',?)",(identity,(datetime.now(timezone.utc)-timedelta(hours=n+1)).isoformat(),100+n))
    for size in ((1280,800),(1920,1080),(1000,700)):
        w.resize(*size);w.navigate(0)
        for _ in range(8):app.processEvents()
        from PySide6.QtWidgets import QScrollArea
        page=w.pages[0];strip=page.findChild(GameStrip)
        viewport=page.findChild(QScrollArea,'homeScroll').viewport()
        offers=page.findChild(QWidget,'homeWishOffers')
        assert offers.mapTo(viewport,QPoint()).x()+offers.width()<=viewport.width()
        hero=page.findChild(LastPlayedBanner)
        assert hero.mapTo(viewport,QPoint()).x()+hero.width()<=viewport.width()
        assert [game['id'] for game in strip.games]==identities[1:11]
        assert len(list(w.library.sql.execute('SELECT id FROM play_sessions')))==len(identities)
        assert [card.game_id for card in strip.tiles]==identities[1:11]
        track=strip.track;view=track.viewport()
        if size[0]==1000:
            x=strip.tiles[2].mapTo(view,QPoint()).x()
            assert x<view.width()<x+strip.tiles[2].width()
        from checkpoint.home_components import HomeSectionHeader
        header=w.pages[0].findChild(QWidget,'homeRecentSection').findChild(HomeSectionHeader)
        assert strip.previous.parentWidget() is header and strip.next.parentWidget() is header
        for button in (strip.previous,strip.next):
            assert abs(header.title.geometry().center().y()-button.geometry().center().y())<=1
        assert all(first.geometry().right()+10<second.x() for first,second in zip(strip.tiles,strip.tiles[1:]))
        assert not strip.previous.isEnabled() and strip.next.isEnabled()
        for card in strip.tiles:
            assert card.height()<=view.height()
            art=card.findChild(RecentArtwork);target=art.image_target()
            assert art.rect().contains(target.toAlignedRect())
            assert abs(target.width()/target.height()-2/3)<.01
            assert 210<target.height()<=230
            frame=art.grab().toImage();x=round(target.center().x());y=round(target.center().y())
            top=frame.pixelColor(x,round(target.top())+2);bottom=frame.pixelColor(x,round(target.bottom())-3)
            left=frame.pixelColor(round(target.left())+2,y);right=frame.pixelColor(round(target.right())-3,y)
            assert top.red()>top.blue() and top.green()>top.blue()
            assert bottom.red()>bottom.green() and bottom.blue()>bottom.green()
            assert left.blue()>left.red() and left.green()>left.red()
            assert right.red()>right.green() and right.red()>right.blue()
        cards=strip.tiles.copy()
        strip.setFocus();QTest.keyClick(strip,Qt.Key_Right)
        assert track.destination()==track.stride
        track.animation.setCurrentTime(track.animation.duration())
        assert strip.tiles==cards and track.horizontalScrollBar().value()==track.stride
        for _ in range(10):strip.next.click()
        track.animation.setCurrentTime(track.animation.duration())
        assert not strip.next.isEnabled()


def test_offers_show_only_same_offer_original_discount_and_current(ui,app):
    from checkpoint.home_data import wish_offers
    w,i=ui
    with w.library.sql:
        w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam','620')",(i,))
    w.library.set_setting(f'prices.ggdeals.{i}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':datetime.now(timezone.utc).isoformat(),
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


def test_official_offer_header_does_not_replace_a_manually_chosen_banner(library):
    from checkpoint.offer_art import steam_header_identity
    identity=library.save_game({'title':'God of War Ragnarök','platform':'PC','banner':'minha-arte.jpg'})
    with library.sql:library.sql.execute("INSERT INTO external_identifiers VALUES (?,'steam','2322010')",(identity,))
    assert steam_header_identity(library,library.get(identity)) is None
    library.save_game({'title':'God of War Ragnarök','banner':''},identity)
    assert steam_header_identity(library,library.get(identity))=='2322010'


def test_home_hero_keeps_entire_wide_and_narrow_banners(ui,app,folder):
    from PySide6.QtGui import QImage,QColor,QPainter
    w,i=ui;seed_recent(w,i)
    for n,(width,height) in enumerate(((1200,300),(640,440))):
        image=QImage(width,height,QImage.Format_RGB32);image.fill(QColor('blue'))
        painter=QPainter(image);painter.fillRect(0,0,width,24,QColor('yellow'))
        painter.fillRect(0,height-24,width,24,QColor('magenta'))
        painter.fillRect(0,24,24,height-48,QColor('cyan'))
        painter.fillRect(width-24,24,24,height-48,QColor('red'));painter.end()
        path=folder/f'hero-{n}.png';assert image.save(str(path))
        game={**w.library.get(i),'banner':str(path)}
        hero=LastPlayedBanner(w,game);hero.show()
        try:
            for window_width in (735,1020,1660):
                hero.resize(window_width,hero.height())
                for _ in range(8):app.processEvents()
                target=hero.banner_target()
                if window_width==1660:
                    assert hero.play_button.width()>=190 and hero.play_button.height()>=50
                assert hero.rect().contains(target.toAlignedRect())
                assert target.left()>hero.play_button.geometry().right()
                assert abs(target.width()/target.height()-width/height)<.01
                rendered=hero.grab().toImage()
                middle=target.center()
                for x,y,expected in ((middle.x(),target.top()+2,'yellow'),(middle.x(),target.bottom()-3,'magenta'),
                                     (target.right()-3,middle.y(),'red')):
                    assert rendered.pixelColor(round(x),round(y))==QColor(expected)
                for y in (target.top()+2,middle.y(),target.bottom()-3):
                    before=rendered.pixelColor(round(target.left()-1),round(y)).getRgb()
                    after=rendered.pixelColor(round(target.left()+1),round(y)).getRgb()
                    assert all(abs(a-b)<16 for a,b in zip(before,after))
                x=round(target.left()+min(54,target.width()*.13))
                center=rendered.pixelColor(x,round(middle.y())).blue()
                for height_ratio in (.17,.83):
                    edge=rendered.pixelColor(x,round(target.top()+height_ratio*target.height())).blue()
                    assert center>edge+18
        finally:hero.close()

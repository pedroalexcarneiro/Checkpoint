from datetime import datetime, timedelta, timezone
from PySide6.QtCore import QPoint
from PySide6.QtGui import QImage, QColor
from PySide6.QtWidgets import QWidget
from checkpoint.home_components import GameStrip, MemoryCarousel
from checkpoint.design_system import ArtworkButton
from test_bugs_0134 import ui, sample


def settle(app):
    for _ in range(12):app.processEvents()


def test_home_shows_each_game_once_and_keeps_sessions_and_totals(ui, app):
    window, first=ui
    second=window.library.save_game({'title':'Outro jogo','platform':'PC'})
    now=datetime.now(timezone.utc)
    with window.library.sql:
        for n, identity in enumerate((first,first,second,first,second)):
            window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid,duration_seconds) VALUES(?,?,'finished',?,600)",(identity,(now-timedelta(hours=n+1)).isoformat(),100+n))
    before=[tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]
    window.navigate(0);settle(app)
    strip=window.pages[0].findChild(GameStrip)
    assert [g['id'] for g in strip.games]==[first,second]
    assert [g['seconds'] for g in strip.games]==[1800,1200]
    assert strip.games[0]['last_played']==(now-timedelta(hours=1)).isoformat()
    assert [tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]==before


def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
    window, identity=ui
    path=folder/'captura.png'
    image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
    for n in range(2):
        copy=folder/f'captura-{n}.png';assert image.save(str(copy))
        window.library.add_media(identity,copy,'Imagem de teste')
    for size in ((1280,800),(1920,1080)):
        window.resize(*size);window.navigate(0);settle(app)
        carousel=window.pages[0].findChild(MemoryCarousel)
        frames=carousel.findChildren(QWidget,'homeMemoryCard')
        assert len(frames)==2 and all(f.width()<=300 for f in frames)
        assert all(a.geometry().right()+12<b.geometry().left() for a,b in zip(frames,frames[1:]))
        for page in (0,3):
            if page==3:window.navigate(3);settle(app)
            if page==0:cards=frames
            else:cards=window.pages[3].findChild(QWidget,'memoriesGrid').cards
            for card in cards:
                assert card.width()<=320
                preview=card.findChild(ArtworkButton)
                from artwork_wait import wait_for_memory_artwork
                wait_for_memory_artwork(card)
                pixels=card.grab().toImage()
                # A lateral da prévia deve continuar o próprio fundo do card.
                at=preview.mapTo(card,QPoint(1,preview.height()//2))
                outside=QPoint(at.x()-3,at.y())
                a,b=pixels.pixelColor(at),pixels.pixelColor(outside)
                assert max(abs(x-y) for x,y in zip(a.getRgb()[:3],b.getRgb()[:3]))<=2


def test_memory_cards_stay_visible_and_separate_after_resizing(ui,app):
    window,identity=ui
    for n in range(8):window.library.add_diary(identity,f'Nota {n}')
    for mode in ('dark','light'):
        window.set_theme('black');window.set_appearance(mode);window.navigate(0)
        for width in (1280,1920,1000,1280):
            window.resize(width,800);settle(app)
            assert window.width()==width
            carousel=window.pages[0].findChild(MemoryCarousel)
            assert all(card.isVisibleTo(carousel) for card in carousel.cards)
            assert all(a.geometry().right()+12<b.geometry().left() for a,b in zip(carousel.cards,carousel.cards[1:]))

from checkpoint.home_view import in_progress,GameStrip
from checkpoint.window import MainWindow
from checkpoint.home_components import LastPlayedBanner,RecentArtwork
from PySide6.QtWidgets import QTabBar

def test_home_only_in_progress_and_latest_session_hero(library,app):
    old=library.save_game({'title':'Em andamento','status':'Jogando'})
    recent=library.save_game({'title':'Pausado recente','status':'Pausado'})
    fresh=library.save_game({'title':'Não iniciado','status':'Não iniciado'})
    with library.sql:
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(recent,'2026-10-12T12:00:00+00:00'))
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(old,'2026-09-12T12:00:00+00:00'))
    assert [g['id'] for g in in_progress(library)]==[recent,old]
    window=MainWindow(library);window.resize(1280,800);window.show()
    for _ in range(4):app.processEvents()
    page=window.pages[0]
    assert page.findChild(LastPlayedBanner).game_id==recent
    assert [art.game['id'] for art in page.findChildren(RecentArtwork)]==[old]
    assert not page.findChildren(QTabBar)
    strip=page.findChild(GameStrip)
    assert {t.game_id for t in strip.tiles}=={old}
    assert window.width()==1280
    assert strip.width()>0 and strip.height()>0
    window.close()

def test_home_without_started_games_has_no_invented_hero(library,app):
    library.save_game({'title':'A começar'})
    window=MainWindow(library)
    assert not window.pages[0].findChildren(LastPlayedBanner)
    assert not window.pages[0].findChildren(RecentArtwork)
    assert not window.pages[0].findChildren(GameStrip)
    window.close()


def test_home_hero_button_remains_inside_banner_after_resizing(library,app):
    library.save_game({'title':'Jogo atual','status':'Jogando','description':'Descrição curta. '*50})
    from datetime import datetime,timezone
    with library.sql:
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(1,?,'interrupted',123)",(datetime.now(timezone.utc).isoformat(),))
    window=MainWindow(library);window.show()
    for width,height in ((1280,800),(1920,1080),(1280,800)):
        window.resize(width,height)
        for _ in range(5):app.processEvents()
        banner=window.pages[0].findChild(LastPlayedBanner)
        assert banner.rect().contains(banner.play_button.geometry())
        assert banner.play_button.text()=='Continuar'
    window.close()

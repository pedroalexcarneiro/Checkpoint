from checkpoint.home_view import in_progress,GameStrip
from checkpoint.window import MainWindow
from checkpoint.ui_components import Hero
from PySide6.QtWidgets import QTabBar

def test_home_only_in_progress_and_latest_session_hero(library,app):
    old=library.save_game({'title':'Em andamento','status':'Jogando'})
    recent=library.save_game({'title':'Pausado recente','status':'Pausado'})
    fresh=library.save_game({'title':'Não iniciado','status':'Não iniciado'})
    with library.sql:
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state) VALUES(?,?,'interrupted')",(recent,'2026-10-12T12:00:00+00:00'))
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state) VALUES(?,?,'interrupted')",(old,'2026-09-12T12:00:00+00:00'))
    assert [g['id'] for g in in_progress(library)]==[recent,old]
    window=MainWindow(library);window.resize(1280,800);window.show()
    for _ in range(4):app.processEvents()
    page=window.pages[0]
    assert page.findChild(Hero).game['id']==recent
    assert not page.findChildren(QTabBar)
    strip=page.findChild(GameStrip)
    assert {t.game_id for t in strip.tiles}=={recent,old}
    assert window.width()==1280
    assert page.rect().contains(strip.mapTo(page,strip.rect().bottomRight()))
    window.close()

def test_home_without_started_games_has_no_invented_hero(library,app):
    library.save_game({'title':'A começar'})
    window=MainWindow(library)
    assert not window.pages[0].findChildren(Hero)
    assert not window.pages[0].findChildren(GameStrip)
    window.close()

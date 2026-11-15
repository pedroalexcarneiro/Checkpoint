from PySide6.QtWidgets import QLabel
from checkpoint.collection_views import WishCard
from checkpoint.playtime import total_seconds
from test_bugs_0134 import ui,sample


def test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time(ui,app):
    w,i=ui;lib=w.library
    lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-11-10T12:00:00Z',8100,'finished')",(i,));lib.sql.commit()
    original=[tuple(r) for r in lib.sql.execute('SELECT * FROM play_sessions')]
    lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
    card=w.pages[2].findChild(WishCard)
    assert not any(l.text()=='2h15min' for l in card.findChildren(QLabel))
    w.detail(i);app.processEvents();assert not w.detail_page.findChild(QLabel,'localPlaytime')
    w.acquire_wish(i);w.detail(i);app.processEvents()
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 2h15min'
    w.add_wish(i)
    assert lib.sql.execute('SELECT 1 FROM wishlist WHERE game_id=?',(i,)).fetchone()
    assert lib.is_owned(i) and i in {g['id'] for g in lib.owned_games()}
    w.detail(i);app.processEvents();assert w.detail_page.findChild(QLabel,'localPlaytime')
    w.remove_wish(i);assert lib.is_owned(i)
    assert total_seconds(lib,i)==8100
    assert [tuple(r) for r in lib.sql.execute('SELECT * FROM play_sessions')]==original


def test_nullable_legacy_ownership_flag_agrees_with_collection(library):
    i=library.save_game({'title':'Portal 2'})
    library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,));library.sql.commit()
    for flag,owned in [(None,False),(True,False),(False,True)]:
        library.set_setting(f'collection.unowned.{i}',flag)
        assert library.is_owned(i)==owned
        assert (i in {g['id'] for g in library.owned_games()})==owned

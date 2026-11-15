from PySide6.QtCore import Qt
from PySide6.QtGui import QImage,QColor
from checkpoint.playtime import collection_times
from test_bugs_0134 import ui,sample


def test_collection_totals_use_bounded_queries_without_duplicate_snapshots(library):
    ids=[library.save_game({'title':f'Jogo {n}'}) for n in range(100)]
    with library.sql:
        library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-01-01',1200,'finished')",(ids[0],))
        for account,minutes in [('1',20),('2',30)]:
            library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES(?,'620',?,'Jogo',?,'2026-01-01')",(account,ids[0],minutes))
    queries=[];library.sql.set_trace_callback(queries.append)
    try:totals=collection_times(library)
    finally:library.sql.set_trace_callback(None)
    assert totals[ids[0]]==3000 and all(totals[i]==0 for i in ids[1:])
    assert len(queries)<=8


def test_cache_is_bounded_and_invalidates_changed_files(app,folder):
    from checkpoint.artwork_cache import ArtworkCache
    cache=ArtworkCache(max_bytes=80_000)
    for n in range(8):
        image=QImage(160,240,QImage.Format_RGB32);image.fill(QColor('red'));path=folder/f'{n}.png';assert image.save(str(path))
        pix=cache.load(str(path),100,150);assert not pix.isNull()
        assert cache.used_bytes<=80_000
    path=folder/'7.png';image.fill(QColor('blue'));assert image.save(str(path))
    pix=cache.load(str(path),100,150)
    assert pix.toImage().pixelColor(50,75).blue()>200
    assert cache.used_bytes<=80_000


def test_refresh_preserves_items_and_scroll_with_equal_grid_margins(ui,app):
    w,i=ui
    for n in range(100):w.library.save_game({'title':f'Jogo {n:03}'})
    for size in ((1280,800),(1920,1080)):
        w.resize(*size);w.navigate(1)
        for _ in range(6):app.processEvents()
        grid=w.gallery;bar=grid.verticalScrollBar();bar.setValue(bar.maximum()//2);position=bar.value();item=grid.item(0)
        w.refresh_library()
        for _ in range(4):app.processEvents()
        assert grid.item(0) is item and bar.value()==position
        first=grid.art_rect(grid.visualItemRect(grid.item(0)))
        last=grid.art_rect(grid.visualItemRect(grid.item(grid.columns-1)))
        assert abs(first.left()-(grid.viewport().width()-last.right()))<=2

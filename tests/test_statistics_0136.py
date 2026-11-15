from datetime import datetime,timezone,timedelta
from zoneinfo import ZoneInfo
import pytest
from checkpoint.statistics_periods import period_bounds,period_stats
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QComboBox,QLabel
from checkpoint.design_system import CardGrid


def session(lib,i,start,seconds):
    lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state) VALUES(?,?,?,?, 'finished')",(i,start.isoformat(),(start+timedelta(seconds=seconds)).isoformat(),seconds));lib.sql.commit()


def test_calendar_bounds_clamp_and_monday():
    now=datetime(2026,5,31,17,25,tzinfo=timezone.utc)
    assert period_bounds('3m',now,timezone.utc)[0]==datetime(2026,2,28,17,25,tzinfo=timezone.utc)
    assert period_bounds('weekly',now,timezone.utc)[0]==datetime(2026,5,25,tzinfo=timezone.utc)
    assert period_bounds('monthly',now,timezone.utc)[0]==datetime(2026,5,1,tzinfo=timezone.utc)
    assert period_bounds('all',now,timezone.utc)==(None,now)
    jan=datetime(2026,1,15,tzinfo=timezone.utc)
    assert period_bounds('6m',jan,timezone.utc)[0]==datetime(2025,7,15,tzinfo=timezone.utc)

@pytest.mark.parametrize('title',['Portal 2','Metroid Fusion'])
def test_period_clips_local_midnight_without_altering_data(library,title):
    i=library.save_game({'title':title});zone=ZoneInfo('America/New_York');now=datetime(2026,1,1,6,tzinfo=timezone.utc)
    session(library,i,datetime(2026,1,1,4,30,tzinfo=timezone.utc),7200)
    original=[tuple(r) for r in library.sql.execute('SELECT * FROM play_sessions')]
    stats=period_stats(library,'daily',now,zone)
    assert stats['seconds']==3600 and stats['sessions']==1 and stats['daily']=={'2026-01-01':3600}
    assert period_stats(library,'all',now,zone)['daily']=={'2025-12-31':1800,'2026-01-01':3600}
    assert [tuple(r) for r in library.sql.execute('SELECT * FROM play_sessions')]==original


def test_dst_and_empty_do_not_distribute_steam(library):
    i=library.save_game({'title':'Portal 2'});zone=ZoneInfo('America/New_York')
    library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES('1','620',?,'Portal 2',10000,'2026-03-08')",(i,));library.sql.commit()
    start=datetime(2026,3,8,5,tzinfo=timezone.utc);session(library,i,start,23*3600)
    stats=period_stats(library,'daily',datetime(2026,3,9,3,59,59,tzinfo=timezone.utc),zone)
    assert stats['seconds']==23*3600-1 and len(stats['daily'])==1
    assert period_stats(library,'daily',datetime(2026,3,10,tzinfo=timezone.utc),zone)['seconds']==0
    assert period_stats(library,'daily',datetime(2026,3,10,tzinfo=timezone.utc),zone)['sessions']==0


def test_equivalent_metrics_and_period_selector(ui,app):
    w,i=ui;w.library.save_game({'title':'Nome muito longo '*20},i)
    for size in [(1280,800),(1920,1080)]:
        w.resize(*size);w.navigate(4)
        for _ in range(5):app.processEvents()
        combo=w.pages[4].findChild(QComboBox,'statisticsPeriod')
        assert combo.count()==7
        for key in ['daily','weekly','monthly','3m','6m','12m','all']:
            combo.setCurrentIndex(combo.findData(key))
            for _ in range(3):app.processEvents()
            grid=w.pages[4].findChild(CardGrid,'statisticsMetrics')
            assert len({c.height() for c in grid.cards})==1
            assert len({c.y() for c in grid.cards})==1
            for c in grid.cards:
                for label in c.findChildren(QLabel):
                    assert c.rect().contains(label.geometry())


def test_fall_dst_is_25_hours_and_year_boundary(library):
    i=library.save_game({'title':'Hades II'});zone=ZoneInfo('America/New_York')
    start=datetime(2026,11,1,4,tzinfo=timezone.utc);session(library,i,start,25*3600)
    result=period_stats(library,'daily',datetime(2026,11,2,4,59,59,tzinfo=timezone.utc),zone)
    assert result['seconds']==25*3600-1
    assert result['daily']=={'2026-11-01':25*3600-1}
    start=datetime(2026,1,1,4,30,tzinfo=timezone.utc);session(library,i,start,3600)
    result=period_stats(library,'monthly',datetime(2026,1,2,tzinfo=timezone.utc),zone)
    assert result['seconds']==1800 and result['completions']=={}

from datetime import date,datetime,timezone,timedelta
from PySide6.QtWidgets import QComboBox,QLabel
from test_bugs_0134 import ui,sample


def test_week_chart_uses_width_and_months_keep_real_days(ui,app):
    w,i=ui
    for size in ((1280,800),(1920,1080)):
        w.resize(*size);w.navigate(4);combo=w.pages[4].findChild(QComboBox,'statisticsPeriod')
        combo.setCurrentIndex(combo.findData('weekly'))
        for _ in range(6):app.processEvents()
        from checkpoint.statistics_view import TimeChart
        chart=w.pages[4].findChild(TimeChart);chart.grab()
        assert chart.period=='weekly' and chart.cells
        span=max(r.right() for r,_,_ in chart.cells)-min(r.left() for r,_,_ in chart.cells)
        assert span>=chart.width()*.65
        combo.setCurrentIndex(combo.findData('12m'))
        for _ in range(5):app.processEvents()
        chart=w.pages[4].findChild(TimeChart);chart.grab()
        first,last=chart.interval();assert len(chart.cells)==(last-first).days+1
        assert not any(l.text()=='Gêneros da coleção' for l in w.pages[4].findChildren(QLabel))


def test_hourly_day_uses_real_local_session_boundaries(library):
    from checkpoint.statistics_periods import day_hours
    i=library.save_game({'title':'Portal 2'})
    with library.sql:library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-11-15T00:30:00+00:00',5400,'finished')",(i,))
    rows=day_hours(library,datetime(2026,11,15,3,tzinfo=timezone.utc),timezone.utc)
    assert len(rows)==24
    assert rows[0]['seconds']==1800 and rows[1]['seconds']==3600
    assert sum(r['seconds'] for r in rows)==5400


def test_day_hours_respect_dst_and_do_not_change_instants(library):
    from zoneinfo import ZoneInfo
    from checkpoint.statistics_periods import day_hours
    zone=ZoneInfo('America/New_York')
    assert len(day_hours(library,datetime(2026,3,8,17,tzinfo=timezone.utc),zone))==23
    assert len(day_hours(library,datetime(2026,11,1,17,tzinfo=timezone.utc),zone))==25

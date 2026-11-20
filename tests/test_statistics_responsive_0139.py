from datetime import datetime, timedelta, timezone
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QBoxLayout
from checkpoint.design_system import AdaptiveColumns
from checkpoint.period_chart import PeriodChart
from test_bugs_0134 import ui, sample


def test_small_statistics_keeps_titles_times_and_heatmap_readable(ui, app):
    window, identity = ui
    titles = ('Honkai: Star Rail', 'The Legend of Zelda: Ocarina of Time 3D')
    with window.library.sql:
        for n, title in enumerate(titles):
            game = window.library.save_game({'title': title, 'platform': 'PC'})
            start = datetime.now(timezone.utc)-timedelta(hours=4+n)
            window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,?,?,'finished')", (game, start.isoformat(), 3600+n*60))
    window.library.set_setting('statistics.period', '3m')
    for width in (1000, 1280, 1920, 1280):
        window.resize(width, 800); window.navigate(4)
        for _ in range(10): app.processEvents()
        columns = window.pages[4].findChild(AdaptiveColumns)
        assert columns.row.direction() == (QBoxLayout.TopToBottom if width == 1000 else QBoxLayout.LeftToRight)
        for row in window.pages[4].findChildren(QWidget, 'statisticsGameRow'):
            button = row.findChild(QPushButton, 'statisticsGameName')
            label = row.findChild(QLabel, 'statisticsGameTime')
            # Text must fit the actual Qt contents, including stylesheet padding.
            from PySide6.QtWidgets import QStyleOptionButton, QStyle
            option = QStyleOptionButton(); button.initStyleOption(option)
            content = button.style().subElementRect(QStyle.SE_PushButtonContents, option, button)
            assert button.fontMetrics().horizontalAdvance(button.text()) <= content.width()
            assert button.text() == button.full_title
            assert not button.geometry().intersects(label.geometry())
            assert label.text() in ('1h00min', '1h01min') and label.font().bold()
        chart = window.pages[4].findChild(PeriodChart)
        summary, legend = chart.footer_layout()
        assert not summary.intersects(legend)
        assert chart.rect().contains(summary.toAlignedRect())
        assert chart.rect().contains(legend.toAlignedRect())
        assert chart.fontMetrics().horizontalAdvance('6h52min') < summary.width()
        assert len(chart.cells) >= 89
        occupied=max(rect.right() for rect,_,_ in chart.cells)-min(rect.left() for rect,_,_ in chart.cells)
        assert occupied/(chart.width()-32) >= .75


def test_heatmap_footer_never_overlaps_legend_in_narrow_view(app):
    from checkpoint.theme import get_theme
    first = datetime.now(timezone.utc).date()-timedelta(days=89)
    values = {(first+timedelta(days=n)).isoformat(): 365999 for n in range(90)}
    chart = PeriodChart(values, get_theme('green'))
    chart.set_interval(first, first+timedelta(days=89)); chart.set_period('3m')
    chart.resize(340, 200); chart.show()
    for _ in range(6): app.processEvents()
    summary, legend = chart.footer_layout()
    assert not summary.intersects(legend) and legend.top() > summary.top()
    assert chart.rect().contains(legend.toAlignedRect())
    assert all(rect.bottom() < summary.top() for rect, day, seconds in chart.cells)
    chart.close()

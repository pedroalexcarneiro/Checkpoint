import time
from PySide6.QtCore import Qt,QPoint,QPointF
from PySide6.QtGui import QWheelEvent
from PySide6.QtTest import QTest
from checkpoint.window import MainWindow
from checkpoint.smooth_scroll import SmoothScrollArea

def test_wheel_with_500_games_uses_pixel_animation_and_remains_responsive(library,app):
    for index in range(500):library.save_game({'title':f'Jogo {index:03}'})
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    window=MainWindow(library);window.resize(1280,800);window.navigate(1);window.show()
    for _ in range(4):app.processEvents()
    grid=window.gallery;bar=grid.verticalScrollBar();assert bar.maximum()>0
    event=QWheelEvent(QPointF(20,20),QPointF(20,20),QPoint(0,0),QPoint(0,-120),Qt.NoButton,Qt.NoModifier,Qt.NoScrollPhase,False)
    start=time.monotonic()
    app.sendEvent(grid.viewport(),event)
    assert grid.scroll_animation.duration()==180
    QTest.qWait(230);app.processEvents()
    assert bar.value()==72 and time.monotonic()-start<2
    for page in (2,3,4):
        window.navigate(page);app.processEvents()
        assert window.pages[page].findChildren(SmoothScrollArea)
    window.close()

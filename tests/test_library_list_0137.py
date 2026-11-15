from PySide6.QtCore import Qt,QPoint
from PySide6.QtGui import QPixmap,QColor
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QTableWidget
from test_bugs_0134 import ui,sample


def test_horizontal_list_has_logo_time_and_independent_favorite(ui,app,folder,monkeypatch):
    from checkpoint.library_list import LibraryList
    w,i=ui;title='Um jogo de nome longo '*8
    logo=QPixmap(200,60);logo.fill(QColor('#18aa60'));path=folder/'logo.png';assert logo.save(str(path))
    w.library.save_game({'title':title,'platform':'GBA','status':'Pausado','logo':str(path)},i)
    with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-01-01T12:00:00+00:00',5520,'finished')",(i,))
    w.navigate(1);w.view.setCurrentIndex(1)
    calls=[];monkeypatch.setattr(w,'detail',lambda identity:calls.append(identity))
    for size in ((1280,800),(1920,1080),(1000,700)):
        w.resize(*size)
        for _ in range(6):app.processEvents()
        view=w.game_list;assert isinstance(view,LibraryList) and view.count()==1
        assert not w.pages[1].findChildren(QTableWidget)
        assert view.horizontalScrollBar().maximum()==0
        item=view.item(0);assert '1h32min' in item.data(Qt.AccessibleTextRole)
        assert 'GBA' not in item.toolTip() and 'Pausado' not in item.toolTip()
        rect=view.visualItemRect(item);heart=view.heart_rect(rect)
        previous=w.library.get(i)['favorite']
        QTest.mouseClick(view.viewport(),Qt.LeftButton,Qt.NoModifier,heart.center())
        app.processEvents();assert w.library.get(i)['favorite']==1-previous
        assert w.current_page==1 and not calls
        view.setCurrentRow(0);view.setFocus();QTest.keyClick(view,Qt.Key_Space)
        assert w.library.get(i)['favorite']==previous and not calls
    QTest.mouseClick(view.viewport(),Qt.LeftButton,Qt.NoModifier,QPoint(180,rect.center().y()))
    assert calls==[i]


def test_list_search_and_sort_preserve_filtering(ui,app):
    w,i=ui;j=w.library.save_game({'title':'ZZZ Segundo jogo','favorite':1})
    w.navigate(1);w.view.setCurrentIndex(1);app.processEvents()
    assert w.game_list.count()==2
    w.library_tabs.setCurrentIndex(1);assert w.game_list.count()==1
    assert w.game_list.item(0).data(Qt.UserRole)==j
    w.library_tabs.setCurrentIndex(0);w.search.setText('ZZZ');assert w.game_list.count()==1
    w.search.clear();w.sort.setCurrentIndex(w.sort.findData('recent'))
    assert w.game_list.item(0).data(Qt.UserRole)==j
    assert w.library.get(i) and w.library.get(j)

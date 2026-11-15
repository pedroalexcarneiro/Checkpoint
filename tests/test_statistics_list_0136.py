from datetime import datetime,timezone,timedelta
from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QWidget
from PySide6.QtGui import QImage,QColor


def test_top_list_logo_name_and_time_are_separate(ui,app,folder):
    w,i=ui
    for n,title in enumerate(['Portal 2','Metroid Fusion com um nome longo '*10]):
        path=folder/f'logo{n}.png';im=QImage(300,100,QImage.Format_RGB32);im.fill(QColor('cyan' if n else 'yellow'));im.save(str(path))
        identity=w.library.save_game({'title':title,'logo':str(path)})
        start=datetime.now(timezone.utc)-timedelta(hours=4)
        w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,?,?,'finished')",(identity,start.isoformat(),3600+n*600))
    w.library.sql.commit()
    for size in [(1280,800),(1920,1080)]:
        w.resize(*size);w.navigate(4)
        for _ in range(4):app.processEvents()
        rows=w.pages[4].findChildren(QWidget,'statisticsGameRow');assert len(rows)==2
        for row in rows:
            logo=row.findChild(QLabel,'statisticsGameLogo');name=row.findChild(QWidget,'statisticsGameName');value=row.findChild(QLabel,'statisticsGameTime')
            assert logo and not logo.pixmap().isNull() and logo.x()<name.x()<value.x()
            assert logo.geometry().right()<name.geometry().left() and name.geometry().right()<value.geometry().left()
            assert row.rect().contains(value.geometry()) and name.toolTip()
            assert value.text() in ('1h00min','1h10min')
        assert rows[0].findChild(QLabel,'statisticsGameTime').text()=='1h10min'

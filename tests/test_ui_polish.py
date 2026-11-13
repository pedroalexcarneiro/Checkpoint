from PySide6.QtCore import Qt
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QLabel
from gamevault.window import MainWindow
from gamevault.ui_components import Hero
from gamevault.statistics_view import TimeChart,StatusRing


def test_banner_is_bounded_at_desktop_width(library,app,tmp_path):
    image=QImage(900,240,QImage.Format_RGB32);image.fill(QColor('red'));path=tmp_path/'wide.png';image.save(str(path))
    hero=Hero({'title':'Teste','banner':str(path)},__import__('gamevault.theme',fromlist=['get_theme']).get_theme('green'))
    hero.resize(750,300);hero.show();app.processEvents()
    assert 220<=hero.height()<=300
    assert hero.grab().toImage().pixelColor(hero.width()-20,hero.height()//2).red()>240
    hero.resize(1700,hero.height());app.processEvents()
    assert hero.height()<=300
    hero.close()


def test_compact_loading_and_centered_name(library,app):
    window=MainWindow(library);window.show();app.processEvents();window.completion_busy(12);app.processEvents()
    assert window.brand.text()=='Checkpoint' and window.brand.alignment()==Qt.AlignCenter
    assert window.task_status.height()==28 and window.task_status.width()<=380
    assert window.completion_bar.width()==16 and window.completion_stop.width()==24
    window.completion_busy(0);assert window.task_status.isHidden();window.close()


def test_statistics_chart_uses_library_totals(library,app):
    library.save_game({'title':'Um','status':'Jogando'});library.save_game({'title':'Dois','status':'Concluído'})
    window=MainWindow(library);window.navigate(4);window.show();app.processEvents()
    ring=window.findChild(StatusRing);chart=window.findChild(TimeChart)
    assert sum(ring.statuses.values())==2 and ring.statuses['Concluído']==1
    assert chart.values=={} and 'Nenhuma sessão' in chart.accessibleDescription()
    window.close()


def test_library_caption_starts_at_visible_cover_edge(library,app,tmp_path):
    image=QImage(120,180,QImage.Format_RGB32);image.fill(QColor('red'));path=tmp_path/'poster.png';image.save(str(path))
    library.save_game({'title':'I','cover':str(path)})
    window=MainWindow(library);window.resize(1000,700);window.navigate(1);window.show()
    for _ in range(3):app.processEvents()
    grid=window.gallery;rect=grid.visualItemRect(grid.item(0));capture=grid.viewport().grab(rect).toImage()
    red=[];letters=[]
    for y in range(capture.height()):
        for x in range(capture.width()):
            pixel=capture.pixelColor(x,y)
            if pixel.red()>240 and pixel.green()<40 and pixel.blue()<40:red.append((x,y))
            elif pixel.red()>215 and pixel.green()>215 and pixel.blue()>215:letters.append((x,y))
    assert red and letters
    assert abs(min(x for x,y in letters)-min(x for x,y in red))<=3
    assert max(x for x,y in red)-min(x for x,y in red)>capture.width()*.8
    window.close()

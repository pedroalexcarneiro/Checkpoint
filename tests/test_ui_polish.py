from PySide6.QtCore import Qt
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QLabel
from gamevault.window import MainWindow
from gamevault.ui_components import Hero
from gamevault.statistics_view import TimeChart,StatusRing


def test_banner_frame_tracks_original_ratio(library,app,tmp_path):
    image=QImage(900,240,QImage.Format_RGB32);image.fill(QColor('red'));path=tmp_path/'wide.png';image.save(str(path))
    hero=Hero({'title':'Teste','banner':str(path)},__import__('gamevault.theme',fromlist=['get_theme']).get_theme('green'))
    hero.resize(750,300);hero.show();app.processEvents()
    assert abs(hero.width()/hero.height()-900/240)<.03
    assert hero.grab().toImage().pixelColor(hero.width()-20,hero.height()//2).red()>240
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

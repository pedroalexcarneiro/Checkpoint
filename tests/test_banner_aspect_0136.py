import pytest
from PySide6.QtGui import QImage,QColor
from checkpoint.ui_components import Hero
from checkpoint.theme import get_theme

@pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
@pytest.mark.parametrize('detail',[False,True])
def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
    image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
    hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
    try:
        for width in [750,1026,1388,1700,1026,750]:
            hero.resize(width,hero.height())
            for _ in range(4):app.processEvents()
            expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
            exact=hero.banner_target();assert abs(exact.width()/exact.height()-shape[0]/shape[1])<1e-9
            assert abs(hero.height()-expected)<=1
            assert abs(target.left())<=1 and abs(target.top())<=1
            assert abs(target.width()-hero.width())<=1 and abs(target.height()-hero.height())<=1
            assert abs(hero.width()/hero.height()-shape[0]/shape[1])<.025
    finally:hero.close();hero.deleteLater()

@pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
def test_all_four_edges_remain_visible(app,folder,title,shape):
    from PySide6.QtGui import QPainter
    image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#0000ff'));p=QPainter(image)
    p.fillRect(0,0,shape[0],16,QColor('yellow'));p.fillRect(0,shape[1]-16,shape[0],16,QColor('magenta'))
    p.fillRect(0,16,16,shape[1]-32,QColor('cyan'));p.fillRect(shape[0]-16,16,16,shape[1]-32,QColor('red'));p.end()
    path=folder/'edges.png';image.save(str(path));hero=Hero({'title':'','banner':str(path),'platform':title},get_theme('green'));hero.detail_mode=True;hero.show()
    try:
        for width in [750,1026,1388,1700,750]:
            hero.resize(width,hero.height());app.processEvents();frame=hero.grab().toImage()
            top=frame.pixelColor(hero.width()//2,2);bottom=frame.pixelColor(hero.width()//2,hero.height()-3)
            left=frame.pixelColor(2,hero.height()//2);right=frame.pixelColor(hero.width()-3,hero.height()//2)
            assert top.red()>top.blue() and top.green()>top.blue()
            assert bottom.red()>bottom.green() and bottom.blue()>bottom.green()
            assert left.green()>left.red() and left.blue()>left.red()
            assert right.red()>right.green() and right.red()>right.blue()
    finally:hero.close();hero.deleteLater()

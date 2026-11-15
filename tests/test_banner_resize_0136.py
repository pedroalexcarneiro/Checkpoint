import pytest
from PySide6.QtGui import QImage,QColor,QPainter
from checkpoint.ui_components import Hero
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('shape',[(1200,250),(600,400)])
@pytest.mark.parametrize('wish',[False,True])
def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
    w,i=ui
    im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
    p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
    path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
    w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
    if wish:
        w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,));w.library.sql.commit()
    for initial in [(1280,800),(1920,1080)]:
        w.resize(*initial);w.detail(i)
        for size in [(1920,1080),(1280,800),(1600,900),(1280,800)]:
            w.resize(*size)
            for _ in range(4):app.processEvents()
            hero=w.detail_page.findChild(Hero);r=hero.banner_rect()
            assert hero.rect().contains(r) and not r.isEmpty()
            assert abs(r.width()/r.height()-shape[0]/shape[1])<.03
            image=hero.grab().toImage();x=r.center().x()
            top=image.pixelColor(x,r.top()+2);bottom=image.pixelColor(x,r.bottom()-2)
            assert top.red()>top.blue() and top.green()>top.blue()
            assert bottom.red()>bottom.green() and bottom.blue()>bottom.green()

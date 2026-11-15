import pytest
from PySide6.QtGui import QImage,QColor,QPainter
from checkpoint.ui_components import Hero
from checkpoint.theme import get_theme
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_hero_keeps_top_and_bottom_borders(app,folder,title):
 image=QImage(100,400,QImage.Format_RGB32);image.fill(QColor('#0000ff'))
 painter=QPainter(image);painter.fillRect(0,0,100,20,QColor('#ffff00'));painter.fillRect(0,380,100,20,QColor('#ff00ff'));painter.end()
 path=folder/'portrait-banner.png';image.save(str(path))
 hero=Hero({'title':'','banner':str(path),'platform':title},get_theme('green'));hero.detail_mode=True;hero.resize(800,240);hero.show();app.processEvents()
 try:
  frame=hero.grab().toImage();x=hero.width()//2
  top=frame.pixelColor(x,5);bottom=frame.pixelColor(x,hero.height()-6)
  assert top.red()>top.blue() and top.green()>top.blue()
  assert bottom.red()>bottom.green() and bottom.blue()>bottom.green()
 finally:hero.close();hero.deleteLater()

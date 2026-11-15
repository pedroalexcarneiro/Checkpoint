import pytest
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget,QSlider
from test_bugs_0134 import ui,sample
@pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
@pytest.mark.parametrize('value',[70,150])
def test_preview_stays_right_with_common_base_and_active_value(ui,app,size,value):
 w,i=ui;w.resize(*size);w.navigate(5)
 slider=w.pages[5].findChild(QSlider,'coverSizeSlider');slider.setValue(value)
 for _ in range(5):app.processEvents()
 card=w.pages[5].findChild(QWidget,'coverSizeCard');preview=w.pages[5].findChild(QWidget,'coverSizePreview')
 active=0 if value==70 else 2;heights=(68,98,126)
 image=preview.grab().toImage();height=heights[active]
 color=image.pixelColor(round(12+active*80+round(height*2/3)/2),140-height)
 assert color.green()>color.red() and color.green()>color.blue()
 rectangles=preview.cover_rects()
 assert len({rect.bottom() for rect in rectangles})==1
 assert rectangles[0].height()<rectangles[1].height()<rectangles[2].height()
 assert preview.active_index()==(0 if value==70 else 2)
 p=preview.mapTo(card,QPoint(0,0));s=slider.mapTo(card,QPoint(0,0))
 assert p.x()>s.x()+slider.width()
 assert p.y()+preview.height()<=card.height() and p.x()+preview.width()<=card.width()
 assert all(preview.rect().contains(rect.toRect()) for rect in rectangles)

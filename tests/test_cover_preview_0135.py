import pytest
from PySide6.QtCore import QPoint,Qt
from PySide6.QtWidgets import QWidget,QSlider
from PySide6.QtTest import QTest
from checkpoint.settings_previews import CoverSizeChoices
from checkpoint.card_layout import nearest_cover_choice
from test_bugs_0134 import ui,sample

@pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
@pytest.mark.parametrize('value',[70,150])
def test_five_clickable_covers_have_common_base_and_active_value(ui,app,size,value):
 w,i=ui;w.resize(*size);w.navigate(5)
 preview=w.pages[5].findChild(CoverSizeChoices);preview.group.button(value).click()
 for _ in range(5):app.processEvents()
 card=w.pages[5].findChild(QWidget,'coverSizeCard')
 assert w.pages[5].findChild(QSlider,'coverSizeSlider') is None
 rectangles=preview.cover_rects();active=0 if value==70 else 4
 assert len(rectangles)==5 and len({round(rect.bottom()) for rect in rectangles})==1
 assert all(a.height()<b.height() for a,b in zip(rectangles,rectangles[1:]))
 assert preview.active_index()==active and sum(b.isChecked() for b in preview.buttons)==1
 image=preview.grab().toImage();rect=rectangles[active]
 color=image.pixelColor(round(rect.center().x()),round(rect.top()))
 assert color.green()>color.red() and color.green()>color.blue()
 p=preview.mapTo(card,QPoint(0,0))
 assert p.y()+preview.height()<=card.height() and p.x()+preview.width()<=card.width()
 assert all(preview.rect().contains(rect.toRect()) for rect in rectangles)
 assert w.library.setting('appearance.cover_size')==value and w.gallery.cover_percent==value
 w.navigate(1);w.navigate(5);app.processEvents()
 preview=w.pages[5].findChild(CoverSizeChoices);assert preview.percent==value


def test_old_percent_preserved_and_keyboard_selects(ui,app):
 w,i=ui;w.library.set_setting('appearance.cover_size',87);w.navigate(5);app.processEvents()
 preview=w.pages[5].findChild(CoverSizeChoices)
 assert preview.percent==90 and w.library.setting('appearance.cover_size')==87
 current=preview.group.button(90);current.setFocus();QTest.keyClick(current,Qt.Key_Right);app.processEvents()
 assert preview.percent==100 and preview.group.button(100).hasFocus()
 assert w.library.setting('appearance.cover_size')==100
 assert nearest_cover_choice(80)==70 and nearest_cover_choice(-10)==70 and nearest_cover_choice(999)==150

@pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
def test_cover_outline_spacing_is_equal_at_both_edges(ui,app,size):
 w,i=ui;w.resize(*size);w.navigate(5)
 for _ in range(5):app.processEvents()
 preview=w.pages[5].findChild(CoverSizeChoices);rects=preview.cover_rects()
 left=rects[0].left();right=preview.width()-rects[-1].right()
 gaps=[b.left()-a.right() for a,b in zip(rects,rects[1:])]
 assert abs(left-right)<=1
 assert max(gaps+[left,right])-min(gaps+[left,right])<=2

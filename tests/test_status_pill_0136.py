import pytest
from PySide6.QtCore import QPoint,Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QComboBox,QLabel,QWidget
from test_bugs_0134 import ui,sample


def test_status_is_one_themed_control_without_annotation(ui,app):
    w,i=ui
    for size in [(1280,800),(1920,1080)]:
        w.resize(*size);w.detail(i)
        for _ in range(4):app.processEvents()
        control=w.detail_page.findChild(QComboBox,'gameStatus');frame=w.detail_page.findChild(QWidget,'gameActions')
        dot=control.findChild(QLabel,'gameStatusDot')
        assert dot is not None and control.rect().contains(dot.geometry())
        assert control.height()==40 and control.minimumWidth()>=176
        assert frame.rect().contains(control.geometry().translated(control.parentWidget().mapTo(frame,QPoint(0,0))))
        assert not any(l.text()=='2' for l in control.findChildren(QLabel))
        for status in ['Backlog','Jogando','Pausado','Concluído','Abandonado']:
            control.setCurrentText(status);app.processEvents()
            image=control.grab().toImage()
            assert image.pixelColor(0,control.height()//2)==QColor(w.theme.colors['accent'])
            assert control.fontMetrics().horizontalAdvance(status)<=control.width()-72
            assert control.itemData(control.currentIndex(),Qt.FontRole).bold()
            if status!='Backlog':assert w.library.get(i)['status']==status


def test_click_on_status_dot_opens_menu_and_keyboard_saves_choice(ui,app):
    from PySide6.QtTest import QTest
    w,i=ui;w.detail(i);app.processEvents();control=w.detail_page.findChild(QComboBox,'gameStatus')
    assert w.library.get(i)['status']=='Não iniciado' and control.currentText()=='Backlog'
    dot=control.findChild(QLabel,'gameStatusDot');QTest.mouseClick(control,Qt.LeftButton,Qt.NoModifier,dot.geometry().center());app.processEvents()
    view=control.view()
    try:
        assert view.isVisible()
        QTest.keyClick(view,Qt.Key_Down);QTest.keyClick(view,Qt.Key_Return);app.processEvents()
        assert control.currentText()=='Jogando' and w.library.get(i)['status']=='Jogando'
    finally:control.hidePopup()

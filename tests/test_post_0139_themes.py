import pytest
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QComboBox
from checkpoint.theme import THEMES, get_theme, apply_theme
from checkpoint.window import MainWindow
from checkpoint.database import Database
from checkpoint.library import Library
from test_themes import contrast


@pytest.mark.parametrize('mode',['dark','light'])
@pytest.mark.parametrize('key',list(THEMES))
def test_all_appearance_modes_keep_text_contrast(key,mode):
    c=get_theme(key,mode).colors
    pairs=[(fg,bg) for fg in ('text','secondary','muted') for bg in ('background','surface','elevated','card','selected')]
    for fg,bg in pairs+[('on_accent','accent')]:
        assert contrast(c[fg],c[bg])>=4.5,(key,mode,fg,bg)
    if key=='black':
        for role in ('background','sidebar','panel'):
            color=QColor(c[role]);assert color.red()==color.green()==color.blue()
    assert QColor(c['background']).lightnessF()>.85 if mode=='light' else QColor(c['background']).lightnessF()<.2


def test_mode_is_independent_of_color_and_survives_reopening(app,library):
    window=MainWindow(library);window.navigate(5)
    control=window.pages[5].findChild(QComboBox,'appearanceMode')
    assert control is not None
    control.setCurrentIndex(control.findData('light'));window.set_theme('purple')
    assert window.theme.mode=='light' and window.theme.key=='purple'
    assert library.setting('appearance.mode')=='light'
    window.close()
    db=Database(library.db.path);reopened=MainWindow(Library(db))
    try:
        assert reopened.theme.mode=='light' and reopened.theme.key=='purple'
        assert app.property('checkpointAppearance')=='light'
    finally:
        reopened.close();db.close();apply_theme(app,'green','dark')

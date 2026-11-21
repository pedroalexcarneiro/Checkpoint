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


def test_app_ignores_legacy_light_mode_and_keeps_selected_color(app,library):
    library.set_setting('appearance.mode','light')
    apply_theme(app,'green','light')
    window=MainWindow(library);window.navigate(5)
    control=window.pages[5].findChild(QComboBox,'appearanceMode')
    assert control is None
    window.set_theme('purple')
    assert window.theme.mode=='dark' and window.theme.key=='purple'
    assert library.setting('appearance.mode')=='light'
    window.close()
    db=Database(library.db.path);reopened=MainWindow(Library(db))
    try:
        assert reopened.theme.mode=='dark' and reopened.theme.key=='purple'
        assert app.property('checkpointAppearance')=='dark'
    finally:
        reopened.close();db.close();apply_theme(app,'green','dark')

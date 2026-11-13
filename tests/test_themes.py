import pytest
from PySide6.QtWidgets import QApplication,QLabel,QPushButton
from checkpoint.theme import THEMES,DEFAULT_THEME,get_theme
from checkpoint.window import MainWindow
from checkpoint.database import Database
from checkpoint.library import Library

def luminance(color):
    channels=[int(color[i:i+2],16)/255 for i in (1,3,5)]
    linear=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in channels]
    return sum(c*w for c,w in zip(linear,[.2126,.7152,.0722]))

def contrast(a,b):
    light,dark=sorted([luminance(a),luminance(b)],reverse=True)
    return (light+.05)/(dark+.05)

@pytest.mark.parametrize('key',list(THEMES))
def test_palette_normal_text_contrast(key):
    c=THEMES[key].colors
    for foreground,background in [('text','background'),('text','panel'),('muted','background'),('muted','panel'),('on_accent','accent'),('text','selected')]:
        assert contrast(c[foreground],c[background])>=4.5,(key,foreground,background)

def test_theme_selection_is_immediate_and_survives_reopening(app,library):
    window=MainWindow(library); window.navigate(5)
    assert window.theme_selector.count()==9
    for key in THEMES:
        window.theme_selector.setCurrentIndex(window.theme_selector.findData(key)); app.processEvents()
        assert app.property('checkpointTheme')==key
        assert library.setting('appearance.theme')==key
        for index in range(6): window.navigate(index); app.processEvents()
    window.navigate(5); window.theme_selector.setCurrentIndex(window.theme_selector.findData('purple')); window.close()
    db=Database(library.db.path); reopened=MainWindow(Library(db))
    assert reopened.theme.key=='purple'
    assert get_theme('purple').colors['background'] in app.styleSheet()
    reopened.close(); db.close()

def test_unknown_theme_falls_back_to_green():
    assert get_theme('removed-theme').key==DEFAULT_THEME
    assert get_theme(None).key==DEFAULT_THEME


def test_unknown_saved_preference_falls_back_without_losing_library(app,library):
    identity=library.save_game({'title':'Preferência removida','notes':'Preservar notas'})
    library.set_setting('appearance.theme','tema-removido')
    window=MainWindow(library);window.navigate(5)
    assert window.theme.key=='green' and library.setting('appearance.theme')=='green'
    assert library.get(identity)['notes']=='Preservar notas'
    window.close()


def test_exactly_nine_themes_and_swatches(app,library):
    from checkpoint.design_system import ThemeSwatch
    assert list(THEMES)==['blue','green','yellow','red','black','purple','pink','orange','cyan']
    window=MainWindow(library);window.navigate(5)
    assert len(window.settings_tabs.findChildren(ThemeSwatch))==9
    assert window.theme_selector.count()==9 and DEFAULT_THEME=='green'
    window.close()

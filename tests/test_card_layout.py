from checkpoint.card_layout import card_metrics,cover_size
from checkpoint.window import MainWindow
from PySide6.QtWidgets import QSlider

def test_six_columns_at_default_and_responsive_scaling():
    assert card_metrics(1386).columns==6
    assert card_metrics(950).columns==4
    assert card_metrics(1386,70).columns>6
    assert card_metrics(1386,150).columns<6
    assert card_metrics(80).columns==1
    for available in (80,600,950,1580):
        m=card_metrics(available)
        assert m.width*m.columns+m.gap*(m.columns-1)<=available

def test_density_preference_preserved_in_settings_without_schema_change(library,app):
    library.set_setting('appearance.density','compact')
    assert cover_size(library)==80
    library.set_setting('appearance.cover_size',135)
    assert cover_size(library)==135
    assert library.sql.execute('PRAGMA user_version').fetchone()[0]==4
    window=MainWindow(library);window.navigate(5)
    slider=window.pages[5].findChild(QSlider,'coverSizeSlider')
    assert (slider.minimum(),slider.maximum(),slider.value())==(70,150,135)
    slider.setValue(100)
    assert cover_size(library)==100
    window.close()

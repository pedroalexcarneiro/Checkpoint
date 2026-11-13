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


def test_both_grids_share_columns_and_size_control_keeps_font_and_items(library,app):
    from checkpoint.collection_views import WishGrid
    for index in range(12):
        identity=library.save_game({'title':f'Fixture {index}'})
        if index>=6:
            with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    window=MainWindow(library);window.show();window.navigate(2);font=app.font()
    for width in (1280,1920):
        window.resize(width,800)
        for percent in (70,100,150):
            item=window.gallery.item(0)
            window.set_cover_size(percent)
            assert window.gallery.item(0) is item and app.font()==font
            for _ in range(4):app.processEvents()
            wishes=window.pages[2].findChild(WishGrid,'wishlistGrid');wish_columns=wishes.columns
            from PySide6.QtWidgets import QPushButton
            link=wishes.cards[0].findChild(QPushButton,'quiet')
            assert link.width()>=link.fontMetrics().horizontalAdvance(link.text())
            window.navigate(1)
            for _ in range(4):app.processEvents()
            assert window.gallery.columns==wish_columns
            window.navigate(2)
    window.close()

from PySide6.QtWidgets import QLabel
from gamevault.window import MainWindow
from gamevault.design_system import empty_state


def test_home_search_opens_library_results(library,app):
    library.save_game({'title':'Zelda'})
    library.save_game({'title':'Outro'})
    window=MainWindow(library)
    window.search.setText('zelda')
    app.processEvents()
    assert window.current_page==1
    assert window.gallery.count()==1
    assert 'Zelda' in window.gallery.item(0).text()
    assert not window.sidebar_add.isHidden()
    window.close()


def test_empty_description_has_room_for_wrapped_text(app):
    widget=empty_state('wish','Sua lista de desejos','Guarde os jogos que você quer.')
    widget.resize(1000,440);widget.show();app.processEvents()
    description=next(label for label in widget.findChildren(QLabel) if label.text().startswith('Guarde'))
    assert description.height()>=description.heightForWidth(description.width())
    widget.close()

import pytest
from PySide6.QtCore import Qt,QRect
from PySide6.QtGui import QFontMetrics
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult


@pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
def test_loading_preview_text_fits_without_cutting(library,app,title):
    dialog=GameDialog(library=library);quick=dialog.quick_add
    quick.timer.stop();quick.art.setText('Carregando prévia…')
    quick.show_result(MetadataResult('rawg','1',title,platforms=('Game Boy Advance',)))
    dialog.show()
    try:
        for _ in range(6):app.processEvents()
        metrics=QFontMetrics(quick.art.font())
        required=metrics.boundingRect(QRect(0,0,quick.art.width(),1000),Qt.TextWordWrap,quick.art.text())
        assert quick.art.wordWrap()
        assert required.width()<=quick.art.width() and required.height()<=quick.art.height()
        assert quick.art.fontMetrics().horizontalAdvance('Carregando')<=quick.art.width()
        assert quick.preview.rect().contains(quick.art.geometry())
        assert quick.title.text()==title and not quick.jobs
    finally:dialog.reject()

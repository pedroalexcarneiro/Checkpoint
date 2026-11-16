import pytest
from dataclasses import asdict
from PySide6.QtCore import QObject,Signal
from PySide6.QtGui import QImage,QColor
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult


@pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
def test_loading_preview_is_blank_until_cover_arrives(library,app,folder,title):
    dialog=GameDialog(library=library);quick=dialog.quick_add
    quick.timer.stop();quick.art.setText('Carregando prévia…')
    result=MetadataResult('rawg','1',title,platforms=('Game Boy Advance',))
    quick.show_result(result)
    dialog.show()
    try:
        for _ in range(6):app.processEvents()
        assert quick.art.text()=='' and quick.art.pixmap().isNull()
        assert quick.preview.rect().contains(quick.art.geometry())
        assert quick.title.text()==title and not quick.jobs
        image=QImage(140,188,QImage.Format_RGB32);color=QColor('#a63772' if title.startswith('Pokémon') else '#389a62');image.fill(color)
        path=folder/'capa pronta.png';assert image.save(str(path))
        class Completed(QObject):done=Signal(object)
        completed=Completed();completed.setProperty('generation',quick.generation);completed.setProperty('operation','catalog_details');completed.done.connect(quick.received)
        completed.done.emit({'result':asdict(result),'preview':{'cover':str(path)}})
        pix=quick.art.pixmap()
        assert quick.art.text()=='' and not pix.isNull()
        assert pix.width()<=quick.art.width() and pix.height()<=quick.art.height()
        assert pix.toImage().pixelColor(pix.width()//2,pix.height()//2)==color
        assert quick.title.text()==title and not quick.jobs
    finally:dialog.reject()

from pathlib import Path
import pytest
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QIcon
from checkpoint.ui_components import service_icon
import checkpoint
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_visual_b_steam_has_real_asset_instead_of_initials(app,library,title):
 library.save_game({'title':title})
 asset=Path(checkpoint.__file__).parent/'assets/services/steam.ico'
 source=QIcon(str(asset)).pixmap(QSize(48,48),1.0).scaled(32,32,Qt.KeepAspectRatio,Qt.SmoothTransformation).toImage()
 rendered=service_icon('Steam').toImage();checked=0
 for x in range(source.width()):
  for y in range(source.height()):
   pixel=source.pixelColor(x,y)
   if pixel.alpha()==255 and min(pixel.red(),pixel.green(),pixel.blue())>220:
    actual=rendered.pixelColor(x+10,y+7)
    assert actual==pixel
    checked+=1
 assert checked>15

from test_bugs_0134 import ui,sample
from checkpoint.collection_views import WishLogo
from PySide6.QtGui import QImage,QColor

def test_wish_banner_fallback_preserves_proportion(ui,folder,app):
 w,i=ui
 for n,title in enumerate(('Zelda: A Link to the Past','Metroid Fusion')):
  image=QImage(400,100+n*100,QImage.Format_RGB32);image.fill(QColor('#00dd55'));path=folder/f'banner{n}.png';image.save(str(path))
  game={**w.library.get(i),'title':title,'banner':str(path),'cover':'','logo':''}
  wish=WishLogo(game)
  try:
   assert not wish.pixmap.isNull()
   assert wish.pixmap.width()/wish.pixmap.height()==400/(100+n*100)
  finally:wish.deleteLater()

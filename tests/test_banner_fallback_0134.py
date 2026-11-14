from PySide6.QtGui import QImage,QColor
from test_bugs_0134 import ui,sample

def test_banner_fills_grid_and_home_without_cover(ui,folder,app):
    from checkpoint.ui_components import GameTile
    from checkpoint.cover_art import cover_pixmap
    w,i=ui;image=QImage(400,600,QImage.Format_RGB32);color=QColor('#a63772');image.fill(color)
    path=folder/'banner.png';assert image.save(str(path))
    w.library.save_game({'title':w.library.get(i)['title'],'banner':str(path)},i)
    game=w.library.get(i);pix=cover_pixmap(game)
    assert pix.width()==400 and pix.height()==600
    tile=GameTile(game,lambda:None,width=200);tile.show();app.processEvents()
    try:
        result=tile.grab().toImage();assert result.width()>=200 and result.height()>=300
        assert result.pixelColor(20,20)==color and result.pixelColor(180,280)==color
        w.navigate(1);app.processEvents();cell=w.gallery.visualItemRect(w.gallery.item(0));view=w.gallery.viewport().grab().toImage()
        assert view.pixelColor(cell.left()+20,cell.top()+20)==color
        cover=folder/'cover.png';image.fill(QColor('#389a62'));assert image.save(str(cover));game['cover']=str(cover)
        assert cover_pixmap(game).toImage().pixelColor(20,20)==QColor('#389a62')
    finally:tile.close();tile.deleteLater()

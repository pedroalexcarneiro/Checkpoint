from test_bugs_0134 import ui,sample
from checkpoint.collection_views import WishGrid,WishCard,WishLogo

def test_wish_maximum_and_columns(ui,app):
 w,i=ui
 for title in ('Zelda: A Link to the Past','Metroid Fusion'):
  game=w.library.save_game({'title':title})
  w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(game,))
 w.library.sql.commit()
 columns=[]
 for width in (1280,2560):
  w.resize(width,800);w.navigate(2)
  for _ in range(4):app.processEvents()
  grid=w.pages[2].findChild(WishGrid);grid.resize(width-300,grid.height());grid.reflow();columns.append(grid.columns)
  for card in grid.findChildren(WishCard):
   assert card.width()<=360
   art=card.findChild(WishLogo);assert art.width()==art.height()
 assert columns[1]>columns[0]

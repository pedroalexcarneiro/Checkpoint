import pytest
from PySide6.QtWidgets import QLabel
from checkpoint.window import MainWindow
from checkpoint.design_system import CardGrid

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_steam_logo_occupancy_matches_drive(app,library,monkeypatch,title):
 monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *a:None)
 library.save_game({'title':title});w=MainWindow(library)
 try:
  w.navigate(5);w.settings_tabs.setCurrentIndex(1);w.show();app.processEvents()
  grid=w.pages[5].findChild(CardGrid,'connectionsGrid')
  bounds=[]
  for provider,card in zip(('Steam','Google Drive'),grid.cards[:2]):
   badge=next(label for label in card.findChildren(QLabel) if not label.pixmap().isNull())
   image=badge.pixmap().toImage();bg=(21,43,73) if provider=='Steam' else (32,41,51)
   points=[(x,y) for x in range(image.width()) for y in range(image.height()) if image.pixelColor(x,y).alpha()>250 and sum(abs(a-b) for a,b in zip(image.pixelColor(x,y).getRgb()[:3],bg))>40]
   xs,ys=zip(*points);bounds.append((min(xs),min(ys),max(xs)-min(xs)+1,max(ys)-min(ys)+1))
  steam,drive=bounds
  assert steam[0]>=5 and steam[1]>=5
  assert steam[2]<=drive[2]+2 and steam[3]<=drive[3]+2
  assert steam[2]>=drive[2]-4 and steam[3]>=drive[3]-4
 finally:w.close();w.deleteLater()

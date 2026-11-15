import pytest
from checkpoint.ui_components import service_icon
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_service_brands_do_not_use_lucide(app,library,monkeypatch,title):
 library.save_game({'title':title})
 def forbidden(*args,**kwargs):pytest.fail('Logo de serviço foi substituída por Lucide')
 monkeypatch.setattr('checkpoint.icons.lucide_icon',forbidden)
 monkeypatch.setattr('checkpoint.ui_components.nav_icon',forbidden)
 pixmaps=[service_icon(provider) for provider in ('Steam','Google Drive','SteamGridDB','RAWG')]
 assert all(not pix.isNull() and pix.width()==pix.height()==48 for pix in pixmaps)
 assert all(a.toImage()!=b.toImage() for index,a in enumerate(pixmaps) for b in pixmaps[index+1:])

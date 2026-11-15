import pytest
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.price_view import display_snapshot
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_official_default(tmp_path,title):
 db=Database(tmp_path/'library.sqlite');lib=Library(db)
 try:
  i=lib.save_game({'title':title})
  lib.set_setting(f'prices.ggdeals.{i}',{'lowest':1000,'current_kind':'keyshop','retail':2000,'keyshop':1000,'currency':'BRL'})
  assert display_snapshot(lib,lib.get(i))['lowest']==2000
 finally:db.close()

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_unknown_cache_is_not_an_official_offer(library,title):
 i=library.save_game({'title':title})
 library.set_setting(f'prices.ggdeals.{i}',{'lowest':1000,'currency':'BRL'})
 assert display_snapshot(library,library.get(i)).get('lowest') is None
 library.set_setting('prices.include_keyshops',True)
 assert display_snapshot(library,library.get(i)).get('lowest') is None
 library.set_setting(f'prices.ggdeals.{i}',{'lowest':1000,'keyshop':1000,'current_kind':'keyshop','retail':2000,'currency':'BRL'})
 assert display_snapshot(library,library.get(i))['lowest']==1000
 library.set_setting('prices.include_keyshops',False)
 assert display_snapshot(library,library.get(i))['lowest']==2000

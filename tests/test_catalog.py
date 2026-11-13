import pytest
from checkpoint.rom_catalog import RomCatalog

def test_catalog_exact_checksum_platform_and_import_idempotence(library,folder):
    dat=folder/'catalog.dat'
    dat.write_text('<datafile><game name="Game"><description>Game USA</description><rom name="game.sfc" size="3" md5="f5c4e398c88b7603991cf8c59674048f" /></game></datafile>',encoding='utf-8')
    catalog=RomCatalog(library)
    assert catalog.import_dat(dat,'SNES')==1
    assert catalog.import_dat(dat,'SNES')==1
    file={'md5':'f5c4e398c88b7603991cf8c59674048f','size':3,'platform':'SNES'}
    assert catalog.candidates(file)[0]['title']=='Game USA'
    assert catalog.candidates({**file,'platform':'PSP'})==[]
    assert library.games()==[]
    dat.write_text('<!DOCTYPE x [<!ENTITY x "test">]><datafile/>',encoding='utf-8')
    with pytest.raises(ValueError): catalog.import_dat(dat,'SNES')

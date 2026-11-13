import pytest
from checkpoint.integrations.drive import rom_identity,DriveScanner

@pytest.mark.parametrize('name,title,platform',[
 ('Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip','Yu-Gi-Oh! - Ultimate Masters 2006','Game Boy Advance'),
 ('Pokemon - Platinum (USA) (Rev 1).nds','Pokemon: Platinum','Nintendo DS'),
 ('Metroid_Fusion [!].gba.zip','Metroid Fusion','Game Boy Advance'),
 ('Zelda (Europe) (En,Fr,De).sfc','Zelda','SNES'),
 ('A Game (The Return).gba','A Game (The Return)','Game Boy Advance')])
def test_rom_identity_cleans_file_metadata_only(name,title,platform):
    assert rom_identity(name)==(title,platform)

def test_drive_records_platform_without_changing_original_name(library):
    name='Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip'
    DriveScanner(library,None).record({'id':'fixture-029','name':name},'/Roms');library.sql.commit()
    row=library.sql.execute('SELECT * FROM game_files').fetchone()
    assert row['original_name']==name and row['platform']=='Game Boy Advance'

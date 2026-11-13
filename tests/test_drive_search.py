from checkpoint.drive_dialog import DriveDialog
from checkpoint.integrations.drive import DriveScanner


def test_rom_search_platform_and_literal_query(library,app):
    scanner=DriveScanner(library,None)
    scanner.record({'id':'gba','name':'Pokémon (USA).gba'},'/GBA/Traduções')
    scanner.record({'id':'ps2','name':'Action_100%.iso'},'/PS2')
    library.sql.commit()
    game_id=scanner.create_game(library.sql.execute("SELECT id FROM game_files WHERE drive_id='ps2'").fetchone()[0],'Título confirmado')
    dialog=DriveDialog(library)
    assert dialog.list.count()==2
    dialog.search.setText('POKEMON');assert dialog.list.count()==1
    assert dialog.files[0]['drive_id']=='gba'
    dialog.search.setText('traducoes');assert dialog.list.count()==1
    dialog.search.setText('titulo confirmado');assert dialog.files[0]['game_id']==game_id
    dialog.search.setText('100%');assert dialog.list.count()==1
    dialog.platform_filter.setCurrentIndex(dialog.platform_filter.findData('Game Boy Advance'))
    assert dialog.list.count()==0 and 'Nenhuma ROM' in dialog.result_count.text()
    assert dialog.selected() is None
    dialog.search.clear();assert dialog.list.count()==1
    dialog.platform_filter.setCurrentIndex(0);assert dialog.list.count()==2
    dialog.list.setCurrentRow(0);selected=dialog.selected()['id'];dialog.refresh()
    assert dialog.selected()['id']==selected
    dialog.search.setText("' OR 1=1 --");assert dialog.list.count()==0
    dialog.close()

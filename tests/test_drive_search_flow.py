"""ROM é um vínculo; texto vem do catálogo e arte vem do SteamGridDB."""
import json
from pathlib import Path
import pytest
from PySide6.QtWidgets import QLabel, QPushButton
from scripts.drive_search_flow_support import EMERALD, ROM_NAME, save_via_drive


@pytest.mark.parametrize('save_during_search', [False, True])
def test_drive_search_saves_metadata_and_link(app, library, folder, save_during_search):
    window, game, file_id, source = save_via_drive(app, library, folder / 'drive-source',
                                                 save_during_search=save_during_search)
    try:
        assert game['developer'] == EMERALD['developer']
        assert game['description'] == EMERALD['description']
        assert game['publisher'] == EMERALD['publisher']
        assert game['release_date'] == EMERALD['release_date']
        assert game['source'] == 'Busca'
        for kind in ('cover', 'banner', 'logo'):
            assert Path(game[kind]).is_file()
        assets = list(library.sql.execute('SELECT kind,provider FROM artwork_assets WHERE game_id=?', (game['id'],)))
        assert {row['kind'] for row in assets} == {'cover', 'banner', 'logo'}
        assert all(row['provider'] == 'steamgriddb' for row in assets)
        rom = library.sql.execute('SELECT * FROM game_files WHERE id=?', (file_id,)).fetchone()
        assert rom['game_id'] == game['id'] and rom['original_name'] == ROM_NAME
        assert rom['available'] == 0
        queries = [json.loads(line)['title'] for line in (source / 'queries-rawg.jsonl').read_text().splitlines()]
        assert queries == ['Pokemon Emerald']
        assert game['platform'] == 'Game Boy Advance'
    finally:
        window.close(); app.processEvents()


@pytest.mark.parametrize('failure', [False, True], ids=['sem-resultado', 'fonte-indisponivel'])
def test_drive_without_metadata_explains_and_offers_manual_search(app, library, folder, failure):
    window, game, file_id, _ = save_via_drive(app, library, folder / 'missing-source',
                                             no_results=not failure, search_failure=failure)
    try:
        assert not game['developer'] and not game['description'] and not game['publisher']
        assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?', (file_id,)).fetchone()[0] == game['id']
        assert any(label.isVisible() and label.text() == 'Não encontramos dados para este jogo. Pesquise manualmente.'
                   for label in window.detail_page.findChildren(QLabel))
        assert any(button.isVisible() and button.isEnabled() and button.text() == 'Pesquisar manualmente'
                   for button in window.detail_page.findChildren(QPushButton))
    finally:
        window.close(); app.processEvents()

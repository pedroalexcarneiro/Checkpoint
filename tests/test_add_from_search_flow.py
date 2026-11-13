"""Regressão: resposta textual selecionada não pode se perder ao salvar."""
from pathlib import Path
from scripts.search_flow_support import METROID, save_via_search


def test_search_selection_persists_text_source_and_images(app, library, folder):
    window, game = save_via_search(app, library, folder / 'search-source')
    try:
        # Confira primeiro as imagens: o caso antigo salvava artes, mas perdia texto.
        assert Path(game['cover']).is_file()
        assert Path(game['banner']).is_file()
        assert game['developer'] == METROID['developer']
        assert game['publisher'] == METROID['publisher']
        assert game['description'] == METROID['description']
        assert game['source'] != 'Manual'
        assert game['source'] == 'Busca'
    finally:
        window.close()
        app.processEvents()


def test_ready_search_result_saves_all_text(app, library, folder):
    window, game = save_via_search(app, library, folder / 'ready-search-source',
                                   save_during_details=False)
    try:
        assert game['developer'] == METROID['developer']
        assert game['publisher'] == METROID['publisher']
        assert game['description'] == METROID['description']
        assert game['source'] == 'Busca'
        assert Path(game['cover']).is_file() and Path(game['banner']).is_file()
    finally:
        window.close()
        app.processEvents()

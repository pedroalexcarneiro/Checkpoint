"""Contratos controlados da API; não equivalem a acesso Steam autenticado."""
import sqlite3
import threading
import time
from contextlib import closing
from urllib.parse import parse_qs, urlsplit

import pytest

from gamevault.database import Database, MIGRATIONS
from gamevault.integrations import IntegrationError
from gamevault.integrations.steam import SteamAchievement, SteamGame, SteamProvider
from gamevault.steam_library import game_accounts, import_games, save_achievements


ACCOUNT = '76561198000000000'
OTHER_ACCOUNT = '76561198000000001'


class Http:
    def __init__(self, payload):
        self.payload = payload
        self.urls = []

    def json(self, url):
        self.urls.append(url)
        return self.payload


def test_owned_games_contract_and_hidden_hours():
    http = Http({'response': {'game_count': 2, 'games': [
        {'appid': 20, 'name': 'Segundo', 'playtime_forever': 125},
        {'appid': 10, 'name': 'Primeiro'},
    ]}})
    games = SteamProvider('example-key', http).owned_games(ACCOUNT)
    assert games == [SteamGame('10', 'Primeiro', None), SteamGame('20', 'Segundo', 125)]
    url = urlsplit(http.urls[0])
    assert url.scheme == 'https' and url.netloc == 'api.steampowered.com'
    assert url.path == '/IPlayerService/GetOwnedGames/v0001/'
    assert parse_qs(url.query) == {'key': ['example-key'], 'steamid': [ACCOUNT], 'include_appinfo': ['1'], 'include_played_free_games': ['1']}
    assert SteamProvider('example-key', Http({'response': {'game_count': 0}})).owned_games(ACCOUNT) == []


@pytest.mark.parametrize('response', [
    {}, {'game_count': 1}, {'game_count': True},
    {'game_count': 1, 'games': [{'appid': 10, 'name': 'Jogo', 'playtime_forever': -1}]},
    {'game_count': 2, 'games': [{'appid': 10, 'name': 'A'}, {'appid': 10, 'name': 'B'}]},
])
def test_private_or_malformed_library_is_not_treated_as_empty(response):
    with pytest.raises(IntegrationError):
        SteamProvider('example-key', Http({'response': response})).owned_games(ACCOUNT)


def test_input_validation_before_network_and_safe_provider_error():
    http = Http({})
    with pytest.raises(ValueError):
        SteamProvider('example-key', http).owned_games('https://steamcommunity.com/id/name')
    assert not http.urls
    class FailingHttp:
        def json(self, url):
            raise IntegrationError(url)
    with pytest.raises(IntegrationError) as error:
        SteamProvider('private-test-key', FailingHttp()).owned_games(ACCOUNT)
    assert 'private-test-key' not in str(error.value) and 'https://' not in str(error.value)


def test_achievements_keep_locked_and_unknown_unlock_date_distinct():
    http = Http({'playerstats': {'success': True, 'achievements': [
        {'apiname': 'LOCKED', 'achieved': 0, 'name': 'Bloqueada'},
        {'apiname': 'NO_DATE', 'achieved': 1, 'unlocktime': 0},
        {'apiname': 'DATED', 'achieved': 1, 'unlocktime': 1700000000, 'name': 'Primeiro passo'},
    ]}})
    rows = SteamProvider('example-key', http).achievements(ACCOUNT, '10')
    assert rows[0].unlocked_at is None and rows[1].unlocked_at == ''
    assert rows[2].unlocked_at == '2023-11-14T22:13:20+00:00'
    query = parse_qs(urlsplit(http.urls[0]).query)
    assert query['appid'] == ['10'] and query['l'] == ['brazilian']
    with pytest.raises(IntegrationError):
        SteamProvider('example-key', Http({'playerstats': {'success': False, 'error': 'private'}})).achievements(ACCOUNT, '10')


def test_import_is_repeatable_and_preserves_local_data_and_separate_accounts(library):
    game_id = library.save_game({'title': 'Meu título', 'notes': 'Pessoal', 'cover': 'minha.png', 'status': 'Jogando'})
    games = [SteamGame('10', 'Título Steam', 120)]
    assert import_games(library, ACCOUNT, games, {'10': game_id}) == (0, 1)
    assert import_games(library, ACCOUNT, [SteamGame('10', 'Nome remoto alterado', 180)]) == (0, 1)
    assert import_games(library, OTHER_ACCOUNT, [SteamGame('10', 'Nome remoto', 60)]) == (0, 1)
    assert len(library.games()) == 1
    game = library.get(game_id)
    assert (game['title'], game['notes'], game['cover'], game['status']) == ('Meu título', 'Pessoal', 'minha.png', 'Jogando')
    assert [row['minutes'] for row in game_accounts(library, game_id)] == [180, 60]
    assert library.stats()['seconds'] == 0 and library.stats()['sessions'] == 0
    assert library.sql.execute('SELECT count(*) FROM achievements').fetchone()[0] == 0


def test_same_name_does_not_merge_without_explicit_choice(library):
    first = library.save_game({'title': 'Mesmo nome'})
    assert import_games(library, ACCOUNT, [SteamGame('10', 'Mesmo nome', 0)]) == (1, 0)
    assert len(library.games()) == 2
    assert library.sql.execute("SELECT game_id FROM external_identifiers WHERE provider='steam'").fetchone()[0] != first
    assert import_games(library, ACCOUNT, []) == (0, 0)
    assert len(library.games()) == 2


def test_conflicting_or_trashed_identity_rolls_back_entire_batch(library):
    import_games(library, ACCOUNT, [SteamGame('10', 'Original', 60)])
    game_id = library.games()[0]['id']
    library.delete(game_id)
    with pytest.raises(ValueError, match='lixeira'):
        import_games(library, ACCOUNT, [SteamGame('20', 'Novo', 0), SteamGame('10', 'Original', 90)])
    assert library.sql.execute('SELECT count(*) FROM games').fetchone()[0] == 1
    assert game_accounts(library, game_id)[0]['minutes'] == 60
    library.restore(game_id)
    with pytest.raises(ValueError, match='outro AppID'):
        import_games(library, ACCOUNT, [SteamGame('30', 'Outro', 0)], {'30': game_id})
    assert library.sql.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'


def test_achievement_snapshot_is_idempotent_and_preserves_personal_records(library):
    import_games(library, ACCOUNT, [SteamGame('10', 'Jogo', 60)])
    game_id = library.games()[0]['id']
    with library.sql:
        library.sql.execute("INSERT INTO achievements(game_id,title,unlocked_at) VALUES(?,'Meu marco','2026-01-01')", (game_id,))
    rows = [SteamAchievement('A', 'Primeira', ''), SteamAchievement('B', 'Segunda', None)]
    save_achievements(library, ACCOUNT, '10', rows)
    save_achievements(library, ACCOUNT, '10', rows)
    account = game_accounts(library, game_id)[0]
    assert (account['achievement_unlocked'], account['achievement_total']) == (1, 2)
    assert account['achievements_checked_at']
    with pytest.raises(ValueError):
        save_achievements(library, ACCOUNT, '10', [rows[0], rows[0]])
    assert game_accounts(library, game_id)[0]['achievement_total'] == 2
    assert library.sql.execute('SELECT title FROM achievements').fetchone()[0] == 'Meu marco'


def test_v3_upgrade_keeps_library_and_creates_recoverable_backup(folder):
    path = folder / 'v3.sqlite'
    with closing(sqlite3.connect(path)) as sql:
        sql.executescript(''.join(MIGRATIONS[:3]) + "PRAGMA user_version=3; INSERT INTO games(title,notes) VALUES('Original','Preservar'); INSERT INTO external_identifiers VALUES(1,'steam','10');")
    db = Database(path)
    try:
        assert db.connection.execute('PRAGMA user_version').fetchone()[0] == 4
        assert tuple(db.connection.execute('SELECT title,notes FROM games').fetchone()) == ('Original', 'Preservar')
        assert db.connection.execute('SELECT count(*) FROM steam_owned_games').fetchone()[0] == 0
        backups = list((folder / 'backups').glob('before-migration-v3-to-v4-*.sqlite'))
        assert len(backups) == 1
        with closing(sqlite3.connect(backups[0])) as backup:
            assert backup.execute('PRAGMA user_version').fetchone()[0] == 3
            assert backup.execute('SELECT notes FROM games').fetchone()[0] == 'Preservar'
            assert backup.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    finally:
        db.close()


def test_dialog_async_query_selection_import_achievements_and_account_change(app, library, monkeypatch):
    from PySide6.QtCore import Qt
    from PySide6.QtTest import QTest
    import gamevault.steam_dialog as module
    from gamevault.window import MainWindow
    main_thread = threading.get_ident()
    class Vault:
        def get(self, name):
            assert name == 'steam'
            return 'example-key'
    class Provider:
        def __init__(self, key):
            assert key == 'example-key'
        def owned_games(self, account):
            assert threading.get_ident() != main_thread
            return [SteamGame('10', 'Primeiro', 120), SteamGame('20', 'Segundo', None)]
        def achievements(self, account, identity):
            assert threading.get_ident() != main_thread
            return [SteamAchievement('A', 'Marco Steam', '')]
    monkeypatch.setattr(module, 'CredentialVault', Vault)
    monkeypatch.setattr(module, 'SteamProvider', Provider)
    monkeypatch.setattr(module.QInputDialog, 'getItem', lambda *args: (args[3][0], True))
    original = library.save_game({'title': 'Meu cadastro', 'notes': 'Preservar'})
    dialog = module.SteamDialog(library)
    window = None
    def wait_job():
        deadline = time.monotonic() + 3
        while dialog.job is not None and time.monotonic() < deadline:
            QTest.qWait(10)
        assert dialog.job is None
    try:
        dialog.account.setText(ACCOUNT)
        dialog.fetch()
        dialog.reject()
        assert 'Aguarde' in dialog.state.text()
        wait_job()
        assert dialog.table.rowCount() == 2 and not dialog.import_button.isEnabled()
        assert len(library.games()) == 1
        dialog.table.setCurrentCell(0, 1)
        dialog.link_selected()
        assert dialog.links == {'10': original}
        dialog.table.item(0, 0).setCheckState(Qt.Checked)
        assert dialog.import_button.isEnabled()
        dialog.import_selected()
        assert [game['title'] for game in library.games()] == ['Meu cadastro']
        assert library.get(original)['notes'] == 'Preservar'
        dialog.table.setCurrentCell(0, 1)
        dialog.fetch_achievements()
        wait_job()
        assert '1/1' in dialog.state.text()
        window = MainWindow(library)
        window.detail(library.games()[0]['id'])
        from PySide6.QtWidgets import QLabel
        texts = [label.text() for label in window.findChildren(QLabel)]
        assert any('2.0 h na Steam' in text for text in texts)
        assert any('Marco Steam' in text and 'Desbloqueada' in text for text in texts)
        assert library.stats()['seconds'] == 0
        dialog.account.setText(OTHER_ACCOUNT)
        assert dialog.table.rowCount() == 0 and not dialog.import_button.isEnabled()
    finally:
        dialog.close()
        dialog.deleteLater()
        if window:
            window.close()
            window.deleteLater()
        app.processEvents()

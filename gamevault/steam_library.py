"""Importação Steam confirmada; horas remotas nunca viram sessões locais."""
from .integrations.steam import steam_id, app_id, nonnegative
from .library import now


def import_games(library, account, games, links=None):
    account = steam_id(account)
    links = links or {}
    games = list(games)
    identities = [app_id(game.app_id) for game in games]
    if len(set(identities)) != len(identities):
        raise ValueError('A seleção contém AppIDs repetidos.')
    if set(links) - set(identities):
        raise ValueError('Associação fora da seleção de jogos.')
    created = updated = 0
    with library.sql:
        for game, identity in zip(games, identities):
            if not isinstance(game.title, str) or not game.title.strip():
                raise ValueError('Jogo Steam sem título.')
            if game.minutes is not None:
                nonnegative(game.minutes)
            existing = library.sql.execute("SELECT game_id FROM external_identifiers WHERE provider='steam' AND external_id=?", (identity,)).fetchone()
            target = links.get(identity)
            if existing and target is not None and target != existing[0]:
                raise ValueError('O AppID já pertence a outro cadastro. Nenhum jogo foi importado.')
            game_id = existing[0] if existing else target
            if game_id is not None:
                if not library.get(game_id):
                    raise ValueError('O cadastro associado está na lixeira ou não existe. Restaure-o antes de importar.')
                other = library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'", (game_id,)).fetchone()
                if other and other[0] != identity:
                    raise ValueError('Este cadastro já está associado a outro AppID Steam.')
                updated += 1
            else:
                game_id = library.sql.execute("INSERT INTO games(title,platform,source) VALUES(?,'PC','Steam')", (game.title.strip(),)).lastrowid
                created += 1
            library.sql.execute("INSERT OR IGNORE INTO external_identifiers VALUES(?,'steam',?)", (game_id, identity))
            library.sql.execute('''INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at)
                VALUES(?,?,?,?,?,?) ON CONFLICT(steam_id,app_id) DO UPDATE SET
                game_id=excluded.game_id,title=excluded.title,minutes=excluded.minutes,checked_at=excluded.checked_at''',
                (account, identity, game_id, game.title.strip(), game.minutes, now()))
    return created, updated


def save_achievements(library, account, identity, achievements):
    account, identity = steam_id(account), app_id(identity)
    if not library.sql.execute('SELECT 1 FROM steam_owned_games WHERE steam_id=? AND app_id=?', (account, identity)).fetchone():
        raise ValueError('Importe este jogo da conta Steam antes de consultar suas conquistas.')
    rows = list(achievements)
    if len({row.api_name for row in rows}) != len(rows):
        raise ValueError('Conquistas Steam duplicadas.')
    with library.sql:
        library.sql.execute('DELETE FROM steam_achievements WHERE steam_id=? AND app_id=?', (account, identity))
        library.sql.executemany('INSERT INTO steam_achievements VALUES(?,?,?,?,?,?)',
            [(account, identity, row.api_name, row.title, row.unlocked_at, now()) for row in rows])
        library.sql.execute('UPDATE steam_owned_games SET achievements_checked_at=? WHERE steam_id=? AND app_id=?', (now(), account, identity))


def game_accounts(library, game_id):
    return [dict(row) for row in library.sql.execute('''SELECT s.*,
        (SELECT count(*) FROM steam_achievements a WHERE a.steam_id=s.steam_id AND a.app_id=s.app_id) AS achievement_total,
        (SELECT count(*) FROM steam_achievements a WHERE a.steam_id=s.steam_id AND a.app_id=s.app_id AND a.unlocked_at IS NOT NULL) AS achievement_unlocked
        FROM steam_owned_games s WHERE s.game_id=? ORDER BY s.steam_id''', (game_id,))]

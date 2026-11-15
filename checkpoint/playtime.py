"""Totais de apresentação: sessões locais e um snapshot remoto por jogo."""
def format_time(seconds):
    minutes=max(0,int(seconds or 0))//60
    return f'{minutes//60}h{minutes%60:02d}min'


def total_seconds(library,game_id):
    local=library.sql.execute("SELECT COALESCE(SUM(duration_seconds),0) FROM play_sessions WHERE game_id=? AND state='finished'",(game_id,)).fetchone()[0]
    # Contas diferentes são snapshots do mesmo jogo; não multiplicar sessões por joins.
    remote=library.sql.execute('SELECT COALESCE(MAX(minutes),0) FROM steam_owned_games WHERE game_id=?',(game_id,)).fetchone()[0]
    return local+remote*60


def collection_times(library):
    # Agregar cada fonte antes de combinar: joins poderiam multiplicar sessões
    # por contas Steam. O número de consultas não cresce com a biblioteca.
    owned=library.owned_games()
    local=dict(library.sql.execute("SELECT game_id,SUM(duration_seconds) FROM play_sessions WHERE state='finished' GROUP BY game_id"))
    remote=dict(library.sql.execute('SELECT game_id,MAX(minutes) FROM steam_owned_games GROUP BY game_id'))
    return {game['id']:(local.get(game['id']) or 0)+(remote.get(game['id']) or 0)*60 for game in owned}

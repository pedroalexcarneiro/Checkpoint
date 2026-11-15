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
    return {game['id']:total_seconds(library,game['id']) for game in library.games() if library.is_owned(game['id'])}

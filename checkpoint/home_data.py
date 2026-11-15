"""Dados locais do Início; execução comprovada, períodos e ofertas compatíveis."""
from datetime import datetime, timezone
from .playtime import collection_times
from .statistics_periods import instant, period_stats


def execution_history(library, limit=None, now=None):
    end=now or datetime.now(timezone.utc)
    owned={g['id']:g for g in library.owned_games()}
    records=[]
    for row in library.sql.execute("SELECT * FROM play_sessions WHERE state IN ('active','finished','interrupted') AND pid>0"):
        if row['game_id'] not in owned:continue
        try:stamp=instant(row['started_at'])
        except (ValueError,TypeError):continue
        if stamp>end:continue
        records.append({**dict(row),'game':owned[row['game_id']],'instant':stamp})
    records.sort(key=lambda r:(r['instant'],r['id']),reverse=True)
    return records if limit is None else records[:limit]


def recent_games(library, limit=2, now=None):
    selected=[];seen=set();totals=collection_times(library)
    for record in execution_history(library,now=now):
        game=record['game']
        if game['id'] in seen:continue
        seen.add(game['id']);selected.append({**game,'last_played':record['started_at'],
                                             'seconds':totals.get(game['id'],0)})
        if limit is not None and len(selected)>=limit:break
    return selected


def week_summary(library, now=None, zone='local'):
    result=period_stats(library,'weekly',now,zone)
    start,end=result['bounds'];owned={g['id'] for g in library.owned_games()};started=set()
    for row in library.sql.execute("SELECT game_id,started_at FROM play_sessions WHERE state='finished' AND duration_seconds>0"):
        if row['game_id'] not in owned:continue
        try:stamp=instant(row['started_at'])
        except (ValueError,TypeError):continue
        if start<=stamp<end:started.add(row['game_id'])
    return {**result,'started_games':len(started)}


def wish_offers(library, limit=3):
    from .prices import selected_quote
    games=[dict(r) for r in library.sql.execute('SELECT g.* FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL')]
    result=[]
    for game in games:
        value=selected_quote(library,game['id'])
        if value.get('state')!='ready' or value.get('currency','BRL')!='BRL':continue
        if type(value.get('lowest')) is not int or value['lowest']<=0:continue
        if value.get('current_kind') not in ('retail','keyshop'):continue
        result.append({**game,'quote':value})
    def key(game):
        discount=game['quote'].get('discount');valid=type(discount) is int and discount>0
        return (not valid,-discount if valid else 0,game['title'].casefold(),game['id'])
    return sorted(result,key=key)[:limit]


def recent_memories(library):
    records=[{**dict(r),'kind':'diary'} for r in library.sql.execute('SELECT d.*,g.title FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL')]
    records.extend(dict(r) for r in library.sql.execute('SELECT m.*,g.title FROM media_files m JOIN games g ON g.id=m.game_id WHERE g.deleted_at IS NULL'))
    def key(row):
        try:stamp=instant(row['created_at'])
        except (ValueError,TypeError):stamp=datetime.min.replace(tzinfo=timezone.utc)
        return stamp,row['id'],row['kind']
    return sorted(records,key=key,reverse=True)

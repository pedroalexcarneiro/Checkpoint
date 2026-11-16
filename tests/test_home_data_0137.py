from datetime import datetime, timedelta, timezone
import pytest


def add_session(lib, identity, when, seconds=3600, state='finished', pid=123):
    with lib.sql:
        lib.sql.execute('INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?,?,?)',
                        (identity, when.isoformat(), (when+timedelta(seconds=seconds)).isoformat(), seconds, state, pid))


@pytest.mark.parametrize('titles', [('Portal 2', 'Hades'), ('Celeste', 'Metroid Fusion')])
def test_recent_games_use_real_start_not_status_or_updated_at(library, titles):
    from checkpoint.home_data import recent_games, execution_history
    now=datetime(2026,11,15,18,tzinfo=timezone.utc)
    a=library.save_game({'title':titles[0],'status':'Concluído'})
    b=library.save_game({'title':titles[1],'status':'Jogando'})
    assert recent_games(library, now=now)==[]
    add_session(library,a,now-timedelta(days=2))
    add_session(library,b,now-timedelta(days=1),state='interrupted')
    add_session(library,a,now+timedelta(days=1))
    add_session(library,a,now-timedelta(hours=1),pid=None)
    library.save_game({'title':titles[0],'status':'Jogando'},a)
    rows=recent_games(library,now=now)
    assert [r['id'] for r in rows]==[b,a]
    assert len(execution_history(library,now=now))==2
    assert rows[0]['last_played']==(now-timedelta(days=1)).isoformat()


def test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed(library):
    from checkpoint.home_data import week_summary
    now=datetime(2026,11,15,18,tzinfo=timezone.utc)
    a=library.save_game({'title':'Portal 2'});b=library.save_game({'title':'Hades'})
    add_session(library,a,datetime(2026,11,8,23,30,tzinfo=timezone.utc),7200)
    add_session(library,b,now-timedelta(hours=2),3600)
    add_session(library,b,now-timedelta(hours=1),state='interrupted')
    add_session(library,b,now-timedelta(minutes=20),state='active')
    with library.sql:
        library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES('1','620',?,'Portal 2',9000,'2026-11-15')",(a,))
    before=[tuple(r) for r in library.sql.execute('SELECT * FROM play_sessions')]
    result=week_summary(library,now=now,zone=timezone.utc)
    assert result['seconds']==9000 and result['sessions']==2 and result['started_games']==1
    assert result['bounds'][0]==datetime(2026,11,9,tzinfo=timezone.utc)
    assert [tuple(r) for r in library.sql.execute('SELECT * FROM play_sessions')]==before


def test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache(library):
    from checkpoint.home_data import wish_offers
    ids=[]
    for title in ('A oferta atual','B desconto','C console','D falha','E sem origem'):
        i=library.save_game({'title':title,'platform':'Switch' if title=='C console' else 'PC'});ids.append(i)
        with library.sql:
            library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
            library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
        value={'retail':4990,'currency':'BRL','state':'ready','checked_at':datetime.now(timezone.utc).isoformat(),'offer_context':{'steam':str(i),'platform':'PC'}}
        if title=='B desconto':value['offers']=[{'cents':4990,'original':9980,'kind':'retail','shop':'Loja teste','url':'https://gg.deals/br/redirect/test/'}]
        if title=='D falha':value['state']='unavailable'
        if title=='E sem origem':value={'lowest':100,'currency':'BRL','state':'ready'}
        library.set_setting(f'prices.ggdeals.{i}',value)
    offers=wish_offers(library)
    assert [g['id'] for g in offers]==[ids[1],ids[0]]
    assert offers[0]['quote']['discount']==50
    assert library.get(ids[2])['platform']=='Switch'


@pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
    from checkpoint.home_data import wish_offers
    end=datetime(2026,11,16,12,tzinfo=timezone.utc)
    identities=[]
    for title in ('Portal 2','Hades'):
        identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
        with library.sql:
            library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
            library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
        library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
    before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
    assert wish_offers(library,now=end)==[]
    assert [library.setting(f'prices.ggdeals.{identity}') for identity in identities]==before
    for identity in identities:
        value=library.setting(f'prices.ggdeals.{identity}');value['checked_at']=(end-timedelta(seconds=3599)).isoformat();library.set_setting(f'prices.ggdeals.{identity}',value)
    assert {game['id'] for game in wish_offers(library,now=end)}==set(identities)

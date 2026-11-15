"""Períodos locais de calendário; recorte em instantes UTC, sem alterar sessões."""
from calendar import monthrange
from collections import defaultdict
from datetime import datetime,time,timedelta,timezone

PERIODS=(('Diário','daily'),('Semanal','weekly'),('Mensal','monthly'),('Últimos 3 meses','3m'),('Últimos 6 meses','6m'),('Últimos 12 meses','12m'),('Todo o período','all'))


def local(value,zone):
    return value.astimezone(None if zone=='local' else zone)


def attach(value,zone):
    return value.astimezone() if zone=='local' else value.replace(tzinfo=zone)


def period_bounds(period,now=None,zone='local'):
    now=now or datetime.now(timezone.utc)
    if now.tzinfo is None:raise ValueError('O instante de referência precisa de fuso.')
    end=now.astimezone(timezone.utc);current=local(end,zone);day=current.date()
    if period=='all':return None,end
    if period=='daily':start=datetime.combine(day,time.min)
    elif period=='weekly':start=datetime.combine(day-timedelta(days=day.weekday()),time.min)
    elif period=='monthly':start=datetime.combine(day.replace(day=1),time.min)
    elif period in ('3m','6m','12m'):
        month=current.year*12+current.month-1-int(period[:-1]);year,month=divmod(month,12);month+=1
        start=current.replace(tzinfo=None,year=year,month=month,day=min(current.day,monthrange(year,month)[1]))
    else:raise ValueError('Período estatístico inválido.')
    return attach(start,zone).astimezone(timezone.utc),end


def instant(value):
    result=datetime.fromisoformat(value.replace('Z','+00:00'))
    return result.replace(tzinfo=timezone.utc) if result.tzinfo is None else result.astimezone(timezone.utc)


def period_stats(library,period='12m',now=None,zone='local'):
    start,end=period_bounds(period,now,zone);owned={g['id']:g for g in library.owned_games()}
    daily=defaultdict(float);top=defaultdict(float);durations=[];completions=defaultdict(int)
    for row in library.sql.execute("SELECT * FROM play_sessions WHERE state='finished' AND duration_seconds>0"):
        if row['game_id'] not in owned:continue
        try:a=instant(row['started_at'])
        except (ValueError,TypeError):continue
        b=min(a+timedelta(seconds=row['duration_seconds']),end)
        if start is not None:a=max(a,start)
        if a>=b:continue
        seconds=(b-a).total_seconds();durations.append(seconds);top[row['game_id']]+=seconds
        while a<b:
            current=local(a,zone)
            midnight=attach(datetime.combine(current.date()+timedelta(days=1),time.min),zone).astimezone(timezone.utc)
            stop=min(b,midnight);portion=(stop-a).total_seconds()
            if portion<=0:raise ValueError('Não foi possível calcular o limite de dia neste fuso.')
            daily[current.date().isoformat()]+=portion;a=stop
    for game in owned.values():
        if not game['completed_at']:continue
        try:stamp=instant(game['completed_at'])
        except (ValueError,TypeError):continue
        if (start is None or stamp>=start) and stamp<end:completions[local(stamp,zone).strftime('%Y-%m')]+=1
    first=local(start,zone).date() if start else min((datetime.fromisoformat(d).date() for d in daily),default=local(end,zone).date())
    return {'seconds':sum(durations),'sessions':len(durations),'average':sum(durations)/len(durations) if durations else 0,'daily':dict(sorted(daily.items())),
            'top':[{'id':i,'title':owned[i]['title'],'seconds':seconds} for i,seconds in sorted(top.items(),key=lambda x:(-x[1],owned[x[0]]['title'].casefold(),x[0]))],
            'completions':dict(sorted(completions.items())),'bounds':(start,end),'dates':(first,local(end,zone).date())}

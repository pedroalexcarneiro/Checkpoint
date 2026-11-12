import json
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from pathlib import Path

STATUSES = ('Não iniciado', 'Backlog', 'Jogando', 'Pausado', 'Concluído', 'Abandonado')
FIELDS = ('title','description','developer','publisher','release_date','platform','genre','status',
          'rating','favorite','notes','source','cover','banner','logo','executable','category')

def now():
    return datetime.now(timezone.utc).isoformat()

def clean_game_data(data):
    clean = {key: data[key] for key in FIELDS if key in data}
    if not clean.get('title', '').strip():
        raise ValueError('Informe o nome do jogo.')
    clean['title'] = clean['title'].strip()
    if clean.get('status', STATUSES[0]) not in STATUSES:
        raise ValueError('Status inválido.')
    if clean.get('rating') is not None and not 0 <= int(clean['rating']) <= 10:
        raise ValueError('A nota deve estar entre 0 e 10.')
    return clean

class Library:
    def __init__(self, database):
        self.db = database
        self.sql = database.connection

    def save_game(self, data, game_id=None):
        clean = clean_game_data(data)
        with self.sql:
            if game_id is None:
                if clean.get('status') == 'Concluído': clean['completed_at'] = now()
                keys = ','.join(clean)
                return self.sql.execute(f'INSERT INTO games({keys}) VALUES({",".join("?" for _ in clean)})', list(clean.values())).lastrowid
            old = self.get(game_id)
            if old is None:
                raise ValueError('Jogo não encontrado.')
            clean['updated_at'] = now()
            if clean.get('status') == 'Concluído' and old['status'] != 'Concluído':
                clean['completed_at'] = now()
            self.sql.execute(f'UPDATE games SET {",".join(k+"=?" for k in clean)} WHERE id=?', [*clean.values(),game_id])
            return game_id

    def get(self, game_id):
        row = self.sql.execute('SELECT * FROM games WHERE id=? AND deleted_at IS NULL', (game_id,)).fetchone()
        return dict(row) if row else None

    def games(self, search='', platform='', genre='', status='', favorite=False, sort='title'):
        clauses, args = ['deleted_at IS NULL'], []
        if search:
            clauses.append("title LIKE ? ESCAPE '\\'")
            args.append('%'+search.replace('\\','\\\\').replace('%','\\%').replace('_','\\_')+'%')
        for key, value in [('platform',platform),('status',status)]:
            if value:
                clauses.append(key+'=?'); args.append(value)
        if favorite:
            clauses.append('favorite=1')
        order = {'title':'title COLLATE NOCASE','recent':'created_at DESC, id DESC','rating':'rating DESC, title'}.get(sort,'title COLLATE NOCASE')
        rows = [dict(r) for r in self.sql.execute('SELECT * FROM games WHERE '+' AND '.join(clauses)+' ORDER BY '+order,args)]
        return [row for row in rows if not genre or genre in {part.strip() for part in row['genre'].split(',')}]

    def delete(self, game_id):
        with self.sql:
            self.sql.execute('UPDATE games SET deleted_at=? WHERE id=?',(now(),game_id))

    def restore(self, game_id):
        with self.sql:
            self.sql.execute('UPDATE games SET deleted_at=NULL WHERE id=?',(game_id,))
            for provider,identity in self.setting(f'trash.identities.{game_id}',[]):
                self.sql.execute('INSERT OR IGNORE INTO external_identifiers VALUES(?,?,?)',(game_id,provider,identity))

    def setting(self, key, default=None):
        row = self.sql.execute('SELECT value FROM settings WHERE key=?',(key,)).fetchone()
        return json.loads(row[0]) if row else default

    def set_setting(self, key, value):
        with self.sql:
            self.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(key,json.dumps(value)))

    def diary(self, game_id):
        return [dict(r) for r in self.sql.execute('SELECT * FROM diary_entries WHERE game_id=? ORDER BY created_at DESC,id DESC',(game_id,))]

    def add_diary(self, game_id, text):
        if not text.strip():
            raise ValueError('Escreva uma memória antes de salvar.')
        with self.sql:
            self.sql.execute('INSERT INTO diary_entries(game_id,created_at,text) VALUES(?,?,?)',(game_id,now(),text.strip()))

    def add_media(self, game_id, path, caption=''):
        path = Path(path).resolve(strict=True)
        extension = path.suffix.lower()
        if extension not in {'.png','.jpg','.jpeg','.webp','.mp4','.mkv','.avi','.mov'}:
            raise ValueError('Formato de mídia não suportado.')
        with self.sql:
            self.sql.execute('INSERT INTO media_files(game_id,path,caption,created_at,kind) VALUES(?,?,?,?,?)',
                             (game_id,str(path),caption,now(),'image' if extension in {'.png','.jpg','.jpeg','.webp'} else 'video'))

    def stats(self):
        games = self.games()
        rows = self.sql.execute("SELECT s.*,g.title FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE g.deleted_at IS NULL AND s.state='finished'").fetchall()
        durations = [r['duration_seconds'] for r in rows]
        today = datetime.now(timezone.utc).date()
        weekly, monthly, top = defaultdict(int), defaultdict(int), defaultdict(int)
        # Distribui sessões entre dias em UTC, em vez de atribuir tudo ao dia de início.
        daily = defaultdict(float)
        for row in rows:
            top[(row['game_id'],row['title'])] += row['duration_seconds']
            try: start = datetime.fromisoformat(row['started_at'].replace('Z','+00:00'))
            except ValueError: continue
            if start.tzinfo is None: start = start.replace(tzinfo=timezone.utc)
            start = start.astimezone(timezone.utc)
            remaining = row['duration_seconds']
            while remaining > 0:
                midnight = (start+timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0)
                portion = min(remaining,(midnight-start).total_seconds())
                daily[start.date()] += portion
                remaining -= portion; start = midnight
        for day,seconds in daily.items():
            monday = day-timedelta(days=day.weekday())
            weekly[monday.isoformat()] += seconds
            monthly[day.strftime('%Y-%m')] += seconds
        completions = defaultdict(int)
        for game in games:
            if game['completed_at']: completions[game['completed_at'][:7]] += 1
        genres = defaultdict(int)
        for game in games:
            for genre in {g.strip() for g in game['genre'].split(',') if g.strip()}: genres[genre] += 1
        return {'total':len(games), 'statuses':{s:sum(g['status']==s for g in games) for s in STATUSES},
                'seconds':sum(durations), 'sessions':len(rows), 'average':sum(durations)/len(rows) if rows else 0,
                'platforms':{p:sum(g['platform']==p for g in games) for p in sorted({g['platform'] for g in games})},
                'genres':dict(genres),'weekly':dict(sorted(weekly.items())[-8:]),'monthly':dict(sorted(monthly.items())[-12:]),
                'completions':dict(sorted(completions.items())),
                'top':[{'id':key[0],'title':key[1],'seconds':value} for key,value in sorted(top.items(),key=lambda item:item[1],reverse=True)[:10]]}

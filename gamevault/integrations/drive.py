"""Drive somente leitura para ROMs. Nunca expõe operações de exclusão remota."""
import hashlib
import json
import re
from collections import deque
from pathlib import Path
from uuid import uuid4
from . import IntegrationError

ROM_EXTENSIONS = {'.3ds','.cia','.nds','.gba','.gb','.gbc','.sfc','.smc','.nes','.n64','.z64','.v64',
                  '.iso','.cso','.chd','.cue','.bin','.wbfs','.wud','.wux','.rpx','.nsp','.xci','.zip','.7z','.rvz'}
PLATFORMS = {'nintendo 3ds':'Nintendo 3DS','nintendo ds':'Nintendo DS','nintendo game boy advance':'Game Boy Advance',
             'gba':'Game Boy Advance','nintendo wii u':'Wii U','wii u':'Wii U','psp':'PSP','snes':'SNES','nintendo switch':'Nintendo Switch'}
FILE_FIELDS = 'id,name,mimeType,size,parents,modifiedTime,md5Checksum,trashed'

def validate_id(file_id):
    if not re.fullmatch(r'[A-Za-z0-9_-]+',file_id): raise ValueError('Identificador do Drive inválido.')
    return file_id

def normalize_rom_name(name):
    name = Path(name).stem
    return re.sub(r'\s+',' ',re.sub(r'\([^)]*\)|\[[^]]*\]','',name).replace('_',' ')).strip()

def platform_for(path):
    for part in reversed(path.split('/')):
        if part.casefold() in PLATFORMS: return PLATFORMS[part.casefold()]
    return ''

class GoogleDriveClient:
    def __init__(self,service): self.service = service

    @classmethod
    def authenticate(cls,client_json,vault,interactive=False):
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        scopes = ['https://www.googleapis.com/auth/drive.readonly']
        stored = vault.get('drive-readonly')
        creds = Credentials.from_authorized_user_info(json.loads(stored),scopes) if stored else None
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        if not creds or not creds.valid:
            if not interactive: raise IntegrationError('Drive aguardando autenticação.')
            flow = InstalledAppFlow.from_client_secrets_file(client_json,scopes)
            creds = flow.run_local_server(host='localhost',port=0,open_browser=True,timeout_seconds=180)
        vault.set('drive-readonly',creds.to_json())
        import httplib2
        from google_auth_httplib2 import AuthorizedHttp
        http = AuthorizedHttp(creds,http=httplib2.Http(timeout=30))
        return cls(build('drive','v3',http=http,cache_discovery=False))

    def start_token(self):
        return self.service.changes().getStartPageToken().execute(num_retries=3)['startPageToken']

    def children(self,parent):
        token = None
        while True:
            data = self.service.files().list(q=f"'{validate_id(parent)}' in parents and trashed=false",
                fields=f'nextPageToken,files({FILE_FIELDS})',pageSize=1000,pageToken=token).execute(num_retries=3)
            yield from data.get('files',[])
            token = data.get('nextPageToken')
            if not token: break

    def changes(self,token):
        return self.service.changes().list(pageToken=token,pageSize=1000,
            fields=f'nextPageToken,newStartPageToken,changes(fileId,removed,file({FILE_FIELDS}))').execute(num_retries=3)

    def download(self,file_id,target):
        from googleapiclient.http import MediaIoBaseDownload
        with open(target,'wb') as stream:
            downloader = MediaIoBaseDownload(stream,self.service.files().get_media(fileId=validate_id(file_id)),chunksize=4*1024*1024)
            done = False
            while not done: _,done = downloader.next_chunk(num_retries=3)

class DriveScanner:
    def __init__(self,library,client): self.library = library; self.client = client

    def record(self,file,path):
        if hasattr(self,'seen_files'): self.seen_files.add(file['id'])
        extension = Path(file['name']).suffix.lower()
        if extension not in ROM_EXTENSIONS: return 0
        previous = self.library.sql.execute('SELECT md5,modified_at FROM game_files WHERE drive_id=?',(file['id'],)).fetchone()
        changed = previous and (previous['md5'] != file.get('md5Checksum') or previous['modified_at'] != file.get('modifiedTime'))
        self.library.sql.execute('''INSERT INTO game_files(drive_id,original_name,extension,size,parent_id,folder_path,modified_at,md5,platform)
            VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(drive_id) DO UPDATE SET original_name=excluded.original_name,
            extension=excluded.extension,size=excluded.size,parent_id=excluded.parent_id,folder_path=excluded.folder_path,
            modified_at=excluded.modified_at,md5=excluded.md5,platform=excluded.platform''',
            (file['id'],file['name'],extension,int(file['size']) if file.get('size') else None,
             (file.get('parents') or [None])[0],path,file.get('modifiedTime'),file.get('md5Checksum'),platform_for(path)))
        if changed:
            self.library.sql.execute("UPDATE game_files SET review_state='remote_changed' WHERE drive_id=?",(file['id'],))
        return 1

    def walk(self,root,path,folders):
        pending = deque([(root,path)]); seen = set(); count = 0
        while pending:
            parent,folder_path = pending.popleft()
            if parent in seen: continue
            seen.add(parent); folders[parent] = folder_path
            for file in self.client.children(parent):
                if file['mimeType']=='application/vnd.google-apps.folder':
                    pending.append((file['id'],folder_path+'/'+file['name']))
                else: count += self.record(file,folder_path)
        return count

    def full_scan(self,root):
        validate_id(root)
        previous = self.library.setting('drive_scan',{})
        if previous and previous['root'] != root: raise IntegrationError('Troca de raiz exige uma biblioteca separada nesta versão.')
        token = self.client.start_token(); folders = {}; self.seen_files = set()
        # Token capturado antes da varredura: alterações concorrentes serão reaplicadas.
        with self.library.sql:
            count = self.walk(root,'',folders)
            for existing in self.library.sql.execute('SELECT drive_id FROM game_files WHERE drive_id IS NOT NULL').fetchall():
                if existing['drive_id'] not in self.seen_files:
                    self.library.sql.execute("UPDATE game_files SET review_state='remote_missing' WHERE drive_id=?",(existing['drive_id'],))
            self.library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                                     ('drive_scan',json.dumps({'root':root,'token':token,'folders':folders})))
        return count

    def incremental(self):
        state = self.library.setting('drive_scan')
        if not state: raise IntegrationError('Faça a varredura inicial primeiro.')
        token = state['token']; folders = state['folders']; count = 0
        while token:
            page = self.client.changes(token)
            with self.library.sql:
                for change in page.get('changes',[]):
                    file_id = change['fileId']; file = change.get('file',{})
                    if change.get('removed') or file.get('trashed'):
                        removed_path = folders.get(file_id)
                        if removed_path is not None:
                            affected = [key for key,path in folders.items() if key==file_id or path.startswith(removed_path+'/')]
                            for key in affected:
                                self.library.sql.execute("UPDATE game_files SET review_state='remote_removed' WHERE parent_id=?",(key,)); folders.pop(key,None)
                        self.library.sql.execute("UPDATE game_files SET review_state='remote_removed' WHERE drive_id=?",(file_id,)); continue
                    parent = next((p for p in file.get('parents',[]) if p in folders),None)
                    if parent is None:
                        if file_id == state['root']: continue
                        old_path = folders.get(file_id)
                        if old_path is not None:
                            affected = [key for key,path in folders.items() if key==file_id or path.startswith(old_path+'/')]
                            for key in affected:
                                self.library.sql.execute("UPDATE game_files SET review_state='outside_root' WHERE parent_id=?",(key,)); folders.pop(key,None)
                        self.library.sql.execute("UPDATE game_files SET review_state='outside_root' WHERE drive_id=?",(file_id,)); continue
                    if file.get('mimeType')=='application/vnd.google-apps.folder':
                        count += self.walk(file_id,folders[parent]+'/'+file['name'],folders)
                    else: count += self.record(file,folders[parent])
                state['token'] = page.get('nextPageToken') or page.get('newStartPageToken')
                state['folders'] = folders
                if not state['token']: raise IntegrationError('Resposta de alterações sem cursor.')
                self.library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',('drive_scan',json.dumps(state)))
            token = page.get('nextPageToken')
        return count

    def associate(self,file_id,game_id):
        if not self.library.get(game_id): raise ValueError('Jogo não encontrado.')
        with self.library.sql:
            cursor = self.library.sql.execute("UPDATE game_files SET game_id=?,review_state='confirmed' WHERE id=?",(game_id,file_id))
            if cursor.rowcount!=1: raise ValueError('Arquivo não encontrado.')
            self.library.sql.execute('INSERT OR IGNORE INTO rom_versions(file_id) VALUES(?)',(file_id,))

    def download(self,file_id,directory):
        row = self.library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
        if not row: raise ValueError('Arquivo não encontrado.')
        directory = Path(directory).resolve(); directory.mkdir(parents=True,exist_ok=True)
        # Nome local por ID; nome original é preservado no banco.
        target = directory/(validate_id(row['drive_id'])+row['extension'])
        if target.exists(): raise ValueError('Arquivo local já existe; nenhum arquivo foi substituído.')
        partial = target.with_name(target.name+'.'+uuid4().hex+'.partial')
        self.client.download(row['drive_id'],partial)
        if row['size'] is not None and partial.stat().st_size!=row['size']:
            raise IntegrationError('Tamanho divergente; download parcial preservado para diagnóstico.')
        if row['md5']:
            checksum = hashlib.md5(usedforsecurity=False)
            with partial.open('rb') as stream:
                for block in iter(lambda:stream.read(1024*1024),b''): checksum.update(block)
            if checksum.hexdigest()!=row['md5']: raise IntegrationError('MD5 divergente. Arquivo não disponibilizado.')
        partial.replace(target)
        with self.library.sql:
            self.library.sql.execute('UPDATE game_files SET local_path=?,available=1 WHERE id=?',(str(target),file_id))
        return target

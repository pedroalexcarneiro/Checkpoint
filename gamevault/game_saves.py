"""Histórico local de backups por perfil; cada worker usa sua própria conexão."""
import json
from pathlib import Path
from .database import Database
from .library import Library,now
from .save_profiles import SaveProfiles
from .saves import SaveBackupService

class GameSaveBackups:
    def __init__(self,library): self.library=library
    def history(self,game_id):
        return [dict(row) for row in self.library.sql.execute('''SELECT b.*,c.directory FROM save_backups b
            JOIN save_configurations c ON c.id=b.configuration_id WHERE c.game_id=? ORDER BY b.id DESC''',(game_id,))]
    def create(self,game_id):
        profile=SaveProfiles(self.library).latest(game_id)
        if not profile: raise ValueError('Configure a pasta de saves deste jogo primeiro.')
        destination=self.library.setting('save_backups')
        if not destination: raise ValueError('Selecione a pasta de backups nas Configurações.')
        path,checksum,manifest=SaveBackupService(Path(destination)/str(game_id)).create(profile['directory'],json.loads(profile['patterns_json']))
        try:
            with self.library.sql:
                backup_id=self.library.sql.execute('INSERT INTO save_backups(configuration_id,created_at,path,sha256,manifest_json) VALUES(?,?,?,?,?)',
                    (profile['id'],now(),str(path),checksum,json.dumps(manifest))).lastrowid
        except Exception:
            # O ZIP íntegro permanece no disco mesmo se o banco falhar.
            raise RuntimeError('Backup criado no disco, mas não registrado no histórico: '+str(path)) from None
        return {'id':backup_id,'path':str(path),'game_id':game_id}
    def restore(self,game_id,backup_id):
        backup=next((row for row in self.history(game_id) if row['id']==backup_id),None)
        if not backup: raise ValueError('Backup não pertence a este jogo.')
        return str(SaveBackupService(Path(backup['path']).parent).restore(backup['path'],backup['directory'],backup['sha256']))

def run_save_operation(database_path,game_id,backup_id=None):
    db=Database(database_path)
    try:
        service=GameSaveBackups(Library(db))
        return service.create(game_id) if backup_id is None else service.restore(game_id,backup_id)
    finally: db.close()

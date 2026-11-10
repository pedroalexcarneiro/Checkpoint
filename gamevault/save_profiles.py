"""Configuração persistente e explícita de saves tradicionais por jogo."""
import json
from pathlib import Path
from .saves import FORBIDDEN

class SaveProfiles:
    def __init__(self,library): self.library=library
    def configure(self,game_id,directory,patterns):
        if not self.library.get(game_id): raise ValueError('Jogo não encontrado.')
        directory=Path(directory).resolve(strict=True)
        if not directory.is_dir(): raise ValueError('Selecione uma pasta.')
        patterns=list(dict.fromkeys(patterns))
        if not patterns or any(not p or p in {'*','*.*'} or '/' in p or '\\' in p or ':' in p for p in patterns):
            raise ValueError('Use padrões específicos de arquivos tradicionais de save.')
        if any(Path(p).suffix.lower() in FORBIDDEN for p in patterns):
            raise ValueError('Save states não são aceitos.')
        with self.library.sql:
            self.library.sql.execute('DELETE FROM save_configurations WHERE game_id=? AND id NOT IN (SELECT configuration_id FROM save_backups WHERE configuration_id IS NOT NULL)',(game_id,))
            return self.library.sql.execute('INSERT INTO save_configurations(game_id,directory,patterns_json) VALUES(?,?,?)',(game_id,str(directory),json.dumps(patterns))).lastrowid
    def latest(self,game_id):
        row=self.library.sql.execute('SELECT * FROM save_configurations WHERE game_id=? ORDER BY id DESC LIMIT 1',(game_id,)).fetchone()
        return dict(row) if row else None

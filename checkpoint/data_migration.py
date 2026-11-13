"""Cópia conservadora dos dados legados, sem alterar schema ou remover a origem."""
from contextlib import closing
import fnmatch
import json
import logging
import os
from pathlib import Path
import shutil
import sqlite3
import sys
from uuid import uuid4
from PySide6.QtCore import QLockFile

# Nome de compatibilidade montado apenas aqui; nunca é a identidade do produto.
LEGACY_PRODUCT = 'Game' + 'Vault'
DATABASE_NAME = 'checkpoint.sqlite'
LEGACY_DATABASE = LEGACY_PRODUCT.lower() + '.sqlite'


class MigrationError(RuntimeError):
    def __init__(self,message,legacy_path):
        super().__init__(message);self.legacy_path=Path(legacy_path)
    def user_message(self):
        return f'{self}\n\nSeus dados originais foram preservados em:\n{self.legacy_path}'


class DataSession:
    def __init__(self,directory,locks):self.directory=directory;self.locks=locks
    def close(self):
        for lock in reversed(self.locks):lock.unlock()
        self.locks=[]
    def __enter__(self):return self
    def __exit__(self,*args):self.close()


def verify_database(connection):
    if connection.execute('PRAGMA integrity_check').fetchall()!=[('ok',)]:
        raise ValueError('integridade do banco não confirmada')


def _inside_path(value,source,destination):
    if not isinstance(value,str) or not value:return value
    try:return str(destination / Path(value).resolve().relative_to(source.resolve()))
    except (ValueError,OSError):return value


def _normalize_copy(connection,source,destination):
    tables={row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if 'settings' in tables:
        for key,value in connection.execute('SELECT key,value FROM settings').fetchall():
            try:decoded=json.loads(value)
            except (ValueError,TypeError):continue
            if key=='appearance.theme' and decoded=='white':decoded='green'
            elif key in ('profile.avatar','downloads','captures','save_backups'):decoded=_inside_path(decoded,source,destination)
            else:continue
            connection.execute('UPDATE settings SET value=? WHERE key=?',(json.dumps(decoded),key))
    paths={'games':('cover','banner','logo','executable'),'game_files':('local_path',),'media_files':('path',),
           'artwork_assets':('local_path',),'save_configurations':('directory',),'save_backups':('path',),'emulators':('executable',)}
    for table,fields in paths.items():
        if table not in tables:continue
        for field in fields:
            for identity,value in connection.execute(f'SELECT rowid,{field} FROM {table}').fetchall():
                replacement=_inside_path(value,source,destination)
                if replacement!=value:connection.execute(f'UPDATE {table} SET {field}=? WHERE rowid=?',(replacement,identity))


def _backup(source,target,old_root=None,new_root=None):
    with closing(sqlite3.connect(source.resolve().as_uri()+'?mode=ro',uri=True)) as original:
        with closing(sqlite3.connect(target)) as copied:
            original.backup(copied)
            if old_root is not None:
                with copied:_normalize_copy(copied,old_root,new_root)
            verify_database(copied)


def _copy_directory(source,staging,destination):
    databases={source/LEGACY_DATABASE}
    for file in source.rglob('*'):
        if file.is_file() and not file.is_symlink() and file.suffix.lower() in ('.sqlite','.db'):
            with file.open('rb') as stream:
                if stream.read(16)==b'SQLite format 3\x00':databases.add(file)
    def ignore(folder,names):
        ignored=[]
        for name in names:
            file=Path(folder)/name;lower=name.lower()
            secret=any(fnmatch.fnmatch(lower,pattern) for pattern in ('credentials*','token*','client_secret*','.env*'))
            if file in databases or lower.endswith(('-wal','-shm','.lock')) or secret:ignored.append(name)
        return ignored
    shutil.copytree(source,staging,ignore=ignore,symlinks=True)
    for file in sorted(databases):
        if not file.is_file():continue
        relative=file.relative_to(source)
        target=staging/(DATABASE_NAME if relative==Path(LEGACY_DATABASE) else relative)
        target.parent.mkdir(parents=True,exist_ok=True)
        _backup(file,target,source if file==source/LEGACY_DATABASE else None,destination)


def _migrate_credentials(directory,vault_factory):
    marker=directory/'migration-v1.done'
    if marker.exists():return
    if vault_factory is None:
        if sys.platform!='win32':return
        from .credentials import CredentialVault
        vault_factory=CredentialVault
    vault=vault_factory();vault.migrate_legacy()
    marker.write_text('1\n',encoding='ascii')


def prepare_data_directory(data_dir=None,*,local_root=None,vault_factory=None,migrate_credentials=True):
    """Retém as travas de instância até DataSession.close(). Testes injetam local_root."""
    root=Path(local_root) if local_root is not None else Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'.local/share')))
    explicit=data_dir is not None
    directory=Path(data_dir) if explicit else root/'Checkpoint'
    legacy=directory if explicit else root/LEGACY_PRODUCT
    parent=directory.parent;parent.mkdir(parents=True,exist_ok=True)
    guard=QLockFile(str(parent/('.'+directory.name+'-migration.lock')))
    if not guard.tryLock(100):raise MigrationError('Outra instância está iniciando ou migrando os dados.',legacy)
    locks=[];staging=None
    try:
        # A trava legada também impede abrir uma versão antiga durante a migração.
        if legacy.exists():
            old_lock=QLockFile(str(legacy/(LEGACY_PRODUCT.lower()+'.lock')))
            if not old_lock.tryLock(100):raise MigrationError('A biblioteca está aberta em outra instância. Feche a versão anterior.',legacy)
            locks.append(old_lock)
        if not explicit and not directory.exists() and legacy.exists():
            staging=parent/('.checkpoint-migration-'+uuid4().hex)
            _copy_directory(legacy,staging,directory)
            if migrate_credentials:_migrate_credentials(staging,vault_factory)
            if directory.exists():raise MigrationError('A pasta de destino foi criada por outra operação; nada foi sobrescrito.',legacy)
            staging.rename(directory);staging=None
        else:
            directory.mkdir(parents=True,exist_ok=True)
            # Suporta pastas personalizadas antigas sem sobrescrever o banco novo.
            old_database=directory/LEGACY_DATABASE
            if old_database.is_file() and not (directory/DATABASE_NAME).exists():
                temporary=directory/('.checkpoint-database-'+uuid4().hex)
                try:_backup(old_database,temporary,directory,directory);temporary.rename(directory/DATABASE_NAME)
                finally:temporary.unlink(missing_ok=True)
            if not explicit and (legacy/LEGACY_DATABASE).exists() and not (directory/DATABASE_NAME).exists():
                raise MigrationError('A pasta de destino já existe, mas não contém um banco válido. Nenhum dado antigo foi sobrescrito.',legacy)
            if migrate_credentials:_migrate_credentials(directory,vault_factory)
        lock=QLockFile(str(directory/'checkpoint.lock'))
        if not lock.tryLock(100):raise MigrationError('Esta biblioteca já está aberta em outra instância.',legacy)
        locks.append(lock)
        return DataSession(directory,locks)
    except Exception as error:
        for lock in reversed(locks):lock.unlock()
        if staging is not None:shutil.rmtree(staging,ignore_errors=True)
        # Não registra caminhos, mensagens de SQLite, nomes de arquivos nem valores do cofre.
        try:
            with (parent/'checkpoint-startup.log').open('a',encoding='utf-8') as log:log.write('Falha na preparação dos dados: '+type(error).__name__+'\n')
        except OSError:pass
        logging.getLogger(__name__).error('Falha na preparação dos dados (%s). Origem preservada.',type(error).__name__)
        if isinstance(error,MigrationError):raise
        raise MigrationError('Não foi possível migrar os dados. A nova biblioteca não foi aberta.',legacy) from None
    finally:guard.unlock()

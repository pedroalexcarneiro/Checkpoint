"""Backups locais versionados de saves tradicionais explicitamente selecionados."""
import hashlib
import json
import fnmatch
import zipfile
import time
from pathlib import Path
from uuid import uuid4
from .library import now

FORBIDDEN = {'.state','.savestate','.ss0','.ss1','.st0','.st1','.zst'}

def digest(path):
    h = hashlib.sha256()
    with open(path,'rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

class SaveBackupService:
    def __init__(self, destination):
        self.destination = Path(destination).resolve()
        self.destination.mkdir(parents=True,exist_ok=True)

    def create(self, source, patterns):
        source = Path(source).resolve(strict=True)
        if not source.is_dir() or not patterns or any(p in {'*','*.*'} for p in patterns):
            raise ValueError('Escolha uma pasta e padrões específicos de saves tradicionais.')
        if source == self.destination or source in self.destination.parents:
            raise ValueError('Backups devem ficar fora da pasta de saves.')
        files = [p for p in source.rglob('*') if p.is_file() and not p.is_symlink()
                 and p.suffix.lower() not in FORBIDDEN
                 and any(fnmatch.fnmatch(p.name, pattern) for pattern in patterns)]
        if not files:
            raise ValueError('Nenhum save corresponde aos padrões configurados.')
        before = {p:(p.stat().st_size,p.stat().st_mtime_ns,digest(p)) for p in files}
        time.sleep(1.0)
        target = self.destination / (uuid4().hex+'.zip')
        partial = target.with_suffix('.partial')
        manifest = {}
        try:
            with zipfile.ZipFile(partial,'w',zipfile.ZIP_DEFLATED) as archive:
                for path, info in before.items():
                    if (path.stat().st_size,path.stat().st_mtime_ns,digest(path)) != info:
                        raise ValueError('Save sendo alterado. Feche o jogo e tente novamente.')
                    name = path.relative_to(source).as_posix()
                    content = path.read_bytes()
                    if hashlib.sha256(content).hexdigest() != info[2]:
                        raise ValueError('Save alterado durante a leitura.')
                    archive.writestr(name,content)
                    manifest[name] = info[2]
                archive.writestr('checkpoint-manifest.json',json.dumps({'created_at':now(),'files':manifest}))
            after = [p for p in source.rglob('*') if p.is_file() and not p.is_symlink()
                     and p.suffix.lower() not in FORBIDDEN
                     and any(fnmatch.fnmatch(p.name, pattern) for pattern in patterns)]
            if set(after) != set(files) or any((p.stat().st_size,p.stat().st_mtime_ns,digest(p)) != info for p,info in before.items()):
                raise ValueError('Os saves mudaram durante o backup. Feche o jogo e tente novamente.')
            with zipfile.ZipFile(partial) as archive:
                if archive.testzip():
                    raise ValueError('Falha na integridade do arquivo de backup.')
            partial.replace(target)
            return target, digest(target), manifest
        finally:
            partial.unlink(missing_ok=True)

    def restore(self, archive_path, destination, expected_sha256):
        archive_path, destination = Path(archive_path), Path(destination).resolve()
        if digest(archive_path) != expected_sha256:
            raise ValueError('O backup falhou na verificação SHA-256.')
        with zipfile.ZipFile(archive_path) as archive:
            manifest = json.loads(archive.read('checkpoint-manifest.json'))['files']
            contents = {}
            for name, checksum in manifest.items():
                path = (destination/name).resolve()
                if destination not in path.parents or path.suffix.lower() in FORBIDDEN:
                    raise ValueError('Caminho inseguro no backup.')
                content = archive.read(name)
                if hashlib.sha256(content).hexdigest() != checksum:
                    raise ValueError('Conteúdo do backup corrompido.')
                contents[path] = content
            # Preserva cada versão existente antes da substituição.
            recovery = self.destination / ('before-restore-'+uuid4().hex+'.zip')
            with zipfile.ZipFile(recovery,'w',zipfile.ZIP_DEFLATED) as previous:
                for path in contents:
                    if path.exists():
                        previous.write(path,path.relative_to(destination).as_posix())
            for path, content in contents.items():
                path.parent.mkdir(parents=True,exist_ok=True)
                temporary = path.with_name(path.name+'.checkpoint-'+uuid4().hex)
                temporary.write_bytes(content)
                temporary.replace(path)
            return recovery

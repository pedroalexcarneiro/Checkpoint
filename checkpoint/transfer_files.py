"""Nomes válidos no Windows e publicação sem sobrescrever arquivos existentes."""
import os
import hashlib
from pathlib import Path
import re


REVISION_FIELDS=('drive_id','original_name','size','md5','modified_at','extension','platform')


def windows_name(original, extension=''):
    name=re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', original or '').rstrip(' .')
    if name in ('', '.', '..'):
        name='ROM'+extension
    stem=Path(name).stem
    suffix=Path(name).suffix
    if re.fullmatch(r'(?i:CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])',name.split('.',1)[0].rstrip(' ')):
        stem='_'+stem
    while len((stem+suffix).encode('utf-16-le'))>510 and stem:
        stem=stem[:-1]
    return (stem or 'ROM')+suffix


def free_destination(directory, name):
    directory=Path(directory)
    source=Path(name)
    for index in range(1,1001):
        serial='' if index==1 else f' ({index})'
        stem=source.stem
        while len((stem+serial+source.suffix).encode('utf-16-le'))>510 and stem:stem=stem[:-1]
        candidate=directory/(stem+serial+source.suffix)
        if not candidate.exists() and not candidate.is_symlink():
            return candidate
    raise ValueError('Muitos arquivos com o mesmo nome. Escolha outra pasta de destino.')


def publish_file(partial, target):
    """Rename Windows/link POSIX falham atomicamente se o destino já existir."""
    partial,target=Path(partial),Path(target)
    if os.name=='nt':
        os.rename(partial,target)
    else:
        os.link(partial,target)
        partial.unlink()


def publish_download(library, row, partial, target, digest):
    """Journal antes do rename: falha posterior do SQLite não exige baixar de novo."""
    key=f'downloads.pending.{row["id"]}'
    value={key:row[key] for key in REVISION_FIELDS}
    value.update(partial=str(partial),target=str(target),sha256=digest)
    library.set_setting(key,value)
    for attempt in range(1000):
        try:
            publish_file(partial,target);break
        except FileExistsError:
            target=free_destination(target.parent,windows_name(row['original_name'],row['extension']))
            value['target']=str(target);library.set_setting(key,value)
    else:raise ValueError('Não foi possível reservar um destino. Parcial preservado.')
    record_download(library,row,target,key)
    return target


def record_download(library,row,target,key):
    fields=(*REVISION_FIELDS,'local_path','available')
    expected=' AND '.join(field+' IS ?' for field in fields)
    with library.sql:
        current=library.sql.execute(
            'UPDATE game_files SET local_path=?,available=1 WHERE id=? AND '+expected
            +" AND review_state NOT IN ('remote_removed','remote_missing','outside_root')",
            (str(target),row['id'],*(row[field] for field in fields)))
        if current.rowcount!=1:
            raise ValueError('O índice da ROM mudou durante o download. A cópia foi preservada. Atualize o índice e confira a versão.')
        library.sql.execute('DELETE FROM settings WHERE key=?',(key,))


def recover_download(library, row, cancel=None):
    from .transfer_progress import check_cancel
    key=f'downloads.pending.{row["id"]}'
    journal=library.setting(key,None)
    if not isinstance(journal,dict):return None
    if any(journal.get(k)!=row[k] for k in REVISION_FIELDS):return None
    digest=journal.get('sha256','')
    if not re.fullmatch('[a-f0-9]{64}',digest):return None
    partial=Path(journal.get('partial',''));target=Path(journal.get('target',''))
    for source in (target,partial):
        if not source.is_file() or source.is_symlink():continue
        check_cancel(cancel)
        checksum=hashlib.sha256()
        with source.open('rb') as stream:
            for block in iter(lambda:stream.read(1024*1024),b''):
                check_cancel(cancel);checksum.update(block)
        if checksum.hexdigest()!=digest:continue
        if source==partial:return publish_download(library,row,partial,target,digest)
        record_download(library,row,target,key)
        return target
    return None

"""Vínculo local confirmado, sem Drive, downloads ou alteração de identidade."""
import json
import re
from datetime import datetime,timezone
from pathlib import Path
from .automatic_catalog import normalized
from .integrations.drive import PLATFORMS,rom_identity,normalize_rom_name


def canonical_platform(value):
    value=(value or '').strip();return PLATFORMS.get(value.casefold(),value)


def extension_set(value):
    result=set()
    for part in (value or '').split(','):
        part='.'+part.strip().lower().lstrip('*.')
        if re.fullmatch(r'\.[a-z0-9]+',part):result.add(part)
    return result


def compatible_profiles(library,platform,extension):
    rows=[]
    for stored in library.sql.execute('SELECT p.*,e.name,e.executable FROM emulator_profiles p JOIN emulators e ON e.id=p.emulator_id ORDER BY e.name,p.id'):
        row=dict(stored)
        if canonical_platform(row['platform']).casefold()!=canonical_platform(platform).casefold():continue
        if extension.lower() not in extension_set(row['extensions']):continue
        try:args=json.loads(row['arguments_json'])
        except (ValueError,TypeError):continue
        if not isinstance(args,list) or not all(isinstance(a,str) for a in args) or not any('{rom}' in a for a in args):continue
        if not Path(row['executable']).is_file():continue
        rows.append(row)
    return rows


def validate_path(path):
    try:
        source=Path(path).resolve(strict=True)
        if not source.is_file():raise OSError()
        with source.open('rb') as stream:
            if not stream.read(1):raise ValueError('A ROM está vazia. Escolha um arquivo válido.')
        stamp=source.stat()
    except (OSError,RuntimeError) as error:
        raise ValueError('Não foi possível ler a ROM. Localize um arquivo existente e acessível.') from None
    title,inferred=rom_identity(source.name)
    return {'local_path':str(source),'original_name':source.name,'extension':source.suffix.lower(),
            'platform':inferred,'size':stamp.st_size,'mtime_ns':stamp.st_mtime_ns,
            'modified_at':datetime.fromtimestamp(stamp.st_mtime,timezone.utc).isoformat()}


def file_title(name):
    return normalize_rom_name(Path(name).stem)


def identity_problem(game,file):
    expected=canonical_platform(game.get('platform'))
    actual=canonical_platform(file.get('platform'))
    if expected and actual and expected.casefold()!=actual.casefold():
        return f'A plataforma da ROM ({actual}) difere da ficha ({expected}). Escolha outra ROM ou a ficha da edição correta.'
    title=game['title'];name=file_title(file['original_name'])
    a=set(re.findall(r'[a-z0-9]+',title.casefold()));b=set(re.findall(r'[a-z0-9]+',name.casefold()))
    markers={'3d','hd','remake','remaster','remastered','deluxe','definitive','redux','collection'}
    common=(a-markers)&(b-markers)
    numeric=lambda values:{v for v in values if v.isdigit() or v in ('ii','iii','iv','vi','vii','viii','ix','xi','xii')}
    if (len(common)>=2 and (a&markers)!=(b&markers)) or (common and numeric(a) and numeric(b) and numeric(a)!=numeric(b)):
        return 'A edição indicada no arquivo difere da ficha. Escolha outra ROM ou cadastre/selecione a edição correta.'
    return ''


def title_needs_confirmation(game,file):
    return normalized(game['title'])!=normalized(file_title(file['original_name']))


def bind_local(library,game_id,path,platform,profile_id,*,confirmed_title=False):
    from .game_import import atomic
    game=library.get(game_id)
    if not game or not library.is_owned(game_id):raise ValueError('Escolha um jogo da Biblioteca.')
    file=validate_path(path);inferred=file['platform'];file['platform']=canonical_platform(platform)
    if not file['platform']:raise ValueError('Selecione a plataforma da ROM.')
    if inferred and canonical_platform(inferred).casefold()!=file['platform'].casefold():
        raise ValueError('A plataforma identificada no arquivo difere da seleção. Confira a ROM e a edição.')
    problem=identity_problem(game,file)
    if problem:raise ValueError(problem)
    if title_needs_confirmation(game,file) and not confirmed_title:raise ValueError('Confirme que o arquivo pertence ao jogo e à edição exibidos.')
    profiles=compatible_profiles(library,file['platform'],file['extension'])
    if not any(p['id']==profile_id for p in profiles):raise ValueError('Selecione um perfil compatível com a plataforma e a extensão da ROM.')
    existing=library.sql.execute('SELECT * FROM game_files WHERE drive_id IS NULL AND local_path=?',(file['local_path'],)).fetchone()
    if existing and existing['game_id'] not in (None,game_id):raise ValueError('Esta ROM já está vinculada a outro jogo. Nenhum vínculo foi alterado.')
    if Path(file['local_path']).stat().st_mtime_ns!=file['mtime_ns']:raise ValueError('O arquivo mudou. Selecione a ROM novamente.')
    with atomic(library.sql):
        if existing:
            file_id=existing['id']
            library.sql.execute("UPDATE game_files SET game_id=?,platform=?,extension=?,size=?,modified_at=?,available=1,review_state='confirmed' WHERE id=?",(game_id,file['platform'],file['extension'],file['size'],file['modified_at'],file_id))
        else:
            file_id=library.sql.execute("INSERT INTO game_files(game_id,original_name,extension,size,folder_path,modified_at,platform,local_path,available,review_state) VALUES(?,?,?,?,?,?,?,?,1,'confirmed')",(game_id,file['original_name'],file['extension'],file['size'],str(Path(file['local_path']).parent),file['modified_at'],file['platform'],file['local_path'])).lastrowid
        library.sql.execute('UPDATE game_files SET game_id=NULL WHERE game_id=? AND id<>?',(game_id,file_id))
        library.sql.execute('INSERT INTO rom_versions(file_id,profile_id) VALUES(?,?) ON CONFLICT(file_id) DO UPDATE SET profile_id=excluded.profile_id',(file_id,profile_id))
    return file_id

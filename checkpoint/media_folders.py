"""Pastas de capturas por jogo sem reorganizar arquivos existentes."""
from pathlib import Path
from .transfer_files import windows_name


FOLDERS='memories.managed_folders'


def capture_root(library):
    value=library.setting('captures','')
    return Path(value).expanduser() if value else library.db.path.parent/'captures'


def managed_folder(library,game_id):
    game=library.get(game_id)
    if game is None:raise ValueError('A ficha deste jogo não está disponível.')
    folders=library.setting(FOLDERS,{})
    if not isinstance(folders,dict):folders={}
    identity=str(game_id)
    prefix=f'Jogo {identity} - '
    name=folders.get(identity)
    if not isinstance(name,str) or not name.startswith(prefix) or '/' in name or '\\' in name:
        name=prefix+windows_name(game['title'][:74])
        folders[identity]=name
        library.set_setting(FOLDERS,folders)
    root=capture_root(library)
    directory=root/name
    if directory.is_symlink():
        raise ValueError('A pasta deste jogo é um link para outro local. Escolha outra pasta de capturas.')
    return directory


def known_folders(library):
    root=capture_root(library).absolute()
    folders=library.setting(FOLDERS,{})
    if not isinstance(folders,dict) or not folders:return {}
    owned={str(game['id']) for game in library.owned_games()}
    return {root/name:int(identity) for identity,name in folders.items()
            if identity in owned and isinstance(name,str) and name.startswith(f'Jogo {identity} - ')
            and '/' not in name and '\\' not in name}

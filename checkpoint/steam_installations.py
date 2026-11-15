"""Instalações Steam locais: raiz do sistema, VDFs e manifests, sem caminho fixo."""
import re
import sys
from pathlib import Path


def read_vdf(path):
    source=Path(path).read_text(encoding='utf-8').lstrip('\ufeff')
    tokens=re.findall(r'"((?:\\.|[^"\\])*)"|([{}])|(?://[^\n]*)',source)
    values=[brace or re.sub(r'\\([\\"])',r'\1',value) for value,brace in tokens if value or brace]
    iterator=iter(values)
    def block():
        result={}
        for key in iterator:
            if key=='}':return result
            value=next(iterator,None)
            if value is None:raise ValueError('Arquivo Steam incompleto.')
            result[key]=block() if value=='{' else value
        return result
    return block()


def steam_roots():
    roots=[]
    if sys.platform=='win32':
        import winreg
        for hive,key,value in ((winreg.HKEY_CURRENT_USER,r'Software\Valve\Steam','SteamPath'),(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\WOW6432Node\Valve\Steam','InstallPath')):
            try:
                with winreg.OpenKey(hive,key) as handle:roots.append(Path(winreg.QueryValueEx(handle,value)[0]))
            except OSError:continue
    return list(dict.fromkeys(roots))


def find_executables(appid,roots=None):
    appid=str(appid)
    if not appid.isdigit():return []
    roots=list(steam_roots() if roots is None else roots);libraries=list(roots)
    for root in roots:
        for path in (root/'steamapps/libraryfolders.vdf',root/'config/libraryfolders.vdf'):
            if not path.is_file():continue
            entries=read_vdf(path).get('libraryfolders',{})
            for key,value in entries.items():
                location=value.get('path') if isinstance(value,dict) else value if key.isdigit() else None
                if location:libraries.append(Path(location))
    result=[]
    for library in dict.fromkeys(libraries):
        manifest=library/'steamapps'/f'appmanifest_{appid}.acf'
        if not manifest.is_file():continue
        data=read_vdf(manifest).get('AppState',{})
        if data.get('appid')!=appid:continue
        base=(library/'steamapps/common').resolve()
        install=(base/data.get('installdir','')).resolve()
        if not data.get('installdir') or not install.is_relative_to(base):continue
        for executable in install.rglob('*'):
            if executable.suffix.casefold()!='.exe' or not executable.is_file():continue
            if not executable.resolve().is_relative_to(install):continue
            if any(re.search(r'unins|redist|crash|setup|install|vcredist|directx',part,re.I) for part in executable.relative_to(install).parts):continue
            result.append(executable.resolve())
    return sorted(set(result))

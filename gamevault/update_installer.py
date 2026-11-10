"""Instalação de atualizações one-dir com recuperação da pasta anterior."""
import argparse
import ctypes
import json
import os
from pathlib import Path,PurePosixPath
import shutil
import subprocess
import sys
import time
from uuid import uuid4
import zipfile

MAX_EXPANDED=1_500_000_000

def extract_package(archive_path,destination):
    destination=Path(destination).resolve()
    if destination.exists(): raise ValueError('A pasta de preparação já existe.')
    destination.mkdir(parents=True)
    with zipfile.ZipFile(archive_path) as archive:
        members=archive.infolist()
        if sum(m.file_size for m in members)>MAX_EXPANDED or len(members)>15000:
            raise ValueError('Pacote excede os limites de extração.')
        names=set()
        for member in members:
            name=member.filename; path=PurePosixPath(name)
            if '\\' in name or ':' in name or path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0]!='Checkpoint':
                raise ValueError('Caminho inválido no pacote de atualização.')
            if (member.external_attr>>16)&0o170000==0o120000: raise ValueError('Links não são aceitos no pacote.')
            key=name.rstrip('/').casefold()
            if key in names: raise ValueError('Caminhos duplicados no pacote.')
            names.add(key)
            for part in path.parts:
                if part.rstrip(' .')!=part or part.split('.')[0].upper() in {'CON','PRN','AUX','NUL',*[f'COM{i}' for i in range(1,10)],*[f'LPT{i}' for i in range(1,10)]}:
                    raise ValueError('Nome de arquivo inválido no Windows.')
        if 'checkpoint/checkpoint.exe' not in names: raise ValueError('Pacote não contém Checkpoint.exe.')
        for member in members:
            target=destination.joinpath(*PurePosixPath(member.filename).parts)
            if destination not in target.resolve().parents: raise ValueError('Destino inválido.')
            if member.is_dir(): target.mkdir(parents=True,exist_ok=True); continue
            target.parent.mkdir(parents=True,exist_ok=True)
            with archive.open(member) as source,target.open('xb') as output: shutil.copyfileobj(source,output,1024*1024)
    return destination/'Checkpoint'

def swap_install(installation,staged):
    installation,staged=Path(installation).resolve(),Path(staged).resolve()
    if installation.name!='Checkpoint' or not (installation/'Checkpoint.exe').is_file() or not (staged/'Checkpoint.exe').is_file():
        raise ValueError('Instalação ou pacote inválido.')
    if installation==staged or installation in staged.parents or staged in installation.parents:
        raise ValueError('A preparação deve estar fora da instalação.')
    # Renomes apenas entre os alvos explicitamente validados; nunca apaga a versão antiga.
    previous=installation.with_name('Checkpoint.previous-'+uuid4().hex)
    installation.rename(previous)
    try:
        shutil.copytree(staged,installation)
    except Exception:
        # Preserva a cópia incompleta para diagnóstico; recupera o nome original.
        if installation.exists(): installation.rename(installation.with_name('Checkpoint.failed-'+uuid4().hex))
        previous.rename(installation)
        raise
    return previous

def wait_for_exit(pid,timeout=60):
    if pid<=0 or pid==os.getpid(): raise ValueError('Processo de origem inválido.')
    if os.name=='nt':
        from ctypes import wintypes
        kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        kernel.OpenProcess.argtypes=[wintypes.DWORD,wintypes.BOOL,wintypes.DWORD]; kernel.OpenProcess.restype=wintypes.HANDLE
        kernel.WaitForSingleObject.argtypes=[wintypes.HANDLE,wintypes.DWORD]; kernel.WaitForSingleObject.restype=wintypes.DWORD
        kernel.CloseHandle.argtypes=[wintypes.HANDLE]
        handle=kernel.OpenProcess(0x100000,False,pid)
        if not handle:
            if ctypes.get_last_error()==87: return
            raise OSError('Não foi possível aguardar o aplicativo encerrar.')
        try:
            if kernel.WaitForSingleObject(handle,int(timeout*1000))!=0: raise TimeoutError('O aplicativo não encerrou a tempo.')
        finally: kernel.CloseHandle(handle)
    else:
        deadline=time.monotonic()+timeout
        while time.monotonic()<deadline:
            try: os.kill(pid,0)
            except ProcessLookupError: return
            time.sleep(.1)
        raise TimeoutError('O aplicativo não encerrou a tempo.')

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--plan',type=Path); parser.add_argument('--no-restart',action='store_true'); parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    if args.check: return 0
    if not args.plan: return 2
    result=args.plan.with_suffix('.result.json')
    try:
        plan=json.loads(args.plan.read_text(encoding='utf-8'))
        wait_for_exit(int(plan['pid']))
        previous=swap_install(plan['installation'],plan['staged'])
        if not args.no_restart:
            command=[str(Path(plan['installation'])/'Checkpoint.exe'),'--data-dir',plan['data_directory']]
            try: subprocess.Popen(command,cwd=plan['installation'],shell=False)
            except Exception:
                failed=Path(plan['installation']).with_name('Checkpoint.failed-'+uuid4().hex)
                Path(plan['installation']).rename(failed); previous.rename(plan['installation']); raise
        result.write_text(json.dumps({'state':'installed','previous':str(previous)}),encoding='utf-8'); return 0
    except Exception as error:
        result.write_text(json.dumps({'state':'failed','message':str(error)}),encoding='utf-8'); return 1

if __name__=='__main__': raise SystemExit(main())

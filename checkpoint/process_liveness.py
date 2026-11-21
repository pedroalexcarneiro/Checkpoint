"""Identidade de processo próprio: PID reutilizado não mantém tarefa órfã ativa."""
import os
from pathlib import Path
import sys


def process_token(pid):
    if type(pid) is not int or pid<=0:return None
    if sys.platform=='win32':
        import ctypes as c
        from ctypes import wintypes as w
        kernel=c.WinDLL('kernel32',use_last_error=True)
        kernel.OpenProcess.argtypes=[w.DWORD,w.BOOL,w.DWORD];kernel.OpenProcess.restype=w.HANDLE
        kernel.CloseHandle.argtypes=[w.HANDLE]
        kernel.WaitForSingleObject.argtypes=[w.HANDLE,w.DWORD]
        kernel.GetProcessTimes.argtypes=[w.HANDLE,c.POINTER(w.FILETIME),c.POINTER(w.FILETIME),c.POINTER(w.FILETIME),c.POINTER(w.FILETIME)]
        handle=kernel.OpenProcess(0x1000|0x100000,False,pid)
        if not handle:return None
        try:
            if kernel.WaitForSingleObject(handle,0)!=258:return None
            created,ended,kernel_time,user_time=(w.FILETIME() for _ in range(4))
            if not kernel.GetProcessTimes(handle,c.byref(created),c.byref(ended),c.byref(kernel_time),c.byref(user_time)):return None
            return str((created.dwHighDateTime<<32)|created.dwLowDateTime)
        finally:kernel.CloseHandle(handle)
    try:
        raw=Path(f'/proc/{pid}/stat').read_text(encoding='utf-8')
        fields=raw[raw.rfind(')')+2:].split()
        return fields[19] if fields[0] not in ('Z','X') else None
    except (OSError,IndexError,UnicodeError):return None


def current_owner():
    token=process_token(os.getpid())
    if token is None:raise ValueError('Não foi possível acompanhar o processo do Checkpoint. Tente novamente.')
    return {'pid':os.getpid(),'token':token}


def owner_alive(owner):
    return (isinstance(owner,dict) and type(owner.get('pid')) is int
            and bool(owner.get('token')) and process_token(owner['pid'])==owner['token'])

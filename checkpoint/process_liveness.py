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


def request_game_close(process):
    """Pede o fechamento do processo iniciado pela sessão, sem forçar no Windows."""
    if process.poll() is not None:
        return False
    if sys.platform!='win32':
        try:
            process.terminate()
        except ProcessLookupError:
            return False
        return True

    import ctypes as c
    from ctypes import wintypes as w
    user=c.WinDLL('user32',use_last_error=True)
    enumerator=c.WINFUNCTYPE(w.BOOL,w.HWND,w.LPARAM)
    user.EnumWindows.argtypes=[enumerator,w.LPARAM]
    user.GetWindowThreadProcessId.argtypes=[w.HWND,c.POINTER(w.DWORD)]
    user.IsWindowVisible.argtypes=[w.HWND]
    user.GetWindow.argtypes=[w.HWND,w.UINT];user.GetWindow.restype=w.HWND
    user.PostMessageW.argtypes=[w.HWND,w.UINT,w.WPARAM,w.LPARAM]

    def window_pid(hwnd):
        pid=w.DWORD()
        user.GetWindowThreadProcessId(hwnd,c.byref(pid))
        return pid.value

    matches=[]
    @enumerator
    def visit(hwnd,_):
        if user.IsWindowVisible(hwnd) and not user.GetWindow(hwnd,4) and window_pid(hwnd)==process.pid:
            matches.append(hwnd)
        return True

    user.EnumWindows(visit,0)
    if process.poll() is not None:
        return False
    if len(matches)!=1 or window_pid(matches[0])!=process.pid:
        raise ValueError('Não encontrei uma única janela do jogo iniciada nesta sessão. Feche pela janela do jogo.')
    if not user.PostMessageW(matches[0],0x10,0,0):  # WM_CLOSE
        raise ValueError('O Windows recusou o pedido de fechamento. Feche pela janela do jogo.')
    return True

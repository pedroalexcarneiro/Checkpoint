"""Elevação explícita do executável Windows antes de abrir dados ou cofre."""
from pathlib import Path
import subprocess


class ElevationCancelled(Exception):
    pass


class WindowsElevationApi:
    def __init__(self):
        import ctypes
        self.ctypes=ctypes
        self.shell=ctypes.WinDLL('shell32',use_last_error=True)
        self.kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        self.advapi=ctypes.WinDLL('advapi32',use_last_error=True)
    def is_admin(self):return bool(self.shell.IsUserAnAdmin())
    def user_sid(self):
        c=self.ctypes
        from ctypes import wintypes as w
        self.kernel.GetCurrentProcess.restype=w.HANDLE
        self.kernel.CloseHandle.argtypes=[w.HANDLE]
        self.advapi.OpenProcessToken.argtypes=[w.HANDLE,w.DWORD,c.POINTER(w.HANDLE)]
        self.advapi.GetTokenInformation.argtypes=[w.HANDLE,c.c_int,c.c_void_p,w.DWORD,c.POINTER(w.DWORD)]
        self.advapi.ConvertSidToStringSidW.argtypes=[c.c_void_p,c.POINTER(w.LPWSTR)]
        self.kernel.LocalFree.argtypes=[c.c_void_p];self.kernel.LocalFree.restype=c.c_void_p
        token=w.HANDLE()
        if not self.advapi.OpenProcessToken(self.kernel.GetCurrentProcess(),8,c.byref(token)):raise c.WinError(c.get_last_error())
        try:
            size=w.DWORD();self.advapi.GetTokenInformation(token,1,None,0,c.byref(size))
            if not size.value:raise c.WinError(c.get_last_error())
            buffer=c.create_string_buffer(size.value)
            if not self.advapi.GetTokenInformation(token,1,buffer,size.value,c.byref(size)):raise c.WinError(c.get_last_error())
            sid=c.cast(buffer,c.POINTER(c.c_void_p)).contents.value;value=w.LPWSTR()
            if not self.advapi.ConvertSidToStringSidW(sid,c.byref(value)):raise c.WinError(c.get_last_error())
            try:return value.value
            finally:self.kernel.LocalFree(c.cast(value,c.c_void_p))
        finally:self.kernel.CloseHandle(token)
    def relaunch(self,executable,arguments,cwd):
        c=self.ctypes
        from ctypes import wintypes as w
        class ExecuteInfo(c.Structure):
            _fields_=[('cbSize',w.DWORD),('fMask',w.ULONG),('hwnd',w.HWND),('lpVerb',w.LPCWSTR),('lpFile',w.LPCWSTR),('lpParameters',w.LPCWSTR),('lpDirectory',w.LPCWSTR),('nShow',c.c_int),('hInstApp',w.HINSTANCE),('lpIDList',c.c_void_p),('lpClass',w.LPCWSTR),('hkeyClass',w.HKEY),('dwHotKey',w.DWORD),('hIconOrMonitor',w.HANDLE),('hProcess',w.HANDLE)]
        self.shell.ShellExecuteExW.argtypes=[c.POINTER(ExecuteInfo)];self.shell.ShellExecuteExW.restype=w.BOOL
        info=ExecuteInfo();info.cbSize=c.sizeof(info);info.fMask=0x40;info.lpVerb='runas';info.lpFile=str(executable)
        info.lpParameters=subprocess.list2cmdline(arguments);info.lpDirectory=str(cwd);info.nShow=1
        if not self.shell.ShellExecuteExW(c.byref(info)):
            error=c.get_last_error()
            if error==1223:raise ElevationCancelled()
            raise c.WinError(error)
        if info.hProcess:
            self.kernel.CloseHandle.argtypes=[w.HANDLE];self.kernel.CloseHandle(info.hProcess)


def elevate_startup(arguments,*,executable,cwd,local_root,owner_sid=None,api=None):
    """None continua; 0 encerra a instância que transferiu a inicialização."""
    api=api or WindowsElevationApi();sid=api.user_sid();admin=api.is_admin()
    if not isinstance(sid,str) or not sid:raise ValueError('Não foi possível confirmar a conta do Windows. Os dados não foram abertos.')
    if owner_sid is not None:
        if sid!=owner_sid:raise ValueError('A elevação mudou a conta do Windows. Use a mesma conta da biblioteca para preservar dados e cofre.')
        if not admin:raise ValueError('A elevação não foi concluída. Abra o Checkpoint novamente para solicitar permissão.')
        return None
    if admin:return None
    args=list(arguments)
    for index,value in enumerate(args):
        if value=='--data-dir' and index+1<len(args):args[index+1]=str(Path(args[index+1]).resolve())
        elif value.startswith('--data-dir='):args[index]='--data-dir='+str(Path(value.split('=',1)[1]).resolve())
    args.extend(['--elevated-owner-sid',sid,'--elevated-data-root',str(Path(local_root).resolve())])
    api.relaunch(str(executable),args,str(cwd));return 0

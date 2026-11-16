"""Abre o app normalmente em Windows elevado e verifica sua janela nativa."""
from contextlib import closing
import ctypes
from ctypes import wintypes as w
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import time

_capture_app=None


def native_startup(command,directory):
    global _capture_app
    if sys.platform!='win32':raise RuntimeError('Validação de HWND exige Windows real.')
    from checkpoint.elevation import WindowsElevationApi
    if not WindowsElevationApi().is_admin():
        raise RuntimeError('O executor desta validação deve estar elevado; não automatizar consentimento UAC.')
    directory=Path(directory).resolve()
    if directory.exists():raise ValueError('Use diretório novo para preservar dados existentes.')
    user=ctypes.WinDLL('user32',use_last_error=True)
    callback_type=ctypes.WINFUNCTYPE(w.BOOL,w.HWND,w.LPARAM)
    user.EnumWindows.argtypes=[callback_type,w.LPARAM]
    user.GetWindowThreadProcessId.argtypes=[w.HWND,ctypes.POINTER(w.DWORD)]
    user.GetWindowTextW.argtypes=[w.HWND,w.LPWSTR,ctypes.c_int]
    user.IsWindowVisible.argtypes=[w.HWND]
    user.GetClientRect.argtypes=[w.HWND,ctypes.POINTER(w.RECT)]
    user.PostMessageW.argtypes=[w.HWND,w.UINT,w.WPARAM,w.LPARAM]
    user.SendMessageTimeoutW.argtypes=[w.HWND,w.UINT,w.WPARAM,w.LPARAM,w.UINT,w.UINT,ctypes.POINTER(ctypes.c_size_t)]
    user.SendMessageTimeoutW.restype=ctypes.c_ssize_t
    process=subprocess.Popen([*command,'--data-dir',str(directory)],env={**os.environ,'QT_QPA_PLATFORM':'windows'},stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result=None
    try:
        handle=None;deadline=time.monotonic()+25;seen=set()
        while time.monotonic()<deadline and process.poll() is None:
            found=[]
            @callback_type
            def visit(hwnd,unused):
                pid=w.DWORD();user.GetWindowThreadProcessId(hwnd,ctypes.byref(pid))
                if pid.value==process.pid and user.IsWindowVisible(hwnd):
                    title=ctypes.create_unicode_buffer(512);user.GetWindowTextW(hwnd,title,len(title))
                    seen.add(title.value)
                    if title.value=='Checkpoint':found.append(hwnd)
                return True
            user.EnumWindows(visit,0)
            if found:handle=found[0];break
            time.sleep(.05)
        if handle is None:raise RuntimeError('Inicialização normal não apresentou a janela Checkpoint; exit='+str(process.poll())+'; janelas='+repr(sorted(seen)))
        response=ctypes.c_size_t()
        if not user.SendMessageTimeoutW(handle,0,0,0,2,5000,ctypes.byref(response)):
            raise RuntimeError('A janela inicial não responde às mensagens do Windows.')
        rect=w.RECT()
        if not user.GetClientRect(handle,ctypes.byref(rect)) or rect.right<=0 or rect.bottom<=0:
            raise RuntimeError('A janela nativa não possui área de conteúdo válida.')
        os.environ['QT_QPA_PLATFORM']='windows'
        from PySide6.QtWidgets import QApplication
        _capture_app=QApplication.instance() or QApplication([]);app=_capture_app
        if app.platformName()!='windows':raise RuntimeError('Captura nativa exige o plugin Qt windows.')
        app.processEvents();screen=app.primaryScreen()
        picture=screen.grabWindow(int(handle)) if screen else None
        if picture is None or picture.isNull() or not picture.save(str(directory/'native-startup.png')):
            raise RuntimeError('A janela nativa não forneceu captura válida.')
        if not user.PostMessageW(handle,0x10,0,0):raise ctypes.WinError(ctypes.get_last_error())
        stdout,stderr=process.communicate(timeout=15)
        if process.returncode!=0:raise RuntimeError('Encerramento normal falhou: '+repr((process.returncode,stdout,stderr)))
        with closing(sqlite3.connect((directory/'checkpoint.sqlite').as_uri()+'?mode=ro',uri=True)) as sql:
            if sql.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise RuntimeError('SQLite inválido após abertura nativa.')
        result={'backend':'windows','ordinary_startup':True,'already_elevated':True,'pid':process.pid,'hwnd':int(handle),'client_size':[rect.right,rect.bottom],'responsive':True,'screenshot':'native-startup.png','exit_code':process.returncode,'stdout':stdout.decode('utf-8',errors='replace'),'stderr':stderr.decode('utf-8',errors='replace')}
        (directory/'native-startup.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return result
    finally:
        if process.poll() is None:process.terminate()
        try:process.communicate(timeout=10)
        except subprocess.TimeoutExpired:process.kill();process.communicate()


if __name__=='__main__':
    if len(sys.argv)<3:raise SystemExit('Uso: native_startup_check.py DIRETORIO_NOVO COMANDO [ARGUMENTOS]')
    print(json.dumps(native_startup(sys.argv[2:],Path(sys.argv[1])),ensure_ascii=False,indent=2))

"""Captura de uma janela pertencente a uma sessão iniciada pelo Checkpoint."""
import sys
from pathlib import Path
from uuid import uuid4


class WindowsCapture:
    def capture(self,pid):
        if sys.platform!='win32':
            raise ValueError('Captura de janela de jogo disponível no Windows.')
        import ctypes
        from ctypes import wintypes
        from PySide6.QtWidgets import QApplication
        user=ctypes.WinDLL('user32',use_last_error=True)
        callback_type=ctypes.WINFUNCTYPE(wintypes.BOOL,wintypes.HWND,wintypes.LPARAM)
        user.EnumWindows.argtypes=[callback_type,wintypes.LPARAM]
        user.IsWindowVisible.argtypes=[wintypes.HWND]
        user.IsIconic.argtypes=[wintypes.HWND]
        user.GetWindowThreadProcessId.argtypes=[wintypes.HWND,ctypes.POINTER(wintypes.DWORD)]
        windows=[]
        @callback_type
        def visit(hwnd,param):
            owner=wintypes.DWORD()
            user.GetWindowThreadProcessId(hwnd,ctypes.byref(owner))
            if owner.value==pid and user.IsWindowVisible(hwnd) and not user.IsIconic(hwnd):windows.append(hwnd)
            return True
        user.EnumWindows(visit,0)
        if len(windows)!=1:
            raise ValueError('Não foi possível identificar uma única janela do jogo. Deixe a janela do jogo aberta e tente novamente.')
        screen=QApplication.primaryScreen()
        if screen is None:raise ValueError('Tela indisponível para captura.')
        return screen.grabWindow(int(windows[0]))


def capture_game(window,adapter=None):
    if not window.isActiveWindow():return None
    sessions={item[2]:item[0] for item in window.launcher.active.values()}
    if not sessions:raise ValueError('Nenhum jogo aberto pelo Checkpoint está em sessão para capturar.')
    current=getattr(window,'current_game',None)
    if current not in sessions:
        if len(sessions)!=1:raise ValueError('Abra a ficha do jogo em sessão que deseja capturar.')
        current=next(iter(sessions))
    pixmap=(adapter or WindowsCapture()).capture(sessions[current].pid)
    if pixmap.isNull():raise ValueError('A janela do jogo não forneceu uma captura. Tente o jogo em modo janela.')
    directory=Path(window.library.setting('captures','') or window.library.db.path.parent/'captures')
    directory.mkdir(parents=True,exist_ok=True)
    path=directory/(uuid4().hex+'.png')
    if not pixmap.save(str(path),'PNG'):raise ValueError('Não foi possível salvar a captura.')
    try:window.library.add_media(current,path,'Captura do jogo')
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path

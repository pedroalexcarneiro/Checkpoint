"""Captura somente a janela em primeiro plano de uma sessão elegível."""
import sys
from pathlib import Path
from uuid import uuid4


class WindowsCapture:
    def __init__(self):
        if sys.platform != 'win32':
            raise ValueError('Captura global de janela de jogo disponível no Windows.')
        import ctypes
        from ctypes import wintypes
        self.ctypes = ctypes; self.types = wintypes
        self.user = ctypes.WinDLL('user32', use_last_error=True)
        self.user.GetForegroundWindow.restype = wintypes.HWND
        self.user.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        self.user.IsWindowVisible.argtypes = [wintypes.HWND]
        self.user.IsIconic.argtypes = [wintypes.HWND]
        self.user.IsWindow.argtypes = [wintypes.HWND]
        self.handle = None

    def foreground_pid(self):
        hwnd = self.user.GetForegroundWindow()
        if not hwnd or not self.user.IsWindow(hwnd) or not self.user.IsWindowVisible(hwnd) or self.user.IsIconic(hwnd):
            raise ValueError('Deixe a janela do jogo aberta e em primeiro plano para capturar.')
        owner = self.types.DWORD()
        self.user.GetWindowThreadProcessId(hwnd, self.ctypes.byref(owner))
        self.handle = hwnd
        return owner.value

    def client_rect(self):
        from .windows_capture import client_rect
        return client_rect(self.user, self.handle)

    def grab_client(self, rect):
        from .windows_capture import grab_client
        return grab_client(self.user, rect)

    def capture(self, pid):
        expected = self.handle
        if self.foreground_pid() != pid or self.handle != expected:
            raise ValueError('A janela em primeiro plano mudou. Tente capturar novamente.')
        rect = self.client_rect()
        pixmap = self.grab_client(rect)
        if self.foreground_pid() != pid or self.handle != expected or self.client_rect() != rect:
            raise ValueError('A janela em primeiro plano mudou durante a captura. Nenhum arquivo foi salvo.')
        return pixmap


def capture_game(window, adapter=None):
    sessions = list(window.launcher.active.values())
    if not sessions:
        raise ValueError('Nenhum jogo aberto pelo Checkpoint está em sessão para capturar.')
    adapter = adapter or WindowsCapture()
    pid = adapter.foreground_pid()
    eligible = [item for item in sessions if item[0].pid == pid and item[0].poll() is None]
    if len(eligible) != 1:
        raise ValueError('A janela em primeiro plano não corresponde a uma única sessão iniciada pelo Checkpoint. Ative o jogo; processos-filhos de launchers ainda não são reconhecidos.')
    current = eligible[0][2]
    pixmap = adapter.capture(pid)
    if pixmap.isNull():
        raise ValueError('A janela do jogo não forneceu uma captura. Tente o jogo em modo janela.')
    directory = Path(window.library.setting('captures', '') or window.library.db.path.parent / 'captures')
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / (uuid4().hex + '.png')
    if not pixmap.save(str(path), 'PNG'):
        raise ValueError('Não foi possível salvar a captura.')
    try:
        window.library.add_media(current, path, 'Captura do jogo')
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path

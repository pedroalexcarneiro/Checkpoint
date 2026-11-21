"""Captura somente a janela em primeiro plano de uma sessão elegível."""
import sys
from collections import deque
from pathlib import Path
from uuid import uuid4
from PySide6.QtCore import QObject,QSaveFile,QIODevice,Signal,Qt


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


def capture_frame(window, adapter=None):
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
    return current,pixmap.toImage()


def save_frame(directory,image):
    path=directory/(uuid4().hex+'.png')
    try:
        directory.mkdir(parents=True,exist_ok=True)
        output=QSaveFile(str(path))
        if not output.open(QIODevice.WriteOnly):raise OSError(output.errorString())
        if not image.save(output,'PNG'):
            output.cancelWriting()
            raise OSError('Falha na codificação PNG')
        if not output.commit():raise OSError(output.errorString())
    except OSError as error:
        raise ValueError('Não foi possível salvar a captura. Confira espaço e permissões da pasta.') from error
    return path


def capture_directory(window):
    return Path(window.library.setting('captures','') or window.library.db.path.parent/'captures')


def register_frame(library,game_id,path):
    try:
        library.add_media(game_id,path,'Captura do jogo')
    except Exception:
        path.unlink(missing_ok=True)
        raise


def capture_game(window,adapter=None):
    """Fluxo direto preservado para a validação isolada do backend."""
    game_id,image=capture_frame(window,adapter)
    path=save_frame(capture_directory(window),image)
    register_frame(window.library,game_id,path)
    return path


class CaptureWriter(QObject):
    saved=Signal(int)
    failed=Signal(str)

    def __init__(self,window):
        super().__init__(window)
        self.window=window
        self.waiting=deque()
        self.job=None

    @property
    def busy(self):return self.job is not None or bool(self.waiting)

    def request(self):
        if len(self.waiting)+bool(self.job)>=4:
            raise ValueError('Aguarde as capturas pendentes antes de tentar de novo.')
        game_id,image=capture_frame(self.window)
        self.waiting.append((game_id,capture_directory(self.window),image))
        self.start_next()

    def start_next(self):
        if self.job is not None or not self.waiting:return
        from .jobs import Job
        game_id,directory,image=self.waiting.popleft()
        self.job=Job(lambda:(game_id,save_frame(directory,image)),self)
        self.job.succeeded.connect(self.register,Qt.QueuedConnection)
        self.job.failed.connect(self.failed,Qt.QueuedConnection)
        self.job.finished.connect(self.finish,Qt.QueuedConnection)
        self.job.start()

    def register(self,result):
        game_id,path=result
        try:register_frame(self.window.library,game_id,path)
        except Exception:
            self.failed.emit('Não foi possível registrar a captura em Memórias. Verifique o banco de dados.')
        else:self.saved.emit(game_id)

    def finish(self):
        self.job.deleteLater()
        self.job=None
        self.start_next()

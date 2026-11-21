"""Eventos Windows de energia/sessão, sem pergunta nem operação de rede."""
import sys
import logging
import sqlite3


class SessionEvents:
    def __init__(self, launcher):
        self.launcher = launcher

    def handle_code(self, code, value):
        if code == 0x11:  # WM_QUERYENDSESSION: desligamento ainda pode ser cancelado.
            self.launcher.checkpoint(force=True, reason='shutdown_query')
        elif code == 0x16 and value:  # WM_ENDSESSION confirmado.
            self.launcher.interrupt(reason='shutdown')
        elif code == 0x218:  # WM_POWERBROADCAST
            if value == 4:  # PBT_APMSUSPEND
                self.launcher.suspend()
            elif value in (7, 18):  # retomada manual/automática
                self.launcher.resume()

    def native(self, message):
        if sys.platform != 'win32':
            return
        import ctypes
        from ctypes import wintypes
        try:
            msg = ctypes.cast(int(message), ctypes.POINTER(wintypes.MSG)).contents
            self.handle_code(msg.message, msg.wParam)
        except (TypeError, ValueError, OSError, sqlite3.Error):
            logging.exception('Não foi possível persistir o evento de sessão do Windows.')
            return

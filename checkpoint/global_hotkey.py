"""Atalho nativo Windows, com substituição transacional e liberação explícita."""
import sys
from PySide6.QtCore import QAbstractNativeEventFilter
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication


def native_key(sequence):
    sequence = QKeySequence(sequence)
    if sequence.count() != 1:
        raise ValueError('Escolha uma combinação única para a captura.')
    text = sequence.toString(QKeySequence.PortableText)
    parts = text.split('+'); key = parts.pop()
    modifiers = {'Ctrl': 2, 'Shift': 4, 'Alt': 1, 'Meta': 8}
    if any(part not in modifiers for part in parts):
        raise ValueError('Combinação de captura inválida.')
    if len(key) == 1 and key.isascii() and key.isalnum():
        vk = ord(key.upper())
    elif key.startswith('F') and key[1:].isdigit() and 1 <= int(key[1:]) <= 24:
        vk = 0x70 + int(key[1:]) - 1
    else:
        raise ValueError('Use uma letra, número ou tecla F1–F24 com modificador.')
    if not parts:
        raise ValueError('Inclua Ctrl, Alt, Shift ou Meta no atalho de captura.')
    return sum(modifiers[part] for part in set(parts)) | 0x4000, vk


class WindowsHotkeyApi:
    def __init__(self):
        import ctypes
        from ctypes import wintypes
        self.user = ctypes.WinDLL('user32', use_last_error=True)
        self.user.RegisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.UINT, wintypes.UINT]
        self.user.UnregisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int]

    def register(self, identity, modifiers, key):
        return bool(self.user.RegisterHotKey(None, identity, modifiers, key))

    def unregister(self, identity):
        return bool(self.user.UnregisterHotKey(None, identity))


class GlobalCaptureHotkey(QAbstractNativeEventFilter):
    def __init__(self, window, callback, sequence, api=None):
        super().__init__()
        self.api = api if api is not None else (WindowsHotkeyApi() if sys.platform == 'win32' else None)
        self.callback = callback; self.identity = None; self.sequence = QKeySequence()
        self.local = None; self.next_identity = 0x4C00
        if self.api is None:
            self.local = QShortcut(window)
            self.local.setAutoRepeat(False)
            self.local.activated.connect(callback)
        else:
            QApplication.instance().installNativeEventFilter(self)
        if sequence is not None:
            self.setKey(QKeySequence(sequence))

    def key(self):
        return QKeySequence(self.sequence)

    def setKey(self, sequence):
        sequence = QKeySequence(sequence)
        modifiers, key = native_key(sequence)
        if sequence == self.sequence:
            return
        if self.api is not None:
            identity = self.next_identity
            if not self.api.register(identity, modifiers, key):
                raise ValueError('Atalho de captura em uso. Escolha outra combinação em Configurações.')
            previous = self.identity
            if previous is not None and not self.api.unregister(previous):
                self.api.unregister(identity)
                raise ValueError('Não foi possível liberar o atalho anterior. A configuração foi mantida.')
            self.identity = identity
            self.next_identity = 0x4C01 if identity == 0x4C00 else 0x4C00
        else:
            self.local.setKey(sequence)
        self.sequence = sequence

    def nativeEventFilter(self, event_type, message):
        import ctypes
        from ctypes import wintypes
        event = ctypes.cast(int(message), ctypes.POINTER(wintypes.MSG)).contents
        if event.message == 0x0312 and event.wParam == self.identity:
            self.callback()
            return True, 0
        return False, 0

    def close(self):
        if self.api is not None:
            if self.identity is not None:
                self.api.unregister(self.identity); self.identity = None
            QApplication.instance().removeNativeEventFilter(self)
        elif self.local is not None:
            self.local.setEnabled(False)

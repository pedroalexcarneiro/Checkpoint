"""Cor nativa da barra de título Windows, preservando os controles do sistema."""
import sys


def titlebar_theme(window,dark):
    if sys.platform!='win32':return False
    try:
        import ctypes
        value=ctypes.c_int(bool(dark))
        function=ctypes.windll.dwmapi.DwmSetWindowAttribute
        function.argtypes=[ctypes.c_void_p,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint]
        for attribute in (20,19):
            if function(int(window.winId()),attribute,ctypes.byref(value),ctypes.sizeof(value))==0:return True
    except (OSError,AttributeError):pass
    return False

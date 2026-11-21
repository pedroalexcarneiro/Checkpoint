"""Moldura Windows com bordas nativas, área útil e HTMAXBUTTON para Snap."""
import sys
import logging
from PySide6.QtCore import Qt,QPoint
from .window_controls import border_hit


class WindowsFrameApi:
    def __init__(self):
        import ctypes
        from ctypes import wintypes as w
        self.c=ctypes;self.w=w;self.user=ctypes.WinDLL('user32',use_last_error=True);self.dwm=ctypes.WinDLL('dwmapi',use_last_error=True)
        self.get_style=getattr(self.user,'GetWindowLongPtrW',self.user.GetWindowLongW);self.set_style=getattr(self.user,'SetWindowLongPtrW',self.user.SetWindowLongW)
        self.get_style.argtypes=[w.HWND,ctypes.c_int];self.get_style.restype=ctypes.c_ssize_t
        self.set_style.argtypes=[w.HWND,ctypes.c_int,ctypes.c_ssize_t];self.set_style.restype=ctypes.c_ssize_t
        self.user.SetWindowPos.argtypes=[w.HWND,w.HWND,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,w.UINT]
        self.user.ScreenToClient.argtypes=[w.HWND,ctypes.POINTER(w.POINT)]
        self.user.ShowWindow.argtypes=[w.HWND,ctypes.c_int]
        self.user.MonitorFromWindow.argtypes=[w.HWND,w.DWORD];self.user.MonitorFromWindow.restype=w.HANDLE
    def apply(self,handle):
        c=self.c;w=self.w;style=self.get_style(handle,-16)
        if not style:raise c.WinError(c.get_last_error())
        c.set_last_error(0);self.set_style(handle,-16,(style&~0x80000000)|0x00C00000|0x00040000|0x00080000|0x00020000|0x00010000)
        if c.get_last_error():raise c.WinError(c.get_last_error())
        class Margins(c.Structure):_fields_=[('left',c.c_int),('right',c.c_int),('top',c.c_int),('bottom',c.c_int)]
        margins=Margins(1,1,1,1);self.dwm.DwmExtendFrameIntoClientArea.argtypes=[w.HWND,c.POINTER(Margins)]
        if self.dwm.DwmExtendFrameIntoClientArea(handle,c.byref(margins))!=0:raise OSError('Moldura nativa indisponível.')
        if not self.user.SetWindowPos(handle,None,0,0,0,0,0x27):raise c.WinError(c.get_last_error())
    def client_point(self,handle,x,y):
        point=self.w.POINT(x,y)
        if not self.user.ScreenToClient(handle,self.c.byref(point)):raise self.c.WinError(self.c.get_last_error())
        return point
    def minimize(self,handle):
        self.user.ShowWindow(handle,6)  # SW_MINIMIZE
    def monitor(self,handle):
        c=self.c;w=self.w
        class Monitor(c.Structure):_fields_=[('size',w.DWORD),('screen',w.RECT),('work',w.RECT),('flags',w.DWORD)]
        info=Monitor();info.size=c.sizeof(info);monitor=self.user.MonitorFromWindow(handle,2)
        self.user.GetMonitorInfoW.argtypes=[w.HANDLE,c.POINTER(Monitor)]
        if not self.user.GetMonitorInfoW(monitor,c.byref(info)):raise c.WinError(c.get_last_error())
        return info
    def dwm_message(self,handle,message,wparam,lparam):
        c=self.c;w=self.w;result=c.c_ssize_t()
        self.dwm.DwmDefWindowProc.argtypes=[w.HWND,w.UINT,c.c_size_t,c.c_ssize_t,c.POINTER(c.c_ssize_t)]
        handled=self.dwm.DwmDefWindowProc(handle,message,wparam,lparam,c.byref(result))
        return bool(handled),result.value


class IntegratedFrame:
    def __init__(self,window,bar):
        self.window=window;self.bar=bar;self.applied=False;self.failed=False;self.api=None;self.original_flags=window.windowFlags()
        if sys.platform=='win32':
            try:self.api=WindowsFrameApi()
            except (OSError,AttributeError):self.failed=True
        window.setWindowFlag(Qt.FramelessWindowHint,True)
    def apply(self):
        if self.applied:return
        if self.failed:self.fallback();return
        if self.api is None:self.applied=True;return
        try:self.api.apply(int(self.window.winId()));self.applied=True
        except (OSError,AttributeError,ValueError):
            self.failed=True;logging.warning('Moldura integrada indisponível; controles nativos preservados.');self.fallback()
    def fallback(self):
        self.applied=True;self.bar.hide();self.window.setWindowFlags(self.original_flags);self.window.show()
    def handle(self,message):
        if self.api is None or self.failed:return False,0
        c=self.api.c;w=self.api.w
        try:
            msg=c.cast(int(message),c.POINTER(w.MSG)).contents;handle=int(msg.hWnd or 0)
            if not handle:return False,0
            if msg.message==0x83:
                if self.window.isMaximized():
                    work=self.api.monitor(handle).work;rect=c.cast(msg.lParam,c.POINTER(w.RECT)).contents
                    rect.left=work.left;rect.top=work.top;rect.right=work.right;rect.bottom=work.bottom
                return True,0
            if msg.message==0x24:
                class Limits(c.Structure):_fields_=[('reserved',w.POINT),('maximum',w.POINT),('position',w.POINT),('minimum_track',w.POINT),('maximum_track',w.POINT)]
                limits=c.cast(msg.lParam,c.POINTER(Limits)).contents;info=self.api.monitor(handle);ratio=self.window.devicePixelRatioF()
                limits.position.x=info.work.left-info.screen.left;limits.position.y=info.work.top-info.screen.top
                limits.maximum.x=info.work.right-info.work.left;limits.maximum.y=info.work.bottom-info.work.top
                limits.minimum_track.x=round(self.window.minimumWidth()*ratio);limits.minimum_track.y=round(self.window.minimumHeight()*ratio)
                limits.maximum_track.x=max(limits.maximum_track.x,limits.maximum.x);limits.maximum_track.y=max(limits.maximum_track.y,limits.maximum.y)
                return True,0
            if msg.message==0x84:
                physical=self.api.client_point(handle,c.c_short(msg.lParam&0xffff).value,
                                               c.c_short((msg.lParam>>16)&0xffff).value)
                ratio=self.window.devicePixelRatioF()
                x=physical.x/ratio;y=physical.y/ratio
                point=QPoint(round(x),round(y))
                for button in (self.bar.minimize,self.bar.maximize,self.bar.close_button):
                    location=button.mapTo(self.window,QPoint())
                    if button.rect().translated(location).contains(point):return True,9 if button is self.bar.maximize else 1
                if not self.window.isMaximized():
                    edge=border_hit(x,y,self.window.width(),self.window.height(),8)
                    if edge is not None:return True,edge
                if self.bar.rect().translated(self.bar.mapTo(self.window,QPoint())).contains(point):return True,2
            return self.api.dwm_message(handle,msg.message,msg.wParam,msg.lParam)
        except (OSError,ValueError,TypeError,AttributeError,OverflowError):return False,0

"""Cópia nova dos pixels visíveis da área cliente, sem PrintWindow/bitmap de HWND."""


def client_rect(user, hwnd):
    import ctypes as c
    from ctypes import wintypes as w
    user.GetClientRect.argtypes = [w.HWND, c.POINTER(w.RECT)]
    user.ClientToScreen.argtypes = [w.HWND, c.POINTER(w.POINT)]
    rect = w.RECT(); origin = w.POINT()
    if not user.GetClientRect(hwnd, c.byref(rect)) or not user.ClientToScreen(hwnd, c.byref(origin)):
        raise ValueError('Não foi possível localizar a área visível do jogo.')
    width, height = rect.right-rect.left, rect.bottom-rect.top
    left, top = user.GetSystemMetrics(76), user.GetSystemMetrics(77)
    right, bottom = left+user.GetSystemMetrics(78), top+user.GetSystemMetrics(79)
    if width <= 0 or height <= 0 or origin.x < left or origin.y < top or origin.x+width > right or origin.y+height > bottom:
        raise ValueError('Deixe a janela inteira do jogo visível na tela para capturar.')
    return origin.x, origin.y, width, height


def grab_client(user, rect):
    import ctypes as c
    from ctypes import wintypes as w
    from PySide6.QtGui import QImage, QPixmap
    gdi = c.WinDLL('gdi32', use_last_error=True)
    user.GetDC.argtypes = [w.HWND]; user.GetDC.restype = w.HDC
    user.ReleaseDC.argtypes = [w.HWND, w.HDC]
    gdi.CreateCompatibleDC.argtypes = [w.HDC]; gdi.CreateCompatibleDC.restype = w.HDC
    gdi.SelectObject.argtypes = [w.HDC, w.HANDLE]; gdi.SelectObject.restype = w.HANDLE
    gdi.DeleteObject.argtypes = [w.HANDLE]; gdi.DeleteDC.argtypes = [w.HDC]
    gdi.BitBlt.argtypes = [w.HDC, c.c_int, c.c_int, c.c_int, c.c_int, w.HDC, c.c_int, c.c_int, w.DWORD]
    class Header(c.Structure):
        _fields_ = [('size', w.DWORD), ('width', w.LONG), ('height', w.LONG),
            ('planes', w.WORD), ('bits', w.WORD), ('compression', w.DWORD), ('image_size', w.DWORD),
            ('x_pixels', w.LONG), ('y_pixels', w.LONG), ('used', w.DWORD), ('important', w.DWORD)]
    class BitmapInfo(c.Structure):
        _fields_ = [('header', Header), ('colors', w.DWORD*3)]
    gdi.CreateDIBSection.argtypes = [w.HDC, c.POINTER(BitmapInfo), w.UINT, c.POINTER(c.c_void_p), w.HANDLE, w.DWORD]
    gdi.CreateDIBSection.restype = w.HBITMAP
    x, y, width, height = rect
    info = BitmapInfo(); info.header = Header(c.sizeof(Header), width, -height, 1, 32, 0, width*height*4, 0, 0, 0, 0)
    desktop = memory = bitmap = previous = None
    try:
        desktop = user.GetDC(None)
        if not desktop: raise ValueError('Tela indisponível para captura.')
        memory = gdi.CreateCompatibleDC(desktop)
        if not memory: raise ValueError('Não foi possível preparar a captura.')
        bits = c.c_void_p()
        bitmap = gdi.CreateDIBSection(desktop, c.byref(info), 0, c.byref(bits), None, 0)
        if not bitmap or not bits.value: raise ValueError('Não foi possível reservar a imagem da captura.')
        previous = gdi.SelectObject(memory, bitmap)
        if not previous or previous == c.c_void_p(-1).value:
            previous = None
            raise ValueError('Não foi possível preparar a imagem da captura.')
        try: c.WinDLL('dwmapi').DwmFlush()
        except (OSError, AttributeError): pass
        if not gdi.BitBlt(memory, 0, 0, width, height, desktop, x, y, 0x00CC0020 | 0x40000000):
            raise ValueError('O Windows não forneceu o quadro atual do jogo. Tente o modo janela sem bordas.')
        data = c.string_at(bits, width*height*4)
        image = QImage(data, width, height, width*4, QImage.Format_RGB32).copy()
        return QPixmap.fromImage(image)
    finally:
        if previous: gdi.SelectObject(memory, previous)
        if bitmap: gdi.DeleteObject(bitmap)
        if memory: gdi.DeleteDC(memory)
        if desktop: user.ReleaseDC(None, desktop)

"""Captura um HWND por Windows Graphics Capture na thread de trabalho."""
from threading import Event
from PySide6.QtGui import QImage


def capture_window(hwnd, native_factory=None):
    if native_factory is None:
        try:
            from ._capture_native.windows_capture import NativeWindowsCapture
        except ImportError as error:
            raise ValueError('A captura por janela não está disponível nesta instalação.') from error
        native_factory=NativeWindowsCapture

    frames=[]
    ready=Event()

    def received(frame,length,width,height,stopping,_timespan):
        try:
            stride=int(frame.bytes_per_row)
            if width<=0 or height<=0 or width*height>60_000_000 or stride<width*4 or length!=stride*height:return
            pixels=frame.buffer_view().tobytes()
            if len(pixels)!=length:return
            image=QImage(pixels,width,height,stride,QImage.Format_RGB32).copy()
            sample=image.scaled(32,32)
            if any(sample.pixel(x,y)&0xffffff for y in range(sample.height()) for x in range(sample.width())):
                frames.append(image)
        finally:
            if frames:
                stopping[0]=True
                ready.set()

    try:
        capture=native_factory(received,ready.set,False,None,False,None,None,None,None,hwnd)
        control=capture.start_free_threaded()
        try:
            ready.wait(1.8)
        finally:
            if not control.is_finished():control.stop()
    except Exception as error:
        raise ValueError('O Windows não conseguiu capturar a janela do jogo. Tente o modo janela ou sem bordas.') from error
    if not frames:
        raise ValueError('A janela do jogo não forneceu uma imagem. Confira se ela está aberta e não minimizada.')
    return frames[0]

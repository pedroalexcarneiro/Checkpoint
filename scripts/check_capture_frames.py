"""Dois quadros de uma janela própria; Windows nativo não homologa DirectX/HSR."""
import json
import os
from pathlib import Path
import sys
from PySide6.QtGui import QColor
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QWidget
from checkpoint.game_capture import WindowsCapture


def main():
    output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
    app=QApplication([]);window=QWidget();window.setWindowTitle(sys.argv[2]);window.resize(320,180)
    window.move(60,60);window.show();window.raise_();window.activateWindow()
    QTest.qWait(150)
    backend=WindowsCapture() if sys.platform=='win32' else None
    if backend is not None:
        backend.user.SetForegroundWindow.argtypes=[backend.types.HWND]
        backend.user.SetForegroundWindow(int(window.winId()))
        QTest.qWait(100)
        if backend.foreground_pid()!=os.getpid() or backend.handle!=int(window.winId()):
            raise RuntimeError('A janela controlada não recebeu o primeiro plano.')
    for name in ('red','blue'):
        window.setStyleSheet('background: '+name+';');window.repaint();QTest.qWait(100)
        if backend is not None:
            assert backend.foreground_pid()==os.getpid()
            pixmap=backend.capture(os.getpid())
        else:pixmap=window.grab()
        image=pixmap.toImage()
        assert image.pixelColor(image.width()//2,image.height()//2)==QColor(name)
        assert pixmap.save(str(output/(name+'.png')))
    window.close()
    print(json.dumps({'qt_platform':app.platformName(),'native_windows':backend is not None,
        'frames':['red','blue'],'target':sys.argv[2],'hsr_validated':False}))


if __name__=='__main__':main()

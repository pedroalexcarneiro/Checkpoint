import ctypes
from ctypes import wintypes
from types import SimpleNamespace
import pytest
import os
import subprocess
import sys


@pytest.mark.parametrize('handle',[0x1234,0x123456789])
def test_creation_message_never_asks_qt_to_create_a_window_again(handle):
    from checkpoint.windows_frame import IntegratedFrame
    class CreatingWindow:
        def winId(self):raise AssertionError('winId recria a janela durante a mensagem de criação')
        def isMaximized(self):return False
    frame=object.__new__(IntegratedFrame)
    frame.window=CreatingWindow();frame.failed=False
    frame.api=SimpleNamespace(c=ctypes,w=wintypes)
    message=wintypes.MSG();message.hWnd=handle;message.message=0x83
    assert frame.handle(ctypes.addressof(message))==(True,0)


def test_invalid_native_message_does_not_create_a_window():
    from checkpoint.windows_frame import IntegratedFrame
    class CreatingWindow:
        def winId(self):raise AssertionError('Não criar HWND para mensagem sem destinatário')
    frame=object.__new__(IntegratedFrame)
    frame.window=CreatingWindow();frame.failed=False
    frame.api=SimpleNamespace(c=ctypes,w=wintypes)
    message=wintypes.MSG();message.message=0x83
    assert frame.handle(ctypes.addressof(message))==(False,0)


@pytest.mark.parametrize('title',['Portal 2','Hades'])
def test_real_platform_window_opens_and_closes_in_isolated_process(folder,title):
    platform='windows' if sys.platform=='win32' else 'offscreen'
    code=r'''
import faulthandler,sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.credentials import CredentialVault
from checkpoint.window import MainWindow
faulthandler.enable();faulthandler.dump_traceback_later(15,exit=True)
root=Path(sys.argv[1]);app=QApplication([])
assert app.platformName()==sys.argv[3]
CredentialVault.get=lambda *args:None
db=Database(root/'native.sqlite');lib=Library(db)
lib.set_setting('artwork.auto',False);lib.set_setting('prices.auto',False)
lib.save_game({'title':sys.argv[2],'platform':'PC'})
window=MainWindow(lib)
def verify():
    try:
        assert window.isVisible() and int(window.winId())>0
        if sys.platform=='win32':
            import ctypes
            from ctypes import wintypes
            api=ctypes.WinDLL('user32');api.IsWindow.argtypes=[wintypes.HWND]
            assert api.IsWindow(int(window.winId()))
        assert window.grab().save(str(root/'native-startup.png'))
        window.close();assert not window.isVisible()
        assert window.capture_shortcut.identity is None
        app.exit(0)
    except BaseException:
        import traceback;traceback.print_exc();app.exit(2)
QTimer.singleShot(200,verify)
window.show();result=app.exec()
faulthandler.cancel_dump_traceback_later();db.close()
raise SystemExit(result)
'''
    result=subprocess.run([sys.executable,'-X','faulthandler','-c',code,str(folder),title,platform],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=25,env={**os.environ,'QT_QPA_PLATFORM':platform})
    assert result.returncode==0,result.stdout+result.stderr
    assert (folder/'native-startup.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n')

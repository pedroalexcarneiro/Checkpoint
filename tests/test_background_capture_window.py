from types import SimpleNamespace
import pytest
from PySide6.QtCore import QThread
from PySide6.QtGui import QColor,QImage
from checkpoint.background_capture import capture_window
from checkpoint.game_capture import WindowsCapture
from test_bugs_0134 import ui,sample
from test_capture_refresh_0139 import wait_for_capture


def test_capture_reads_frame_of_requested_hwnd_and_copies_it():
    pixels=bytearray((0,40,230,255)*3+(0,0,0,0))
    class Native:
        def __init__(self,on_frame,on_closed,*options):
            assert options[-3:]==(None,None,77)
            self.callback=on_frame

        def start_free_threaded(self):
            frame=SimpleNamespace(bytes_per_row=16,buffer_view=lambda:memoryview(pixels))
            stopping=[False]
            self.callback(frame,len(pixels),3,1,stopping,0)
            assert stopping[0]
            return SimpleNamespace(is_finished=lambda:True)

    result=capture_window(77,Native)
    pixels[:]=bytes(len(pixels))
    assert result.width()==3 and result.height()==1
    assert result.pixelColor(1,0)==QColor(230,40,0)


def test_background_target_resolves_one_window_and_refuses_ambiguity():
    capture=object.__new__(WindowsCapture)
    visible={19:900,20:101,30:202}
    def list_windows(callback,_):
        for hwnd in visible:callback(hwnd,0)
    capture.visible_owner=visible.get
    capture.user=SimpleNamespace(GetForegroundWindow=lambda:19,EnumWindows=list_windows,GetWindow=lambda *_:0)
    capture.enumerator=lambda callback:callback
    capture.read_target=lambda hwnd,process:(hwnd,process.pid)
    one=(SimpleNamespace(pid=101,poll=lambda:None),0,10,True)
    two=(SimpleNamespace(pid=202,poll=lambda:None),0,20,True)
    game_id,read=capture.capture_target([one])
    assert game_id==10 and read()==(20,101)
    with pytest.raises(ValueError,match='mais de uma janela'):
        capture.capture_target([one,two])


def test_window_frame_is_read_off_gui_and_saved_without_success_banner(ui,app,monkeypatch):
    window,game_id=ui
    window.launcher.active[1]=(SimpleNamespace(pid=101,poll=lambda:None),0,game_id,True)
    window.navigate(3)
    class Capture:
        def capture_target(self,sessions):
            assert sessions[0][2]==game_id
            return game_id,self.read

        def read(self):
            assert QThread.currentThread() is not app.thread()
            frame=QImage(12,12,QImage.Format_RGB32)
            frame.fill(QColor('#993011'))
            return frame

    monkeypatch.setattr('checkpoint.game_capture.WindowsCapture',Capture)
    try:
        window.capture_game_window();wait_for_capture(window)
        assert not window.statusBar().currentMessage()
        row=window.library.sql.execute('SELECT * FROM media_files').fetchone()
        assert row['game_id']==game_id
        assert QImage(row['path']).pixelColor(2,2)==QColor('#993011')
    finally:window.launcher.active.clear()

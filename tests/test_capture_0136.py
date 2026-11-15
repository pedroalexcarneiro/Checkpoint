from types import SimpleNamespace
import pytest
from PySide6.QtGui import QPixmap
from checkpoint.global_hotkey import GlobalCaptureHotkey, native_key
from checkpoint.game_capture import capture_game
from test_bugs_0134 import ui, sample

class Api:
    def __init__(self):self.active={};self.conflict=False
    def register(self,i,m,k):
        if self.conflict:return False
        assert i not in self.active
        self.active[i]=(m,k);return True
    def unregister(self,i):return self.active.pop(i,None) is not None


def test_registration_is_atomic_and_released(app):
    api=Api();h=GlobalCaptureHotkey(None,lambda:None,'Ctrl+Shift+S',api)
    first=h.identity;assert len(api.active)==1 and api.active[first][0]&0x4000
    h.setKey('Ctrl+Shift+S');assert h.identity==first and len(api.active)==1
    api.conflict=True
    with pytest.raises(ValueError,match='em uso'):h.setKey('Ctrl+Alt+S')
    assert h.identity==first and h.key().toString()=='Ctrl+Shift+S'
    api.conflict=False;h.setKey('Ctrl+Alt+S')
    assert first not in api.active and len(api.active)==1
    h.close();h.close();assert api.active=={}

@pytest.mark.parametrize('text',['S','Ctrl+S, Ctrl+P','Ctrl+Left'])
def test_invalid_shortcuts_rejected(text):
    with pytest.raises(ValueError):native_key(text)


def test_foreground_selects_session_not_open_detail(ui):
    w,i=ui;j=w.library.save_game({'title':'Segundo jogo','platform':'PC'})
    w.launcher.active={1:(SimpleNamespace(pid=101,poll=lambda:None),0,i,True),2:(SimpleNamespace(pid=202,poll=lambda:None),0,j,True)}
    w.current_game=i
    class Adapter:
        pid=202
        def foreground_pid(self):return self.pid
        def capture(self,pid):
            assert pid==self.pid
            pix=QPixmap(200,100);pix.fill();return pix
    a=Adapter()
    try:
        path=capture_game(w,a)
        rows=w.library.sql.execute('SELECT game_id,path FROM media_files').fetchall()
        assert [(r['game_id'],r['path']) for r in rows]==[(j,str(path))]
        assert len(w.launcher.active)==2 and w.current_game==i
        for pid in [999,303]:
            a.pid=pid
            with pytest.raises(ValueError,match='sessão'):capture_game(w,a)
        assert w.library.sql.execute('SELECT count(*) FROM media_files').fetchone()[0]==1
        a.pid=101;w.launcher.active[3]=(SimpleNamespace(pid=101,poll=lambda:None),0,j,True)
        with pytest.raises(ValueError,match='sessão'):capture_game(w,a)
        del w.launcher.active[3];w.launcher.active[1][0].poll=lambda:0
        with pytest.raises(ValueError,match='sessão'):capture_game(w,a)
    finally:w.launcher.active.clear()

from datetime import datetime,timezone
import os
from time import monotonic
from uuid import uuid4

from PySide6.QtGui import QColor,QImage
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QLabel

from checkpoint import media_index
from checkpoint.media_folders import managed_folder
from test_bugs_0134 import ui,sample


def picture(path,color='cyan'):
    image=QImage(70,40,QImage.Format_RGB32)
    image.fill(QColor(color))
    assert image.save(str(path))


def wait_for(predicate):
    end=monotonic()+6
    while not predicate() and monotonic()<end:QTest.qWait(10)
    assert predicate()


def test_import_waits_for_stable_file_and_rejects_bad_data(folder,monkeypatch):
    where=folder/'capture'
    where.mkdir()
    frame=where/'frame.PNG'
    frame.write_bytes(b'not an image')
    text=where/'texto.txt';text.write_text('nota',encoding='utf-8')
    invalid=where/'filme.mp4';invalid.write_bytes(b'invalid video')
    clock=[0]
    monkeypatch.setattr(media_index,'monotonic',lambda:clock[0])
    def scan(pending=None,rejected=None):
        return media_index.scan_folders({where:1},set(),{},set(),pending or {},rejected or {})
    first=scan()
    assert not first[2] and set(first[0])=={frame,invalid}
    clock[0]=1
    picture(frame)
    second=scan(first[0])
    assert not second[2]
    clock[0]=2
    third=scan(second[0])
    assert not third[2] and invalid in third[1]
    clock[0]=3
    final=scan(third[0],third[1])
    assert len(final[2])==1
    game_id,path,kind,_=final[2][0]
    assert (game_id,path,kind)==(1,str(frame),'image')


def test_index_updates_visible_memories_preserves_dates_and_ignores_deleted_card(ui,folder,monkeypatch):
    window,first=ui
    library=window.library
    title='Mesmo título: versão?'
    library.save_game({'title':title,'platform':'PC'},first)
    second=library.save_game({'title':title,'platform':'Nintendo Switch'})
    timestamp=1_700_000_000
    one=managed_folder(library,first);two=managed_folder(library,second)
    assert one!=two and ':' not in one.name and '?' not in one.name
    one.mkdir(parents=True);two.mkdir(parents=True)
    library.save_game({'title':'Novo nome'},first)
    assert managed_folder(library,first)==one
    external=folder/f'externo-{uuid4().hex}.png';picture(external)
    library.add_media(first,external)
    window.navigate(3)
    window.media_index.request()
    wait_for(lambda:str(one) in window.media_index.watcher.directories())
    index=window.media_index
    a=one/'Captura A.png';b=two/'Captura B.png'
    picture(a,'red');picture(b,'blue')
    os.utime(a,(timestamp,timestamp))
    def media():
        return {row['path']:dict(row) for row in library.sql.execute('SELECT * FROM media_files')}
    wait_for(lambda:len(media())==3 and window.memory_browser.game_filter.count()==3)
    assert media()[str(a)]['game_id']==first and media()[str(b)]['game_id']==second
    assert media()[str(a)]['created_at']==datetime.fromtimestamp(timestamp,timezone.utc).isoformat()
    record={**media()[str(a)],'title':'Novo nome'}
    from checkpoint.dialog_style import AppMessages
    monkeypatch.setattr('checkpoint.dialog_style.AppMessages.question',lambda *args:AppMessages.Yes)
    window.delete_memory(record)
    b.unlink();wait_for(lambda:str(b) in index.missing)
    assert a.exists() and external.exists()
    assert len(media())==2 and str(b) in media() and str(a) not in media()
    assert any(label.text()=='Arquivo movido ou removido.' for label in window.pages[3].findChildren(QLabel))
    reimport=media_index.MediaFolderIndex(library)
    try:
        wait_for(lambda:str(b) in reimport.missing and reimport.job is None)
        assert len(media())==2
    finally:reimport.stop();reimport.deleteLater()

"""Executa salvar, enriquecer, renderizar e encerrar num processo Qt real."""
import os
import subprocess
import sys

import pytest


CHILD = r'''
import json,sys
from pathlib import Path
from PySide6.QtCore import QBuffer,QByteArray,QIODevice
from PySide6.QtGui import QImage,QColor
from checkpoint.worker import execute_request
from checkpoint.integrations import MetadataResult
import checkpoint.automatic_catalog as catalog
import checkpoint.auto_artwork as artwork
request=Path(sys.argv[1])
payload=json.loads(request.read_text(encoding='utf-8'))
game_id=payload['arguments']['game_id']
catalog.resolve_title=lambda title,platform:MetadataResult('rawg',str(game_id),title,developer='Fixture studio',publisher='Fixture publisher')
def images(lib,identity,force=False):
 from checkpoint.integrations.images import ImageCache
 image=QImage(120,180,QImage.Format_RGB32);image.fill(QColor('blue'))
 data=QByteArray();buffer=QBuffer(data);buffer.open(QIODevice.WriteOnly)
 assert image.save(buffer,'PNG');buffer.close()
 cached=ImageCache(lib.db.path.parent/'images').store(bytes(data))
 with lib.sql:
  lib.sql.execute('UPDATE games SET cover=?,banner=?,logo=? WHERE id=?',(cached,cached,cached,identity))
 return 'Ficha e imagens concluídas'
artwork.obtain_artwork=images
raise SystemExit(execute_request(request))
'''

UI = r'''
import json,sys
from pathlib import Path
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.drive_dialog import DriveDialog
from checkpoint.integrations.drive import DriveScanner
from checkpoint.worker import run_isolated
import checkpoint.completion_queue as completion
import checkpoint.worker as worker
root=Path(sys.argv[1]);mode=sys.argv[2];child=sys.argv[3]
app=QApplication([]);app.setQuitOnLastWindowClosed(False)
db=Database(root/'library.sqlite');lib=Library(db)
original=run_isolated

def isolated(operation,database,**kwargs):
 script='import os;os._exit(139)' if mode=='failure' else child
 return original(operation,database,command_factory=lambda request:[sys.executable,'-X','faulthandler','-c',script,str(request)],**kwargs)
completion.run_isolated=isolated;worker.run_isolated=isolated
window=MainWindow(lib);window.show();drive=None
if mode=='drive':
 DriveScanner(lib,None).record({'id':'fixture','name':'Example (USA).gba'},'/GBA');lib.sql.commit()
 drive=DriveDialog(lib,window);drive.list.setCurrentRow(0);drive.show()

def fill():
 active=app.activeModalWidget()
 if isinstance(active,GameDialog):
  active.fields['title'].setText('Example');active.validate()
 else:QTimer.singleShot(5,fill)

def begin():
 QTimer.singleShot(5,fill)
 if drive:drive.create_game()
 else:window.add_game()
 assert len(lib.games())==1
 print('saved before enrichment finished',flush=True)
 QTimer.singleShot(10,check)

def check():
 busy=bool(drive.jobs) if drive else window.completion_queue.active is not None
 if busy:
  QTimer.singleShot(10,check);return
 game=lib.games()[0]
 if mode=='failure':
  assert not game['cover']
  assert 'continua aberto' in window.statusBar().currentMessage()
 else:
  assert game['developer']=='Fixture studio'
  assert game['publisher']=='Fixture publisher'
  assert all(Path(game[kind]).is_file() for kind in ('cover','banner','logo'))
  window.detail(game['id'])
  if drive:
   row=lib.sql.execute('SELECT * FROM game_files').fetchone()
   assert row['original_name']=='Example (USA).gba' and row['game_id']==game['id']
 assert lib.sql.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
 if drive:drive.close()
 window.close();app.quit()
 print('complete flow and shutdown OK',flush=True)
QTimer.singleShot(0,begin)
QTimer.singleShot(15000,lambda:app.exit(12))
result=app.exec();db.close()
raise SystemExit(result)
'''


@pytest.mark.parametrize('mode',['success','failure','drive'])
def test_full_save_and_loading_process_exits_cleanly(folder,mode):
    result=subprocess.run([sys.executable,'-X','faulthandler','-c',UI,str(folder.resolve()),mode,CHILD],
                          env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,timeout=25)
    assert result.returncode==0,result.stdout+'\n'+result.stderr
    assert 'saved before enrichment finished' in result.stdout
    assert 'complete flow and shutdown OK' in result.stdout


def test_save_smoke_refuses_existing_database(folder):
    database=folder/'checkpoint.sqlite'
    database.write_bytes(b'preserve-existing-data')
    result=subprocess.run([sys.executable,'-m','checkpoint.app','--save-smoke-test','--data-dir',str(folder)],
                          env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,timeout=10)
    assert result.returncode==2
    assert database.read_bytes()==b'preserve-existing-data'

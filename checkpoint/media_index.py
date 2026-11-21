"""Indexa arquivos estáveis em pastas associadas explicitamente a jogos."""
from datetime import datetime,timezone
from pathlib import Path
import sqlite3
import sys
from time import monotonic
from PySide6.QtCore import QFileSystemWatcher,QObject,QSize,QTimer,Qt,Signal
from PySide6.QtGui import QImageReader
from PySide6.QtWidgets import QApplication
from .jobs import Job
from .media_folders import known_folders


IMAGES={'.png','.jpg','.jpeg','.webp'}
VIDEOS={'.mp4','.mkv','.avi','.mov'}
IGNORED='memories.ignored_managed_files'


def media_kind(path):
    suffix=path.suffix.lower()
    if suffix in IMAGES:
        reader=QImageReader(str(path))
        size=reader.size()
        if not size.isValid() or size.width()*size.height()>60_000_000:return None
        reader.setScaledSize(size.scaled(QSize(120,120),Qt.KeepAspectRatio))
        return None if reader.read().isNull() else 'image'
    with path.open('rb') as stream:
        length=path.stat().st_size
        if suffix in ('.mov','.mp4'):
            atoms=set()
            for _ in range(256):
                start=stream.tell()
                header=stream.read(8)
                if not header:break
                if len(header)!=8:return None
                size=int.from_bytes(header[:4],'big')
                if size==1:size=int.from_bytes(stream.read(8),'big')
                if not size:size=length-start
                if start+size<stream.tell() or start+size>length:return None
                atoms.add(header[4:]);stream.seek(start+size)
                if b'moov' in atoms and b'mdat' in atoms:return 'video'
        elif suffix=='.mkv':
            header=stream.read(4096)
            if header.startswith(b'\x1a\x45\xdf\xa3') and b'\x18\x53\x80\x67' in header[4:]:return 'video'
        elif suffix=='.avi':
            header=stream.read(24)
            if (len(header)==24 and header[:4]==b'RIFF' and header[8:16]==b'AVI LIST'
                    and header[20:24]==b'hdrl' and int.from_bytes(header[4:8],'little')+8<=length):return 'video'
    return None


def signature(path):
    stamp=path.stat()
    return stamp.st_size,stamp.st_mtime_ns


def writable_handle_open(path):
    if sys.platform!='win32':return False
    import ctypes
    from ctypes import wintypes
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.CreateFileW.argtypes=(wintypes.LPCWSTR,wintypes.DWORD,wintypes.DWORD,wintypes.LPVOID,
                                 wintypes.DWORD,wintypes.DWORD,wintypes.HANDLE)
    kernel.CreateFileW.restype=wintypes.HANDLE
    kernel.CloseHandle.argtypes=(wintypes.HANDLE,)
    generic_read,file_share_read,open_existing,file_attribute_normal=0x80000000,1,3,128
    handle=kernel.CreateFileW(str(path),generic_read,file_share_read,None,open_existing,file_attribute_normal,None)
    if handle==ctypes.c_void_p(-1).value:
        error=ctypes.get_last_error()
        if error in (32,33):return True
        raise ctypes.WinError(error)
    kernel.CloseHandle(handle)
    return False


def scan_folders(folders,records,indexed,ignored,pending,rejected):
    waiting={};invalid={};added=[];missing=set();watch=set()
    for directory,game_id in folders.items():
        if directory.is_symlink():continue
        directory_path=directory.resolve()
        registered=indexed.get(directory_path,set())
        if directory.parent.is_dir():watch.add(str(directory.parent))
        try:entries=list(directory.iterdir())
        except FileNotFoundError:
            missing.update(registered);continue
        except OSError:continue
        watch.add(str(directory))
        present=set()
        for entry in entries:
            if entry.suffix.lower() not in IMAGES|VIDEOS or entry.is_symlink():continue
            try:
                if not entry.is_file():continue
                path=entry.resolve(strict=True)
                present.add(str(path))
                if str(path) in records or str(path) in ignored:continue
                stamp=signature(path)
                if rejected.get(path)==stamp:
                    invalid[path]=stamp;continue
                observed=monotonic()
                previous=pending.get(path)
                if not previous or previous[0]!=stamp:
                    waiting[path]=(stamp,observed);continue
                if observed-previous[1]<1.5:
                    waiting[path]=previous;continue
                if writable_handle_open(path):
                    waiting[path]=(stamp,observed);continue
                kind=media_kind(path)
                current=signature(path)
                if current!=stamp:
                    waiting[path]=(current,monotonic());continue
                if kind:added.append((game_id,str(path),kind,stamp))
                else:invalid[path]=stamp
            except OSError:continue
        missing.update(registered-present)
    return waiting,invalid,added,missing,watch


class MediaFolderIndex(QObject):
    changed=Signal(object)

    def __init__(self,library,parent=None):
        super().__init__(parent)
        self.library=library;self.job=None;self.rescan=False;self.stopped=False
        self.waiting={};self.rejected={};self.missing=set()
        self.watcher=QFileSystemWatcher(self)
        self.watcher.directoryChanged.connect(self.request)
        self.timer=QTimer(self);self.timer.setSingleShot(True);self.timer.timeout.connect(self.scan)
        QApplication.instance().applicationStateChanged.connect(self.application_state_changed)
        if known_folders(self.library):self.request()

    def application_state_changed(self,state):
        if state==Qt.ApplicationActive:self.request()

    def request(self,*args):
        if self.stopped:return
        if self.job is not None:self.rescan=True
        else:self.timer.start(120)

    def scan(self):
        database=self.library.db.path
        self.job=Job(lambda:scan_library(database,self.waiting,self.rejected),self)
        self.job.succeeded.connect(self.accept,Qt.QueuedConnection)
        self.job.finished.connect(self.finished,Qt.QueuedConnection)
        self.job.start()

    def accept(self,result):
        if self.stopped:return
        self.waiting,self.rejected,added,missing,watch=result
        watched=set(self.watcher.directories())
        if to_remove:=watched-watch:self.watcher.removePaths(list(to_remove))
        if to_add:=watch-watched:self.watcher.addPaths(list(to_add))
        changed=set()
        if added:
            folders=known_folders(self.library)
            allowed={(directory.resolve(),game_id) for directory,game_id in folders.items() if not directory.is_symlink()}
            ignored=set(self.library.setting(IGNORED,[]))
            sql=self.library.sql
            timeout=sql.execute('PRAGMA busy_timeout').fetchone()[0]
            sql.execute('PRAGMA busy_timeout=25')
            try:
                with sql:
                    for game_id,path,kind,stamp in added:
                        if (Path(path).parent,game_id) not in allowed or path in ignored:continue
                        try:
                            if signature(Path(path))!=stamp:
                                self.rescan=True;continue
                        except OSError:continue
                        mtime=datetime.fromtimestamp(stamp[1]/1_000_000_000,timezone.utc).isoformat()
                        cursor=self.library.sql.execute(
                            'INSERT INTO media_files(game_id,path,caption,created_at,kind) '
                            'SELECT ?,?,?,?,? WHERE NOT EXISTS(SELECT 1 FROM media_files WHERE path=?)',
                            (game_id,path,'',mtime,kind,path))
                        if cursor.rowcount:changed.add(game_id)
            except sqlite3.Error:
                self.rescan=True;changed.clear()
            finally:sql.execute(f'PRAGMA busy_timeout={int(timeout)}')
        if changed or missing!=self.missing:
            self.missing=missing
            self.changed.emit(changed)

    def finished(self):
        self.job.deleteLater();self.job=None
        if self.stopped:return
        if self.waiting:self.timer.start(1500)
        elif self.rescan:self.timer.start(120)
        self.rescan=False

    def ignore_deleted(self,path):
        folders=known_folders(self.library)
        if not any(directory.resolve()==Path(path).parent for directory in folders):return
        ignored=set(self.library.setting(IGNORED,[]));ignored.add(path)
        self.library.set_setting(IGNORED,sorted(ignored))

    def stop(self):
        self.stopped=True
        self.timer.stop()
        paths=self.watcher.directories()
        if paths:self.watcher.removePaths(paths)


def scan_library(database,waiting,rejected):
    from contextlib import closing
    from types import SimpleNamespace
    from .library import Library

    with closing(sqlite3.connect(database.absolute().as_uri()+'?mode=ro',uri=True,timeout=.25)) as sql:
        sql.row_factory=sqlite3.Row
        library=Library(SimpleNamespace(path=database,connection=sql))
        folders=known_folders(library)
        records=set();indexed={}
        if folders:
            for row in sql.execute('SELECT path FROM media_files'):
                path=row['path']
                records.add(path)
                indexed.setdefault(Path(path).parent,set()).add(path)
        ignored=set(library.setting(IGNORED,[]))
    return scan_folders(folders,records,indexed,ignored,waiting,rejected)

"""LRU de rasters de apresentação; limite em bytes e invalidação por arquivo."""
from collections import OrderedDict
from pathlib import Path
from PySide6.QtCore import Qt,QSize,QObject,Signal,Slot,QRunnable,QThreadPool
from PySide6.QtGui import QPixmap,QImage,QImageReader


def _read_image(path,width,height,trim):
    """Somente QImage: leitura, recorte transparente e escala podem sair da GUI."""
    reader=QImageReader(str(path));reader.setAutoTransform(True)
    size=reader.size()
    if size.width()<=0 or size.height()<=0 or size.width()*size.height()>60_000_000:return QImage()
    if not trim:reader.setScaledSize(size.scaled(QSize(width,height),Qt.KeepAspectRatio))
    image=reader.read()
    if image.isNull():return image
    if trim and image.hasAlphaChannel():
        mask=image.createAlphaMask();stride=mask.bytesPerLine();data=bytes(mask.constBits())
        left=mask.width();right=-1;top=mask.height();bottom=-1
        for y in range(mask.height()):
            for x,byte in enumerate(data[y*stride:y*stride+(mask.width()+7)//8]):
                if byte:
                    first=x*8+(byte & -byte).bit_length()-1
                    last=min(mask.width()-1,x*8+byte.bit_length()-1)
                    if first<mask.width():
                        left=min(left,first);right=max(right,last);top=min(top,y);bottom=y
        if right>=left:image=image.copy(left,top,right-left+1,bottom-top+1)
    return image.scaled(width,height,Qt.KeepAspectRatio,Qt.SmoothTransformation)


class _RasterSignals(QObject):
    finished=Signal(object,QImage)


class _RasterTask(QRunnable):
    def __init__(self,key):
        super().__init__();self.key=key;self.signals=_RasterSignals()
    def run(self):
        try:image=_read_image(self.key[0],self.key[3],self.key[4],self.key[5])
        except Exception:image=QImage()
        self.signals.finished.emit(self.key,image)


_pool=None


def _raster_pool():
    global _pool
    if _pool is None:
        _pool=QThreadPool();_pool.setMaxThreadCount(2)
    return _pool


class ArtworkCache(QObject):
    ready=Signal()
    def __init__(self,max_bytes=32*1024*1024,*,asynchronous=False,parent=None):
        super().__init__(parent)
        self.max_bytes=max(0,int(max_bytes));self.used_bytes=0;self.entries=OrderedDict()
        self.asynchronous=asynchronous;self.pending={}
    @staticmethod
    def _key(path,width,height,trim):
        if not path or width<=0 or height<=0:return None
        try:
            source=Path(path);stamp=source.stat()
            if not source.is_file():return None
        except OSError:return None
        return (str(source.resolve()),stamp.st_mtime_ns,stamp.st_size,int(width),int(height),trim)
    def load(self,path,width,height,trim=False,*,prefetch=False):
        key=self._key(path,width,height,trim)
        if key is None:return QPixmap()
        if key in self.entries:
            pix,cost=self.entries.pop(key);self.entries[key]=(pix,cost);return pix
        if self.asynchronous:
            if key not in self.pending and len(self.pending)<24:
                task=_RasterTask(key);task.signals.finished.connect(self._image_ready)
                self.pending[key]=task;_raster_pool().start(task,0 if prefetch else 1)
            return QPixmap()
        pix=QPixmap.fromImage(_read_image(key[0],width,height,trim));self._remember(key,pix);return pix
    def _remember(self,key,pix):
        cost=pix.width()*pix.height()*4
        if cost<=self.max_bytes:
            while self.entries and (self.used_bytes+cost>self.max_bytes or len(self.entries)>=256):
                _,(_,previous)=self.entries.popitem(last=False);self.used_bytes-=previous
            self.entries[key]=(pix,cost);self.used_bytes+=cost
    @Slot(object,QImage)
    def _image_ready(self,key,image):
        self.pending.pop(key,None);self._remember(key,QPixmap.fromImage(image));self.ready.emit()
    def cover(self,game,size,*,prefetch=False):
        for field in ('cover','banner'):
            pix=self.load(game.get(field),size.width(),size.height(),prefetch=prefetch)
            if not pix.isNull():return pix
            if self.asynchronous:
                key=self._key(game.get(field),size.width(),size.height(),False)
                if key and key not in self.entries:return QPixmap()
        return QPixmap()

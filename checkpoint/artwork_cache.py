"""LRU de rasters de apresentação; limite em bytes e invalidação por arquivo."""
from collections import OrderedDict
from pathlib import Path
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QPixmap,QImageReader,QRegion


class ArtworkCache:
    def __init__(self,max_bytes=32*1024*1024):
        self.max_bytes=max(0,int(max_bytes));self.used_bytes=0;self.entries=OrderedDict()
    def load(self,path,width,height,trim=False):
        if not path or width<=0 or height<=0:return QPixmap()
        try:
            source=Path(path);stamp=source.stat()
            if not source.is_file():return QPixmap()
        except OSError:return QPixmap()
        key=(str(source.resolve()),stamp.st_mtime_ns,stamp.st_size,int(width),int(height),trim)
        if key in self.entries:
            pix,cost=self.entries.pop(key);self.entries[key]=(pix,cost);return pix
        reader=QImageReader(str(source));reader.setAutoTransform(True)
        size=reader.size()
        if size.width()<=0 or size.height()<=0 or size.width()*size.height()>60_000_000:return QPixmap()
        if not trim:reader.setScaledSize(size.scaled(QSize(width,height),Qt.KeepAspectRatio))
        image=reader.read()
        if image.isNull():return QPixmap()
        pix=QPixmap.fromImage(image)
        if trim and pix.hasAlphaChannel():
            bounds=QRegion(pix.mask()).boundingRect()
            if not bounds.isEmpty():pix=pix.copy(bounds)
        pix=pix.scaled(width,height,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        cost=pix.width()*pix.height()*4
        if cost<=self.max_bytes:
            while self.entries and self.used_bytes+cost>self.max_bytes:
                _,(_,previous)=self.entries.popitem(last=False);self.used_bytes-=previous
            self.entries[key]=(pix,cost);self.used_bytes+=cost
        return pix
    def cover(self,game,size):
        for field in ('cover','banner'):
            pix=self.load(game.get(field),size.width(),size.height())
            if not pix.isNull():return pix
        return QPixmap()

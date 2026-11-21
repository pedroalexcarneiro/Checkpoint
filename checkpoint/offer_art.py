"""Miniatura oficial para ofertas Steam, sem substituir arte da ficha."""
from pathlib import Path
import re
import shutil
from uuid import uuid4

from PySide6.QtCore import QObject,Signal,Slot

from .integrations.images import ImageCache
from .jobs import Job


def steam_header_identity(library,game):
    row=library.sql.execute(
        """SELECT e.external_id, a.provider, a.external_id,
                  a.local_path
           FROM external_identifiers e
           LEFT JOIN artwork_assets a ON a.game_id=e.game_id AND a.kind='banner'
           WHERE e.game_id=? AND e.provider='steam'""",(game['id'],)).fetchone()
    if not row or not re.fullmatch(r'[0-9]{1,10}',row[0]):return None
    current=game.get('banner')
    if current and (row[1:4]!=('steam',row[0],current)):
        return None
    return row[0]


class OfferArt(QObject):
    available=Signal(str,str)

    def __init__(self,root,parent):
        super().__init__(parent)
        self.root=Path(root)/'offer-headers'
        self.requested=set()

    def request(self,identity):
        target=self.root/(identity+'.jpg')
        if target.is_file():return str(target)
        if identity not in self.requested:
            self.requested.add(identity)
            job=Job(lambda:self.download(identity,target),self)
            job.succeeded.connect(self.loaded)
            job.finished.connect(job.deleteLater)
            job.start()
        return None

    def download(self,identity,target):
        url=f'https://cdn.akamai.steamstatic.com/steam/apps/{identity}/header.jpg'
        cached=ImageCache(self.root/'cache',timeout=8).download(url)
        temporary=target.with_name(uuid4().hex+'.partial')
        try:
            shutil.copyfile(cached,temporary)
            temporary.replace(target)
        finally:temporary.unlink(missing_ok=True)
        return identity,str(target)

    @Slot(object)
    def loaded(self,result):
        self.available.emit(*result)

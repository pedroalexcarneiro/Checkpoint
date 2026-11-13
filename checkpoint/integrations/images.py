"""Cache imutável por SHA-256; valida imagem antes da instalação atômica."""
import hashlib
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlsplit
from uuid import uuid4
from PySide6.QtGui import QImageReader
from PySide6.QtCore import QBuffer,QByteArray,QIODevice
from . import IntegrationError

class ImageCache:
    def __init__(self,directory,timeout=30):
        self.timeout=timeout
        self.directory = Path(directory); self.directory.mkdir(parents=True,exist_ok=True)

    def store(self,content):
        if len(content)>25_000_000: raise IntegrationError('Imagem maior que 25 MB.')
        temporary = self.directory/(uuid4().hex+'.partial')
        try:
            temporary.write_bytes(content)
            buffer = QBuffer(); buffer.setData(QByteArray(content)); buffer.open(QIODevice.ReadOnly)
            reader = QImageReader(buffer); reader.setDecideFormatFromContent(True)
            size = reader.size()
            if bytes(reader.format()).lower()==b'gif' or reader.supportsAnimation() or reader.imageCount()>1:
                raise IntegrationError('Use uma imagem estática PNG, JPEG ou WebP; GIFs e animações não são aceitos.')
            if size.width()<=0 or size.height()<=0 or size.width()*size.height()>60_000_000:
                raise IntegrationError('Imagem inválida ou excede o limite de resolução.')
            if reader.read().isNull(): raise IntegrationError('Não foi possível decodificar a imagem.')
            extension = bytes(reader.format()).decode('ascii')
            target = self.directory/(hashlib.sha256(content).hexdigest()+'.'+extension)
            temporary.replace(target); return str(target)
        finally: temporary.unlink(missing_ok=True)

    def download(self,url):
        parsed = urlsplit(url)
        allowed = {'media.rawg.io','cdn2.steamgriddb.com','cdn.steamgriddb.com','images.igdb.com','cdn.akamai.steamstatic.com',
                   'shared.akamai.steamstatic.com','shared.fastly.steamstatic.com',
                   'cdn.cloudflare.steamstatic.com'}
        if parsed.scheme!='https' or parsed.hostname not in allowed:
            raise IntegrationError('Origem de imagem não autorizada.')
        try:
            with urlopen(Request(url,headers={'User-Agent':'Checkpoint/0.1'}),timeout=self.timeout) as response:
                if urlsplit(response.url).hostname not in allowed: raise IntegrationError('Redirecionamento de imagem não autorizado.')
                return self.store(response.read(25_000_001))
        except OSError:
            raise IntegrationError('Falha no download da imagem.') from None

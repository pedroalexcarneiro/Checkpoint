"""GitHub Releases: credencial somente na API, SHA-256 obrigatório, staging local."""
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit
from uuid import uuid4
import requests
from .update_installer import extract_package

REPOSITORY='pedroalexcarneiro/Checkpoint'
MAX_DOWNLOAD=400_000_000

class UpdateError(ValueError): pass

def version(tag):
    match=re.fullmatch(r'v?(\d+)\.(\d+)\.(\d+)',tag)
    return tuple(map(int,match.groups())) if match else None

def select_update(releases,current,previews=False):
    installed=version(current)
    if installed is None: raise UpdateError('Versão instalada inválida.')
    choices=[]
    for release in releases:
        number=version(release.get('tag_name',''))
        if release.get('draft') or release.get('prerelease') and not previews or number is None or number<=installed: continue
        assets=[a for a in release.get('assets',[]) if a.get('name')==f'Checkpoint-{number[0]}.{number[1]}.{number[2]}-windows-x64.zip' and a.get('state')=='uploaded']
        if len(assets)!=1: continue
        asset=assets[0]
        if not re.fullmatch(r'sha256:[0-9a-f]{64}',asset.get('digest') or ''): continue
        if not isinstance(asset.get('id'),int) or asset['id']<=0 or not 0<int(asset.get('size',0))<=MAX_DOWNLOAD: continue
        choices.append((number,{'tag':release['tag_name'],'asset_id':asset['id'],'size':int(asset['size']),'sha256':asset['digest'][7:]}))
    return max(choices,key=lambda c:c[0])[1] if choices else None

class GitHubUpdates:
    def __init__(self,token=None): self.token=token
    def headers(self,binary=False):
        headers={'User-Agent':'Checkpoint','Accept':'application/octet-stream' if binary else 'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
        if self.token: headers['Authorization']='Bearer '+self.token
        return headers
    def check(self,current,previews=False):
        url=f'https://api.github.com/repos/{REPOSITORY}/releases?per_page=100'
        try:
            with requests.get(url,headers=self.headers(),timeout=(10,30),allow_redirects=False,stream=True) as response:
                if response.status_code in {401,403,404}: raise UpdateError('Acesso ao repositório recusado. Verifique o token e a permissão Contents: read.')
                if response.status_code!=200: raise UpdateError('O GitHub não respondeu à consulta. Tente novamente mais tarde.')
                raw=response.raw.read(8_000_001)
                if len(raw)>8_000_000: raise UpdateError('Resposta de versões excedeu o limite.')
                releases=json.loads(raw)
                if not isinstance(releases,list): raise UpdateError('Resposta de versões inválida.')
                return select_update(releases,current,previews)
        except (requests.RequestException,OSError,json.JSONDecodeError): raise UpdateError('Falha ao consultar versões. Verifique a conexão.') from None
    def prepare(self,update,directory):
        directory=Path(directory).resolve()/uuid4().hex; directory.mkdir(parents=True)
        target=directory/'package.zip'; partial=directory/'package.partial'
        response=None
        try:
            response=requests.get(f'https://api.github.com/repos/{REPOSITORY}/releases/assets/{int(update["asset_id"])}',headers=self.headers(True),stream=True,timeout=(10,30),allow_redirects=False)
            if response.status_code in {301,302,303,307,308}:
                location=response.headers.get('Location',''); response.close(); parsed=urlsplit(location)
                if parsed.scheme!='https' or parsed.hostname not in {'release-assets.githubusercontent.com','objects.githubusercontent.com'} or parsed.username or parsed.port not in {None,443}:
                    raise UpdateError('Destino do download não autorizado.')
                # Nunca envia o token para o CDN ou a URL assinada.
                response=requests.get(location,stream=True,timeout=(10,30),allow_redirects=False)
            if response.status_code!=200: raise UpdateError('Falha ao baixar o pacote. Verifique o acesso ao repositório.')
            checksum=hashlib.sha256(); count=0
            with partial.open('xb') as output:
                for block in response.iter_content(1024*1024):
                    count+=len(block)
                    if count>update['size'] or count>MAX_DOWNLOAD: raise UpdateError('Download excedeu o tamanho esperado.')
                    checksum.update(block); output.write(block)
            if count!=update['size'] or checksum.hexdigest()!=update['sha256']: raise UpdateError('Falha na integridade do pacote. A instalação foi preservada.')
            partial.rename(target)
            return str(extract_package(target,directory/'staged'))
        except requests.RequestException: raise UpdateError('Download interrompido. Tente novamente; a versão instalada foi preservada.') from None
        finally:
            if response is not None: response.close()
            partial.unlink(missing_ok=True)

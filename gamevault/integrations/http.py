"""HTTP com TLS, limite de resposta, timeout e erros sem URL/credenciais."""
import json
import time
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from . import IntegrationError

class HttpClient:
    def json(self,url,headers=None,data=None,method=None):
        request = Request(url,data=data,headers={'User-Agent':'GameVault/0.1',**(headers or {})},method=method)
        for attempt in range(3):
            try:
                with urlopen(request,timeout=20) as response:
                    raw = response.read(8_000_001)
                    if len(raw)>8_000_000: raise IntegrationError('Resposta do provedor excedeu o limite.')
                    return json.loads(raw)
            except HTTPError as error:
                if error.code in {429,500,502,503,504} and attempt<2:
                    time.sleep(2**attempt); continue
                raise IntegrationError(f'O provedor respondeu HTTP {error.code}. Verifique a configuração e a disponibilidade.') from None
            except (URLError,TimeoutError,OSError):
                if attempt<2:
                    time.sleep(2**attempt); continue
                raise IntegrationError('Não foi possível conectar ao provedor. Tente novamente mais tarde.') from None
        raise IntegrationError('Limite de tentativas atingido.')

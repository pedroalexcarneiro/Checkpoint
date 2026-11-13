"""Contrato de preços; nenhuma dependência de transporte ou armazenamento de chave."""
from typing import Protocol,TypedDict
from . import IntegrationError

class PriceQuote(TypedDict,total=False):
    current: int|None
    original: int|None
    discount: int|None
    currency: str
    stores: list[dict]

class PriceProvider(Protocol):
    def prices(self,identity=None,url=None)->PriceQuote: ...

class GgDealsApiProvider:
    """Estrutura reservada; transporte depende da documentação oficial."""
    def __init__(self,vault=None):
        self.enabled=vault is not None and vault.get('ggdeals') is not None
    def prices(self,identity=None,url=None)->PriceQuote:
        if not self.enabled:raise IntegrationError('API GG.deals não configurada.')
        raise IntegrationError('API GG.deals aguardando documentação oficial. Use a página pública para consultar preços.')

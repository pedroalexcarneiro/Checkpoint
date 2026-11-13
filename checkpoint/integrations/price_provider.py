"""Contrato de preços; nenhuma dependência de transporte ou armazenamento de chave."""
from typing import Protocol,TypedDict
from . import IntegrationError

class PriceQuote(TypedDict,total=False):
    current: int|None
    historical: int|None
    current_kind: str|None
    original: int|None
    discount: int|None
    currency: str
    stores: list[dict]

class PriceProvider(Protocol):
    def prices(self,identity=None,url=None)->PriceQuote: ...

# Reexportação preserva os imports existentes; implementação em módulo próprio.
from .ggdeals_api import GgDealsApiProvider

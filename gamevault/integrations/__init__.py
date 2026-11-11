"""Contratos comuns de provedores. Nenhum segredo é persistido no SQLite."""
from dataclasses import dataclass,field
from typing import Protocol

@dataclass(frozen=True)
class MetadataResult:
    provider: str
    external_id: str
    title: str
    description: str = ''
    release_date: str = ''
    genres: tuple[str,...] = ()
    platforms: tuple[str,...] = ()
    images: dict[str,str] = field(default_factory=dict)
    developer: str = ''
    publisher: str = ''

class MetadataProvider(Protocol):
    def search(self,title:str) -> list[MetadataResult]: ...

class IntegrationError(RuntimeError):
    pass

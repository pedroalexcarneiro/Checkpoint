"""Filtro visual por famílias; não transfere identidade ou preços entre versões."""
import re
from .integrations.drive import PLATFORMS

FAMILIES=(('Todas','all'),('PC','pc'),('Switch','switch'),('PlayStation','playstation'),('Xbox','xbox'))


def canonical(value):
    value=(value or '').strip();return PLATFORMS.get(value.casefold(),value)


def family(value):
    name=re.sub(r'[^a-z0-9]+',' ',canonical(value).casefold()).strip()
    if name in ('pc','windows','linux','mac','macos','pc windows'):return 'pc'
    if name in ('switch','nintendo switch','nintendo switch 2','switch 2'):return 'switch'
    if name.startswith('playstation') or name in ('ps1','ps2','ps3','ps4','ps5','psp','psx','ps vita'):return 'playstation'
    if name.startswith('xbox') or name in ('x360','xone','xsx','xss'):return 'xbox'
    return 'platform:'+canonical(value)


def options(games):
    extra={canonical(g.get('platform')) for g in games if family(g.get('platform')).startswith('platform:')}
    return [*FAMILIES,*[(p or 'Não definida','platform:'+p) for p in sorted(extra)]]


def selected(games,key):return list(games) if key=='all' else [g for g in games if family(g.get('platform'))==key]

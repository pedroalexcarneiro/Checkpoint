"""Lucide ISC: mesmo traço de 2/24, tamanho definido pelo contexto de uso."""
from functools import lru_cache
from pathlib import Path
from PySide6.QtCore import Qt,QByteArray
from PySide6.QtGui import QIcon,QPixmap,QPainter,QColor
from PySide6.QtSvg import QSvgRenderer

NAMES={'home':'house','library':'layout-grid','stats':'chart-no-axes-column',
       'memories':'image','settings':'settings','wish':'heart','heart':'heart',
       'help':'circle-help','platform':'monitor','clock':'clock-3','user':'user-round',
       'search':'search','folder':'folder-open','download':'download','trophy':'trophy',
       'trash':'trash-2','play':'play','list':'list','filter':'sliders-horizontal','plus':'plus',
       'close':'x','chevron':'chevron-down','chevron-right':'chevron-right','back':'arrow-left','more':'ellipsis',
       'check':'check','warning':'circle-alert','busy':'loader-circle'}

@lru_cache(maxsize=512)
def lucide_icon(name,color,size=24):
    size=max(1,int(size));path=Path(__file__).parent/'assets'/'lucide'/(NAMES.get(name,'file-text')+'.svg')
    data=path.read_text().replace('currentColor',QColor(color).name())
    renderer=QSvgRenderer(QByteArray(data.encode()))
    if not renderer.isValid():raise ValueError('Ícone Lucide inválido: '+name)
    pix=QPixmap(size,size);pix.fill(Qt.transparent);p=QPainter(pix);renderer.render(p);p.end()
    return QIcon(pix)

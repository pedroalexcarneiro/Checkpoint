"""Tamanho de cards compartilhado; preferências sem mudar o schema."""
from dataclasses import dataclass
from .visual_tokens import SPACE

@dataclass(frozen=True)
class CardMetrics:
    columns: int
    width: int
    gap: int

def card_metrics(available,percent=100):
    scale=max(70,min(150,int(percent)))/100
    gap=SPACE['md'] if scale<1 else SPACE['lg'] if scale<=1.25 else SPACE['xl']
    target=round(200*scale)
    columns=max(1,(max(1,int(available))+gap)//(target+gap))
    # QListView reserva a borda final do viewport ao decidir a quebra de linha.
    width=max(1,max(1,int(available)-1)//columns-gap)
    return CardMetrics(columns,width,gap)

def cover_size(library):
    value=library.setting('appearance.cover_size',None)
    if value is None:
        value=80 if library.setting('appearance.density','comfortable')=='compact' else 100
        library.set_setting('appearance.cover_size',value)
    try:return max(70,min(150,int(value)))
    except (ValueError,TypeError):return 100


COVER_CHOICES=(70,90,100,125,150)

def nearest_cover_choice(value):
    try:value=int(value)
    except (TypeError,ValueError):value=100
    return min(COVER_CHOICES,key=lambda choice:(abs(choice-value),choice))

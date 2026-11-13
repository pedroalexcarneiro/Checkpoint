"""Contratos visuais: contraste, componentes, estados e geometrias reais."""
import pytest
from checkpoint.theme import THEMES
from checkpoint.visual_tokens import TYPE,SPACE,RADIUS,WEIGHT,contrast


@pytest.mark.parametrize('key',list(THEMES))
def test_semantic_tokens_and_normal_text_contrast(key):
    colors=THEMES[key].colors
    for token in ('background','surface','elevated','card','border_subtle','text','secondary','muted','accent','success','alert'):
        assert token in colors
    for foreground in ('text','secondary','muted'):
        for surface in ('background','surface','elevated','card','selected'):
            assert contrast(colors[foreground],colors[surface])>=4.5,(key,foreground,surface)
    assert contrast(colors['on_accent'],colors['accent'])>=4.5
    assert len(set(TYPE.values()))>=4 and len(set(WEIGHT.values()))>=2
    assert tuple(SPACE.values())==(4,8,12,16,24,32)
    assert RADIUS=={'card':12,'button':8}

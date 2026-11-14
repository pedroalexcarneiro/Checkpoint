from pathlib import Path
import pytest
from PySide6.QtCore import QSize
from checkpoint.icons import NAMES,lucide_icon

@pytest.mark.parametrize('size',[10,16,18,20,22,24,32])
def test_lucide_uses_context_size_and_one_stroke(app,size):
    from PySide6.QtGui import QRegion
    for name in NAMES:
        pix=lucide_icon(name,'#44aa77',size).pixmap(size,size)
        assert pix.size()==QSize(size,size)
        bounds=QRegion(pix.mask()).boundingRect()
        assert not bounds.isEmpty() and pix.rect().contains(bounds)
    root=Path('checkpoint/assets/lucide')
    for path in root.glob('*.svg'):
        data=path.read_text(encoding='utf-8');assert 'stroke-width="2"' in data and 'viewBox="0 0 24 24"' in data
    assert 'ISC License' in Path('THIRD_PARTY_NOTICES.md').read_text(encoding='utf-8')

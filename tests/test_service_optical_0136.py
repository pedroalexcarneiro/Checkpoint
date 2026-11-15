from hashlib import sha256
from pathlib import Path
from checkpoint.ui_components import service_icon


def test_steam_white_mark_optically_centered_and_asset_unchanged(app):
    path=Path('checkpoint/assets/services/steam.ico')
    assert sha256(path.read_bytes()).hexdigest()=='9f890a9debcdfccc339149a7943be9aff9e4c9203c2fa37d5671a5b2c88503ad'
    image=service_icon('Steam').toImage()
    points=[(x,y) for y in range(48) for x in range(48) if min(image.pixelColor(x,y).getRgb()[:3])>180]
    assert points
    x=sum(p[0] for p in points)/len(points);y=sum(p[1] for p in points)/len(points)
    assert abs(x-23.5)<.6 and abs(y-23.5)<.6

"""Escalas visuais compartilhadas: medidas em pixels lógicos do Qt."""
SPACE = {'xxs': 4, 'xs': 8, 'sm': 12, 'md': 16, 'lg': 24, 'xl': 32}
TYPE = {'caption': 12, 'small': 13, 'body': 14, 'card': 16, 'section': 20, 'title': 30, 'display': 36}
WEIGHT = {'regular': 400, 'strong': 600}
RADIUS = {'card': 12, 'button': 8}
HEIGHT = {'button': 40, 'compact': 32, 'actions': 64}


def luminance(color):
    channels = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
    return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)

"""Dados substantivos da ficha; nome, plataforma e origem não são enriquecimento."""
from .prices import snapshot


def has_game_data(library,game):
    fields=('description','developer','publisher','genre','category','release_date','cover','banner','logo','notes')
    value=snapshot(library,game['id'])
    return any(str(game.get(key) or '').strip() for key in fields) or any(
        type(value.get(key)) is int and value[key]>0 for key in ('lowest','current','historical'))

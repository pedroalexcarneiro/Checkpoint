"""Dados substantivos da ficha; nome, plataforma e origem não são enriquecimento."""
from .prices import snapshot


def has_game_data(library,game):
    fields=('description','developer','publisher','genre','category','release_date','cover','banner','logo','notes')
    value=snapshot(library,game['id'])
    return any(str(game.get(key) or '').strip() for key in fields) or any(
        type(value.get(key)) is int and value[key]>0 for key in ('lowest','current','historical'))


def display_source(library,game):
    value=(game.get('source') or '').strip()
    if value not in ('','Manual','Não identificada'):
        return value
    identities=dict(library.sql.execute('SELECT provider,external_id FROM external_identifiers WHERE game_id=?',(game['id'],)))
    if 'rawg' in identities:return 'Busca'
    if 'steam' in identities:return 'Steam'
    if 'steamgriddb' in identities:return 'Busca'
    if library.sql.execute('SELECT 1 FROM game_files WHERE game_id=? AND drive_id IS NOT NULL',(game['id'],)).fetchone():return 'Drive'
    return value or 'Não identificada'


def completion_feedback(library,game,message):
    """Zero campos novos não significa falha: pode haver textos e artes anteriores."""
    failure='Não foi possível preencher a ficha automaticamente. Tente novamente.'
    if failure not in message:return message
    if any(game.get(field) for field in ('description','developer','publisher')):
        replacement='Consulta concluída; os textos existentes foram preservados.'
    elif has_game_data(library,game):
        replacement='Consulta sem novos textos; imagens, preço e dados existentes preservados. Tente novamente para completar os textos.'
    else:
        replacement='Ficha não preenchida: a fonte não disponibilizou os campos solicitados. Verifique as conexões e tente novamente.'
    return message.replace(failure,replacement)

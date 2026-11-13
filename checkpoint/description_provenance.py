"""Proveniência de texto; não altera schema e nunca substitui uma edição local."""
import hashlib
import json


def text_hash(value):return hashlib.sha256(value.encode('utf-8')).hexdigest()


def record(library,game_id,result):
    game=library.get(game_id)
    if not game or not result.description or game['description']!=result.description or not result.description_source:return
    value={'sha256':text_hash(result.description),'source':result.description_source,'language':result.description_language}
    # Participa da transação do chamador, sem commit implícito.
    library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
                        (f'description.source.{game_id}',json.dumps(value)))


def current(library,game):
    value=library.setting(f"description.source.{game['id']}",{})
    return value if value.get('sha256')==text_hash(game['description']) else {}

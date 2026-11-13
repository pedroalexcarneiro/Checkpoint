"""Cadastro confirmado + vínculo de ROM em uma única transação."""
from .library import clean_game_data,now
from contextlib import contextmanager

@contextmanager
def atomic(sql):
    sql.execute('SAVEPOINT game_import')
    try:
        yield
        sql.execute('RELEASE SAVEPOINT game_import')
    except Exception:
        sql.execute('ROLLBACK TO SAVEPOINT game_import')
        sql.execute('RELEASE SAVEPOINT game_import')
        raise



def complete_identity(library,game_id,result):
    if not library.get(game_id):raise ValueError('Jogo indisponível.')
    identities={**result.identifiers,result.provider:result.external_id}
    with atomic(library.sql):
        for provider,external_id in identities.items():
            if provider not in {'rawg','steamgriddb','steam'} or not str(external_id).isdigit() or int(external_id)<=0:
                raise ValueError('Identidade de catálogo inválida.')
            row=library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(provider,external_id)).fetchone()
            previous=library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,provider)).fetchone()
            if (row and row[0]!=game_id) or (previous and previous[0]!=external_id):
                raise ValueError('Identidade já associada a outro cadastro. Revise em Editar jogo.')
            library.sql.execute('INSERT OR IGNORE INTO external_identifiers VALUES(?,?,?)',(game_id,provider,external_id))
        values={'description':result.description,'genre':', '.join(result.genres),'developer':result.developer,
                'publisher':result.publisher,'release_date':result.release_date}
        for field,value in values.items():
            if value:library.sql.execute(f"UPDATE games SET {field}=?,updated_at=? WHERE id=? AND {field}='' AND deleted_at IS NULL",(value,now(),game_id))

        from .description_provenance import record
        record(library,game_id,result)


def save_import(library,data,file_id=None,result=None):
    clean=clean_game_data(data)
    if result:
        values={'description':result.description,'developer':result.developer,'publisher':result.publisher,'genre':', '.join(result.genres),'release_date':result.release_date}
        for field,value in values.items():
            if value and not clean.get(field):clean[field]=value
        if clean.get('source') in (None,'','Manual'):clean['source']='Busca'
    file=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone() if file_id is not None else None
    if file_id is not None and file is None: raise ValueError('A ROM selecionada não está mais no índice.')
    existing=None
    identities={}
    if result:
        identities={**result.identifiers,result.provider:result.external_id}
        for provider,external_id in identities.items():
            if provider not in {'rawg','steamgriddb','steam'} or not str(external_id).isdigit() or int(external_id)<=0:raise ValueError('Identidade de catálogo inválida.')
            row=library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(provider,external_id)).fetchone()
            if row:
                if existing and existing!=row[0]:raise ValueError('As identidades do catálogo pertencem a cadastros diferentes.')
                existing=row[0]
    if file and file['game_id']:
        if existing and existing!=file['game_id']: raise ValueError('Esta ROM já está associada a outro jogo. Revise a associação no gerenciador Drive.')
        existing=file['game_id']
    if existing and not library.get(existing): raise ValueError('O jogo correspondente está na lixeira. Restaure-o antes de associar outra versão.')
    with atomic(library.sql):
        if existing:
            game_id=existing
        else:
            if clean.get('status')=='Concluído':clean['completed_at']=now()
            game_id=library.sql.execute(f'INSERT INTO games({",".join(clean)}) VALUES({",".join("?" for _ in clean)})',list(clean.values())).lastrowid
        if result:
            # Se a ROM já tinha jogo, não troca silenciosamente uma identidade previamente confirmada.
            for provider,external_id in identities.items():
                identity=library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,provider)).fetchone()
                if identity and identity[0]!=external_id: raise ValueError('Este cadastro já tem outra identidade confirmada neste catálogo.')
                library.sql.execute('INSERT OR IGNORE INTO external_identifiers VALUES(?,?,?)',(game_id,provider,external_id))
            if existing:
                values={'description':result.description,'genre':', '.join(result.genres),'developer':result.developer,'publisher':result.publisher,'release_date':result.release_date}
                values={key:value for key,value in values.items() if value and not library.get(game_id)[key]}
                if values:library.sql.execute(f'UPDATE games SET {",".join(key+"=?" for key in values)},updated_at=? WHERE id=?',[*values.values(),now(),game_id])
        if result:
            from .description_provenance import record
            record(library,game_id,result)
        if file:
            library.sql.execute("UPDATE game_files SET game_id=?,review_state='confirmed' WHERE id=?",(game_id,file_id))
            library.sql.execute('INSERT OR IGNORE INTO rom_versions(file_id) VALUES(?)',(file_id,))
        library.sql.execute('DELETE FROM wishlist WHERE game_id=?',(game_id,))
        library.sql.execute('DELETE FROM settings WHERE key=?',(f'collection.unowned.{game_id}',))
    return game_id

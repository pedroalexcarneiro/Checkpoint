"""Cadastro confirmado + vínculo de ROM em uma única transação."""
from .library import clean_game_data,now


def save_import(library,data,file_id=None,result=None):
    clean=clean_game_data(data)
    file=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone() if file_id is not None else None
    if file_id is not None and file is None: raise ValueError('A ROM selecionada não está mais no índice.')
    existing=None
    if result:
        if result.provider not in {'rawg','steamgriddb'} or not str(result.external_id).isdigit(): raise ValueError('Identidade de catálogo inválida.')
        row=library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(result.provider,result.external_id)).fetchone()
        existing=row[0] if row else None
    if file and file['game_id']:
        if existing and existing!=file['game_id']: raise ValueError('Esta ROM já está associada a outro jogo. Revise a associação no gerenciador Drive.')
        existing=file['game_id']
    if existing and not library.get(existing): raise ValueError('O jogo correspondente está na lixeira. Restaure-o antes de associar outra versão.')
    with library.sql:
        if existing:
            game_id=existing
        else:
            if clean.get('status')=='Concluído':clean['completed_at']=now()
            game_id=library.sql.execute(f'INSERT INTO games({",".join(clean)}) VALUES({",".join("?" for _ in clean)})',list(clean.values())).lastrowid
        if result:
            # Se a ROM já tinha jogo, não troca silenciosamente uma identidade previamente confirmada.
            identity=library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,result.provider)).fetchone()
            if identity and identity[0]!=result.external_id: raise ValueError('Este cadastro já tem outra identidade confirmada neste catálogo.')
            library.sql.execute('INSERT OR IGNORE INTO external_identifiers VALUES(?,?,?)',(game_id,result.provider,result.external_id))
            if existing:
                values={'title':clean['title'],'description':result.description,'genre':', '.join(result.genres),'developer':result.developer,'publisher':result.publisher,'release_date':result.release_date}
                values={key:value for key,value in values.items() if value}
                library.sql.execute(f'UPDATE games SET {",".join(key+"=?" for key in values)},updated_at=? WHERE id=?',[*values.values(),now(),game_id])
        if file:
            library.sql.execute("UPDATE game_files SET game_id=?,review_state='confirmed' WHERE id=?",(game_id,file_id))
            library.sql.execute('INSERT OR IGNORE INTO rom_versions(file_id) VALUES(?)',(file_id,))
    return game_id

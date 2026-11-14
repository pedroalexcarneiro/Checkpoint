"""Decisão explícita ao adicionar novamente um cadastro removido."""
import json
import unicodedata


def title_key(value):
    return unicodedata.normalize('NFKC',value or '').strip().casefold()


def removed_match(library,data,file_id=None,result=None):
    ids=set()
    if result:
        for provider,identity in {**result.identifiers,result.provider:result.external_id}.items():
            row=library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(provider,identity)).fetchone()
            if row:ids.add(row[0])
    if file_id is not None:
        row=library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file_id,)).fetchone()
        if row and row[0]:ids.add(row[0])
    if ids:
        if len(ids)>1:return None  # O serviço mantém a rejeição de identidades conflitantes.
        row=library.sql.execute('SELECT * FROM games WHERE id=? AND deleted_at IS NOT NULL',(next(iter(ids)),)).fetchone()
        return dict(row) if row else None
    matches=[dict(row) for row in library.sql.execute('SELECT * FROM games WHERE deleted_at IS NOT NULL')
             if not (result and library.setting(f"trash.identities.{row['id']}") is not None)
             and title_key(row['title'])==title_key(data.get('title')) and title_key(row['platform'])==title_key(data.get('platform'))]
    return matches[0] if len(matches)==1 else None


def detach_removed(library,game_id):
    """Arquiva apenas vínculos públicos; notas, artes e histórico ficam intactos."""
    row=library.sql.execute('SELECT deleted_at FROM games WHERE id=?',(game_id,)).fetchone()
    if not row or not row[0]:raise ValueError('O cadastro anterior não está na lixeira.')
    identities=[list(row) for row in library.sql.execute('SELECT provider,external_id FROM external_identifiers WHERE game_id=?',(game_id,))]
    key=f'trash.identities.{game_id}'
    previous=library.setting(key,[])
    identities=previous+[row for row in identities if row not in previous]
    library.sql.execute('INSERT OR REPLACE INTO settings VALUES(?,?)',(key,json.dumps(identities)))
    library.sql.execute('DELETE FROM external_identifiers WHERE game_id=?',(game_id,))


def save_decision(library,data,file_id=None,result=None,*,removed_id=None,decision='cancel'):
    from .game_import import save_import,atomic
    if removed_id is None:return save_import(library,data,file_id,result)
    if decision=='cancel':return None
    if decision not in {'restore','new'}:raise ValueError('Decisão inválida.')
    with atomic(library.sql):
        if decision=='restore':
            library.sql.execute('UPDATE games SET deleted_at=NULL WHERE id=?',(removed_id,))
            if result:
                from .game_import import complete_identity
                complete_identity(library,removed_id,result)
            if file_id is not None:
                row=library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(file_id,)).fetchone()
                if not row:raise ValueError('A ROM selecionada não está mais no índice.')
                if row[0] and row[0]!=removed_id:raise ValueError('A ROM pertence a outro cadastro.')
                library.sql.execute("UPDATE game_files SET game_id=?,review_state='confirmed' WHERE id=?",(removed_id,file_id))
                library.sql.execute('INSERT OR IGNORE INTO rom_versions(file_id) VALUES(?)',(file_id,))
            return removed_id
        detach_removed(library,removed_id)
        if file_id is not None:
            library.sql.execute('UPDATE game_files SET game_id=NULL WHERE id=? AND game_id=?',(file_id,removed_id))
        return save_import(library,data,file_id,result)


def ask_removed(parent,title):
    from PySide6.QtWidgets import QMessageBox
    box=QMessageBox(parent);box.setWindowTitle('Jogo na lixeira');box.setText(f'“{title}” já esteve na sua biblioteca.')
    box.setInformativeText('Restaurar recupera suas notas, imagens e histórico. Adicionar como novo mantém o cadastro anterior na lixeira.')
    restore=box.addButton('Restaurar jogo',QMessageBox.AcceptRole)
    fresh=box.addButton('Adicionar como novo',QMessageBox.ActionRole)
    box.addButton('Cancelar',QMessageBox.RejectRole);box.setDefaultButton(restore);box.exec()
    return 'restore' if box.clickedButton()==restore else 'new' if box.clickedButton()==fresh else 'cancel'


def save_with_prompt(parent,library,data,file_id=None,result=None):
    removed=removed_match(library,data,file_id,result)
    decision=ask_removed(parent,removed['title']) if removed else 'cancel'
    from .game_import import atomic
    with atomic(library.sql):
        game_id=save_decision(library,data,file_id,result,removed_id=removed['id'] if removed else None,decision=decision)
        if game_id is not None and file_id is not None:
            from .rom_link import bind
            bind(library,file_id,game_id)
        return game_id

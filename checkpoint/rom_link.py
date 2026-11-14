"""Busca exata e vínculo único de ROM; download e ficha são etapas independentes."""
import hashlib
import re
from pathlib import Path
from .automatic_catalog import normalized
from .integrations.drive import normalize_rom_name,PLATFORMS,DriveScanner
from .integrations import MetadataResult,IntegrationError


def candidates(library,title,platform=''):
    query=normalized(title)
    if not query:return []
    canonical=lambda value:PLATFORMS.get(value.casefold(),value).casefold()
    rows=[]
    for row in library.sql.execute('SELECT * FROM game_files WHERE drive_id IS NOT NULL'):
        row=dict(row);name=normalized(normalize_rom_name(row['original_name']))
        if row['review_state'] in ('remote_missing','remote_removed','outside_root'):continue
        if platform and canonical(platform)!=canonical(row['platform'] or ''):continue
        if query!=name and query not in name:continue
        revision=re.search(r'\((?:Rev(?:ision)?)[ ._-]*(\d+)\)',row['original_name'],re.I)
        region=0 if re.search(r'\(USA(?:,|\))',row['original_name'],re.I) else 1 if '(Europe)' in row['original_name'] else 2
        rows.append(((name!=query,region,-int(revision[1]) if revision else 0,row['original_name'],row['id']),row))
    return [row for _,row in sorted(rows,key=lambda pair:pair[0])[:3]]


def bind(library,file_id,game_id):
    from .game_import import atomic
    row=library.sql.execute('SELECT * FROM game_files WHERE id=? AND drive_id IS NOT NULL',(file_id,)).fetchone()
    if not library.get(game_id) or not row:raise ValueError('Jogo ou ROM indisponível.')
    if row['game_id'] not in (None,game_id):raise ValueError('Esta ROM já pertence a outro jogo. Nenhum vínculo foi alterado.')
    with atomic(library.sql):
        # Desvincula; não apaga índice remoto, arquivos locais ou versões históricas.
        library.sql.execute('UPDATE game_files SET game_id=NULL WHERE game_id=? AND id<>?',(game_id,file_id))
        changed=library.sql.execute("UPDATE game_files SET game_id=?,review_state='confirmed' WHERE id=? AND (game_id IS NULL OR game_id=?)",(game_id,file_id,game_id))
        if changed.rowcount!=1:raise ValueError('O vínculo mudou durante a operação. Nenhum arquivo foi substituído.')
        library.sql.execute('INSERT OR IGNORE INTO rom_versions(file_id) VALUES(?)',(file_id,))


def verify(file):
    path=Path(file['local_path'] or '')
    if not file['available'] or not path.is_file():return False
    if file['size'] is not None and path.stat().st_size!=file['size']:return False
    if file['md5']:
        digest=hashlib.md5(usedforsecurity=False)
        with path.open('rb') as stream:
            for block in iter(lambda:stream.read(1024*1024),b''):digest.update(block)
        if digest.hexdigest()!=file['md5']:return False
    return True


def complete_link(library,file_id,game_id=None,*,client=None,sources=None,art_provider=None,cache=None):
    from .game_import import save_import,complete_identity,atomic
    from .unified_catalog import search_titles,selected_details
    from .auto_artwork import AutoArtwork
    from .credentials import CredentialVault
    from .integrations.drive import GoogleDriveClient
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
    if not row:raise ValueError('A ROM selecionada não está mais no índice.')
    with atomic(library.sql):
        if game_id is None:
            game_id=save_import(library,{'title':normalize_rom_name(row['original_name']),'platform':row['platform'] or '','source':'Drive'},file_id)
        bind(library,file_id,game_id)
    game=library.get(game_id);errors=[]
    if not verify(dict(row)):
        try:
            directory=library.setting('downloads') or str(library.db.path.parent/'ROMs')
            library.set_setting('downloads',directory)
            DriveScanner(library,client or GoogleDriveClient.authenticate(None,CredentialVault())).download(file_id,directory)
        except (IntegrationError,ValueError,OSError):
            errors.append('Download não concluído: verifique a autenticação, a conexão e a integridade da ROM.')
    try:
        payload=search_titles(game['title'],game['platform'],sources)
        exact=[MetadataResult(**item) for item in payload['results'] if normalized(item['title'])==normalized(game['title'])]
        # Sem escolha extra, só uma identidade inequívoca pode ser aplicada.
        if len(exact)!=1:
            reason='catálogos indisponíveis' if not exact and payload.get('unavailable') else 'nenhum resultado exato' if not exact else 'mais de uma identidade exata'
            errors.append('Ficha não preenchida: '+reason+'. Pesquise manualmente ou tente novamente.')
        else:
            match=exact[0]
            if match.provider=='steamgriddb' and 'rawg' in match.identifiers:
                match=MetadataResult('rawg',match.identifiers['rawg'],match.title)
            result=selected_details(match.provider,match.external_id,game['platform'],sources)
            if normalized(result.title)!=normalized(game['title']):raise ValueError('Identidade divergente.')
            complete_identity(library,game_id,result)
            if any((result.description,result.developer,result.publisher)):
                with library.sql:library.sql.execute("UPDATE games SET source='Busca' WHERE id=? AND source IN ('Drive','Google Drive','Não identificada','Manual','')",(game_id,))
            if not any((result.description,result.developer,result.publisher)):
                errors.append('Ficha não preenchida: o catálogo retornou somente a identidade, sem texto.')
            message=AutoArtwork(library,provider=art_provider,cache=cache).obtain(game_id,force=True)
            if not all(library.get(game_id)[kind] for kind in ('cover','banner','logo')):errors.append('Imagens pendentes: '+message)
    except (IntegrationError,ValueError,OSError):
        errors.append('Ficha não preenchida: falha na consulta ao catálogo. Verifique as conexões e tente novamente.')
    result={'game_id':game_id,'file_id':file_id,'errors':errors,
            'message':' '.join(errors) if errors else 'ROM vinculada, baixada e verificada. Ficha e imagens preenchidas.'}
    library.set_setting(f'rom.link.{game_id}',result)
    return result

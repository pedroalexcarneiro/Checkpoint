"""Busca exata e vínculo único de ROM; download e ficha são etapas independentes."""
import hashlib
import re
import sqlite3
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


def verify(file,*,cancel=None,progress=None):
    from .transfer_progress import check_cancel
    check_cancel(cancel)
    path=Path(file['local_path'] or '')
    if not file['available'] or not path.is_file():return False
    size=path.stat().st_size
    if file['size'] is not None and size!=file['size']:return False
    if file['md5']:
        digest=hashlib.md5(usedforsecurity=False)
        received=0
        with path.open('rb') as stream:
            for block in iter(lambda:stream.read(1024*1024),b''):
                check_cancel(cancel);digest.update(block);received+=len(block)
                if progress:progress({'stage':'verifying','verified_bytes':received,'total':size})
        if digest.hexdigest()!=file['md5']:return False
    return True


def complete_link(library,file_id,game_id=None,*,client=None,sources=None,art_provider=None,cache=None,
                  progress_path=None,cancel_path=None,owner=None):
    from .game_import import save_import,complete_identity,atomic
    from .unified_catalog import search_titles,selected_details
    from .auto_artwork import AutoArtwork
    from .credentials import CredentialVault
    from .integrations.drive import GoogleDriveClient
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
    if not row:raise ValueError('A ROM selecionada não está mais no índice.')
    from .transfer_progress import TransferProgress,TransferCancelled
    context=TransferProgress(progress_path,cancel_path,owner)
    managed=bool(progress_path or cancel_path or owner)
    download_state='downloaded';link_state='linked';metadata_state='completed'
    if game_id is not None:
        from .local_rom import identity_problem
        game=library.get(game_id)
        if not game:raise ValueError('Jogo indisponível.')
        problem=identity_problem(game,dict(row))
        if problem:raise ValueError(problem)
        if managed and row['game_id'] not in (None,game_id):raise ValueError('Esta ROM já pertence a outro jogo. Nenhum vínculo foi alterado.')
    if not managed:
        with atomic(library.sql):
            if game_id is None:
                game_id=save_import(library,{'title':normalize_rom_name(row['original_name']),'platform':row['platform'] or '','source':'Drive'},file_id)
            bind(library,file_id,game_id)
    elif game_id is None:
        raise ValueError('Escolha a ficha do jogo para vincular. Download avulso não cadastra jogos.')
    game=library.get(game_id);errors=[]
    if managed:
        from .transfer_download import download_file
        try:
            path=download_file(library,file_id,context,client=client)
            context.check()
            context.report({'stage':'linking','game_id':game_id,'file_id':file_id})
            bind(library,file_id,game_id)
            context.report({'stage':'linked','download_state':'downloaded','link_state':'linked'})
        except (TransferCancelled,IntegrationError,ValueError,OSError,sqlite3.Error) as error:
            actual=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
            downloaded=bool(actual and actual['available'] and actual['local_path']==context.snapshot.get('local_path')
                            and context.snapshot.get('stage') in ('downloaded','linking','linked','metadata'))
            cancelled=isinstance(error,TransferCancelled)
            download_state='downloaded' if downloaded else 'cancelled' if cancelled else 'failed'
            message=str(error) if isinstance(error,(IntegrationError,ValueError)) else 'Download não concluído. Verifique conexão, acesso ao Drive e destino.'
            result={'game_id':game_id,'file_id':file_id,'errors':[] if cancelled else [message],
                    'download_state':download_state,'link_state':'not_completed','metadata_state':'not_started',
                    'cancelled':cancelled,'local_path':actual['local_path'] if downloaded else None,'message':message}
            result['transfer_state']=context.snapshot.get('transfer_state','cancelled' if cancelled else 'failed')
            if result['transfer_state'] in ('running','not_started'):result['transfer_state']='cancelled' if cancelled else 'failed'
            result['verification_state']=context.snapshot.get('verification_state','not_started')
            if result['verification_state']=='running':result['verification_state']='cancelled' if cancelled else 'failed'
            library.set_setting(f'rom.link.{game_id}',result)
            context.report({'stage':'cancelled' if cancelled else 'failed',**result})
            return result
    elif not verify(dict(row)):
        try:
            directory=library.setting('downloads') or str(library.db.path.parent/'ROMs')
            library.set_setting('downloads',directory)
            DriveScanner(library,client or GoogleDriveClient.authenticate(None,CredentialVault())).download(file_id,directory)
        except (IntegrationError,ValueError,OSError):
            errors.append('Download não concluído: verifique a autenticação, a conexão e a integridade da ROM.')
            download_state='failed'
    try:
        if managed:context.check();context.report({'stage':'metadata','download_state':download_state,'link_state':link_state})
        payload=search_titles(game['title'],game['platform'],sources)
        if managed:context.check()
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
            if managed:context.check()
            if normalized(result.title)!=normalized(game['title']):raise ValueError('Identidade divergente.')
            from .local_rom import canonical_platform
            if game['platform'] and result.platforms and not any(canonical_platform(p).casefold()==canonical_platform(game['platform']).casefold() for p in result.platforms):raise ValueError('Plataforma de catálogo divergente.')
            complete_identity(library,game_id,result)
            if any((result.description,result.developer,result.publisher)):
                with library.sql:library.sql.execute("UPDATE games SET source='Busca' WHERE id=? AND source IN ('Drive','Google Drive','Não identificada','Manual','')",(game_id,))
            if not any((result.description,result.developer,result.publisher)):
                errors.append('Ficha não preenchida: o catálogo retornou somente a identidade, sem texto.')
            message=AutoArtwork(library,provider=art_provider,cache=cache).obtain(game_id,force=True)
            if managed:context.check()
            if not all(library.get(game_id)[kind] for kind in ('cover','banner','logo')):errors.append('Imagens pendentes: '+message)
    except TransferCancelled:
        metadata_state='cancelled';errors.append('Consulta de metadados cancelada. A ROM baixada e vinculada foi preservada.')
    except (IntegrationError,ValueError,OSError):
        errors.append('Ficha não preenchida: falha na consulta ao catálogo. Verifique as conexões e tente novamente.')
    if errors and metadata_state=='completed':metadata_state='pending'
    result={'game_id':game_id,'file_id':file_id,'errors':errors,
            'download_state':download_state,'link_state':link_state,'metadata_state':metadata_state,
            'message':' '.join(errors) if errors else 'ROM vinculada, baixada e verificada. Ficha e imagens preenchidas.'}
    if managed:
        result['local_path']=str(path)
        result['transfer_state']=context.snapshot.get('transfer_state','completed')
        result['verification_state']='completed'
    library.set_setting(f'rom.link.{game_id}',result)
    if managed:context.report({'stage':'completed' if not errors else 'metadata_pending',**result})
    return result

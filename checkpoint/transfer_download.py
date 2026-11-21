"""Transferir/verificar um arquivo sem cadastrar jogo ou buscar metadados."""
from pathlib import Path
import sqlite3
from .transfer_progress import TransferProgress,TransferCancelled
from .integrations import IntegrationError


def download_file(library,file_id,context,*,client=None,directory=None):
    from .rom_link import verify
    from .integrations.drive import DriveScanner,GoogleDriveClient
    from .credentials import CredentialVault
    row=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
    if not row or not row['drive_id']:raise ValueError('Arquivo do Drive indisponível.')
    context.check()
    context.report({'stage':'checking_existing','file_id':file_id,'file_name':row['original_name'],
                    'received':0,'total':row['size'],'transfer_state':'not_started','verification_state':'running'})
    def checking(values):context.report({**values,'stage':'checking_existing'})
    if verify(dict(row),cancel=context.cancelled,progress=checking):
        path=Path(row['local_path'])
        context.report({'stage':'downloaded','received':path.stat().st_size,'local_path':str(path),
                        'transfer_state':'not_required','verification_state':'completed','registration_state':'completed'})
        return path
    destination=directory or library.setting('downloads') or str(library.db.path.parent/'ROMs')
    if not library.setting('downloads'):library.set_setting('downloads',str(destination))
    context.report({'stage':'authorizing','verification_state':'not_started','transfer_state':'not_started'})
    context.check()
    client=client or GoogleDriveClient.authenticate(None,CredentialVault())
    context.check()
    return DriveScanner(library,client).download(file_id,destination,progress=context.report,cancel=context.cancelled)


def download_only(library,file_id,*,directory=None,progress_path=None,cancel_path=None,owner=None,client=None):
    context=TransferProgress(progress_path,cancel_path,owner)
    try:
        path=download_file(library,file_id,context,client=client,directory=directory)
        context.report({'stage':'completed','download_state':'downloaded','local_path':str(path)})
        return {'file_id':file_id,'game_id':None,'errors':[],'download_state':'downloaded',
                'link_state':'not_requested','metadata_state':'not_requested','local_path':str(path),
                'transfer_state':context.snapshot.get('transfer_state','completed'),'verification_state':'completed','registration_state':'completed',
                'message':'Download concluído e arquivo verificado.'}
    except TransferCancelled:
        partial=context.snapshot.get('partial_path')
        message='Download cancelado.'+(' Parcial preservado.' if partial and Path(partial).is_file() else '')
        transfer=context.snapshot.get('transfer_state','cancelled')
        if transfer in ('running','not_started'):transfer='cancelled'
        verification=context.snapshot.get('verification_state','not_started')
        if verification=='running':verification='cancelled'
        context.report({'stage':'cancelled','download_state':'cancelled','message':message,'transfer_state':transfer,'verification_state':verification})
        return {'file_id':file_id,'game_id':None,'errors':[],'download_state':'cancelled',
                'link_state':'not_requested','metadata_state':'not_requested','cancelled':True,'message':message,
                'transfer_state':transfer,'verification_state':verification}
    except (IntegrationError,ValueError,OSError,sqlite3.Error) as error:
        stage=context.snapshot.get('stage')
        message=(str(error) if isinstance(error,(IntegrationError,ValueError)) else
                 'Arquivo verificado; confirmação no banco pendente. Tente novamente para conferir o arquivo já baixado.'
                 if stage=='registering' else 'Não foi possível gravar ou verificar o arquivo. Confira espaço e permissões do destino; parcial preservado, se existente.')
        transfer=context.snapshot.get('transfer_state','failed')
        if transfer in ('running','not_started'):transfer='failed'
        verification=context.snapshot.get('verification_state','not_started')
        if verification=='running':verification='failed'
        context.report({'stage':'failed','download_state':'failed','message':message,'transfer_state':transfer,'verification_state':verification})
        return {'file_id':file_id,'game_id':None,'errors':[message],'download_state':'failed',
                'link_state':'not_requested','metadata_state':'not_requested','message':message,
                'transfer_state':transfer,'verification_state':verification,'registration_state':'failed' if stage=='registering' else 'not_started'}

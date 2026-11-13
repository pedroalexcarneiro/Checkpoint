"""Operações nativas isoladas: uma falha no auxiliar não encerra a interface."""
import faulthandler
import json
import logging
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from .integrations import IntegrationError


def run_isolated(operation, database, *, command_factory=None, **arguments):
    database = Path(database).resolve()
    jobs = database.parent / 'jobs'
    jobs.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='task-', dir=jobs) as temporary:
        root = Path(temporary)
        request = root / 'request.json'
        response = root / 'response.json'
        request.write_text(json.dumps({'operation': operation, 'database': str(database),
                                      'response': str(response), 'arguments': arguments}), encoding='utf-8')
        if command_factory:
            command = command_factory(request)
        elif getattr(sys, 'frozen', False):
            command = [sys.executable, '--worker-request', str(request)]
        else:
            command = [sys.executable, '-m', 'checkpoint.app', '--worker-request', str(request)]
        try:
            result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL,
                                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        except OSError:
            raise IntegrationError('Não foi possível iniciar a operação auxiliar. Cadastro e arquivos preservados.') from None
        if result.returncode != 0 or not response.is_file():
            logging.getLogger(__name__).warning('Auxiliary operation=%s exit=%s', operation, result.returncode)
            raise IntegrationError('A operação auxiliar foi interrompida. O Checkpoint continua aberto; '
                                   'cadastro, downloads concluídos e arquivos parciais foram preservados.')
        payload = json.loads(response.read_text(encoding='utf-8'))
        if not payload.get('ok'):
            raise IntegrationError(payload.get('message', 'Operação não concluída. Dados preservados.'))
        return payload['result']


def execute_request(request):
    payload = json.loads(Path(request).read_text(encoding='utf-8'))
    database = Path(payload['database'])
    # Sem valores de credenciais, URLs de OAuth ou mensagens brutas de exceção.
    logging.getLogger('google_auth_oauthlib.flow').setLevel(logging.WARNING)
    from PySide6.QtCore import QCoreApplication
    app = QCoreApplication.instance() or QCoreApplication([])
    with (database.parent / 'native-crash.log').open('a', encoding='utf-8') as diagnostic:
        faulthandler.enable(file=diagnostic, all_threads=True)
        try:
            operation = payload['operation']
            arguments = payload['arguments']
            from .database import Database
            from .library import Library
            db = Database(database)
            try:
                lib = Library(db)
                if operation == 'download':
                    from .credentials import CredentialVault
                    from .integrations.drive import GoogleDriveClient, DriveScanner
                    client = GoogleDriveClient.authenticate(None, CredentialVault())
                    DriveScanner(lib, client).download(arguments['file_id'], arguments['directory'])
                    row = lib.sql.execute('SELECT * FROM game_files WHERE id=?', (arguments['file_id'],)).fetchone()
                    game_id = row['game_id']
                    if not game_id:
                        from .integrations.drive import normalize_rom_name
                        from .game_import import save_import
                        game_id = save_import(lib, {'title': normalize_rom_name(row['original_name']),
                            'platform': row['platform'] or '', 'source': 'Google Drive'}, row['id'])
                    result = {'message': 'ROM baixada, verificada e adicionada à biblioteca.', 'game_id': game_id}
                elif operation == 'enrich':
                    from .auto_artwork import obtain_artwork
                    game_id = arguments['game_id']
                    restore_candidate = None
                    if (arguments.get('force', False) or lib.setting('artwork.auto', True)) and not lib.sql.execute('SELECT 1 FROM external_identifiers WHERE game_id=?', (game_id,)).fetchone():
                        from .automatic_catalog import resolve_title
                        from .game_import import complete_identity
                        game = lib.get(game_id)
                        match = resolve_title(game['title'], game['platform']) if game else None
                        if match:
                            from .trash_import import removed_match
                            restore_candidate = removed_match(lib, game, result=match)
                            if not restore_candidate:complete_identity(lib, game_id, match)
                    identities=dict(lib.sql.execute('SELECT provider,external_id FROM external_identifiers WHERE game_id=?',(game_id,)))
                    game=lib.get(game_id)
                    needs_pair=('rawg' in identities and 'steamgriddb' not in identities) or ('steamgriddb' in identities and not {'rawg','steam'} & identities.keys())
                    if game and not restore_candidate and needs_pair and any(not game[kind] for kind in ('description','cover','banner','logo')) and (arguments.get('force',False) or lib.setting('artwork.auto',True)):
                        from .unified_catalog import selected_details
                        from .game_import import complete_identity
                        from .trash_import import removed_match
                        source='rawg' if 'rawg' in identities else 'steamgriddb'
                        try:
                            match=selected_details(source,identities[source],game['platform'])
                            restore_candidate=removed_match(lib,game,result=match)
                            if not restore_candidate:complete_identity(lib,game_id,match)
                        except (IntegrationError,ValueError):pass
                    result = {'state':'restore_required','removed_id':restore_candidate['id']} if restore_candidate else obtain_artwork(lib, arguments['game_id'], force=arguments.get('force', False))
                elif operation == 'catalog_search':
                    from .unified_catalog import search_titles
                    result = search_titles(arguments['title'],arguments.get('platform',''))
                elif operation == 'catalog_details':
                    from .unified_catalog import preview_details
                    result = preview_details(database,arguments['provider'],arguments['identity'],arguments.get('platform',''))
                elif operation == 'prices':
                    from .prices import refresh_prices
                    result=refresh_prices(lib,arguments['game_id'])
                elif operation == 'resolve':
                    from dataclasses import asdict
                    from .automatic_catalog import resolve_title
                    match = resolve_title(arguments['title'], arguments.get('platform', ''))
                    result = asdict(match) if match else None
                elif operation == 'ping':
                    result = {'worker': 'ok', 'schema': lib.sql.execute('PRAGMA user_version').fetchone()[0]}
                else:
                    raise ValueError('Operação auxiliar desconhecida.')
                reply = {'ok': True, 'result': result}
            finally:
                db.close()
        except (IntegrationError, ValueError) as error:
            reply = {'ok': False, 'message': str(error)}
        except Exception as error:
            logging.getLogger(__name__).warning('Auxiliary error_type=%s', type(error).__name__)
            reply = {'ok': False, 'message': 'Operação não concluída. Verifique conexão e permissões. Dados preservados.'}
        finally:
            faulthandler.disable()
    Path(payload['response']).write_text(json.dumps(reply), encoding='utf-8')
    return 0

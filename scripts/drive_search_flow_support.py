"""Percurso Drive por cliques; somente índice e fornecedores são controlados."""
from contextlib import ExitStack
from dataclasses import replace
import json
from pathlib import Path
import sys
import time
from unittest.mock import patch

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QColor
from PySide6.QtTest import QTest

from checkpoint.integrations import IntegrationError, MetadataResult
from scripts.search_flow_support import source_assets

EMERALD = dict(provider='rawg', identity='11', title='Pokemon Emerald Version',
               query='Pokemon', platform='Game Boy Advance', developer='Game Freak',
               publisher='Nintendo', release_date='2004-09-16',
               description='Dados controlados: explore Hoenn e complete a Pokédex.')
ROM_NAME = 'Pokemon Emerald [USA] # GBA.zip'


def drive_worker(request, root):
    root = Path(root)
    profile = json.loads((root / 'source.json').read_text())
    operation = json.loads(Path(request).read_text())['operation']

    class Catalog:
        def __init__(self, provider): self.provider = provider
        def search(self, title):
            if operation == 'catalog_search':
                with (root / ('queries-' + self.provider + '.jsonl')).open('a') as output:
                    output.write(json.dumps({'title': title}) + '\n')
                (root / 'search.started').touch()
                deadline = time.monotonic() + 15
                while not (root / 'search.release').exists():
                    if time.monotonic() > deadline: raise IntegrationError('Prazo da fonte controlada.')
                    time.sleep(.01)
            if profile.get('search_failure'): raise IntegrationError('Catálogo indisponível (teste).')
            if profile.get('no_results'): return []
            return [MetadataResult(self.provider, profile['identity'], profile['title'],
                                   platforms=(profile['platform'],))]
        def details(self, identity):
            if operation == 'enrich': raise IntegrationError('Texto indisponível após seleção (teste).')
            result = self.search('')[0]
            if self.provider == 'steamgriddb': return result
            (root / 'details.started').touch()
            deadline = time.monotonic() + 15
            while not (root / 'details.release').exists():
                if time.monotonic() > deadline: raise IntegrationError('Prazo dos detalhes controlados.')
                time.sleep(.01)
            return replace(result, developer=profile['developer'], publisher=profile['publisher'],
                           description=profile['description'], release_date=profile['release_date'])
        def artworks(self, identity, kind):
            return ['https://cdn.steamgriddb.com/' + kind + '.png']

    import checkpoint.unified_catalog as catalog
    import checkpoint.enrichment as enrichment
    import checkpoint.auto_artwork as artwork
    from checkpoint.credentials import CredentialVault
    from checkpoint.integrations.images import ImageCache
    from checkpoint.integrations import metadata, descriptions
    from checkpoint.worker import execute_request
    primary, art_source = Catalog('rawg'), Catalog('steamgriddb')
    real_artwork = artwork.AutoArtwork
    class ControlledArtwork(real_artwork):
        def __init__(self, library, **kwargs): super().__init__(library, provider=art_source, **kwargs)
    def download(cache, url): return cache.store((root / Path(url).name).read_bytes())
    with ExitStack() as stack:
        stack.enter_context(patch.object(CredentialVault, 'get', return_value=None))
        stack.enter_context(patch.object(catalog, 'providers', return_value={'rawg': primary, 'steamgriddb': art_source}))
        stack.enter_context(patch.object(metadata, 'RawgProvider', return_value=primary))
        stack.enter_context(patch.object(enrichment, 'SteamStoreProvider', return_value=primary))
        stack.enter_context(patch.object(artwork, 'AutoArtwork', ControlledArtwork))
        stack.enter_context(patch.object(ImageCache, 'download', download))
        stack.enter_context(patch.object(descriptions.PortugueseDescriptions, 'find', return_value=None))
        return execute_request(request)


def save_via_drive(app, library, root, *, save_during_search=False, no_results=False, search_failure=False):
    from checkpoint.window import MainWindow
    from checkpoint.jobs import Job
    from checkpoint.worker import run_isolated
    from checkpoint.credentials import CredentialVault
    from checkpoint.integrations.drive import DriveScanner
    import checkpoint.quick_add as quick_module
    import checkpoint.completion_queue as queue_module
    root = Path(root)
    profile = {**EMERALD, 'no_results': no_results, 'search_failure': search_failure}
    if save_during_search: profile['title'] = 'Pokemon Emerald'
    source_assets(root, profile)
    logo = QImage(360, 160, QImage.Format_RGB32); logo.fill(QColor('#58ad64'))
    assert logo.save(str(root / 'logo.png'))
    # Apenas metadados do índice de ROMs, sem jogo cadastrado nem arquivo baixado.
    DriveScanner(library, None).record({'id': 'controlled-emerald', 'name': ROM_NAME}, '/Roms/GBA')
    library.sql.commit()
    file_id = library.sql.execute('SELECT id FROM game_files').fetchone()[0]
    library.set_setting('prices.auto', False)
    support = str(Path(__file__).resolve())
    def isolated(operation, database, **arguments):
        bootstrap = "import runpy,sys; m=runpy.run_path(sys.argv[1]); sys.exit(m['drive_worker'](sys.argv[2],sys.argv[3]))"
        return run_isolated(operation, database, command_factory=lambda request: [
            sys.executable, '-X', 'faulthandler', '-c', bootstrap, support, str(request), str(root)], **arguments)
    with ExitStack() as stack:
        stack.enter_context(patch.object(CredentialVault, 'get', return_value=None))
        stack.enter_context(patch.object(quick_module, 'run_isolated', isolated))
        stack.enter_context(patch.object(queue_module, 'run_isolated', isolated))
        window = MainWindow(library); window.show(); app.processEvents()
        state = {'stage': 'open', 'dialog': None, 'error': None}
        timer = QTimer(); timer.setInterval(10); deadline = time.monotonic() + 30
        def tick():
            try:
                assert time.monotonic() < deadline, 'O fluxo Drive por cliques não terminou.'
                dialog = app.activeModalWidget()
                if state['stage'] == 'open' and dialog and hasattr(dialog, 'quick_add'):
                    state['dialog'] = dialog
                    quick = dialog.quick_add
                    QTest.mouseClick(quick.sources, Qt.LeftButton, pos=quick.sources.tabRect(1).center())
                    QTest.keyClicks(quick.query, 'Pokemon')
                    state['stage'] = 'rom'
                elif state['stage'] == 'rom' and dialog.quick_add.results.count():
                    results = dialog.quick_add.results
                    QTest.mouseClick(results.viewport(), Qt.LeftButton, pos=results.visualItemRect(results.item(0)).center())
                    state['stage'] = 'search'
                elif state['stage'] == 'search' and (root / 'search.started').exists():
                    QTimer.singleShot(100, lambda: (root / 'search.release').touch())
                    state['stage'] = 'save' if save_during_search else 'catalog'
                elif state['stage'] == 'catalog':
                    quick = dialog.quick_add
                    if no_results or search_failure:
                        if not quick.jobs: state['stage'] = 'save'
                    elif quick.results.isVisible():
                        for index in range(quick.results.count()):
                            item = quick.results.item(index)
                            if item.text().split('\n')[0] == profile['title']:
                                QTest.mouseClick(quick.results.viewport(), Qt.LeftButton, pos=quick.results.visualItemRect(item).center())
                                state['stage'] = 'details'; break
                elif state['stage'] == 'details' and (root / 'details.started').exists():
                    (root / 'details.release').touch(); state['stage'] = 'save'
                elif state['stage'] == 'save':
                    if (root / 'details.started').exists(): (root / 'details.release').touch()
                    if dialog.quick_add.save.isEnabled():
                        state['stage'] = 'saved'; timer.stop()
                        QTest.mouseClick(dialog.quick_add.save, Qt.LeftButton)
            except BaseException as error:
                state['error'] = error; timer.stop()
                (root / 'search.release').touch(); (root / 'details.release').touch()
                if state['dialog']: state['dialog'].reject()
        timer.timeout.connect(tick); timer.start()
        QTest.mouseClick(window.add_button, Qt.LeftButton); timer.stop()
        deadline = time.monotonic() + 25
        while (any(job.isRunning() for job in window.findChildren(Job)) or window.completion_queue.active or
               window.completion_queue.pending or (state['dialog'] and state['dialog'].quick_add.jobs)):
            assert time.monotonic() < deadline, 'Trabalho pendente após cadastro pelo Drive.'
            app.processEvents(); QTest.qWait(10)
        if state['error']:
            window.close(); raise state['error']
        rows = library.games(); assert len(rows) == 1
        game = library.get(rows[0]['id']); window.detail(game['id']); app.processEvents()
        return window, game, file_id, root

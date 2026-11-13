"""Automação de cliques com provedores controlados, sem cadastro pré-preenchido.

O auxiliar real continua isolado em subprocesso. Somente fontes externas e o
transporte das imagens são substituídos; diálogo, fila, cache e SQLite são reais.
"""
from contextlib import ExitStack
from dataclasses import replace
import json
from pathlib import Path
import sys
import time
from unittest.mock import patch

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont, QImage, QPainter
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from checkpoint.integrations import IntegrationError, MetadataResult


METROID = dict(provider='rawg', identity='1', title='Metroid Dread', query='Metroid',
               platform='Nintendo Switch', developer='MercurySteam', publisher='Nintendo',
               description='Dados de teste: explore ZDR e enfrente os robôs E.M.M.I.')
INSIDE = dict(provider='steam', identity='304430', title='INSIDE', query='INS',
              platform='PC', developer='Playdead', publisher='Playdead',
              description='Dados de teste: um garoto explora um mundo sombrio.')


def source_assets(root, profile):
    root.mkdir(parents=True, exist_ok=True)
    (root / 'source.json').write_text(json.dumps(profile), encoding='utf-8')
    for kind, size in [('cover', (480, 720)), ('banner', (1600, 520))]:
        image = QImage(*size, QImage.Format_RGB32)
        image.fill(QColor('#193b44'))
        painter = QPainter(image)
        painter.setPen(QColor('#d9f9df'))
        painter.setFont(QFont('DejaVu Sans', 28))
        painter.drawText(image.rect().adjusted(30, 30, -30, -30),
                         Qt.AlignCenter | Qt.TextWordWrap,
                         profile['title'] + '\n\nFONTE CONTROLADA\n' + kind)
        painter.end()
        assert image.save(str(root / (kind + '.png')))


def worker_with_source(request, root):
    """Executado no auxiliar: não substitui execute_request nem a persistência."""
    root = Path(root)
    profile = json.loads((root / 'source.json').read_text(encoding='utf-8'))
    operation = json.loads(Path(request).read_text(encoding='utf-8'))['operation']

    class Catalog:
        def __init__(self, provider):
            self.provider = provider

        def search(self, title):
            first = MetadataResult(self.provider, profile['identity'], profile['title'],
                                   platforms=(profile['platform'],))
            # Duas opções garantem uma escolha explícita, sem sugestão automática.
            return [first, replace(first, external_id='999', title='Outra aventura')]

        def details(self, identity):
            if operation == 'enrich':
                raise IntegrationError('Fonte textual indisponível após a seleção (teste).')
            if self.provider != 'steamgriddb':
                (root / 'details.started').touch()
                deadline = time.monotonic() + 15
                while not (root / 'details.release').exists():
                    if time.monotonic() > deadline:
                        raise IntegrationError('Prazo da fonte controlada esgotado.')
                    time.sleep(.01)
            summary = self.search('')[0]
            if self.provider == 'steamgriddb':
                return summary
            return replace(summary, developer=profile['developer'], publisher=profile['publisher'],
                           description=profile['description'],
                           images={kind: 'https://cdn.steamgriddb.com/' + kind + '.png'
                                   for kind in ('cover', 'banner')})

        def artworks(self, identity, kind):
            return ['https://cdn.steamgriddb.com/' + kind + '.png'] if kind != 'logo' else []

    import checkpoint.unified_catalog as catalog
    import checkpoint.enrichment as enrichment
    import checkpoint.auto_artwork as artwork
    from checkpoint.credentials import CredentialVault
    from checkpoint.integrations.images import ImageCache
    from checkpoint.integrations import metadata, descriptions
    from checkpoint.worker import execute_request
    primary = Catalog(profile['provider'])
    art_source = Catalog('steamgriddb')
    real_artwork = artwork.AutoArtwork

    class ControlledArtwork(real_artwork):
        def __init__(self, library, **kwargs):
            super().__init__(library, provider=art_source, **kwargs)

    def download(cache, url):
        # Validação/decodificação/instalação atômica reais, transporte local.
        if profile.get('images_unavailable'):
            raise IntegrationError('Transporte de imagens indisponível (teste).')
        return cache.store((root / Path(url).name).read_bytes())

    with ExitStack() as stack:
        stack.enter_context(patch.object(CredentialVault, 'get', return_value=None))
        stack.enter_context(patch.object(catalog, 'providers', return_value={
            profile['provider']: primary, 'steamgriddb': art_source}))
        stack.enter_context(patch.object(metadata, 'RawgProvider', return_value=primary))
        stack.enter_context(patch.object(enrichment, 'SteamStoreProvider', return_value=primary))
        stack.enter_context(patch.object(artwork, 'AutoArtwork', ControlledArtwork))
        stack.enter_context(patch.object(ImageCache, 'download', download))
        stack.enter_context(patch.object(descriptions.PortugueseDescriptions, 'find', return_value=None))
        return execute_request(request)


def save_via_search(app, library, root, profile=None, size=(1280, 800), *, save_during_details=True):
    """Abre pelo botão da janela; digita, escolhe e salva usando QTest.

    Salva com a consulta de detalhes em andamento. A fonte textual fica offline
    no enriquecimento, para que ele não esconda a perda de dados da seleção.
    Retorna a janela aberta para permitir capturas do mesmo fluxo.
    """
    root = Path(root)
    profile = profile or METROID
    source_assets(root, profile)
    library.set_setting('prices.auto', False)
    library.set_setting('artwork.auto', True)
    from checkpoint.window import MainWindow
    from checkpoint.jobs import Job
    from checkpoint.worker import run_isolated
    import checkpoint.quick_add as quick_module
    import checkpoint.completion_queue as queue_module
    from checkpoint.credentials import CredentialVault

    support = str(Path(__file__).resolve())
    def isolated(operation, database, **arguments):
        bootstrap = ("import runpy,sys; m=runpy.run_path(sys.argv[1]); "
                     "sys.exit(m['worker_with_source'](sys.argv[2],sys.argv[3]))")
        return run_isolated(operation, database, command_factory=lambda request: [
            sys.executable, '-X', 'faulthandler', '-c', bootstrap, support, str(request), str(root)],
            **arguments)

    with ExitStack() as stack:
        stack.enter_context(patch.object(CredentialVault, 'get', return_value=None))
        stack.enter_context(patch.object(quick_module, 'run_isolated', isolated))
        stack.enter_context(patch.object(queue_module, 'run_isolated', isolated))
        window = MainWindow(library)
        window.resize(*size)
        window.show()
        app.processEvents()
        state = {'stage': 'dialog', 'error': None, 'dialog': None}
        started = time.monotonic()
        driver = QTimer()
        driver.setInterval(10)

        def click_through():
            try:
                assert time.monotonic() - started < 25, 'O fluxo por cliques não terminou.'
                dialog = app.activeModalWidget()
                if state['stage'] == 'dialog' and dialog and hasattr(dialog, 'quick_add'):
                    # Referência forte normal do driver; não modifica o ciclo de vida Qt.
                    state['dialog'] = dialog
                    QTest.keyClicks(dialog.quick_add.query, profile['query'])
                    QTest.keyClick(dialog.quick_add.query, Qt.Key_Return)
                    state['stage'] = 'results'
                elif state['stage'] == 'results' and dialog and dialog.quick_add.results.count() == 2:
                    results = dialog.quick_add.results
                    QTest.mouseClick(results.viewport(), Qt.LeftButton,
                                     pos=results.visualItemRect(results.item(0)).center())
                    state['stage'] = 'details'
                elif state['stage'] == 'details' and (root / 'details.started').exists():
                    assert dialog.quick_add.save.isEnabled()
                    if not save_during_details:
                        (root / 'details.release').touch()
                        state['stage'] = 'ready'
                        return
                    # A fonte só responde depois do clique em Salvar, sem sleep na UI.
                    QTimer.singleShot(100, lambda: (root / 'details.release').touch())
                    state['stage'] = 'saved'
                    QTest.mouseClick(dialog.quick_add.save, Qt.LeftButton)
                    driver.stop()
                elif state['stage'] == 'ready' and dialog and dialog.catalog_result.developer:
                    state['stage'] = 'saved'
                    QTest.mouseClick(dialog.quick_add.save, Qt.LeftButton)
                    driver.stop()
            except BaseException as error:
                state['error'] = error
                driver.stop()
                (root / 'details.release').touch()
                if state['dialog']:
                    state['dialog'].reject()

        driver.timeout.connect(click_through)
        driver.start()
        QTest.mouseClick(window.add_button, Qt.LeftButton)
        driver.stop()
        deadline = time.monotonic() + 25
        while (any(job.isRunning() for job in window.findChildren(Job)) or
               window.completion_queue.active or window.completion_queue.pending or
               (state['dialog'] and state['dialog'].quick_add.jobs)):
            assert time.monotonic() < deadline, 'Trabalho pendente após salvar.'
            app.processEvents()
            QTest.qWait(10)
        if state['error']:
            window.close()
            raise state['error']
        assert state['stage'] == 'saved'
        rows = library.games()
        assert len(rows) == 1, 'O clique em Salvar deve criar exatamente um jogo.'
        game = library.get(rows[0]['id'])
        window.detail(game['id'])
        app.processEvents()
        return window, game

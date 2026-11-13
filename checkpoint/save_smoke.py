"""Smoke de cadastro em diretório novo; fixture explícita, sem serviços autenticados."""
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QColor

from .dialogs import GameDialog
from . import completion_queue
from .worker import run_isolated


def start_save_smoke(app, window, directory):
    image = QImage(120, 180, QImage.Format_RGB32)
    image.fill(QColor('blue'))
    cover = directory / 'fixture-cover.png'
    if not image.save(str(cover)):
        app.exit(3)
        return
    original = completion_queue.run_isolated

    def fixture(operation, database, **arguments):
        result = run_isolated('ping', database)
        if result != {'worker': 'ok', 'schema': 4}:
            raise RuntimeError('Auxiliar do cadastro não respondeu.')
        return 'Auxiliar verificado; fixture de cadastro preservada.'

    completion_queue.run_isolated = fixture
    finished = False

    def fail():
        if not finished:
            print('Cadastro smoke: timeout', flush=True)
            app.exit(4)

    def fill():
        dialog = app.activeModalWidget()
        if not isinstance(dialog, GameDialog):
            QTimer.singleShot(5, fill)
            return
        from .integrations import MetadataResult
        result=MetadataResult('steam','1','Fixture de cadastro isolado')
        dialog.apply_catalog(result);dialog.quick_add.show_result(result)
        dialog.fields['cover'].setText(str(cover))
        dialog.validate()

    def verify():
        nonlocal finished
        if window.completion_queue.active or window.completion_queue.pending:
            QTimer.singleShot(10, verify)
            return
        try:
            games = window.library.games()
            assert len(games) == 1 and games[0]['title'] == 'Fixture de cadastro isolado'
            assert games[0]['cover'] == str(cover)
            assert window.library.sql.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
            window.detail(games[0]['id'])
            assert window.grab().save(str(directory / 'save-smoke.png'))
            print('Cadastro smoke: salvar, auxiliar, renderização e SQLite OK', flush=True)
            finished = True
            completion_queue.run_isolated = original
            window.close()
            app.exit(0)
        except Exception:
            app.exit(5)

    def begin():
        QTimer.singleShot(5, fill)
        window.add_game()
        QTimer.singleShot(10, verify)

    QTimer.singleShot(0, begin)
    QTimer.singleShot(30000, fail)

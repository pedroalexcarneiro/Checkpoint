import argparse
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtCore import QLockFile
from .database import Database
from .library import Library
from .theme import DARK
from .window import MainWindow

def main():
    parser = argparse.ArgumentParser(description='Checkpoint desktop')
    parser.add_argument('--data-dir',type=Path,help='Diretório de dados isolado')
    parser.add_argument('--smoke-test',action='store_true',help='Abre todas as páginas e encerra em ambiente isolado')
    parser.add_argument('--network-test', action='store_true', help='Testa HTTPS público sem autenticação e salva network-test.txt no diretório de dados')
    parser.add_argument('--worker-request',type=Path,help=argparse.SUPPRESS)
    parser.add_argument('--save-smoke-test',action='store_true',help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker_request:
        from .worker import execute_request
        return execute_request(args.worker_request)
    if args.save_smoke_test and (not args.data_dir or (args.data_dir/'gamevault.sqlite').exists()):
        parser.error('--save-smoke-test exige --data-dir novo, sem banco existente.')
    # Preserve o armazenamento e a trava legados para manter bibliotecas existentes.
    directory = args.data_dir or Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'.local/share')))/'GameVault'
    directory.mkdir(parents=True,exist_ok=True)
    if args.network_test:
        from .integrations.network import probe_google_connection
        result = probe_google_connection()
        (directory/'network-test.txt').write_text(result,encoding='utf-8')
        return 0
    handler = RotatingFileHandler(directory/'gamevault.log',maxBytes=2_000_000,backupCount=3,encoding='utf-8')
    logging.basicConfig(level=logging.INFO,handlers=[handler],format='%(asctime)s %(levelname)s %(message)s')
    # O callback OAuth e o URL de autorização incluem códigos e estado privados.
    logging.getLogger('google_auth_oauthlib.flow').setLevel(logging.WARNING)
    if args.smoke_test or args.save_smoke_test: os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    import faulthandler
    try:
        native_fd=os.open(directory/'native-crash.log',os.O_WRONLY|os.O_CREAT|os.O_APPEND,0o600)
        faulthandler.enable(file=native_fd,all_threads=True)
    except OSError:
        logging.warning('Registro nativo indisponível; inicialização continua.')
    # O descritor permanece aberto até a saída para registrar também falhas no shutdown.
    app = QApplication(sys.argv[:1]); app.setApplicationName('Checkpoint'); app.setStyle('Fusion'); app.setStyleSheet(DARK)
    lock = QLockFile(str(directory/'gamevault.lock'))
    if not lock.tryLock(100):
        QMessageBox.warning(None,'Checkpoint','Esta biblioteca já está aberta em outra instância.'); return 1
    db = None
    try:
        db = Database(directory/'gamevault.sqlite')
        window = MainWindow(Library(db)); window.show()
        if args.save_smoke_test:
            from .save_smoke import start_save_smoke
            start_save_smoke(app,window,directory)
        if args.smoke_test:
            from PySide6.QtCore import QTimer
            from PySide6.QtGui import QFontDatabase
            font = Path('C:/Windows/Fonts/segoeui.ttf')
            if font.exists(): QFontDatabase.addApplicationFont(str(font))
            def verify():
                try:
                    for index in range(6): window.navigate(index); app.processEvents()
                    window.navigate(0); app.processEvents(); window.grab().save(str(directory/'smoke-home.png'))
                    print('Checkpoint smoke: 6 pages OK; SQLite integrity='+db.connection.execute('PRAGMA integrity_check').fetchone()[0])
                    window.close(); app.exit(0)
                except Exception:
                    logging.exception('Smoke test falhou'); app.exit(2)
            QTimer.singleShot(200,verify)
        return app.exec()
    except Exception:
        logging.exception('Falha ao iniciar')
        QMessageBox.critical(None,'Checkpoint','Falha ao abrir a biblioteca. Consulte o log no diretório de dados.'); return 1
    finally:
        if db: db.close()
        lock.unlock()

if __name__=='__main__':
    raise SystemExit(main())

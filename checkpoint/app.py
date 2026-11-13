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
    from .data_migration import prepare_data_directory,MigrationError,LEGACY_DATABASE
    if (args.smoke_test or args.save_smoke_test) and (not args.data_dir or any((args.data_dir/name).exists() for name in ('checkpoint.sqlite',LEGACY_DATABASE))):
        parser.error('Smoke exige --data-dir novo, sem banco existente.')
    if args.smoke_test or args.save_smoke_test:os.environ['QT_QPA_PLATFORM']='offscreen'
    app=QApplication(sys.argv[:1]);app.setApplicationName('Checkpoint');app.setStyle('Fusion');app.setStyleSheet(DARK)
    from .fonts import install_fonts
    install_fonts(app)
    try:session=prepare_data_directory(args.data_dir,migrate_credentials=not (args.smoke_test or args.save_smoke_test or args.network_test))
    except MigrationError as error:
        QMessageBox.critical(None,'Dados preservados',error.user_message());return 2
    directory=session.directory
    if args.network_test:
        from .integrations.network import probe_google_connection
        try:(directory/'network-test.txt').write_text(probe_google_connection(),encoding='utf-8');return 0
        finally:session.close()
    handler = RotatingFileHandler(directory/'checkpoint.log',maxBytes=2_000_000,backupCount=3,encoding='utf-8')
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
    db = None
    try:
        db = Database(directory/'checkpoint.sqlite')
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
                    from .ui_components import service_icon
                    for name in ('Steam','Google Drive'):
                        pix=service_icon(name)
                        asset=Path(__file__).resolve().parent/'assets'/'services'/('steam.ico' if name=='Steam' else 'google-drive.png')
                        from PySide6.QtGui import QIcon
                        if not asset.is_file() or QIcon(str(asset)).pixmap(48,48).isNull() or pix.isNull():raise RuntimeError('Asset oficial ausente no pacote: '+name)
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
        session.close()

if __name__=='__main__':
    raise SystemExit(main())

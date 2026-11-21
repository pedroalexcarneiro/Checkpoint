"""Screenshots Qt reais com fixtures próprias; nunca abre dados pessoais."""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys

from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QWidget, QComboBox
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.window import MainWindow
from checkpoint.fonts import install_fonts
from render_ui_review import artwork


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--only', default='home,wishes,memories,appearance,files,settings,dialogs,statistics,library')
    parser.add_argument('--screen-width',type=int,default=1920)
    parser.add_argument('--screen-height',type=int,default=1080)
    parser.add_argument('--statistics-long-titles',action='store_true')
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    if (root/'review.sqlite').exists():
        raise SystemExit('Use uma pasta nova; evidência anterior preservada.')
    config = root/'screen.json'
    config.write_text(json.dumps({'screens': [{'name': 'review', 'width': args.screen_width, 'height': args.screen_height,
        'logicalDpi': 96, 'logicalBaseDpi': 96, 'dpr': 1}]}), encoding='utf-8')
    app = QApplication(['review', '-platform', 'offscreen:configfile='+str(config)])
    app.setStyle('Fusion')
    install_fonts(app)
    db = Database(root/'review.sqlite')
    lib = Library(db)
    lib.set_setting('artwork.auto', False)
    lib.set_setting('prices.auto', False)
    now = datetime.now(timezone.utc)
    ids = []
    titles = ('Portal 2', 'Hades', 'Celeste', 'Metroid Fusion', 'Hollow Knight', 'Animal Well')
    if args.statistics_long_titles:
        titles=('Honkai: Star Rail','The Legend of Zelda: Ocarina of Time 3D',*titles[2:])
    for n, title in enumerate(titles):
        paths = {kind: artwork(root, n, title, ('#366077', '#875560', '#536d7a', '#5c7b68', '#495972', '#78694d')[n],
            kind, width, height) for kind, width, height in (('cover', 600, 900), ('banner', 1600, 450), ('logo', 620, 150))}
        game_id = lib.save_game({'title': title, 'platform': 'GBA' if n == 3 else 'PC',
            'status': 'Jogando' if n < 2 else 'Não iniciado', 'favorite': int(n == 0), **paths})
        ids.append(game_id)
        if n < 4:
            lib.add_diary(game_id, 'Nota curta de teste.' if n % 2 else 'Encontrei uma passagem. Texto de fixture para revisar tipografia e alinhamento.')
            lib.add_media(game_id, paths['banner'], 'Captura de fixture')
        else:
            with lib.sql:
                lib.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
                lib.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)", (game_id, str(1000+n)))
            lib.set_setting(f'prices.ggdeals.{game_id}', {'state': 'ready', 'currency': 'BRL', 'checked_at': now.isoformat(),
                'retail': 2490+n*100, 'offer_context': {'steam': str(1000+n), 'platform': 'PC'},
                'offers': [{'kind': 'retail', 'shop': 'Loja de teste', 'cents': 2490+n*100, 'original': 5990,
                    'url': 'https://gg.deals/br/redirect/fixture/'}]})
    with lib.sql:
        for n, game_id in enumerate((ids[0], ids[1], ids[2], ids[0], ids[3], ids[1], ids[2])):
            start = now-timedelta(hours=n+2)
            lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?, 'finished',?)",
                (game_id, start.isoformat(), (start+timedelta(minutes=32+n)).isoformat(), (32+n)*60, 100+n))
        lib.sql.execute('INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
            (ids[0], 'isolated-review-0139', 'Portal 2 — Arquivo de teste com nome muito extenso para conferir a largura central e a ação lateral.rom', 'PC'))
        emulator = lib.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)', ('Perfil de fixture', sys.executable)).lastrowid
        lib.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',
            (emulator, 'GBA', '["{rom}"]', '.gba'))
    for platform in ('PC', 'Switch'):
        logo = artwork(root, 100, 'Registro homônimo de teste', '#366077', 'logo', 620, 150)
        game_id = lib.save_game({'title': 'Registro homônimo de teste', 'platform': platform, 'logo': logo})
        lib.delete(game_id)
    undated=lib.save_game({'title': 'Registro sem data'})
    with lib.sql:lib.sql.execute("UPDATE games SET deleted_at='' WHERE id=?",(undated,))
    window = MainWindow(lib)
    window.resize(1280, 800)
    window.show()
    manifest = []

    def settle():
        for _ in range(12):
            app.processEvents()
        pending = lambda: (window.gallery.art_cache.pending or window.game_list.art_cache.pending
                           or bool(getattr(window,'memory_art_cache',None) and window.memory_art_cache.pending))
        elapsed = 0
        while pending() and elapsed < 3000:
            QTest.qWait(5)
            elapsed += 5
        if pending():
            raise RuntimeError('Arte ainda pendente; captura recusada.')

    def capture(name, widget=window):
        settle()
        path = root/(name+'.png')
        assert widget.grab().save(str(path))
        manifest.append({'file': path.name, 'window_size': list(widget.size().toTuple()),
            'screen_size': list(app.primaryScreen().size().toTuple()), 'maximized': widget.isMaximized(),
            'dpr': widget.devicePixelRatioF(), 'qt_platform': app.platformName(), 'fixtures': True})

    selected = set(args.only.split(','))
    if 'home' in selected:
        window.navigate(0)
        capture('home-normal-1280x800')
        window.showMaximized()
        capture('home-maximizada')
        window.showNormal()
        capture('home-restaurada')
        window.resize(1920, 1080)
        capture('home-1920x1080')
        window.resize(1000, 700)
        capture('home-menor-1000x700')
    if 'wishes' in selected:
        window.showNormal()
        window.resize(1280, 800)
        window.navigate(2)
        capture('desejos-dois-normal')
        window.showMaximized()
        capture('desejos-dois-maximizada')
        window.showNormal()
        for n in range(6):
            game_id = lib.save_game({'title': ('Título longo de fixture ' * 5) if n == 0 else f'Desejo de teste {n}', 'platform': 'Switch' if n % 2 else 'PC'})
            with lib.sql:
                lib.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        window.navigate(2)
        capture('desejos-varios-normal')
        window.showMaximized()
        capture('desejos-varios-maximizada')
    if 'memories' in selected:
        window.showNormal()
        window.resize(1280, 800)
        window.navigate(3)
        capture('memorias-mista')
        tabs = window.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        capture('memorias-diario')
    if 'live-capture' in selected:
        from types import SimpleNamespace
        from PySide6.QtGui import QColor,QPixmap
        from checkpoint import game_capture
        original=game_capture.WindowsCapture
        class Frames:
            color='red'
            pid=101
            def foreground_pid(self):return self.pid
            def capture(self,pid):
                assert pid==self.pid
                pixmap=QPixmap(640,360);pixmap.fill(QColor(self.color));return pixmap
        frames=Frames();game_capture.WindowsCapture=lambda:frames
        window.launcher.active={1:(SimpleNamespace(pid=101,poll=lambda:None),0,ids[0],True),
            2:(SimpleNamespace(pid=202,poll=lambda:None),0,ids[1],True)}
        try:
            from time import monotonic
            window.resize(1280,800);window.navigate(3)
            for name,color,pid in (('primeiro-quadro','red',101),('segundo-quadro','blue',202)):
                frames.color=color;frames.pid=pid;window.capture_game_window()
                deadline=monotonic()+5
                while window.capture_writer.busy and monotonic()<deadline:QTest.qWait(5)
                assert not window.capture_writer.busy
                capture('captura-'+name)
        finally:
            game_capture.WindowsCapture=original;window.launcher.active.clear()
    if 'appearance' in selected:
        window.showNormal()
        window.resize(1280, 800)
        window.navigate(5)
        from checkpoint.settings_previews import CoverSizeChoices
        choices = window.pages[5].findChild(CoverSizeChoices)
        for percent in (70, 150):
            choices.group.button(percent).click()
            capture('capas-'+str(percent))
        choices.group.button(100).click()
        window.set_theme('black')
        window.navigate(5)
        capture('tema-preto')
        window.navigate(1)
        capture('tema-preto-biblioteca')
        window.set_theme('green')
    if 'files' in selected:
        window.showNormal()
        window.resize(1280, 800)
        window.detail(ids[0])
        window.detail_tabs.setCurrentIndex(3)
        settle();window.detail_page.ensureWidgetVisible(window.detail_tabs.currentWidget().findChild(QWidget,'traditionalSaves'),16,16)
        capture('arquivos-saves-vazio')
        from checkpoint.save_profiles import SaveProfiles
        source = root/'saves-fixture'
        source.mkdir()
        (source/'teste.sav').write_bytes(b'save sintetico de revisao')
        SaveProfiles(lib).configure(ids[0], source, ['*.sav'])
        window.detail(ids[0])
        window.detail_tabs.setCurrentIndex(3)
        settle();window.detail_page.ensureWidgetVisible(window.detail_tabs.currentWidget().findChild(QWidget,'traditionalSaves'),16,16)
        capture('arquivos-saves-configurado')
    if 'settings' in selected:
        window.showNormal()
        window.resize(1280, 800)
        window.navigate(5)
        for index in range(window.settings_tabs.count()):
            title = window.settings_tabs.tabText(index)
            if title in ('Emuladores', 'Lixeira'):
                window.settings_tabs.setCurrentIndex(index)
                capture('config-'+('emuladores' if title == 'Emuladores' else 'lixeira'))
    if 'statistics' in selected:
        lib.save_game({'title':lib.get(ids[2])['title'],'status':'Concluído'},ids[2])
        window.showNormal();window.resize(1280,800);window.navigate(4)
        period=window.pages[4].findChild(QComboBox,'statisticsPeriod');period.setCurrentIndex(period.findData('weekly'))
        capture('estatisticas')
        scroll=window.pages[4].findChildren(QWidget,'completionMetrics')[0]
        window.pages[4].layout().itemAt(0).widget().ensureWidgetVisible(scroll)
        capture('estatisticas-conclusoes')
        from checkpoint.statistics_view import HeatmapViewport
        for width,height in ((1000,700),(1280,800),(1920,1080)):
            window.resize(width,height);window.navigate(4)
            period=window.pages[4].findChild(QComboBox,'statisticsPeriod');period.setCurrentIndex(period.findData('3m'))
            settle()
            scroller=window.pages[4].layout().itemAt(0).widget()
            scroller.ensureWidgetVisible(window.pages[4].findChild(HeatmapViewport),16,16)
            capture(f'estatisticas-{width}x{height}-calendario')
            scroller.ensureWidgetVisible(window.pages[4].findChild(QWidget,'statisticsGameRow'),16,16)
            capture(f'estatisticas-{width}x{height}-lista')
    if 'library' in selected:
        for n in range(24):lib.save_game({'title':f'Jogo extra de teste {n}'})
        window.showNormal();window.resize(1280,800);window.navigate(1);window.view.setCurrentIndex(1)
        capture('biblioteca-lista-rolagem')
    if 'controller' in selected or 'switch-controller' in selected:
        from checkpoint.controller_capture import PREFERENCE
        from PySide6.QtCore import QTimer
        from types import SimpleNamespace
        controller=window.controller_capture
        controller.backend=SimpleNamespace(buttons=lambda slot:0 if slot==1 else None)
        if 'switch-controller' in selected:
            from checkpoint.switch_controller import CAPTURE_MASK,SwitchDevice
            identity='switch:'+'a'*64
            controller.switch_backend=SimpleNamespace(
                devices=lambda:{identity:SwitchDevice('Switch Pro · USB',1,0)},close=lambda:None)
            controller.switch_injected=True
            preference={'device':identity,'buttons':CAPTURE_MASK}
            capture_name='captura-switch-pro'
        else:
            preference={'slot':1,'buttons':0x1100}
            capture_name='captura-controle'
        lib.set_setting(PREFERENCE,preference);controller.load()
        window.navigate(5);window.settings_tabs.setCurrentIndex(0)
        def capture_controller():
            dialog=QApplication.activeModalWidget()
            try:capture(capture_name,dialog)
            finally:dialog.reject()
        QTimer.singleShot(0,capture_controller)
        controller.configure()
    if 'lists' in selected:
        from checkpoint.library_lists import LibraryLists,manage_lists
        from PySide6.QtCore import QTimer
        lists=LibraryLists(lib)
        identity=lists.save(None,'Para o fim de semana',ids[:3])
        lists.save(None,'Favoritos do ano',ids[1:4])
        window.showNormal();window.resize(1280,800);window.navigate(1);window.view.setCurrentIndex(1)
        window.update_custom_lists();window.select_custom_list(window.custom_lists.findData(identity))
        capture('biblioteca-lista-personalizada')
        def capture_lists():
            from checkpoint.artwork_cache import ArtworkCache
            dialog=QApplication.activeModalWidget()
            try:
                cache=dialog.findChild(ArtworkCache,'listPickerLogoCache')
                dialog.grab()
                for _ in range(600):
                    if not cache.pending:break
                    QTest.qWait(5)
                assert not cache.pending
                capture('biblioteca-gerenciar-listas',dialog)
            finally:dialog.reject()
        QTimer.singleShot(0,capture_lists)
        manage_lists(window,identity)
    if 'dialogs' in selected:
        from checkpoint.local_rom_dialog import RomSourceDialog, LocalRomDialog
        from checkpoint.emulator_dialog import EmulatorDialog
        from checkpoint.home_components import show_execution_history
        from PySide6.QtCore import QTimer
        from PySide6.QtWidgets import QDialog
        for name, dialog in (('dialog-origem-rom', RomSourceDialog(lib, ids[0], window)),
                ('dialog-rom-local', LocalRomDialog(lib, ids[0], window)),
                ('dialog-emuladores', EmulatorDialog(lib, window))):
            dialog.show()
            capture(name, dialog)
            dialog.reject()
        def history():
            for widget in QApplication.topLevelWidgets():
                if isinstance(widget, QDialog) and widget.windowTitle() == 'Histórico de execuções' and widget.isVisible():
                    capture('dialog-historico', widget)
                    widget.reject()
        QTimer.singleShot(20, history)
        show_execution_history(window)
        from checkpoint.dialog_style import AppMessages
        def confirmation():
            modal=QApplication.activeModalWidget()
            if modal is not None:
                capture('dialog-confirmar-sessao',modal)
                modal.reject()
        QTimer.singleShot(20,confirmation)
        AppMessages.start_session(window)
    (root/'manifest.json').write_text(json.dumps({'platform': 'Linux Qt offscreen; não homologa Windows',
        'fixtures': True, 'screenshots': manifest}, indent=2), encoding='utf-8')
    window.close()
    db.close()
    print(root)


if __name__ == '__main__':
    main()

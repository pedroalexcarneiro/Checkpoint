import json
import logging
from pathlib import Path
from PySide6.QtCore import Qt,QSize,QTimer,QUrl,Slot
from PySide6.QtGui import QPixmap,QIcon,QDesktopServices
from PySide6.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QPushButton,
    QLineEdit,QComboBox,QListWidget,QListWidgetItem,QAbstractItemView,QTableWidget,QTableWidgetItem,
    QStackedWidget,QScrollArea,QFrame,QMessageBox,QFileDialog,QTextEdit,QInputDialog,QDialog,
    QProgressBar,QFormLayout,QCheckBox)
from .library import STATUSES,now
from .dialogs import GameDialog,ImageDialog
from .launcher import Launcher
from .saves import SaveBackupService

PAGES = ['Início','Biblioteca','Desejos','Memórias','Estatísticas','Configurações']

def label(text,kind=None):
    widget = QLabel(text); widget.setWordWrap(True)
    widget.setTextFormat(Qt.PlainText)
    if kind: widget.setObjectName(kind)
    return widget

def button(text,callback,primary=False):
    widget = QPushButton(text); widget.clicked.connect(callback)
    if primary: widget.setObjectName('primary')
    return widget

class MainWindow(QMainWindow):
    def __init__(self,library):
        super().__init__(); self.library = library; self.launcher = Launcher(library)
        from PySide6.QtWidgets import QApplication
        from .theme import apply_theme,DEFAULT_THEME
        self.theme=apply_theme(QApplication.instance(),library.setting('appearance.theme',DEFAULT_THEME))
        self.setWindowTitle('Checkpoint'); self.resize(1380,900); self.setMinimumSize(1000,700)
        from .completion_queue import CompletionQueue
        self.completion_queue=CompletionQueue(library.db.path,self)
        self.completion_queue.updated.connect(self.game_completed)
        self.completion_queue.busy_changed.connect(self.completion_busy)
        self.completion_bar=QProgressBar();self.completion_bar.setRange(0,0);self.completion_bar.hide()
        self.statusBar().addPermanentWidget(self.completion_bar)
        self.completion_stop=button('Parar após o jogo atual',self.completion_queue.cancel_pending)
        self.completion_stop.hide();self.statusBar().addPermanentWidget(self.completion_stop)
        self.hero_upgrade_attempted=set();self.current_page = 0; self.current_game = None; self.last_deleted = None; self.save_jobs = {}
        root = QWidget(); root.setObjectName('root'); self.setCentralWidget(root)
        layout = QHBoxLayout(root); layout.setContentsMargins(0,0,0,0); layout.setSpacing(0)
        sidebar = QWidget(); sidebar.setObjectName('sidebar'); sidebar.setFixedWidth(238)
        nav = QVBoxLayout(sidebar); nav.setContentsMargins(10,20,10,20)
        from .branding import BrandWidget,app_icon
        self.brand=BrandWidget(self.theme);nav.addWidget(self.brand);nav.addSpacing(24)
        self.setWindowIcon(app_icon(self.theme));QApplication.instance().setWindowIcon(self.windowIcon())
        self.nav_names=['home','library','wish','memories','stats','settings']
        self.nav_buttons = []
        for index,title in enumerate(PAGES):
            item = button(title,lambda checked=False,i=index:self.navigate(i)); item.setObjectName('nav'); item.setCheckable(True)
            from .ui_components import nav_icon
            item.setIcon(nav_icon(self.nav_names[index],self.theme.colors['muted']));item.setIconSize(QSize(21,21))
            self.nav_buttons.append(item)
            if index==5:nav.addStretch()
            nav.addWidget(item)
        from . import __version__
        nav.addWidget(label('v'+__version__,'muted'))
        layout.addWidget(sidebar)
        self.host = QVBoxLayout(); self.host.setContentsMargins(34,28,34,22); self.host.setSpacing(24)
        layout.addLayout(self.host,1)
        self.header_widget=QWidget();self.header = QHBoxLayout(self.header_widget);self.header.setContentsMargins(0,0,0,0); self.heading = label('','title'); self.header.addWidget(self.heading); self.header.addStretch()
        self.add_button=button('+ Adicionar jogo',self.add_game,True);self.header.addWidget(self.add_button); self.host.addWidget(self.header_widget)
        self.stack = QStackedWidget(); self.host.addWidget(self.stack,1)
        self.pages = []
        for _ in PAGES:
            page = QWidget(); self.pages.append(page); self.stack.addWidget(page)
        self.build_library()
        self.library_filters.removeWidget(self.search);self.search.setMinimumWidth(220);self.search.setMaximumWidth(380)
        self.header.insertWidget(1,self.search);self.header.setSpacing(22)
        self.search.returnPressed.connect(self.search_library)
        self.library_filters.removeWidget(self.platform);self.library_options.insertWidget(2,self.platform)
        self.platform.setMaximumWidth(190);self.sort.setMaximumWidth(150);self.view.setMaximumWidth(100)
        self.navigate(0)
        self.timer = QTimer(self); self.timer.timeout.connect(self.poll_sessions); self.timer.start(1000)
        self.statusBar().setSizeGripEnabled(False);self.statusBar().showMessage('')

    def showEvent(self,event):
        super().showEvent(event)
        from .window_style import titlebar_theme
        titlebar_theme(self,self.theme.key!='white')

    def search_library(self):self.navigate(1)

    def guard(self,callback):
        try: return callback()
        except Exception as error:
            logging.exception('Operação falhou')
            QMessageBox.warning(self,'Checkpoint',str(error))

    def clear_page(self,index):
        old = self.pages[index]
        self.stack.removeWidget(old); old.deleteLater()
        page = QWidget(); self.pages[index] = page; self.stack.insertWidget(index,page)
        layout = QVBoxLayout(page); layout.setContentsMargins(0,0,0,0); layout.setSpacing(18)
        return layout

    def navigate(self,index):
        self.current_page = index; self.current_game = None;self.header_widget.show()
        for i,b in enumerate(self.nav_buttons): b.setChecked(i==index)
        self.heading.setText(PAGES[index]);self.add_button.setVisible(index in (0,1));self.search.setVisible(index in (0,1))
        if index==0: self.home()
        elif index==1: self.refresh_library()
        elif index==2: self.wishlist()
        elif index==3: self.memories()
        elif index==4: self.statistics()
        else: self.settings()
        self.stack.setCurrentIndex(index)

    def panel(self,layout,title,subtitle=''):
        frame = QFrame(); frame.setObjectName('panel'); inner = QVBoxLayout(frame); inner.setContentsMargins(24,24,24,24)
        inner.addWidget(label(title,'title'))
        if subtitle: inner.addWidget(label(subtitle,'muted'))
        layout.addWidget(frame); return inner

    def home(self):
        from .home_view import build_home
        build_home(self)

    def build_library(self):
        layout = QVBoxLayout(self.pages[1]); layout.setContentsMargins(0,0,0,0)
        from PySide6.QtWidgets import QTabBar
        self.library_tabs=QTabBar();self.library_tabs.setExpanding(False);self.library_tabs.setDrawBase(False);self.library_tabs.setObjectName('libraryTabs')
        for name in ('Todos','Favoritos','Jogando','Concluídos'):self.library_tabs.addTab(name)
        self.library_tabs.currentChanged.connect(self.library_tab_changed);layout.addWidget(self.library_tabs)
        filters = QHBoxLayout();self.library_filters=filters; self.search = QLineEdit(); self.search.setPlaceholderText('Buscar jogo…');self.search.setObjectName('headerSearch')
        self.search.textChanged.connect(self.refresh_library); filters.addWidget(self.search,2)
        self.platform = QComboBox(); self.genre = QComboBox(); self.status = QComboBox()
        self.extra_filters=QWidget();extra_layout=QHBoxLayout(self.extra_filters);extra_layout.setContentsMargins(0,0,0,0)
        self.platform.addItem('Todas as plataformas',''); self.genre.addItem('Todos os gêneros','')
        self.status.addItem('Todos os status','')
        for value in STATUSES: self.status.addItem(value,value)
        for combo in [self.platform,self.genre,self.status]:
            combo.currentIndexChanged.connect(self.refresh_library)
            if combo is self.platform:filters.addWidget(combo)
            else:extra_layout.addWidget(combo)
        layout.addLayout(filters)
        options = QHBoxLayout();self.library_options=options; self.count = label('','muted'); options.addWidget(self.count); options.addStretch()
        self.favorites = QCheckBox('Favoritos',self.pages[1]); self.favorites.toggled.connect(self.refresh_library);self.favorites.hide()
        filter_button=QPushButton('Filtros');filter_button.setCheckable(True);filter_button.toggled.connect(self.extra_filters.setVisible);options.addWidget(filter_button)
        self.sort = QComboBox(); self.sort.addItem('Título','title'); self.sort.addItem('Mais recentes','recent'); self.sort.addItem('Maior nota','rating')
        self.sort.currentIndexChanged.connect(self.refresh_library); options.addWidget(self.sort)
        self.view = QComboBox(); self.view.addItems(['Galeria','Lista']); self.view.currentIndexChanged.connect(self.refresh_library); options.addWidget(self.view)
        layout.addLayout(options);layout.addWidget(self.extra_filters);self.extra_filters.hide()
        from .cover_grid import CoverGrid
        self.gallery=CoverGrid(self.theme,self.pages[1]);self.gallery.setIconSize(QSize(174,232))
        self.gallery.itemActivated.connect(lambda item:self.detail(item.data(Qt.UserRole)))
        self.gallery.itemClicked.connect(lambda item:self.detail(item.data(Qt.UserRole)))
        self.table = QTableWidget(0,5); self.table.setIconSize(QSize(42,56)); self.table.setHorizontalHeaderLabels(['Jogo','Plataforma','Status','Gênero','Nota'])
        self.table.horizontalHeader().setStretchLastSection(True); self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(lambda row,col:self.detail(self.table.item(row,0).data(Qt.UserRole)))
        layout.addWidget(self.gallery,1); layout.addWidget(self.table,1)
        self.gallery.setObjectName('coverGrid');self.gallery.setFrameShape(QFrame.NoFrame);self.gallery.setTextElideMode(Qt.ElideRight)

    @Slot(int)
    def library_tab_changed(self,index):
        self.favorites.blockSignals(True);self.status.blockSignals(True)
        self.favorites.setChecked(index==1)
        status={2:'Jogando',3:'Concluído'}.get(index,'')
        self.status.setCurrentIndex(max(0,self.status.findData(status)))
        self.favorites.blockSignals(False);self.status.blockSignals(False);self.refresh_library()

    def refresh_library(self,*args):
        if not hasattr(self,'gallery'): return
        for combo,key,caption in [(self.platform,'platform','Todas as plataformas'),(self.genre,'genre','Todos os gêneros')]:
            selected = combo.currentData(); values = sorted({value.strip() for g in self.library.games() for value in (g[key].split(',') if key=='genre' else [g[key]]) if value.strip()})
            combo.blockSignals(True); combo.clear(); combo.addItem(caption,'')
            for value in values: combo.addItem(value,value)
            index = combo.findData(selected); combo.setCurrentIndex(max(0,index)); combo.blockSignals(False)
        games = self.library.games(self.search.text(),self.platform.currentData(),self.genre.currentData(),self.status.currentData(),self.favorites.isChecked(),self.sort.currentData())
        compact=self.library.setting('appearance.density','comfortable')=='compact'
        self.gallery.setIconSize(QSize(138,184) if compact else QSize(174,232));self.gallery.theme=self.theme;self.gallery.set_density(compact)
        self.gallery.clear(); self.table.setRowCount(len(games)); self.count.setText(f'{len(games)} jogos' if games else 'Nenhum jogo encontrado. Adicione um jogo ou ajuste os filtros.')
        for row,game in enumerate(games):
            pix = QPixmap(game['cover']) if game['cover'] else QPixmap()
            if pix.isNull():
                pix = QPixmap(174,232); pix.fill(Qt.GlobalColor.darkCyan)
                from PySide6.QtGui import QPainter,QColor,QFont
                painter = QPainter(pix); painter.fillRect(pix.rect(),QColor(self.theme.colors['selected'])); painter.setPen(QColor(self.theme.colors['accent']))
                painter.setFont(QFont('Segoe UI',42)); painter.drawText(pix.rect(),Qt.AlignCenter,game['title'][:2].upper()); painter.end()
            item = QListWidgetItem(QIcon(pix),('★ ' if game['favorite'] else '')+game['title']+'\n'+game['status'])
            item.setData(Qt.UserRole,game['id']);item.setData(Qt.UserRole+1,game);self.gallery.addItem(item)
            for col,key in enumerate(['title','platform','status','genre','rating']):
                cell = QTableWidgetItem(str(game[key]) if game[key] is not None else '—'); cell.setData(Qt.UserRole,game['id']);
                if col==0: cell.setIcon(QIcon(pix))
                self.table.setItem(row,col,cell)
            self.table.setRowHeight(row,64)
        self.table.resizeColumnsToContents(); self.gallery.setVisible(self.view.currentIndex()==0); self.table.setVisible(self.view.currentIndex()==1)

    def open_selected(self):
        if self.view.currentIndex()==0:
            item = self.gallery.currentItem()
        else:
            row = self.table.currentRow(); item = self.table.item(row,0) if row>=0 else None
        if item: self.detail(item.data(Qt.UserRole))

    def add_game(self):
        dialog = GameDialog(self,library=self.library)
        result=dialog.exec()
        if dialog.steam_requested:
            QTimer.singleShot(0,self.steam);return
        if result==QDialog.Accepted:
            def save():
                from .game_import import save_import
                game_id=save_import(self.library,dialog.data(),dialog.drive_file_id,dialog.catalog_result)
                self.refresh_library();self.detail(game_id)
                self.statusBar().showMessage('Jogo salvo na biblioteca.')
                if dialog.complete_on_save.isChecked():
                    self.completion_queue.submit([game_id])
            self.guard(save)

    def edit_game(self,game_id):
        dialog = GameDialog(self,self.library.get(game_id),library=self.library)
        if dialog.exec()==QDialog.Accepted:
            def save():
                result=dialog.catalog_result
                if result:
                    with self.library.sql:
                        existing=self.library.sql.execute('SELECT game_id FROM external_identifiers WHERE provider=? AND external_id=?',(result.provider,result.external_id)).fetchone()
                        previous=self.library.sql.execute('SELECT external_id FROM external_identifiers WHERE game_id=? AND provider=?',(game_id,result.provider)).fetchone()
                        if existing and existing[0]!=game_id:raise ValueError('Este jogo do catálogo já pertence a outro cadastro.')
                        if previous and previous[0]!=result.external_id:raise ValueError('Este cadastro já tem outra identidade confirmada.')
                        self.library.sql.execute('INSERT OR IGNORE INTO external_identifiers VALUES(?,?,?)',(game_id,result.provider,result.external_id))
                self.library.save_game(dialog.data(),game_id)
                if result:
                    self.completion_queue.submit([game_id],force=True)
                self.refresh_library();self.detail(game_id)
            self.guard(save)

    def detail(self,game_id):
        game=self.library.get(game_id)
        if not game:return
        from .detail_view import build_detail
        build_detail(self,game)
        self.upgrade_steam_banner(game)

    def upgrade_steam_banner(self,game):
        if game['id'] in self.hero_upgrade_attempted or not self.library.setting('artwork.auto',True):return
        identity=self.library.sql.execute("SELECT external_id FROM external_identifiers WHERE game_id=? AND provider='steam'",(game['id'],)).fetchone()
        if not identity:return
        from .enrichment import replaceable_steam_header
        if replaceable_steam_header(self.library,game,identity[0]):
            self.hero_upgrade_attempted.add(game['id']);self.completion_queue.submit([game['id']])

    def remove_game(self,game_id):
        if QMessageBox.question(self,'Remover jogo','Mover este jogo para a lixeira? Arquivos e saves serão preservados.')==QMessageBox.Yes:
            self.library.delete(game_id); self.last_deleted = game_id; self.navigate(1)
            self.statusBar().showMessage('Jogo removido. Restaure pela lixeira em Configurações.')

    def achievement(self,game_id):
        text,ok = QInputDialog.getText(self,'Conquista pessoal','Nome do marco alcançado:')
        if ok and text.strip():
            with self.library.sql:
                self.library.sql.execute('INSERT INTO achievements(game_id,title,unlocked_at) VALUES(?,?,?)',(game_id,text.strip(),now()))
            self.detail(game_id)

    def import_media(self,game_id):
        path,_ = QFileDialog.getOpenFileName(self,'Selecionar mídia','','Mídia (*.png *.jpg *.jpeg *.webp *.mp4 *.mkv *.avi *.mov)')
        if path:
            caption,ok = QInputDialog.getText(self,'Legenda','Descrição da captura:')
            if ok: self.guard(lambda:self.library.add_media(game_id,path,caption)); self.detail(game_id)

    def show_media(self,media):
        if not Path(media['path']).is_file():
            QMessageBox.warning(self,'Mídia indisponível','O arquivo foi movido ou removido.'); return
        if media['kind']=='image': ImageDialog(media['path'],self).exec()
        else: QDesktopServices.openUrl(QUrl.fromLocalFile(media['path']))

    def memories(self):
        layout = self.clear_page(3)
        rows = self.library.sql.execute('SELECT d.*,g.title FROM diary_entries d JOIN games g ON g.id=d.game_id WHERE g.deleted_at IS NULL ORDER BY d.created_at DESC').fetchall()
        scroll = QScrollArea(); scroll.setWidgetResizable(True); body = QWidget(); inner = QVBoxLayout(body)
        if not rows: inner.addWidget(label('Nenhuma memória registrada.','muted'))
        for row in rows:
            panel = self.panel(inner,row['title'],row['created_at'][:10]); panel.addWidget(label(row['text']))
            panel.addWidget(button('Abrir jogo',lambda checked=False,g=row['game_id']:self.detail(g)))
        inner.addWidget(label('MÍDIA IMPORTADA','eyebrow'))
        for row in self.library.sql.execute('SELECT m.* FROM media_files m JOIN games g ON g.id=m.game_id WHERE g.deleted_at IS NULL ORDER BY m.id DESC'):
            inner.addWidget(button(Path(row['path']).name,lambda checked=False,m=dict(row):self.show_media(m)))
        inner.addStretch(); scroll.setWidget(body); layout.addWidget(scroll)

    def add_wish(self,game_id):
        value,ok = QInputDialog.getDouble(self,'Lista de desejos','Preço desejado em R$:',0,0,100000,2)
        if ok:
            with self.library.sql:
                self.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,?) ON CONFLICT(game_id) DO UPDATE SET target_cents=excluded.target_cents',(game_id,round(value*100)))
            self.statusBar().showMessage('Jogo adicionado à lista de desejos.')

    def wishlist(self):
        layout = self.clear_page(2)
        layout.addWidget(label('Preço desejado em reais. Consultas automáticas de lojas ainda não estão disponíveis nesta versão.','muted'))
        rows = self.library.sql.execute('SELECT g.*,w.target_cents FROM wishlist w JOIN games g ON g.id=w.game_id WHERE g.deleted_at IS NULL').fetchall()
        if not rows: layout.addWidget(label('Nenhum jogo na lista de desejos.','muted'))
        for row in rows:
            bar = QHBoxLayout(); bar.addWidget(button(row['title'],lambda checked=False,g=row['id']:self.detail(g)))
            bar.addWidget(label(f"Meta: R$ {row['target_cents']/100:.2f}")); bar.addWidget(button('Alterar meta',lambda checked=False,g=row['id']:self.add_wish(g)))
            bar.addWidget(button('Retirar',lambda checked=False,g=row['id']:self.remove_wish(g))); layout.addLayout(bar)
        layout.addStretch()

    def remove_wish(self,game_id):
        with self.library.sql: self.library.sql.execute('DELETE FROM wishlist WHERE game_id=?',(game_id,))
        self.navigate(2)

    def statistics(self):
        outer = self.clear_page(4); scroll = QScrollArea(); scroll.setWidgetResizable(True); body = QWidget(); layout = QVBoxLayout(body); scroll.setWidget(body); outer.addWidget(scroll); stats = self.library.stats()
        panel = self.panel(layout,f"{stats['total']} jogos na sua biblioteca",f"{stats['seconds']/3600:.1f} horas · {stats['sessions']} sessões confirmadas · média de {stats['average']/60:.1f} min por sessão")
        for status,count in stats['statuses'].items():
            panel.addWidget(label(f'{status}  ·  {count}'))
            progress = QProgressBar(); progress.setRange(0,max(1,stats['total'])); progress.setValue(count); progress.setTextVisible(False); panel.addWidget(progress)
        layout.addWidget(label('DISTRIBUIÇÃO POR PLATAFORMA','eyebrow'))
        for platform,count in stats['platforms'].items(): layout.addWidget(label(f'{platform}   {count} jogos'))
        for title,key in [('Por gênero','genres'),('Tempo semanal (início da semana UTC)','weekly'),('Tempo mensal (UTC)','monthly'),('Conclusões por mês','completions')]:
            layout.addWidget(label(title.upper(),'eyebrow'))
            values = stats[key]
            if not values: layout.addWidget(label('Sem registros neste período.','muted'))
            for name,value in values.items():
                unit = f'{value/3600:.1f} h' if key in {'weekly','monthly'} else str(value)
                layout.addWidget(label(f'{name} · {unit}'))
        layout.addWidget(label('MAIS JOGADOS','eyebrow'))
        for game in stats['top']: layout.addWidget(label(game['title']+f" · {game['seconds']/3600:.1f} h"))
        if not stats['total']: layout.addWidget(label('Nenhum jogo cadastrado.','muted'))
        layout.addStretch()

    def settings(self):
        from .settings_view import build_settings
        build_settings(self)

    @Slot(int)
    def theme_changed(self,index):
        self.set_theme(self.theme_selector.itemData(index))

    @Slot(int)
    def settings_section_changed(self,index):self.settings_section=index

    def set_density(self,density):
        self.library.set_setting('appearance.density',density);self.refresh_library()

    def complete_library(self):
        ids=[row[0] for row in self.library.sql.execute('SELECT id FROM games WHERE deleted_at IS NULL')]
        if not ids:
            self.statusBar().showMessage('Nenhum jogo cadastrado.');return
        self.completion_queue.submit(ids,force=True)

    @Slot(int,str)
    def game_completed(self,game_id,message):
        self.refresh_library()
        if self.current_game==game_id and self.library.get(game_id):self.detail(game_id)
        elif self.current_page==0:self.home()
        self.statusBar().showMessage(message)

    @Slot(int)
    def completion_busy(self,count):
        self.completion_bar.setVisible(count>0);self.completion_stop.setVisible(count>0)
        if count:
            self.completion_bar.setToolTip(f'{count} jogos aguardando ficha e imagens')
            self.statusBar().showMessage('Buscando ficha e imagens em segundo plano…')

    def set_theme(self,key):
        from PySide6.QtWidgets import QApplication
        from .theme import apply_theme
        self.library.set_setting('appearance.theme',key)
        self.theme=apply_theme(QApplication.instance(),key)
        from .branding import app_icon
        from .ui_components import Hero,nav_icon
        from .window_style import titlebar_theme
        titlebar_theme(self,self.theme.key!='white')
        self.brand.set_theme(self.theme);self.setWindowIcon(app_icon(self.theme));QApplication.instance().setWindowIcon(self.windowIcon())
        for item,name in zip(self.nav_buttons,self.nav_names):item.setIcon(nav_icon(name,self.theme.colors['muted']))
        for hero in self.findChildren(Hero):hero.set_theme(self.theme)
        self.refresh_library()

    def updates(self):
        if self.launcher.active or self.save_jobs:
            QMessageBox.information(self,'Atualizações','Encerre as sessões e aguarde os backups antes de atualizar.'); return
        from .updates_dialog import UpdatesDialog
        dialog=UpdatesDialog(self.library.db.path.parent,self)
        dialog.exec()
        if dialog.approved: self.close()

    def emulators(self):
        from .emulator_dialog import EmulatorDialog
        EmulatorDialog(self.library,self).exec()

    def artworks(self,game_id):
        from .artwork_dialog import ArtworkDialog
        ArtworkDialog(self.library,self.library.get(game_id),self).exec(); self.detail(game_id)

    def start_game(self,game):
        if game['id'] in self.save_jobs:
            QMessageBox.information(self,'Saves','Aguarde a operação de saves antes de jogar.'); return
        self.guard(lambda:self.launcher.start(game))

    def launch_rom(self,game_id,file):
        if game_id in self.save_jobs:
            QMessageBox.information(self,'Saves','Aguarde a operação de saves antes de jogar.'); return
        from .launcher import EmulatorCommand
        profiles = [dict(r) for r in self.library.sql.execute('SELECT p.*,e.name,e.executable FROM emulator_profiles p JOIN emulators e ON e.id=p.emulator_id')]
        profiles = [p for p in profiles if p['platform']==file['platform'] and (not p['extensions'].strip() or file['extension'].casefold() in [e.strip().casefold() for e in p['extensions'].split(',')])]
        if not profiles:
            QMessageBox.information(self,'Emuladores','Nenhum perfil compatível. Configure plataforma e extensões do emulador.'); return
        choice,ok = QInputDialog.getItem(self,'Executar versão','Escolha o perfil:',[p['name'] for p in profiles],0,False)
        if not ok: return
        profile = profiles[[p['name'] for p in profiles].index(choice)]
        if QMessageBox.question(self,'Registro da sessão','Este emulador não possui detecção validada de encerramento da ROM. Você deverá encerrar o registro manualmente ao terminar de jogar. Iniciar?')!=QMessageBox.Yes: return
        def launch():
            command = EmulatorCommand.build(profile['executable'],profile['arguments_json'],file['local_path'])
            self.launcher.start_command(game_id,command,False)
            with self.library.sql:
                self.library.sql.execute('UPDATE rom_versions SET profile_id=? WHERE file_id=?',(profile['id'],file['id']))
            self.detail(game_id)
        self.guard(launch)

    def end_session(self,session,game_id):
        if session in self.launcher.active:
            self.launcher.finish(session); self.detail(game_id); self.auto_backup(game_id)

    def metadata(self):
        from .metadata_dialog import MetadataDialog
        dialog = MetadataDialog(self.library,self)
        if dialog.exec()==QDialog.Accepted and dialog.imported_id:
            self.refresh_library(); self.detail(dialog.imported_id)

    def drive(self):
        from .drive_dialog import DriveDialog
        DriveDialog(self.library,self).exec(); self.refresh_library()

    def steam(self):
        from .steam_dialog import SteamDialog
        dialog = SteamDialog(self.library, self)
        dialog.exec()
        if dialog.changed:
            self.refresh_library()
            if self.current_game and self.library.get(self.current_game):
                self.detail(self.current_game)

    def integration_status(self,provider):
        key = {'Google Drive':'drive-readonly','RAWG':'rawg','SteamGridDB':'steamgriddb','Steam':'steam'}.get(provider)
        if not key: return 'Provedor ainda não implementado'
        try:
            from .credentials import CredentialVault
            return 'Credencial salva · conexão não verificada' if CredentialVault().get(key) else 'Não configurada'
        except Exception: return 'Cofre de credenciais indisponível'

    def configure_key(self,provider):
        value,ok = QInputDialog.getText(self,'Credencial '+provider,'Chave da API (armazenada no cofre do Windows):',QLineEdit.Password)
        if ok and value.strip():
            from .credentials import CredentialVault
            self.guard(lambda:CredentialVault().set(provider,value.strip())); self.navigate(5)

    def choose_directory(self,key):
        path = QFileDialog.getExistingDirectory(self,'Selecionar pasta')
        if path: self.library.set_setting(key,path); self.navigate(5)

    def backup_database(self):
        path,_ = QFileDialog.getSaveFileName(self,'Backup do banco','gamevault-backup.sqlite','SQLite (*.sqlite)')
        if path: self.guard(lambda:self.library.db.backup(Path(path)))

    def configure_saves(self,game_id):
        if game_id in self.save_jobs:
            QMessageBox.information(self,'Saves','Aguarde a operação de saves antes de alterar o perfil.'); return
        source = QFileDialog.getExistingDirectory(self,'Pasta de saves tradicionais deste jogo')
        if not source: return
        patterns,ok = QInputDialog.getText(self,'Saves tradicionais','Padrões separados por vírgula (ex.: *.sav,*.srm):')
        if not ok: return
        def save():
            from .save_profiles import SaveProfiles
            SaveProfiles(self.library).configure(game_id,source,[p.strip() for p in patterns.split(',') if p.strip()])
            self.statusBar().showMessage('Configuração de saves salva para este jogo.')
        self.guard(save)

    def backup_saves(self):
        source = QFileDialog.getExistingDirectory(self,'Pasta de saves tradicionais')
        if not source: return
        patterns,ok = QInputDialog.getText(self,'Arquivos de progresso','Padrões separados por vírgula (ex.: *.sav,*.srm). Não inclua save states:')
        if not ok: return
        destination = self.library.setting('save_backups')
        if not destination:
            QMessageBox.information(self,'Configuração necessária','Selecione a pasta de backups nas configurações.'); return
        def create():
            path,checksum,manifest = SaveBackupService(destination).create(source,[p.strip() for p in patterns.split(',') if p.strip()])
            with self.library.sql:
                self.library.sql.execute('INSERT INTO save_backups(created_at,path,sha256,manifest_json) VALUES(?,?,?,?)',(now(),str(path),checksum,json.dumps(manifest)))
            QMessageBox.information(self,'Backup criado',str(path))
        self.guard(create)

    def restore_saves(self):
        rows = self.library.sql.execute('SELECT * FROM save_backups ORDER BY id DESC').fetchall()
        if not rows:
            QMessageBox.information(self,'Backups','Ainda não há backups locais registrados.'); return
        options = [f"{r['id']} · {r['created_at']}" for r in rows]
        selected,ok = QInputDialog.getItem(self,'Restaurar','Versão:',options,0,False)
        if not ok: return
        row = rows[options.index(selected)]
        destination = QFileDialog.getExistingDirectory(self,'Restaurar na pasta de saves')
        if not destination: return
        if QMessageBox.question(self,'Restaurar saves','Restaurar esta versão? Os arquivos existentes serão preservados em uma cópia antes da substituição.')!=QMessageBox.Yes: return
        self.guard(lambda:SaveBackupService(Path(row['path']).parent).restore(row['path'],destination,row['sha256']))

    def restore_game(self,game_id):
        self.library.restore(game_id); self.navigate(5)

    def recover_sessions(self):
        rows = self.library.sql.execute("SELECT s.*,g.title FROM play_sessions s JOIN games g ON g.id=s.game_id WHERE s.state='interrupted'").fetchall()
        if not rows: QMessageBox.information(self,'Sessões','Não há sessões interrompidas.'); return
        for row in rows:
            minutes,ok = QInputDialog.getInt(self,'Recuperar sessão',row['title']+'\nInforme os minutos efetivamente jogados (0 para descartar):',0,0,100000)
            if ok: self.launcher.resolve(row['id'],minutes*60)

    def auto_backup(self,game_id):
        if self.library.setting('auto_save_'+str(game_id),False): self.game_backup(game_id)

    def game_backup(self,game_id,backup_id=None):
        if game_id in self.save_jobs:
            self.statusBar().showMessage('Já existe uma operação de saves em andamento para este jogo.'); return
        if any(item[2]==game_id for item in self.launcher.active.values()):
            QMessageBox.information(self,'Saves','Encerre o jogo e seu registro de sessão antes de operar os saves.'); return
        from .jobs import Job
        from .game_saves import run_save_operation
        path=self.library.db.path
        job=Job(lambda:run_save_operation(path,game_id,backup_id),self)
        self.save_jobs[game_id]=job
        job.succeeded.connect(lambda result:self.save_operation_done(game_id,backup_id))
        job.failed.connect(lambda message:QMessageBox.warning(self,'Saves',message))
        job.finished.connect(lambda:self.release_save_job(game_id))
        self.statusBar().showMessage('Processando saves em segundo plano…'); job.start()

    def save_operation_done(self,game_id,backup_id):
        self.statusBar().showMessage('Backup salvo.' if backup_id is None else 'Saves restaurados. A versão anterior foi preservada.')
        if self.current_game==game_id: self.detail(game_id)

    def release_save_job(self,game_id):
        job=self.save_jobs.pop(game_id); job.deleteLater()

    def restore_game_backup(self,game_id,backup):
        message='Restaurar esta versão em '+backup['directory']+'? Feche o jogo antes de continuar. Os saves existentes serão copiados antes da substituição.'
        if QMessageBox.question(self,'Restaurar saves',message)==QMessageBox.Yes: self.game_backup(game_id,backup['id'])

    def poll_sessions(self):
        for game_id in self.launcher.poll():
            self.statusBar().showMessage('Sessão encerrada e tempo salvo.'); self.auto_backup(game_id)

    def closeEvent(self,event):
        from .jobs import Job
        if any(job.isRunning() for job in self.findChildren(Job)):
            QMessageBox.information(self,'Operação em andamento','Aguarde a operação terminar antes de fechar o Checkpoint.');event.ignore();return
        if self.save_jobs:
            QMessageBox.information(self,'Saves','Aguarde a operação de saves terminar antes de fechar.'); event.ignore(); return
        if self.launcher.active:
            if QMessageBox.question(self,'Sessões ativas','Fechar o Checkpoint? O jogo continuará aberto e a sessão precisará de revisão manual.')!=QMessageBox.Yes:
                event.ignore(); return
        self.launcher.interrupt(); event.accept()

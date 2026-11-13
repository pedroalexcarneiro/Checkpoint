from .locale import count_text
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
        if library.setting('appearance.theme',DEFAULT_THEME)!=self.theme.key:library.set_setting('appearance.theme',self.theme.key)
        self.setWindowTitle('Checkpoint'); self.resize(1100,740); self.setMinimumSize(1000,700)
        from .completion_queue import CompletionQueue
        self.completion_queue=CompletionQueue(library.db.path,self)
        self.completion_queue.updated.connect(self.game_completed)
        self.completion_queue.restore_requested.connect(self.offer_restore_match)
        self.completion_queue.busy_changed.connect(self.completion_busy)
        from .task_status import TaskStatus
        self.task_status=TaskStatus(self.theme,self.completion_queue.cancel_pending)
        self.completion_bar=self.task_status.spinner;self.completion_stop=self.task_status.stop
        self.statusBar().addPermanentWidget(self.task_status)
        self.status_timer=QTimer(self);self.status_timer.setSingleShot(True);self.status_timer.setInterval(6000)
        self.status_timer.timeout.connect(self.statusBar().clearMessage)
        self.statusBar().messageChanged.connect(self.status_message_changed)
        from .price_queue import PriceQueue
        self.price_queue=PriceQueue(library,self);self.price_queue.updated.connect(self.prices_updated)
        self.hero_upgrade_attempted=set();self.description_upgrade_attempted=set();self.current_page = 0; self.current_game = None; self.last_deleted = None; self.save_jobs = {}
        root = QWidget(); root.setObjectName('root'); self.setCentralWidget(root)
        layout = QHBoxLayout(root); layout.setContentsMargins(0,0,0,0); layout.setSpacing(0)
        sidebar = QWidget(); sidebar.setObjectName('sidebar'); sidebar.setFixedWidth(198)
        nav = QVBoxLayout(sidebar); nav.setContentsMargins(10,10,10,12);nav.setSpacing(4)
        from .branding import SystemName,app_icon
        self.brand=SystemName(self.theme);nav.addWidget(self.brand);nav.addSpacing(8)
        self.setWindowIcon(app_icon(self.theme));QApplication.instance().setWindowIcon(self.windowIcon())
        self.nav_names=['home','library','wish','memories','stats','settings']
        self.nav_buttons = []
        for index,title in enumerate(PAGES):
            item = button(title,lambda checked=False,i=index:self.navigate(i)); item.setObjectName('nav'); item.setCheckable(True)
            from .ui_components import nav_icon
            item.setIcon(nav_icon(self.nav_names[index],self.theme.colors['muted']));item.setIconSize(QSize(21,21))
            self.nav_buttons.append(item)
            if index==5:
                nav.addStretch()
                divider=QFrame();divider.setObjectName('sidebarDivider');divider.setFixedHeight(1);nav.addWidget(divider);nav.addSpacing(6)
            nav.addWidget(item)
        from . import __version__
        # O divisor agrupa Configurações e perfil no rodapé da lateral.
        from .ui_components import ProfileButton
        self.profile_button=ProfileButton(self.library.setting('profile.name','Meu perfil'),self.open_profile);self.profile_button.setObjectName('profileButton');self.profile_button.setIcon(nav_icon('user',self.theme.colors['muted']));self.profile_button.setIconSize(QSize(22,22));self.profile_button.setToolTip('Perfil local e aparência');nav.addWidget(self.profile_button)
        self.profile_button.setToolTip('Perfil local · Checkpoint v'+__version__)
        self.refresh_profile()
        layout.addWidget(sidebar)
        content=QWidget();content.setObjectName('mainContent');content.setMaximumWidth(1440)
        self.host = QVBoxLayout(content); self.host.setContentsMargins(24,20,24,18); self.host.setSpacing(12)
        main_area=QWidget();main_row=QHBoxLayout(main_area);main_row.setContentsMargins(0,0,0,0);main_row.setSpacing(0)
        main_row.addWidget(content,1);layout.addWidget(main_area,1)
        self.header_widget=QWidget();self.header_widget.setFixedHeight(38);self.header = QHBoxLayout(self.header_widget);self.header.setContentsMargins(0,0,0,0); self.heading = label('','title'); self.header.addWidget(self.heading); self.header.addStretch()
        self.add_button=button('+ Adicionar jogo',self.add_library_game,True);self.header.addWidget(self.add_button); self.host.addWidget(self.header_widget)
        self.stack = QStackedWidget(); self.host.addWidget(self.stack,1)
        self.pages = []
        for _ in PAGES:
            page = QWidget(); self.pages.append(page); self.stack.addWidget(page)
        self.build_library()
        self.library_filters.removeWidget(self.search);self.search.setMinimumWidth(200);self.search.setMaximumWidth(280)
        self.search.addAction(nav_icon('search',self.theme.colors['muted']),QLineEdit.LeadingPosition)
        self.header.insertWidget(2,self.search);self.header.setSpacing(12)
        self.search.returnPressed.connect(self.search_library)
        self.library_filters.removeWidget(self.platform);self.library_options.insertWidget(1,self.platform)
        self.platform.setObjectName('libraryPlatform');self.sort.setObjectName('librarySort');self.platform.setFixedWidth(165);self.sort.setFixedWidth(145)
        from .design_system import IconButton
        self.view_buttons=[]
        for index,name in enumerate(('library','list')):
            control=IconButton(name,'Mostrar capas' if index==0 else 'Mostrar lista',lambda checked=False,i=index:self.view.setCurrentIndex(i))
            control.setCheckable(True);control.setChecked(index==self.view.currentIndex());self.header.insertWidget(3+index,control);self.view_buttons.append(control)
        self.view.currentIndexChanged.connect(self.update_view_buttons)
        self.navigate(0)
        self.timer = QTimer(self); self.timer.timeout.connect(self.poll_sessions); self.timer.start(1000)
        self.statusBar().setSizeGripEnabled(False);self.statusBar().showMessage('');self.statusBar().hide()

    def update_view_buttons(self,index):
        for i,control in enumerate(self.view_buttons):control.setChecked(i==index)

    def open_profile(self):
        from .profile_dialog import ProfileDialog
        dialog=ProfileDialog(self.library,self)
        if dialog.exec()==QDialog.Accepted:self.refresh_profile()

    def refresh_profile(self):
        from .profile_dialog import avatar_icon
        from .ui_components import nav_icon
        nickname=self.library.setting('profile.name','Meu perfil') or 'Meu perfil'
        self.profile_button.setText(nickname);self.profile_button.setToolTip(nickname)
        icon=avatar_icon(self.library.setting('profile.avatar',''),64)
        self.profile_button.setIcon(icon if not icon.isNull() else nav_icon('user',self.theme.colors['muted']))
        self.profile_button.setIconSize(QSize(28,28))

    def showEvent(self,event):
        super().showEvent(event)
        from .window_style import titlebar_theme
        titlebar_theme(self,True)

    def search_library(self):self.navigate(1)

    def add_library_game(self):
        self.navigate(1)
        self.add_game()

    def search_changed(self,value):
        if self.current_page==0 and value.strip():self.navigate(1)
        self.refresh_library()

    def guard(self,callback):
        try: return callback()
        except Exception as error:
            logging.exception('Operação falhou')
            QMessageBox.warning(self,'Checkpoint',str(error))

    def clear_page(self,index):
        old = self.pages[index];was_current=self.stack.currentWidget() is old
        self.stack.removeWidget(old); old.deleteLater()
        page = QWidget(); self.pages[index] = page; self.stack.insertWidget(index,page)
        if was_current:self.stack.setCurrentWidget(page)
        layout = QVBoxLayout(page); layout.setContentsMargins(0,0,0,0); layout.setSpacing(18)
        return layout

    def navigate(self,index):
        self.detail_notice=None
        self.current_page = index; self.current_game = None;self.header_widget.show()
        for i,b in enumerate(self.nav_buttons): b.setChecked(i==index)
        self.heading.show();self.heading.setText(PAGES[index]);self.add_button.setText('+ Adicionar jogo');self.add_button.setVisible(index in (0,1));self.search.setVisible(index in (0,1))
        for control in self.view_buttons:control.setVisible(index==1)
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
        filters = QHBoxLayout();self.library_filters=filters; self.search = QLineEdit(); self.search.setPlaceholderText('Buscar jogos…');self.search.setObjectName('headerSearch')
        self.search.textChanged.connect(self.search_changed); filters.addWidget(self.search,2)
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
        from .ui_components import nav_icon
        filter_button=QPushButton();filter_button.setIcon(nav_icon('filter',self.theme.colors['muted']));filter_button.setFixedSize(32,32);filter_button.setToolTip('Mais filtros');filter_button.setAccessibleName('Mais filtros');filter_button.setCheckable(True);filter_button.toggled.connect(self.extra_filters.setVisible);options.addWidget(filter_button)
        self.sort = QComboBox(); self.sort.addItem('Ordenar: A – Z','title'); self.sort.addItem('Mais recentes','recent'); self.sort.addItem('Maior nota','rating')
        self.sort.currentIndexChanged.connect(self.refresh_library); options.addWidget(self.sort)
        self.view = QComboBox(); self.view.addItems(['Galeria','Lista']); self.view.currentIndexChanged.connect(self.refresh_library); self.view.hide()
        layout.addLayout(options);layout.addWidget(self.extra_filters);self.extra_filters.hide()
        from .cover_grid import CoverGrid
        self.gallery=CoverGrid(self.theme,self.pages[1]);self.gallery.setIconSize(QSize(174,232))
        self.gallery.itemActivated.connect(lambda item:self.detail(item.data(Qt.UserRole)))
        self.gallery.itemClicked.connect(lambda item:self.detail(item.data(Qt.UserRole)))
        self.table = QTableWidget(0,5);self.table.setAlternatingRowColors(True);self.table.verticalHeader().hide();self.table.setShowGrid(False); self.table.setIconSize(QSize(42,56)); self.table.setHorizontalHeaderLabels(['Jogo','Plataforma','Status','Gênero','Nota'])
        self.table.horizontalHeader().setStretchLastSection(True); self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(lambda row,col:self.detail(self.table.item(row,0).data(Qt.UserRole)))
        from .ui_components import ResponsiveToolbar
        layout.removeWidget(self.library_tabs);options.setSpacing(8);options.removeWidget(self.count)
        layout.removeItem(options);options.setParent(None);controls=QWidget();controls.setLayout(options)
        layout.removeItem(filters);layout.insertWidget(0,ResponsiveToolbar(self.library_tabs,controls));self.count.hide()
        layout.setSpacing(12)
        layout.addWidget(self.gallery,1); layout.addWidget(self.table,1)
        from .design_system import empty_state
        self.library_empty=empty_state('library','Biblioteca vazia','',self.add_library_game,'Adicionar jogo');layout.addWidget(self.library_empty);self.library_empty.hide()
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
        for combo,key,caption in [(self.platform,'platform','Plataforma: Todas'),(self.genre,'genre','Todos os gêneros')]:
            selected = combo.currentData(); values = sorted({value.strip() for g in self.library.owned_games() for value in (g[key].split(',') if key=='genre' else [g[key]]) if value.strip()})
            combo.blockSignals(True); combo.clear(); combo.addItem(caption,'')
            for value in values: combo.addItem(value,value)
            index = combo.findData(selected); combo.setCurrentIndex(max(0,index)); combo.blockSignals(False)
        games = self.library.owned_games(self.search.text(),self.platform.currentData(),self.genre.currentData(),self.status.currentData(),self.favorites.isChecked(),self.sort.currentData())
        from .card_layout import cover_size
        self.gallery.theme=self.theme;self.gallery.set_cover_size(cover_size(self.library))
        self.gallery.clear(); self.table.setRowCount(len(games)); self.count.setText(count_text(len(games),'jogo'))
        for row,game in enumerate(games):
            pix = QPixmap(game['cover']) if game['cover'] else QPixmap()
            if pix.isNull():
                pix = QPixmap(174,232); pix.fill(Qt.GlobalColor.darkCyan)
                from PySide6.QtGui import QPainter,QColor,QFont
                painter = QPainter(pix); painter.fillRect(pix.rect(),QColor(self.theme.colors['selected'])); painter.setPen(QColor(self.theme.colors['accent']))
                painter.setFont(QFont('Segoe UI',15)); painter.drawText(pix.rect().adjusted(12,12,-12,-12),Qt.AlignCenter|Qt.TextWordWrap,game['title']); painter.end()
            item = QListWidgetItem(QIcon(pix),('★ ' if game['favorite'] else '')+game['title']+'\n'+game['status'])
            item.setData(Qt.UserRole,game['id']);item.setData(Qt.UserRole+1,game);self.gallery.addItem(item)
            for col,key in enumerate(['title','platform','status','genre','rating']):
                cell = QTableWidgetItem(str(game[key]) if game[key] is not None else '—'); cell.setData(Qt.UserRole,game['id']);
                if col==0: cell.setIcon(QIcon(pix))
                self.table.setItem(row,col,cell)
            self.table.setRowHeight(row,64)
        self.table.resizeColumnsToContents(); self.gallery.setVisible(bool(games) and self.view.currentIndex()==0); self.table.setVisible(bool(games) and self.view.currentIndex()==1);self.library_empty.setVisible(not games)
        if not games:self.update_library_empty()

    def clear_library_filters(self):
        for widget in (self.search,self.platform,self.genre,self.status,self.favorites,self.library_tabs):widget.blockSignals(True)
        self.search.clear()
        for combo in (self.platform,self.genre,self.status):combo.setCurrentIndex(0)
        self.favorites.setChecked(False);self.library_tabs.setCurrentIndex(0)
        for widget in (self.search,self.platform,self.genre,self.status,self.favorites,self.library_tabs):widget.blockSignals(False)
        self.refresh_library()

    def update_library_empty(self):
        owned=self.library.owned_games();tab=self.library_tabs.currentIndex()
        extra=bool(self.search.text().strip() or self.platform.currentData() or self.genre.currentData() or self.status.currentText()!=({2:'Jogando',3:'Concluído'}.get(tab,'Todos os status')))
        if not owned:title='Biblioteca vazia';caption='Adicionar jogo';callback=self.add_library_game
        elif extra:title='Nenhum resultado para esta busca';caption='Limpar filtros';callback=self.clear_library_filters
        elif tab in (1,2,3):
            title={1:'Nenhum favorito ainda',2:'Nenhum jogo em andamento',3:'Nenhum jogo concluído ainda'}[tab];caption='Ver todos os jogos';callback=self.clear_library_filters
        else:title='Nenhum resultado';caption='Limpar filtros';callback=self.clear_library_filters
        self.library_empty.findChild(QLabel,'sectionTitle').setText(title)
        action_button=self.library_empty.findChild(QPushButton);action_button.setText(caption)
        try:action_button.clicked.disconnect()
        except RuntimeError:pass
        action_button.clicked.connect(callback)

    def open_selected(self):
        if self.view.currentIndex()==0:
            item = self.gallery.currentItem()
        else:
            row = self.table.currentRow(); item = self.table.item(row,0) if row>=0 else None
        if item: self.detail(item.data(Qt.UserRole))

    def add_game(self):
        wish=self.current_page==2
        owned_before={game['id'] for game in self.library.owned_games()}
        dialog = GameDialog(self,library=self.library,purpose='wish' if wish else 'library')
        result=dialog.exec()
        if dialog.steam_requested:
            QTimer.singleShot(0,self.steam);return
        if result==QDialog.Accepted:
            def save():
                from .trash_import import save_with_prompt
                game_id=save_with_prompt(self,self.library,dialog.data(),dialog.drive_file_id,dialog.catalog_result)
                if game_id is None:return
                already_owned=wish and game_id in owned_before
                if wish and not already_owned:
                    with self.library.sql:
                        self.library.sql.execute('INSERT OR IGNORE INTO wishlist(game_id,target_cents) VALUES(?,0)',(game_id,))
                        self.library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(f'collection.unowned.{game_id}','true'))
                message='Este jogo já está na sua biblioteca.' if already_owned else 'Adicionado à lista de desejos' if wish else 'Jogo salvo na biblioteca.'
                self.detail_notice=(game_id,message) if wish else None
                self.refresh_library();self.detail(game_id)
                self.statusBar().showMessage(message)
                if dialog.complete_on_save.isChecked():
                    self.completion_queue.submit([game_id])
            self.guard(save)

    def toggle_favorite(self,game_id):
        game=self.library.get(game_id)
        if game:
            self.library.save_game({'title':game['title'],'favorite':int(not game['favorite'])},game_id)
            self.refresh_library();self.detail(game_id)

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
        self.upgrade_description(game)

    def upgrade_description(self,game):
        if not self.isVisible() or game['id'] in self.description_upgrade_attempted or not self.library.setting('artwork.auto',True):return
        from .description_provenance import current
        provenance=current(self.library,game)
        if provenance.get('language') in ('pt','pt-BR'):return
        if not self.library.sql.execute('SELECT 1 FROM external_identifiers WHERE game_id=?',(game['id'],)).fetchone():return
        self.description_upgrade_attempted.add(game['id']);self.completion_queue.submit([game['id']])

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
        from .collection_views import build_memories
        build_memories(self)

    def add_wish(self,game_id):
        if self.library.is_owned(game_id):
            self.detail_notice=(game_id,'Este jogo já está na sua biblioteca.');self.detail(game_id)
            self.statusBar().showMessage('Este jogo já está na sua biblioteca.');return
        with self.library.sql:
            self.library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(f'collection.unowned.{game_id}','true'))
            self.library.sql.execute('INSERT OR IGNORE INTO wishlist(game_id,target_cents) VALUES(?,0)',(game_id,))
        self.statusBar().showMessage('Jogo adicionado à lista de desejos.')
        self.refresh_library()
        if self.current_game==game_id:self.detail(game_id)
        elif self.current_page==2:self.wishlist()

    def prices_updated(self,game_id):
        if self.current_game==game_id:self.detail(game_id)
        elif self.current_page==2:self.wishlist()

    def wishlist(self):
        from .collection_views import build_wishlist
        build_wishlist(self)

    def remove_wish(self,game_id):
        with self.library.sql:
            self.library.sql.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(f'collection.unowned.{game_id}','true'))
            self.library.sql.execute('DELETE FROM wishlist WHERE game_id=?',(game_id,))
        self.navigate(2)

    def acquire_wish(self,game_id):
        self.library.acquire(game_id);self.refresh_library();self.detail(game_id)

    def statistics(self):
        from .statistics_view import build_statistics
        build_statistics(self)

    def settings(self):
        from .settings_view import build_settings
        build_settings(self)

    @Slot(int)
    def theme_changed(self,index):
        self.set_theme(self.theme_selector.itemData(index))

    @Slot(int)
    def settings_section_changed(self,index):self.settings_section=index

    def set_cover_size(self,percent):
        self.library.set_setting('appearance.cover_size',percent);self.gallery.set_cover_size(percent)
        from .collection_views import WishGrid
        grid=self.pages[2].findChild(WishGrid,'wishlistGrid')
        if grid:grid.cover_percent=percent;grid.reflow()

    def complete_library(self):
        ids=[row[0] for row in self.library.sql.execute('SELECT id FROM games WHERE deleted_at IS NULL')]
        if not ids:
            self.statusBar().showMessage('Nenhum jogo cadastrado.');return
        self.completion_queue.submit(ids,force=True)

    @Slot(int,int)
    def offer_restore_match(self,new_id,old_id):
        QTimer.singleShot(0,lambda:self.resolve_restore_match(new_id,old_id))

    def resolve_restore_match(self,new_id,old_id):
        from .trash_import import ask_removed,detach_removed
        game=self.library.get(new_id)
        old=self.library.sql.execute('SELECT * FROM games WHERE id=? AND deleted_at IS NOT NULL',(old_id,)).fetchone()
        if not game or not old:return
        decision=ask_removed(self,old['title'])
        if decision=='cancel':return
        def apply():
            with self.library.sql:
                if decision=='restore':
                    self.library.sql.execute('UPDATE games SET deleted_at=NULL WHERE id=?',(old_id,))
                    self.library.sql.execute('UPDATE game_files SET game_id=? WHERE game_id=?',(old_id,new_id))
                    from .library import now
                    self.library.sql.execute('UPDATE games SET deleted_at=? WHERE id=?',(now(),new_id))
                else:detach_removed(self.library,old_id)
            target=old_id if decision=='restore' else new_id
            self.refresh_library();self.detail(target)
            self.completion_queue.submit([target])
        self.guard(apply)

    @Slot(int,str)
    def game_completed(self,game_id,message):
        self.refresh_library()
        if self.current_game==game_id and self.library.get(game_id):self.detail(game_id)
        elif self.current_page==0:self.home()
        elif self.current_page==2:self.wishlist()
        self.statusBar().showMessage(message)

    @Slot(str)
    def status_message_changed(self,message):
        busy=self.completion_queue.active is not None or bool(self.completion_queue.pending)
        self.statusBar().setVisible(bool(message) or busy)
        if message:self.status_timer.start()

    @Slot(int)
    def completion_busy(self,count):
        self.task_status.set_count(count)
        self.statusBar().setVisible(count>0 or bool(self.statusBar().currentMessage()))

    def set_theme(self,key):
        from PySide6.QtWidgets import QApplication
        from .theme import apply_theme,get_theme
        key=get_theme(key).key
        self.library.set_setting('appearance.theme',key)
        self.theme=apply_theme(QApplication.instance(),key)
        from .branding import app_icon
        from .ui_components import Hero,nav_icon
        from .window_style import titlebar_theme
        titlebar_theme(self,True)
        self.refresh_profile()
        self.brand.set_theme(self.theme);self.setWindowIcon(app_icon(self.theme));QApplication.instance().setWindowIcon(self.windowIcon())
        for item,name in zip(self.nav_buttons,self.nav_names):item.setIcon(nav_icon(name,self.theme.colors['muted']))
        for hero in self.findChildren(Hero):hero.set_theme(self.theme)
        self.completion_bar.theme=self.theme;self.completion_bar.update()
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
        key = {'Google Drive':'drive-readonly','RAWG':'rawg','SteamGridDB':'steamgriddb','Steam':'steam','GG.deals':'ggdeals'}.get(provider)
        if not key: return 'Provedor ainda não implementado'
        try:
            from .credentials import CredentialVault
            vault=getattr(self,'ggdeals_vault_factory',CredentialVault)() if provider=='GG.deals' else CredentialVault()
            return 'Credencial salva · conexão não verificada' if vault.get(key) else 'Não configurada'
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
        path,_ = QFileDialog.getSaveFileName(self,'Backup do banco','checkpoint-backup.sqlite','SQLite (*.sqlite)')
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
        self.price_queue.stop();self.timer.stop();self.status_timer.stop();self.launcher.interrupt();event.accept()

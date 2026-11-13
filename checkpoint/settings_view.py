"""Configurações em quatro áreas compactas e consistentes com a biblioteca."""
from pathlib import Path
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QTabWidget,QComboBox,QToolButton,QMessageBox,QLineEdit,QCheckBox,QSizePolicy
from .ui_components import text,action,card,service_icon
from .design_system import page_scroll,ThemeSwatch,Badge,CardGrid
from .theme import THEMES


class DisclosureButton(QToolButton):
    def __init__(self,title,parent=None):
        super().__init__(parent);self.setText(title);self.setCheckable(True);self.setObjectName('disclosure');self.setMinimumHeight(44);self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon);self.setArrowType(Qt.RightArrow)
        self.toggled.connect(self.indicate)
    def indicate(self,expanded):self.setArrowType(Qt.DownArrow if expanded else Qt.RightArrow)


def disclosure(title,content,parent_layout):
    toggle=DisclosureButton(title);toggle.toggled.connect(content.setVisible)
    parent_layout.addWidget(toggle);parent_layout.addWidget(content);content.hide();return toggle


def folder_row(window,key,title):
    frame,inside=card();row=QHBoxLayout();row.setSpacing(14);row.addWidget(Badge('folder'))
    words=QVBoxLayout();words.addWidget(text(title,'cardTitle'));path=window.library.setting(key,'')
    label=text(Path(path).name if path else 'Pasta não definida','muted');label.setToolTip(path);words.addWidget(label);row.addLayout(words,1)
    row.addWidget(action('Selecionar pasta',lambda checked=False:window.choose_directory(key)));inside.addLayout(row);return frame


def build_settings(window):
    layout=window.clear_page(5);tabs=QTabWidget();tabs.setObjectName('settingsTabs');window.settings_tabs=tabs;pages=[]
    for name in ('Aparência','Conexões','Downloads','Dados e backup'):
        page=QWidget();outer=QVBoxLayout(page);outer.setContentsMargins(0,18,0,0);pages.append(page_scroll(outer));tabs.addTab(page,name)
    appearance,connections,downloads,data=pages
    frame,inside=card();head=QHBoxLayout();head.addWidget(text('Tema de cores','sectionTitle'));head.addStretch();window.theme_selector=QComboBox();window.theme_selector.setObjectName('themeSelector')
    for key,theme in THEMES.items():window.theme_selector.addItem(theme.name,key)
    window.theme_selector.setCurrentIndex(window.theme_selector.findData(window.theme.key));window.theme_selector.currentIndexChanged.connect(window.theme_changed);head.addWidget(window.theme_selector);inside.addLayout(head)
    swatches=QHBoxLayout();swatches.setSpacing(10)
    for key,theme in THEMES.items():swatches.addWidget(ThemeSwatch(theme,lambda checked=False,k=key:window.theme_selector.setCurrentIndex(window.theme_selector.findData(k))))
    swatches.addStretch();inside.addLayout(swatches)
    row=QHBoxLayout();row.addWidget(text('Densidade da biblioteca','muted'));row.addStretch();density=QComboBox();density.addItem('Confortável','comfortable');density.addItem('Compacta','compact');density.setCurrentIndex(max(0,density.findData(window.library.setting('appearance.density','comfortable'))));density.currentIndexChanged.connect(lambda index:window.set_density(density.itemData(index)));row.addWidget(density);inside.addLayout(row)
    appearance.addWidget(frame);appearance.addStretch()
    grid=CardGrid(320,max_columns=2);grid.setObjectName('connectionsGrid')
    for provider,callback in [('Steam',window.steam),('Google Drive',window.drive),('SteamGridDB',lambda:window.configure_key('steamgriddb')),('RAWG',lambda:window.configure_key('rawg'))]:
        frame,inside=card();head=QHBoxLayout();badge=text('');badge.setPixmap(service_icon(provider));badge.setFixedSize(48,48);head.addWidget(badge)
        words=QVBoxLayout();words.addWidget(text(provider,'cardTitle'));configured=window.integration_status(provider).startswith('Credencial salva');state=QHBoxLayout();dot=text('●');dot.setObjectName('connectionStateDot');dot.setFixedWidth(12);dot.setProperty('configured',configured)
        from .theme import get_theme
        dot.setStyleSheet('color: '+(get_theme('green').colors['accent'] if configured else window.theme.colors['muted']));state.addWidget(dot);state.addWidget(text('Configurado' if configured else 'Não configurado','muted'));state.addStretch();words.addLayout(state);head.addLayout(words,1);head.setSpacing(18);head.addWidget(action('Gerenciar' if configured else 'Conectar',callback,not configured));inside.addLayout(head);inside.setContentsMargins(18,16,18,16);grid.add_card(frame)
    connections.addWidget(grid)
    from .design_system import IconButton
    help_row=QHBoxLayout();help_row.addStretch();help_button=IconButton('help','Ajuda sobre conexões',lambda:QMessageBox.information(window,'Conexões','Configurado indica uma credencial salva. Use Gerenciar para verificar o acesso.'));help_row.addWidget(help_button);connections.insertLayout(0,help_row)
    extra=QWidget();inside=QVBoxLayout(extra);inside.setContentsMargins(0,0,0,0);inside.addWidget(action('Completar fichas e imagens da biblioteca',window.complete_library));inside.addWidget(action('Pesquisar metadados manualmente',window.metadata))
    prices=QCheckBox('Consultar preços do GG.deals automaticamente');prices.setChecked(window.library.setting('prices.auto',True));prices.toggled.connect(lambda value:window.library.set_setting('prices.auto',value));inside.addWidget(prices)
    disclosure('Avançado',extra,connections);connections.addStretch()
    for key,title in [('downloads','ROMs baixadas'),('captures','Capturas'),('save_backups','Backups de saves')]:downloads.addWidget(folder_row(window,key,title))
    downloads.addStretch()
    grid=CardGrid(330)
    for title,description,name,actions in [('Biblioteca','Seu banco de jogos e suas preferências.','library',[('Criar backup',window.backup_database),('Abrir pasta de dados',lambda:QDesktopServices.openUrl(QUrl.fromLocalFile(str(window.library.db.path.parent.resolve()))))]),('Saves tradicionais','Cópias de segurança dos saves configurados.','folder',[('Criar backup',window.backup_saves),('Restaurar saves',window.restore_saves)])]:
        frame,inside=card();head=QHBoxLayout();head.addWidget(Badge(name));head.addWidget(text(title,'cardTitle'),1);inside.addLayout(head)
        row=QHBoxLayout()
        for caption,callback in actions:row.addWidget(action(caption,callback))
        inside.addLayout(row);grid.add_card(frame)
    data.addWidget(grid);update=action('Verificar atualizações',window.updates);update.setObjectName('quiet');data.addWidget(update,0,Qt.AlignLeft)
    extra=QWidget();inside=QVBoxLayout(extra);inside.addWidget(action('Perfis de emuladores',window.emulators));inside.addWidget(action('Revisar sessões interrompidas',window.recover_sessions));disclosure('Avançado',extra,data)
    removed=window.library.sql.execute('SELECT id,title FROM games WHERE deleted_at IS NOT NULL ORDER BY title').fetchall();trash=QWidget();inside=QVBoxLayout(trash)
    if not removed:inside.addWidget(text('A lixeira está vazia.','muted'))
    for game in removed:
        line=QHBoxLayout();line.addWidget(text(game['title']),1);line.addWidget(action('Restaurar',lambda checked=False,g=game['id']:window.restore_game(g)));inside.addLayout(line)
    disclosure(f'Lixeira · {len(removed)} jogos',trash,data)
    archived=[game for game in window.library.games() if not window.library.is_owned(game['id']) and not window.library.sql.execute('SELECT 1 FROM wishlist WHERE game_id=?',(game['id'],)).fetchone()]
    if archived:
        archive=QWidget();inside=QVBoxLayout(archive)
        for game in archived:
            line=QHBoxLayout();line.addWidget(text(game['title']),1);line.addWidget(action('Adicionar à biblioteca',lambda checked=False,g=game['id']:window.acquire_wish(g)));inside.addLayout(line)
        disclosure(f'Desejos removidos · {len(archived)} jogos',archive,data)
    data.addStretch()
    tabs.setCurrentIndex(min(getattr(window,'settings_section',0),3));tabs.currentChanged.connect(window.settings_section_changed);layout.addWidget(tabs)

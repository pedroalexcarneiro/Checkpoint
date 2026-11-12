"""Configurações compactas, com ajuda e detalhes apenas sob demanda."""
from pathlib import Path
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QTabWidget,QComboBox,QToolButton,QMessageBox,QCheckBox,QScrollArea
from .ui_components import text,action,card
from .theme import THEMES


class DisclosureButton(QToolButton):
    def __init__(self,title,parent=None):
        super().__init__(parent);self.setText(title);self.setCheckable(True)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon);self.setArrowType(Qt.RightArrow)
        self.toggled.connect(self.indicate)
    def indicate(self,expanded):self.setArrowType(Qt.DownArrow if expanded else Qt.RightArrow)


def disclosure(title,content,parent_layout):
    toggle=DisclosureButton(title)
    toggle.toggled.connect(content.setVisible);parent_layout.addWidget(toggle);parent_layout.addWidget(content);content.hide()
    return toggle


def build_settings(window):
    layout=window.clear_page(5)
    tabs=QTabWidget();tabs.setObjectName('settingsTabs');window.settings_tabs=tabs
    pages=[]
    for name in ('Aparência','Conexões','Downloads','Dados e backup'):
        scroll=QScrollArea();scroll.setWidgetResizable(True)
        body=QWidget();inside=QVBoxLayout(body);inside.setContentsMargins(4,22,8,12);inside.setSpacing(18);scroll.setWidget(body);tabs.addTab(scroll,name);pages.append(inside)
    appearance,connections,downloads,data=pages
    frame,inside=card();inside.addWidget(text('Personalize seu espaço','sectionTitle'))
    row=QHBoxLayout();row.addWidget(text('Tema'));row.addStretch()
    window.theme_selector=QComboBox();window.theme_selector.setObjectName('themeSelector')
    for key,theme in THEMES.items():window.theme_selector.addItem(theme.name,key)
    window.theme_selector.setCurrentIndex(window.theme_selector.findData(window.theme.key))
    window.theme_selector.currentIndexChanged.connect(window.theme_changed);row.addWidget(window.theme_selector);inside.addLayout(row)
    density=QHBoxLayout();density.addWidget(text('Capas da biblioteca'));density.addStretch();selector=QComboBox();selector.addItem('Confortável', 'comfortable');selector.addItem('Compacta','compact')
    selector.setCurrentIndex(max(0,selector.findData(window.library.setting('appearance.density','comfortable'))));selector.currentIndexChanged.connect(lambda index:window.set_density(selector.itemData(index)));density.addWidget(selector);inside.addLayout(density);appearance.addWidget(frame)
    appearance.addWidget(text('As cores se adaptam à navegação, aos botões e à identidade do aplicativo.','muted'));appearance.addStretch()
    grid=QGridLayout();grid.setSpacing(16)
    for index,(provider,short,callback) in enumerate([('Steam','S',window.steam),('Google Drive','D',window.drive),('SteamGridDB','SG',lambda:window.configure_key('steamgriddb')),('RAWG','R',lambda:window.configure_key('rawg'))]):
        frame,inside=card();row=QHBoxLayout();badge=text(short,'serviceBadge');badge.setAlignment(Qt.AlignCenter);badge.setFixedSize(42,42);row.addWidget(badge)
        names=QVBoxLayout();names.addWidget(text(provider,'sectionTitle'));status=window.integration_status(provider);configured=status.startswith('Credencial salva')
        names.addWidget(text('Configurado' if configured else 'Não configurado','muted'));row.addLayout(names,1);row.addWidget(action('Gerenciar' if configured else 'Configurar',callback));inside.addLayout(row);grid.addWidget(frame,index//2,index%2)
    connections.addLayout(grid)
    help_button=action('Sobre as conexões',lambda:QMessageBox.information(window,'Conexões','Configurado indica uma credencial salva. Use Gerenciar para consultar o serviço e verificar o acesso. Chaves ficam no cofre do Windows.'))
    help_button.setObjectName('quiet');connections.addWidget(help_button)
    extra=QWidget();extra_layout=QVBoxLayout(extra);extra_layout.addWidget(action('Completar fichas e imagens da biblioteca',window.complete_library));extra_layout.addWidget(action('Pesquisar metadados manualmente',window.metadata));disclosure('Avançado',extra,connections);connections.addStretch()
    for key,title in [('downloads','ROMs baixadas'),('captures','Capturas'),('save_backups','Backups de saves')]:
        frame,inside=card();row=QHBoxLayout();names=QVBoxLayout();names.addWidget(text(title,'sectionTitle'));path=window.library.setting(key,'');caption=text(Path(path).name if path else 'Pasta não definida','muted');caption.setToolTip(path);names.addWidget(caption);row.addLayout(names,1);row.addWidget(action('Selecionar pasta',lambda checked=False,k=key:window.choose_directory(k)));inside.addLayout(row);downloads.addWidget(frame)
    downloads.addWidget(text('As ROMs são baixadas somente quando você solicita.','muted'));downloads.addStretch()
    frame,inside=card();inside.addWidget(text('Sua biblioteca','sectionTitle'));row=QHBoxLayout();row.addWidget(action('Criar backup do banco',window.backup_database));row.addWidget(action('Atualizações',window.updates));inside.addLayout(row)
    folder=action('Abrir pasta de dados',lambda:QDesktopServices.openUrl(QUrl.fromLocalFile(str(window.library.db.path.parent.resolve()))));inside.addWidget(folder);data.addWidget(frame)
    frame,inside=card();inside.addWidget(text('Saves tradicionais','sectionTitle'));row=QHBoxLayout();row.addWidget(action('Criar backup de saves',window.backup_saves));row.addWidget(action('Restaurar saves',window.restore_saves));inside.addLayout(row);data.addWidget(frame)
    advanced=QWidget();inside=QVBoxLayout(advanced);inside.addWidget(action('Perfis de emuladores',window.emulators));inside.addWidget(action('Revisar sessões interrompidas',window.recover_sessions));disclosure('Avançado',advanced,data)
    removed=window.library.sql.execute('SELECT id,title FROM games WHERE deleted_at IS NOT NULL ORDER BY title').fetchall()
    trash=QWidget();trash_layout=QVBoxLayout(trash)
    if not removed:trash_layout.addWidget(text('A lixeira está vazia.','muted'))
    for game in removed:trash_layout.addWidget(action('Restaurar '+game['title'],lambda checked=False,g=game['id']:window.restore_game(g)))
    disclosure(f'Lixeira · {len(removed)} jogos',trash,data);data.addStretch()
    tabs.setCurrentIndex(min(getattr(window,'settings_section',0),3));tabs.currentChanged.connect(window.settings_section_changed)
    layout.addWidget(tabs)

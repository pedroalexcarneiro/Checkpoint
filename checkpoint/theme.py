"""Paletas discretas e completas para as superfícies e estados do aplicativo."""
from dataclasses import dataclass
from PySide6.QtGui import QColor,QPalette

@dataclass(frozen=True)
class Theme:
    key: str
    name: str
    colors: dict

def blend(base,tint,amount):
    values=[round(int(base[i:i+2],16)*(1-amount)+int(tint[i:i+2],16)*amount) for i in (1,3,5)]
    return '#'+''.join(f'{v:02x}' for v in values)

def dark_theme(key,name,accent):
    background='#0e141d';surface='#151e29';elevated='#202c3a';card='#192330'
    return Theme(key,name,{
        'background':background,'sidebar':'#101821','surface':surface,
        'elevated':elevated,'card':card,'panel':card,'input':'#101923',
        'button':elevated,'hover':blend(elevated,accent,.10),
        'border':'#344456','border_subtle':'#2a394a',
        'text':'#f0f4f8','secondary':'#becad7','muted':'#a4b4c6',
        'accent':accent,'on_accent':'#111b22','selected':blend(surface,accent,.18),
        'success':'#a1dfb5','alert':'#efd090','error':'#f0b0b8','disabled':'#899aad'})


THEMES={theme.key:theme for theme in [
    dark_theme('blue','Azul','#a3b8cf'),
    dark_theme('green','Verde','#a6df8d'),
    dark_theme('yellow','Amarelo','#c7ba91'),
    dark_theme('red','Vermelho','#cba3a0'),
    dark_theme('black','Preto','#b6b8bc'),
    dark_theme('purple','Roxo','#b7a9ca'),
    dark_theme('pink','Rosa','#e6abc9'),
    dark_theme('orange','Laranja','#cbb195'),
    dark_theme('cyan','Ciano','#9cbfc3'),
]}
DEFAULT_THEME='green'

def get_theme(key): return THEMES.get(key,THEMES[DEFAULT_THEME]) if isinstance(key,str) else THEMES[DEFAULT_THEME]

def stylesheet(key):
    c=get_theme(key).colors
    from .visual_tokens import TYPE,SPACE,RADIUS
    return f"""
* {{ font-family: 'Segoe UI'; font-size: {TYPE['body']}px; }}
QMainWindow, QDialog {{ background: {c['background']}; color: {c['text']}; }}
QWidget {{ color: {c['text']}; }}
QWidget#root {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {blend(c['background'],c['panel'],.35)},stop:.6 {c['background']},stop:1 {blend(c['background'],c['accent'],.025)}); }}
QWidget#sidebar {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 {c['sidebar']},stop:1 {blend(c['sidebar'],c['background'],.45)}); border-right: 1px solid {blend(c['border'],c['background'],.42)}; }}
QFrame#sidebarDivider {{ background: {c['border']}; border: none; max-height: 1px; }}
QLabel#title, QLabel#pageTitle {{ font-size: {TYPE['title']}px; font-weight: 600; }}
QLabel#sectionTitle {{ font-size: {TYPE['section']}px; font-weight: 600; }}
QLabel#cardTitle {{ font-size: {TYPE['card']}px; font-weight: 600; }}
QLabel#bodyText {{ font-size: 14px; }}
QLabel#muted {{ color: {c['muted']}; font-size: 13px; }}
QLabel#caption, QLabel#eyebrow {{ color: {c['muted']}; font-size: 12px; }}
QLabel#error {{ color: {c['error']}; }}
QLabel#metricValue {{ font-size: 30px; font-weight: 600; }}
QLabel#activityKind {{ color: {c['text']}; font-size: 12px; font-weight: 600; }}
QPushButton, QToolButton {{ background: {c['button']}; border: 1px solid {blend(c['border'],c['button'],.3)}; border-radius: {RADIUS['button']}px; padding: 8px 14px; }}
QPushButton:hover, QToolButton:hover {{ background: {c['hover']}; border-color: {blend(c['accent'],c['background'],.45)}; }}
QPushButton:focus, QToolButton:focus, QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QSpinBox:focus {{ border: 1px solid {c['accent']}; }}
QPushButton#primary {{ background: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 {blend(c['accent'],c['on_accent'],.025)},stop:1 {c['accent']}); color: {c['on_accent']}; font-weight: 600; border: 1px solid {c['accent']}; }}
QPushButton#primary:hover {{ background: {blend(c['accent'],c['text'],.12)}; }}
QPushButton:disabled, QPushButton#primary:disabled, QToolButton:disabled {{ background: {c['button']}; color: {c['disabled']}; border-color: {c['border']}; }}
QPushButton#quiet, QPushButton#activityLink {{ background: transparent; border: none; color: {c['muted']}; padding: 3px 0; text-align: left; }}
QPushButton#quiet:hover {{ color: {c['text']}; }}
QPushButton#activityLink {{ color: {c['text']}; font-weight: 600; }}
QPushButton#activityLink:hover {{ color: {c['accent']}; }}
QPushButton#nav {{ background: transparent; border: none; padding: 8px 12px; color: {c['muted']}; text-align: left; border-radius: {RADIUS['button']}px; }}
QPushButton#nav:hover {{ background: {blend(c['sidebar'],c['accent'],.065)}; color: {c['text']}; }}
QPushButton#nav:checked {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 {blend(c['sidebar'],c['accent'],.25)},stop:1 {blend(c['sidebar'],c['accent'],.14)}); color: {c['text']}; }}
QPushButton#profileButton {{ background: transparent; border: none; padding: 12px 10px; text-align: left; }}
QPushButton#profileButton:hover {{ background: {c['selected']}; }}
QPushButton#iconButton {{ background: transparent; border: 1px solid transparent; padding: 0; }}
QPushButton#iconButton:checked {{ background: {c['selected']}; border-color: {c['border']}; }}
QPushButton#iconButton:hover {{ background: {c['selected']}; border-color: {c['border']}; }}
QPushButton#heroBack {{ background: rgba(15,18,22,160); color: #ffffff; border: none; border-radius: 16px; padding: 0; }}
QLineEdit, QTextEdit, QComboBox, QSpinBox, QListWidget, QTableWidget {{ background: {c['input']}; border: 1px solid {c['border']}; border-radius: {RADIUS['button']}px; padding: 7px 10px; selection-background-color: {c['selected']}; selection-color: {c['text']}; }}
QLineEdit#headerSearch {{ background: {blend(c['input'],c['panel'],.4)}; border-radius: 8px; padding: 7px 14px; font-size: 13px; }}
QLineEdit#gameSearch {{ font-size: 16px; padding: 10px 16px; border-radius: 9px; }}
QComboBox {{ padding-right: 22px; }}
QComboBox#libraryPlatform, QComboBox#librarySort {{ font-size: 12px; padding: 6px 22px 6px 9px; }}
QComboBox::drop-down {{ border: none; width: 25px; }}
QComboBox QAbstractItemView {{ background: {c['panel']}; color: {c['text']}; selection-background-color: {c['selected']}; padding: 5px; }}
QAbstractItemView {{ outline: none; }}
QTableWidget {{ gridline-color: {blend(c['border'],c['input'],.4)}; alternate-background-color: {c['panel']}; }}
QTableWidget::item {{ padding: 8px; border-bottom: 1px solid {blend(c['border'],c['input'],.5)}; }}
QTableWidget::item:selected {{ background: {c['selected']}; }}
QHeaderView::section {{ background: {c['panel']}; color: {c['muted']}; border: none; padding: 10px 12px; font-size: 12px; }}
QListWidget::item {{ padding: 6px; border-radius: 6px; }}
QListWidget::item:selected {{ background: {c['selected']}; color: {c['text']}; }}
QListWidget::item:hover {{ background: {c['hover']}; }}
QListWidget#coverGrid {{ background: transparent; border: none; padding: 0; }}
QListWidget#coverGrid::item {{ padding: 0; margin: 0; border: none; background: transparent; }}
QListWidget#gameSearchResults {{ background: transparent; border: none; padding: 0; }}
QListWidget#gameSearchResults::item {{ background: {c['panel']}; border: 1px solid transparent; border-radius: 8px; padding: 9px 12px; }}
QListWidget#gameSearchResults::item:selected {{ background: {c['selected']}; border-color: {c['accent']}; }}
QFrame#panel, QFrame#ggdealsConnection, QFrame#activityCard, QFrame#addPreview, QFrame#emptyState {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {blend(c['panel'],c['text'],.016)},stop:1 {c['panel']}); border: 1px solid {blend(c['border'],c['panel'],.36)}; border-radius: {RADIUS['card']}px; }}
QFrame#emptyState {{ border: 1px dashed {c['border']}; }}
QToolButton#disclosure {{ background: transparent; border: none; border-top: 1px solid {c['border']}; border-bottom: 1px solid {c['border']}; border-radius: 0; padding: 10px 12px; text-align: left; }}
QLabel#iconBadge, QLabel#activityBadge, QLabel#serviceBadge {{ background: {c['selected']}; border-radius: 12px; }}
QLabel#connectionDot {{ color: {c['accent']}; }}
QWidget#detailGallery {{ border-left: 1px solid {c['border']}; }}
QWidget#gameActions {{ background: {c['panel']}; border: 1px solid {blend(c['border'],c['panel'],.5)}; border-radius: 9px; }}
QLabel#addPreviewArt {{ background: transparent; color: {c['muted']}; }}
QPushButton#wishOpen {{ background: transparent; border: none; padding: 0; font-size: 12px; color: {c['muted']}; text-align: center; }}
QPushButton#wishOpen:hover {{ color: {c['accent']}; }}
QPushButton#wishLogo, QPushButton#gameTile, QPushButton#artworkButton {{ background: transparent; border: none; padding: 0; }}
QTabWidget::pane {{ background: transparent; border: none; }}
QTabBar::tab {{ background: transparent; color: {c['muted']}; padding: 12px 15px; border-bottom: 2px solid transparent; }}
QTabBar::tab:selected {{ color: {c['text']}; border-bottom-color: {c['accent']}; }}
QTabBar::tab:hover {{ color: {c['text']}; background: {blend(c['panel'],c['accent'],.035)}; }}
QTabBar#libraryTabs {{ background: {c['panel']}; border: 1px solid {blend(c['border'],c['panel'],.4)}; border-radius: 8px; }}
QTabBar#libraryTabs::tab {{ padding: 6px 12px; margin: 0; border: none; border-radius: 6px; }}
QTabBar#libraryTabs::tab:selected {{ background: {c['accent']}; color: {c['on_accent']}; }}
QTabWidget#settingsTabs QTabBar::tab {{ padding: {SPACE['xs']}px {SPACE['md']}px; font-size: {TYPE['body']}px; }}
QTabWidget#settingsTabs QTabBar::tab:selected {{ color: {c['accent']}; font-weight: 600; }}
QDialog#quickAddDialog {{ background: {c['surface']}; border: 1px solid {c['border']}; }}
QWidget#dialogTitleBar QLabel#pageTitle {{ font-size: 24px; }}
QFrame#addPreview {{ background: {c['elevated']}; border-color: {c['border']}; }}
QTabBar#sourceTabs {{ border: 1px solid {c['border']}; border-radius: 8px; }}
QTabBar#sourceTabs::tab {{ padding: 9px 14px; border: none; border-right: 1px solid {c['border']}; color: {c['text']}; }}
QTabBar#sourceTabs::tab:selected {{ background: {c['selected']}; border: 1px solid {c['accent']}; border-radius: {RADIUS['button']}px; }}
QPushButton#resultLink {{ background: transparent; border: none; color: {c['accent']}; text-decoration: underline; padding: 0; }}
QLabel#selectedCheck {{ background: {c['accent']}; color: {c['on_accent']}; border-radius: 14px; font-size: 20px; }}
QLabel#discountBadge {{ background: {c['selected']}; color: {c['accent']}; border-radius: 4px; font-size: 12px; font-weight: 600; padding: 2px 6px; }}
QSlider::groove:horizontal {{ height: 4px; border: none; border-radius: 2px; background: {c['input']}; }}
QSlider::sub-page:horizontal {{ background: {c['accent']}; border-radius: 2px; }}
QSlider::handle:horizontal {{ width: 14px; margin: -5px 0; border-radius: {RADIUS['button']}px; background: {c['accent']}; }}
QScrollBar::handle:disabled {{ background: transparent; }}
QToolButton#addDisclosure {{ background: transparent; border: none; border-top: 1px solid {c['border']}; border-bottom: 1px solid {c['border']}; border-radius: 0; padding: 12px 0; text-align: left; }}
QScrollArea, QScrollArea > QWidget > QWidget {{ background: transparent; border: none; }}
QScrollBar:vertical {{ background: transparent; width: 6px; margin: 2px 0; }}
QScrollBar:horizontal {{ background: transparent; height: 6px; margin: 0 2px; }}
QScrollBar::handle {{ background: {c['accent']}; border-radius: 3px; min-height: 24px; min-width: 24px; }}
QScrollBar::handle:hover {{ background: {c['muted']}; }}
QScrollBar::add-line, QScrollBar::sub-line {{ height: 0; width: 0; }}
QScrollBar::add-page, QScrollBar::sub-page {{ background: transparent; }}
QToolButton::menu-indicator {{ image: none; width: 0; height: 0; }}
QMenu {{ background: {c['panel']}; color: {c['text']}; border: 1px solid {c['border']}; padding: 6px; }}
QMenu::item {{ padding: 9px 20px; border-radius: 5px; }}
QMenu::item:selected {{ background: {c['selected']}; }}
QCheckBox {{ spacing: 8px; padding: 4px 0; }}
QCheckBox::indicator {{ width: 15px; height: 15px; background: {c['input']}; border: 1px solid {c['muted']}; border-radius: 4px; }}
QCheckBox::indicator:checked {{ background: {c['accent']}; border: 2px solid {c['on_accent']}; }}
QCheckBox:disabled {{ color: {c['disabled']}; }}
QGroupBox {{ border: 1px solid {c['border']}; border-radius: 8px; margin-top: 16px; padding: 12px; }}
QGroupBox::title {{ color: {c['muted']}; subcontrol-origin: margin; padding: 0 5px; }}
QProgressBar {{ background: {c['button']}; border: none; border-radius: 3px; max-height: 6px; text-align: center; }}
QProgressBar::chunk {{ background: {c['accent']}; border-radius: 3px; }}
QToolTip {{ background: {c['panel']}; color: {c['text']}; border: 1px solid {c['border']}; padding: 6px; }}
QStatusBar {{ background: {c['background']}; color: {c['muted']}; font-size: 12px; }}
QStatusBar::item {{ border: none; }}
QFrame[component="card"] {{ background: {c['card']}; border: 1px solid {c['border_subtle']}; border-radius: {RADIUS['card']}px; }}
QFrame[component="card"]:hover {{ border-color: {c['border']}; }}
QLabel#secondary {{ color: {c['secondary']}; }}
QLabel#priceValue {{ font-size: 24px; font-weight: 600; color: {c['text']}; }}
QLabel#statusChip {{ color: {c['secondary']}; background: {c['selected']}; border: 1px solid {c['border_subtle']}; border-radius: {RADIUS['button']}px; padding: 4px 8px; font-size: 12px; }}
QLabel#statusChip[active="true"] {{ color: {c['accent']}; }}
QPushButton[variant="ghost"] {{ background: transparent; border-color: transparent; color: {c['secondary']}; }}
QPushButton[variant="ghost"]:hover {{ background: {c['elevated']}; color: {c['text']}; }}
QLabel#emptyDescription {{ color: {c['secondary']}; font-size: 14px; }}
QFrame#emptyState {{ background: {c['surface']}; border: 1px solid {c['border_subtle']}; border-radius: {RADIUS['card']}px; }}
QFrame#activityCard {{ background: {c['card']}; border: 1px solid {c['border_subtle']}; border-radius: {RADIUS['card']}px; }}
QLabel#eyebrow {{ color: {c['accent']}; font-size: 12px; font-weight: 600; }}
QWidget#gameActions {{ background: {c['elevated']}; border-color: {c['border_subtle']}; border-radius: {RADIUS['card']}px; }}
QWidget#taskStatus QToolButton {{ padding: 0; border: none; background: transparent; }}
"""


def apply_theme(application,key):
    theme=get_theme(key); c=theme.colors; palette=QPalette()
    roles={'Window':'background','WindowText':'text','Base':'input','AlternateBase':'selected',
           'Text':'text','Button':'button','ButtonText':'text','Highlight':'accent','HighlightedText':'on_accent',
           'ToolTipBase':'panel','ToolTipText':'text','PlaceholderText':'muted','Link':'accent'}
    for role,color in roles.items(): palette.setColor(getattr(QPalette.ColorRole,role),QColor(c[color]))
    for role in [QPalette.ColorRole.Text,QPalette.ColorRole.ButtonText,QPalette.ColorRole.WindowText]:
        palette.setColor(QPalette.ColorGroup.Disabled,role,QColor(c['disabled']))
    application.setPalette(palette); application.setStyleSheet(stylesheet(theme.key)); application.setProperty('checkpointTheme',theme.key)
    return theme

# Compatibilidade com ferramentas e testes que importavam o tema padrão.
DARK=stylesheet(DEFAULT_THEME)

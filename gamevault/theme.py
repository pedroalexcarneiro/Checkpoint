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
    return Theme(key,name,{
        'background':'#191b1d','sidebar':'#17191b',
        'panel':'#24272a','input':'#202326',
        'button':'#2c3033','hover':blend('#303438',accent,.08),
        'border':'#3c4145','text':'#e8eaed','muted':'#abb3bd',
        'accent':accent,'on_accent':'#152027','selected':blend('#242b32',accent,.16),
        'error':'#e2b3ad','disabled':'#7c858f'})

THEMES={theme.key:theme for theme in [
    dark_theme('blue','Azul','#a3b8cf'),
    dark_theme('green','Verde','#a1d38e'),
    dark_theme('yellow','Amarelo','#c7ba91'),
    dark_theme('red','Vermelho','#cba3a0'),
    dark_theme('black','Preto','#b6b8bc'),
    dark_theme('purple','Roxo','#b7a9ca'),
    dark_theme('pink','Rosa','#c6a8b9'),
    dark_theme('orange','Laranja','#cbb195'),
    dark_theme('cyan','Ciano','#9cbfc3'),
]}
DEFAULT_THEME='green'

def get_theme(key): return THEMES.get(key,THEMES[DEFAULT_THEME]) if isinstance(key,str) else THEMES[DEFAULT_THEME]

def stylesheet(key):
    c=get_theme(key).colors
    return f"""
* {{ font-family: 'Segoe UI'; font-size: 14px; }}
QMainWindow, QDialog {{ background: {c['background']}; color: {c['text']}; }}
QWidget {{ color: {c['text']}; }}
QWidget#root {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {blend(c['background'],c['panel'],.35)},stop:.6 {c['background']},stop:1 {blend(c['background'],c['accent'],.025)}); }}
QWidget#sidebar {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 {c['sidebar']},stop:1 {blend(c['sidebar'],c['background'],.45)}); border-right: 1px solid {blend(c['border'],c['background'],.42)}; }}
QFrame#sidebarDivider {{ background: {c['border']}; border: none; max-height: 1px; }}
QLabel#title, QLabel#pageTitle {{ font-size: 28px; font-weight: 650; }}
QLabel#sectionTitle {{ font-size: 18px; font-weight: 600; }}
QLabel#cardTitle {{ font-size: 15px; font-weight: 600; }}
QLabel#bodyText {{ font-size: 14px; }}
QLabel#muted {{ color: {c['muted']}; font-size: 13px; }}
QLabel#caption, QLabel#eyebrow {{ color: {c['muted']}; font-size: 12px; }}
QLabel#error {{ color: {c['error']}; }}
QLabel#metricValue {{ font-size: 30px; font-weight: 600; }}
QLabel#activityKind {{ color: {c['text']}; font-size: 12px; font-weight: 600; }}
QPushButton, QToolButton {{ background: {c['button']}; border: 1px solid {blend(c['border'],c['button'],.3)}; border-radius: 7px; padding: 8px 14px; }}
QPushButton:hover, QToolButton:hover {{ background: {c['hover']}; border-color: {blend(c['accent'],c['background'],.45)}; }}
QPushButton:focus, QToolButton:focus, QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QSpinBox:focus {{ border: 1px solid {c['accent']}; }}
QPushButton#primary {{ background: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 {blend(c['accent'],c['on_accent'],.025)},stop:1 {c['accent']}); color: {c['on_accent']}; font-weight: 600; border: 1px solid {c['accent']}; }}
QPushButton#primary:hover {{ background: {blend(c['accent'],c['text'],.12)}; }}
QPushButton:disabled, QPushButton#primary:disabled, QToolButton:disabled {{ background: {c['button']}; color: {c['disabled']}; border-color: {c['border']}; }}
QPushButton#quiet, QPushButton#activityLink {{ background: transparent; border: none; color: {c['muted']}; padding: 3px 0; text-align: left; }}
QPushButton#quiet:hover {{ color: {c['text']}; }}
QPushButton#activityLink {{ color: {c['text']}; font-weight: 600; }}
QPushButton#activityLink:hover {{ color: {c['accent']}; }}
QPushButton#nav {{ background: transparent; border: none; padding: 8px 12px; color: {c['muted']}; text-align: left; border-radius: 7px; }}
QPushButton#nav:hover {{ background: {blend(c['sidebar'],c['accent'],.065)}; color: {c['text']}; }}
QPushButton#nav:checked {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 {blend(c['sidebar'],c['accent'],.25)},stop:1 {blend(c['sidebar'],c['accent'],.14)}); color: {c['text']}; }}
QPushButton#profileButton {{ background: transparent; border: none; padding: 12px 10px; text-align: left; }}
QPushButton#profileButton:hover {{ background: {c['selected']}; }}
QPushButton#iconButton {{ background: transparent; border: 1px solid transparent; padding: 0; }}
QPushButton#iconButton:checked {{ background: {c['selected']}; border-color: {c['border']}; }}
QPushButton#iconButton:hover {{ background: {c['selected']}; border-color: {c['border']}; }}
QPushButton#heroBack {{ background: rgba(15,18,22,160); color: white; border: none; border-radius: 16px; padding: 0; }}
QLineEdit, QTextEdit, QComboBox, QSpinBox, QListWidget, QTableWidget {{ background: {c['input']}; border: 1px solid {c['border']}; border-radius: 7px; padding: 7px 10px; selection-background-color: {c['selected']}; selection-color: {c['text']}; }}
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
QFrame#panel, QFrame#activityCard, QFrame#addPreview, QFrame#emptyState {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {blend(c['panel'],c['text'],.016)},stop:1 {c['panel']}); border: 1px solid {blend(c['border'],c['panel'],.36)}; border-radius: 11px; }}
QFrame#emptyState {{ border: 1px dashed {c['border']}; }}
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
QTabWidget#settingsTabs QTabBar::tab {{ padding: 12px 18px; }}
QDialog#quickAddDialog {{ background: {c['panel']}; }}
QTabBar#sourceTabs {{ border: 1px solid {c['border']}; border-radius: 8px; }}
QTabBar#sourceTabs::tab {{ padding: 9px 14px; border: none; border-right: 1px solid {c['border']}; color: {c['text']}; }}
QTabBar#sourceTabs::tab:selected {{ background: {c['selected']}; border: 1px solid {c['accent']}; border-radius: 7px; }}
QPushButton#resultLink {{ background: transparent; border: none; color: {c['accent']}; text-decoration: underline; padding: 0; }}
QLabel#selectedCheck {{ background: {c['accent']}; color: {c['on_accent']}; border-radius: 14px; font-size: 20px; }}
QToolButton#addDisclosure {{ background: transparent; border: none; border-top: 1px solid {c['border']}; border-bottom: 1px solid {c['border']}; border-radius: 0; padding: 12px 0; text-align: left; }}
QScrollArea, QScrollArea > QWidget > QWidget {{ background: transparent; border: none; }}
QScrollBar:vertical {{ background: transparent; width: 6px; margin: 2px 0; }}
QScrollBar:horizontal {{ background: transparent; height: 6px; margin: 0 2px; }}
QScrollBar::handle {{ background: {c['border']}; border-radius: 3px; min-height: 24px; min-width: 24px; }}
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

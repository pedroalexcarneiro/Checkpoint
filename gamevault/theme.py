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
        'background':blend('#101216',accent,.035),'sidebar':blend('#16191d',accent,.045),
        'panel':blend('#1c2025',accent,.05),'input':blend('#171b20',accent,.04),
        'button':blend('#272d34',accent,.06),'hover':blend('#303841',accent,.12),
        'border':blend('#30363e',accent,.08),'text':'#e8eaed','muted':'#abb3bd',
        'accent':accent,'on_accent':'#152027','selected':blend('#242b32',accent,.16),
        'error':'#e2b3ad','disabled':'#7c858f'})

THEMES={theme.key:theme for theme in [
    dark_theme('blue','Azul','#a3b8cf'),
    dark_theme('green','Verde','#a3bfae'),
    dark_theme('yellow','Amarelo','#c7ba91'),
    dark_theme('red','Vermelho','#cba3a0'),
    dark_theme('black','Preto','#b6b8bc'),
    Theme('white','Branco',{'background':'#f4f3f0','sidebar':'#eaeae6','panel':'#ffffff',
        'input':'#ffffff','button':'#e4e7e7','hover':'#d5dddf','border':'#b9c0c3',
        'text':'#252c31','muted':'#58646b','accent':'#465e69','on_accent':'#ffffff',
        'selected':'#d9e3e7','error':'#9b3636','disabled':'#697279'}),
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
* {{ font-family: 'Segoe UI'; font-size: 15px; }}
QMainWindow, QDialog, QWidget#root {{ background: {c['background']}; color: {c['text']}; }}
QWidget {{ color: {c['text']}; }}
QWidget#sidebar {{ background: {c['sidebar']}; border-right: 1px solid {c['border']}; }}
QLabel#brand {{ font-size: 25px; font-weight: 800; color: {c['accent']}; padding: 22px 12px; }}
QLabel#eyebrow {{ color: {c['muted']}; font-size: 11px; letter-spacing: 2px; }}
QLabel#title {{ font-size: 36px; font-weight: 700; }}
QLabel#muted {{ color: {c['muted']}; font-size: 13px; }}
QLabel#error {{ color: {c['error']}; }}
QPushButton {{ background: {c['button']}; border: 1px solid {c['border']}; border-radius: 9px; padding: 11px 18px; }}
QPushButton:hover {{ background: {c['hover']}; border-color: {c['accent']}; }}
QPushButton:focus, QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QSpinBox:focus {{ border: 2px solid {c['accent']}; }}
QPushButton#primary {{ background: {c['accent']}; color: {c['on_accent']}; border: none; font-weight: 700; }}
QPushButton#primary:hover {{ background: {blend(c['accent'],c['text'],.12)}; }}
QPushButton:disabled, QPushButton#primary:disabled {{ background: {c['button']}; color: {c['disabled']}; border: 1px solid {c['border']}; }}
QPushButton#nav {{ text-align: left; background: transparent; border: none; padding: 13px 20px; color: {c['muted']}; }}
QPushButton#nav:hover {{ background: {c['hover']}; color: {c['text']}; }}
QPushButton#nav:checked {{ background: {c['selected']}; color: {c['text']}; border-left: 3px solid {c['accent']}; border-radius: 0; }}
QLineEdit, QTextEdit, QComboBox, QSpinBox, QListWidget, QTableWidget {{ background: {c['input']}; border: 1px solid {c['border']}; border-radius: 6px; padding: 9px; selection-background-color: {c['accent']}; selection-color: {c['on_accent']}; }}
QLineEdit#headerSearch {{ border-radius: 19px; padding: 10px 18px; font-size: 14px; }}
QComboBox::drop-down {{ subcontrol-origin: padding; subcontrol-position: top right; width: 24px; border: none; background: transparent; }}
QStatusBar::item {{ border: none; }}
QComboBox QAbstractItemView {{ background: {c['panel']}; color: {c['text']}; selection-background-color: {c['accent']}; selection-color: {c['on_accent']}; }}
QScrollArea, QScrollArea > QWidget > QWidget {{ background: transparent; border: none; }}
QHeaderView::section {{ background: {c['button']}; color: {c['muted']}; padding: 10px; border: none; }}
QTableWidget {{ gridline-color: {c['border']}; }}
QFrame#panel {{ background: {c['panel']}; border: 1px solid {c['border']}; border-radius: 10px; }}
QProgressBar {{ background: {c['button']}; border: none; border-radius: 4px; min-height: 10px; }}
QProgressBar::chunk {{ background: {c['accent']}; border-radius: 4px; }}
QCheckBox {{ padding: 5px; }}
QCheckBox:disabled, QComboBox:disabled {{ color: {c['disabled']}; }}
QCheckBox::indicator {{ width: 14px; height: 14px; border: 1px solid {c['muted']}; border-radius: 3px; background: {c['input']}; }}
QCheckBox::indicator:checked {{ background: {c['accent']}; border: 2px solid {c['on_accent']}; }}
QToolTip {{ background: {c['selected']}; color: {c['text']}; border: 1px solid {c['border']}; }}
QLabel#sectionTitle {{ font-size: 20px; font-weight: 600; }}
QLabel#cardTitle {{ font-size: 16px; font-weight: 600; }}
QLabel#caption {{ font-size: 12px; color: {c['muted']}; }}
QLabel#activityKind {{ font-size: 12px; color: {c['accent']}; font-weight: 600; }}
QFrame#activityCard {{ background: {c['panel']}; border: 1px solid {c['border']}; border-radius: 12px; }}
QWidget#gameActions {{ background: {c['panel']}; border-radius: 10px; }}
QLabel#bodyText {{ font-size: 16px; padding: 5px 0; }}
QLabel#connectionDot {{ color: {c['accent']}; font-size: 10px; }}
QLabel#serviceBadge {{ background: {c['selected']}; color: {c['accent']}; border-radius: 10px; font-weight: 700; }}
QPushButton#nav {{ padding: 13px 14px; font-size: 15px; }}
QPushButton#nav:checked {{ background: {c['selected']}; color: {c['text']}; border: none; border-radius: 8px; }}
QPushButton#gameTile {{ background: transparent; border: 1px solid transparent; padding: 0; text-align: left; }}
QPushButton#gameTile:hover, QPushButton#gameTile:focus {{ background: {c['panel']}; border: 1px solid {c['accent']}; }}
QLabel#tileArt {{ background: {c['selected']}; color: {c['accent']}; font-size: 26px; border-radius: 8px; }}
QPushButton#activityLink {{ background: transparent; border: none; padding: 2px 0; text-align: left; font-size: 16px; font-weight: 600; }}
QPushButton#activityLink:hover {{ color: {c['accent']}; }}
QPushButton#quiet {{ background: transparent; border: none; text-align: left; color: {c['muted']}; padding: 6px 0; }}
QListWidget#coverGrid {{ background: transparent; border: none; padding: 0; }}
QListWidget#coverGrid::item {{ border: none; padding: 0; margin: 0; }}
QListWidget#coverGrid::item:selected {{ background: transparent; border: none; color: {c['text']}; }}
QListWidget#coverGrid::item:hover {{ background: transparent; }}
QTabWidget::pane {{ border: none; background: transparent; }}
QTabBar::tab {{ background: transparent; color: {c['muted']}; padding: 12px 16px; border-bottom: 2px solid transparent; }}
QTabBar::tab:selected {{ color: {c['text']}; border-bottom: 2px solid {c['accent']}; }}
QTabBar#libraryTabs::tab {{ margin-right: 8px; padding: 10px 17px; border: none; border-radius: 8px; }}
QTabBar#libraryTabs::tab:selected {{ background: {c['accent']}; color: {c['on_accent']}; }}
QTabBar::tab:hover {{ color: {c['text']}; background: {c['panel']}; }}
QToolButton {{ background: {c['button']}; border: 1px solid {c['border']}; border-radius: 7px; padding: 8px 12px; }}
QToolButton:hover {{ background: {c['hover']}; }}
QMenu {{ background: {c['panel']}; color: {c['text']}; border: 1px solid {c['border']}; padding: 5px; }}
QMenu::item {{ padding: 10px 18px; border-radius: 4px; }}
QMenu::item:selected {{ background: {c['selected']}; }}
QScrollBar:vertical {{ background: transparent; width: 8px; margin: 2px; }}
QScrollBar::handle:vertical {{ background: {c['border']}; border-radius: 3px; min-height: 28px; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
QGroupBox {{ border: none; margin-top: 18px; }}
QGroupBox::title {{ color: {c['muted']}; subcontrol-origin: margin; }}
QLabel#systemName {{ font-size: 22px; font-weight: 600; color: {c['text']}; }}
QLabel#metricValue {{ font-size: 30px; font-weight: 600; }}
QToolButton::menu-indicator {{ image: none; width: 0px; height: 0px; }}
QWidget#taskStatus QToolButton {{ padding: 0; border: none; background: transparent; }}
QStatusBar::item {{ border: none; }}
QStatusBar {{ color: {c['muted']}; background: {c['background']}; }}
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

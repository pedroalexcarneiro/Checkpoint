"""Lixeira em cards horizontais; restauração preserva a identidade do registro."""
from datetime import datetime, timezone
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QSizePolicy
from .ui_components import card,text,action,ElidedLabel,nav_icon
from .locale import count_text


def deletion_label(value):
    if not value:return 'Data não registrada'
    try:
        if len(value)==10:
            return 'Movido para a lixeira: '+datetime.fromisoformat(value).strftime('%d/%m/%Y')+' · horário não registrado'
        stamp=datetime.fromisoformat(value.replace('Z','+00:00'))
        if stamp.tzinfo is None:stamp=stamp.replace(tzinfo=timezone.utc)
        return 'Movido para a lixeira: '+stamp.astimezone().strftime('%d/%m/%Y %H:%M')
    except (ValueError,TypeError,AttributeError):
        return 'Data não registrada'


def build_trash(window,layout):
    rows=[dict(r) for r in window.library.sql.execute('SELECT * FROM games WHERE deleted_at IS NOT NULL ORDER BY title,id')]
    layout.setContentsMargins(0,0,16,8)
    header=QHBoxLayout();header.addWidget(text('Lixeira','sectionTitle'));header.addWidget(text(count_text(len(rows),'jogo'),'muted'));header.addStretch();layout.addLayout(header)
    if not rows:
        layout.addWidget(text('A lixeira está vazia.','cardTitle'))
        layout.addWidget(action('Abrir biblioteca',lambda:window.navigate(1)),0,Qt.AlignLeft)
    for game in rows:
        frame,inside=card();frame.setObjectName('trashCard');inside.setContentsMargins(16,14,16,14)
        row=QHBoxLayout();row.setSpacing(16)
        logo=QLabel();logo.setObjectName('trashLogo');logo.setFixedSize(96,48);logo.setAlignment(Qt.AlignCenter)
        if not QPixmap(game.get('logo') or '').isNull():
            from .list_art import list_icon
            logo.setPixmap(list_icon(game,window.theme.colors['text']).pixmap(96,48))
        else:logo.setPixmap(nav_icon('library',window.theme.colors['muted'],24).pixmap(24,24))
        row.addWidget(logo)
        words_widget=QWidget();words_widget.setMinimumWidth(0);words_widget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        words=QVBoxLayout(words_widget);words.setContentsMargins(0,0,0,0);words.setSpacing(4)
        title=ElidedLabel(game['title'],'cardTitle');title.setObjectName('trashName');title.setStyleSheet('font-size: 16px; font-weight: 600;');words.addWidget(title)
        stamp=deletion_label(game['deleted_at'])
        ambiguous=sum(other['title']==game['title'] for other in rows)>1
        if ambiguous:stamp+=' · '+(game['platform'] or 'Plataforma não definida')+' · Registro '+str(game['id'])
        date=ElidedLabel(stamp,'caption');date.setObjectName('trashDeletedAt');words.addWidget(date)
        row.addWidget(words_widget,1)
        row.addWidget(action('Restaurar',lambda checked=False,identity=game['id']:window.restore_game(identity),True))
        inside.addLayout(row);layout.addWidget(frame)
    layout.addStretch()

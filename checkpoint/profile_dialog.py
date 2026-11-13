"""Foto e apelido locais, sem cadastro de conta."""
from pathlib import Path
from PySide6.QtCore import Qt,QRectF,Slot
from PySide6.QtGui import QPixmap,QPainter,QPainterPath,QIcon,QImageReader
from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QFileDialog,QDialogButtonBox
from .integrations.images import ImageCache


def avatar_icon(path,size=64):
    source=QPixmap(path or '')
    if source.isNull():return QIcon()
    image=QPixmap(size,size);image.fill(Qt.transparent)
    painter=QPainter(image);painter.setRenderHint(QPainter.Antialiasing)
    clip=QPainterPath();clip.addEllipse(QRectF(0,0,size,size));painter.setClipPath(clip)
    scaled=source.scaled(size,size,Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
    painter.drawPixmap((size-scaled.width())//2,(size-scaled.height())//2,scaled);painter.end()
    return QIcon(image)


class ProfileDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent);self.library=library;self.selected=None;self.remove_photo=False
        self.setWindowTitle('Perfil');self.resize(420,330)
        from .window_style import titlebar_theme
        titlebar_theme(self,True)
        layout=QVBoxLayout(self);layout.setContentsMargins(24,24,24,24);layout.setSpacing(16)
        self.photo=QLabel();self.photo.setFixedSize(88,88);self.photo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.photo,0,Qt.AlignHCenter)
        row=QHBoxLayout();choose=QPushButton('Escolher foto');choose.clicked.connect(self.choose_photo);row.addWidget(choose)
        remove=QPushButton('Remover foto');remove.clicked.connect(self.clear_photo);row.addWidget(remove);layout.addLayout(row)
        layout.addWidget(QLabel('Apelido'))
        self.nickname=QLineEdit(library.setting('profile.name',''));self.nickname.setMaxLength(40);self.nickname.setPlaceholderText('Apelido');layout.addWidget(self.nickname)
        self.error=QLabel();self.error.setObjectName('error');self.error.setWordWrap(True);layout.addWidget(self.error)
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Save).setText('Salvar');buttons.button(QDialogButtonBox.Save).setObjectName('primary')
        buttons.button(QDialogButtonBox.Cancel).setText('Cancelar');buttons.accepted.connect(self.save);buttons.rejected.connect(self.reject);layout.addWidget(buttons)
        self.preview(library.setting('profile.avatar',''))

    def preview(self,path):
        icon=avatar_icon(path,88)
        if icon.isNull():
            from .ui_components import nav_icon
            from .design_system import colors
            icon=nav_icon('user',colors()['muted'])
        self.photo.setPixmap(icon.pixmap(88,88))

    @Slot()
    def choose_photo(self):
        path,_=QFileDialog.getOpenFileName(self,'Foto de perfil','','Imagens (*.png *.jpg *.jpeg *.webp)')
        if path:
            try:
                size=QImageReader(path).size()
                valid=Path(path).stat().st_size<=25_000_000 and 0<size.width()*size.height()<=60_000_000 and not QPixmap(path).isNull()
            except OSError:valid=False
            if not valid:
                self.error.setText('Imagem inválida ou maior que 25 MB.');return
            self.selected=path;self.remove_photo=False;self.error.clear();self.preview(path)

    @Slot()
    def clear_photo(self):
        self.selected=None;self.remove_photo=True;self.preview('')

    @Slot()
    def save(self):
        avatar=self.library.setting('profile.avatar','')
        try:
            if self.selected:
                path=Path(self.selected)
                if path.stat().st_size>25_000_000:raise ValueError('Imagem maior que 25 MB.')
                avatar=ImageCache(self.library.db.path.parent/'images'/'profile').store(path.read_bytes())
            elif self.remove_photo:avatar=''
        except Exception:
            self.error.setText('Não foi possível salvar essa imagem.');return
        self.library.set_setting('profile.name',self.nickname.text().strip() or 'Meu perfil')
        self.library.set_setting('profile.avatar',avatar)
        self.accept()

"""Foto e apelido locais, sem cadastro de conta."""
from pathlib import Path
import json
from PySide6.QtCore import Qt,QRectF,Slot,QBuffer,QIODevice
from PySide6.QtGui import QPixmap,QPainter,QPainterPath,QIcon,QImageReader,QImage
from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QFileDialog,QDialogButtonBox,QSlider
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
        super().__init__(parent);self.library=library;self.selected=None;self.remove_photo=False;self.crop_dirty=False
        from .dialog_style import prepare_dialog
        prepare_dialog(self)
        self.original_source=library.setting('profile.avatar_original','') or library.setting('profile.avatar','')
        self.setWindowTitle('Perfil');self.resize(500,540)
        from .window_style import titlebar_theme
        titlebar_theme(self,True)
        layout=QVBoxLayout(self);layout.setContentsMargins(24,24,24,24);layout.setSpacing(16)
        self.photo=QLabel();self.photo.setFixedSize(88,88);self.photo.setAlignment(Qt.AlignCenter)
        from .avatar_crop import AvatarCrop
        self.crop=AvatarCrop(self);self.zoom=QSlider(Qt.Horizontal);self.zoom.setObjectName('avatarZoom');self.zoom.setRange(100,400);self.zoom.setValue(100)
        from .design_system import colors
        palette=colors()
        self.zoom.setStyleSheet('QSlider#avatarZoom::groove:horizontal { height: 4px; background: '+palette['border']+'; border-radius: 2px; } QSlider#avatarZoom::sub-page:horizontal { background: '+palette['accent']+'; border-radius: 2px; } QSlider#avatarZoom::handle:horizontal { width: 14px; height: 14px; margin: -5px 0; border: none; border-radius: 7px; background: '+palette['accent']+'; }')
        self.zoom.setAccessibleName('Zoom da foto');self.zoom.valueChanged.connect(self.crop.set_zoom)
        preview=QHBoxLayout();preview.addWidget(self.crop);words=QVBoxLayout();words.addWidget(QLabel('Prévia'));words.addWidget(self.photo);words.addStretch();preview.addLayout(words);layout.addLayout(preview)
        controls=QHBoxLayout();controls.addWidget(QLabel('Zoom'));controls.addWidget(self.zoom,1);self.zoom_value=QLabel('100%');controls.addWidget(self.zoom_value);layout.addLayout(controls)
        self.zoom.valueChanged.connect(lambda value:self.zoom_value.setText(str(value)+'%'))
        self.crop.changed.connect(self.crop_changed)
        row=QHBoxLayout();choose=QPushButton('Escolher foto');choose.clicked.connect(self.choose_photo);row.addWidget(choose)
        remove=QPushButton('Remover foto');remove.clicked.connect(self.clear_photo);row.addWidget(remove);layout.addLayout(row)
        layout.addWidget(QLabel('Apelido'))
        self.nickname=QLineEdit(library.setting('profile.name',''));self.nickname.setMaxLength(40);self.nickname.setPlaceholderText('Apelido');layout.addWidget(self.nickname)
        self.error=QLabel();self.error.setObjectName('error');self.error.setWordWrap(True);layout.addWidget(self.error)
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Save).setText('Salvar');buttons.button(QDialogButtonBox.Save).setObjectName('primary')
        buttons.button(QDialogButtonBox.Cancel).setText('Cancelar');buttons.accepted.connect(self.save);buttons.rejected.connect(self.reject);layout.addWidget(buttons)
        if self.original_source:
            image=self.read_photo(self.original_source)
            if not image.isNull():
                self.crop.set_source(image,library.setting('profile.avatar_crop',{}));self.zoom.blockSignals(True);self.zoom.setValue(round(self.crop.zoom*100));self.zoom.blockSignals(False);self.zoom_value.setText(str(self.zoom.value())+'%')
        self.crop_dirty=False
        self.preview(library.setting('profile.avatar',''))

    def preview(self,path):
        icon=avatar_icon(path,88)
        if icon.isNull():
            from .ui_components import nav_icon
            from .design_system import colors
            icon=nav_icon('user',colors()['muted'])
        self.photo.setPixmap(icon.pixmap(88,88))

    @staticmethod
    def read_photo(path):
        try:
            reader=QImageReader(str(path));reader.setAutoTransform(True);size=reader.size()
            if Path(path).stat().st_size>25_000_000 or not 0<size.width()*size.height()<=60_000_000 or reader.supportsAnimation():return QImage()
            return reader.read()
        except OSError:return QImage()

    def crop_changed(self):
        self.crop_dirty=True
        image=self.crop.render_avatar()
        if not image.isNull():self.photo.setPixmap(avatar_icon_from_image(image,88))
        else:self.preview('')

    def select_photo(self,path):
        image=self.read_photo(path)
        if image.isNull():self.error.setText('Imagem inválida ou maior que 25 MB.');return False
        self.selected=str(path);self.original_source=str(path);self.remove_photo=False;self.error.clear()
        self.crop.set_source(image);self.zoom.setValue(100);return True

    @Slot()
    def choose_photo(self):
        path,_=QFileDialog.getOpenFileName(self,'Foto de perfil','','Imagens (*.png *.jpg *.jpeg *.webp)')
        if path:self.select_photo(path)

    @Slot()
    def clear_photo(self):
        self.selected=None;self.original_source='';self.remove_photo=True;self.crop.set_source(QImage());self.zoom.setValue(100);self.preview('')

    @Slot()
    def save(self):
        avatar=self.library.setting('profile.avatar','');original=self.library.setting('profile.avatar_original','');state=self.library.setting('profile.avatar_crop',{})
        try:
            if (self.selected or self.crop_dirty) and not self.remove_photo and not self.crop.source.isNull():
                path=Path(self.original_source)
                if path.stat().st_size>25_000_000:raise ValueError('Imagem maior que 25 MB.')
                cache=ImageCache(self.library.db.path.parent/'images'/'profile')
                original=cache.store(path.read_bytes());buffer=QBuffer();buffer.open(QIODevice.WriteOnly)
                if not self.crop.render_avatar().save(buffer,'PNG'):raise ValueError('Recorte inválido.')
                avatar=cache.store(bytes(buffer.data()));state=self.crop.state()
            elif self.remove_photo:avatar='';original='';state={}
        except Exception:
            self.error.setText('Não foi possível salvar essa imagem.');return
        values={'profile.name':self.nickname.text().strip() or 'Meu perfil','profile.avatar':avatar,'profile.avatar_original':original,'profile.avatar_crop':state}
        with self.library.sql:
            self.library.sql.executemany('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',[(key,json.dumps(value)) for key,value in values.items()])
        self.accept()


def avatar_icon_from_image(image,size):
    pix=QPixmap(size,size);pix.fill(Qt.transparent);p=QPainter(pix);p.setRenderHint(QPainter.Antialiasing);p.setRenderHint(QPainter.SmoothPixmapTransform)
    path=QPainterPath();path.addEllipse(QRectF(0,0,size,size));p.setClipPath(path);p.drawImage(QRectF(0,0,size,size),image);p.end();return pix

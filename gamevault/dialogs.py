from pathlib import Path
from PySide6.QtCore import Qt, QSize, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import (QDialog,QDialogButtonBox,QFormLayout,QLineEdit,QTextEdit,QComboBox,
    QSpinBox,QCheckBox,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog,QLabel,QScrollArea,QWidget)
from .library import STATUSES

class GameDialog(QDialog):
    def __init__(self, parent=None, game=None):
        super().__init__(parent)
        self.setWindowTitle('Editar jogo' if game else 'Adicionar à biblioteca')
        self.resize(620,720)
        outer = QVBoxLayout(self)
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        body = QWidget(); form = QFormLayout(body); form.setSpacing(14)
        self.fields = {}
        for key,label in [('title','Nome *'),('platform','Plataforma'),('genre','Gênero'),('category','Categoria'),
                          ('developer','Desenvolvedora'),('publisher','Publicadora'),('release_date','Lançamento (AAAA-MM-DD)'),
                          ('source','Origem')]:
            widget = QLineEdit(); form.addRow(label,widget); self.fields[key] = widget
        self.fields['platform'].setText('PC'); self.fields['source'].setText('Manual')
        status = QComboBox(); status.addItems(STATUSES); form.addRow('Status',status); self.fields['status'] = status
        rating = QSpinBox(); rating.setRange(-1,10); rating.setValue(-1); rating.setSpecialValueText('Sem nota')
        form.addRow('Nota pessoal',rating); self.fields['rating'] = rating
        favorite = QCheckBox('Marcar como favorito'); form.addRow('',favorite); self.fields['favorite'] = favorite
        for key,label in [('cover','Capa'),('banner','Banner'),('logo','Logo'),('executable','Executável local')]:
            row = QHBoxLayout(); line = QLineEdit(); button = QPushButton('Escolher…')
            button.clicked.connect(lambda checked=False,k=key:self.choose(k))
            row.addWidget(line); row.addWidget(button); form.addRow(label,row); self.fields[key] = line
        for key,label in [('description','Descrição'),('notes','Observações')]:
            text = QTextEdit(); text.setMaximumHeight(100); form.addRow(label,text); self.fields[key] = text
        scroll.setWidget(body); outer.addWidget(scroll)
        self.error = QLabel(); self.error.setObjectName('error'); outer.addWidget(self.error)
        buttons = QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.validate); buttons.rejected.connect(self.reject); outer.addWidget(buttons)
        if game:
            for key, widget in self.fields.items():
                value = game.get(key)
                if isinstance(widget,QComboBox): widget.setCurrentText(value or STATUSES[0])
                elif isinstance(widget,QSpinBox): widget.setValue(value if value is not None else -1)
                elif isinstance(widget,QCheckBox): widget.setChecked(bool(value))
                elif isinstance(widget,QTextEdit): widget.setPlainText(value or '')
                else: widget.setText(value or '')

    def choose(self,key):
        filters = 'Executáveis (*.exe);;Todos (*)' if key=='executable' else 'Imagens (*.png *.jpg *.jpeg *.webp)'
        path,_ = QFileDialog.getOpenFileName(self,'Selecionar arquivo','',filters)
        if path: self.fields[key].setText(path)

    def data(self):
        result = {}
        for key,w in self.fields.items():
            if isinstance(w,QComboBox): value = w.currentText()
            elif isinstance(w,QSpinBox): value = None if w.value()<0 else w.value()
            elif isinstance(w,QCheckBox): value = int(w.isChecked())
            elif isinstance(w,QTextEdit): value = w.toPlainText()
            else: value = w.text().strip()
            result[key] = value
        return result

    def validate(self):
        if not self.fields['title'].text().strip():
            self.error.setText('Informe o nome do jogo.'); return
        date = self.fields['release_date'].text().strip()
        if date:
            from datetime import date as date_type
            try: date_type.fromisoformat(date)
            except ValueError:
                self.error.setText('Data inválida. Use AAAA-MM-DD.'); return
        for key in ['cover','banner','logo','executable']:
            value = self.fields[key].text().strip()
            if value and not Path(value).is_file():
                self.error.setText('Arquivo não encontrado: '+key); return
            if value and key!='executable' and QPixmap(value).isNull():
                self.error.setText('Imagem inválida: '+key); return
        self.accept()

class ImageDialog(QDialog):
    def __init__(self,path,parent=None):
        super().__init__(parent); self.setWindowTitle(Path(path).name); self.resize(1000,750)
        layout = QVBoxLayout(self); image = QLabel(); image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(path)
        image.setPixmap(pixmap.scaled(950,680,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        layout.addWidget(image)

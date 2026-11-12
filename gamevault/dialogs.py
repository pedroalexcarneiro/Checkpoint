from pathlib import Path
from PySide6.QtCore import Qt, QSize, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import (QDialog,QDialogButtonBox,QFormLayout,QLineEdit,QTextEdit,QComboBox,
    QSpinBox,QCheckBox,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog,QLabel,QScrollArea,QWidget,QListWidget,QGroupBox,QMessageBox,QTabBar)
from .library import STATUSES

class GameDialog(QDialog):
    def __init__(self, parent=None, game=None, library=None, allow_steam=True):
        super().__init__(parent)
        self.setWindowTitle('Editar jogo' if game else 'Adicionar jogo')
        self.resize(660,760 if game else 390)
        self.library=library;self.drive_file_id=None;self.catalog_result=None;self.drive_results=[]
        self.steam_requested=False
        outer = QVBoxLayout(self);outer.setContentsMargins(24,24,24,24);outer.setSpacing(14)
        heading=QLabel('Editar jogo' if game else 'Adicionar jogo');heading.setObjectName('sectionTitle');outer.addWidget(heading)
        if library is not None and game is None:
            self.source_tabs=QTabBar();self.source_tabs.setObjectName('sourceTabs');self.source_tabs.setExpanding(True)
            for name in ('Pesquisar jogo','ROM do Drive','Steam'):self.source_tabs.addTab(name)
            if not allow_steam:self.source_tabs.setTabVisible(2,False)
            outer.addWidget(self.source_tabs)
            self.steam_panel=QWidget();steam_layout=QVBoxLayout(self.steam_panel)
            steam_layout.addWidget(QLabel('Escolha os jogos da sua conta para importar de uma vez.'))
            steam_button=QPushButton('Importar biblioteca Steam');steam_button.setObjectName('primary');steam_button.clicked.connect(self.request_steam);steam_layout.addWidget(steam_button)
            outer.addWidget(self.steam_panel);self.steam_panel.hide()
        if library is not None and game is None:
            group=QGroupBox('Adicionar do Google Drive');drive=QVBoxLayout(group)
            self.drive_query=QLineEdit();self.drive_query.setObjectName('addDriveSearch');self.drive_query.setPlaceholderText('Buscar ROM por nome ou pasta…')
            drive.addWidget(self.drive_query);self.drive_list=QListWidget();self.drive_list.setMaximumHeight(115);drive.addWidget(self.drive_list)
            row=QHBoxLayout();use=QPushButton('Usar ROM selecionada');use.clicked.connect(self.choose_drive);row.addWidget(use)
            manage=QPushButton('Atualizar índice do Drive');manage.clicked.connect(self.manage_drive);row.addWidget(manage);drive.addLayout(row)
            self.drive_info=QLabel('Escolha uma versão no índice do Drive.');self.drive_info.setWordWrap(True);drive.addWidget(self.drive_info)
            self.drive_query.textChanged.connect(self.search_drive)
            self.drive_toggle=QCheckBox('Escolher ROM do Google Drive')
            self.drive_toggle.toggled.connect(group.setVisible)
            self.drive_group=group;self.drive_toggle.hide();outer.addWidget(group);group.hide()
            lookup=QPushButton('Confirmar título original e completar dados no catálogo');lookup.clicked.connect(self.lookup_catalog);outer.addWidget(lookup);self.catalog_button=lookup
        if library is not None and game is not None:
            lookup=QPushButton('Identificar e completar ficha e imagens');lookup.clicked.connect(self.lookup_catalog);outer.addWidget(lookup);self.catalog_button=lookup
        if library is not None and game is None:
            self.complete_on_save=QCheckBox('Buscar ficha e imagens automaticamente')
            self.complete_on_save.setChecked(bool(library.setting('artwork.auto',True)));outer.addWidget(self.complete_on_save)
        scroll = QScrollArea(); scroll.setWidgetResizable(True);self.form_scroll=scroll
        body = QWidget(); form = QFormLayout(body); form.setSpacing(14); self.form=form
        self.fields = {}
        for key,label in [('title','Nome *'),('platform','Plataforma'),('genre','Gênero'),('category','Categoria'),
                          ('developer','Desenvolvedora'),('publisher','Publicadora'),('release_date','Lançamento (AAAA-MM-DD)'),
                          ('source','Origem')]:
            widget = QLineEdit(); form.addRow(label,widget); self.fields[key] = widget
        self.fields['title'].setPlaceholderText('Ex.: Hollow Knight');self.fields['title'].setClearButtonEnabled(True)
        self.fields['platform'].setText('PC'); self.fields['source'].setText('Manual')
        status = QComboBox(); status.addItems(STATUSES); form.addRow('Status',status); self.fields['status'] = status
        rating = QSpinBox(); rating.setRange(-1,10); rating.setValue(-1); rating.setSpecialValueText('Sem nota')
        form.addRow('Nota pessoal',rating); self.fields['rating'] = rating
        favorite = QCheckBox('Marcar como favorito'); form.addRow('',favorite); self.fields['favorite'] = favorite
        for key,label in [('cover','Capa'),('banner','Banner'),('logo','Logo'),('executable','Executável local')]:
            row = QHBoxLayout(); line = QLineEdit(); button = QPushButton('Escolher…')
            # Um método do receptor permite ao Qt encerrar a conexão com o diálogo.
            # Lambdas que capturam self mantêm um ciclo até o shutdown do PySide.
            button.setProperty('gameField',key)
            button.clicked.connect(self.choose_field)
            row.addWidget(line); row.addWidget(button); form.addRow(label,row); self.fields[key] = line
        for key,label in [('description','Descrição'),('notes','Observações')]:
            text = QTextEdit(); text.setMaximumHeight(100); form.addRow(label,text); self.fields[key] = text
        self.advanced=QCheckBox('Opções avançadas')
        self.advanced.toggled.connect(self.toggle_advanced)
        outer.addWidget(self.advanced)
        self.advanced.setChecked(bool(game))
        self.toggle_advanced(bool(game))
        scroll.setWidget(body); outer.addWidget(scroll)
        self.error = QLabel(); self.error.setObjectName('error'); outer.addWidget(self.error)
        buttons = QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel);self.buttons=buttons
        buttons.button(QDialogButtonBox.Save).setText('Salvar' if game else 'Adicionar à biblioteca');buttons.button(QDialogButtonBox.Save).setObjectName('primary');buttons.button(QDialogButtonBox.Cancel).setText('Cancelar')
        buttons.accepted.connect(self.validate); buttons.rejected.connect(self.reject); outer.addWidget(buttons)
        outer.removeWidget(self.advanced)
        if hasattr(self,'complete_on_save'):
            outer.removeWidget(self.complete_on_save);outer.insertWidget(outer.indexOf(self.error),self.complete_on_save)
        outer.insertWidget(outer.indexOf(self.error),self.advanced)
        if hasattr(self,'source_tabs'):
            self.source_tabs.currentChanged.connect(self.source_changed);self.source_changed(0)
        if game:
            for key, widget in self.fields.items():
                value = game.get(key)
                if isinstance(widget,QComboBox): widget.setCurrentText(value or STATUSES[0])
                elif isinstance(widget,QSpinBox): widget.setValue(value if value is not None else -1)
                elif isinstance(widget,QCheckBox): widget.setChecked(bool(value))
                elif isinstance(widget,QTextEdit): widget.setPlainText(value or '')
                else: widget.setText(value or '')

        if library is not None and game is None:
            from .quick_add import QuickAdd
            self.quick_add=QuickAdd(self,outer,allow_steam)
        elif game is not None:
            from .game_editor import build_editor
            build_editor(self,outer)

    def finish_or_wait(self,result):
        quick=getattr(self,'quick_add',None)
        if quick and quick.owner is self and quick.jobs:
            quick.deferred_result=result;quick.closed=True;quick.timer.stop()
            quick.state.setText('Encerrando a consulta atual…');return
        self.done(result)

    def accept(self):self.finish_or_wait(QDialog.Accepted)
    def reject(self):self.finish_or_wait(QDialog.Rejected)

    def request_steam(self):
        self.steam_requested=True;self.reject()

    def source_changed(self,index):
        if hasattr(self,'quick_add'):return
        self.steam_panel.setVisible(index==2);self.drive_toggle.setChecked(index==1)
        self.form_scroll.setVisible(index!=2);self.advanced.setVisible(index!=2);self.complete_on_save.setVisible(index!=2)
        self.buttons.button(QDialogButtonBox.Save).setVisible(index!=2)
        if index==0 and self.drive_file_id is not None:
            self.drive_file_id=None;self.fields['source'].setText('Manual')
        self.resize(660,540 if index==1 else 390)

    def toggle_advanced(self,visible):
        if hasattr(self,'catalog_button'):self.catalog_button.setVisible(visible)
        for row in range(self.form.rowCount()):
            self.form.setRowVisible(row,visible or row in (0,1))

    def search_drive(self,text):
        import unicodedata
        def fold(value):return ''.join(c for c in unicodedata.normalize('NFKD',value.casefold()) if not unicodedata.combining(c))
        query=fold(text.strip());self.drive_list.clear();self.drive_results=[]
        if not query:self.drive_info.setText('Digite o nome do jogo para pesquisar as ROMs já indexadas.');return
        rows=self.library.sql.execute('SELECT f.*,g.title FROM game_files f LEFT JOIN games g ON f.game_id=g.id WHERE f.drive_id IS NOT NULL ORDER BY f.original_name')
        self.drive_results=[dict(row) for row in rows if any(query in fold(row[key] or '') for key in ('original_name','title','folder_path'))]
        for row in self.drive_results:self.drive_list.addItem(row['original_name']+' · '+(row['platform'] or 'Revisar plataforma'))
        self.drive_info.setText(f'{len(self.drive_results)} ROMs encontradas. Selecione a versão desejada.')
    def choose_drive(self):
        index=self.drive_list.currentRow()
        if index<0:self.drive_info.setText('Selecione uma ROM.');return
        self.load_drive_file(self.drive_results[index])
    def load_drive_file(self,file):
        if hasattr(self,'quick_add'):self.quick_add.suspend=True
        from .integrations.drive import normalize_rom_name
        if not hasattr(self,'quick_add'):self.source_tabs.setCurrentIndex(1);self.drive_toggle.setChecked(True)
        self.drive_file_id=file['id'];self.catalog_result=None
        for key in ('genre','developer','publisher','release_date','description','cover','banner','logo','executable'):
            widget=self.fields[key]
            if isinstance(widget,QTextEdit):widget.clear()
            else:widget.clear()
        self.fields['title'].setText(normalize_rom_name(file['original_name']))
        self.fields['platform'].setText(file['platform'] or '')
        self.fields['source'].setText('Google Drive')
        if file['game_id']:
            existing=self.library.get(file['game_id'])
            if existing:
                self.fields['title'].setText(existing['title'])
                for key in ('genre','developer','publisher','release_date','description'):
                    widget=self.fields[key]
                    if isinstance(widget,QTextEdit):widget.setPlainText(existing[key] or '')
                    else:widget.setText(existing[key] or '')
        self.drive_info.setText('Selecionada: '+file['original_name']+'. Download somente quando solicitado.')
        if hasattr(self,'quick_add'):
            self.quick_add.suspend=False;self.quick_add.drive_loaded(file)
    def manage_drive(self):
        from .drive_dialog import DriveDialog
        DriveDialog(self.library,self).exec();self.search_drive(self.drive_query.text())
    def lookup_catalog(self):
        from .catalog_picker import CatalogPicker
        dialog=CatalogPicker(self.fields['title'].text(),self)
        if self.drive_file_id is not None:
            dialog.provider.setCurrentIndex(dialog.provider.findData('rawg'))
        from PySide6.QtCore import QTimer
        QTimer.singleShot(0,dialog.lookup)
        if dialog.exec()==QDialog.Accepted:self.apply_catalog(dialog.selected_result)
    def apply_catalog(self,result):
        if hasattr(self,'quick_add'):self.quick_add.suspend=True
        self.catalog_result=result
        values={'title':result.title,'description':result.description,'genre':', '.join(result.genres),'developer':result.developer,'publisher':result.publisher,'release_date':result.release_date}
        for key,value in values.items():
            if value:
                widget=self.fields[key]
                if isinstance(widget,QTextEdit):widget.setPlainText(value)
                else:widget.setText(value)
        if hasattr(self,'drive_info'):self.drive_info.setText('Título confirmado: '+result.title+'. A plataforma e o nome original da ROM foram preservados.')
        if hasattr(self,'quick_add'):self.quick_add.suspend=False
    def choose_field(self):
        self.choose(self.sender().property('gameField'))

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

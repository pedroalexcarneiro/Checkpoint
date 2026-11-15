"""Escolha e confirmação de ROM local; nenhum vínculo muda antes de confirmar."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit,QComboBox,QLabel,QCheckBox,QFileDialog,QDialogButtonBox,QPushButton,QInputDialog
from .ui_components import text,action
from .local_rom import validate_path,canonical_platform,compatible_profiles,identity_problem,title_needs_confirmation,bind_local,extension_set


class LocalRomDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id;self.file=None;self.file_id=None
        self.setWindowTitle('Vincular ROM local');self.resize(680,480)
        layout=QVBoxLayout(self);layout.setContentsMargins(24,24,24,24);layout.setSpacing(16)
        self.game_title=text('','sectionTitle');layout.addWidget(self.game_title)
        line=QHBoxLayout();self.path=QLineEdit();self.path.setObjectName('romLocalPath');self.path.setReadOnly(True);self.path.setPlaceholderText('Arquivo da ROM');line.addWidget(self.path,1)
        line.addWidget(action('Escolher arquivo',self.choose_file));layout.addLayout(line)
        form=QFormLayout();self.platform=QComboBox();self.platform.setObjectName('romLocalPlatform');self.profile=QComboBox();self.profile.setObjectName('romLocalProfile')
        form.addRow('Plataforma da ROM',self.platform);form.addRow('Perfil do emulador',self.profile);layout.addLayout(form)
        self.title_confirm=QCheckBox('Confirmo que este arquivo pertence ao jogo e à edição exibidos.');self.title_confirm.hide();layout.addWidget(self.title_confirm)
        self.state=text('Escolha uma ROM local.','muted');self.state.setObjectName('romLocalState');layout.addWidget(self.state)
        correction=QHBoxLayout();self.other=action('Escolher outra ficha',self.choose_game);self.register=action('Cadastrar edição',self.register_game);correction.addWidget(self.other);correction.addWidget(self.register);correction.addStretch();layout.addLayout(correction)
        layout.addWidget(action('Configurar perfis de emulador',self.configure_profiles),0,Qt.AlignLeft);layout.addStretch()
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.confirm=buttons.button(QDialogButtonBox.Save);self.confirm.setText('Vincular ROM local');self.confirm.setObjectName('primary');self.confirm.setEnabled(False)
        buttons.button(QDialogButtonBox.Cancel).setText('Cancelar');buttons.accepted.connect(self.save);buttons.rejected.connect(self.reject);layout.addWidget(buttons)
        self.platform.currentIndexChanged.connect(self.refresh_profiles);self.profile.currentIndexChanged.connect(self.refresh_state);self.title_confirm.toggled.connect(self.refresh_state)
        self.refresh_platforms()
    def refresh_platforms(self):
        game=self.library.get(self.game_id);self.game_title.setText(game['title'])
        current=self.platform.currentData();values={canonical_platform(r[0]) for r in self.library.sql.execute('SELECT DISTINCT platform FROM emulator_profiles') if r[0]}
        if game['platform']:values.add(canonical_platform(game['platform']))
        if self.file and self.file['platform']:values.add(canonical_platform(self.file['platform']))
        self.platform.blockSignals(True);self.platform.clear();self.platform.addItem('Selecionar plataforma','')
        for value in sorted(values):self.platform.addItem(value,value)
        selected=(self.file or {}).get('platform') or current or canonical_platform(game['platform'])
        self.platform.setCurrentIndex(max(0,self.platform.findData(selected)));self.platform.blockSignals(False);self.refresh_profiles()
    def refresh_profiles(self,*args):
        selected=self.profile.currentData();self.profile.blockSignals(True);self.profile.clear()
        if self.file:
            for profile in compatible_profiles(self.library,self.platform.currentData(),self.file['extension']):self.profile.addItem(profile['name'],profile['id'])
        index=self.profile.findData(selected)
        if index>=0:self.profile.setCurrentIndex(index)
        self.profile.blockSignals(False);self.refresh_state()
    def refresh_state(self,*args):
        game=self.library.get(self.game_id);problem='';warning=False
        if self.file:
            file={**self.file,'platform':self.platform.currentData() or ''};problem=identity_problem(game,file)
            inferred=self.file['platform']
            if inferred and canonical_platform(inferred).casefold()!=canonical_platform(file['platform']).casefold():problem='A plataforma identificada no arquivo difere da seleção.'
            warning=title_needs_confirmation(game,file)
        self.other.setVisible(bool(problem));self.register.setVisible(bool(problem))
        self.title_confirm.setVisible(warning and not problem)
        ready=bool(self.file and self.platform.currentData() and self.profile.currentData() and not problem and (not warning or self.title_confirm.isChecked()))
        self.confirm.setEnabled(ready)
        if problem:self.state.setText(problem)
        elif not self.file:self.state.setText('Escolha uma ROM local.')
        elif not self.platform.currentData():self.state.setText('Selecione a plataforma da ROM.')
        elif not self.profile.count():self.state.setText('Nenhum perfil compatível com esta plataforma e extensão. Configure um perfil.')
        elif warning and not self.title_confirm.isChecked():self.state.setText('O nome do arquivo difere da ficha. Confira a edição antes de confirmar.')
        else:self.state.setText('')
    def choose_file(self):
        extensions=set()
        for row in self.library.sql.execute('SELECT extensions FROM emulator_profiles'):extensions.update(extension_set(row[0]))
        pattern=' '.join('*'+value for value in sorted(extensions))
        filters=('ROMs dos perfis ('+pattern+');;' if pattern else '')+'Todos os arquivos (*)'
        path,_=QFileDialog.getOpenFileName(self,'Escolher ROM local','',filters)
        if path:self.select_path(path)
    def select_path(self,path):
        try:file=validate_path(path)
        except ValueError as error:self.state.setText(str(error));self.confirm.setEnabled(False);return False
        self.file=file;self.path.setText(file['local_path']);self.path.setToolTip(file['local_path']);self.title_confirm.setChecked(False);self.refresh_platforms();return True
    def configure_profiles(self):
        from .emulator_dialog import EmulatorDialog
        EmulatorDialog(self.library,self).exec();self.refresh_platforms()
    def choose_game(self):
        games=self.library.owned_games();names=[f'{n+1}. '+g['title']+' · '+(g['platform'] or 'Plataforma não definida') for n,g in enumerate(games)]
        choice,ok=QInputDialog.getItem(self,'Escolher ficha','Jogo e edição:',names,0,False)
        if ok:
            self.game_id=games[names.index(choice)]['id'];self.title_confirm.setChecked(False);self.refresh_platforms()
    def register_game(self):
        parent=self.parentWidget()
        if parent and hasattr(parent,'add_library_game'):self.reject();parent.add_library_game()
        else:self.state.setText('Abra Adicionar jogo e cadastre a edição correta antes de vincular a ROM.')
    def save(self):
        if not self.file:return
        try:self.file_id=bind_local(self.library,self.game_id,self.file['local_path'],self.platform.currentData(),self.profile.currentData(),confirmed_title=self.title_confirm.isChecked())
        except (ValueError,OSError) as error:self.state.setText(str(error));return
        self.accept()


class RomSourceDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id;self.outcome=None
        self.setWindowTitle('Vincular ROM');self.resize(460,210)
        layout=QVBoxLayout(self);layout.setContentsMargins(24,24,24,24);layout.setSpacing(12)
        layout.addWidget(text(library.get(game_id)['title'],'sectionTitle'))
        layout.addWidget(action('Escolher ROM local',self.local,True));layout.addWidget(action('Vincular ROM do Drive',self.drive));layout.addWidget(action('Cancelar',self.reject))
    def local(self):
        dialog=LocalRomDialog(self.library,self.game_id,self.parentWidget());dialog.choose_file()
        if dialog.file and dialog.exec()==QDialog.Accepted:
            self.game_id=dialog.game_id;self.outcome={'game_id':dialog.game_id,'file_id':dialog.file_id,'message':'ROM local vinculada.'};self.accept()
    def drive(self):
        from .rom_link_dialog import RomLinkDialog
        dialog=RomLinkDialog(self.library,self.game_id,self)
        if dialog.exec()==QDialog.Accepted:
            self.outcome=dialog.outcome;self.game_id=dialog.game_id;self.accept()

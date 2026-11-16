"""Seleção de perfil para um vínculo existente, sem iniciar ou baixar ROM."""
from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QComboBox, QDialogButtonBox
from .ui_components import text, action
from .local_rom import compatible_profiles


class ExecutionProfileDialog(QDialog):
    def __init__(self,library,game_id,parent=None):
        super().__init__(parent);self.library=library;self.game_id=game_id
        from .dialog_style import prepare_dialog
        prepare_dialog(self)
        self.setWindowTitle('Configurar execução');self.resize(620,320)
        layout=QVBoxLayout(self);layout.setContentsMargins(24,24,24,24);layout.setSpacing(16)
        layout.addWidget(text(library.get(game_id)['title'],'sectionTitle'))
        form=QFormLayout();self.file=QComboBox();self.file.setMinimumWidth(0);self.file.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.profile=QComboBox();self.profile.setObjectName('executionProfile')
        form.addRow('ROM vinculada',self.file);form.addRow('Perfil do emulador',self.profile);layout.addLayout(form)
        self.state=text('','muted');layout.addWidget(self.state)
        layout.addWidget(action('Gerenciar emuladores',self.manage))
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.confirm=buttons.button(QDialogButtonBox.Save);self.confirm.setText('Salvar perfil');self.confirm.setObjectName('primary')
        buttons.button(QDialogButtonBox.Cancel).setText('Cancelar')
        buttons.accepted.connect(self.save);buttons.rejected.connect(self.reject);layout.addWidget(buttons)
        self.files={r['id']:dict(r) for r in library.sql.execute('SELECT * FROM game_files WHERE game_id=? ORDER BY id',(game_id,))}
        for identity,record in self.files.items():self.file.addItem(record['original_name'],identity)
        self.file.currentIndexChanged.connect(self.refresh);self.profile.currentIndexChanged.connect(lambda:self.confirm.setEnabled(bool(self.profile.currentData())))
        self.refresh()
    def refresh(self):
        self.profile.clear();self.profile.addItem('Selecionar perfil',None)
        record=self.files.get(self.file.currentData())
        if not record:self.state.setText('Nenhuma ROM vinculada.');self.confirm.setEnabled(False);return
        self.file.setToolTip(record['original_name'])
        for profile in compatible_profiles(self.library,record['platform'],record['extension']):
            self.profile.addItem(profile['name']+' · '+profile['platform'],profile['id'])
        saved=self.library.sql.execute('SELECT profile_id FROM rom_versions WHERE file_id=?',(record['id'],)).fetchone()
        self.profile.setCurrentIndex(max(0,self.profile.findData(saved[0] if saved else None)))
        self.state.setText('Nenhum perfil compatível. Abra Gerenciar emuladores.' if self.profile.count()==1 else '')
        self.confirm.setEnabled(bool(self.profile.currentData()))
    def manage(self):
        from .emulator_dialog import EmulatorDialog
        EmulatorDialog(self.library,self).exec();self.refresh()
    def save(self):
        record=self.files.get(self.file.currentData());identity=self.profile.currentData()
        current=self.library.sql.execute('SELECT game_id FROM game_files WHERE id=?',(record['id'],)).fetchone() if record else None
        if not current or current[0]!=self.game_id:
            self.state.setText('O vínculo mudou. Feche e selecione novamente.');return
        if not any(p['id']==identity for p in compatible_profiles(self.library,record['platform'],record['extension'])):
            self.state.setText('Selecione um perfil compatível.');return
        with self.library.sql:
            self.library.sql.execute('INSERT INTO rom_versions(file_id,profile_id) VALUES(?,?) ON CONFLICT(file_id) DO UPDATE SET profile_id=excluded.profile_id',(record['id'],identity))
        self.accept()

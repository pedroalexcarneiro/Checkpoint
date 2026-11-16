import json
from pathlib import Path
from PySide6.QtWidgets import (QDialog,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit,QPushButton,QListWidget,QFileDialog,QMessageBox)
from .ui_components import text,action

class EmulatorProfiles(QWidget):
    def __init__(self,library,parent=None):
        super().__init__(parent); self.library=library; self.rows=[]; self.selected_id=None
        self.setObjectName('emulatorProfiles')
        layout=QVBoxLayout(self);layout.setContentsMargins(0,0,0,0);layout.setSpacing(12)
        self.list=QListWidget();self.list.setAccessibleName('Perfis de emuladores');self.list.setMinimumHeight(120);self.list.setMaximumHeight(220)
        layout.addWidget(self.list); self.list.currentRowChanged.connect(self.select)
        self.state=text('','muted');layout.addWidget(self.state)
        form=QFormLayout(); self.name=QLineEdit(); self.platform=QLineEdit(); self.executable=QLineEdit(); self.arguments=QLineEdit('["{rom}"]'); self.extensions=QLineEdit()
        for title,widget in [('Nome',self.name),('Plataforma',self.platform),('Executável',self.executable),('Argumentos (lista JSON)',self.arguments),('Extensões separadas por vírgula',self.extensions)]: form.addRow(title,widget)
        layout.addLayout(form)
        actions=QHBoxLayout()
        for title,callback in [('Escolher executável',self.choose),('Novo perfil',self.reset),('Salvar perfil',self.save)]:
            item=action(title,callback,title=='Salvar perfil');actions.addWidget(item)
        self.remove_button=action('Remover perfil',self.remove);self.remove_button.setEnabled(False);actions.addWidget(self.remove_button)
        layout.addLayout(actions); self.refresh()

    def refresh(self):
        self.rows=[dict(r) for r in self.library.sql.execute('SELECT p.*,e.name,e.executable FROM emulator_profiles p JOIN emulators e ON e.id=p.emulator_id')]
        self.list.clear()
        for row in self.rows:
            missing=not Path(row['executable']).is_file()
            self.list.addItem(row['name']+' · '+row['platform']+(' · Executável ausente' if missing else ''))
            self.list.item(self.list.count()-1).setToolTip(row['executable'])
        self.state.setText('' if self.rows else 'Nenhum perfil. Escolha Novo perfil para configurar um emulador.')
    def select(self,index):
        if index<0: return
        row=self.rows[index]; self.selected_id=row['id']
        self.remove_button.setEnabled(True)
        for key,widget in [('name',self.name),('platform',self.platform),('executable',self.executable),('arguments_json',self.arguments),('extensions',self.extensions)]: widget.setText(row[key])
    def choose(self):
        path,_=QFileDialog.getOpenFileName(self,'Emulador','','Executável (*.exe);;Todos (*)')
        if path: self.executable.setText(path)
    def reset(self):
        self.selected_id=None; self.list.setCurrentRow(-1);self.list.clearSelection();self.remove_button.setEnabled(False)
        for widget in [self.name,self.platform,self.executable,self.extensions]: widget.clear()
        self.arguments.setText('["{rom}"]')
    def save(self):
        try:
            args=json.loads(self.arguments.text())
            if not self.name.text().strip() or not self.platform.text().strip(): raise ValueError('Nome e plataforma são obrigatórios.')
            if not Path(self.executable.text()).is_file(): raise ValueError('Executável não encontrado.')
            if not isinstance(args,list) or not all(isinstance(a,str) for a in args) or not any('{rom}' in a for a in args): raise ValueError('Informe uma lista JSON de argumentos contendo {rom}.')
            with self.library.sql:
                if self.selected_id:
                    row=next(r for r in self.rows if r['id']==self.selected_id)
                    self.library.sql.execute('UPDATE emulators SET name=?,executable=? WHERE id=?',(self.name.text().strip(),self.executable.text(),row['emulator_id']))
                    self.library.sql.execute('UPDATE emulator_profiles SET platform=?,arguments_json=?,extensions=? WHERE id=?',(self.platform.text().strip(),json.dumps(args),self.extensions.text(),self.selected_id))
                else:
                    emulator=self.library.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)',(self.name.text().strip(),self.executable.text())).lastrowid
                    self.library.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',(emulator,self.platform.text().strip(),json.dumps(args),self.extensions.text()))
            self.refresh(); self.reset()
        except (ValueError,TypeError) as error: QMessageBox.warning(self,'Perfil inválido',str(error))

    def remove(self):
        if self.selected_id is None:return
        linked=self.library.sql.execute('SELECT count(*) FROM rom_versions WHERE profile_id=?',(self.selected_id,)).fetchone()[0]
        if linked:
            self.state.setText('Perfil usado por '+str(linked)+' vínculo(s). Selecione outro perfil na execução dessas ROMs antes de remover.')
            return
        if QMessageBox.question(self,'Remover perfil','Remover somente esta configuração? Emulador, ROMs e saves serão preservados.')!=QMessageBox.Yes:return
        with self.library.sql:self.library.sql.execute('DELETE FROM emulator_profiles WHERE id=?',(self.selected_id,))
        self.refresh();self.reset()


class EmulatorDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent);self.setWindowTitle('Perfis de emuladores');self.resize(720,620)
        from .dialog_style import prepare_dialog
        prepare_dialog(self)
        layout=QVBoxLayout(self)
        from .design_system import dialog_heading
        dialog_heading(layout,'Perfis de emuladores',name='settings')
        self.editor=EmulatorProfiles(library,self);layout.addWidget(self.editor)
        layout.addWidget(action('Fechar',self.reject))

from .dialog_style import AppMessages as QMessageBox

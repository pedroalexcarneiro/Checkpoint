import json
from pathlib import Path
from PySide6.QtWidgets import (QDialog,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit,QPushButton,QListWidget,QFileDialog,QMessageBox)

class EmulatorDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent); self.library=library; self.rows=[]; self.selected_id=None
        self.setWindowTitle('Perfis de emuladores'); self.resize(720,620)
        layout=QVBoxLayout(self); self.list=QListWidget(); layout.addWidget(self.list); self.list.currentRowChanged.connect(self.select)
        form=QFormLayout(); self.name=QLineEdit(); self.platform=QLineEdit(); self.executable=QLineEdit(); self.arguments=QLineEdit('["{rom}"]'); self.extensions=QLineEdit()
        for title,widget in [('Nome',self.name),('Plataforma',self.platform),('Executável',self.executable),('Argumentos (lista JSON)',self.arguments),('Extensões separadas por vírgula',self.extensions)]: form.addRow(title,widget)
        layout.addLayout(form)
        actions=QHBoxLayout()
        for title,callback in [('Escolher executável',self.choose),('Novo perfil',self.reset),('Salvar perfil',self.save)]:
            item=QPushButton(title); item.clicked.connect(callback); actions.addWidget(item)
        layout.addLayout(actions); self.refresh()
    def refresh(self):
        self.rows=[dict(r) for r in self.library.sql.execute('SELECT p.*,e.name,e.executable FROM emulator_profiles p JOIN emulators e ON e.id=p.emulator_id')]
        self.list.clear()
        for row in self.rows: self.list.addItem(row['name']+' · '+row['platform'])
    def select(self,index):
        if index<0: return
        row=self.rows[index]; self.selected_id=row['id']
        for key,widget in [('name',self.name),('platform',self.platform),('executable',self.executable),('arguments_json',self.arguments),('extensions',self.extensions)]: widget.setText(row[key])
    def choose(self):
        path,_=QFileDialog.getOpenFileName(self,'Emulador','','Executável (*.exe);;Todos (*)')
        if path: self.executable.setText(path)
    def reset(self):
        self.selected_id=None; self.list.clearSelection()
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

from PySide6.QtWidgets import QDialog,QVBoxLayout,QLabel,QComboBox,QPushButton,QMessageBox
from .integrations.drive import DriveScanner,PLATFORMS


class FolderPlatformDialog(QDialog):
    def __init__(self,library,parent=None):
        super().__init__(parent)
        self.library=library
        self.setWindowTitle('Pastas e plataformas'); self.resize(640,300)
        layout=QVBoxLayout(self)
        text=QLabel('Escolha uma pasta indexada e sua plataforma. Subpastas herdam a escolha; uma regra mais específica tem prioridade. Atualize o Drive para encontrar pastas novas.')
        text.setWordWrap(True);layout.addWidget(text)
        self.folder=QComboBox();self.folder.setObjectName('platformFolder');layout.addWidget(self.folder)
        folders=library.setting('drive_scan',{}).get('folders',{})
        for folder_id,path in sorted(folders.items(),key=lambda item:item[1].casefold()):
            self.folder.addItem(path or 'Pasta principal',folder_id)
        self.platform=QComboBox();self.platform.setEditable(True);self.platform.setObjectName('folderPlatform')
        self.platform.addItems(sorted(set(PLATFORMS.values())));layout.addWidget(self.platform)
        self.state=QLabel();self.state.setWordWrap(True);layout.addWidget(self.state)
        apply=QPushButton('Salvar associação e aplicar aos arquivos');apply.clicked.connect(self.apply);layout.addWidget(apply)
        remove=QPushButton('Remover associação personalizada');remove.clicked.connect(self.remove);layout.addWidget(remove)
        self.folder.currentIndexChanged.connect(self.selected);self.selected()
        from .design_system import dialog_heading
        dialog_heading(layout,'Pastas e plataformas','Uma regra por pasta, herdada pelas subpastas.','folder')

    def selected(self):
        rules=self.library.setting('drive_folder_platforms',{})
        value=rules.get(self.folder.currentData())
        self.state.setText('Associação personalizada: '+value if value else 'Sem associação personalizada. Será usado o nome da pasta ou uma regra herdada.')
        self.platform.setCurrentText(value or '')
    def save(self,value):
        try:
            count=DriveScanner(self.library,None).set_folder_platform(self.folder.currentData(),value)
            self.selected();self.state.setText(f'{count} arquivos reclassificados. Arquivos e jogos associados preservados.')
        except ValueError as error: QMessageBox.warning(self,'Plataforma',str(error))
    def apply(self): self.save(self.platform.currentText())
    def remove(self): self.save(None)

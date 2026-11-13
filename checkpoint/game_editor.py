"""Editor opcional em quatro abas; não expõe um formulário único interminável."""
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,QTabWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLabel,QPushButton,QScrollArea,QGridLayout
from .ui_components import text,action,card
from .design_system import dialog_heading


class ImageEditor(QWidget):
    def __init__(self,dialog,key,title):
        super().__init__();self.dialog=dialog;self.key=key
        row=QVBoxLayout(self);row.setContentsMargins(0,0,0,0);row.setSpacing(10);row.addWidget(text(title,'cardTitle'))
        self.preview=QLabel();self.preview.setAlignment(Qt.AlignCenter);self.preview.setMinimumSize(150,150);self.preview.setMaximumHeight(220);self.preview.setObjectName('addPreviewArt');row.addWidget(self.preview,1)
        line=dialog.fields[key];line.setPlaceholderText('Nenhuma imagem selecionada');row.addWidget(line)
        choose=QPushButton('Escolher imagem');choose.setProperty('gameField',key);choose.clicked.connect(dialog.choose_field);row.addWidget(choose)
        line.textChanged.connect(self.refresh);self.refresh()
    def refresh(self,*args):
        pix=QPixmap(self.dialog.fields[self.key].text())
        if pix.isNull():self.preview.clear();self.preview.setText('Sem imagem')
        else:self.preview.setPixmap(pix.scaled(210,180,Qt.KeepAspectRatio,Qt.SmoothTransformation))


def build_editor(dialog,outer):
    while outer.count():
        item=outer.takeAt(0)
        if item.widget():item.widget().hide()
    dialog.resize(900,690);dialog.setMinimumSize(780,600)
    dialog_heading(outer,'Editar jogo','Ficha, execução, imagens e suas preferências.','library')
    tabs=QTabWidget();tabs.setObjectName('editorTabs');dialog.editor_tabs=tabs
    pages=[]
    for title in ('Ficha','Execução','Imagens','Pessoal'):
        scroll=QScrollArea();scroll.setWidgetResizable(True);body=QWidget();inside=QVBoxLayout(body);inside.setContentsMargins(4,20,6,8);inside.setSpacing(16);scroll.setWidget(body);tabs.addTab(scroll,title);pages.append(inside)
    ficha,run,images,personal=pages
    # Reparent the existing fields so validation/data contracts stay identical.
    for field in dialog.fields.values():dialog.form.removeWidget(field);field.show()
    form=QFormLayout();form.setSpacing(12);form.addRow('Nome',dialog.fields['title']);form.addRow('Plataforma',dialog.fields['platform']);ficha.addLayout(form)
    pair=QHBoxLayout()
    for fields in [[('Desenvolvedora','developer'),('Gênero','genre')],[('Publicadora','publisher'),('Lançamento','release_date')]]:
        box=QWidget();form=QFormLayout(box);form.setContentsMargins(0,0,0,0);form.setSpacing(12)
        for title,key in fields:form.addRow(title,dialog.fields[key])
        pair.addWidget(box)
    ficha.addLayout(pair);ficha.addWidget(text('Descrição','muted'));dialog.fields['description'].setMaximumHeight(180);dialog.fields['description'].setMinimumHeight(120);ficha.addWidget(dialog.fields['description']);ficha.addStretch()
    frame,inside=card();inside.addWidget(text('Como abrir este jogo','sectionTitle'));inside.addWidget(text('Escolha o executável local. ROMs e perfis de emuladores ficam na aba Arquivos da ficha.','muted'))
    row=QHBoxLayout();row.addWidget(dialog.fields['executable'],1);choose=QPushButton('Escolher executável');choose.setProperty('gameField','executable');choose.clicked.connect(dialog.choose_field);row.addWidget(choose);inside.addLayout(row);run.addWidget(frame)
    form=QFormLayout();form.addRow('Origem',dialog.fields['source']);form.addRow('Categoria',dialog.fields['category']);run.addLayout(form);run.addStretch()
    row=QHBoxLayout();row.setSpacing(20)
    for key,title in [('cover','Capa'),('banner','Banner'),('logo','Logo')]:row.addWidget(ImageEditor(dialog,key,title),1)
    images.addLayout(row);images.addWidget(text('Capa na biblioteca; banner e logo na página do jogo. As imagens originais são preservadas.','caption'));images.addStretch()
    form=QFormLayout();form.setSpacing(14)
    for title,key in [('Status','status'),('Nota pessoal','rating'),('Favorito','favorite')]:
        if key=='status' and not dialog.owned:dialog.fields[key].hide();continue
        form.addRow(title,dialog.fields[key])
    personal.addLayout(form);personal.addWidget(text('Suas observações','cardTitle'));dialog.fields['notes'].setMaximumHeight(220);dialog.fields['notes'].setMinimumHeight(120);personal.addWidget(dialog.fields['notes']);personal.addStretch()
    outer.addWidget(tabs,1);dialog.error.show();outer.addWidget(dialog.error)
    footer=QHBoxLayout()
    if hasattr(dialog,'catalog_button'):dialog.catalog_button.setText('Identificar jogo');dialog.catalog_button.setObjectName('quiet');dialog.catalog_button.show();footer.addWidget(dialog.catalog_button)
    footer.addStretch();dialog.buttons.show();footer.addWidget(dialog.buttons);outer.addLayout(footer)

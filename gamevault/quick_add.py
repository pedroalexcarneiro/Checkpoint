"""Cadastro amplo com busca única, prévia e enriquecimento em segundo plano."""
from functools import partial
from PySide6.QtCore import QObject,Qt,QTimer,Slot,QSize,QEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,
    QListWidget,QListWidgetItem,QComboBox,QFrame,QDialogButtonBox)
from .jobs import Job
from .worker import run_isolated
from .integrations import MetadataResult
from .automatic_catalog import best_match,normalized
from .ui_components import text,action


class QuickAdd(QObject):
    def __init__(self,dialog,outer,allow_steam):
        super().__init__(dialog);self.dialog=dialog;self.library=dialog.library
        self.generation=0;self.jobs=[];self.suspend=False;self.closed=False;self.pending_show_lookup=False;self.pending_search=False;self.pending_details=None
        self.candidates=[];self.local=[];self.owner=dialog
        while self.owner.parentWidget() is not None:self.owner=self.owner.parentWidget()
        while outer.count():
            item=outer.takeAt(0)
            if item.widget():item.widget().hide()
        dialog.resize(1040,720);dialog.setMinimumSize(850,620)
        from .window_style import titlebar_theme
        titlebar_theme(dialog,self.library.setting('appearance.theme','green')!='white')
        outer.setContentsMargins(28,24,28,22);outer.setSpacing(18)
        head=QHBoxLayout();head.addWidget(text('Adicionar jogo','pageTitle'));head.addStretch()
        if allow_steam:
            steam=action('Importar da Steam',dialog.request_steam);steam.setObjectName('quiet');head.addWidget(steam)
        outer.addLayout(head)
        search=QHBoxLayout();self.query=dialog.fields['title'];dialog.form.removeWidget(self.query)
        self.query.setParent(dialog);self.query.setObjectName('gameSearch');self.query.setPlaceholderText('Qual jogo você quer adicionar?');self.query.show()
        self.query.setMinimumHeight(46);search.addWidget(self.query,1)
        self.platform=QComboBox();self.platform.addItem('Todas as plataformas','')
        for name in sorted({row['platform'] for row in self.library.sql.execute('SELECT DISTINCT platform FROM game_files') if row['platform']}|{'PC','Nintendo Switch','Nintendo DS','Game Boy Advance','Super Nintendo','PlayStation','PlayStation 2'}):self.platform.addItem(name,name)
        self.platform.setMinimumWidth(180);search.addWidget(self.platform)
        button=action('Buscar',self.lookup,True);search.addWidget(button);outer.addLayout(search)
        body=QHBoxLayout();body.setSpacing(24)
        left=QWidget();column=QVBoxLayout(left);column.setContentsMargins(0,0,0,0);column.setSpacing(10)
        column.addWidget(text('Resultados','cardTitle'));self.results=QListWidget();self.results.setObjectName('gameSearchResults');self.results.setMinimumWidth(330);self.results.setSpacing(4);column.addWidget(self.results,1)
        self.state=text('Digite um nome. Ficha e imagens são buscadas automaticamente.','muted')
        from .task_status import BusyIndicator
        from .theme import get_theme
        self.busy=BusyIndicator(get_theme(self.library.setting('appearance.theme','green')));self.busy.hide()
        status=QHBoxLayout();status.addWidget(self.busy);status.addWidget(self.state,1);column.addLayout(status)
        body.addWidget(left,3)
        preview=QFrame();preview.setObjectName('addPreview');preview.setMinimumWidth(290);right=QVBoxLayout(preview);right.setContentsMargins(22,22,22,22);right.setSpacing(14)
        self.art=QLabel();self.art.setObjectName('addPreviewArt');self.art.setFixedSize(150,225);self.art.setAlignment(Qt.AlignCenter);self.art.setText('Prévia');right.addWidget(self.art,0,Qt.AlignHCenter)
        self.title=text('Seu próximo jogo','sectionTitle');right.addWidget(self.title)
        self.facts=text('Selecione um resultado para conferir a ficha.','muted');right.addWidget(self.facts)
        self.description=text('','bodyText');right.addWidget(self.description)
        self.association=text('','caption');right.addWidget(self.association);right.addStretch()
        self.edit=action('Ajustar detalhes',self.edit_details);self.edit.setObjectName('quiet');right.addWidget(self.edit)
        body.addWidget(preview,2);outer.addLayout(body,1)
        dialog.error.setWordWrap(True);dialog.error.show();outer.addWidget(dialog.error)
        footer=QHBoxLayout();footer.addWidget(text('Capa, banner, logo e dados disponíveis são preenchidos ao adicionar.' if self.library.setting('artwork.auto',True) else 'Preenchimento de imagens desativado nas Configurações.','caption'),1)
        self.save=dialog.buttons.button(QDialogButtonBox.Save);self.cancel=dialog.buttons.button(QDialogButtonBox.Cancel)
        dialog.buttons.setParent(dialog);dialog.buttons.show();footer.addWidget(dialog.buttons);outer.addLayout(footer)
        for control in dialog.findChildren(QPushButton):control.setAutoDefault(False);control.setDefault(False)
        dialog.complete_on_save.setChecked(bool(self.library.setting('artwork.auto',True)))
        self.timer=QTimer(self);self.timer.setSingleShot(True);self.timer.setInterval(550);self.timer.timeout.connect(self.lookup)
        self.dialog.installEventFilter(self)
        self.query.installEventFilter(self)
        self.query.textChanged.connect(self.changed);self.query.returnPressed.connect(self.lookup)
        self.platform.currentIndexChanged.connect(self.platform_changed)
        self.results.currentRowChanged.connect(self.choose)
        dialog.finished.connect(self.finished);self.query.setFocus()
        dialog.fields['platform'].setText('')

    def eventFilter(self,watched,event):
        if not hasattr(self,'dialog'):return False
        if watched is self.dialog and event.type()==QEvent.Show and self.pending_show_lookup:
            self.pending_show_lookup=False;QTimer.singleShot(0,self.lookup)
        if watched is self.query and event.type()==QEvent.KeyPress and event.key() in (Qt.Key_Return,Qt.Key_Enter):
            self.lookup();return True
        return super().eventFilter(watched,event)

    @Slot(int)
    def finished(self,result):self.closed=True;self.timer.stop()

    @Slot(str)
    def changed(self,value):
        if self.suspend:return
        self.dialog.error.clear()
        self.generation+=1;self.dialog.catalog_result=None;self.dialog.drive_file_id=None
        for key in ('description','genre','developer','publisher','release_date','cover','banner','logo','executable'):
            self.dialog.fields[key].clear()
        self.dialog.fields['source'].setText('Manual');self.dialog.fields['platform'].setText(self.platform.currentData() or '')
        self.title.setText(value.strip() or 'Seu próximo jogo');self.art.clear();self.art.setText('Prévia');self.facts.setText('Buscando pelo nome…' if len(value.strip())>=2 else 'Selecione um resultado para conferir a ficha.')
        self.association.clear();self.description.clear();self.results.clear();self.candidates=[]
        self.local_results()
        if len(value.strip())>=2:self.timer.start()
        else:self.timer.stop();self.state.setText('Digite pelo menos duas letras.')

    @Slot(int)
    def platform_changed(self,index):
        self.dialog.fields['platform'].setText(self.platform.currentData() or '')
        self.changed(self.query.text())

    def local_results(self):
        from .integrations.drive import normalize_rom_name
        from .automatic_catalog import normalized
        query=normalized(self.query.text());platform=self.platform.currentData()
        rows=self.library.sql.execute('SELECT * FROM game_files WHERE drive_id IS NOT NULL ORDER BY original_name')
        self.local=[dict(row) for row in rows if query and query in normalized(normalize_rom_name(row['original_name'])) and (not platform or platform==row['platform'])][:40]
        self.results.blockSignals(True);self.results.clear()
        for row in self.local:
            item=QListWidgetItem(normalize_rom_name(row['original_name'])+'\nDisponível no Drive · '+(row['platform'] or 'Plataforma não definida'))
            item.setSizeHint(QSize(0,60));item.setToolTip(row['original_name']);self.results.addItem(item)
        self.results.blockSignals(False)

    @Slot()
    def lookup(self):
        self.timer.stop()
        if self.closed or len(self.query.text().strip())<2:return
        if not self.dialog.isVisible():self.pending_show_lookup=True;return
        if any(job.property('operation')=='catalog_search' for job in self.jobs):self.pending_search=True;return
        self.pending_search=False;self.state.setText('Buscando jogos e versões disponíveis…')
        self.run('catalog_search',title=self.query.text().strip(),platform=self.dialog.fields['platform'].text())

    def run(self,operation,**arguments):
        if operation=='catalog_details' and any(job.property('operation')==operation for job in self.jobs):
            self.pending_details=(self.generation,arguments);return
        job=Job(partial(run_isolated,operation,self.library.db.path,**arguments),self.owner)
        job.setProperty('generation',self.generation);job.setProperty('operation',operation)
        self.busy.show()
        self.jobs.append(job);job.succeeded.connect(self.received);job.failed.connect(self.failed);job.finished.connect(self.job_finished);job.start()

    @Slot(object)
    def received(self,payload):
        job=self.sender()
        if self.closed or job.property('generation')!=self.generation:return
        if job.property('operation')=='catalog_search':
            self.candidates=[MetadataResult(**row) for row in payload['results']];self.local_results()
            self.results.blockSignals(True)
            for result in self.candidates:
                platforms=' / '.join(result.platforms[:3]) or 'Jogo'
                item=QListWidgetItem(result.title+'\n'+platforms+(' · '+result.release_date[:4] if result.release_date else ''));item.setSizeHint(QSize(0,60));self.results.addItem(item)
            self.results.blockSignals(False)
            self.state.setText('Escolha o jogo ou a versão do Drive.' if self.candidates or self.local else 'Nenhum resultado disponível. Você pode adicionar pelo nome e completar depois.')
            if payload.get('unavailable'):self.state.setText(self.state.text()+' Parte dos catálogos está indisponível.')
            # Nunca seleciona uma ROM automaticamente. Uma ficha inequívoca pode ser sugerida.
            match=best_match(self.query.text(),self.dialog.fields['platform'].text(),self.candidates)
            if self.dialog.drive_file_id is not None and match and normalized(match.title)!=normalized(self.query.text()):match=None
            if match:self.results.setCurrentRow(len(self.local)+self.candidates.index(match))
        else:
            result=MetadataResult(**payload['result']);self.dialog.apply_catalog(result)
            self.show_result(result)
            path=payload.get('preview',{}).get('cover')
            if path:self.art.setPixmap(QPixmap(path).scaled(self.art.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            self.state.setText('Ficha preenchida. Imagens disponíveis serão aplicadas ao adicionar.')

    @Slot(str)
    def failed(self,message):
        if not self.closed and self.sender().property('generation')==self.generation:self.state.setText('A consulta não foi concluída. Você pode adicionar agora e tentar completar depois.')

    @Slot()
    def job_finished(self):
        job=self.sender();self.jobs.remove(job);job.deleteLater()
        self.busy.setVisible(bool(self.jobs))
        if not self.jobs and hasattr(self,'deferred_result'):
            self.dialog.done(self.deferred_result);return
        if self.pending_search and not self.closed:self.lookup()
        if self.pending_details and not self.closed:
            generation,arguments=self.pending_details;self.pending_details=None
            if generation==self.generation:self.run('catalog_details',**arguments)

    @Slot(int)
    def choose(self,index):
        if index<0:return
        if index<len(self.local):self.dialog.load_drive_file(self.local[index]);return
        offset=index-len(self.local)
        if offset>=len(self.candidates):return
        result=self.candidates[offset];self.generation+=1;self.art.clear();self.art.setText('Carregando prévia…')
        self.dialog.apply_catalog(result)
        if not self.dialog.fields['platform'].text() and result.platforms:self.dialog.fields['platform'].setText('PC' if 'PC' in result.platforms else result.platforms[0])
        self.show_result(result);self.state.setText('Preenchendo ficha e prévia… Você já pode adicionar o jogo.')
        self.run('catalog_details',provider=result.provider,identity=result.external_id,platform=self.dialog.fields['platform'].text())

    def show_result(self,result):
        self.title.setText(result.title)
        details=[self.dialog.fields['platform'].text() or ' / '.join(result.platforms[:3]),result.developer,result.release_date[:4]]
        self.facts.setText(' · '.join(value for value in details if value));self.description.setText(result.description[:260])

    def drive_loaded(self,file):
        self.art.clear();self.art.setText('Prévia')
        self.generation+=1;self.title.setText(self.query.text());self.facts.setText(file['platform'] or 'Plataforma não definida');self.description.clear()
        self.association.setText('ROM selecionada · '+file['original_name']);self.state.setText('ROM selecionada. Buscando a ficha para esta plataforma…');self.lookup()

    def use_name(self):
        self.timer.stop();self.generation+=1;self.state.setText('Pronto para adicionar. Ficha e imagens serão buscadas em segundo plano.');self.dialog.validate()

    def edit_details(self):
        # Editor existente é opcional; nenhuma escolha de provedor é necessária.
        from .dialogs import GameDialog
        editor=GameDialog(self.dialog,self.dialog.data(),self.library)
        if editor.exec()==editor.Accepted:
            self.suspend=True
            for key,value in editor.data().items():
                widget=self.dialog.fields[key]
                if hasattr(widget,'setPlainText'):widget.setPlainText(value or '')
                elif hasattr(widget,'setCurrentText'):widget.setCurrentText(value or '')
                elif hasattr(widget,'setChecked'):widget.setChecked(bool(value))
                elif hasattr(widget,'setValue'):widget.setValue(value if value is not None else -1)
                else:widget.setText(value or '')
            if editor.catalog_result:self.dialog.catalog_result=editor.catalog_result
            self.suspend=False;self.title.setText(self.query.text())

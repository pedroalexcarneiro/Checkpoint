from .locale import count_text
"""Cadastro amplo com busca única, prévia e enriquecimento em segundo plano."""
from functools import partial
from PySide6.QtCore import QObject,Qt,QTimer,Slot,QSize,QEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,
    QListWidget,QListWidgetItem,QLineEdit,QComboBox,QFrame,QDialogButtonBox)
from .jobs import Job
from .worker import run_isolated
from .integrations import MetadataResult
from .automatic_catalog import best_match,normalized
from .ui_components import text,action


class QuickAdd(QObject):
    def __init__(self,dialog,outer,allow_steam):
        super().__init__(dialog);self.dialog=dialog;self.library=dialog.library
        self.generation=0;self.jobs=[];self.finishing=False;self.suspend=False;self.closed=False;self.pending_show_lookup=False;self.pending_search=False;self.pending_details=None
        self.candidates=[];self.local=[];self.drive_catalog=False;self.metadata_unavailable=False;self.owner=dialog
        while self.owner.parentWidget() is not None:self.owner=self.owner.parentWidget()
        while outer.count():
            item=outer.takeAt(0)
            if item.widget():item.widget().hide()
        dialog.resize(620,600);dialog.setMinimumSize(560,600);dialog.setObjectName('quickAddDialog');dialog.setWindowFlag(Qt.FramelessWindowHint,True)
        from .window_style import titlebar_theme
        from .ui_components import nav_icon,service_icon
        from .theme import get_theme
        from PySide6.QtGui import QIcon
        from .settings_view import disclosure
        titlebar_theme(dialog,True)
        outer.setContentsMargins(22,20,22,18);outer.setSpacing(12)
        from .window_style import DialogTitleBar
        outer.addWidget(DialogTitleBar(dialog))
        self.sources=dialog.source_tabs;self.sources.setParent(dialog);self.sources.show()
        self.sources.setCurrentIndex(0);self.sources.setObjectName('sourceTabs')
        color=get_theme(self.library.setting('appearance.theme','green')).colors['text']
        self.sources.setTabIcon(0,nav_icon('search',color))
        self.sources.setTabIcon(1,QIcon(service_icon('Google Drive')))
        self.sources.setTabIcon(2,QIcon(service_icon('Steam')))
        self.sources.setIconSize(QSize(22,22));outer.addWidget(self.sources)
        self.query=dialog.fields['title'];dialog.form.removeWidget(self.query)
        self.query.setParent(dialog);self.query.setObjectName('gameSearch');self.query.setPlaceholderText('Pesquisar jogo…');self.query.show()
        self.query.setClearButtonEnabled(True);self.query.setMinimumHeight(40);self.query.addAction(nav_icon('search',color),QLineEdit.LeadingPosition);outer.addWidget(self.query)
        self.results=QListWidget();self.results.setObjectName('gameSearchResults');self.results.setSpacing(4);self.results.setMinimumHeight(100);self.results.setMaximumHeight(180);self.results.hide();outer.addWidget(self.results)
        self.preview=QFrame();self.preview.setObjectName('addPreview');self.preview.setMinimumHeight(116);preview=QHBoxLayout(self.preview);preview.setContentsMargins(14,10,14,10);preview.setSpacing(16)
        self.art=QLabel();self.art.setObjectName('addPreviewArt');self.art.setFixedSize(70,94);self.art.setAlignment(Qt.AlignCenter);self.art.setText('Sem capa');preview.addWidget(self.art)
        words=QVBoxLayout();words.setSpacing(6);self.title=text('Nenhum jogo selecionado','sectionTitle');words.addWidget(self.title)
        self.facts=text('','muted');words.addWidget(self.facts)
        self.description=text('','bodyText');self.description.hide()
        self.association=text('','caption');self.association.hide();words.addWidget(self.association);preview.addLayout(words,1)
        self.confirmed=text('✓','selectedCheck');self.confirmed.setAlignment(Qt.AlignCenter);self.confirmed.setFixedSize(28,28);self.confirmed.hide();preview.addWidget(self.confirmed);outer.addWidget(self.preview)
        self.other=action('Escolher outro resultado',self.show_choices);self.other.setObjectName('resultLink');self.other.hide();outer.addWidget(self.other,0,Qt.AlignHCenter)
        from .task_status import BusyIndicator
        self.state=text('','muted')
        self.busy=BusyIndicator(get_theme(self.library.setting('appearance.theme','green')));self.busy.hide()
        status=QHBoxLayout();status.addWidget(self.busy);status.addWidget(self.state,1);outer.addLayout(status)
        self.steam_panel=dialog.steam_panel;self.steam_panel.setParent(dialog);outer.addWidget(self.steam_panel);self.steam_panel.hide()
        self.drive_manage=action('Atualizar índice do Drive',self.manage_drive);self.drive_manage.setObjectName('quiet');outer.addWidget(self.drive_manage,0,Qt.AlignLeft);self.drive_manage.hide()
        self.manual=action('Pesquisar manualmente',self.manual_search);self.manual.hide();outer.addWidget(self.manual,0,Qt.AlignLeft)
        advanced=QWidget();advanced_row=QVBoxLayout(advanced);advanced_row.setContentsMargins(0,0,0,0);advanced_row.setSpacing(10)
        self.platform=QComboBox();self.platform.setMinimumSize(220,40);self.platform.setSizeAdjustPolicy(QComboBox.AdjustToContents);self.platform.addItem('Todas as plataformas','')
        for name in sorted({row['platform'] for row in self.library.sql.execute('SELECT DISTINCT platform FROM game_files') if row['platform']}|{'PC','Nintendo Switch','Nintendo DS','Game Boy Advance','Super Nintendo','PlayStation','PlayStation 2'}):self.platform.addItem(name,name)
        platform_row=QHBoxLayout();platform_row.addWidget(text('Plataforma'));platform_row.addWidget(self.platform,1);advanced_row.addLayout(platform_row)
        dialog.complete_on_save.setParent(dialog);dialog.complete_on_save.hide()
        self.automation=QWidget();info=QHBoxLayout(self.automation);info.setContentsMargins(0,0,0,0);badge=QLabel();badge.setPixmap(nav_icon('download',color).pixmap(18,18));info.addWidget(badge);info.addWidget(text('Ficha e imagens serão buscadas automaticamente','caption'),1);outer.addWidget(self.automation)
        self.advanced=disclosure('Opções avançadas',advanced,outer);self.advanced.setObjectName('addDisclosure');self.advanced.setMinimumWidth(dialog.minimumWidth()-44)
        outer.addStretch()
        dialog.error.setWordWrap(True);dialog.error.show();outer.addWidget(dialog.error)
        self.save=dialog.buttons.button(QDialogButtonBox.Save);self.save.setText('Salvar desejo' if dialog.purpose=='wish' else 'Adicionar à biblioteca');self.save.setEnabled(False);self.cancel=dialog.buttons.button(QDialogButtonBox.Cancel)
        # Ordem explícita: Cancelar à esquerda, ação principal à direita em todos os SO.
        dialog.buttons.removeButton(self.save);dialog.buttons.removeButton(self.cancel)
        self.save.setParent(dialog);self.cancel.setParent(dialog);self.save.clicked.connect(dialog.validate);self.cancel.clicked.connect(dialog.reject)
        dialog.buttons.setParent(dialog);dialog.buttons.hide()
        footer=QHBoxLayout();footer.addStretch();footer.addWidget(self.cancel);footer.addWidget(self.save);self.cancel.show();self.save.show();outer.addLayout(footer)
        self.sources.currentChanged.connect(self.source_changed)
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

    def show_choices(self):
        self.results.show();self.preview.hide();self.other.hide();self.confirmed.hide()
        self.dialog.adjustSize()

    @Slot(int)
    def source_changed(self,index):
        self.timer.stop();self.generation+=1;self.pending_search=False;self.pending_details=None
        self.dialog.drive_file_id=None;self.dialog.catalog_result=None;self.drive_catalog=False;self.metadata_unavailable=False;self.manual.hide()
        self.query.setVisible(index!=2);self.preview.setVisible(index==0);self.results.setVisible(index==1)
        self.steam_panel.setVisible(index==2);self.drive_manage.setVisible(index==1)
        self.advanced.setVisible(index!=2);self.automation.setVisible(index!=2);self.save.setVisible(index!=2);self.save.setEnabled(False);self.other.hide();self.confirmed.hide()
        self.query.setPlaceholderText('Pesquisar ROM no índice do Drive…' if index==1 else 'Pesquisar jogo…')
        if index!=2:self.changed(self.query.text())
        else:self.state.clear()

    def manage_drive(self):
        self.dialog.manage_drive();self.local_results();self.results.show()

    def eventFilter(self,watched,event):
        if not hasattr(self,'dialog'):return False
        if watched is self.dialog and event.type()==QEvent.Resize:self.advanced.setFixedWidth(max(0,event.size().width()-44))
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
        self.dialog.error.clear();self.save.setEnabled(False)
        self.generation+=1;self.dialog.catalog_result=None
        preserve_rom=self.drive_catalog and self.dialog.drive_file_id is not None and self.sources.currentIndex()==1
        if not preserve_rom:self.dialog.drive_file_id=None
        self.metadata_unavailable=False;self.manual.hide()
        for key in ('description','genre','developer','publisher','release_date','cover','banner','logo','executable'):
            self.dialog.fields[key].clear()
        self.dialog.fields['source'].setText('Não identificada' if preserve_rom else 'Manual')
        if not preserve_rom:self.dialog.fields['platform'].setText(self.platform.currentData() or '')
        self.title.setText(value.strip() or 'Nenhum jogo selecionado');self.art.clear();self.art.setText('Prévia');self.facts.clear()
        if not preserve_rom:self.association.clear();self.association.hide()
        self.description.clear();self.results.clear();self.candidates=[];self.confirmed.hide();self.other.hide();self.preview.hide()
        self.local_results()
        if len(value.strip())>=2 and (self.sources.currentIndex()==0 or preserve_rom):self.state.setText('Buscando…');self.timer.start()
        elif self.sources.currentIndex()==1:
            self.save.setEnabled(False);self.results.show()
            self.state.setText(count_text(len(self.local),'ROM','ROMs') if self.local else 'Nenhuma ROM encontrada')
        else:self.timer.stop();self.state.clear()

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
        if self.sources.currentIndex()==0 or self.dialog.drive_file_id is not None:self.local=[]
        for row in self.local:
            item=QListWidgetItem(row['original_name']+'\nDisponível no Drive · '+(row['platform'] or 'Plataforma não definida'))
            item.setSizeHint(QSize(0,60));item.setToolTip(row['original_name']);self.results.addItem(item)
        self.results.blockSignals(False)
        if self.local:self.results.show()

    @Slot()
    def lookup(self):
        self.timer.stop()
        if self.closed or len(self.query.text().strip())<2:return
        if self.sources.currentIndex()==1 and self.dialog.drive_file_id is None:self.local_results();return
        if not self.dialog.isVisible():self.pending_show_lookup=True;return
        if any(job.property('operation')=='catalog_search' for job in self.jobs):self.pending_search=True;return
        self.pending_search=False;self.preview.hide();self.results.hide();self.state.setText('Buscando…')
        if self.dialog.drive_file_id is not None:self.save.setEnabled(False)
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
            if self.finishing:return
            self.candidates=[MetadataResult(**row) for row in payload['results']];self.local_results()
            self.results.blockSignals(True)
            for result in self.candidates:
                platforms=' / '.join(result.platforms[:3]) or 'Jogo'
                item=QListWidgetItem(result.title+'\n'+platforms+(' · '+result.release_date[:4] if result.release_date else ''));item.setSizeHint(QSize(0,60));self.results.addItem(item)
            self.results.blockSignals(False)
            self.state.setText('' if self.candidates or self.local else 'Nenhum resultado')
            if not self.candidates and not self.local:
                if self.dialog.drive_file_id is not None:
                    self.show_missing_metadata()
                else:self.preview.hide();self.results.hide();self.facts.clear();self.save.setEnabled(False)
            if payload.get('unavailable') and not self.metadata_unavailable:self.state.setText(self.state.text()+' Parte dos catálogos está indisponível.')
            # Nunca seleciona uma ROM automaticamente. Uma ficha inequívoca pode ser sugerida.
            match=best_match(self.query.text(),self.dialog.fields['platform'].text(),self.candidates)
            if self.dialog.drive_file_id is not None and match and normalized(match.title)!=normalized(self.query.text()):match=None
            if match:self.results.setCurrentRow(len(self.local)+self.candidates.index(match))
            elif self.candidates or self.local:self.show_choices()
        else:
            result=MetadataResult(**payload['result']);self.dialog.apply_catalog(result)
            self.show_result(result)
            path=payload.get('preview',{}).get('cover')
            if path:self.art.setPixmap(QPixmap(path).scaled(self.art.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            self.state.clear()
            if self.dialog.drive_file_id is not None and not all((result.description,result.developer,result.publisher)):
                self.show_missing_metadata()

    @Slot(str)
    def failed(self,message):
        if not self.closed and self.sender().property('generation')==self.generation:
            if self.dialog.drive_file_id is not None:self.show_missing_metadata()
            else:self.state.setText('Consulta indisponível')

    @Slot()
    def job_finished(self):
        job=self.sender();self.jobs.remove(job);job.deleteLater()
        self.busy.setVisible(bool(self.jobs))
        if self.pending_search and not self.closed and not self.finishing:self.lookup()
        if self.pending_details and not self.closed:
            generation,arguments=self.pending_details;self.pending_details=None
            if generation==self.generation:self.run('catalog_details',**arguments)
        if not self.jobs and hasattr(self,'deferred_result'):
            self.closed=True;self.dialog.done(self.deferred_result)

    @Slot(int)
    def choose(self,index):
        if index<0:return
        if index<len(self.local):self.dialog.load_drive_file(self.local[index]);return
        offset=index-len(self.local)
        if offset>=len(self.candidates):return
        result=self.candidates[offset];self.generation+=1;self.art.clear();self.art.setText('Carregando prévia…')
        self.dialog.apply_catalog(result)
        if not self.dialog.fields['platform'].text() and result.platforms:self.dialog.fields['platform'].setText('PC' if 'PC' in result.platforms else result.platforms[0])
        self.show_result(result);self.state.setText('Carregando ficha…')
        if self.dialog.drive_file_id is not None:self.save.setEnabled(False)
        self.run('catalog_details',provider=result.provider,identity=result.external_id,platform=self.dialog.fields['platform'].text())

    def show_result(self,result):
        self.metadata_unavailable=False;self.manual.hide()
        self.save.setEnabled(not self.finishing);self.preview.show();self.results.hide();self.other.setVisible(bool(self.candidates));self.confirmed.show()
        self.title.setText(result.title)
        details=[self.dialog.fields['platform'].text() or ' / '.join(result.platforms[:3]),result.developer,result.release_date[:4]]
        self.facts.setText(' · '.join(value for value in details if value));self.description.setText(result.description[:260])

    def drive_loaded(self,file):
        self.art.clear();self.art.setText('Prévia')
        self.generation+=1;self.title.setText(self.query.text());self.facts.setText(file['platform'] or 'Plataforma não definida');self.description.clear()
        self.drive_catalog=True;self.metadata_unavailable=False;self.manual.hide();self.save.setEnabled(False)
        self.association.setText('ROM selecionada · '+file['original_name']);self.association.show();self.preview.show();self.results.hide();self.state.setText('ROM selecionada. Buscando a ficha para esta plataforma…');self.lookup()

    def show_missing_metadata(self):
        self.metadata_unavailable=True;self.preview.show();self.save.setEnabled(not self.finishing)
        self.state.setText('Não encontramos dados para este jogo. Pesquise manualmente.')
        self.manual.show()

    def manual_search(self):
        # Pesquisar novamente não remove nem troca o vínculo da ROM selecionada.
        self.drive_catalog=True;self.query.setPlaceholderText('Pesquisar dados do jogo…')
        self.query.setFocus();self.query.selectAll();self.lookup()

    def use_name(self):
        self.timer.stop();self.generation+=1;self.state.clear();self.dialog.validate()

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
                else:
                    from .locale import date_display
                    widget.setText(date_display(value) if key=='release_date' else value or '')
            if editor.catalog_result:self.dialog.catalog_result=editor.catalog_result
            self.suspend=False;self.title.setText(self.query.text())

"""Acompanhamento reutilizável; destruir a tela não cancela a fila do aplicativo."""
from pathlib import Path
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QProgressBar,QPushButton
from .design_system import CardSurface
from .ui_components import text,action


STAGES={'queued':'Na fila','authorizing':'Autorizando Drive','downloading':'Baixando',
        'checking_existing':'Conferindo arquivo existente','received':'Recebido · aguardando verificação',
        'waiting':'Aguardando servidor','verifying':'Verificando arquivo',
        'registering':'Confirmando arquivo','downloaded':'Arquivo verificado',
        'linking':'Vinculando ROM','linked':'ROM vinculada','metadata':'Consultando metadados',
        'metadata_pending':'ROM pronta · metadados pendentes','completed':'Concluído',
        'failed':'Falha','cancelled':'Cancelado','interrupted':'Interrompido'}


def byte_text(value):
    value=max(0,float(value or 0))
    for suffix in ('B','KiB','MiB','GiB','TiB'):
        if value<1024 or suffix=='TiB':return f'{value:.1f} {suffix}'.replace('.',',') if suffix!='B' else f'{int(value)} B'
        value/=1024


class TransferCard(CardSurface):
    def __init__(self,manager,task,parent=None,*,allow_retry=True):
        super().__init__(parent);self.manager=manager;self.task=task
        self.allow_retry=allow_retry
        self.setObjectName('transferCard')
        layout=QVBoxLayout(self);layout.setContentsMargins(16,16,16,16);layout.setSpacing(8)
        head=QHBoxLayout();self.title=text(task.title,'cardTitle');head.addWidget(self.title,1)
        self.cancel=action('Cancelar',lambda: self.request_cancel());head.addWidget(self.cancel)
        self.retry=action('Tentar novamente',self.restart);head.addWidget(self.retry)
        layout.addLayout(head)
        self.filename=text(task.file_name,'muted');layout.addWidget(self.filename)
        row=QHBoxLayout();self.stage=text('','caption');row.addWidget(self.stage,1)
        self.percent=text('','caption');row.addWidget(self.percent);layout.addLayout(row)
        self.bar=QProgressBar();self.bar.setObjectName('transferProgress');self.bar.setTextVisible(False);self.bar.setFixedHeight(8)
        layout.addWidget(self.bar)
        self.metrics=text('','caption');layout.addWidget(self.metrics)
        self.steps=text('','caption');layout.addWidget(self.steps)
        self.message=text('','muted');layout.addWidget(self.message)
        self.folder=action('Abrir pasta',self.open_folder);layout.addWidget(self.folder,0,Qt.AlignLeft)
        manager.updated.connect(self.changed)
        self.render()

    def changed(self,task):
        if task.id==self.task.id:self.render()

    def request_cancel(self):
        from .dialog_style import AppMessages
        try:self.manager.cancel(self.task.id)
        except ValueError as error:AppMessages.warning(self,'Cancelar download',str(error))

    def restart(self):
        from .dialog_style import AppMessages
        try:self.manager.start(self.task.file_id,self.task.game_id,mode=self.task.mode,directory=self.task.directory)
        except ValueError as error:AppMessages.warning(self,'Downloads',str(error))

    def open_folder(self):
        path=self.task.outcome.get('local_path') or self.task.progress.get('local_path') or self.task.progress.get('partial_path')
        if path:QDesktopServices.openUrl(QUrl.fromLocalFile(str(Path(path).parent)))

    def render(self):
        task=self.task;progress=task.progress;outcome=task.outcome
        stage=progress.get('stage','queued') if task.active else task.status
        label=STAGES.get(stage,stage)
        if task.status=='partial':label='ROM pronta · metadados pendentes' if outcome.get('link_state')=='linked' else 'Arquivo baixado · vínculo pendente'
        if task.cancel_requested and task.active:label='Cancelando · aguardando a operação atual'
        if task.stalled and task.active:label='Sem atualização de progresso há mais de 60 s. Aguarde ou cancele.'
        self.stage.setText(label)
        self.title.setText(task.title);self.filename.setText(task.file_name)
        self.cancel.setVisible(task.active);self.cancel.setEnabled(not task.cancel_requested)
        self.retry.setVisible(self.allow_retry and not task.active and task.status in ('failed','partial','cancelled','interrupted'))
        self.retry.setText('Consultar novamente' if task.status=='partial' and outcome.get('link_state')=='linked' else 'Tentar novamente')
        received=progress.get('verified_bytes',0) if stage in ('verifying','checking_existing') else progress.get('received',0)
        total=progress.get('total')
        known=type(total) is int and total>0
        if task.active and stage in ('downloading','verifying','checking_existing','waiting') and known:
            value=max(0,min(100,round(received*100/total)))
            self.bar.setRange(0,100);self.bar.setValue(value);self.percent.setText(f'{value}%')
        elif task.active:
            self.bar.setRange(0,0);self.percent.setText('')
        else:
            self.bar.setRange(0,100);self.bar.setValue(100 if outcome.get('download_state')=='downloaded' else 0);self.percent.setText('')
        self.bar.setVisible((task.active and task.status!='queued') or outcome.get('download_state')=='downloaded')
        metrics=byte_text(received)+((' / '+byte_text(total)) if known else '')
        speed=progress.get('bytes_per_second');eta=progress.get('eta_seconds')
        if stage=='downloading' and isinstance(speed,(int,float)) and speed>0:metrics+=' · '+byte_text(speed)+'/s'
        if stage=='downloading' and isinstance(eta,(int,float)) and eta>=0:metrics+=' · estimado '+str(max(1,round(eta/60)))+' min'
        self.metrics.setText(metrics);self.metrics.setVisible(bool(received) or known)
        phases=[]
        values={**progress,**outcome}
        if values:
            names={'downloaded':'verificado','failed':'falhou','cancelled':'cancelado','linked':'concluído',
                   'completed':'concluídos','pending':'pendentes','not_completed':'não concluído','not_started':'não iniciados','running':'em andamento','not_required':'não necessária'}
            phase_fields=[('transfer_state','Transferência'),('verification_state','Verificação'),('link_state','Vínculo'),('metadata_state','Metadados')]
            if not values.get('transfer_state'):phase_fields.insert(0,('download_state','Arquivo'))
            for key,caption in phase_fields:
                value=values.get(key)
                if value and value!='not_requested':
                    label=names.get(value,value)
                    if key in ('transfer_state','verification_state'):
                        label={'completed':'concluída','not_started':'não iniciada','cancelled':'cancelada'}.get(value,label)
                    phases.append(caption+': '+label)
        self.steps.setText(' · '.join(phases));self.steps.setVisible(bool(phases))
        message=outcome.get('message','') if not task.active else ''
        self.message.setText(message);self.message.setVisible(bool(message))
        path=outcome.get('local_path') or progress.get('local_path') or progress.get('partial_path')
        self.folder.setVisible(bool(path))


class TransferList(QWidget):
    def __init__(self,manager,parent=None):
        super().__init__(parent);self.manager=manager;self.cards={};self.setObjectName('transferList')
        self.layout_box=QVBoxLayout(self);self.layout_box.setContentsMargins(0,0,0,0);self.layout_box.setSpacing(12)
        self.empty=text('Nenhuma transferência. Escolha uma ROM do Drive para baixar.','muted');self.layout_box.addWidget(self.empty)
        for task in manager.tasks.values():self.update_task(task)
        manager.updated.connect(self.update_task)

    def update_task(self,task):
        if task.id not in self.cards:
            card=TransferCard(self.manager,task,self);self.cards[task.id]=card;self.layout_box.insertWidget(0,card)
        tasks=list(self.manager.tasks.values())
        rank=lambda value:0 if value.status in ('running','cancelling') else 1 if value.status=='queued' else 2
        desired=[value.id for value in sorted(tasks,key=rank) if value.id in self.cards]
        if desired!=getattr(self,'display_order',[]):
            self.display_order=desired
            for index,identity in enumerate(desired):self.layout_box.insertWidget(index,self.cards[identity])
        self.empty.setVisible(not self.cards)

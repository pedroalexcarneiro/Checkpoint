"""Fila de downloads pertencente ao app, independente dos painéis de acompanhamento."""
from dataclasses import dataclass,field
from functools import partial
import json
from pathlib import Path
import sqlite3
import re
import time
from uuid import uuid4
from PySide6.QtCore import QObject,QTimer,Signal,Qt
from .jobs import Job
from .process_liveness import current_owner


@dataclass
class Transfer:
    id:str
    file_id:int
    game_id:int|None
    file_name:str
    title:str
    mode:str='download'
    directory:str|None=None
    status:str='queued'
    progress:dict=field(default_factory=dict)
    outcome:dict=field(default_factory=dict)
    job:object=None
    worker:object=None
    cancel_requested:bool=False
    stalled:bool=False
    last_advance:float=field(default_factory=time.monotonic)

    @property
    def active(self):return self.status in ('queued','running','cancelling')

    def record(self):
        return {name:getattr(self,name) for name in ('id','file_id','game_id','file_name','title',
                'mode','directory','status','progress','outcome')}


class TransferManager(QObject):
    updated=Signal(object)
    completed=Signal(object)
    idle=Signal()

    def __init__(self,library,parent=None):
        super().__init__(parent)
        self.library=library
        self.tasks={}
        self.current=None
        self.closing=False
        self.dirty=False
        self.root=library.db.path.parent/'jobs'/'transfers'
        self.timer=QTimer(self);self.timer.setInterval(200);self.timer.timeout.connect(self.poll)
        saved=library.setting('downloads.transfers',[])
        for row in saved if isinstance(saved,list) else []:
            if (not isinstance(row,dict) or not isinstance(row.get('id'),str)
                    or not re.fullmatch('[a-f0-9]{32}',row['id'])):continue
            if not isinstance(row.get('progress'),dict) or not isinstance(row.get('outcome'),dict):continue
            try:
                task=Transfer(**{key:row[key] for key in ('id','file_id','game_id','file_name','title',
                                'mode','directory','status','progress','outcome')})
            except (TypeError,KeyError):continue
            if task.active:
                task.status='interrupted'
                task.outcome={'message':'Interrompido ao fechar o Checkpoint. Tentar novamente reinicia a transferência.'}
            self.tasks[task.id]=task

    @property
    def busy(self):return any(task.active for task in self.tasks.values())

    def persist(self,strict=False):
        sql=self.library.sql
        timeout=sql.execute('PRAGMA busy_timeout').fetchone()[0]
        sql.execute('PRAGMA busy_timeout=25')
        try:
            records=list(self.tasks.values())
            saved=[task.record() for task in records if task.active]
            saved.extend(task.record() for task in records[-50:] if not task.active)
            self.library.set_setting('downloads.transfers',saved)
            self.dirty=False
        except sqlite3.Error:
            self.dirty=True
            if strict:raise ValueError('Biblioteca ocupada. Aguarde um instante e tente iniciar novamente.') from None
        finally:sql.execute(f'PRAGMA busy_timeout={int(timeout)}')

    def start(self,file_id,game_id=None,*,mode='download',directory=None,worker=None):
        if self.closing:raise ValueError('O Checkpoint está aguardando o cancelamento para fechar.')
        if mode not in ('download','link','import'):raise ValueError('Origem de transferência inválida.')
        row=self.library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone()
        if not row or not row['drive_id']:raise ValueError('Escolha um arquivo do Drive.')
        if mode=='link' and (not game_id or not self.library.get(game_id) or not self.library.is_owned(game_id)):
            raise ValueError('Escolha uma ficha da Biblioteca para vincular a ROM.')
        if mode=='link' and row['game_id'] not in (None,game_id):
            raise ValueError('Esta ROM já pertence a outro jogo. Nenhum vínculo foi alterado.')
        for existing in self.tasks.values():
            if not existing.active:continue
            if existing.file_id==file_id:
                if mode=='download' or (existing.mode==mode and existing.game_id==game_id):return existing
                raise ValueError('Este arquivo já está sendo baixado. Aguarde concluir antes de vincular.')
            if mode=='link' and existing.mode=='link' and existing.game_id==game_id:
                raise ValueError('Este jogo já tem uma transferência. Aguarde ou cancele antes de substituir.')
        game=self.library.get(game_id or row['game_id']) if (game_id or row['game_id']) else None
        task=Transfer(uuid4().hex,file_id,game_id,row['original_name'],game['title'] if game else row['original_name'],
                      mode=mode,directory=str(directory) if directory else None,worker=worker)
        task.progress={'stage':'queued','received':0,'total':row['size']}
        self.tasks[task.id]=task
        try:self.persist(strict=True)
        except Exception:
            self.tasks.pop(task.id,None)
            raise
        self.updated.emit(task)
        self.start_next()
        self.timer.start()
        return task

    def start_next(self):
        if self.current is not None:return
        task=next((item for item in self.tasks.values() if item.status=='queued'),None)
        if task is None:return
        directory=self.root/task.id
        try:
            directory.mkdir(parents=True,exist_ok=False)
            owner=current_owner()
            options={'progress_path':str(directory/'progress.json'),
                     'cancel_path':str(directory/'cancel'),'owner':owner}
            if task.mode=='link':
                from .rom_link_worker import run_link
                work=partial(task.worker or run_link,self.library.db.path,task.file_id,task.game_id,**options)
            else:
                from .rom_link_worker import run_download
                if task.mode=='import':options['import_after']=True
                work=partial(task.worker or run_download,self.library.db.path,task.file_id,directory=task.directory,**options)
            task.status='running';self.current=task.id
            task.job=Job(work,self)
            task.job.succeeded.connect(partial(self.received,task),Qt.QueuedConnection)
            task.job.failed.connect(partial(self.failed,task),Qt.QueuedConnection)
            task.job.finished.connect(partial(self.finished,task),Qt.QueuedConnection)
            self.persist();self.updated.emit(task);task.job.start()
        except (OSError,ValueError):
            task.status='failed';task.outcome={'message':'Não foi possível preparar a transferência. Verifique a pasta de dados.'}
            self.current=None;self.persist();self.updated.emit(task);self.completed.emit(task)

    def received(self,task,result):
        task.outcome=result if isinstance(result,dict) else {'message':'A transferência não retornou um resultado válido.','errors':['Resultado inválido.']}

    def failed(self,task,message):
        self.read_progress(task)
        task.outcome={'errors':[message],'message':message,'download_state':'failed'}
        for key in ('transfer_state','verification_state','registration_state'):
            value=task.progress.get(key)
            if value:task.outcome[key]='failed' if value=='running' else value

    def finished(self,task):
        self.read_progress(task)
        outcome=task.outcome
        downloaded=outcome.get('download_state')=='downloaded'
        if outcome.get('cancelled') or outcome.get('download_state')=='cancelled':task.status='cancelled'
        elif downloaded and task.mode=='download':task.status='completed'
        elif downloaded and outcome.get('link_state')=='linked':
            task.status='completed' if outcome.get('metadata_state')=='completed' else 'partial'
        else:task.status='partial' if downloaded else 'failed'
        job=task.job;task.job=None
        if job:job.deleteLater()
        self.current=None;self.persist();self.updated.emit(task);self.completed.emit(task)
        self.start_next()
        if not self.busy:
            if not self.dirty:self.timer.stop()
            self.idle.emit()

    def read_progress(self,task):
        path=self.root/task.id/'progress.json'
        try:
            if path.stat().st_size>32*1024:return
            value=json.loads(path.read_text(encoding='utf-8'))
        except (OSError,ValueError):return
        if not isinstance(value,dict) or value==task.progress:return
        if type(value.get('received',0)) is not int:return
        if (value.get('received',0)>task.progress.get('received',0)
                or value.get('verified_bytes',0)>task.progress.get('verified_bytes',0)
                or value.get('stage')!=task.progress.get('stage')):
            task.last_advance=time.monotonic()
            task.stalled=False
        task.progress=value
        if value.get('file_name'):task.file_name=str(value['file_name'])
        self.updated.emit(task)

    def poll(self):
        if self.current is None:self.start_next()
        if self.current:
            task=self.tasks[self.current];self.read_progress(task)
            if time.monotonic()-task.last_advance>60:
                if not task.stalled:
                    task.stalled=True;self.updated.emit(task)
        if self.dirty:self.persist()
        if not self.busy and not self.dirty:self.timer.stop()

    def cancel(self,task_id):
        task=self.tasks.get(task_id)
        if not task or not task.active:return
        if task.status=='queued':
            task.status='cancelled';task.outcome={'message':'Transferência cancelada antes de iniciar.'}
            self.persist();self.updated.emit(task)
            if not self.busy:self.idle.emit()
            return
        try:(self.root/task.id/'cancel').touch(exist_ok=True)
        except OSError:raise ValueError('Não foi possível solicitar cancelamento. Verifique as permissões da pasta de dados.') from None
        task.cancel_requested=True;task.status='cancelling';self.persist();self.updated.emit(task)

    def cancel_all(self):
        for task in list(self.tasks.values()):
            if task.active:self.cancel(task.id)


def manager_for(library,parent=None):
    owner=parent
    while owner is not None:
        if hasattr(owner,'download_manager'):return owner.download_manager
        owner=owner.parentWidget() if hasattr(owner,'parentWidget') else None
    from PySide6.QtWidgets import QApplication
    return TransferManager(library,QApplication.instance())

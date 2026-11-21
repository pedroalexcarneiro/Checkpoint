"""Progresso/cancelamento cooperativo do auxiliar sem alterar seu protocolo-base."""
from collections import deque
import json
from pathlib import Path
import statistics
import time
from .integrations import IntegrationError


class TransferCancelled(IntegrationError):
    pass


def check_cancel(cancel):
    if cancel and cancel():
        raise TransferCancelled('Operação cancelada. Arquivos existentes foram preservados.')


class TransferProgress:
    def __init__(self, progress_path=None, cancel_path=None,owner=None):
        self.path=Path(progress_path) if progress_path else None
        self.cancel_path=Path(cancel_path) if cancel_path else None
        self.owner=owner
        self.last=time.monotonic()
        self.rate_started=self.last
        self.received=0
        self.rates=deque(maxlen=5)
        self.snapshot={}
        self.last_written=0.0

    def cancelled(self):
        if self.owner is not None:
            from .process_liveness import owner_alive
            if not owner_alive(self.owner):return True
        return bool(self.cancel_path and self.cancel_path.exists())

    def check(self):
        check_cancel(self.cancelled)

    def report(self, values):
        current=time.monotonic()
        old_stage=self.snapshot.get('stage')
        self.snapshot.update(values)
        received=self.snapshot.get('received',0)
        total=self.snapshot.get('total')
        total=total if type(total) is int and total>0 else None
        self.snapshot['total']=total
        if type(received) is not int or received<0:received=0
        self.snapshot['received']=received
        self.snapshot['percent']=(min(100,received*100/total) if total else None)
        delta=current-self.last
        if received>self.received and delta>=0.05:
            self.rates.append((received-self.received)/delta)
            self.received=received
            self.last=current
        rate=statistics.mean(self.rates) if len(self.rates)>=2 else None
        stable=bool(rate and len(self.rates)>=3 and current-self.rate_started>=4 and statistics.pstdev(self.rates)/rate<0.35)
        self.snapshot['bytes_per_second']=rate
        self.snapshot['eta_seconds']=((total-received)/rate if total and stable and total>=received else None)
        self.snapshot['updated_monotonic']=current
        if values.get('stage')=='downloading' and old_stage!='downloading':
            self.rates.clear();self.last=current;self.rate_started=current;self.received=received
        if self.path:
            if old_stage==self.snapshot.get('stage') and current-self.last_written<.1:
                return True
            self.path.parent.mkdir(parents=True,exist_ok=True)
            temporary=self.path.with_suffix('.writing')
            try:
                temporary.write_text(json.dumps(self.snapshot),encoding='utf-8')
                temporary.replace(self.path)
                self.last_written=current
            except OSError:
                # Uma leitura simultânea no Windows pode impedir replace.
                # Progresso é observação; não invalidar bytes válidos por isso.
                return False
        return True

"""Execução explícita e sessões recuperáveis; nunca usa shell."""
import json
import subprocess
import time
from pathlib import Path
from .library import now

class Launcher:
    def __init__(self, library, *, clock=None, timestamp=None):
        self.library = library
        self.active = {}
        self.clock = clock or time.monotonic
        self.timestamp = timestamp or now
        from .session_tracking import SessionTracker
        self.tracking = SessionTracker(library, self.clock, self.timestamp)

    def start(self, game):
        if any(item[2] == game['id'] for item in self.active.values()):
            raise ValueError('Este jogo já possui uma sessão ativa.')
        executable = Path(game['executable']).resolve()
        if not game['executable'] or not executable.is_file():
            raise ValueError('Configure um executável local válido na edição do jogo.')
        return self.start_command(game['id'],[str(executable)],True)

    def start_command(self,game_id,command,monitor_process=False):
        if any(item[2] == game_id for item in self.active.values()):
            raise ValueError('Este jogo já possui uma sessão ativa.')
        if not self.library.get(game_id): raise ValueError('Jogo não encontrado.')
        command = [str(Path(command[0]).resolve()),*command[1:]]
        process = subprocess.Popen(command,cwd=str(Path(command[0]).parent),shell=False)
        stamp = self.timestamp()
        with self.library.sql:
            session = self.library.sql.execute('INSERT INTO play_sessions(game_id,started_at,pid) VALUES(?,?,?)',
                                               (game_id,stamp,process.pid)).lastrowid
        anchor = self.clock()
        self.active[session] = (process,anchor,game_id,monitor_process)
        self.tracking.started(session,game_id,stamp,anchor)
        self.checkpoint(force=True,reason='started')
        return session

    def poll(self):
        finished = []
        for session, (process, started, game_id, monitor) in list(self.active.items()):
            if monitor and process.poll() is not None:
                self.finish(session)
                finished.append(game_id)
        self.checkpoint()
        return finished

    def finish(self, session, *, reason='finished'):
        process, started, game_id, monitor = self.active[session]
        sample=self.tracking.samples.get(session)
        try:
            self.tracking.checkpoint(self.active,force=True,reason=reason,only={session},terminal={session})
        finally:
            if sample is not None:
                sample['ended']=True
                sample.setdefault('stopped_at',self.timestamp())
        self.active.pop(session)
        self.tracking.samples.pop(session,None)

    def checkpoint(self, *, force=False, reason='heartbeat'):
        self.tracking.checkpoint(self.active,force=force,reason=reason)

    def interrupt(self, *, reason='closed'):
        for session in list(self.active):
            self.finish(session,reason=reason)

    def suspend(self):self.tracking.suspend(self.active)

    def resume(self):self.tracking.resume(self.active)

    def resolve(self, session_id, seconds):
        if not isinstance(seconds,int) or seconds < 0:
            raise ValueError('Duração inválida.')
        with self.library.sql:
            self.library.sql.execute("UPDATE play_sessions SET ended_at=?,duration_seconds=?,state='finished' WHERE id=? AND state='interrupted'",
                                     (now(),seconds,session_id))

class EmulatorCommand:
    @staticmethod
    def build(executable, arguments_json, rom):
        executable, rom = Path(executable).resolve(), Path(rom).resolve()
        if not executable.is_file() or not rom.is_file():
            raise ValueError('Executável ou ROM indisponível.')
        arguments = json.loads(arguments_json)
        if not isinstance(arguments,list) or not all(isinstance(a,str) for a in arguments):
            raise ValueError('Argumentos devem ser uma lista JSON de textos.')
        if not any('{rom}' in a for a in arguments):
            raise ValueError('Inclua {rom} nos argumentos.')
        return [str(executable),*[a.replace('{rom}',str(rom.resolve())) for a in arguments]]

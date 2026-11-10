"""Execução explícita e sessões recuperáveis; nunca usa shell."""
import json
import subprocess
import time
from pathlib import Path
from .library import now

class Launcher:
    def __init__(self, library):
        self.library = library
        self.active = {}
        with library.sql:
            library.sql.execute("UPDATE play_sessions SET state='interrupted' WHERE state='active'")

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
        with self.library.sql:
            session = self.library.sql.execute('INSERT INTO play_sessions(game_id,started_at,pid) VALUES(?,?,?)',
                                               (game_id,now(),process.pid)).lastrowid
        self.active[session] = (process,time.monotonic(),game_id,monitor_process)
        return session

    def poll(self):
        finished = []
        for session, (process, started, game_id, monitor) in list(self.active.items()):
            if monitor and process.poll() is not None:
                self.finish(session)
                finished.append(game_id)
        return finished

    def finish(self, session):
        process, started, game_id, monitor = self.active.pop(session)
        duration = max(0,int(time.monotonic()-started))
        with self.library.sql:
            self.library.sql.execute("UPDATE play_sessions SET ended_at=?,duration_seconds=?,state='finished' WHERE id=?",
                                     (now(),duration,session))

    def interrupt(self):
        with self.library.sql:
            for session in self.active:
                self.library.sql.execute("UPDATE play_sessions SET state='interrupted' WHERE id=?",(session,))
        self.active.clear()

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

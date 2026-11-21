"""Entrada auxiliar separada: preserva o protocolo protegido do worker anterior."""
import json
import sys
from pathlib import Path
from .worker import run_isolated


def run_link(database,file_id,game_id=None,*,progress_path=None,cancel_path=None,owner=None):
    def command(request):
        return [sys.executable,'--rom-link-request',str(request)] if getattr(sys,'frozen',False) else [sys.executable,'-m','checkpoint.rom_link_worker',str(request)]
    return run_isolated('rom_link',database,command_factory=command,file_id=file_id,game_id=game_id,
                        progress_path=progress_path,cancel_path=cancel_path,owner=owner)


def run_download(database,file_id,*,directory=None,progress_path=None,cancel_path=None,owner=None,import_after=False):
    def command(request):
        return [sys.executable,'--rom-link-request',str(request)] if getattr(sys,'frozen',False) else [sys.executable,'-m','checkpoint.rom_link_worker',str(request)]
    return run_isolated('rom_download',database,command_factory=command,file_id=file_id,directory=directory,
                        progress_path=progress_path,cancel_path=cancel_path,owner=owner,import_after=import_after)


def execute(request):
    from PySide6.QtCore import QCoreApplication
    app=QCoreApplication.instance() or QCoreApplication([])
    from .database import Database
    from .library import Library
    from .rom_link import complete_link
    data=json.loads(Path(request).read_text(encoding='utf-8'));db=Database(Path(data['database']))
    try:
        if data['operation']=='rom_download':
            from .transfer_download import download_only
            result=download_only(Library(db),**data['arguments'])
        else:result=complete_link(Library(db),**data['arguments'])
        payload={'ok':True,'result':result}
    except ValueError as error:
        payload={'ok':False,'message':str(error)}
    except Exception:
        payload={'ok':False,'message':'Não foi possível concluir o vínculo. Dados preservados; tente novamente.'}
    finally:db.close()
    Path(data['response']).write_text(json.dumps(payload),encoding='utf-8')
    return 0


if __name__=='__main__':raise SystemExit(execute(sys.argv[1]))

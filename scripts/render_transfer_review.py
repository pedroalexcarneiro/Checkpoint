"""Captura Qt real do painel de transferências com estados ilustrativos isolados."""
import argparse
import json
from pathlib import Path
from uuid import uuid4
from PySide6.QtWidgets import QApplication
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.transfers import Transfer
from checkpoint.window import MainWindow


def main():
    parser=argparse.ArgumentParser();parser.add_argument('output',type=Path)
    args=parser.parse_args();root=args.output.resolve();root.mkdir(parents=True,exist_ok=False)
    config=root/'screen.json'
    config.write_text(json.dumps({'screens':[{'name':'review','width':1920,'height':1080,
        'logicalDpi':96,'logicalBaseDpi':96,'dpr':1}]}),encoding='utf-8')
    app=QApplication(['review','-platform','offscreen:configfile='+str(config)])
    app.setQuitOnLastWindowClosed(False);app.setStyle('Fusion')
    from checkpoint.fonts import install_fonts
    install_fonts(app)
    db=Database(root/'fixture.sqlite');library=Library(db)
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    library.set_setting('appearance.theme','red');library.set_setting('downloads',str(root/'ROMs'))
    (root/'ROMs').mkdir()
    window=MainWindow(library)
    task=Transfer(uuid4().hex,1,1,'Jardim de Névoa.nsp','Jardim de Névoa',mode='link',status='running',
        progress={'stage':'downloading','received':650*1024**2,'total':2*1024**3,
                  'bytes_per_second':8.4*1024**2,'eta_seconds':None,'transfer_state':'running',
                  'verification_state':'not_started','partial_path':str(root/'ROMs'/'Jardim.partial')})
    queued=Transfer(uuid4().hex,2,None,'Aventura nas Ilhas.nsp','Aventura nas Ilhas',status='queued')
    window.download_manager.tasks={task.id:task,queued.id:queued}
    window.download_updated(task)
    window.open_downloads();window.resize(1280,800);window.show()
    manifest=[]
    for width,height in [(1280,800),(1920,1080),(1000,700)]:
        window.resize(width,height)
        for _ in range(12):app.processEvents()
        path=root/f'downloads-{width}x{height}.png';assert window.grab().save(str(path))
        manifest.append({'file':path.name,'window_size':[width,height],'dpr':window.devicePixelRatioF(),
                         'fixtures':True,'progress_simulated':True,'qt_platform':app.platformName()})
    (root/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    window.download_manager.tasks.clear();window.close();window.deleteLater();app.processEvents();db.close()
    print(root)


if __name__=='__main__':main()

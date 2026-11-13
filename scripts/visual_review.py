"""Matriz visual 0.1.32: fixtures explícitos, sem contas ou chamadas externas."""
import hashlib
import json
import subprocess
from pathlib import Path
from unittest.mock import patch
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter,QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult
from checkpoint.integrations.drive import DriveScanner


def settle(app):
    for _ in range(6):app.processEvents()
    QTest.qWait(30)


def render(app,window,library,ids,root):
    from render_ui_review import artwork
    root=Path(root)
    commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
    dirty=bool(subprocess.check_output(['git','status','--porcelain'],text=True).strip())
    from checkpoint.credentials import CredentialVault
    records=[]
    def capture(screen,theme,width,height,widget=window,dialog=None):
        window.statusBar().clearMessage();settle(app)
        assert (widget.width(),widget.height())==(width,height),(screen,widget.size())
        shot=widget.grab()
        if dialog:
            dialog.move(widget.mapToGlobal(widget.rect().center())-dialog.rect().center());settle(app)
            position=dialog.mapToGlobal(dialog.rect().topLeft())-widget.mapToGlobal(widget.rect().topLeft())
            assert position.x()>=0 and position.y()>=0
            assert position.x()+dialog.width()<=width and position.y()+dialog.height()<=height
            painter=QPainter(shot);painter.drawPixmap(position,dialog.grab());painter.end()
        name=f'visual-{screen}-{theme}-{width}x{height}.png';path=root/name
        assert shot.save(str(path))
        records.append({'file':name,'screen':screen,'theme':theme,'width':width,'height':height,
                        'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                        'commit':commit,'dirty':dirty})
    # Covers below are local artwork fixtures; no ROM is downloaded or bundled.
    for index,(name,linked) in enumerate([('Pokemon Emerald (USA).gba',True),('Pokemon FireRed [Europe] # GBA.zip',False),('Pokemon LeafGreen (USA).gba',True)]):
        game=None
        if linked:
            title=name.split(' (')[0]
            cover=artwork(root,30+index,title,'#46715c','cover',600,900)
            banner=artwork(root,30+index,title,'#46715c','banner',1600,450)
            game=library.save_game({'title':title,'platform':'Game Boy Advance','cover':cover,'banner':banner,
                'developer':'Game Freak','publisher':'Nintendo','description':'Dados de teste para a apresentação visual.','source':'Busca'})
        DriveScanner(library,None).record({'id':f'visual-rom-{index}','name':name},'/Fixtures/GBA')
        if game:
            with library.sql:library.sql.execute('UPDATE game_files SET game_id=? WHERE drive_id=?',(game,f'visual-rom-{index}'))
    library.sql.commit()
    from checkpoint.integrations.ggdeals_api import parse_api_prices
    quote=parse_api_prices({'success':True,'data':{'1145350':{'title':'Hades II','url':'https://gg.deals/game/hades-ii/','prices':{'currentRetail':'79.90','currentKeyshops':'59.90','historicalRetail':'39.90','historicalKeyshops':'29.90','currency':'BRL'}}}},'1145350')
    quote['state']='ready';library.set_setting(f'prices.ggdeals.{ids[8]}',quote)
    library.set_setting(f'prices.ggdeals.{ids[9]}',{'state':'ready','provider':'public','currency':'BRL','lowest':12990,'retail':12990,'current_kind':'retail','original':19990,'discount':35,'historical':9990,'offers':[{'kind':'retail','shop':'Loja de teste','cents':12990,'url':'https://gg.deals/','drm':'Steam'}]})
    empty_db=Database(root/'empty-visual.sqlite');empty_library=Library(empty_db)
    empty_library.set_setting('artwork.auto',False);empty_library.set_setting('prices.auto',False)
    with patch.object(CredentialVault,'get',return_value=None):
        empty=MainWindow(empty_library);empty.integration_status=lambda provider:'Não configurada';empty.show()
        try:
            for key,label in [('green','verde'),('pink','rosa')]:
                window.set_theme(key);empty.set_theme(key)
                window.integration_status=lambda provider:'Credencial salva · estado de teste' if provider in ('Steam','RAWG') else 'Não configurada'
                for width,height in [(1280,800),(1920,1080)]:
                    empty.hide();window.show();window.resize(width,height)
                    for page,screen in [(0,'inicio'),(1,'biblioteca'),(2,'desejos')]:
                        window.navigate(page);capture(screen,label,width,height)
                    window.detail(ids[0]);capture('ficha',label,width,height)
                    for index,screen in [(1,'ficha-atividade'),(2,'ficha-memorias'),(3,'ficha-arquivos')]:
                        window.detail_tabs.setCurrentIndex(index);capture(screen,label,width,height)
                    window.navigate(5)
                    for index,screen in enumerate(('config-aparencia','config-conexoes','config-downloads','config-dados')):
                        window.settings_tabs.setCurrentIndex(index);capture(screen,label,width,height)
                    window.navigate(0)
                    dialog=GameDialog(window,library=library);quick=dialog.quick_add
                    selected=MetadataResult('steam','367520','Hollow Knight',platforms=('PC',),developer='Team Cherry',publisher='Team Cherry',description='Dados de teste do resultado escolhido.')
                    dialog.apply_catalog(selected);quick.candidates=[selected];quick.show_result(selected);quick.timer.stop()
                    quick.art.setPixmap(QPixmap(library.get(ids[0])['cover']).scaled(quick.art.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
                    dialog.show();capture('adicionar',label,width,height,dialog=dialog)
                    dialog.source_tabs.setCurrentIndex(1)
                    quick.suspend=True;quick.query.setText('Pokemon');quick.suspend=False;quick.local_results();quick.timer.stop();quick.state.setText(str(len(quick.local))+' ROMs disponíveis no índice')
                    capture('rom-drive',label,width,height,dialog=dialog);dialog.reject()
                    window.hide();empty.show();empty.resize(width,height)
                    for page,screen in [(0,'inicio-vazio'),(1,'biblioteca-vazia'),(2,'desejos-vazio')]:
                        empty.navigate(page);capture(screen,label,width,height,widget=empty)
                    cover=artwork(root,42,'Jogo sem ficha','#6a637d','cover',600,900)
                    sparse=empty_library.save_game({'title':'Jogo sem ficha','platform':'PC','cover':cover})
                    empty.navigate(0);capture('inicio-sem-andamento',label,width,height,widget=empty)
                    empty_library.save_game({'title':'Jogo sem ficha','platform':'PC','cover':''},sparse)
                    empty.detail(sparse);capture('ficha-incompleta',label,width,height,widget=empty)
                    with empty_library.sql:empty_library.sql.execute('DELETE FROM games WHERE id=?',(sparse,))
            manifest={'commit':commit,'dirty':dirty,'environment':'Linux / Qt offscreen / Fusion',
                'fixtures':'Jogos, artes, preços, sessões, estados de conexão e índice Drive controlados. Nenhuma conta ou credencial real. Não prova o fluxo de cadastro.',
                'dialogs':'Composição dos grabs Qt reais; sem retoques, sem captura do desktop.',
                'captures':records}
            (root/'visual-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        finally:
            empty.close();empty_db.close();window.close()
    print(f'{len(records)} capturas: {root}')

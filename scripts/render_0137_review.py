"""Grabs Qt reais com dados sintéticos isolados; nunca abre biblioteca pessoal."""
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
import json
from PySide6.QtWidgets import QApplication,QComboBox
from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.window import MainWindow
from checkpoint.fonts import install_fonts
from render_ui_review import artwork


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',type=Path);args=parser.parse_args();root=args.output.resolve()
    root.mkdir(parents=True,exist_ok=True)
    if (root/'review.sqlite').exists():raise SystemExit('Use diretório novo; dados existentes preservados.')
    app=QApplication([]);app.setStyle('Fusion');install_fonts(app)
    db=Database(root/'review.sqlite');lib=Library(db)
    lib.set_setting('artwork.auto',False);lib.set_setting('prices.auto',False)
    now=datetime.now(timezone.utc);ids=[]
    for index,title in enumerate(['Portal 2','Hades','Celeste','Metroid Fusion','Hollow Knight','Animal Well']):
        color=['#366077','#875560','#536d7a','#5c7b68','#495972','#78694d'][index]
        paths={kind:artwork(root,index,title,color,kind,width,height) for kind,width,height in [('cover',600,900),('banner',1600,450),('logo',620,150)]}
        identity=lib.save_game({'title':title,'platform':'PC' if index!=3 else 'GBA','status':'Jogando' if index<2 else 'Não iniciado','favorite':int(index==0),**paths});ids.append(identity)
        if index<4:
            started=now-timedelta(hours=index*5+2)
            with lib.sql:lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state,pid) VALUES(?,?,?,?, 'finished',?)",(identity,started.isoformat(),(started+timedelta(minutes=32+index)).isoformat(),(32+index)*60,100+index))
            lib.add_diary(identity,'Anotação sintética para revisar a interface.');lib.add_media(identity,paths['banner'],'Captura sintética de revisão')
        else:
            with lib.sql:
                lib.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                lib.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(1000+index)))
            lib.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','currency':'BRL','checked_at':now.isoformat(),'retail':2490+index*100,'offer_context':{'steam':str(1000+index),'platform':'PC'},'offers':[{'kind':'retail','shop':'Loja de teste','cents':2490+index*100,'original':5990,'url':'https://gg.deals/br/redirect/fixture/'}]})
    window=MainWindow(lib);window.show()
    def capture(name,widget=window):
        for _ in range(6):app.processEvents()
        from PySide6.QtCore import QElapsedTimer
        from PySide6.QtTest import QTest
        clock=QElapsedTimer();clock.start()
        while (window.gallery.art_cache.pending or window.game_list.art_cache.pending) and clock.elapsed()<3000:
            QTest.qWait(5);app.processEvents()
        assert not window.gallery.art_cache.pending and not window.game_list.art_cache.pending
        assert widget.grab().save(str(root/(name+'.png')))
    for width,height in ((1280,800),(1920,1080),(1000,700)):
        window.resize(width,height);prefix=f'{width}x{height}-'
        for page,name in ((0,'home'),(1,'grid'),(2,'wishes'),(4,'statistics'),(5,'appearance')):
            window.navigate(page)
            if page==5:window.settings_tabs.setCurrentIndex(0)
            capture(prefix+name)
        from checkpoint.settings_previews import CoverSizeChoices
        choices=window.pages[5].findChild(CoverSizeChoices)
        for percent in (70,150):
            choices.group.button(percent).click();capture(prefix+'appearance-'+str(percent))
        choices.group.button(100).click()
        window.settings_tabs.setCurrentIndex(1);capture(prefix+'connections')
        window.navigate(1);window.view.setCurrentIndex(1);capture(prefix+'list');window.view.setCurrentIndex(0)
        window.navigate(4);period=window.pages[4].findChild(QComboBox,'statisticsPeriod')
        for key in ('daily','weekly','monthly','12m','all'):
            period.setCurrentIndex(period.findData(key));capture(prefix+'statistics-'+key)
    from checkpoint.profile_dialog import ProfileDialog
    window.resize(1280,800);window.navigate(2)
    combo=window.pages[2].findChild(QComboBox,'wishlistPlatform');combo.showPopup()
    for _ in range(5):app.processEvents()
    from PySide6.QtGui import QPainter
    popup=combo.view().window();shot=window.grab();painter=QPainter(shot);painter.drawPixmap(window.mapFromGlobal(popup.mapToGlobal(popup.rect().topLeft())),popup.grab());painter.end()
    assert shot.save(str(root/'wishes-platform-menu.png'));combo.hidePopup()
    dialog=ProfileDialog(lib,window);dialog.select_photo(lib.get(ids[0])['cover']);dialog.zoom.setValue(150);dialog.show();capture('profile',dialog);dialog.reject()
    from checkpoint.local_rom_dialog import RomSourceDialog,LocalRomDialog
    import sys
    local=lib.save_game({'title':'Programa Á','platform':'CHIP-8'})
    path=root/'ROMs de teste'/'Programa Á.ch8';path.parent.mkdir();path.write_bytes(bytes.fromhex('00e01200'))
    with lib.sql:
        emulator=lib.sql.execute('INSERT INTO emulators(name,executable) VALUES(?,?)',('Perfil controlado CHIP-8',sys.executable)).lastrowid
        lib.sql.execute('INSERT INTO emulator_profiles(emulator_id,platform,arguments_json,extensions) VALUES(?,?,?,?)',(emulator,'CHIP-8',json.dumps(['-c','pass','{rom}']),'.ch8'))
    source=RomSourceDialog(lib,local,window);source.show();capture('rom-origem',source);source.reject()
    link=LocalRomDialog(lib,local,window);link.select_path(path);link.show();capture('rom-local',link);link.save()
    window.detail(local);window.detail_tabs.setCurrentIndex(3);capture('rom-local-vinculada')
    from checkpoint.dialogs import GameDialog
    from checkpoint.integrations import MetadataResult
    loading=GameDialog(window,library=lib);quick=loading.quick_add;quick.suspend=True;quick.query.setText('Pokémon FireRed and LeafGreen+');quick.suspend=False
    quick.art.setText('Carregando prévia…');quick.show_result(MetadataResult('rawg','1','Pokémon FireRed and LeafGreen+',platforms=('Game Boy Advance',)));quick.state.setText('Carregando ficha…');loading.resize(760,700);loading.show();quick.query.deselect();capture('loading-preview',loading);loading.reject()
    (root/'manifest.json').write_text(json.dumps({'platform':'Linux Qt offscreen','fixtures':True,'window_sizes':['1280x800','1920x1080','1000x700'],'device_pixel_ratio':window.devicePixelRatioF(),'screenshots':sorted(p.name for p in root.glob('*.png') if not p.stem[0].isdigit() or 'x' in p.stem)},indent=2),encoding='utf-8')
    window.close();db.close();print(root)


if __name__=='__main__':main()

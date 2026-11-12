"""Capturas Qt reais com fixtures locais; recusa reutilizar uma base existente.

Uso: QT_QPA_PLATFORM=offscreen python scripts/render_ui_review.py /tmp/revisao-nova
Os jogos e as artes são dados de teste, não integração autenticada nem mockup.
"""
import sys
from pathlib import Path
from datetime import datetime,timezone,timedelta
from PySide6.QtCore import Qt,QRectF,QPointF
from PySide6.QtGui import QImage,QPainter,QColor,QFont,QLinearGradient,QPolygonF
from PySide6.QtWidgets import QApplication
from gamevault.database import Database
from gamevault.library import Library
from gamevault.window import MainWindow
from gamevault.dialogs import GameDialog
from gamevault.drive_dialog import DriveDialog
from gamevault.artwork_dialog import ArtworkDialog
from gamevault.steam_dialog import SteamDialog
from gamevault.emulator_dialog import EmulatorDialog
from gamevault.integrations.drive import DriveScanner


def artwork(root,index,title,color,kind,width,height):
    image=QImage(width,height,QImage.Format_ARGB32);image.fill(Qt.transparent);p=QPainter(image);p.setRenderHint(QPainter.Antialiasing)
    if kind!='logo':
        gradient=QLinearGradient(0,0,width,height);gradient.setColorAt(0,QColor(color));gradient.setColorAt(1,QColor('#101825'));p.fillRect(image.rect(),gradient)
        p.setPen(Qt.NoPen);p.setBrush(QColor(220,230,240,55));p.drawEllipse(QPointF(width*.78,height*.24),height*.16,height*.16)
        for layer in range(3):
            p.setBrush(QColor(14+layer*10,24+layer*10,38+layer*10,230));p.drawPolygon(QPolygonF([QPointF(0,height),QPointF(width*.25,height*(.3+layer*.1)),QPointF(width*.48,height*.7),QPointF(width*.72,height*(.2+layer*.12)),QPointF(width,height*.65),QPointF(width,height)]))
    p.setPen(Qt.white);font=QFont('DejaVu Sans');font.setPixelSize(42 if kind=='logo' else 30);font.setWeight(QFont.Bold);p.setFont(font)
    if kind!='banner':p.drawText(QRectF(16,16,width-32,height-32),Qt.AlignCenter|Qt.TextWordWrap,title)
    p.end();path=root/f'{index}-{kind}.png';assert image.save(str(path));return str(path)


def main():
    root=Path(sys.argv[1]).resolve();root.mkdir(parents=True,exist_ok=True)
    if (root/'review.sqlite').exists():raise SystemExit('Use um diretório novo: base existente preservada.')
    app=QApplication([]);app.setStyle('Fusion')
    from gamevault.fonts import install_fonts,verify_text_font
    install_fonts(app)
    if not verify_text_font():raise SystemExit('Fonte sem os glifos necessários; capturas bloqueadas.')
    db=Database(root/'review.sqlite');lib=Library(db)
    names=['Hollow Knight','Celeste','INSIDE','Hades','The Legend of Zelda: Breath of the Wild','Ori and the Will of the Wisps','Returnal','Dead Cells']
    colors=['#365d79','#a06388','#86474e','#9d5b43','#668771','#42888b','#4a687e','#71577c'];ids=[]
    for index,(title,color) in enumerate(zip(names,colors)):
        cover=artwork(root,index,title,color,'cover',600,900)
        banner=artwork(root,index,title,color,'banner',1600,450);logo=artwork(root,index,title,color,'logo',620,150)
        identity=lib.save_game({'title':title,'platform':'PC','cover':cover,'banner':banner,'logo':logo,'status':'Jogando' if index<4 else 'Concluído' if index<6 else 'Não iniciado','developer':'Estúdio de teste','publisher':'Publicadora de teste','genre':'Aventura','release_date':'2024-01-12','description':'Dados de teste para conferir a interface: explore um mundo cheio de caminhos, encontros e descobertas. As artes desta captura são fixtures locais, sem acesso a contas pessoais.','favorite':int(index==0)});ids.append(identity)
        if index<4:
            lib.add_diary(identity,'Uma lembrança de teste para conferir a leitura, os espaçamentos e a navegação da interface.')
            lib.add_media(identity,banner,'Captura de teste · paisagem')
            start=(datetime.now(timezone.utc)-timedelta(days=index*7+1)).isoformat()
            with lib.sql:
                lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,ended_at,duration_seconds,state) VALUES(?,?,?,?, 'finished')",(identity,start,start,(index+1)*3600))
                lib.sql.execute('INSERT INTO achievements(game_id,title,unlocked_at) VALUES(?,?,?)',(identity,'Primeiro caminho explorado',start))
        if index>=4:
            with lib.sql:lib.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,?)',(identity,9900+index*1000))
    DriveScanner(lib,None).record({'id':'fixture-rom','name':'Example (USA).gba'},'/GBA');lib.sql.commit()
    lib.set_setting('artwork.auto',False);w=MainWindow(lib);w.integration_status=lambda provider:'Não configurada';w.resize(1440,960);w.show()
    def capture(name,widget=w):
        for _ in range(4):app.processEvents()
        assert widget.grab().save(str(root/(name+'.png')))
    for page,name in enumerate(['home','library','wishlist','memories','statistics','settings']):w.navigate(page);capture(name)
    w.navigate(5)
    for index,name in enumerate(['appearance','connections','downloads','data']):w.settings_tabs.setCurrentIndex(index);capture('settings-'+name)
    w.detail(ids[0])
    for index,name in enumerate(['overview','activity','memories','files']):w.detail_tabs.setCurrentIndex(index);capture('detail-'+name)
    for dialog,name in [(GameDialog(w,library=lib),'add'),(GameDialog(w,game=lib.get(ids[0]),library=lib),'edit'),(DriveDialog(lib,w),'drive'),(ArtworkDialog(lib,lib.get(ids[0]),w),'artwork'),(SteamDialog(lib,w),'steam'),(EmulatorDialog(lib,w),'emulators')]:
        dialog.show();capture(name,dialog)
        if name=='edit':
            for index in range(4):dialog.editor_tabs.setCurrentIndex(index);capture('edit-'+str(index),dialog)
        dialog.close()
    original=[lib.get(identity)['cover'] for identity in ids]
    for index in (1,2):
        path=artwork(root,index,names[index],colors[index],'mixed-cover',600,800 if index==1 else 600)
        lib.save_game({'title':names[index],'cover':path},ids[index])
    w.navigate(1);capture('library-mixed-ratios')
    for identity,path in zip(ids,original):lib.save_game({'title':lib.get(identity)['title'],'cover':path},identity)
    for theme in ('green','purple','white'):
        w.set_theme(theme);w.resize(1000,700)
        for page,name in [(0,'home'),(1,'library'),(4,'statistics'),(5,'settings')]:w.navigate(page);capture(theme+'-small-'+name)
    w.close();db.close();print(root)


if __name__=='__main__':main()

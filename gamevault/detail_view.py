"""Ficha editorial: banner/logo, ações claras e informações em abas."""
import json
from pathlib import Path
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QScrollArea,QTabWidget,QToolButton,QMenu,QTextEdit,QCheckBox
from .ui_components import Hero,text,action,card,CurrentPageTabs


def build_detail(window,game):
    game_id=game['id'];saved_tab=window.detail_tabs.currentIndex() if getattr(window,'current_game',None)==game_id and hasattr(window,'detail_tabs') else 0
    draft=window.detail_diary.toPlainText() if getattr(window,'current_game',None)==game_id and hasattr(window,'detail_diary') else ''
    window.current_game=game_id;window.current_page=1;window.header_widget.hide()
    for index,nav in enumerate(window.nav_buttons):nav.setChecked(index==1)
    if hasattr(window,'detail_page'):
        window.stack.removeWidget(window.detail_page);window.detail_page.deleteLater()
    page=QScrollArea();page.setWidgetResizable(True);window.detail_page=page
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(16)
    back=QHBoxLayout();back.addWidget(action('← Biblioteca',lambda:window.navigate(1)));back.addStretch();layout.addLayout(back)
    layout.addWidget(Hero(game,window.theme))
    bar=QHBoxLayout()
    files=[dict(r) for r in window.library.sql.execute('SELECT * FROM game_files WHERE game_id=? ORDER BY original_name',(game_id,))]
    available=[f for f in files if f['available']]
    if game['executable']:bar.addWidget(action('▶ Jogar',lambda:window.start_game(game),True))
    elif available:bar.addWidget(action('▶ Jogar',lambda:window.launch_rom(game_id,available[0]),True))
    elif files:bar.addWidget(action('Baixar ROM',window.drive,True))
    else:bar.addWidget(action('Configurar execução',lambda:window.edit_game(game_id),True))
    seconds=window.library.sql.execute("SELECT COALESCE(SUM(duration_seconds),0) FROM play_sessions WHERE game_id=? AND state='finished'",(game_id,)).fetchone()[0]
    bar.addWidget(text(game['status'],'muted'));bar.addWidget(text(f'{seconds/3600:.1f} h registradas','muted'));bar.addStretch()
    more=QToolButton();more.setText('⋯');more.setAccessibleName('Gerenciar jogo');more.setPopupMode(QToolButton.InstantPopup)
    menu=QMenu(more)
    for title,callback in [('Editar ficha',lambda:window.edit_game(game_id)),('Trocar imagens',lambda:window.artworks(game_id)),('Obter ficha e imagens faltantes',lambda:window.completion_queue.submit([game_id],force=True)),('Adicionar aos desejos',lambda:window.add_wish(game_id)),('Remover da biblioteca',lambda:window.remove_game(game_id))]:
        item=menu.addAction(title);item.triggered.connect(callback)
    more.setMenu(menu);bar.addWidget(more);layout.addLayout(bar)
    tabs=CurrentPageTabs();tabs.setObjectName('detailTabs');window.detail_tabs=tabs
    layouts=[]
    for name in ('Visão geral','Atividade','Memórias','Arquivos'):
        tab=QWidget();inside=QVBoxLayout(tab);inside.setContentsMargins(8,20,8,12);inside.setSpacing(16);tabs.addTab(tab,name);layouts.append(inside)
    overview,activity,memories,technical=layouts
    overview.addWidget(text(game['description'] or 'A descrição aparecerá aqui quando estiver disponível.','bodyText'))
    frame,info=card();grid=QGridLayout();grid.setHorizontalSpacing(36);grid.setVerticalSpacing(15)
    fields=[('Plataforma',game['platform']),('Desenvolvedora',game['developer']),('Publicadora',game['publisher']),('Lançamento',game['release_date']),('Gênero',game['genre']),('Origem',game['source']),('Categoria',game['category']),('Sua nota',str(game['rating'])+'/10' if game['rating'] is not None else '')]
    for index,(caption,value) in enumerate(fields):
        cell=QVBoxLayout();cell.addWidget(text(caption,'muted'));cell.addWidget(text(value or '—'));grid.addLayout(cell,index//2,index%2)
    info.addLayout(grid);overview.addWidget(frame)
    if game['notes']:overview.addWidget(text('Suas observações','sectionTitle'));overview.addWidget(text(game['notes']))
    media=[dict(r) for r in window.library.sql.execute('SELECT * FROM media_files WHERE game_id=? ORDER BY id DESC',(game_id,))]
    images=[m for m in media if m['kind']=='image'][:3]
    if images:
        overview.addWidget(text('Galeria','sectionTitle'));row=QHBoxLayout()
        for image in images:
            b=action('',lambda checked=False,m=image:window.show_media(m));pix=QPixmap(image['path']);b.setIcon(QIcon(pix));b.setIconSize(QSize(170,100));b.setAccessibleName(image['caption'] or 'Abrir captura');row.addWidget(b)
        overview.addLayout(row)
    from .steam_library import game_accounts
    accounts=game_accounts(window.library,game_id)
    if accounts:activity.addWidget(text('Steam','sectionTitle'))
    for account in accounts:
        frame,inside=card();hours='Tempo não disponível' if account['minutes'] is None else f"{account['minutes']/60:.1f} h na Steam"
        inside.addWidget(text(hours,'sectionTitle'));inside.addWidget(text(f"AppID {account['app_id']} · Consulta {(account['checked_at'] or '')[:10]}",'muted'))
        if account['achievements_checked_at']:
            inside.addWidget(text(f"Conquistas: {account['achievement_unlocked']}/{account['achievement_total']}"))
            for achievement in window.library.sql.execute('SELECT title,unlocked_at FROM steam_achievements WHERE steam_id=? AND app_id=? ORDER BY title COLLATE NOCASE',(account['steam_id'],account['app_id'])):
                status='Bloqueada' if achievement['unlocked_at'] is None else 'Desbloqueada'
                inside.addWidget(text(achievement['title']+' · '+status))
        else:inside.addWidget(text('Conquistas ainda não consultadas.','muted'))
        activity.addWidget(frame)
    if accounts:activity.addWidget(action('Gerenciar Steam',window.steam))
    activity.addWidget(text('Marcos pessoais','sectionTitle'));activity.addWidget(action('+ Registrar marco',lambda:window.achievement(game_id)))
    for row in window.library.sql.execute('SELECT * FROM achievements WHERE game_id=?',(game_id,)):activity.addWidget(text(row['title']+' · '+(row['unlocked_at'] or '')[:10]))
    activity.addWidget(text('Sessões','sectionTitle'))
    sessions=window.library.sql.execute('SELECT * FROM play_sessions WHERE game_id=? ORDER BY id DESC',(game_id,)).fetchall()
    if not sessions:activity.addWidget(text('Nenhuma sessão registrada.','muted'))
    for row in sessions:activity.addWidget(text(f"{row['started_at'][:16]} · {row['state']} · {row['duration_seconds']//60} min"))
    for session,item in window.launcher.active.items():
        if item[2]==game_id:activity.addWidget(action('Encerrar registro desta sessão',lambda checked=False,i=session:window.end_session(i,game_id)))
    memories.addWidget(text('Diário de jogo','sectionTitle'));entry=QTextEdit();window.detail_diary=entry;entry.setPlainText(draft);entry.setPlaceholderText('O que você quer guardar desta experiência?');entry.setMaximumHeight(110);memories.addWidget(entry)
    def save_entry():
        def save():
            window.library.add_diary(game_id,entry.toPlainText());entry.clear();window.detail(game_id)
        window.guard(save)
    memories.addWidget(action('Salvar memória',save_entry))
    for record in window.library.diary(game_id):
        frame,inside=card();inside.addWidget(text(record['created_at'][:10],'muted'));inside.addWidget(text(record['text']));memories.addWidget(frame)
    memories.addWidget(action('Adicionar captura ou vídeo',lambda:window.import_media(game_id)))
    for item in media:memories.addWidget(action(item['caption'] or Path(item['path']).name,lambda checked=False,m=item:window.show_media(m)))
    technical.addWidget(text('Arquivos e versões','sectionTitle'))
    if not files:technical.addWidget(text('Nenhuma ROM associada.','muted'))
    for file in files:
        frame,inside=card();inside.addWidget(text(file['original_name']));inside.addWidget(text('Disponível neste computador' if file['available'] else 'Somente no Drive','muted'))
        inside.addWidget(action('Executar versão',lambda checked=False,f=file:window.launch_rom(game_id,f)) if file['available'] else action('Baixar pelo Drive',window.drive));technical.addWidget(frame)
    technical.addWidget(action('Configurar execução',lambda:window.edit_game(game_id)))
    technical.addWidget(text('Saves tradicionais','sectionTitle'));technical.addWidget(action('Configurar saves',lambda:window.configure_saves(game_id)))
    from .save_profiles import SaveProfiles
    from .game_saves import GameSaveBackups
    profile=SaveProfiles(window.library).latest(game_id)
    if profile:
        technical.addWidget(text(Path(profile['directory']).name+' · '+', '.join(json.loads(profile['patterns_json'])),'muted'))
        automatic=QCheckBox('Backup ao encerrar a sessão');automatic.setChecked(window.library.setting('auto_save_'+str(game_id),False));automatic.toggled.connect(lambda value:window.library.set_setting('auto_save_'+str(game_id),value));technical.addWidget(automatic)
        technical.addWidget(action('Fazer backup agora',lambda:window.game_backup(game_id)))
        for backup in GameSaveBackups(window.library).history(game_id):technical.addWidget(action('Restaurar · '+backup['created_at'][:19],lambda checked=False,b=backup:window.restore_game_backup(game_id,b)))
    for inside in layouts:inside.addStretch()
    tabs.setCurrentIndex(min(saved_tab,3));layout.addWidget(tabs);page.setWidget(body);window.stack.addWidget(page);window.stack.setCurrentWidget(page)

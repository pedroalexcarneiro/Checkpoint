"""Ficha editorial: banner/logo, ações claras e informações em abas."""
import json
from .locale import date_display,datetime_display
from pathlib import Path
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QScrollArea,QTabWidget,QToolButton,QMenu,QTextEdit,QCheckBox,QSizePolicy
from .ui_components import Hero,text,action,card,CurrentPageTabs
from .design_system import ArtworkButton,AdaptiveColumns,CardGrid,IconButton,Badge,empty_state,CardSurface,ActionCard,StatusChip
from .visual_tokens import SPACE,HEIGHT


def build_detail(window,game):
    game_id=game['id'];saved_tab=window.detail_tabs.currentIndex() if getattr(window,'current_game',None)==game_id and hasattr(window,'detail_tabs') else 0
    draft=window.detail_diary.toPlainText() if getattr(window,'current_game',None)==game_id and hasattr(window,'detail_diary') else ''
    window.current_game=game_id;window.current_page=1;window.header_widget.hide();window.heading.hide();window.search.hide();window.add_button.hide()
    for control in window.view_buttons:control.hide()
    for index,nav in enumerate(window.nav_buttons):nav.setChecked(index==1)
    if hasattr(window,'detail_page'):
        window.stack.removeWidget(window.detail_page);window.detail_page.deleteLater()
    page=QScrollArea();page.setWidgetResizable(True);window.detail_page=page
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,SPACE['xs'],0);layout.setSpacing(SPACE['md']);layout.setAlignment(Qt.AlignTop)
    hero=Hero(game,window.theme);hero.detail_mode=True;hero.compact=not any(game[field] for field in ('description','developer','publisher'))
    back=QHBoxLayout();back_button=action('←',lambda:window.navigate(1));back_button.setFixedSize(32,32);back_button.setObjectName('heroBack');back_button.setAccessibleName('Voltar à biblioteca');back_button.setToolTip('Voltar à biblioteca');back.addWidget(back_button);back.addStretch();hero.content.insertLayout(0,back)
    layout.addWidget(hero)
    if hero.compact or (hero.banner.isNull() and hero.logo.isNull()):
        if hero.banner.isNull() and hero.logo.isNull():hero.hide()
        heading=QHBoxLayout();heading.addWidget(action('←',lambda:window.navigate(1)))
        title=text(game['title'],'sectionTitle');title.setObjectName('gameDetailTitle')
        heading.addWidget(title,1);layout.addLayout(heading)
    actions_frame=QWidget();actions_frame.setObjectName('gameActions');actions_frame.setFixedHeight(HEIGHT['actions']);actions_frame.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed);bar=QHBoxLayout(actions_frame);bar.setContentsMargins(14,8,14,8);bar.setSpacing(20)
    files=[dict(r) for r in window.library.sql.execute('SELECT * FROM game_files WHERE game_id=? ORDER BY original_name',(game_id,))]
    available=[f for f in files if f['available']]
    owned=window.library.is_owned(game_id)
    if not owned:bar.addWidget(action('Adicionar à biblioteca',lambda:window.acquire_wish(game_id),True))
    elif game['executable']:bar.addWidget(action('Jogar',lambda:window.start_game(game),True))
    else:bar.addWidget(action('Configurar execução',lambda:window.edit_game(game_id)))
    seconds=window.library.sql.execute("SELECT COALESCE(SUM(duration_seconds),0) FROM play_sessions WHERE game_id=? AND state='finished'",(game_id,)).fetchone()[0]
    if owned:
        status_row=QHBoxLayout();dot=text('●');dot.setObjectName('gameStatusDot');dot.setStyleSheet('color: '+(window.theme.colors['accent'] if game['status'] in ('Jogando','Concluído') else window.theme.colors['muted']));status_row.addWidget(dot);status_row.addWidget(text(game['status'],'muted'));bar.addLayout(status_row)
        bar.addWidget(text('Tempo jogado: '+f'{seconds/3600:g}'.replace('.',',')+' h','muted'))
    else:bar.addWidget(text('Na lista de desejos' if window.library.sql.execute('SELECT 1 FROM wishlist WHERE game_id=?',(game_id,)).fetchone() else 'Desejo arquivado','muted'))
    bar.addStretch()
    bar.addWidget(IconButton('heart','Retirar dos favoritos' if game['favorite'] else 'Marcar como favorito',lambda:window.toggle_favorite(game_id)))
    more=QToolButton();more.setFixedSize(40,36);more.setText('⋯');more.setAccessibleName('Gerenciar jogo');more.setPopupMode(QToolButton.InstantPopup)
    menu=QMenu(more)
    for title,callback in [('Editar ficha',lambda:window.edit_game(game_id)),('Trocar imagens',lambda:window.artworks(game_id)),('Obter ficha e imagens faltantes',lambda:window.completion_queue.submit([game_id],force=True)),('Adicionar aos desejos',lambda:window.add_wish(game_id)),('Remover da biblioteca',lambda:window.remove_game(game_id))]:
        item=menu.addAction(title);item.triggered.connect(callback)
    more.setMenu(menu);bar.addWidget(more);layout.addWidget(actions_frame)
    notice=getattr(window,'detail_notice',None)
    if notice and notice[0]==game_id:
        banner=text(notice[1]);banner.setObjectName('wishNotice');banner.setAccessibleName(notice[1]);banner.setStyleSheet('padding: 10px; border: 1px solid '+window.theme.colors['accent']+'; border-radius: 7px;');layout.addWidget(banner)
    if any(file['drive_id'] for file in files) and not all(game[field] for field in ('description','developer','publisher')):
        warning=text('Não encontramos dados para este jogo. Pesquise manualmente.')
        warning.setObjectName('metadataNotice');layout.addWidget(warning)
        layout.addWidget(action('Pesquisar manualmente',lambda:window.search_game_data(game_id)),0,Qt.AlignLeft)
    tabs=CurrentPageTabs();tabs.setObjectName('detailTabs');window.detail_tabs=tabs
    layouts=[]
    for name in ('Visão geral','Atividade','Memórias','Arquivos'):
        tab=QWidget();inside=QVBoxLayout(tab);inside.setContentsMargins(8,20,8,12);inside.setSpacing(16);tabs.addTab(tab,name);layouts.append(inside)
    overview,activity,memories,technical=layouts
    columns=None
    about=CardSurface();about_layout=QVBoxLayout(about);about_layout.setContentsMargins(*([SPACE['lg']]*4));about_layout.setSpacing(SPACE['md'])
    about_layout.addWidget(text('Sobre o jogo','sectionTitle'))
    if not any(game[field] for field in ('description','developer','publisher')):
        about.setProperty('emptyState',True)
        about_layout.addWidget(text('A ficha ainda está incompleta. Adicione informações para organizar este jogo.','emptyDescription'))
        about_layout.addWidget(action('Editar ficha',lambda:window.edit_game(game_id)),0,Qt.AlignLeft)
    if game['description']:about_layout.addWidget(text(game['description'],'bodyText'))
    from .description_provenance import current
    provenance=current(window.library,game)
    if provenance.get('source','').startswith('https://pt.wikipedia.org/'):
        from PySide6.QtGui import QDesktopServices
        from PySide6.QtCore import QUrl
        source=provenance['source']
        attribution=action('Fonte: Wikipédia · CC BY-SA 4.0',lambda:QDesktopServices.openUrl(QUrl(source)))
        attribution.setObjectName('quiet');attribution.setToolTip(source);about_layout.addWidget(attribution,0,Qt.AlignLeft)
    if game['notes']:about_layout.addWidget(text('Suas observações','cardTitle'));about_layout.addWidget(text(game['notes'],'muted'))
    media=[dict(r) for r in window.library.sql.execute('SELECT * FROM media_files WHERE game_id=? ORDER BY id DESC',(game_id,))]
    images=[m for m in media if m['kind']=='image'][:2]
    fields=[('Desenvolvedora',game['developer']),('Plataforma',game['platform']),('Gênero',game['genre']),('Lançamento',date_display(game['release_date']))]
    facts=QGridLayout();facts.setHorizontalSpacing(36);facts.setVerticalSpacing(16)
    for index,(caption,value) in enumerate((pair for pair in fields if pair[1])):
        item=QWidget();row=QHBoxLayout(item);row.setContentsMargins(0,0,0,0);row.setSpacing(10);row.addWidget(Badge('platform' if caption=='Plataforma' else 'settings' if caption=='Desenvolvedora' else 'clock' if caption=='Lançamento' else 'library',30))
        words=QVBoxLayout();words.setSpacing(3);words.addWidget(text(caption,'caption'));words.addWidget(text(value));row.addLayout(words,1);facts.addWidget(item,index//2,index%2)
    about_layout.addLayout(facts)
    extra=QWidget();extra_layout=QVBoxLayout(extra);extra_layout.setContentsMargins(0,4,0,0)
    other=[('Publicadora',game['publisher']),('Origem',game['source']),('Categoria',game['category']),('Sua nota',str(game['rating'])+'/10' if game['rating'] is not None else '')]
    for caption,value in other:
        if value:extra_layout.addWidget(text(f'{caption} · {value}','muted'))
    from .settings_view import disclosure
    if any(value for _,value in other):about_layout.addWidget(extra)
    if not owned:
        from .price_view import comparison
        about_layout.addWidget(comparison(window,game))
        if window.isVisible() and window.library.setting('prices.auto',True):window.price_queue.submit([game_id])
    about_layout.addStretch()
    gallery=CardSurface();gallery.setMaximumWidth(380);gallery.setMinimumWidth(240);gallery.setObjectName('detailGallery')
    gallery_layout=QVBoxLayout(gallery);gallery_layout.setContentsMargins(*([SPACE['lg']]*4));gallery_layout.setSpacing(SPACE['md'])
    gallery_layout.addWidget(text('Galeria','sectionTitle'))
    if images:
        row=QHBoxLayout()
        for image in images:
            row.addWidget(ArtworkButton(image['path'],image['caption'] or 'Abrir captura',lambda checked=False,m=image:window.show_media(m),height=100))
        gallery_layout.addLayout(row)
    else:
        gallery.setProperty('emptyState',True);gallery_layout.addWidget(Badge('memories',40))
        gallery_layout.addWidget(text('Guarde suas melhores cenas','cardTitle'))
        gallery_layout.addWidget(text('Adicione capturas e vídeos deste jogo à sua galeria.','emptyDescription'))
    add=action('Adicionar captura',lambda:window.import_media(game_id));add.setObjectName('quiet');gallery_layout.addWidget(add,0,Qt.AlignLeft);gallery_layout.addStretch()
    overview.addWidget(AdaptiveColumns(about,gallery,(3,2),breakpoint=640))
    from .steam_library import game_accounts
    accounts=game_accounts(window.library,game_id)
    if accounts:activity.addWidget(text('Steam','sectionTitle'))
    for account in accounts:
        frame,inside=card();hours='Tempo não disponível' if account['minutes'] is None else f"{account['minutes']/60:.1f} h na Steam"
        inside.addWidget(text(hours,'sectionTitle'));inside.addWidget(text(f"AppID {account['app_id']} · Consulta {date_display(account['checked_at'])}",'muted'))
        if account['achievements_checked_at']:
            inside.addWidget(text(f"Conquistas: {account['achievement_unlocked']}/{account['achievement_total']}"))
            for achievement in window.library.sql.execute('SELECT title,unlocked_at FROM steam_achievements WHERE steam_id=? AND app_id=? ORDER BY title COLLATE NOCASE',(account['steam_id'],account['app_id'])):
                status='Bloqueada' if achievement['unlocked_at'] is None else 'Desbloqueada'
                inside.addWidget(text(achievement['title']+' · '+status))
        else:inside.addWidget(text('Conquistas ainda não consultadas.','muted'))
        activity.addWidget(frame)
    if accounts:activity.addWidget(action('Gerenciar Steam',window.steam))
    heading=QHBoxLayout();heading.addWidget(text('Marcos pessoais','sectionTitle'));heading.addStretch();heading.addWidget(action('+ Registrar marco',lambda:window.achievement(game_id)));activity.addLayout(heading)
    milestones=window.library.sql.execute('SELECT * FROM achievements WHERE game_id=?',(game_id,)).fetchall()
    if not milestones:activity.addWidget(ActionCard('trophy','Nenhum marco registrado','Guarde conquistas e objetivos pessoais deste jogo.',lambda:window.achievement(game_id),'Registrar marco'))
    for record in milestones:
        frame,inside=card();row=QHBoxLayout();row.addWidget(Badge('trophy'));row.addWidget(text(record['title'],'cardTitle'),1);row.addWidget(text(date_display(record['unlocked_at']),'caption'));inside.addLayout(row);activity.addWidget(frame)
    activity.addWidget(text('Sessões','sectionTitle'))
    sessions=window.library.sql.execute('SELECT * FROM play_sessions WHERE game_id=? ORDER BY id DESC',(game_id,)).fetchall()
    if not sessions:activity.addWidget(ActionCard('clock','Nenhuma sessão registrada','O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.',lambda:window.edit_game(game_id),'Configurar execução'))
    for record in sessions:
        frame,inside=card();row=QHBoxLayout();row.addWidget(Badge('clock'));words=QVBoxLayout();words.addWidget(text(datetime_display(record['started_at']),'cardTitle'));words.addWidget(text({'finished':'Concluída','active':'Em andamento','interrupted':'Interrompida'}.get(record['state'],record['state']),'muted'));row.addLayout(words,1);row.addWidget(text(f"{record['duration_seconds']//60} min",'cardTitle'));inside.addLayout(row);activity.addWidget(frame)
    for session,item in window.launcher.active.items():
        if item[2]==game_id:activity.addWidget(action('Encerrar registro desta sessão',lambda checked=False,i=session:window.end_session(i,game_id)))
    memories.addWidget(text('Diário de jogo','sectionTitle'));entry=QTextEdit();window.detail_diary=entry;entry.setPlainText(draft);entry.setPlaceholderText('O que você quer guardar desta experiência?');entry.setMaximumHeight(110);memories.addWidget(entry)
    def save_entry():
        def save():
            window.library.add_diary(game_id,entry.toPlainText());entry.clear();window.detail(game_id)
        window.guard(save)
    row=QHBoxLayout();row.addWidget(action('Salvar memória',save_entry,True));row.addStretch();row.addWidget(action('Adicionar captura ou vídeo',lambda:window.import_media(game_id)));memories.addLayout(row)
    from .collection_views import memory_card
    records=[{**record,'kind':'diary','title':game['title']} for record in window.library.diary(game_id)]
    records.extend({**item,'title':game['title']} for item in media);records.sort(key=lambda record:record['created_at'],reverse=True)
    if records:
        grid=CardGrid(300)
        for record in records:grid.add_card(memory_card(window,record))
        memories.addWidget(grid)
    technical.addWidget(text('Arquivos e versões','sectionTitle'))
    if not files:technical.addWidget(ActionCard('folder','Nenhuma ROM associada','Os arquivos e as versões vinculadas a este jogo aparecem aqui.',window.drive,'Abrir Drive'))
    for file in files:
        frame,inside=card();row=QHBoxLayout();row.addWidget(Badge('folder'));words=QVBoxLayout();words.addWidget(text(file['original_name'],'cardTitle'));words.addWidget(StatusChip('Disponível neste computador' if file['available'] else 'Somente no Drive'));row.addLayout(words,1)
        row.addWidget(action('Executar versão',lambda checked=False,f=file:window.launch_rom(game_id,f),True) if file['available'] else action('Baixar ROM',window.drive,True));inside.addLayout(row);technical.addWidget(frame)
    edit=action('Configurar execução',lambda:window.edit_game(game_id));edit.setObjectName('quiet');technical.addWidget(edit,0,Qt.AlignLeft)
    heading=QHBoxLayout();heading.addWidget(text('Saves tradicionais','sectionTitle'));heading.addStretch();heading.addWidget(action('Configurar saves',lambda:window.configure_saves(game_id)));technical.addLayout(heading)
    from .save_profiles import SaveProfiles
    from .game_saves import GameSaveBackups
    profile=SaveProfiles(window.library).latest(game_id)
    if profile:
        frame,inside=card();inside.addWidget(text(Path(profile['directory']).name,'cardTitle'));inside.addWidget(text(', '.join(json.loads(profile['patterns_json'])),'muted'))
        automatic=QCheckBox('Backup ao encerrar a sessão');automatic.setChecked(window.library.setting('auto_save_'+str(game_id),False));automatic.toggled.connect(lambda value:window.library.set_setting('auto_save_'+str(game_id),value));inside.addWidget(automatic)
        inside.addWidget(action('Fazer backup agora',lambda:window.game_backup(game_id)),0,Qt.AlignLeft);technical.addWidget(frame)
        for backup in GameSaveBackups(window.library).history(game_id):
            frame,inside=card();row=QHBoxLayout();row.addWidget(text(datetime_display(backup['created_at'])),1);row.addWidget(action('Restaurar',lambda checked=False,b=backup:window.restore_game_backup(game_id,b)));inside.addLayout(row);technical.addWidget(frame)
    else:technical.addWidget(ActionCard('folder','Proteja seus saves','Escolha a pasta de saves tradicionais para preparar seus backups.',lambda:window.configure_saves(game_id),'Configurar saves'))
    for inside in layouts:inside.addStretch()
    tabs.setCurrentIndex(min(saved_tab,3));layout.addWidget(tabs);layout.addStretch();page.setWidget(body);window.stack.addWidget(page);window.stack.setCurrentWidget(page)

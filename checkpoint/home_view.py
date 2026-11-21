"""Início integrado com execuções, semana, ofertas e memórias locais."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QSizePolicy
from .design_system import SectionHeader,AdaptiveColumns,CardSurface,empty_state,ArtworkButton,Badge
from .ui_components import text,action,ElidedAction
from .home_components import GameStrip,MemoryCarousel,HomeSectionHeader,HomeOfferRow,LastPlayedBanner
from .home_data import recent_games,week_summary,wish_offers,recent_memories
from .playtime import format_time,total_seconds
from .smooth_scroll import SmoothScrollArea


def in_progress(library):
    """Consulta de status mantida para consumidores; não é histórico de execução."""
    sessions={row['game_id']:dict(row) for row in library.sql.execute("SELECT game_id,MAX(started_at) AS last_played FROM play_sessions GROUP BY game_id")}
    games=[{**game,**sessions.get(game['id'],{}),'seconds':total_seconds(library,game['id'])} for game in library.owned_games() if game['status'] in ('Jogando','Pausado')]
    return sorted(games,key=lambda game:game.get('last_played') or game['created_at'],reverse=True)


def section(title,callback=None,button='Ver tudo'):
    frame=CardSurface();frame.setMinimumWidth(0)
    inside=QVBoxLayout(frame);inside.setContentsMargins(16,16,16,16);inside.setSpacing(14)
    inside.setAlignment(Qt.AlignTop)
    inside.addWidget(HomeSectionHeader(title,callback,button));return frame,inside


def build_home(window):
    outer=window.clear_page(0);scroll=SmoothScrollArea();scroll.setObjectName('homeScroll');scroll.setWidgetResizable(True)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(20)
    games=window.library.owned_games();recent=recent_games(window.library,limit=11)
    if recent:layout.addWidget(LastPlayedBanner(window,recent[0]))
    left,inside=section('Últimas sessões');left.setObjectName('homeRecentSection')
    if len(recent)>1:inside.addWidget(GameStrip(window,recent[1:]))
    elif recent:inside.addWidget(text('Nenhum outro jogo iniciado.','muted'))
    elif games:inside.addWidget(empty_state('library','Nenhuma execução registrada','Escolha um jogo para começar.',lambda:window.navigate(1),'Abrir biblioteca'))
    else:inside.addWidget(empty_state('library','Biblioteca vazia','Adicione um jogo à biblioteca.',window.add_library_game,'Adicionar jogo'))
    right=QWidget();right.setMinimumWidth(0);right_layout=QVBoxLayout(right);right_layout.setContentsMargins(0,0,0,0);right_layout.setSpacing(16)
    def open_week():
        window.library.set_setting('statistics.period','weekly');window.navigate(4)
    frame,inside=section('Resumo da semana',open_week,'Ver estatísticas');frame.setObjectName('homeWeekSummary')
    inside.setSpacing(18)
    summary=week_summary(window.library)
    for icon,title,value in [('clock','Tempo jogado',format_time(summary['seconds'])),('calendar','Sessões',str(summary['sessions'])),('library','Jogos iniciados',str(summary['started_games']))]:
        row=QHBoxLayout();row.setSpacing(10);row.addWidget(Badge(icon,28));row.addWidget(text(title),1)
        label=text(value,'cardTitle');label.setObjectName('homeWeekValue');label.setStyleSheet('color: '+window.theme.colors['accent']+'; font-weight: 600;');row.addWidget(label);inside.addLayout(row)
    right_layout.addWidget(frame)
    frame,inside=section('Ofertas',lambda:window.navigate(2),'Ver desejos');frame.setObjectName('homeWishOffers')
    offers=wish_offers(window.library)
    offer_list=QWidget();offer_list.setObjectName('homeOfferList')
    offer_rows=QVBoxLayout(offer_list);offer_rows.setContentsMargins(0,0,0,0);offer_rows.setSpacing(8)
    for game in offers:
        ambiguous=sum(other['title'].casefold()==game['title'].casefold() for other in offers)>1
        offer_rows.addWidget(HomeOfferRow(window,game,show_platform=ambiguous or game.get('platform') not in ('PC','')))
    if not offers:offer_rows.addWidget(text('Nenhuma oferta válida nos desejos.','muted'))
    inside.addWidget(offer_list)
    right_layout.addWidget(frame)
    columns=AdaptiveColumns(left,right,(3,2),breakpoint=780)
    left.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
    right.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum)
    layout.addWidget(columns)
    layout.addWidget(MemoryCarousel(window,recent_memories(window.library)))
    from .session_tracking import pending_reviews
    interrupted=len(pending_reviews(window.library))
    if interrupted:
        from .locale import count_text
        layout.addWidget(action(count_text(interrupted,'sessão para revisar','sessões para revisar'),lambda:window.recover_sessions(automatic=True)))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

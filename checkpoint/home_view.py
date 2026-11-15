"""Início integrado com execuções, semana, ofertas e memórias locais."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QSizePolicy
from .design_system import SectionHeader,AdaptiveColumns,CardSurface,empty_state,ArtworkButton,Badge
from .ui_components import text,action,ElidedAction
from .home_components import GameStrip,MemoryCarousel,show_execution_history,OfferLogo
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
    inside.addWidget(SectionHeader(title,'',callback,button));return frame,inside


def build_home(window):
    outer=window.clear_page(0);scroll=SmoothScrollArea();scroll.setObjectName('homeScroll');scroll.setWidgetResizable(True)
    body=QWidget();layout=QVBoxLayout(body);layout.setContentsMargins(0,0,8,0);layout.setSpacing(20)
    games=window.library.owned_games();recent=recent_games(window.library,limit=None)
    left,inside=section('Últimos jogos abertos',lambda:show_execution_history(window),'Ver histórico');left.setObjectName('homeRecentSection')
    if recent:inside.addWidget(GameStrip(window,recent))
    elif games:inside.addWidget(empty_state('library','Nenhuma execução registrada','Escolha um jogo para começar.',lambda:window.navigate(1),'Abrir biblioteca'))
    else:inside.addWidget(empty_state('library','Biblioteca vazia','Adicione um jogo à biblioteca.',window.add_library_game,'Adicionar jogo'))
    right=QWidget();right.setMinimumWidth(0);right_layout=QVBoxLayout(right);right_layout.setContentsMargins(0,0,0,0);right_layout.setSpacing(16)
    def open_week():
        window.library.set_setting('statistics.period','weekly');window.navigate(4)
    frame,inside=section('Resumo da semana',open_week,'Ver estatísticas');frame.setObjectName('homeWeekSummary')
    summary=week_summary(window.library)
    for icon,title,value in [('clock','Tempo jogado',format_time(summary['seconds'])),('calendar','Sessões',str(summary['sessions'])),('library','Jogos iniciados',str(summary['started_games']))]:
        row=QHBoxLayout();row.setSpacing(10);row.addWidget(Badge(icon,28));row.addWidget(text(title),1)
        label=text(value,'cardTitle');label.setObjectName('homeWeekValue');label.setStyleSheet('color: '+window.theme.colors['accent']+'; font-weight: 600;');row.addWidget(label);inside.addLayout(row)
    right_layout.addWidget(frame)
    frame,inside=section('Ofertas',lambda:window.navigate(2),'Ver desejos');frame.setObjectName('homeWishOffers');frame.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    offers=wish_offers(window.library)
    offer_list=QWidget();offer_list.setObjectName('homeOfferList')
    offer_rows=QVBoxLayout(offer_list);offer_rows.setContentsMargins(0,0,0,0);offer_rows.setSpacing(0)
    for game in offers:
        offer_row=QWidget();offer_row.setObjectName('homeOfferRow');offer_row.setFixedHeight(72)
        row=QHBoxLayout(offer_row);row.setContentsMargins(0,8,0,8);row.setSpacing(12);identity=game['id']
        logo=OfferLogo(game,lambda checked=False,i=identity:window.detail(i));row.addWidget(logo)
        words=QVBoxLayout();words.setSpacing(3);title=ElidedAction(game['title'],lambda checked=False,i=identity:window.detail(i));title.setObjectName('activityLink');words.addWidget(title)
        quote=game['quote'];kind='Loja oficial' if quote['current_kind']=='retail' else 'Keyshop'
        words.addWidget(text(game['platform']+' · '+kind,'caption'));row.addLayout(words,1)
        from .price_view import source_link
        from .prices import money
        price=source_link(window.library,game,money(quote['lowest']));price.setProperty('homeOfferPrice',True);price.setMinimumWidth(88);price.setStyleSheet('color: '+window.theme.colors['accent']+'; font-weight: 600; text-align: right;');row.addWidget(price);offer_rows.addWidget(offer_row)
    if not offers:offer_rows.addWidget(text('Nenhuma oferta válida nos desejos.','muted'))
    inside.addWidget(offer_list);inside.addStretch(1)
    right_layout.addWidget(frame,1)
    columns=AdaptiveColumns(left,right,(3,2),breakpoint=780)
    columns.row.setAlignment(left,Qt.Alignment());columns.row.setAlignment(right,Qt.Alignment())
    left.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    layout.addWidget(columns)
    layout.addWidget(MemoryCarousel(window,recent_memories(window.library)))
    interrupted=window.library.sql.execute("SELECT count(*) FROM play_sessions WHERE state='interrupted'").fetchone()[0]
    if interrupted:
        from .locale import count_text
        layout.addWidget(action(count_text(interrupted,'sessão para revisar','sessões para revisar'),window.recover_sessions))
    layout.addStretch();scroll.setWidget(body);outer.addWidget(scroll)

from PySide6.QtWidgets import QWidget,QPushButton,QLabel
from checkpoint.window import MainWindow,PAGES
from checkpoint.design_system import CardGrid,IconButton
from checkpoint.ui_components import Hero,ProfileButton
from checkpoint.theme import get_theme


def test_sidebar_keeps_identity_navigation_footer_and_profile_chevron(library,app):
    window=MainWindow(library);window.show();app.processEvents()
    sidebar=window.centralWidget().findChild(QWidget,'sidebar')
    assert [button.text() for button in window.nav_buttons]==PAGES
    assert window.brand.accessibleName()=='Checkpoint'
    assert isinstance(window.profile_button,ProfileButton)
    divider=sidebar.findChild(QWidget,'sidebarDivider')
    assert divider.y()<window.nav_buttons[5].y()<window.profile_button.y()
    assert window.nav_buttons[0].isChecked();window.close()


def test_home_has_reference_hero_cta_and_personal_sections(library,app):
    identity=library.save_game({'title':'Meu jogo','status':'Jogando'})
    window=MainWindow(library);window.show();app.processEvents()
    assert len(window.pages[0].findChildren(Hero))==1
    cta=next(button for button in window.pages[0].findChildren(QPushButton) if button.text()=='Continuar jogando')
    labels=[label.text() for label in window.pages[0].findChildren(QLabel)]
    assert 'Continuar jogando' in labels and 'Sua atividade' in labels and 'Adicionados recentemente' not in labels
    cta.click();assert window.current_game==identity;window.close()


def test_detail_play_and_secondary_setup_obey_execution_configuration(library,app,folder,monkeypatch):
    identity=library.save_game({'title':'Configurar'})
    window=MainWindow(library);window.detail(identity)
    setup=next(button for button in window.detail_page.findChildren(QPushButton) if button.text()=='Configurar execução')
    assert setup.objectName()!='primary'
    executable=folder/'jogo.exe';executable.write_bytes(b'fixture sem execucao')
    library.save_game({'title':'Configurar','executable':str(executable)},identity);calls=[];monkeypatch.setattr(window,'start_game',lambda game:calls.append(game['id']))
    window.detail(identity)
    play=next(button for button in window.detail_page.findChildren(QPushButton) if button.text()=='Jogar')
    assert play.objectName()=='primary';play.click();assert calls==[identity]
    assert any(label.text().startswith('Tempo jogado:') for label in window.detail_page.findChildren(QLabel))
    assert window.detail_page.findChild(QLabel,'gameStatusDot') is not None
    assert [window.detail_tabs.tabText(index) for index in range(4)]==['Visão geral','Atividade','Memórias','Arquivos'];window.close()


def test_connections_match_two_by_two_cards_help_and_green_configured_dot(library,app,monkeypatch):
    window=MainWindow(library)
    monkeypatch.setattr(window,'integration_status',lambda name:'Credencial salva · não verificada' if name in ('Steam','RAWG') else 'Não configurada')
    window.resize(1000,700);window.show();window.navigate(5);window.settings_tabs.setCurrentIndex(1)
    for _ in range(4):app.processEvents()
    assert [window.settings_tabs.tabText(index) for index in range(4)]==['Aparência','Conexões','Downloads','Dados e backup']
    page=window.settings_tabs.currentWidget();grid=page.findChild(CardGrid,'connectionsGrid')
    assert grid.columns==2 and len(grid.cards)==4
    dots=page.findChildren(QLabel,'connectionStateDot');assert len(dots)==4
    assert sum(bool(dot.property('configured')) for dot in dots)==2
    assert all(get_theme('green').colors['accent'] in dot.styleSheet() for dot in dots if dot.property('configured'))
    assert any(button.name=='help' for button in page.findChildren(IconButton));window.close()

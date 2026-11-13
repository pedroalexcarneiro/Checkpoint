"""Contratos visuais: contraste, componentes, estados e geometrias reais."""
import pytest
from checkpoint.theme import THEMES
from checkpoint.visual_tokens import TYPE,SPACE,RADIUS,WEIGHT,contrast


@pytest.mark.parametrize('key',list(THEMES))
def test_semantic_tokens_and_normal_text_contrast(key):
    colors=THEMES[key].colors
    for token in ('background','surface','elevated','card','border_subtle','text','secondary','muted','accent','success','alert'):
        assert token in colors
    for foreground in ('text','secondary','muted'):
        for surface in ('background','surface','elevated','card','selected'):
            assert contrast(colors[foreground],colors[surface])>=4.5,(key,foreground,surface)
    assert contrast(colors['on_accent'],colors['accent'])>=4.5
    assert len(set(TYPE.values()))>=4 and len(set(WEIGHT.values()))>=2
    assert tuple(SPACE.values())==(4,8,12,16,24,32)
    assert RADIUS=={'card':12,'button':8}

from PySide6.QtCore import QPoint,Qt,QCoreApplication,QEvent
from PySide6.QtGui import QImage,QColor
from PySide6.QtWidgets import QWidget,QPushButton,QLabel
from checkpoint.window import MainWindow
from checkpoint.dialogs import GameDialog
from checkpoint.design_system import CardSurface


def settle(app):
    for _ in range(6):app.processEvents()


def dispose(widget,app):
    # Só widgets criados por estes testes; nenhuma tarefa de cadastro é abortada.
    widget.deleteLater()
    QCoreApplication.sendPostedEvents(None,QEvent.DeferredDelete)
    settle(app)


@pytest.fixture
def visual_window(app,library,folder,monkeypatch):
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *args:None)
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    path=folder/'cover.png';image=QImage(400,600,QImage.Format_RGB32);image.fill(QColor('#48637c'));image.save(str(path))
    identity=library.save_game({'title':'Jogo em andamento','status':'Jogando','platform':'PC','cover':str(path),'developer':'Estúdio','publisher':'Editora','description':'Descrição para verificar largura e hierarquia. '*8})
    for index in range(9):
        game=library.save_game({'title':('Título muito longo para avaliar elipse e alinhamento ' * 6) if index==0 else f'Jogo {index}','platform':'PC','cover':str(path)})
        if index>=4:
            with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(game,))
    from checkpoint.integrations.drive import DriveScanner
    DriveScanner(library,None).record({'id':'visual-row','name':'Example (USA).gba'},'/Fixtures/GBA');library.sql.commit()
    window=MainWindow(library);window.integration_status=lambda provider:'Não configurada';window.resize(1280,800);window.show();settle(app)
    yield window,identity
    window.close();dispose(window,app)


def assert_inside_horizontal(root):
    outside=[]
    for widget in root.findChildren(QWidget):
        if not widget.isVisibleTo(root) or widget.isWindow() or widget.width()==0:continue
        left=widget.mapTo(root,QPoint(0,0)).x();right=left+widget.width()
        if left<0 or right>root.width()+1:
            outside.append((type(widget).__name__,widget.objectName(),left,right,root.width()))
    assert not outside,outside


@pytest.mark.parametrize('theme',['green','pink'])
@pytest.mark.parametrize('screen',['home','library','wish','detail','sparse','settings-0','settings-1','settings-2','settings-3','add','drive'])
def test_scope_fits_1280_without_horizontal_overflow(app,visual_window,theme,screen):
    window,identity=visual_window;window.set_theme(theme);window.resize(1280,800)
    dialog=None
    if screen in ('home','library','wish'):window.navigate({'home':0,'library':1,'wish':2}[screen])
    elif screen=='detail':window.detail(identity)
    elif screen=='sparse':
        game=window.library.save_game({'title':'Sem ficha','platform':'PC'});window.detail(game)
    elif screen.startswith('settings'):
        window.navigate(5);window.settings_tabs.setCurrentIndex(int(screen[-1]))
    else:
        dialog=GameDialog(window,library=window.library);dialog.show()
        if screen=='drive':dialog.source_tabs.setCurrentIndex(1);dialog.quick_add.query.setText('Example')
    settle(app)
    try:
        assert window.width()==1280
        assert_inside_horizontal(window)
        if dialog:
            assert dialog.width()<=1280 and dialog.height()<=800
            assert_inside_horizontal(dialog)
        if screen in ('detail','sparse'):
            actions=window.detail_page.findChild(QWidget,'gameActions')
            assert actions.height()==64
            assert window.detail_tabs.y()-actions.geometry().bottom()<=18
            gallery=window.detail_page.findChild(QWidget,'detailGallery')
            panels=[widget for widget in window.detail_tabs.currentWidget().findChildren(CardSurface) if widget.parentWidget()==gallery.parentWidget()]
            assert len({widget.y() for widget in panels})==1
    finally:
        if dialog:dialog.reject();dispose(dialog,app)


@pytest.mark.parametrize('page',[0,1,2])
def test_empty_pages_have_title_description_and_action(app,library,monkeypatch,page):
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *args:None)
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    window=MainWindow(library);window.show();window.navigate(page);settle(app)
    try:
        frame=window.pages[page].findChild(QWidget,'emptyState')
        assert frame and frame.isVisible()
        assert frame.findChild(QLabel,'sectionTitle').text().strip()
        assert len(frame.findChild(QLabel,'emptyDescription').text())>20
        assert any(button.isVisible() and button.isEnabled() for button in frame.findChildren(QPushButton))
        if page==1:
            from checkpoint.ui_components import ResponsiveToolbar
            toolbar=window.pages[1].findChild(ResponsiveToolbar)
            assert toolbar.y()==0
            assert frame.y()-toolbar.geometry().bottom()<=26
    finally:window.close();dispose(window,app)


def test_library_and_wishes_reuse_art_component_and_dimensions(app,visual_window):
    from checkpoint.cover_art import CoverArtwork
    from checkpoint.collection_views import WishCard,WishLogo,WishGrid
    window,_=visual_window;window.navigate(2);settle(app)
    assert window.gallery.itemDelegate().art_component is CoverArtwork
    cards=window.pages[2].findChildren(WishCard)
    assert cards and all(isinstance(card,CardSurface) for card in cards)
    assert len({(card.width(),card.height()) for card in cards})==1
    assert all(isinstance(card.findChild(WishLogo),CoverArtwork) for card in cards)
    assert window.gallery.property('cardComponent')==window.pages[2].findChild(WishGrid).property('cardComponent')


def test_protected_drive_and_registration_logic_is_unchanged():
    import ast,subprocess
    from pathlib import Path
    # A 0.1.33 muda somente a apresentação dos candidatos e da ausência de dados.
    # Os demais métodos e os caminhos de persistência/lifecycle continuam congelados.
    names={'apply_catalog','validate','finish_or_wait','accept','reject','load_drive_file','source_changed','data'}
    for filename in ('checkpoint/quick_add.py','checkpoint/dialogs.py'):
        original=ast.parse(subprocess.check_output(['git','show',f'c51c245:{filename}'],text=True))
        current=ast.parse(Path(filename).read_text())
        def methods(tree):
            return {node.name:ast.dump(node,include_attributes=False) for node in ast.walk(tree)
                    if isinstance(node,ast.FunctionDef) and ((filename.endswith('quick_add.py') and node.name not in {'show_result','show_missing_metadata'}) or node.name in names)}
        assert methods(original)==methods(current),filename
    for filename in ('tests/test_drive_search_flow.py','scripts/drive_search_flow_support.py','tests/test_drive_metadata_policy.py','checkpoint/game_import.py','checkpoint/worker.py','checkpoint/enrichment.py','checkpoint/completion_queue.py'):
        assert subprocess.check_output(['git','show',f'c51c245:{filename}'])==Path(filename).read_bytes()


def test_sparse_detail_and_gallery_explain_missing_content(app,visual_window):
    window,_=visual_window
    identity=window.library.save_game({'title':'Ficha sem dados','platform':'PC'})
    window.detail(identity);settle(app)
    frames=[frame for frame in window.detail_page.findChildren(CardSurface) if frame.property('emptyState')]
    assert len(frames)>=2
    for frame in frames:
        assert frame.findChild(QLabel,'emptyDescription').text()
        assert any(button.isEnabled() for button in frame.findChildren(QPushButton))


def test_settings_without_accounts_still_has_states_and_actions(app,visual_window):
    window,_=visual_window;window.navigate(5);window.settings_tabs.setCurrentIndex(1);settle(app)
    from checkpoint.design_system import CardGrid
    grid=window.settings_tabs.currentWidget().findChild(CardGrid,'connectionsGrid')
    assert len(grid.cards)==4 and len({card.width() for card in grid.cards})==1
    for frame in grid.cards:
        assert any(label.text()=='Não configurado' for label in frame.findChildren(QLabel))
        assert any(button.text()=='Conectar' for button in frame.findChildren(QPushButton))
    assert not window.settings_tabs.tabBar().expanding()


def test_empty_drive_list_has_explanation_and_existing_refresh_action(app,library,monkeypatch):
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get',lambda *args:None)
    dialog=GameDialog(library=library);dialog.source_tabs.setCurrentIndex(1);dialog.show();settle(app)
    try:
        empty=dialog.findChild(QWidget,'resultEmptyState')
        assert empty.isVisible() and empty.findChild(QLabel,'emptyDescription').text()
        assert dialog.quick_add.drive_manage.isVisible() and dialog.quick_add.drive_manage.isEnabled()
        assert not dialog.quick_add.save.isEnabled()
    finally:dialog.reject();dispose(dialog,app)


def test_empty_search_dialog_keeps_instruction_and_disabled_save(app,library):
    dialog=GameDialog(library=library);dialog.show();settle(app)
    try:
        assert dialog.quick_add.title.text()=='Nenhum jogo selecionado'
        assert len(dialog.quick_add.facts.text())>20
        assert dialog.quick_add.query.isVisible()
        assert dialog.quick_add.cancel.isEnabled() and not dialog.quick_add.save.isEnabled()
    finally:dialog.reject();dispose(dialog,app)


def test_reapplying_same_theme_does_not_repolish_all_widgets(app,monkeypatch):
    from checkpoint.theme import apply_theme
    apply_theme(app,'green')
    calls=[]
    original=app.setStyleSheet
    def tracked(style):
        calls.append(style)
        original(style)
    monkeypatch.setattr(app,'setStyleSheet',tracked)
    apply_theme(app,'green')
    assert calls==[]
    apply_theme(app,'pink')
    assert len(calls)==1

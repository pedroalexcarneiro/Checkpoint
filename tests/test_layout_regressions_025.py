from PySide6.QtWidgets import QLabel
from checkpoint.window import MainWindow
from checkpoint.design_system import empty_state


def test_home_search_opens_library_results(library,app):
    library.save_game({'title':'Zelda'})
    library.save_game({'title':'Outro'})
    window=MainWindow(library)
    window.search.setText('zelda')
    app.processEvents()
    assert window.current_page==1
    assert window.gallery.count()==1
    assert 'Zelda' in window.gallery.item(0).text()
    assert not window.add_button.isHidden()
    window.close()


def test_empty_state_omits_instructional_description(app):
    widget=empty_state('wish','Sua lista de desejos','Guarde os jogos que você quer.')
    widget.resize(1000,440);widget.show();app.processEvents()
    assert not any(label.text().startswith('Guarde') for label in widget.findChildren(QLabel))
    widget.close()


def test_sidebar_and_page_bounds_at_full_hd(library,app):
    library.save_game({'title':'Layout'})
    window=MainWindow(library);window.resize(1920,1080);window.show()
    for page in range(6):
        window.navigate(page);app.processEvents()
        assert window.add_button.isVisible()==(page in (0,1))
        sidebar=window.centralWidget().findChild(__import__('PySide6.QtWidgets',fromlist=['QWidget']).QWidget,'sidebar')
        assert sidebar.x()==0
        assert window.header_widget.width()<=1392
        assert window.header_widget.width()>=700
    window.close()


def test_add_game_uses_library_from_home_and_library(library,app,monkeypatch):
    window=MainWindow(library);window.navigate(1)
    pages=[];monkeypatch.setattr(window,'add_game',lambda:pages.append(window.current_page))
    window.add_button.click()
    assert pages==[1]
    window.navigate(0);window.add_button.click()
    assert pages==[1,1]
    assert window.add_button.text()=='+ Adicionar jogo'
    window.close()


def test_large_steam_import_keeps_dialog_bounded_without_per_game_log(library,app,monkeypatch):
    import time
    from PySide6.QtCore import Qt
    from PySide6.QtTest import QTest
    from checkpoint.steam_dialog import SteamDialog
    from checkpoint.integrations.steam import SteamGame
    monkeypatch.setattr('checkpoint.worker.run_isolated',lambda *a,**kw:'Ficha e imagens verificadas '+('detalhe '*100))
    dialog=SteamDialog(library);dialog.show()
    games=[SteamGame(str(index+1),f'Jogo {index} '+('título longo '*10),0) for index in range(300)]
    dialog.show_games(('76561198000000000',games));app.processEvents()
    before=dialog.size()
    assert dialog.table.verticalScrollBar().maximum()>0
    dialog.mark_all(Qt.Checked);dialog.import_selected()
    # Verifica layout/resultado, não um limite de desempenho do runner Windows.
    deadline=time.monotonic()+60
    while dialog.job and time.monotonic()<deadline:QTest.qWait(10)
    assert dialog.job is None
    app.processEvents()
    assert dialog.size()==before
    assert dialog.height()<=760 and dialog.width()<=1100
    assert '300 jogos processados de 300' in dialog.state.text()
    assert '\n' not in dialog.state.text() and len(dialog.state.text())<150
    dialog.close()


def test_wishlist_fetches_missing_logo_once_and_updates_card(library,app,monkeypatch,tmp_path):
    from PySide6.QtGui import QImage,QColor
    from checkpoint.collection_views import WishLogo
    identity=library.save_game({'title':'Logo fixture'})
    with library.sql:
        library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
        library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(identity,'steam','367520'))
    library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
    window=MainWindow(library);window.show();app.processEvents()
    requests=[];monkeypatch.setattr(window.completion_queue,'submit',lambda ids:requests.append(ids))
    library.set_setting('artwork.auto',True)
    window.navigate(2);app.processEvents()
    assert requests==[[identity]]
    window.navigate(2);app.processEvents();assert len(requests)==1
    path=tmp_path/'logo.png';image=QImage(240,80,QImage.Format_ARGB32);image.fill(QColor('red'));image.save(str(path))
    library.save_game({'title':'Logo fixture','logo':str(path)},identity)
    window.game_completed(identity,'Logo obtida');app.processEvents()
    logo=window.pages[2].findChild(WishLogo)
    assert not logo.pixmap.isNull()
    captured=logo.grab().toImage()
    assert captured.pixelColor(captured.width()//2,captured.height()//2).red()>240
    assert window.current_page==2 and len(requests)==1
    window.close()

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from checkpoint.window import MainWindow
from checkpoint.collection_views import WishCard,WishLogo
from checkpoint.locale import count_text


def drain(app):
    for _ in range(4):app.processEvents()


def test_wishlist_one_and_five_cards_keep_same_fixed_square_art_area(library,app):
    library.set_setting('prices.auto',False);library.set_setting('artwork.auto',False)
    window=MainWindow(library);window.show();dimensions={}
    for total in (1,5):
        while library.sql.execute('SELECT count(*) FROM wishlist').fetchone()[0]<total:
            identity=library.save_game({'title':f'Desejo {len(library.games())+1}'})
            with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
        for width,height in ((1000,700),(1920,1080)):
            window.resize(width,height);window.navigate(2);drain(app)
            cards=window.pages[2].findChildren(WishCard)
            assert len(cards)==total and len({(card.width(),card.height()) for card in cards})==1
            assert all(card.height()>card.width() and card.height()<height for card in cards)
            logos=[card.findChild(WishLogo) for card in cards]
            assert len({(logo.width(),logo.height()) for logo in logos})==1
            assert all(logo.width()==logo.height() for logo in logos)
            assert all(card.rect().contains(logo.geometry()) for card,logo in zip(cards,logos))
            assert all(not first.geometry().intersects(second.geometry()) for index,first in enumerate(cards) for second in cards[index+1:])
            if total==1:dimensions[width]=(cards[0].size(),logos[0].size())
            else:assert dimensions[width]==(cards[0].size(),logos[0].size())
    assert any(label.text()=='5 jogos' for label in window.pages[2].findChildren(QLabel));window.close()


def test_library_has_responsive_vertical_columns_at_minimum_and_full_hd(library,app):
    for index in range(9):library.save_game({'title':f'Jogo {index}'})
    window=MainWindow(library);window.show();window.navigate(1)
    for width,height in ((1000,700),(1920,1080)):
        window.resize(width,height);drain(app);grid=window.gallery
        first=[grid.visualItemRect(grid.item(index)) for index in range(grid.count()) if grid.visualItemRect(grid.item(index)).top()==0]
        assert len(first)==(6 if width==1920 else grid.columns) and all(rect.height()>rect.width() for rect in first)
        assert first[-1].right()<=grid.viewport().width()
    window.close()


def test_count_helper_handles_zero_singular_plural_and_irregular():
    assert count_text(0,'jogo')=='0 jogos'
    assert count_text(1,'jogo')=='1 jogo'
    assert count_text(5,'jogo')=='5 jogos'
    assert count_text(1,'sessão','sessões')=='1 sessão'
    assert count_text(2,'sessão','sessões')=='2 sessões'

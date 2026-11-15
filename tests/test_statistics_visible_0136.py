from test_bugs_0134 import ui,sample
from PySide6.QtWidgets import QLabel,QToolButton


def test_genres_are_removed_from_statistics_and_completions_remain(ui,app):
    w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'genre':'Aventura','status':'Concluído'},i)
    w.navigate(4);app.processEvents()
    assert not any(b.text()=='Mais estatísticas' for b in w.pages[4].findChildren(QToolButton))
    genres=[l for l in w.pages[4].findChildren(QLabel) if l.text()=='Aventura · 1']
    assert not genres
    assert not any(l.text()=='Gêneros da coleção' for l in w.pages[4].findChildren(QLabel))
    assert any(l.text()=='Conclusões no período' for l in w.pages[4].findChildren(QLabel))
    assert w.library.get(i)['genre']=='Aventura' and w.library.get(i)['status']=='Concluído'

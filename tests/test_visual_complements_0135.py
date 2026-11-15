import pytest
from PySide6.QtWidgets import QLabel
from checkpoint.price_view import price_summary
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_visual_a_no_official_offer_has_reason(app,library,title):
 i=library.save_game({'title':title})
 with library.sql:library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
 library.set_setting(f'prices.ggdeals.{i}',{'lowest':None,'retail':None,'currency':'BRL','state':'ready','checked_at':'2026-11-14T12:00:00+00:00'})
 frame=price_summary(library,library.get(i))
 labels=[label.text() for label in frame.findChildren(QLabel)]
 assert '-' in labels and 'Indisponível' not in labels
 assert 'Consulta sem oferta em lojas oficiais.' in labels

@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_visual_a_no_id_is_explicit(app,library,title):
 i=library.save_game({'title':title});frame=price_summary(library,library.get(i))
 labels=[label.text() for label in frame.findChildren(QLabel)]
 assert '-' in labels and 'Sem ID da Steam para consultar ofertas.' in labels
 assert 'Indisponível' not in labels

import pytest
from checkpoint.wiki_text import intro
@pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
def test_wiki_parentheses_and_written_dates(title):
 raw=title+' (日本語 (nome original)) é uma aventura de exploração. Foi lançado em vinte e um de março de dois mil e um. A história acompanha uma jornada por cavernas.'
 result=intro(raw)
 assert '日本語' not in result and '(' not in result and ')' not in result
 assert 'março' not in result and 'dois mil' not in result
 assert 'aventura de exploração' in result and 'jornada por cavernas' in result

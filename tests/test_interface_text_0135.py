import pytest
from PySide6.QtWidgets import QLabel
from test_bugs_0134 import ui,sample

REMOVED=(
 'O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.',
 'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.',
 'Serviços para completar fichas, imagens e arquivos.',
 'Seu banco de jogos e suas preferências.',
 'Cópias de segurança dos saves configurados.',
 'Consulte as versões disponíveis sem alterar sua biblioteca.',
 'Jogos removidos poderão ser restaurados aqui.',
 'Conquistas, sessões e memórias recentes.',
 'Suas sessões, conquistas e anotações aparecerão aqui.',
 'Retome de onde você parou.',
 'Jogos prontos para a sua próxima escolha.',
 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.',
 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.',
 'Guarde conquistas e objetivos pessoais deste jogo.',
 'Guarde suas melhores cenas',
)
@pytest.mark.parametrize('page',range(7))
def test_interface_has_only_labels_data_and_actionable_absence(ui,app,page):
 w,i=ui
 description='Descrição externa integral do jogo.';notes='Texto digitado pelo usuário.'
 w.library.save_game({'title':w.library.get(i)['title'],'description':description,'notes':notes},i)
 if page==6:w.detail(i);target=w.detail_page
 else:w.navigate(page);target=w.pages[page]
 app.processEvents();texts=[label.text() for label in target.findChildren(QLabel)]
 assert not set(REMOVED).intersection(texts)
 if page==6:assert description in texts and notes in texts
 if page==3:assert any('Memórias' in text and 'anotação' in text for text in texts)

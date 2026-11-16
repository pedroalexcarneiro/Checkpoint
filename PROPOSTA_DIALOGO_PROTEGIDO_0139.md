# Item 12 — proposta específica, ainda não aplicada

Arquivo protegido: checkpoint/dialogs.py.
Método: ImageDialog.__init__. Atualmente cria QDialog nativo 1000×750 e
reduz uma única vez a imagem a 950×680; não configura a barra Windows nem
recalcula o conteúdo ao redimensionar. É a visualização de captura já existente.

Proposta restrita à apresentação: chamar o novo helper opt-in de diálogos
após montar o layout, com título original do arquivo; usar visualização da
imagem inteira cuja escala acompanha a área disponível. Fechar/Escape continuam
rejeitando o modal e não modificam mídia, banco, sessão nem cadastro.
Não mudar GameDialog, métodos de cadastro, QuickAdd ou qualquer caminho A4.
Não normalizar os demais bytes do arquivo protegido.

O contrato tests/test_visual_0132.py permanece intacto. Embora seu conjunto
AST não inclua ImageDialog.__init__, a proteção textual adicional do pedido
abrange o arquivo inteiro. Por isso a proposta aguarda autorização específica,
sem interceptar o diálogo por fora para contornar essa proteção.

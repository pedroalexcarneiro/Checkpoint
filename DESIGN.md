# Direção visual do Checkpoint

## Revisão de fidelidade — 0.1.19

O usuário não aprovou a fidelidade da implementação 0.1.18 às imagens. Manter as
referências como alvo; conferir capturas reais, hierarquia, proporções e estados
sem arte. Cards próprios substituem a aparência nativa da lista; Início usa duas
colunas abaixo do hero. Metadados não devem voltar a um formulário largo na ficha.
A validação funcional não equivale à aprovação visual do usuário.

Direção aprovada com o usuário e implementada inicialmente na 0.1.18.

## Identidade

O símbolo é C//. Na palavra, as duas barras substituem o i: checkpo//nt.
Elas pertencem ao corpo da palavra, sem ponto ou acento acima. Símbolo e nome
ficam separados por 18 pixels lógicos (um pouco mais de respiro). O desenho é
vetorial Qt, nítido com escala/DPI e colorido pelo tema. O executável recebe
ICO multirresolução; o ícone estático usa o tema verde padrão.

## Telas

- Início: banner de um jogo da própria biblioteca, continuidade, adicionados e
  atividade pessoal. Sem loja, publicidade ou conteúdo inventado.
- Biblioteca: capas inteiras 3:4, busca, abas Todos/Favoritos/Jogando/Concluídos,
  filtros extras recolhidos, opção de lista e densidade compacta/confortável.
- Ficha: banner e logo, sem repetir a capa. Ações secundárias em ⋯; Visão geral,
  Atividade, Memórias e Arquivos. Execução, versões, saves e edição continuam reais.
- Cadastro: entradas Pesquisar jogo / ROM do Drive / Steam. Formulário simples,
  opções avançadas recolhidas, identificação e imagens em segundo plano após salvar.
  Não reintroduzir carregamentos modais automáticos no salvamento.
- Configurações: Aparência / Conexões / Downloads / Dados e backup. Cards curtos,
  ajuda sob demanda, detalhes avançados e lixeira recolhidos. Uma credencial salva
  significa Configurado, nunca conexão autenticada comprovada.

## Imagens e comportamento

A capa pertence à biblioteca; banner e logo identificam a ficha. A arte principal
é exibida inteira, sem deformação. O fundo derivado do banner só preenche margens;
o original e o cache não são modificados. Somente bordas transparentes do logo
podem ser aparadas para apresentação. Sem imagens, há título/estado vazio coerente.

Todos os dez temas existentes permanecem disponíveis, inclusive o branco.
Atualizar imagens não pode apagar um rascunho de diário em edição. A posição da
aba da ficha e a seção de Configurações devem sobreviver às reconstruções da tela.
As prévias usam fixtures fora do repositório; não incluir jogos demonstrativos na
biblioteca distribuída nem tratar fixtures como validação de serviços autenticados.

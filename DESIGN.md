# Direção visual do Checkpoint

## Sistema visual completo — 0.1.22

A referência aprovada orienta toda a aplicação: shell carvão, wordmark central,
sidebar de 198 px, tipografia compacta, botões com cor do perfil, biblioteca de
capas, hero com banner/logo, continuidade e feed pessoal. Sem copiar identidade
de terceiros nem inserir conteúdo fictício na biblioteca distribuída.

- Títulos 28 px, seções 18 px, corpo 14 px e legendas 12 px; espaçamentos 8–28 px.
- Superfícies com gradiente sutil, raio 7–11 px, borda discreta e contraste em dez temas.
- Ícones vetoriais comuns para navegação, perfis, tempo, marcos, arquivos e ações.
- Header com altura estável; grade confortável de quatro colunas na janela mínima.
- Ficha: quatro abas completas, cards de atividade/memórias e arquivos/saves com ações.
- Desejos e Memórias usam coleções visuais, não as antigas listas de botões.
- Configurações usam amostras de cores e cards compactos; perfil é local, sem conta remota.
- Editor opcional em quatro abas. Diálogos compartilham títulos, dimensões e controles.
- Estados vazios úteis, indicadores pequenos, foco/hover e nomes acessíveis.

Arte continua inteira: sem corte de texto, distorção ou cópia desfocada. Formatos
atípicos preservam a proporção dentro da área, enquanto posters 2:3 ocupam o espaço.
Biblioteca e imagens pessoais não são modificadas pela apresentação.
Revisão visual: 37 capturas reais com fixtures, incluindo formatos mistos, janelas
pequenas, temas escuro/roxo/branco, abas e diálogos. Arquivos são gerados fora do
repositório e disponibilizados como ui-review.zip, sem banco/logs/credenciais.


## Ajuste de direção — 0.1.21

O nome centralizado é o wordmark checkpo//nt original, sem o símbolo C//.
A orientação anterior de texto simples foi uma interpretação incorreta.
Início, biblioteca e ficha continuam seguindo a composição das referências:
lateral compacta, busca à direita, abas segmentadas, cards de atividade com
ícones, biblioteca com filtros que quebram em outra linha sem cortar abas,
retorno dentro do hero da ficha. Nenhuma validação funcional é aprovação estética.
Cadastro tem busca única ampla e prévia; as bases são detalhes da integração,
não etapas que o usuário precisa repetir para cada jogo. Metadados e imagens
disponíveis são o padrão; editor e importação Steam em lote são opcionais.


## Revisão após capturas Windows — 0.1.20

Na 0.1.20 a barra lateral mostrava Checkpoint simples centralizado; o símbolo fica no
ícone do executável. Capas usam espaços 2:3 para os posters Steam, sem molduras
laterais: outras proporções preservam toda a arte, sem esticar nem cortar texto.
Cantos suaves acompanham a imagem. O banner define a altura do próprio quadro;
nenhuma cópia desfocada preenche margens. Títulos dos cards são pintados abaixo
da arte, sem layouts filhos de QPushButton sujeitos a sobreposição em DPI Windows.
Ficha: descrição/dados em duas colunas à esquerda, galeria pessoal à direita.
Estatísticas: quatro indicadores, tempo por período, distribuição de status,
mais jogados e plataformas. Todos derivados do SQLite, sem exemplos na biblioteca.
Carregamento: indicador de 16 px, texto curto e botão de interrupção de 24 px;
rodapé oculto quando ocioso. Mensagens transitórias desaparecem após seis segundos.
O usuário ainda precisa avaliar o resultado visual; testes não aprovam estética.

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
- Biblioteca: capas inteiras, espaço 2:3, busca, abas Todos/Favoritos/Jogando/Concluídos,
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
é exibida inteira, sem deformação. O quadro acompanha a proporção do banner, sem preenchimento desfocado;
o original e o cache não são modificados. Somente bordas transparentes do logo
podem ser aparadas para apresentação. Sem imagens, há título/estado vazio coerente.

Todos os dez temas existentes permanecem disponíveis, inclusive o branco.
Atualizar imagens não pode apagar um rascunho de diário em edição. A posição da
aba da ficha e a seção de Configurações devem sobreviver às reconstruções da tela.
As prévias usam fixtures fora do repositório; não incluir jogos demonstrativos na
biblioteca distribuída nem tratar fixtures como validação de serviços autenticados.

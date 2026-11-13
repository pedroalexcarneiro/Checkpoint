# Direção visual do Checkpoint

## Revisão 0.1.25

O prompt reenviado solicita dez temas: Branco restaurado substitui a decisão
histórica de remoção abaixo. Banners limitados a 220–300 px e área principal
a 1440 px; arte inteira, logos legíveis, legendas próximas, grade adaptativa,
cadastro global. Estados vazios com espaço textual e métricas/calendário
adaptativos. Referências do usuário são a especificação visual.

## Decisões finais desta continuidade — 12/11/2026

- Modo claro removido por pedido expresso posterior do usuário. Permanecem nove
  temas escuros e as preferências de cor existentes. Uma preferência legada `white`
  passa para Verde ao abrir; dados da biblioteca não são alterados. Esta decisão
  substitui os registros históricos de dez temas/tema Branco abaixo.

- O usuário descartou o modo quadrado da **Biblioteca** porque não há garantia de
  artes quadradas estáticas para todos os jogos. A Biblioteca mantém o formato
  vertical com área ampliada para o pôster e as imagens inteiras, sem corte/deformação. Não há seletor de formato
  quadrado nem obtenção paralela de artes quadradas nesta entrega.
- **Wishlist:** cards quadrados com logos estáticas, proporção preservada, mesma
  área de apresentação, título de uma linha, preço e ações alinhados. Ver ofertas, + e lixeira
  ficam na mesma linha; logos maiores sem fundo preto no tema claro. Sem logo,
  usa placeholder discreto e o título normal; não estica texto nem improvisa uma logo.
- **Horas de jogo:** calendário diário no estilo GitHub, com intensidade e tooltip
  de data/duração, últimos 12 meses ou ano escolhido. Usa sessões reais em UTC.
- Retirada a repetição do nome do serviço dos textos de preço. Os botões de ofertas
  continuam abrindo a comparação completa, com links originais preservados.
- Downloads/cadastro de artes recusam GIFs e animações. Os vídeos pessoais em
  Memórias continuam disponíveis; essa regra se refere às artes do jogo.

## Continuidade de design e PT-BR — revisão em 12/11/2026

Esta revisão parte de `codex/steam-library-import` em `d23439d`, árvore inicialmente
limpa. Implementação em `codex/design-fidelity-pt-br`, para revisão contra a branch
de desenvolvimento. `main`, tags e releases existentes foram preservadas. A versão
publicada continua v0.1.23. Esta revisão não declara o design aprovado/concluído.
As imagens anexadas pelo usuário continuam sendo a especificação visual; os
registros históricos de “interface completa” abaixo não representam sua aprovação.

- Shell e cabeçalhos compactados; Início mantém continuidade/atividade lado a lado
  em 1000 px; Biblioteca agrupa filtros sem perder lista, ordenação ou favoritos.
  Cadastro passa a diálogo compacto com Pesquisar jogo / ROM do Drive / Steam,
  sugestão em linha e configurações opcionais. Busca/enriquecimento continuam isolados.
- Ícones Steam e Drive são arquivos oficiais, sem redesenho. Incluídos nos dados do
  pacote Python e PyInstaller; origem em THIRD_PARTY_NOTICES.md. O smoke verifica assets.
- Biblioteca vertical com capas inteiras; wishlist em cards quadrados com logos,
  sem texto espremido e com preço/ações em posições comuns. O modo quadrado da
  Biblioteca foi descartado por decisão explícita do usuário, conforme nota acima.
- Steam solicita `brazilian`; datas localizadas da fonte são normalizadas em ISO.
  Ficha/editor/catálogos exibem DD/MM/AAAA; SQLite e contratos permanecem ISO.
  Publicadora, origem, categoria e nota existentes ficam sempre visíveis na ficha.
- ROMs com identidade confirmada podem obter texto PT da Wikipédia quando há artigo
  exato, plataforma compatível e tradução. Desambiguação, remake/ano incompatível e
  ausência de PT não são associados. Fonte/licença ficam visíveis; hash de texto
  protege edições locais. Inglês legado da Steam/RAWG só é substituído com comprovação
  de que ainda coincide com a fonte automática. Sem tradução disponível não há texto
  inventado nem promessa de cobertura integral. Fontes existentes são preservadas.
- Desejos não exibem status de progresso e não contam como coleção possuída nas
  estatísticas/Início/Biblioteca. “Adicionar à biblioteca” confirma aquisição.
  Retirar dos desejos preserva o cadastro como não possuído, recuperável em Dados e
  backup > Desejos removidos. Notas, histórico, status legado, artes e arquivos não
  são apagados. O campo legado de meta de preço é preservado no banco, sem uso na UI.
- Desejos mostra **menor preço atual do GG.deals**, não meta pessoal. A ficha apresenta
  lojas oficiais/keyshops, ofertas carregadas e links originais; botão abre a página
  brasileira com a comparação completa. Usa página pública BR identificada pelo
  redirecionamento oficial de AppID, moeda BRL verificada, cache de uma hora e fila
  espaçada em 6,5 s. Não precisa de chave de API. Falha não vira R$ 0: sinaliza
  indisponibilidade/valor salvo e mantém link e última consulta. Lista local pode ser
  parcial; todas as ofertas ficam acessíveis no GG.deals. Sem AppID/página confirmada,
  oferece pesquisa no site sem presumir uma associação.
- Estatísticas passam a calendário diário com intensidade e distribuição por barras,
  sem pizza; sessões/períodos ausentes recebem zero no intervalo apresentado.
  Totais continuam derivados do SQLite e horas Steam não duplicam sessões locais.

Schema permanece 4. Nenhum banco pessoal, ROM, save, nota, credencial ou log privado
foi lido, copiado ou versionado. Regressões cobrem edição manual, versão de ROM,
origens do cadastro, datas, wishlist/posse, formatos e cache/preços em BRL.
Windows tem workflow de validação de PR separado da publicação de releases.
Resultados efetivos e limitações estão em TESTING.md e evidence/design-ptbr-validation.txt.

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

# Revisão local após a 0.1.39 — em execução

Requisitos/ordem: PLANO_POS_0139.md. A versão publicada não é alterada.

Diagnóstico inicial:

- Início usa recent_sessions, uma linha por sessão. O pedido novo exige uma
  projeção única por ID de jogo, sem deduplicar ou apagar o histórico no banco.
- MemoryCarousel distribui todo o espaço entre os cards presentes; MemoryGrid
  também expande colunas. ArtworkButton pinta o fundo input na área que sobra.
  A correção deve retirar essas faixas artificiais sem recortar a captura.
- price_summary/comparison já exibem percentual quando selected_quote comprova
  original/atual da mesma oferta. A API oficial atual fornece currentRetail/
  currentKeyshops e historicalRetail/historicalKeyshops, sem original individual.
  O print contém histórico, que não permite deduzir desconto. Sem conta/cache do
  dono aqui, a causa da ausência específica não pode ser afirmada como homologada.
- O fundo foi construído a partir de constantes azul-petróleo, mesmo em outras
  cores. HTML de referência usa accent dinâmico e superfícies tingidas levemente,
  com variantes clara/escura. Usar somente esses tokens, nunca dados/scripts.

Preços de consoles continuam sem cobertura confirmada. Filtro não é consulta;
preço PC não é transferido para Switch/PlayStation/Xbox.

## Implementação e verificações direcionadas

- Itens 1–3: build_home usa recent_games sem limite, por ID, com session_id da
  última sessão. recent_sessions/execution_history continuam completos. Memórias
  usam teto 300 px no Início e 320 px na grade geral; mais itens conforme largura.
  ArtworkButton tem fundo opcional, desativado só nessas prévias. Arte inteira e
  áreas equivalentes de nota/captura preservadas; nenhum arquivo é regravado.
- Reprodução na base d57dc56, com teste corrigido e dois jogos: quatro falhas
  (repetição e largura). A primeira fixture tentou repetir um caminho único de
  mídia; foi corrigida para dois arquivos, sem alterar a restrição do banco.
- Primeiro ajuste: 49 testes direcionados aprovados. Na revisão visual, alguns
  cards recém-recriados ainda não estavam visíveis ao layout, causando sobreposição
  temporária. Política de largura fixa, limite de tamanho mínimo e show explícito
  após inserir resolvem a construção/redimensionamento, sem temporizador.
- Tema: nove cores preservam seus identificadores, com saturação moderadamente
  maior. Fundo/lateral/cards/barra do topo acompanham o destaque; Preto neutro.
  Claro/Escuro é uma preferência independente (appearance.mode), persistida e
  aplicada também às prévias. Padrão escuro para instalações existentes.
- 94 testes direcionados passaram antes da revisão final. A suíte integral inicial
  encontrou três falhas de contraste muted/selected (verde/amarelo/ciano) e foi
  interrompida para corrigir. O texto secundário é ajustado no código até 4,5:1;
  nenhuma asserção do teste protegido tests/test_visual_0132.py foi alterada.
- Após a correção: final-targeted, 92 passed in 24.75s, exit 0, incluindo as 18
  combinações claro/escuro e contraste de texto/secondary/muted em cinco superfícies.
  Nova suíte integral será executada no código congelado.

## Expectativas atualizadas por requisito posterior

- test_home_polish_0139: fixture de navegação passa a ter cinco jogos distintos,
  preservando todas as asserções de setas/teclado; o teste do histórico com sessões
  repetidas permanece intacto. Motivo: pedido explícito de não repetir jogo no Início.
- test_polish_0139: a exigência de fundo verde fixo em #0e141d foi substituída
  pela distinção entre fundos de cores diferentes. Preto neutro e nove opções
  continuam cobertos. Motivo: pedido explícito de remover o fundo azul fixo.

## Limites e decisões abertas

- Percentual: interface existente testada com original válido da mesma oferta;
  a API atual não preenche esse dado. Não calcular a partir do histórico. Proposta
  de complemento opcional em PROPOSTA_DESCONTOS_POS_0139.md, ainda não implementada
  nem ativada; pergunta de preferência apresentada ao dono.
- Ofertas: comparação real com capa 52×70 e banner inteiro 120×40. O banner não
  deforma, mas fica baixo e reduz o espaço dos textos na coluna estreita. Mantida
  a capa no aplicativo; alternativa de banner existe só no renderizador descartável.
- Capturas são Qt real/Linux com dados próprios, não a biblioteca do dono nem
  homologação Windows. Nenhum push/workflow/tag/release desta revisão.

## Fechamento da etapa visual e complemento aprovado

Suíte integral da etapa visual em f4a7139: **789 passed in 556.71s (0:09:16)**,
exit 0, Linux/Python 3.12.14, QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp.
Esse resultado antecede o novo serviço de preços aprovado posteriormente.

O dono escolheu “Adicionar complemento opcional do GG.deals”. Implementado em
price_enrichment.OfferDetailsProvider, selecionado por prices.default_provider
somente com a opção prices.offer_details ativa e API configurada. Controle
ggdealsOfferDetails em Conexões, desativado por padrão; altera versão do cache
sem descartar valores. refresh_prices registra a configuração do início da
consulta para não marcar como fresca uma resposta iniciada antes da mudança.

O teste real da página pública de Cyberpunk mostrou regular em base-price,
enquanto o coletor anterior lia somente price-old. Mostrou também ofertas com
data-game-name de Xbox & PC/Ultimate dentro da página canônica de PC. O parser
agora lê os dois formatos, filtra produtos com identificação diferente e calcula
mínimos apenas com as ofertas correspondentes quando a página traz esses IDs;
agregados/cabeçalhos não sobrepõem essa confirmação.

O complemento exige canônico, BRL, produto da oferta e valor coincidentes com
a API. Não traz o preço de outra oferta para a API. Se um mínimo da API só
coincidir com produto excluído, o cache bruto é mantido, mas esse grupo não é
apresentado como preço confirmado da edição. Divergência simples mantém o preço
atribuído à API e não inventa percentual; Ofertas do Início não promove esse caso.
Keyshops continuam dependentes de sua opção própria, sem entrar no padrão oficial.

Reprodução sem a opção/serviço: 11 failed, 1 passed. Após implementação: conjuntos
direcionados de 69, 28, 77, 75, 82 e finalmente **83 passed in 17.99s**, exit 0,
incluindo ficha, opção/cache, dois jogos, edições divergentes, preço divergente,
falha pública, API falhando, configuração mudando durante consulta e loja de chaves.
Nenhuma asserção antiga de preços foi modificada. Nova suíte integral necessária
para o conjunto com o serviço; será registrada após concluir.

Consultas públicas reais a Cyberpunk e Hades executadas sem chave/conta. A versão
filtrada retornou apenas produtos canônicos; nessas consultas as ofertas PC não
informaram original maior que o atual, portanto nenhum percentual foi inventado.
O teste não homologa a API autenticada do dono, rede/cofre/Windows ou disponibilidade
permanente da página. Metadados em /workspace/work/evidence-pos-0139/public-live-final.json.

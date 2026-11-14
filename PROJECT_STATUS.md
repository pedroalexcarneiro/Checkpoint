# Estado atual — Checkpoint 0.1.32

## Correções noturnas — fix/0.1.34-bugs (somente local)

Base: fix/0.1.33-drive em cffbeb3d744fade381ea7573a6602e41d616c5de. Código segue declarando 0.1.33; não houve lançamento ou alteração de versão. Concluídos os itens 1, 2, 3, 5, 7, 8 e 9: estado do Drive após seleção, ficha preenchida, cache de preço, refresh da arte, posição do menu, recorte proporcional de capas e resumo de Wikipédia. Item 4 sem erro reproduzido no mapeamento dos menus; item 6 revertido após falha do teste de coordenadas de imagem; item 10 revertido integralmente após a validação de indicador pequeno continuar falhando. Esses itens não fazem parte da branch final.

Validação final Linux Qt offscreen, dados em /tmp: 379 passed in 425.74s (0:07:05), exit 0. Cada correção mantida passou em teste com dois jogos e no teste de preservação. Só show_missing_metadata mudou em QuickAdd; dialogs.py, lifecycle e o teste de preservação ficaram intactos. O teste antigo de preço passou a exigir preservação de 5900 em vez de None, pois a nova regra exige reter o último valor válido. Nenhum skip/xfail novo. Windows real, DPI, contas e APIs reais não validados. Sem push, tag, release ou PR. Tempo Steam, logos de jogos e os layouts pendentes foram preservados. A nova regra de capas usa recorte central proporcional, prevalecendo sobre a orientação anterior de exibir a capa inteira.

## Trabalho atual — 0.1.33 Drive

Branch `fix/0.1.33-drive`, base `4bdb4ef`. Normalização No-Intro e candidatos na aba Drive; ficha incompleta com cabeçalho. Relatório: [RELATORIO_0133_DRIVE.md](RELATORIO_0133_DRIVE.md). Publicar somente esta branch, sem tag, release ou PR. Lifecycle e fluxos anteriores preservados. **357 passed in 474.59s (0:07:54)**, exit 0, sem falhas/erros/skips/xfails na execução final. Linux Qt offscreen, dados em /tmp.

## Contexto anterior

Trabalho atual: `fix/0.1.32-visual`, base `c51c2456f8479f208d73a1281eb0dfada8ee7213`. Revisão visual com tokens comuns aos nove temas, telas e estados vazios, sem alterar cadastro/Drive. Evidências e limitações em [RELATORIO_0132_VISUAL.md](RELATORIO_0132_VISUAL.md). Sem tag, release ou PR; publicar somente a branch visual, sem force. Preservar as branches 0.1.30 e 0.1.29.

Suíte integral final: **344 passed in 429.70s (0:07:09)**, exit 0; sem falhas/erros e sem novos skips ou xfails. Qt offscreen, CHECKPOINT_TEST_ROOT=/tmp, Python 3.12.

## Contexto preservado da base 0.1.30


## Correção do cadastro Drive

Branch fix/0.1.30 a partir de 90dec8e, sem alterar fix/0.1.29 nem releases. Cadastro de ROM pesquisa o nome limpo, aguarda os detalhes e grava textos com origem Busca; o arquivo fica vinculado e não é baixado. Arte persistida de ROM usa SteamGridDB. Sem dados: origem Não identificada, aviso persistente e botão Pesquisar manualmente; a recuperação reutiliza o cadastro e mantém o arquivo. Relatório: RELATORIO_0130_DRIVE.md.

Suíte final: 303 passaram, 0 falhas/erros em 546,27 s (Qt offscreen, dados em /tmp). As quatro regressões por cliques falham na base e passam com a correção. Fontes e transporte de imagens controlados; atual versão não homologada em Windows real ou com contas reais. Uma rodada parcial teve queda nativa no GC final do pytest; base e repetição passaram. Registro detalhado no relatório, sem skip/xfail nem mudança no teste de lifecycle.

## Funciona

- Biblioteca com capas verticais, tamanho de 70% a 150%, colunas responsivas e migração da densidade anterior.
- Início restrito a jogos Jogando/Pausado, destaque recente, atividade pessoal e estado vazio.
- Rolagem animada por pixel, com barras finas na cor do tema, em Biblioteca, Desejos, Memórias e Estatísticas.
- Desejos com área de arte 1:1, logo contida, alternativa de capa/título, preços atuais/históricos e atribuição, ordenação por nome ou menor preço e posição de rolagem preservada.
- Busca com origem correta e salvamento aguardando a ficha selecionada; diálogo com fechamento único e nomes de ROM limpos.
- Nove temas, Verde padrão; identidade checkpo//nt e ícone próprio; quatro Conexões em 2×2 e GG.deals abaixo, com indicadores de configuração.
- Migração não destrutiva de dados/cofre, schema 4, saves, diário, lixeira, Steam e Drive preservados.
- Diálogos aninhados aguardam seus jobs antes de concluir; regressões exercitam o fluxo com faulthandler.

## Prova do cadastro por busca

O teste de fluxo por cliques reproduz em 8d39c18 capa/banner presentes com
desenvolvedora vazia; na base atual a46bff4 os textos e origem Busca são preservados.
A automação d64d6a0 cobre salvar durante e depois dos detalhes, com fontes
controladas e persistência/cache/subprocessos reais. Não houve correção adicional no app.
Suíte integral desta verificação: 296 passando, 0 falhas/erros em 387,99 s.
Duas novas capturas real-flow-* registram o commit limpo da geração; as antigas
servem só como fixtures visuais. Consulte RELATORIO_FLUXO_BUSCA_0.1.29.md.

## Pendente

Configuração da chave pelo dono no cofre e validação autenticada da API GG.deals. Decisão sobre futura fonte de preço original para percentual, sem usar histórico. Remoção pelo dono da pré-release anterior publicada por engano. Futura decisão sobre unificar os três componentes de cadastro; a fusão não foi executada.

## Limitações

API oficial implementada e validada com respostas controladas; sem validação de conta real. O fallback público depende de HTML e pode ser bloqueado. A API retorna histórico, não preço original/desconto. As imagens e a ficha dependem da cobertura dos provedores. Testes e capturas desta revisão são Qt offscreen em Linux, com dados isolados; não validam Windows real, DPI ou contas autenticadas.

Resultados por etapa, diferenças visuais e caminhos das capturas estão em RELATORIO_CORRECOES.md. Histórico em CHANGELOG.md. Não houve build, tag nem publicação de release nesta revisão.

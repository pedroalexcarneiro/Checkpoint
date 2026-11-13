# Estado atual — Checkpoint 0.1.30

## Publicação posterior autorizada

Em 13/11/2026, após o pedido de publicação, a pré-release v0.1.30 foi publicada a partir de c51c2456f8479f208d73a1281eb0dfada8ee7213. Windows CI: 303 testes, zero falhas/erros/skips, build, smokes do fonte/executável extraído e revisão visual com fixtures aprovados (execução 43482592085). Publicação validada pela execução 43484462109. Código do app preservado; somente workflow e documentação acrescentados depois do commit da release. Download: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.30

A homologação no computador pessoal, contas reais e diferentes DPIs continua pendente. A etapa de correção abaixo usou Linux; o Windows CI foi executado posteriormente para publicar.

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

# Estado atual — Checkpoint 0.1.32

## Publicação posterior autorizada — 0.1.32

A pré-release [v0.1.32](https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.32) foi publicada após autorização posterior do dono. Tag em `29f34626efeda7a09d2bcc265e46578ef75a9941` (não na main). Execução Windows [43518936038](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43518936038): 344 testes, zero falhas/erros/skips, 336,454 s; build do app/atualizador e validação do ZIP extraído aprovados. Pacote portátil: `Checkpoint-0.1.32-windows-x64.zip`, 84.103.765 bytes, com SHA-256 e relatório de validação anexados à release. Isso comprova validação automática em Windows, não homologação manual de DPI/fontes/contas reais.

Primeira tentativa: 343 passaram e 1 falhou por conversão LF→CRLF no checkout Windows. O workflow foi ajustado com `core.autocrlf=false` antes do checkout; nenhum teste ou código do aplicativo foi alterado para resolver essa falha. Releases anteriores preservadas. As restrições de não publicar descritas na entrega visual original referem-se àquela etapa, antes da autorização de publicação.

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

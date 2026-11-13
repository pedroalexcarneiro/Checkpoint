# Continuidade do Checkpoint

## Publicação posterior autorizada — 0.1.32

A pré-release [v0.1.32](https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.32) foi publicada após autorização posterior do dono. Tag em `29f34626efeda7a09d2bcc265e46578ef75a9941` (não na main). Execução Windows [43518936038](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43518936038): 344 testes, zero falhas/erros/skips, 336,454 s; build do app/atualizador e validação do ZIP extraído aprovados. Pacote portátil: `Checkpoint-0.1.32-windows-x64.zip`, 84.103.765 bytes, com SHA-256 e relatório de validação anexados à release. Isso comprova validação automática em Windows, não homologação manual de DPI/fontes/contas reais.

Primeira tentativa: 343 passaram e 1 falhou por conversão LF→CRLF no checkout Windows. O workflow foi ajustado com `core.autocrlf=false` antes do checkout; nenhum teste ou código do aplicativo foi alterado para resolver essa falha. Releases anteriores preservadas. As restrições de não publicar descritas na entrega visual original referem-se àquela etapa, antes da autorização de publicação.

Trabalho atual: `fix/0.1.32-visual`, base `c51c2456f8479f208d73a1281eb0dfada8ee7213`. Revisão visual com tokens comuns aos nove temas, telas e estados vazios, sem alterar cadastro/Drive. Evidências e limitações em [RELATORIO_0132_VISUAL.md](RELATORIO_0132_VISUAL.md). Sem tag, release ou PR; publicar somente a branch visual, sem force. Preservar as branches 0.1.30 e 0.1.29.

Suíte integral final: **344 passed in 429.70s (0:07:09)**, exit 0; sem falhas/erros e sem novos skips ou xfails. Qt offscreen, CHECKPOINT_TEST_ROOT=/tmp, Python 3.12.

## Contexto preservado da base 0.1.30


Trabalho atual: versão 0.1.30, branch `fix/0.1.30`, iniciada no commit `90dec8e168d822698e176e5c93dd98951e01ab09`. O prefixo 90dec8e8 do pedido não existe; foi usado o 90dec8e confirmado na entrega anterior. Não alterar fix/0.1.29. Não usar a main defasada nem alterar as branches codex existentes.

Leia PROJECT_STATUS.md, RELATORIO_CORRECOES.md e ARCHITECTURE.md. Referências visuais e decisões do dono prevalecem: wordmark checkpo//nt e ícone próprio; Biblioteca vertical com tamanho ajustável e seis colunas no padrão largo; Desejos com arte 1:1; Início de andamento; ficha com galeria; quatro Conexões 2×2 e GG.deals abaixo. São nove temas, Verde padrão.

Não volte a permitir que um GameDialog conclua enquanto seus jobs de busca estão ativos, inclusive sob DriveDialog. Ao salvar durante a consulta de detalhes selecionados, aguarde a resposta no loop Qt e preserve desenvolvedora, editora e descrição. Não use skip/xfail para quedas nativas.

Valide com QT_QPA_PLATFORM=offscreen, CHECKPOINT_TEST_ROOT em /tmp e --data-dir novo nos smokes. O schema permanece 4; a migração copia e preserva a origem. Nunca consultar cofre real em testes.

Não criar tags, releases ou PRs nesta tarefa; dar push somente de fix/0.1.30, sem force. A pré-release 0.1.29 já existe e deve ser preservada, assim como as demais releases. A API oficial GG.deals permanece inalterada. Não fundir os componentes de cadastro sem decisão do dono.

No cadastro Drive, arquivo e origem de dados são independentes: origem Busca quando houver texto do catálogo; Não identificada quando não houver dados. Salvar fica indisponível até a pesquisa/detalhes terminarem. Sem resultado/falha, manter aviso e ação de pesquisa manual; não iniciar enriquecimento sem identidade para esconder o resultado da busca. Ao pesquisar novamente, preservar o vínculo da ROM e preencher o mesmo cadastro. Artes persistidas de ROMs devem vir do SteamGridDB, não do Drive nem da imagem RAWG/Steam. Provas, diffs e limitações em RELATORIO_0130_DRIVE.md.

## Prova adicional do cadastro pela busca

Base desta verificação: a46bff4. O commit d64d6a0 acrescenta automação por cliques
com fonte controlada e subprocessos reais. O mesmo teste perde desenvolvedora em
8d39c18 e passa na branch atual, inclusive salvando durante a consulta. Nenhum arquivo
de checkpoint/ ou test_save_lifecycle.py foi alterado nesta verificação. As novas
capturas real-flow-* têm commit limpo e hashes em real-flow-info.json; não representam
contas reais. As 16 capturas anteriores usam cadastro/preview manual e não comprovam
a busca. Detalhes e saídas completas: RELATORIO_FLUXO_BUSCA_0.1.29.md.

Suíte integral desta prova: 296 passaram em 387,99 s; sem falhas/erros, skips ou xfails novos.

Validação final 0.1.30: 303 testes passaram em 546,27 s, exit 0. A revisão adicional preserva add_game() sem argumentos para clicked(bool), com teste de abertura por Desejos. Os quatro casos Drive falharam na base e passaram sem alteração de teste/suporte. Rodada parcial com queda no GC e repetição bem-sucedida estão integralmente documentadas no RELATORIO_0130_DRIVE.md. Windows e fontes reais ainda não validados nesta versão.

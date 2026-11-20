# Continuidade do Checkpoint

## Revisão local após 0.1.39 — fix/pos-0139-layout

Base d57dc56, sem alterar publicação/tag 7703d80. Pedido novo: jogos únicos no
Início, memórias sem expansão/faixas artificiais (Início e grade), cores mais
vivas com fundos por destaque, claro/escuro e barra do topo adaptada. Implementado
localmente; gate final em d808f76: 808 testes Linux aprovados em 547,90 s,
smoke de seis páginas/SQLite aprovado. Relatório e capturas registrados em
RELATORIO_POS_0139_TESTES.md e evidence/ui-pos-0139/.
Após pedido de continuidade, branch enviada e workflow Windows UI validation
44749088810 aprovado: 808 testes Windows, pacote extraído/abertura nativa ok.
ZIP b24b3bac05b3705b368a29a4bc7ae6a88415786c318f1e12a515e51909e0b896.
Sem nova release/tag; publicação anterior preservada. RELATORIO_WINDOWS_POS_0139.md.
Percentual depende de dado original da oferta;
complemento opcional GG.deals público aprovado e implementado, com validação
por oferta/edição e opção desligada por padrão. Capa mantida após
comparação com banner. PLANO_POS_0139.md e RELATORIO_POS_0139.md registram a revisão.

## 0.1.39 publicada — correções e degradê aprovado

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.39
Tag/código: 7703d8048884009a5d9e9addb348620d4a788ff0. Windows release
44660106137 concluiu testes/build/pacote/publicação com sucesso. Linux:
764 passed in 487.00s; Windows/Python 3.12.10: 764 passed in 664.04s,
zero falhas/erros/skips. JUnit baixado e conferido; quadros vermelho/azul
passaram em duas janelas próprias usando backend nativo Windows.

Dez arquivos publicados baixados e conferidos por tamanho/SHA-256/digests
GitHub; CRC dos dois ZIPs válido. ZIP Windows: 84345311 bytes, SHA-256
dc6132969de8622e64ab4a36afbc0197c8de527a55cd6ad040813d18ddc9f4a3.
Fonte e executável extraído passaram por abertura normal nativa/SQLite/
cadastro/auxiliar/atualizador; runner já elevado não homologa consentimento UAC.
Tags/arquivos 0.1.38 e 0.1.37 preservados, sem force push ou mudanças de workflow.

HSR/DirectX/tela cheia e uso pessoal ainda não homologados. Console sem preço
autenticado comprovado, saves sem upload Drive e fechar apenas ROM continuam
limitações. Não declarar o projeto inteiro concluído. Relatórios completos:
RELATORIO_0139.md, RELATORIO_0139_TESTES.md e RELATORIO_LANCAMENTO_0139.md.
Documentação posterior não move a tag. Os registros seguintes são históricos.

## 0.1.39 — correções em validação e lançamento autorizado

Complementos implementados após o fechamento inicial: quadros novos na captura,
Memórias atualizada sem troca de aba, Estatísticas responsiva e degradê aprovado
na segunda prévia do Início. Os 752 testes abaixo antecedem esses complementos;
Nova suíte integral: 764 passed in 487.00s, exit 0, código 03272d0. Windows
a validar/publicar pelo workflow autorizado. Detalhes C1–C4 no plano/relatório.

Branch fix/0.1.39-polimento, base normal 0.1.38 em 9dd9c93. Variante sem
administrador preservada. Pedido inicial local; após revisar botões/aviso e ser
informado da pendência console, o dono autorizou: “quando finalizar, pode já dar
release no github”. Não mover tags/releases anteriores nem usar force push.

Início em largura útil, Últimas sessões sem deduplicar jogos, cards/arte compactos
inteiros/arredondados e ofertas com miniaturas; Desejos compactos; Diário com prévia
proporcional na grade mista e altura compacta em Diário; conclusões pela última
marcação já persistida; foco na capa e Preto neutro. Emuladores/Lixeira em abas,
perfis/vínculos preservados, restauração individual com data real/fallback,
nomes longos e saves compactos, ícones e diálogos em português/tema.

Única exceção nova protegida: ImageDialog.__init__, autorizada expressamente;
GameDialog/QuickAdd/A4 e demais protegidos intactos. Schema 4, UAC e dados
preservados. Suíte integral Linux final: **752 passed in 577.63s**, exit 0, sobre
8dd4c24; código preservado após a execução. Smokes de seis páginas/cadastro/SQLite
e verificação de contratos aprovados. Validação/publicação Windows a seguir. Capturas
Qt reais em 100/150/200%, bancos isolados; não homologam Windows do dono.

Consulta console continua bloqueada por capacidade/identificação/autenticação;
backup de saves é local, sem upload Drive; fechar só ROM continua limitação.
DIAGNOSTICO_INTEGRACOES_0139.md detalha provas e propostas. PLANO_0139.md,
RELATORIO_0139.md, RELATORIO_0139_TESTES.md e RELATORIO_LANCAMENTO_0139.md
registram andamento/gates/SHAs/resultados, inclusive tentativas descartadas.

## 0.1.38 publicada — correção de abertura

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.38

Tag/código: c4a7e1d221ba52a8580dd73ab884b1964e6ffd32. Windows release 43857996709 concluído com build e publicação aprovados. Windows/Python 3.12.10: 700 passed in 633.27s (0:10:33), zero falhas/erros/skips. Linux/Python 3.12.14: 700 passed in 483.81s (0:08:03), código funcional idêntico. Fonte e executável extraído passaram também por abertura normal com Qt windows, HWND visível/responsivo, captura, fechamento e SQLite, em Windows já elevado.

Dez arquivos publicados baixados e conferidos por tamanho/SHA-256 contra os digests do GitHub. CRC dos dois ZIPs válido. ZIP Windows: 84314842 bytes, SHA-256 15fef170b44dcf6073d50fed3f601f8b1cb265540c5e456113fe2befad0e3702. A 0.1.37/tag/arquivos foram preservados. Fonte do fix usa MSG.hWnd durante criação nativa, evitando chamar winId recursivamente; não muda dados, schema 4, cofre ou A4.

Upload local inicial recusado por autenticação em uploads.github.com; publicação concluída pelo workflow existente com identidade do próprio GitHub, sem alterar o workflow de release. A execução read-only anterior foi preservada como validação, e o publisher repetiu todos os gates. Documentação posterior não move a tag.

Consentimento UAC interativo e uso no PC do dono continuam sujeitos à confirmação; não confundir execução nativa já elevada no runner com consentimento automatizado. As demais limitações anteriores de fontes de preço, A4 e fechamento somente da ROM permanecem. Registros seguintes descrevem a preparação e as falhas de infraestrutura.

## Correção de abertura 0.1.38 — validada, sem publicação

Após relato e vídeo do dono de que a 0.1.37 não abre, foi identificado uso de QWidget.winId em callback de criação nativa, capaz de reentrar na criação. Branch fix/0.1.38-abertura, commit 5e77741: handler passa a usar MSG.hWnd. Nenhuma alteração em dados/cofre/A4/arquivos protegidos. A validação anterior offscreen não cobria essa sequência; a nova cobertura usa Qt windows no Windows e abertura normal do fonte/executável extraído com executor já elevado, HWND visível/responsivo/captura/fechamento.

700 testes Linux e 700 Windows aprovados. Windows UI validation 43799707113 concluiu build e abertura normal do fonte/executável extraído: HWND visível/responsivo, captura e fechamento, exit 0 e SQLite íntegro. Candidato ff13658; ZIP SHA-256 9f2238c621d0fb5fc9ed22106bee34b938283ef3f8b0cd7e96770a757496cfce. Publicação da 0.1.38 autorizada pelo dono; execução 43857996709 em andamento, sem mover a tag/arquivos 0.1.37. Não declarar abertura/consentimento UAC no PC do dono homologados. A 0.1.37/tag/arquivos permanecem preservados. Detalhes em PLANO_0138.md e RELATORIO_0138.md.

## Pré-release 0.1.37 publicada

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37

Tag/código: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52. Workflow https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592: testes/build/publicação concluídos com sucesso. Windows/Python 3.12.10: **695 passed in 638.21s (0:10:38)**, zero falhas/erros/skips. Linux/Python 3.12.14: **695 passed in 478.98s (0:07:58)**. Fonte, ZIP extraído, cadastro, auxiliar, atualizador e revisão visual aprovados. Oito arquivos publicados baixados e conferidos por tamanho/SHA-256; CRC dos dois ZIPs válido. ZIP Windows: 54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a.

Primeira execução foi interrompida após reproduzir vazamento do hotkey no próprio teste de fechamento. Correção só no teste, sem alterar aplicativo/asserções existentes/contratos. Nova execução aprovada. Histórico integral: RELATORIO_LANCAMENTO_0137.md. Esta atualização documental é posterior ao build e não move a tag.

Persistem preços console/original individual sem prova autenticada, homologação interativa de moldura/UAC/captura/launchers/contas/emuladores no PC do dono, A4 e fechar apenas a ROM. Elevação para outra conta é recusada para preservar dados/cofre. Runner Windows não homologa uso pessoal. A rodada não é declarada inteiramente concluída com essas pendências.

Registros seguintes descrevem a preparação e versões anteriores.

## Lançamento 0.1.37 autorizado — em preparação

Durante a validação final, o dono instruiu: “dps de acabar tu lanca a versao ta”. Essa autorização posterior permite enviar a branch 0.1.37 e acionar o workflow existente para testar/buildar/publicar a pré-release, depois de fechar as verificações. Não permite reescrever histórico/tags existentes nem remover contratos. Publicação ainda não realizada; resultados serão registrados em RELATORIO_LANCAMENTO_0137.md. Preços console, original da API e homologação real no PC continuam limitações explícitas.

## Rodada local 0.1.37 — implementação e validação

Branch fix/0.1.37-ajustes, base remota 0.1.36 reconfirmada em 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1. A fase inicial autorizou somente implementação/commits/validações locais; a autorização nova acima substitui a restrição de publicação. Versão declarada 0.1.37, schema 4. Workflows, assets e contratos protegidos preservados; notas públicas preparadas para esta versão após a autorização.

Implementados Início integrado com três capas inteiras em carrossel, resumo semanal real, lista de Ofertas com banners e memórias; Biblioteca em cards horizontais e grade com cache limitado, totais em consultas limitadas e arte carregada em segundo plano; períodos estatísticos próprios, sem Gêneros da coleção; editor de avatar; vínculo/execução de ROM local pela ficha; filtros de plataforma em Desejos, cards compactos e prévia vazia até chegar a capa. Alfabeticamente, Todas e Não iniciado são os rótulos atuais; Backlog salvo continua compatível.

Moldura integrada e bootstrap UAC implementados, com testes controlados Linux; Windows real/pacote não homologados. Preços console e original individual da API oficial continuam sem capacidade autenticada comprovada: filtro de plataforma não significa consulta multiplataforma pronta. A4 e fechar somente a ROM com emulador aberto permanecem separados e inalterados. Suíte integral final desta versão: 695 passed in 479.02s (0:07:59), exit 0, Linux/Python 3.12.14/Qt offscreen, código congelado em f543166; smokes de seis páginas/cadastro/SQLite aprovados. Plano/relatório/evidências: PLANO_0137.md, RELATORIO_0137.md e RELATORIO_0137_TESTES.md.

As seções seguintes são históricas, inclusive autorizações antigas de lançamento.

## Pré-release 0.1.36 publicada

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.36

Código/tag: 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Workflow https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264: build e publish concluídos com sucesso. **613 passed in 582.04s (0:09:42)** no Windows/Python 3.12.10, zero falhas/erros/skips; Linux: 613 passed in 401.33s. Build, smokes do fonte e do ZIP extraído, atualizador e revisão com 61 capturas aprovados. Oito arquivos publicados baixados e conferidos por tamanho/SHA-256 com os digests do GitHub; CRC dos dois ZIPs válido. ZIP Windows: d2fffc594295ec9cd8800300ce4a7535f60ce76211d63454e0544d276cdfb69a.

A primeira execução atingiu o limite por conflito do atalho entre janelas do renderizador. Correção restrita ao script e regressão; aplicativo, assets, workflows e contratos protegidos preservados. Relatório integral: RELATORIO_LANCAMENTO_0136.md. Esta documentação é posterior ao build e não move a tag. Persistem as limitações 02/03/06, A4 e fechar somente a ROM; captura real, contas e homologação no PC do dono continuam pendentes. Runner Windows não equivale a uso pessoal real.

Registros anteriores abaixo são históricos.

## Retomada do lançamento 0.1.36 — revisão visual

A execução Windows 43742802876 aprovou 612 testes (453,60 s), build e smokes do pacote extraído, mas excedeu 30 minutos na revisão visual. O renderizador ocultava a primeira MainWindow antes de criar outra, mantendo o mesmo atalho global registrado. O aviso modal de conflito bloqueou o runner. Correção restrita ao ciclo de vida em scripts/render_ui_review.py: fechar a janela e o banco antes dos estados vazios; workflows e aplicativo preservados. Regressão executa o renderizador inteiro com adaptador exclusivo controlado: falhou antes e passou depois, incluindo 13 jogos e quatro telas vazias. Resultados integrais e nova publicação em RELATORIO_LANCAMENTO_0136.md; não declarar lançamento antes da confirmação de tag e arquivos.

## Lançamento 0.1.36 autorizado — preparação

O dono autorizou explicitamente lançar a 0.1.36 no GitHub nesta conversa, após a entrega local. A autorização permite enviar fix/0.1.36-ajustes e acionar Windows release para publicar a pré-release, preservando workflows e releases anteriores. Código local validado em da12842e6de663ee4791a6a4010bc622cfed8222, 612 testes Linux; a publicação depende agora dos testes/build/smokes Windows do próprio commit enviado.

Notas públicas atualizadas para a 0.1.36. Itens 02/03/06 continuam com limitações de cobertura da fonte e uso real, sem alegação de homologação no PC do dono. A4 e fechar somente a ROM permanecem separados. Registros anteriores de proibição de publicação descrevem a fase anterior a esta nova autorização. Resultados e links serão registrados em RELATORIO_LANCAMENTO_0136.md.

## Validação final local 0.1.36

Código `da12842e6de663ee4791a6a4010bc622cfed8222`: **612 passed in 428.94s (0:07:08)**, exit 0, Linux/Python 3.12.14, Qt offscreen e dados em /tmp. Sem alterações no código durante a execução. Planos/relatórios/capturas e patches completos na entrega local; nenhum push/PR/tag/release/workflow. Windows real e console na API não comprovados; itens 02, 03 e 06 parciais. A4/ROM descarregada com emulador vivo continuam separados. Últimos ajustes: ficha em Desejos sem aquisição, favorito persistido e visível, status único conforme molde sem anotação.

## Rodada local 0.1.36 — em preparação, sem publicação

Branch local `fix/0.1.36-ajustes`, base remota reconfirmada `818ec80a492a29936782ddb3a43eecaf3ef996e3` de `fix/0.1.35-ajustes`. Versão alvo/declarada 0.1.36, schema 4. Autorização não inclui push, PR, tag, release, troca de assets ou workflow de lançamento; nenhum desses atos foi realizado nesta rodada.

Implementação local: atalho Windows global com associação ao processo em primeiro plano; banner com bloco proporcional à arte inteira ao redimensionar; Início sem descrição sobreposta; Desejos sem tempo, desconto somente de oferta contextual válida e ordenação por desconto; filtros locais em Estatísticas, dados extras visíveis, mapa de calor sem sobra fixa e lista com logo/nome/tempo; cinco tamanhos de capa com espaços iguais; centralização óptica/DPI Steam, asset intacto; títulos de Memórias acessíveis.

**Rodada parcial:** expansão de preços por plataforma/edição (02) sem cobertura autenticada console comprovada; API oficial não documenta original individual (03); captura real e processos-filhos/launchers não homologados (06). Suporte a filhos não confiáveis é recusado. A4 e fechar somente a ROM com emulador vivo continuam separados/bloqueados. Não declarar prontidão Windows ou versão lançada a partir dos testes Linux.

Plano/registro: PLANO_0136.md, RELATORIO_0136.md e RELATORIO_0136_TESTES.md (saídas integrais e resultados atuais). Capturas sintéticas em 1280×800/1920×1080 foram compartilhadas no chat; geometria adicional em escalas Qt 150%/200%. Esses resultados não substituem Windows real nem pacote Windows correspondente. Histórico abaixo é referência, não instrução de publicação.

## Pré-release 0.1.35 publicada

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.35

Código/tag: df5ff41e74b36cea4e2abd160e1172f4166bf32a. Workflow https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335: build e publish concluídos com sucesso; **542 passed in 379.76s**, 0 falhas/erros/skips no Windows Python 3.12.10. Smokes do fonte e do ZIP extraído, auxiliar, cadastro isolado, atualizador e revisão visual passaram. ZIP SHA-256: c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571, igual ao digest publicado pelo GitHub.

Versão 0.1.35, schema 4. Persistem A4, detecção de encerrar apenas a ROM e validação real de captura/contas/emuladores no PC do dono. Não confundir runner Windows com homologação pessoal. tzdata fixado nas dependências de teste para os fusos IANA no Windows; asserções e workflows intactos. Relatório integral: RELATORIO_LANCAMENTO_0135.md. Esta atualização documental é posterior ao commit do build e não muda o aplicativo publicado.

## Lançamento 0.1.35 autorizado pelo dono

Versão declarada atualizada para 0.1.35, schema 4. O dono autorizou o lançamento após o envio da branch fix/0.1.35-ajustes em f0a5514. Publicação de pré-release pelo workflow Windows release, sem alterar os workflows ou as releases protegidas. A publicação depende dos testes Windows, build e smokes do pacote extraído.

Pendências preservadas nas notas públicas: fechar somente a ROM mantendo o emulador aberto ainda pode exigir fim manual do registro; A4 ainda exige escolha/confirmação; captura real de jogos no Windows e homologação no PC do dono não foram validadas. Os 542 testes Linux da entrega anterior não substituem essa homologação. Resultados da execução Windows e arquivos verificados acompanham a release.

Os registros abaixo são históricos e descrevem a entrega antes da autorização de lançamento.

## Trabalho local 0.1.35 — validação Linux, com bloqueio parcial do item 2

Branch fix/0.1.35-ajustes a partir do remoto af1d3ab. Itens 1–22 e complementos visuais/textuais em commits próprios; o item 2 só está resolvido para encerramento do processo. Fechar apenas a ROM mantendo o emulador aberto continua sem sinal validado por perfil. A4 e arquivos protegidos intactos. Não houve push, tag, release, PR ou workflow de publicação.

Código validado em 94fecc1: **542 passed in 353.65s (0:05:53)**, exit 0, Linux Python 3.12.14, QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp. Saída integral final em RELATORIO_0135.md; histórico completo de comandos/reproduções em RELATORIO_0135_TESTES.md. Patches completos e SHA-256 na entrega local. Capturas Qt são fixtures, não validação Windows.

Jogar usa o fluxo da ROM; processo encerrado finaliza registro e atualiza ficha. Cards Desejos até 360 px; total app + snapshot Steam sem duplicação; ações e orientação de Memórias; status editável; ficha exclusiva de desejos; banners contidos; resumo Wikipédia e ausência de texto; preço oficial por padrão com opção keyshops. Atalho configurável para captura por PID e descoberta Steam por VDF/manifests. Tabulação por clique completo; calendário local sem regravar instantes.

Logos de serviços preservadas fora de Lucide. Steam usa steam.ico contido. Aparência com nove prévias e slider à esquerda/exemplos à direita; exclusões de mockup e regra de texto aplicadas em commits adicionais aprovados.

Captura real no Windows não validada; primeiro uso real será no PC do dono. Não declarar detecção de fechamento interno de ROM ou origem exata do registro pessoal de data como validadas. Versão declarada do pacote ainda 0.1.34; schema 4. O projeto completo não está concluído.

## Entrega local 0.1.34 — continuação da branch atual

Partida: 10458eea4b037236e2ae79731f53c06625eaf5b2, mantendo os sete commits noturnos anteriores. Branch única fix/0.1.34-bugs; versão declarada 0.1.34, schema 4. Sem push, tag, release ou PR. **A4 permanece bloqueado:** o cadastro pela aba ROM do Drive continua exigindo escolha de ficha e confirmação. Não declarar a tarefa inteira concluída nem lançar esta branch como se A4 estivesse entregue.

Arquivos da ficha têm busca própria: um clique numa ROM vincula, baixa/verifica e consulta texto/imagens. As entradas da interface substituem o vínculo anterior sem apagar índice, arquivo local ou histórico. O serviço legado save_import permanece congelado; chamadas externas diretas e dados antigos podem conter múltiplas versões. Não foi executada limpeza em massa dos dados existentes.

Texto e origem da ficha, preço preservado, tempos app/Steam separados, clique do menu na borda, alternativa de banner, Lucide ISC e os ajustes de layout foram validados com fontes controladas. Detalhes, mudança de expectativa E3, saídas e limitações em RELATORIO_0134_COMPLETA.md. As 72 capturas são fixtures, não contas reais.


## Correções noturnas — fix/0.1.34-bugs (somente local)

Base: fix/0.1.33-drive em cffbeb3d744fade381ea7573a6602e41d616c5de. Código segue declarando 0.1.33; não houve lançamento ou alteração de versão. Concluídos os itens 1, 2, 3, 5, 7, 8 e 9: estado do Drive após seleção, ficha preenchida, cache de preço, refresh da arte, posição do menu, recorte proporcional de capas e resumo de Wikipédia. Item 4 sem erro reproduzido no mapeamento dos menus; item 6 revertido após falha do teste de coordenadas de imagem; item 10 revertido integralmente após a validação de indicador pequeno continuar falhando. Esses itens não fazem parte da branch final.

Validação final Linux Qt offscreen, dados em /tmp: 379 passed in 425.74s (0:07:05), exit 0. Cada correção mantida passou em teste com dois jogos e no teste de preservação. Só show_missing_metadata mudou em QuickAdd; dialogs.py, lifecycle e o teste de preservação ficaram intactos. O teste antigo de preço passou a exigir preservação de 5900 em vez de None, pois a nova regra exige reter o último valor válido. Nenhum skip/xfail novo. Windows real, DPI, contas e APIs reais não validados. Sem push, tag, release ou PR. Tempo Steam, logos de jogos e os layouts pendentes foram preservados. A nova regra de capas usa recorte central proporcional, prevalecendo sobre a orientação anterior de exibir a capa inteira.

## Trabalho atual — 0.1.33 Drive

Branch `fix/0.1.33-drive`, base `4bdb4ef`. Normalização No-Intro e candidatos na aba Drive; ficha incompleta com cabeçalho. Relatório: [RELATORIO_0133_DRIVE.md](RELATORIO_0133_DRIVE.md). Publicar somente esta branch, sem tag, release ou PR. Lifecycle e fluxos anteriores preservados. **357 passed in 474.59s (0:07:54)**, exit 0, sem falhas/erros/skips/xfails na execução final. Linux Qt offscreen, dados em /tmp.

## Contexto anterior

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

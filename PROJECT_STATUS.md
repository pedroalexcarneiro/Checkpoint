# Estado atual — Checkpoint 0.1.39 publicada

Revisão local em fix/pos-0139-layout, sem nova publicação: Início sem jogos
repetidos, memórias com largura padrão/fundo transparente, nove destaques mais
vivos e modos claro/escuro independentes, topo adaptado. Validação em execução;
percentual ausente na API exige complemento opcional ainda não autorizado/ativado.
Estado do release publicado abaixo; detalhes da revisão em RELATORIO_POS_0139.md.

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.39
Fonte/tag 7703d8048884009a5d9e9addb348620d4a788ff0; workflow 44660106137
aprovado. 764 testes Linux e 764 Windows, zero falhas/erros/skips. Pacote
extraído validado, dez arquivos baixados e hashes/CRC conferidos. ZIP:
dc6132969de8622e64ab4a36afbc0197c8de527a55cd6ad040813d18ddc9f4a3.
0.1.38/0.1.37 e workflows preservados. HSR real/contas/UAC pessoal ainda não
homologados; preços console/saves Drive/fechar só ROM continuam pendentes.
Detalhes atuais no relatório de lançamento; registros anteriores abaixo.

## 0.1.39 — rodada de correções

Complementos implementados: captura de quadro atual e publicação imediata
em Memórias, Estatísticas menor sem sobreposição e degradê aprovado no Início.
A contagem de 752 abaixo corresponde ao fechamento anterior. Novo gate Linux:
764 passed in 487.00s, exit 0, código 03272d0; falta o workflow Windows antes
de confirmar o lançamento autorizado. HSR real permanece não homologado.

Implementação local na branch fix/0.1.39-polimento, da base normal 0.1.38;
lançamento autorizado depois das verificações. Interface revisada por capturas
reais/fixtures e testes direcionados; suíte integral Linux final aprovada: 752 testes em 577,63 s, exit 0.
Pacote Windows ainda será validado pelo workflow; sem homologação do PC do dono.

Entregas: Últimas sessões reais e compactas, Ofertas em linhas, Desejos menores,
Diário consistente, métrica de conclusão com significado explícito, foco de capas,
Preto neutro, abas Emuladores/Lixeira, perfis compatíveis na ficha, restauração
individual e datas ausentes sem invenção, nomes de ROM/saves/rolagem/diálogos.

Pendências importantes: preços console sem oferta autenticada comprovada;
saves têm backup local e não upload Drive. Não declarar projeto inteiro pronto.
A4 e fechar apenas ROM mantêm seus limites; dados/schema 4/cofre/assets
preservados. Somente ImageDialog.__init__ teve exceção protegida autorizada.
Detalhes e validações: RELATORIO_0139.md e DIAGNOSTICO_INTEGRACOES_0139.md.

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

## Rodada 0.1.37 — lançamento autorizado, em validação

Branch fix/0.1.37-ajustes, base 58b0c118. Início integrado, lista da Biblioteca, cache/rolagem assíncrona, gráficos por período, avatar editável e ROM local pela ficha implementados. Complementos posteriores de layout, rótulos, filtro de plataforma em Desejos e rodapé compacto incorporados sem reescrever commits. Versão declarada 0.1.37; schema 4.

Suíte integral final Linux: 695 passed in 479.02s (0:07:59), exit 0, código f543166; rodada anterior de 690 também aprovada. Smokes de seis páginas/cadastro/SQLite aprovados. Moldura e UAC são parciais até teste real do pacote Windows. Preços console e original individual da API oficial permanecem sem cobertura/identidade da fonte comprovadas; filtro visual não resolve essa consulta. A4 protegido, fechamento interno da ROM e captura real/emuladores do dono continuam pendentes. O dono autorizou posteriormente o lançamento após as verificações; publicação depende do workflow Windows e será registrada em RELATORIO_LANCAMENTO_0137.md. Detalhes nos relatórios 0137; registros abaixo são históricos.

## Pré-release 0.1.36 publicada

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.36

Código/tag: 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Workflow https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264: build e publish concluídos com sucesso. **613 passed in 582.04s (0:09:42)** no Windows/Python 3.12.10, zero falhas/erros/skips; Linux: 613 passed in 401.33s. Build, smokes do fonte e do ZIP extraído, atualizador e revisão com 61 capturas aprovados. Oito arquivos publicados baixados e conferidos por tamanho/SHA-256 com os digests do GitHub; CRC dos dois ZIPs válido. ZIP Windows: d2fffc594295ec9cd8800300ce4a7535f60ce76211d63454e0544d276cdfb69a.

A primeira execução atingiu o limite por conflito do atalho entre janelas do renderizador. Correção restrita ao script e regressão; aplicativo, assets, workflows e contratos protegidos preservados. Relatório integral: RELATORIO_LANCAMENTO_0136.md. Esta documentação é posterior ao build e não move a tag. Persistem as limitações 02/03/06, A4 e fechar somente a ROM; captura real, contas e homologação no PC do dono continuam pendentes. Runner Windows não equivale a uso pessoal real.

Registros anteriores abaixo são históricos.

## Retomada do lançamento 0.1.36

Primeira execução Windows 43742802876: 612 testes passaram, build e pacote extraído validados; revisão visual bloqueada por conflito de atalho entre as duas janelas do renderizador, até atingir o limite de 30 minutos. Nenhuma publicação nessa execução. Correção fecha a primeira janela antes da segunda, sem mudar aplicativo, assets ou workflows. Regressão completa do renderizador reproduziu o erro antes e passou depois (7 testes direcionados aprovados). Nova suíte integral e publicação serão registradas em RELATORIO_LANCAMENTO_0136.md. Homologação de jogo real no PC do dono continua pendente.

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

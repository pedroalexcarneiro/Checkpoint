# Validação do Checkpoint

## Rodada atual 0.1.39

Publicação confirmada no código 7703d80, mesma árvore de aplicação/testes/scripts
do gate Linux 03272d0. Workflow 44660106137: **764 passed in 664.04s**, Windows
x64/Python 3.12.10, JUnit com 764 testes/0 falhas/0 erros/0 skips, SHA-256 do
artefato aa7079708a57f208ad85840dfc6d9f85f378fefc310fdfd094dde28c72ffa1fd.
Dois casos nativos de quadros sucessivos aprovados. Executável extraído, fonte,
cadastro/auxiliar/atualizador e abertura normal Qt windows/SQLite aprovados.
Dez arquivos de release baixados, digests e dois ZIPs/CRC conferidos. Registros
integrais Linux/Windows no relatório de testes e no de lançamento.
Não homologa HSR/DirectX/tela cheia, contas, emuladores ou consentimento UAC real.

Complementos C1–C4 posteriores: tests/test_capture_refresh_0139.py valida quadros
distintos, associação a dois jogos, atualização sem navegar, preservação do filtro
e rejeição de alvo mudado. scripts/check_capture_frames.py usa duas janelas
controladas em subprocesso: backend GDI com Qt windows quando executado em
Windows; grab Qt offscreen em Linux, sem equivalência com HSR/DirectX real.
tests/test_statistics_responsive_0139.py verifica nomes, tempos, ocupação do
mapa, legenda e disposição em três tamanhos/restauração. Nenhuma asserção antiga
foi alterada nesses complementos. Os 752 resultados abaixo antecedem C1–C4;
a suíte integral complementar foi aprovada em 03272d0: **764 passed in 487.00s**,
exit 0, Qt offscreen/CHECKPOINT_TEST_ROOT=/tmp. Registro integral no relatório.

Base normal 9dd9c93: 700 testes Linux passaram em 557,77 s antes das mudanças.
Reprodução final dos novos contratos na base isolada: 33 falhas em 4,12 s.
Suíte integral final Linux: **752 passed in 577.63s (0:09:37)**, exit 0,
código/testes congelados em 8dd4c24. Os quatro últimos ajustes foram somente
expectativas de layout expressamente substituídas. Resultado integral registrado
em RELATORIO_0139_TESTES.md com stdout/stderr/exit/comando/ambiente integrais.

Novo renderizador scripts/render_0139_review.py cria banco/arte/tempos/preços
sintéticos isolados e captura app Qt real, incluindo showMaximized/showNormal,
1280×800/1920×1080/1000×700 e DPR 1/1,5/2 em tela virtual apropriada. Manifesto
registra dimensões/estado/escala; não é mockup nem homologação Windows.

Fábricas próprias de diálogos têm testes reais de modais, português, Escape/
cancelamento/padrão, espaçamento e limites. Testes antigos que substituíam Qt
passam a substituir a nova fábrica correspondente, sem alterar asserções de dados.
Única exceção protegida é ImageDialog.__init__, com prefixo byte a byte verificado.
Nenhum skip/xfail novo. Ver relatório para falhas intermediárias e protótipo descartado.

## Publicação 0.1.38

Tag c4a7e1d; Windows release 43857996709: 700 testes em 633,27 s, zero falhas/erros/skips, build/smokes/abertura normal do fonte e executável extraído aprovados. Linux: 700 testes em 483,81 s. Dez arquivos baixados e digests GitHub/CRC verificados. Logs integrais e resultados em RELATORIO_LANCAMENTO_0138.md. O teste usa HWND nativo e executor já elevado; consentimento UAC no PC do dono não é automatizado. Registros anteriores abaixo são históricos.

## Correção de abertura 0.1.38

Candidato ff13658 validado em Windows UI validation 43799707113: 700 passed in 673.05s (0:11:13), zero falhas/erros/skips. Linux: 700 passed in 483.81s (0:08:03). Nova cobertura exige MSG.hWnd sem recriar HWND no callback e duas janelas reais com plugin Qt windows nos testes Windows. Linux usa offscreen e é identificado como tal.

package_windows_release.py preserva os smokes anteriores e acrescenta abertura normal via native_startup_check.py, no fonte e no .exe extraído: executor já elevado, plugin windows, diretório novo, PID/HWND próprios, visibilidade/resposta, captura, WM_CLOSE, exit e SQLite. Não usa --smoke-test nessa cobertura e não automatiza consentimento UAC. Screenshot e JSON nativos acompanham os artefatos. Não equivale à homologação no PC do dono.

Checkout Windows UI validation usa fetch-depth: 0 para disponibilizar c51c245 ao contrato protegido. Primeiro run falhou por histórico raso; ajuste YAML intermediário recusado por chave duplicada foi corrigido antes do run final. Nenhuma asserção protegida modificada. Relatórios 0138 preservam falhas e resultados integrais. Versão ainda sem publicação.

## Resultado publicado 0.1.37

Commit/tag c526cb4bc5e8721dfdfdf20222c8c1c41562ce52: Windows/Python 3.12.10, 695 passed in 638.21s (0:10:38), zero falhas/erros/skips; Linux/Python 3.12.14, 695 passed in 478.98s (0:07:58). Testes/smokes do pacote extraído, auxiliar/cadastro/atualizador e revisão visual passaram no workflow 43793047592. Oito arquivos baixados/conferidos com digests GitHub; CRC dos dois ZIPs válido. Logs completos em RELATORIO_LANCAMENTO_0137.md e RELATORIO_0137_TESTES.md.

Primeiro run 43790327035 foi interrompido por limpeza incorreta no teste dos controles; spy de close corrigido e verificações de liberação acrescentadas. Não usar o run interrompido como aprovação. A repetição aprovada usa o commit novo sem reescrever o histórico. Protegidos e aplicativo não mudaram nessa correção.

Windows runner/pacote aprovados não equivalem a homologar UAC/DWM/Snap/captura/contas/emuladores reais no PC do dono. Esses limites permanecem explícitos. Registros seguintes incluem fases anteriores.

## Rodada local 0.1.37

Suíte integral final: 695 passed in 479.02s (0:07:59), exit 0, código f543166037e545aad99c6aef21bf6ed95fe4bb10. Comando: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp /workspace/work/venv/bin/python -m pytest tests -q -p no:cacheprovider. Resultados integrais, comandos, ambiente e códigos de saída em RELATORIO_0137_TESTES.md; contagens abaixo são históricas. Código permaneceu congelado durante a suíte; só documentação/notas foram alteradas em paralelo.

Cobertura nova: execuções reais versus alterações de status/falhas, resumo semanal e limites locais, carrosséis/ações, lista e favorito, consultas em volume/cache/arte assíncrona com leitura lenta sem bloquear eventos, gráficos por período e DST, avatar/orientação/cancelamento, dois programas CHIP-8 próprios com executor controlado e fechamento de processo, filtro de plataformas e rodapé, carregamento sem corte, moldura/UAC controlados. Nenhum teste desses equivale a homologação de contas ou emuladores reais.

scripts/render_0137_review.py gera capturas Qt reais com fixtures identificadas em 1280×800/1920×1080/1000×700: Início, lista, grade, Desejos, períodos, Aparência 70/150, Conexões, Perfil, origem/ROM vinculada e carregamento. Espera conclusão da arte antes da captura. Linux offscreen/DPR 1; revisões em outras escalas serão registradas separadamente. Windows, DWM/Snap/UAC reais, captura elevada e pacote não validados. Schema 4 e arquivos protegidos preservados.

## Validação final local 0.1.36

Código `da12842e6de663ee4791a6a4010bc622cfed8222`: **612 passed in 428.94s (0:07:08)**, exit 0, Linux/Python 3.12.14, Qt offscreen e dados em /tmp. Sem alterações no código durante a execução. Planos/relatórios/capturas e patches completos na entrega local; nenhum push/PR/tag/release/workflow. Windows real e console na API não comprovados; itens 02, 03 e 06 parciais. A4/ROM descarregada com emulador vivo continuam separados. Últimos ajustes: ficha em Desejos sem aquisição, favorito persistido e visível, status único conforme molde sem anotação.

## Rodada 0.1.36

Comando integral: `QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp python -m pytest tests -q -p no:cacheprovider`. Ambiente desta rodada: Linux/Python 3.12.14. `RELATORIO_0136_TESTES.md` contém stdout, stderr e exit integrais, incluindo falhas antes das correções. Resultado final será registrado no relatório da rodada; os 542 testes Windows publicados anteriormente não são resultado 0.1.36.

Novos contratos: hotkey transacional e associação segura por PID; banner proporcional, quatro bordas e estados de janela; preços oficiais/contexto/sem oferta e desconto real; períodos locais, limites/DST de 23/25h e Steam sem datas; cinco capas e margens iguais; DPI 150%/200% em geometria/raster; preservação de histórico/posse e textos externos. Tests autenticados e Windows real não executados. Nenhum skip/xfail criado; arquivos protegidos intactos.

Screenshots de revisão usam cadastro isolado e arte pública Steam; preços/tempos são fixtures identificadas na comunicação. Não são capturas obtidas de um jogo por hotkey real. Nenhum vídeo pessoal, banco, token ou arquivo de ROM faz parte da entrega versionada.

Use Python 3.12 e as dependências de requirements-tested.txt. Não é necessário instalar dependências adicionais nesta revisão.

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-smoke-novo
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-cadastro-novo
QT_QPA_PLATFORM=offscreen .venv/bin/python scripts/render_ui_review.py /tmp/checkpoint-revisao-nova --reference-sizes
```

Use pastas novas, fora dos dados pessoais. A conclusão atual começou com 271 testes passando no estado recebido da branch. O trabalho anterior e a correção de ciclo de vida do Drive foram preservados. Consulte RELATORIO_CORRECOES.md para resultados completos por etapa e repetições com faulthandler.

A cobertura inclui migração de dados/cofre e preferências, nove temas/contraste, layout, cards/colunas, 500 jogos com roda do mouse, preços atuais/históricos da API, moeda/nulos, segredo fora de erros/logs, cofre, atribuição, ordenação, busca gravada, nomes de ROM, estados vazios e ciclo de vida com jobs ativos. Integrações de testes usam fixtures; isso não valida contas reais nem autenticação/transporte real da API oficial GG.deals. Capturas são Qt offscreen em Linux; o diálogo é composto com grabs Qt da janela e do modal. Não é captura do desktop Windows. Evidências de versões anteriores são históricas.

## Revisão visual 0.1.32

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python scripts/render_ui_review.py /tmp/checkpoint-visual-novo --visual-review
```

Gera 72 capturas e manifesto com dados controlados, sem consultas externas. Copiar somente PNGs e manifesto para evidence; o banco e o cache são temporários. Consulte RELATORIO_0132_VISUAL.md para resultados e limites.

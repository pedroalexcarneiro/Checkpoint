# Validação do Checkpoint

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

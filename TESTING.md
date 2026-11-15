# Validação do Checkpoint

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

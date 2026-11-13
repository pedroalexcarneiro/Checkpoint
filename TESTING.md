# Validação do Checkpoint

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

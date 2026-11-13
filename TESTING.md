# Validação da 0.1.28

## Executar

```bash
QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests -q -p no:cacheprovider
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-smoke-novo
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-cadastro-novo
QT_QPA_PLATFORM=offscreen .venv/bin/python scripts/render_ui_review.py /tmp/checkpoint-revisao-nova
```

Instale o projeto editável conforme SETUP.md antes de executar scripts. Use sempre pastas novas/isoladas; o smoke recusa banco existente. CHECKPOINT_TEST_ROOT permite colocar as fixtures fora do checkout. Nunca usar LOCALAPPDATA real para testes.

## Cobertura e evidências

Estado inicial: 225 testes passaram antes de alterações. Migração inclui origem em WAL, backup/integridade, primeira abertura, destino existente, corrupção, travas, falha do cofre, credencial fictícia em memória e normalização de preferências. Testes de tema verificam exatamente nove paletas e contraste; testes de layout e regressão verificam menu, quatro colunas, dimensões de Desejos, banner, execução, Conexões e estados do cadastro.

Resultado final: 252 testes passaram em Linux (273,37 s) e em Windows CI (174,51 s). No runner Windows também passaram build, smokes e capturas. Resultados por etapa, comandos, artefatos e limitações estão em RELATORIO_CORRECOES.md. Capturas são Qt real com fixtures declaradas, não acesso autenticado nem execução Windows. Testes controlados não garantem DPI, hardware ou contas reais. Os arquivos evidence anteriores são registros históricos, não resultados desta revisão.

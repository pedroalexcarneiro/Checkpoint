# Continuidade do Checkpoint

Base desta revisão: código-fonte 0.1.27 da branch `codex/design-fidelity-pt-br`. Trabalho 0.1.28 em `fix/rename-redesign-0.1.28`; não usar a main defasada.

Leia `PROJECT_STATUS.md`, `RELATORIO_CORRECOES.md` e `ARCHITECTURE.md`. O histórico está no CHANGELOG; não reintroduzir exigências antigas de formato ou temas removidos.

Preservar o wordmark checkpo//nt e o ícone de identidade. Referências visuais do dono prevalecem sobre o código: capas verticais, quatro colunas, banner/continuidade, ficha com galeria e Conexões 2×2. Não fundir os componentes de cadastro sem a decisão registrada no relatório.

Validação local:

```bash
QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests -q -p no:cacheprovider
QT_QPA_PLATFORM=offscreen .venv/bin/python scripts/render_ui_review.py /tmp/revisao-checkpoint-nova
```

Use sempre diretórios isolados e novos para smoke. Não leia credenciais, altere releases antigas ou recrie dados do usuário. A migração mantém a origem e não muda o schema 4.

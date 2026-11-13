# Checkpoint

Biblioteca pessoal de jogos para Windows, em português do Brasil. Código-fonte atual: **0.1.28**, Python 3.12, PySide6 e SQLite (schema 4). Esta revisão não publica release.

A Biblioteca usa quatro colunas de capas verticais. Início reúne o jogo atual, continuidade e atividade pessoal; a ficha reúne banner, execução, informações e galeria. Desejos mostra artes contidas e ofertas disponíveis.

Os nove temas são Azul, Verde (padrão), Amarelo, Vermelho, Preto, Roxo, Rosa, Laranja e Ciano. Identidade: wordmark **checkpo//nt** e ícone próprio.

Os dados ficam em `%LOCALAPPDATA%\Checkpoint`; na primeira abertura elegível, a pasta anterior é copiada com verificação do banco e a origem é preservada. Credenciais permanecem no cofre do Windows.

## Executar

```powershell
python -m pip install -r requirements-tested.txt
python -m pip install --no-deps --no-build-isolation -e .
python run_checkpoint.py
```

Consulte [SETUP.md](SETUP.md) para build e dados, [INTEGRATIONS.md](INTEGRATIONS.md) para serviços, [TESTING.md](TESTING.md) para validação e [RELATORIO_CORRECOES.md](RELATORIO_CORRECOES.md) para a revisão atual.

Jogos Steam, ROMs e executáveis locais compartilham a Biblioteca. Uma seleção no catálogo permite buscar ficha e imagens automaticamente; resultados dependem dos provedores, das credenciais configuradas e da disponibilidade de arte. Downloads Drive são somente sob demanda; nenhum arquivo remoto é excluído.

# Checkpoint

Biblioteca pessoal de jogos para Windows, em português do Brasil. Código-fonte atual: **0.1.32**, Python 3.12, PySide6 e SQLite (schema 4). A [pré-release 0.1.32](https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.32) está disponível com ZIP portátil Windows x64, após 344 testes Windows e validação do executável extraído. Código na branch `fix/0.1.32-visual`.

A Biblioteca tem capas verticais e tamanho ajustável entre 70% e 150%, com seis colunas no padrão em janela larga. Desejos tem arte 1:1, logos contidas, preços atuais e menores históricos quando disponíveis. A ordenação padrão é Nome A–Z, com alternativa por menor preço atual. Início reúne jogos em andamento e atividade pessoal; a ficha reúne banner, execução, informações e galeria.

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

GG.deals usa a [API oficial](https://gg.deals/api/prices/) quando há chave configurada em Conexões, salva apenas no cofre do Windows. Sem chave, a página pública pode ser usada conforme a preferência. Histórico não é preço original; a API não fornece porcentagem de desconto. Toda tela de preços apresenta atribuição ativa ao GG.deals.

Cadastro pelo Drive: o nome limpo da ROM é pesquisado no catálogo; textos vêm de RAWG/Steam e artes salvas vêm do SteamGridDB. O arquivo é somente vinculado, sem download automático. Fichas incompletas mostram um aviso e a ação Pesquisar manualmente. Provas e limitações: [RELATORIO_0130_DRIVE.md](RELATORIO_0130_DRIVE.md).

Revisão visual: [relatório 0.1.32](RELATORIO_0132_VISUAL.md), com 72 capturas Verde/Rosa em duas resoluções, limites de validação e preservação do cadastro Drive.

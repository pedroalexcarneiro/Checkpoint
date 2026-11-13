# Relatório de conclusão — Checkpoint 0.1.29

Revisão em 13/11/2026 15:36 UTC. Base histórica solicitada: `8d39c18`. Estado recebido: branch `fix/0.1.29`, commit `f0be1b9`, árvore limpa, dez commits anteriores e versão 0.1.29 no módulo e no pyproject. A branch foi continuada sem recriação, reset, rebase ou remoção de trabalho. Os dez commits recebidos permanecem ancestrais da entrega.

Esta conclusão acrescenta commits locais; não houve push, tag, release, PR ou build de release. Main e branches codex não foram alteradas. A remoção da pré-release v0.1.28 continua sendo ação do dono. Documentos locais de release não foram publicados como descrições no GitHub.

## O que já existia e foi preservado

O estado recebido já implementava tamanho das capas 70–150%, seis colunas no padrão largo, conversão da densidade, Início por andamento, scroll de 180 ms, arte 1:1 dos desejos, busca com ficha/origem, limpeza de ROM, estados vazios e proteção do ciclo de vida dos diálogos. A suíte inicial confirmou 271 testes passando. Esses recursos foram mantidos e novamente exercitados pelas suítes completas; não foram reescritos por conveniência.

Wordmark checkpo//nt, ícone da base e nove temas foram preservados. A migração de diretório, snapshot SQLite, integridade, travas e credenciais anteriores continua intacta. O schema permanece 4. Nenhuma pasta pessoal ou cofre real foi aberto para testes. Não foram necessárias dependências novas.

## Preços oficiais e decisões registradas

Fontes consultadas: [GG.deals API](https://gg.deals/api/) e [Prices API](https://gg.deals/api/prices/). O endpoint implementado é `https://api.gg.deals/v1/prices/by-steam-app-id/`, com IDs de `external_identifiers`/`steam` e região BR. O parâmetro de autenticação é obtido do cofre somente em memória; não entra no banco, argumentos de subprocesso, arquivos de pedido ou relatório.

- Com chave acessível, usa API oficial. Sem chave, usa página pública apenas se a opção `prices.public_fallback` estiver ativa. Essa opção é verdadeira por padrão, preservando o comportamento público anterior. Falha com uma chave presente não provoca fallback silencioso: conserva o último valor válido.
- Consulta automática exige ID Steam, inclusive no fallback; sem ID, informa “Sem ID da Steam para consulta” e mantém Ver ofertas. Escolhi não consultar por título para evitar associar preços a outra edição.
- O menor entre `currentRetail` e `currentKeyshops` é exibido com Loja oficial ou Keyshop. Empate favorece loja oficial. Somente BRL é aceito; não há conversão. Nulo e zero não são oferta utilizável.
- `historicalRetail`/`historicalKeyshops` fornecem “Menor histórico”. Não são preço de lista: a API sempre retorna original/desconto ausentes. Também há proteção na interface contra cache de outra moeda.
- A página pública permanece disponível e pode mostrar original/percentual apenas com `price-old` explícito na mesma oferta. Histórico nunca é usado para calcular desconto.
- Nome A–Z é o padrão; Menor preço atual ordena valores positivos em ordem crescente, sem preço no fim. A preferência antiga de maior desconto é convertida para Nome A–Z, sem mexer em outros dados. Atualizar preços conserva a rolagem.
- Toda página que mostra preços tem “Preços: GG.deals”, com link ativo para https://gg.deals/. URLs recebidas não têm afiliados/referrals alterados.
- A documentação declara plano gratuito para uso pessoal, hobby e open source, com atribuição. A fila existente consulta um jogo por vez em intervalos de 6,5 s, com cache de uma hora. HTTP 429 e demais erros geram mensagens fixas sem URL/corpo autenticado. O transporte não segue redirecionamentos autenticados.

## Conexões e cofre

O pedido enumera cinco serviços em uma grade 2×2. Para conservar o desenho aprovado, mantive os quatro cards originais em 2×2 e coloquei GG.deals abaixo, ocupando a largura disponível. Isso mantém a chave e Salvar/Remover legíveis em 1280 px.

O campo GG.deals é mascarado, nunca recebe a chave armazenada e é limpo após salvar ou falhar. Salvar/Remover opera apenas no cofre; presença configurada tem ponto verde e ausência tem ponto cinza. Exceções do backend são substituídas por mensagens fixas. Alterar a configuração permite uma nova consulta de preços, sem apagar o último valor válido ou mudar o schema.

Os testes usam marcadores transitórios gerados em memória, sem chave literal em fixture ou arquivo. Conferem a ausência do valor no cache, nas mensagens e nos logs. Nenhuma captura contém campo de chave preenchido. A guarda do cofre nativo Windows ainda depende de validação no computador real.

## SIGSEGV

A correção funcional já estava nos dez commits recebidos: a versão antiga só aguardava consultas quando `quick.owner is self`; sob DriveDialog, o owner era outra janela. O diálogo podia concluir com jobs ativos. A implementação recebida preserva o diálogo/receptor até `finished`, também com pai, e aguarda detalhes selecionados antes de salvar.

Não alterei `tests/test_save_lifecycle.py`, não introduzi skip/xfail e não alterei a correção de ciclo de vida para liberar a versão. O baseline atual passou. Confirmei novamente o caso Drive isolado, cinco vezes com `-X faulthandler`:

- Execução 1: 1 passed in 15.45s
- Execução 2: 1 passed in 15.56s
- Execução 3: 1 passed in 14.72s
- Execução 4: 1 passed in 14.68s
- Execução 5: 1 passed in 15.67s

Não houve SIGSEGV nem nova pilha de falha. A suíte final também inclui o caso original. Isso valida o caminho corrigido em Qt offscreen Linux; não identifica uma instrução C++ nem comprova Windows/DPI/hardware do usuário.

## Testes e comandos reais

Ambiente existente: Python 3.12.14, PySide6 6.8.3. A suíte foi rodada antes de qualquer alteração e após cada etapa. Pastas das fixtures ficam em /tmp.

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 \
.venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

| Etapa | Resultado |
|---|---|
| Estado recebido, antes de alterar | 271 passed in 319.65s (0:05:19) |
| Provedor oficial | 287 passed in 311.64s (0:05:11) |
| Conexões e cofre | 290 passed in 323.44s (0:05:23) |
| Desejos, histórico, ordenação e atribuição | 293 passed in 346.41s (0:05:46) |
| Revisão final, incluindo proteção do cache em outra moeda | 294 passed in 586.18s (0:09:46) |

Cobertura nova: JSON com preços atuais/históricos distintos, nulos, moeda incompatível, campo ausente e valores inválidos; parâmetros do endpoint; HTTP 429 e erros sem segredo; seleção API/fallback e ausência de ID Steam; cofre mascarado/limpo e fora do SQLite; atribuição ativa; novas ordenações e conservação da rolagem. A cobertura anterior de 500 jogos, nove temas, migração, busca gravada, ROM, desejos já possuídos e estados vazios continua na suíte.

Testes dirigidos: API e regressões de preço, 25 passaram; cofre/conexões e regressões visuais, 31 passaram; exibição/ordenação/layout, 18 passaram na preparação final. Uma iteração da cópia de preparação teve 2 falhas/16 sucessos por remover inadvertidamente o helper de invalidação do cache; foi corrigida antes do commit e da suíte da etapa. A proteção final de moeda teve 4 testes dirigidos passando.

Comando do caso isolado, repetido cinco vezes:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 \
.venv/bin/python -X faulthandler -m pytest 'tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[drive]' -q -p no:cacheprovider
```

Smokes em dados novos:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-029-official-smoke
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-029-official-save-smoke
```

```text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK
```

Logs desta execução: `/tmp/checkpoint-029-official-*.log`. O resumo durável fica em `evidence/validation-0.1.29.txt`.

## Capturas

Geradas com o script solicitado no checkout, sem conta/chave real:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python scripts/render_ui_review.py /tmp/checkpoint-029-official-final-review --reference-sizes
```

São 16 PNGs: seis telas nas duas resoluções, Aparência adicional e ficha do desejo com preços. Dados, preços e artes são fixtures locais declaradas. O exemplo passa pelo parser oficial, mas não demonstra resposta de conta autenticada. No modo offscreen, Adicionar jogo é composição dos grabs Qt reais da janela e do diálogo, sem captura do desktop. Somente PNGs e a descrição foram copiados para o repositório; nenhum banco ou log privado.

| Caminho | Dimensão | Bytes |
|---|---|---:|
| [1280x800-add.png](evidence/ui-0.1.29/1280x800-add.png) | 1280×800 | 117088 |
| [1280x800-appearance.png](evidence/ui-0.1.29/1280x800-appearance.png) | 1280×800 | 56633 |
| [1280x800-detail.png](evidence/ui-0.1.29/1280x800-detail.png) | 1280×800 | 114374 |
| [1280x800-home.png](evidence/ui-0.1.29/1280x800-home.png) | 1280×800 | 165978 |
| [1280x800-library.png](evidence/ui-0.1.29/1280x800-library.png) | 1280×800 | 221150 |
| [1280x800-settings.png](evidence/ui-0.1.29/1280x800-settings.png) | 1280×800 | 86643 |
| [1280x800-wish-prices.png](evidence/ui-0.1.29/1280x800-wish-prices.png) | 1280×800 | 124287 |
| [1280x800-wishlist.png](evidence/ui-0.1.29/1280x800-wishlist.png) | 1280×800 | 86942 |
| [1920x1080-add.png](evidence/ui-0.1.29/1920x1080-add.png) | 1920×1080 | 170742 |
| [1920x1080-appearance.png](evidence/ui-0.1.29/1920x1080-appearance.png) | 1920×1080 | 67614 |
| [1920x1080-detail.png](evidence/ui-0.1.29/1920x1080-detail.png) | 1920×1080 | 132637 |
| [1920x1080-home.png](evidence/ui-0.1.29/1920x1080-home.png) | 1920×1080 | 182846 |
| [1920x1080-library.png](evidence/ui-0.1.29/1920x1080-library.png) | 1920×1080 | 230954 |
| [1920x1080-settings.png](evidence/ui-0.1.29/1920x1080-settings.png) | 1920×1080 | 99626 |
| [1920x1080-wish-prices.png](evidence/ui-0.1.29/1920x1080-wish-prices.png) | 1920×1080 | 150363 |
| [1920x1080-wishlist.png](evidence/ui-0.1.29/1920x1080-wishlist.png) | 1920×1080 | 99162 |

Comparação com as referências:

- Início mantém banner/CTA, continuidade vertical e atividade à direita, sem abas da Biblioteca; cabe em 1280 px.
- Biblioteca mantém cabeçalho, filtros, seleção e capas verticais; seis colunas no padrão largo seguem a decisão atual, em vez das quatro antigas.
- Desejos mantém áreas 1:1 uniformes, logos contidas e ações alinhadas; agora apresenta histórico, atribuição, Nome A–Z e mensagens sem ID. Capas/título são alternativas quando falta logo.
- Ficha mantém banner, voltar, barra de execução, abas e galeria. A captura sem executável mostra Configurar execução secundário. A imagem adicional da ficha de desejo mostra o painel de preços e a atribuição.
- Adicionar mantém fechamento único, pesquisa, três fontes, resultado/check, link de troca e automação. Os testes conservam plataforma legível e seleção obrigatória.
- Conexões conserva quatro cards 2×2 e acrescenta GG.deals abaixo. Aparência conserva nove temas e o slider.

Diferenças restantes: artes, logos dos jogos e conteúdo são fixtures; fontes/renderização são as do Linux. SteamGridDB e RAWG continuam com identificadores SG/R. A ficha exibe metadados adicionais; a ajuda de Conexões permanece em linha própria. O quinto card é um desvio necessário pela quantidade de serviços. Não se afirma igualdade pixel a pixel com fotografias nem validação visual Windows/DPI.

## Arquivo por arquivo, desde a base histórica

A lista inclui o trabalho recebido, preservado, e a conclusão atual. O diff específico desta conclusão parte de `f0be1b9`.

- `.github/release-notes.md` — Atualiza apenas o documento local; não altera nem publica uma release no GitHub.
- `AGENTS.md` — Distingue a arte dos Desejos das capas da Biblioteca.
- `CHANGELOG.md` — Atualiza a entrada 0.1.29 com a conclusão da API e a mudança da ordenação/histórico.
- `CLOUD_SETUP.md` — Registra acesso à documentação por ferramenta web e limites de rede do executor.
- `CONTINUITY.md` — Preserva a base e as regras de ciclo de vida; registra API implementada e proibição atual de push/publicação.
- `DESIGN.md` — Área de arte 1:1, preços atuais/históricos e quinto card de conexão.
- `INTEGRATIONS.md` — Documentação oficial, plano gratuito, parâmetros, quotas, atribuição, cofre e limite do desconto.
- `PRODUCT_VISION.md` — Remove formato antigo rígido e alinha Biblioteca vertical/Desejos 1:1.
- `PROJECT_STATUS.md` — Estado implementado e pendências reais; sem hashes, IDs de workflow ou nomes de branch.
- `README.md` — Estado atual da versão, preços/históricos, cofre, fallback e atribuição.
- `RELATORIO_CORRECOES.md` — Consolida o trabalho recebido e esta conclusão, com resultados reais e diferenças visuais.
- `ROADMAP.md` — Retira documentação oficial como bloqueio; mantém validação autenticada, revisão Windows e decisões do dono.
- `SETUP.md` — Instalação, execução, build e dados; preferência sem mudança de schema.
- `TESTING.md` — Comandos, baseline atual e cobertura da API/cofre/atribuição.
- `checkpoint/__init__.py` — Versão 0.1.29.
- `checkpoint/auto_artwork.py` — Conclusão das imagens em linguagem simples, sem totais de tipos indisponíveis.
- `checkpoint/card_layout.py` — Métrica única de colunas/tamanho/espaçamento e conversão da preferência de densidade.
- `checkpoint/collection_views.py` — Preserva arte 1:1/ações/scroll; adiciona atribuição, ordenações novas e espaço para preço/histórico/ausência de ID.
- `checkpoint/cover_grid.py` — Capas verticais, tamanho responsivo e rolagem por pixel.
- `checkpoint/data_migration.py` — Identificador de paleta legada centralizado; mesma conversão, sem alterar schema, backup ou origem.
- `checkpoint/design_system.py` — Áreas de rolagem suave e referência à área criada para restaurar posição.
- `checkpoint/dialogs.py` — Conclusão aguarda jobs em qualquer hierarquia; origem Busca e plataforma da ROM.
- `checkpoint/enrichment.py` — Mensagem de ficha preenchida e orientação de falha, sem relatório técnico de totais.
- `checkpoint/game_import.py` — Metadados selecionados completam o novo cadastro na mesma transação, com origem correta.
- `checkpoint/ggdeals_connection.py` — Novo card com campo mascarado, Salvar/Remover apenas no cofre, limpeza da entrada e estado verde/cinza.
- `checkpoint/home_view.py` — Seleção por andamento/recência, ausência de arte aleatória e composição que cabe em 1280 px.
- `checkpoint/integrations/drive.py` — Limpeza conservadora de extensão, tags e plataforma; preserva original_name.
- `checkpoint/integrations/ggdeals.py` — Preço original da oferta, desconto calculado e rejeição de preço zero.
- `checkpoint/integrations/ggdeals_api.py` — Novo parser oficial, transporte HTTPS sem redirecionamento autenticado, BRL, nulos, menor atual/histórico separados e erros fixos sem segredo.
- `checkpoint/integrations/price_provider.py` — Contrato com histórico/tipo de oferta e reexportação do provedor oficial implementado.
- `checkpoint/price_queue.py` — Fila sem jogos sem ID Steam; falhas registram apenas mensagem fixa e versão de configuração.
- `checkpoint/price_view.py` — Atribuição ativa, histórico sem desconto, tipo do menor preço, mensagem sem Steam e proteção contra moeda de cache incompatível.
- `checkpoint/prices.py` — Seleção API/fallback, ausência de ID Steam, cache, revisão da configuração e ordenação por nome ou menor preço.
- `checkpoint/quick_add.py` — Estados de consulta/conclusão, detalhes aguardados, fechamento único e simplificação das opções visíveis.
- `checkpoint/settings_view.py` — Preserva slider e quatro cards existentes; acrescenta GG.deals abaixo e opção de fallback em Avançado.
- `checkpoint/smooth_scroll.py` — Animação de 180 ms sobre a barra vertical e tratamento por pixel.
- `checkpoint/statistics_view.py` — Uso da área de rolagem animada.
- `checkpoint/theme.py` — Mantém nove temas e acabamento anterior; aplica a superfície comum ao card GG.deals.
- `checkpoint/ui_components.py` — Recalcula a área do banner para manter o botão dentro dela ao redimensionar.
- `checkpoint/window.py` — Mantém as correções anteriores; acrescenta status GG.deals e injeção do cofre para testes controlados.
- `checkpoint/window_style.py` — Barra própria do diálogo, fechamento e arraste.
- `evidence/checkpoint-015-validation.txt` — Troca do nome da paleta descontinuada por descrição genérica; números e marcação histórica preservados.
- `evidence/validation-0.1.29.txt` — Resultados reais desta conclusão, com baseline, etapas, caso Drive e smokes.
- `pyproject.toml` — Versão 0.1.29; dependências e schema mantidos.
- `scripts/LEIA-ME.txt` — Instruções simples de GG.deals no cofre, ordenação e diferença entre histórico e desconto.
- `scripts/render_ui_review.py` — Capturas com preços fictícios processados pelo parser oficial, campo de chave vazio e ficha de desejo adicional.
- `tests/test_add_dialog_0129.py` — Fechamento único, plataforma legível, seleção e opções visíveis.
- `tests/test_card_layout.py` — Colunas, migração da densidade, persistência, mesma fórmula e ações legíveis em 70%.
- `tests/test_complete_layout.py` — Atualiza expectativa antiga de colunas para o comportamento responsivo.
- `tests/test_data_migration.py` — Mantém teste de conversão da preferência usando a constante de compatibilidade.
- `tests/test_enrichment.py` — Mensagens novas e metadados já preenchidos na importação.
- `tests/test_ggdeals_api.py` — JSON documentado com BRL/nulos/campos ausentes/valores inválidos, parâmetros, erros sem segredo, fallback e preservação do cache.
- `tests/test_ggdeals_connection.py` — Cofre em memória, entrada mascarada/limpa, Salvar/Remover, estados, ausência de segredo no banco/log/texto e reconsulta após configuração.
- `tests/test_home_0129.py` — Andamento/recência, ausência de abas, estado vazio, largura e botão dentro do banner.
- `tests/test_price_display_official.py` — Histórico sem percentual, moeda incompatível não exibida em reais, ordenação, atribuição e fila sem Steam.
- `tests/test_prices_0129.py` — Preserva o teste público com original explícito e atualiza testes para API sem chave, Nome A–Z e menor preço atual.
- `tests/test_quick_add.py` — Regressão de diálogo aninhado com job pendente e estado de conclusão.
- `tests/test_registration_0128.py` — CTAs de abas/filtros e biblioteca vazia, sem regressão de desejos já possuídos.
- `tests/test_revision_0128.py` — Arte 1:1 dos desejos e colunas responsivas, preservando limites dos cards.
- `tests/test_rom_titles_0129.py` — Cinco nomes típicos e preservação do original/plataforma no índice.
- `tests/test_search_save_0129.py` — Salvar durante detalhes pendentes e conferir desenvolvedora, editora, descrição e origem no SQLite.
- `tests/test_smooth_scroll.py` — Roda com 500 jogos, pixel/animação e áreas das demais telas.
- `tests/test_ui_redesign.py` — Atualiza a contagem de estados configurados para as cinco conexões.
- `evidence/ui-0.1.29/*.png` — cada captura individual está listada na tabela acima; as anteriores continuam no histórico do Git.
- `evidence/ui-0.1.29/review-info.json` — ambiente, fixtures, chave ausente e composição do diálogo.

`SETUP.md` foi revisado e mantido: já contém somente instalação, execução, build e dados. Módulo/pyproject já estavam em 0.1.29 e foram mantidos. Não se criou migração de schema.

## Limitações e pendências do dono

A documentação foi acessada pela ferramenta web. O cliente HTTP do executor retornou URLError e os hosts GG.deals não constam na política aplicada. Não houve chamada real autenticada à API, nem teste com conta/chave real. Não foram validados Windows real, DPI, cofre nativo, contas Steam/Drive/RAWG/SteamGridDB/GG.deals ou bloqueios reais da página pública.

As decisões conservadoras foram: conservar os dez commits anteriores; manter a branch e versão; fallback público configurável sem fallback silencioso com chave; consulta automática apenas com Steam; preço histórico separado; Nome A–Z como padrão; quinto card abaixo dos quatro; nenhuma fusão dos três componentes de cadastro; commits somente locais, sem publicação.

Dependem do dono: configurar a chave no aplicativo Windows e validar acesso real; remover a pré-release v0.1.28 publicada por engano; decidir sobre futura fonte que forneça preço original se quiser percentuais pela API. Histórico não será usado como desconto. A revisão de estética/DPI permanece humana. Não foi gerado pacote Windows.

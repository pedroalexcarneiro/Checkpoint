# Relatório de correções — Checkpoint 0.1.29

Revisão em 13/11/2026 11:49 -03. Base confirmada: `fix/rename-redesign-0.1.28`, commit `8d39c18`, versão 0.1.28 nos dois arquivos. Branch de entrega: `fix/0.1.29`. A árvore estava limpa antes das alterações. A versão final é 0.1.29 no módulo e no pyproject.

## Escopo e preservação

Schema 4 mantido. A migração de diretório, snapshot SQLite por backup, integridade, travas, cofre e origem foram preservados. Nenhum dado pessoal foi aberto para testes. Nenhuma dependência nova foi instalada: ambiente existente com Python 3.12.14 e PySide6 6.8.3.

Não houve build de release, tag, edição/remoção de release, PR ou force push. Main e branches codex não foram alteradas. O texto `.github/release-notes.md` é um documento local atualizado, não uma publicação. A pré-release v0.1.28 publicada por engano permanece sob responsabilidade do dono.

## SIGSEGV: causa funcional e correção

A suíte completa inicial passou, mas o caso Drive isolado retornou -11 na base. Portanto, o resultado da suíte em conjunto não foi tomado como prova de ausência da queda.

A proteção de `GameDialog.finish_or_wait()` só esperava as consultas quando `quick.owner is self`. No fluxo Drive, o owner era a janela principal; `apply_catalog()` seguido de `validate()` podia concluir o diálogo com uma busca ainda em execução. O faulthandler mostrou a queda na thread principal, antes do encerramento programado da janela, enquanto havia Jobs em `worker.run_isolated` e `DriveDialog.queue_artwork`.

Trechos do traceback reproduzido na base:

```text
Current thread:
  File "<string>", line 45 in check
  File "<string>", line 67 in <module>

Thread de trabalho:
  File "checkpoint/worker.py", line 31 in run_isolated
  File "<string>", line 22 in isolated
  File "checkpoint/drive_dialog.py", line 154 in <lambda>
  File "checkpoint/drive_dialog.py", line 76 in work
  File "checkpoint/jobs.py", line 10 in run
```

A correção está em `checkpoint/dialogs.py:102` e `checkpoint/quick_add.py:205`: o diálogo aguarda seus Jobs independentemente do pai, mantendo receptor/widgets vivos até `finished`. Cancelar descarta respostas; salvar aguarda os detalhes selecionados e só então conclui. Buscas pendentes não substituem uma escolha durante esse encerramento. A thread principal continua processando eventos; não há `wait()` bloqueante no fluxo da interface.

O novo teste de diálogo aninhado mantém um job bloqueado e verifica que o diálogo permanece aberto até sua conclusão. O teste original `tests/test_save_lifecycle.py` não foi alterado, removido, pulado ou marcado como xfail. Após a correção inicial: 5/5 execuções isoladas passaram. Após a correção completa de cadastro: mais 5/5 passaram com `-X faulthandler`, sem SIGSEGV, em 17,81 s, 17,65 s, 16,94 s, 17,06 s e 18,42 s. O fluxo também integra todas as suítes completas posteriores.

O diagnóstico confirma o caminho funcional de encerramento prematuro e a regressão corrigida; não identifica uma instrução C++ específica. Não foi feita validação equivalente no Windows real.

## Ficha da busca

Ao selecionar, a consulta de detalhes ainda podia estar ativa. O salvamento encerrava o diálogo e a resposta posterior era descartada; a origem continuava no valor inicial Manual. Agora o aceite aguarda detalhes, `apply_catalog` registra Busca e `save_import` completa dados selecionados dentro da transação. O teste salva durante uma consulta pendente e confere os três dados e a origem no banco. ROMs mantêm Google Drive como origem e seu nome original no índice.

## Decisões sem confirmação

- Priorizei a queda nativa antes do desenho, pois o pedido proíbe encobrir a falha.
- Densidade compacta vira 80%; confortável vira 100%. A preferência antiga permanece gravada e um tamanho já existente tem precedência.
- Um único cálculo atende às duas grades; o padrão largo tem seis colunas e janelas menores reduzem. Em 70%, ações de Desejos usam duas linhas para preservar texto e ícones, sem zoom global.
- Arte dos Desejos é 1:1: logo contida, capa recortada ao centro ou título. A Biblioteca preserva a capa vertical inteira. Não foi criado seletor de formato.
- Automação continua ativa por padrão. A caixa local foi retirada da interface; seu controle interno é mantido para compatibilidade, respeitando a preferência global anterior de automação.
- Limpeza de ROM remove apenas tags reconhecidas de região/versão, extensões e plataforma explícita; parênteses que podem fazer parte do título permanecem. A regra de plataforma da pasta tem precedência sobre a indicação do arquivo.
- Provedor público GG.deals permanece em uso. A classe de API só reconhece presença de configuração injetada no cofre e retorna indisponibilidade enquanto faltar documentação. Não há endpoint presumido, transporte real nem credencial em arquivo/teste.
- Os três componentes de cadastro foram mantidos. Não foi executada uma fusão não solicitada.
- A partir das etapas finais, validei cópias imutáveis em /tmp, com PYTHONPATH explícito e bancos isolados. Os arquivos de aplicativo/testes no checkout foram comparados byte a byte com a cópia final. Os tempos abaixo incluem concorrência entre suítes e não medem desempenho do aplicativo.

## Testes reais

Comando da suíte, executado antes das mudanças e após cada etapa:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 \
  .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

Nas cópias, o executável foi `/workspace/Checkpoint/.venv/bin/python`, com `PYTHONPATH=/tmp/checkpoint-029-stageN` e cwd da mesma cópia. A base inicial usou `/tmp/checkpoint-029-baseline.oPaXCM` como raiz de dados. Logs desta execução ficam em `/tmp/checkpoint-029-*.log`; o resumo durável está em `evidence/validation-0.1.29.txt`.

| Etapa | Resumo real |
|---|---|
| Base, antes de qualquer alteração | 252 passed in 216.36s (0:03:36) |
| Ciclo de vida do Drive | 253 passed in 223.42s (0:03:43) |
| Tamanho — iteração intermediária | 2 failed, 253 passed in 234.42s (0:03:54) |
| Tamanho — fechamento | 255 passed in 241.47s (0:04:01) |
| Início | 257 passed in 250.39s (0:04:10) |
| Rolagem | 258 passed in 950.10s (0:15:50) |
| Desejos e preços | 261 passed in 1092.91s (0:18:12) |
| Ficha da busca | 262 passed in 1131.58s (0:18:51) |
| Diálogo e ROM | 269 passed in 1236.45s (0:20:36) |
| Estados vazios | 269 passed in 1112.42s (0:18:32) |
| Documentação e acabamento inicial | 271 passed in 896.00s (0:14:56) |
| Acabamento dos cards em 70% — final | 271 passed in 570.80s (0:09:30) |

As duas falhas intermediárias de tamanho correspondiam ao encaixe exato da última coluna no Qt e a uma expectativa antiga de quatro colunas em janela estreita. Foram corrigidas antes do fechamento. Testes de contratos antigos foram atualizados para a ficha já preenchida na importação e o estado de salvamento pendente. Na revisão visual, um teste novo de identidade de item foi corrigido para verificar somente o ajuste do slider: navegar até a Biblioteca normalmente recria seus itens.

O teste de rolagem usa 500 jogos, roda do mouse, animação de 180 ms e verifica progresso por pixel sem travar o loop. O parser é testado com e sem preço original e não fabrica desconto. A API é testada com objetos em memória, sem valor de chave. Migração, nove temas/contraste, estados vazios e proteção de jogos já possuídos continuam na suíte.

Smokes repetidos no checkout final, com pastas novas e Qt offscreen:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-029-root-smoke
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-029-root-save-smoke
```

Saídas reais:

```text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK
```

## Capturas e comparação

Geradas por `scripts/render_ui_review.py --reference-sizes`, em `/tmp/checkpoint-029-evidence-complete`, com cópias somente dos PNGs e da descrição da revisão em `evidence/ui-0.1.29/`. Nenhum banco, imagem pessoal, log privado ou arquivo de credencial foi incluído. São 14 capturas: seis telas em duas resoluções, mais Aparência nas duas.

```bash
QT_QPA_PLATFORM=offscreen python scripts/render_ui_review.py /tmp/revisao-nova --reference-sizes
```

Os dados, preços e artes são fixtures declaradas; não demonstram integrações autenticadas. No modo offscreen, a imagem de Adicionar jogo compõe grabs Qt reais da janela e do diálogo na posição correspondente; não é captura do desktop Windows.

| Arquivo | Dimensão | Bytes |
|---|---|---:|
| [1280x800-add.png](evidence/ui-0.1.29/1280x800-add.png) | 1280×800 | 117088 |
| [1280x800-appearance.png](evidence/ui-0.1.29/1280x800-appearance.png) | 1280×800 | 56633 |
| [1280x800-detail.png](evidence/ui-0.1.29/1280x800-detail.png) | 1280×800 | 114374 |
| [1280x800-home.png](evidence/ui-0.1.29/1280x800-home.png) | 1280×800 | 165978 |
| [1280x800-library.png](evidence/ui-0.1.29/1280x800-library.png) | 1280×800 | 221150 |
| [1280x800-settings.png](evidence/ui-0.1.29/1280x800-settings.png) | 1280×800 | 74332 |
| [1280x800-wishlist.png](evidence/ui-0.1.29/1280x800-wishlist.png) | 1280×800 | 83399 |
| [1920x1080-add.png](evidence/ui-0.1.29/1920x1080-add.png) | 1920×1080 | 170742 |
| [1920x1080-appearance.png](evidence/ui-0.1.29/1920x1080-appearance.png) | 1920×1080 | 67614 |
| [1920x1080-detail.png](evidence/ui-0.1.29/1920x1080-detail.png) | 1920×1080 | 132637 |
| [1920x1080-home.png](evidence/ui-0.1.29/1920x1080-home.png) | 1920×1080 | 182846 |
| [1920x1080-library.png](evidence/ui-0.1.29/1920x1080-library.png) | 1920×1080 | 230954 |
| [1920x1080-settings.png](evidence/ui-0.1.29/1920x1080-settings.png) | 1920×1080 | 86933 |
| [1920x1080-wishlist.png](evidence/ui-0.1.29/1920x1080-wishlist.png) | 1920×1080 | 94628 |

Comparação visual feita com as referências fornecidas:

- Início: banner, texto curto, Continuar jogando, quatro jogos em andamento e atividade à direita; sem abas da Biblioteca. Botão permanece dentro do banner em ambas as resoluções.
- Biblioteca: capas verticais, título/status, busca, adição, visualização, abas e filtros. Seis colunas no padrão largo substituem as quatro da referência por decisão explícita desta versão.
- Desejos: cinco jogos de teste em cards uniformes, arte 1:1, preço/indisponibilidade, desconto e ações. A nova proporção prevalece sobre a foto antiga.
- Ficha: banner, voltar, barra de execução/status/tempo/menu, abas e galeria. A captura usa Configurar execução secundário porque a fixture não tem executável, conforme a exceção solicitada.
- Adicionar: uma barra própria, um fechamento, três fontes, seleção/check, Escolher outro resultado, informação de automação, avançado e ações. A plataforma expandida é coberta por teste de largura/altura.
- Conexões: quatro cards 2×2, estados verdes/cinzas e botões; as presenças configuradas das capturas são simuladas, sem autenticação. Aparência mostra nove temas e o slider.

Diferenças restantes: artes/logos de jogos e textos são fixtures, não os arquivos das imagens aprovadas; a tipografia/renderização é a disponível no Linux. SteamGridDB e RAWG mantêm identificadores gráficos SG/R em vez das marcas completas. A ficha conserva metadados adicionais de gênero, lançamento, publicadora e origem; a referência os resume. A ajuda de Conexões fica em linha própria acima dos cards. Margens e espaço livre variam com a largura e a quantidade de dados; não se afirma igualdade pixel a pixel com as fotografias. Capas reais de proporções diferentes são preservadas inteiras, sem fundo desfocado. A revisão final de estética e DPI no Windows continua humana.

## Arquivos alterados

- `.github/release-notes.md` — Texto local atualizado; nenhuma descrição de release existente foi editada no GitHub.
- `AGENTS.md` — Distingue a arte dos Desejos das capas da Biblioteca.
- `CHANGELOG.md` — Entrada da revisão e histórico identificado como histórico.
- `CLOUD_SETUP.md` — Branch de trabalho atual e dados isolados.
- `CONTINUITY.md` — Base, continuidade, regras de encerramento e restrição de publicação.
- `DESIGN.md` — Decisões atuais de tamanho, colunas e arte dos desejos.
- `INTEGRATIONS.md` — Provedor público versus estrutura de API; cobertura e limites.
- `PRODUCT_VISION.md` — Remove formato antigo rígido e alinha Biblioteca vertical/Desejos 1:1.
- `PROJECT_STATUS.md` — Estado atual, pendências e limitações, sem hashes/IDs/branches.
- `README.md` — Versão, funcionalidades e ausência de nova release.
- `ROADMAP.md` — Pendências do dono e validação Windows.
- `SETUP.md` — Instalação, execução, build e dados; preferência sem mudança de schema.
- `TESTING.md` — Comandos e cobertura atuais, isolamento e limites das capturas.
- `checkpoint/__init__.py` — Versão 0.1.29.
- `checkpoint/auto_artwork.py` — Conclusão das imagens em linguagem simples, sem totais de tipos indisponíveis.
- `checkpoint/card_layout.py` — Métrica única de colunas/tamanho/espaçamento e conversão da preferência de densidade.
- `checkpoint/collection_views.py` — Arte 1:1, alternativas de capa/título, descontos, ordenação, restauração da rolagem e ações adaptáveis nos cards pequenos.
- `checkpoint/cover_grid.py` — Capas verticais, tamanho responsivo e rolagem por pixel.
- `checkpoint/data_migration.py` — Identificador de paleta legada centralizado; mesma conversão, sem alterar schema, backup ou origem.
- `checkpoint/design_system.py` — Áreas de rolagem suave e referência à área criada para restaurar posição.
- `checkpoint/dialogs.py` — Conclusão aguarda jobs em qualquer hierarquia; origem Busca e plataforma da ROM.
- `checkpoint/enrichment.py` — Mensagem de ficha preenchida e orientação de falha, sem relatório técnico de totais.
- `checkpoint/game_import.py` — Metadados selecionados completam o novo cadastro na mesma transação, com origem correta.
- `checkpoint/home_view.py` — Seleção por andamento/recência, ausência de arte aleatória e composição que cabe em 1280 px.
- `checkpoint/integrations/drive.py` — Limpeza conservadora de extensão, tags e plataforma; preserva original_name.
- `checkpoint/integrations/ggdeals.py` — Preço original da oferta, desconto calculado e rejeição de preço zero.
- `checkpoint/integrations/price_provider.py` — Contrato de preços e implementação separada da API, sem transporte real.
- `checkpoint/price_view.py` — Preço atual, original riscado, desconto e indisponibilidade legível.
- `checkpoint/prices.py` — Validação de BRL/valor positivo, último valor válido e ordenação dos desejos.
- `checkpoint/quick_add.py` — Estados de consulta/conclusão, detalhes aguardados, fechamento único e simplificação das opções visíveis.
- `checkpoint/settings_view.py` — Slider 70–150%, padrão 100%, no lugar da densidade.
- `checkpoint/smooth_scroll.py` — Animação de 180 ms sobre a barra vertical e tratamento por pixel.
- `checkpoint/statistics_view.py` — Uso da área de rolagem animada.
- `checkpoint/theme.py` — Barras temáticas, slider e selo de desconto; nove paletas preservadas.
- `checkpoint/ui_components.py` — Recalcula a área do banner para manter o botão dentro dela ao redimensionar.
- `checkpoint/window.py` — Atualiza tamanho sem reconstruir os itens, preserva a página no refresh e distingue estados vazios.
- `checkpoint/window_style.py` — Barra própria do diálogo, fechamento e arraste.
- `evidence/checkpoint-015-validation.txt` — Troca do nome da paleta descontinuada por descrição genérica; números e marcação histórica preservados.
- `pyproject.toml` — Versão 0.1.29; dependências e schema mantidos.
- `scripts/LEIA-ME.txt` — Orientação simples para a revisão atual, dados, cadastro e tamanho das capas.
- `scripts/render_ui_review.py` — Matriz das seis telas em duas resoluções, Aparência adicional e composição declarada do diálogo.
- `tests/test_add_dialog_0129.py` — Fechamento único, plataforma legível, seleção e opções visíveis.
- `tests/test_card_layout.py` — Colunas, migração da densidade, persistência, mesma fórmula e ações legíveis em 70%.
- `tests/test_complete_layout.py` — Atualiza expectativa antiga de colunas para o comportamento responsivo.
- `tests/test_data_migration.py` — Mantém teste de conversão da preferência usando a constante de compatibilidade.
- `tests/test_enrichment.py` — Mensagens novas e metadados já preenchidos na importação.
- `tests/test_home_0129.py` — Andamento/recência, ausência de abas, estado vazio, largura e botão dentro do banner.
- `tests/test_prices_0129.py` — Preço original/desconto, ausência de original, zero, API sem transporte, ordenação e rolagem.
- `tests/test_quick_add.py` — Regressão de diálogo aninhado com job pendente e estado de conclusão.
- `tests/test_registration_0128.py` — CTAs de abas/filtros e biblioteca vazia, sem regressão de desejos já possuídos.
- `tests/test_revision_0128.py` — Arte 1:1 dos desejos e colunas responsivas, preservando limites dos cards.
- `tests/test_rom_titles_0129.py` — Cinco nomes típicos e preservação do original/plataforma no índice.
- `tests/test_search_save_0129.py` — Salvar durante detalhes pendentes e conferir desenvolvedora, editora, descrição e origem no SQLite.
- `tests/test_smooth_scroll.py` — Roda com 500 jogos, pixel/animação e áreas das demais telas.
- `tests/test_ui_redesign.py` — Controle de tamanho substitui a expectativa antiga de densidade.
- `RELATORIO_CORRECOES.md` — relatório desta revisão, substituindo o relatório atual anterior; o histórico permanece no Git e no CHANGELOG.
- `evidence/ui-0.1.29/*.png` — 14 capturas listadas acima, uma por caminho.
- `evidence/ui-0.1.29/review-info.json` — ambiente, resoluções e natureza das fixtures/composição.
- `evidence/validation-0.1.29.txt` — resumos reais de validação.

## Auditoria e limitações

Busca case-insensitive pelo identificador anterior: zero ocorrências fora do CHANGELOG; as menções históricas no CHANGELOG foram preservadas. Não há paleta descontinuada no seletor, swatches ou catálogo de temas. Seu valor legado só é reconhecido na fronteira de migração e no teste correspondente. O schema continua 4. A identidade checkpo//nt e os arquivos do ícone da base não foram substituídos.

Não foram lidas ou expostas credenciais reais. Nenhuma chave foi criada ou registrada em arquivos, logs ou testes novos. Não foram validados Windows real, DPI, cofre nativo real, contas de Steam/Drive/RAWG/SteamGridDB, bloqueios reais de GG.deals, nem API oficial autenticada. Não foi gerado executável Windows nesta revisão.

Pendências do dono: documentação oficial e chave própria para a futura API GG.deals; remoção da pré-release v0.1.28 publicada por engano; revisão visual e validação em Windows real. A futura unificação dos componentes de cadastro permanece uma decisão separada.

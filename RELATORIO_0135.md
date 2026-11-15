# RELATORIO_0135 — entrega local

Branch: `fix/0.1.35-ajustes`. Base remota reconfirmada, sem mudança: `af1d3ab56492cba56b541ddb971759d9c15b015b` de `fix/0.1.34-bugs`. Conta conectada `pedroalexcarneiro`, com escrita/admin. Releases v0.1.28, v0.1.33 e v0.1.34 confirmadas e preservadas.

**O conjunto não está integralmente concluído:** item 2 permanece bloqueado no fechamento apenas da ROM com o emulador aberto. O encerramento do processo foi corrigido. Por essa condição, não houve push. Nenhuma tag, release, PR ou workflow de publicação foi criado/disparado. A4 continua fora de escopo.

Os itens originalmente aprovados receberam um commit por item. O item 16 aguardou autorização de expectativas enquanto os independentes avançaram. Reforços locais de teste foram consolidados antes da instrução de preservar commits; depois dessa instrução, todos os ajustes entraram em commits novos, sem reescrever os anteriores.

## Itens, arquivos, funções e status

### 1 — feito

Commit: `2b43ea87886207c97397b92881c844f4c7ebbcd2`.

Arquivos: `checkpoint/detail_view.py`, `checkpoint/window.py`, `tests/test_launch_0135.py`.

Funções: window.MainWindow.start_game; detail_view.build_detail.

Jogar encaminha ROM disponível ao mesmo fluxo de Executar versão; ROM ausente não vira execução avulsa do emulador.

### 2 — bloqueado

Commit: `5c582f2a0fe32310db49e2fd4a7c7958b1fae9d3`.

Arquivos: `checkpoint/window.py`, `tests/test_launch_0135.py`, `tests/test_sessions_0135.py`.

Funções: window.MainWindow.launch_rom/poll_sessions.

Parcial: encerramento do processo remove a sessão e atualiza a ficha. Fechar só a ROM mantendo o emulador aberto continua sem sinal validado. Esse subcaso permanece bloqueado.

### 3 — feito

Commit: `89c137b675043d3a4d6510e69f2a48da1b6066fd`.

Arquivos: `checkpoint/collection_views.py`, `tests/test_layout_0134.py`, `tests/test_wishes_0135.py`.

Funções: collection_views.WishGrid.reflow.

Teto 360 px, arte 1:1 e aumento de colunas sem limite artificial de quatro.

### 4 — feito

Commit: `1d866017946cb774d0b304bb8582efe621df0ae7`.

Arquivos: `checkpoint/activity_heatmap.py`, `checkpoint/collection_views.py`, `checkpoint/detail_view.py`, `checkpoint/home_view.py`, `checkpoint/playtime.py`, `checkpoint/statistics_view.py`, `checkpoint/ui_components.py`, `tests/test_registration_0128.py`, `tests/test_steam.py`, `tests/test_time_0135.py`, `tests/test_time_prices_0134.py`.

Funções: playtime.format_time/total_seconds/collection_times; detail_view.build_detail; statistics_view.build_statistics; collection_views.build_wishlist; home_view.in_progress; ui_components.GameTile.paintEvent; activity_heatmap.set_values/paintEvent/mouseMoveEvent.

Total app + um snapshot Steam por jogo; sessões locais agregadas uma vez, sem multiplicação por join/contas. Formato único 4h00min. Calendário e médias de sessões usam registros locais; snapshots Steam não fornecem datas de sessões.

### 5 — feito

Commit: `2f7032c354760b753268150402092713996cb13a`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/window.py`, `tests/test_memories_0135.py`.

Funções: window.MainWindow.first_memory; collection_views.build_memories.

Estado vazio orienta captura/anotação e Biblioteca abre a escolha do jogo seguida da aba Memórias.

### 6 — feito

Commit: `d7e171407f798131e3dc25b15ad4c5804390b67e`.

Arquivos: `checkpoint/collection_views.py`, `tests/test_memories_0135.py`.

Funções: collection_views.memory_card.

Mesma altura mínima e estrutura de título nos cards de texto/captura.

### 7 — feito

Commit: `4888201b4e5f759d6318f466e74b1e034d44a7a2`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/window.py`, `tests/test_memories_0135.py`.

Funções: window.MainWindow.delete_memory; collection_views.memory_card.

Confirmação; cancelar preserva dados; exclusão restrita ao registro do jogo. Arquivo original importado é preservado.

### 8 — feito

Commit: `7b5798d24eeb6748755c6ef799c8e11efdbaeaec`.

Arquivos: `checkpoint/detail_view.py`, `checkpoint/statistics_view.py`, `tests/test_status_0135.py`.

Funções: detail_view.build_detail/change_status; statistics_view.StatusRing.__init__.

Cinco estados editáveis e persistidos; Início reflete Jogando/Pausado; Não iniciado é apresentado como Backlog.

### 9 — feito

Commit: `278692b653c3dc95315f9e87240077e8dea8d62e`.

Arquivos: `checkpoint/settings_view.py`, `tests/test_settings_0135.py`.

Funções: settings_view.build_settings.

Primeiro ajuste de largura e destaque do controle; complementado pelo commit 9 adicional, sem reescrever este.

### 10 — feito

Commit: `677e852d14c69a3a6ca95b06768af15c0368c420`.

Arquivos: `checkpoint/ggdeals_connection.py`, `checkpoint/settings_view.py`, `tests/test_settings_0135.py`.

Funções: settings_view.build_settings; ggdeals_connection.GgDealsConnection.__init__.

Uma ação principal por conexão, botões padronizados; checkboxes do tema e rótulo GG.deals preservados.

### 11 — feito

Commit: `872b33279e0ed4233a6211480d2174a6656c8001`.

Arquivos: `checkpoint/settings_view.py`, `tests/test_settings_0135.py`.

Funções: settings_view.build_settings.

Criar backup principal; secundárias à esquerda junto do texto.

### 12 — feito

Commit: `59b8f995fe1dbf991ab2d1172a9c2b11ca07f990`.

Arquivos: `checkpoint/detail_view.py`, `tests/test_detail_0135.py`.

Funções: detail_view.build_detail.

Exclusivos de Desejos ficam com visão geral e Adicionar à biblioteca; aquisição restaura a ficha da biblioteca.

### 13 — feito

Commit: `14392949df8e759d29ad1fd435ada09019327d88`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/ui_components.py`, `tests/test_banner_0135.py`, `tests/test_banner_render_0135.py`.

Funções: ui_components.Hero.paintEvent; collection_views.WishLogo.__init__.

Imagem contida, sem expandir/recortar; banner também é alternativa em Desejos. Prova por bordas em renderização real Qt.

### 14 — feito

Commit: `981910d1889f5f07308d42adbaa315c15a702973`.

Arquivos: `checkpoint/wiki_text.py`, `tests/test_wiki_0135.py`.

Funções: wiki_text.intro.

Remove parênteses, inclusive japoneses/aninhados, datas e contexto editorial somente na apresentação.

### 15 — feito

Commit: `414b8d0341f39b11413bc2f6b33bdd6586b13192`.

Arquivos: `checkpoint/detail_view.py`, `tests/test_detail_0135.py`.

Funções: detail_view.build_detail.

Sobre o jogo permanece com ausência explícita e pesquisa/edição; texto final foi encurtado pela regra de texto.

### 17 — feito

Commit: `e68f9c78adfede37d0236b56aa14cf197806ef92`.

Arquivos: `checkpoint/game_capture.py`, `checkpoint/settings_view.py`, `checkpoint/window.py`, `tests/test_capture_0135.py`.

Funções: game_capture.WindowsCapture.capture/capture_game; window.MainWindow.__init__/set_capture_shortcut/capture_game_window; settings_view.build_settings.

Atalho configurável, somente com Checkpoint ativo; PNG vinculado ao jogo iniciado. Windows real não validado; primeiro uso real será no PC do dono.

### 18 — feito

Commit: `4b0ce3eb1de2d88c8517d19a119a6fdafec7d307`.

Arquivos: `checkpoint/game_editor.py`, `checkpoint/steam_installations.py`, `checkpoint/window.py`, `tests/test_steam_installations_0135.py`.

Funções: steam_installations.read_vdf/steam_roots/find_executables; game_editor.add_steam_detection; window.MainWindow.edit_game.

Lê raiz Steam no registro, libraryfolders.vdf e manifests; filtra executáveis no installdir correto. Ambiguidade exige escolha.

### 19 — feito

Commit: `09b1047b4dbf8dd4b01bdc3806da1edc0565ccf1`.

Arquivos: `checkpoint/ui_components.py`, `tests/test_tabs_0135.py`.

Funções: ui_components.ClickTabBar; CurrentPageTabs.__init__.

Reproduzido mousePress selecionando aba antes de concluir arrasto. Seleção passa ao clique completo; teclado preservado e roda não troca abas.

### 20 — feito

Commit: `643c66e2af82efab98ed7a71b701a3a0e8912c26`.

Arquivos: `checkpoint/activity_heatmap.py`, `checkpoint/library.py`, `checkpoint/locale.py`, `checkpoint/statistics_view.py`, `tests/test_dates_0135.py`, `tests/test_wishlist_prices.py`.

Funções: library.Library.stats; statistics_view.build_statistics; activity_heatmap.ActivityHeatmap.__init__/interval; locale.datetime_display.

Converte agrupamento/apresentação para fuso local, sem UPDATE nos instantes. Origem específica do registro do PC do dono não foi acessada; causa UTC−3 demonstrada em banco isolado.

### 16 — feito

Commit: `d4623212ed4f4f2ba7ffec223704d7642166b816`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/price_view.py`, `checkpoint/prices.py`, `tests/test_bugs_0134.py`, `tests/test_price_display_official.py`, `tests/test_prices_0129.py`, `tests/test_prices_0135.py`, `tests/test_time_prices_0134.py`.

Funções: prices.selected_quote/wishlist_order; price_view.display_snapshot/price_summary; collection_views.build_wishlist/include_keyshops.

Loja oficial por padrão; opção keyshops persistida, ordenação coerente e cache sem origem não apresentado como oficial. Sem preço original/desconto na interface.

### 21 — feito

Commit: `3b776d862e815a4627a40830cd50877befbf237f`.

Arquivos: `checkpoint/ui_components.py`, `tests/test_service_logo_0135.py`.

Funções: ui_components.service_icon.

Arquivo steam.ico mostrado e confirmado antes da alteração. Escala contida 32 px em quadrado de 48 px, comparada ao Drive; arquivo original intacto.

### 22 — feito

Commit: `117f362d0a8b66c53910a36b54b8688875d00f7a`.

Arquivos: `checkpoint/ui_components.py`, `tests/test_service_branding_0135.py`.

Funções: ui_components.service_icon (documentação); teste de exclusão de Lucide.

Feito por verificação: logos já eram independentes de Lucide. Teste passa antes/depois; não foi inventado defeito.

### 9 adicional — feito

Commit: `335d5375d7d6d7448bb950fb06344d9e3254d1fa`.

Arquivos: `checkpoint/detail_view.py`, `checkpoint/settings_previews.py`, `checkpoint/settings_view.py`, `checkpoint/window.py`, `tests/test_settings_space_0135.py`.

Funções: settings_previews.ThemePreview/CoverSizePreview; settings_view.build_settings; window.MainWindow.navigate; detail_view.build_detail.

Correção adicional expressamente autorizada após 22: largura útil, nove prévias funcionais e card de capas destacado. Cabeçalho preservado pelo complemento de exclusões.

### Visual A — feito

Commit: `8dddbc3cec3bfe8660c56afc841911aeba4a9e83`.

Arquivos: `checkpoint/prices.py`, `tests/test_visual_complements_0135.py`.

Funções: prices.selected_quote.

Referência Desejos/Vale das Marés: Sem preço salvo e motivo real; consulta sem oferta oficial não é tratada como nunca consultada.

### Visual B — feito

Commit: `3281c286bbb9696ed17593f00fe1b1254df123e1`.

Arquivos: `checkpoint/ui_components.py`, `tests/test_visual_steam_asset_0135.py`.

Funções: ui_components.service_icon (documentação); teste de pixels da marca.

Referência Conexões/ST: feito por verificação, prova de pixels do steam.ico, sem substituir a marca por iniciais.

### Visual C — feito

Commit: `0c8b119625aec169a06eef8b18a2cb7076fe2526`.

Arquivos: `checkpoint/detail_view.py`, `tests/test_visual_status_0135.py`.

Funções: detail_view.build_detail/highlight_status/change_status.

Referência Ficha/Jogando: menu completo com atual em negrito; nenhuma regravação automática do legado Não iniciado.

### Exclusões do mockup — feito

Commit: `1d67c155cbf5274911b83b08ec1d154af9dbb554`.

Arquivos: `checkpoint/settings_view.py`, `checkpoint/window.py`, `tests/test_mockup_exclusions_0135.py`.

Funções: settings_view.build_settings; window.MainWindow.__init__/navigate.

Não entram números/círculos, título extra, rodapé e nome de tema duplicado. Cards selecionam o tema; cabeçalho mantém os limites anteriores.

### Prévia de capas (9) — feito

Commit: `f5df459eea328f4746da22c9e3c6c102ee2b0391`.

Arquivos: `checkpoint/settings_previews.py`, `tests/test_cover_preview_0135.py`.

Funções: settings_previews.CoverSizePreview.active_index/cover_rects/paintEvent.

Slider à esquerda e três exemplos à direita na mesma linha, base comum, verde no valor correspondente e percentual junto ao slider. Testes 70%/150% em 1280×800 e 1920×1080, sem overflow.

### Regra de texto — feito

Commit: `a2e7f605afb07122676e67b050bee9f2f0421657`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/design_system.py`, `checkpoint/detail_view.py`, `checkpoint/ggdeals_connection.py`, `checkpoint/home_view.py`, `checkpoint/settings_previews.py`, `checkpoint/settings_view.py`, `checkpoint/statistics_view.py`, `checkpoint/window.py`, `tests/test_interface_text_0135.py`.

Funções: settings_view.build_settings; ggdeals_connection.__init__; home_view.activity/game_strip/build_home; window.update_library_empty; detail_view.build_detail; collection_views.build_wishlist; statistics_view.build_statistics; design_system.ActionCard.__init__; settings_previews.CoverSizePreview.paintEvent.

Remoção de apoio/tutorial/vibe nas sete telas; dados externos, notas, erros e estados vazios acionáveis preservados. Lista integral abaixo.

### Texto — estados vazios — feito

Commit: `94fecc1b4bb7426503c9f492d119c353c9c68dc1`.

Arquivos: `checkpoint/collection_views.py`, `checkpoint/home_view.py`, `checkpoint/window.py`, `tests/test_empty_copy_0135.py`.

Funções: home_view.build_home; window.MainWindow.update_library_empty; collection_views.build_wishlist.

Estado vazio identifica o destino da ação (biblioteca/desejos). Preserva o contrato existente de descrição informativa, sem mudar o teste protegido nem adicionar frase decorativa.

## Autorizações específicas de expectativas

- Item 3/E3: test_wishes_fill_columns_with_square_art passou de preenchimento integral a teto 360 px, preservando arte quadrada, largura e colunas. Motivo: a regra antiga contradizia o teto e as colunas adicionais. Autorização explícita do dono.
- Item 4: test_app_and_steam_times_are_separate foi substituído por soma em um número só. Teste novo com duas sessões e duas contas verifica 4h00min, sem duplicação. As expectativas textuais de test_steam.py::test_dialog_async_query_selection_import_achievements_and_account_change e test_registration_0128.py::test_activity_summary_uses_singular_day_and_brazilian_date foram alteradas somente de 2.0 h/1,0 h para 2h00min/1h00min, após autorização específica; valores, data e singular/plural preservados.
- Item 16: autorizadas a retirada das expectativas de desconto/preço original de test_prices_0129.py::test_wishlist_name_price_sort_and_scroll_survive_refresh e a classificação explícita das fixtures de preço nesse teste, em test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence, test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price e test_price_display_official.py::test_price_order_places_missing_prices_last_and_respects_name. Preservadas as verificações de valores/cache; nova cobertura recusa cache sem origem.
- Item 20: autorizada a fixture de sessão atravessando meia-noite local e comparação do calendário com agrupamento local em test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips. Mantidos 1800+1800 segundos, 365 células e preservação dos instantes UTC.

Nenhuma outra asserção antiga foi alterada. Sem skip, xfail, exclusão de teste ou contorno de contrato.

## Item 20 — origem e conversão mostradas antes da correção

Prova em banco isolado; não é o banco pessoal do dono. Em play_sessions, linhas id=1/game_id=1 (Zelda: A Link to the Past) e id=2/game_id=2 (Metroid Fusion):

```text
started_at = 2026-11-15T00:30:00+00:00
ended_at = 2026-11-15T00:40:00+00:00
duration_seconds = 600
state = finished
```

Fuso bruto: UTC, explícito no offset +00:00. library.now() grava datetime.now(timezone.utc).isoformat(). Cada início convertido para America/Sao_Paulo é 2026-11-14T21:30:00-03:00. Antes da correção, Library.stats() agrupava em UTC e enviava `{'2026-11-15': 1200.0}` ao ActivityHeatmap. O motivo e essa cadeia foram mostrados no chat antes da proposta de conversão local. A interface passou a solicitar agrupamento local e usar o dia local; o contrato UTC padrão do serviço foi preservado. Não foram regravados, apagados ou recuados registros. A origem exata do registro no PC continua não confirmada.

## Complementos visuais

As imagens de Configurações, Ficha, Desejos, Memórias, Início e índice são guia de layout/hierarquia, não dados do aplicativo. Jogos, preços, datas e arte de exemplo não foram copiados para dados pessoais.

- A — imagem Desejos, card Vale das Marés; itens 3/16: Sem preço salvo em destaque. Motivos distintos para consulta sem oferta oficial, cache sem origem e falta de ID Steam. Loja oficial é o padrão.
- B — imagem Conexões com ST; item 21: ST é apenas mockup. O app mantém o arquivo checkpoint/assets/services/steam.ico, mostrado ao dono e confirmado antes da mudança de escala. Comparação de área com Google Drive e prova dos pixels da marca original.
- C — imagem Ficha com Jogando; item 8: Backlog, Jogando, Pausado, Concluído e Abandonado, com atual destacado. Não iniciado é apresentado como Backlog sem alteração automática do banco.
- Configurações/Aparência; item 9: prévias dos nove temas e card de tamanho proporcional. Slider à esquerda, exemplos à direita, base comum, tamanho crescente, destaque verde que acompanha 70%/100%/150% e percentual junto do slider; Menores/Maiores são rótulos do controle. Nos valores intermediários, o exemplo mais próximo fica destacado. Testados 70% e 150% nas duas resoluções solicitadas, em dois jogos.
- Ficha e Início; itens 4/8: total em XhXXmin e estado do jogo controlável. Memórias; item 5: ausência orienta abrir o jogo e adicionar captura/anotação, com acesso à aba correta.

### Elementos de mockup não implementados

| Elemento | Referência visual e item | Tratamento |
|---|---|---|
| Números e círculos de anotação | Ficha e Configurações; itens 4, 8 e 9 | Não adicionados. |
| Título Checkpoint acima das telas/índice | Índice e telas enviadas; itens 3, 5, 9 e 21 | Cabeçalho e wordmark existentes preservados; nenhum cabeçalho de estudo copiado. |
| Rodapé Biblioteca pessoal | Menu lateral das referências; itens 3, 5, 9 e 21 | Não adicionado. |
| Verde avulso no canto do card de tema | Configurações/Aparência; item 9 | Sem nome duplicado no canto. A seleção funciona nos cards; nome aparece uma vez por card. |

## Ajuste de texto — frases removidas por tela

Configurações:

- O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.
- Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.
- Serviços para completar fichas, imagens e arquivos.
- Seu banco de jogos e suas preferências.
- Cópias de segurança dos saves configurados.
- Consulte as versões disponíveis sem alterar sua biblioteca.
- Jogos removidos poderão ser restaurados aqui.
- API oficial · valores em reais; histórico não é preço original.
- Capa, como legenda decorativa dentro dos desenhos de prévia.

O aviso acionado por Ajuda foi encurtado de “Configurado indica uma credencial salva. Use Gerenciar para verificar o acesso.” para “Credencial salva não confirma acesso. Use Gerenciar.” Erros do cofre e estados de conexão continuam.

Biblioteca:

- Adicione um jogo para começar a organizar sua coleção. → Adicione um jogo à biblioteca.
- Tente outro termo ou ajuste os filtros para encontrar seus jogos. → Altere a busca ou limpe os filtros.

Desejos:

- Salve os jogos que você quer jogar para acompanhar suas ofertas. → Adicione um jogo aos desejos.

Mantidos preço, origem, atribuição e motivo da ausência de oferta; nenhum Indisponível silencioso foi introduzido.

Memórias:

- Nenhuma frase de apoio adicional foi encontrada na tela global; nenhuma memória, legenda digitada, data ou conteúdo do usuário foi removido. O estado vazio com caminho concreto para criar a primeira memória foi preservado conforme item 5.

Estatísticas:

- Na biblioteca, legenda redundante do total de jogos.
- Jogos finalizados, legenda redundante do total de concluídos.

Mantidos números, rótulos, origem App + Steam, média e motivos de ausência de registros.

Início:

- Conquistas, sessões e memórias recentes.
- Suas sessões, conquistas e anotações aparecerão aqui.
- Retome de onde você parou.
- Jogos prontos para a sua próxima escolha.
- Sua história começa ao jogar → Nenhuma atividade.
- Sua biblioteca começa aqui → Biblioteca vazia.
- Adicione um jogo para reunir capas, progresso e memórias em um só lugar. → Adicione um jogo à biblioteca.
- Escolha seu próximo jogo → Nenhum jogo em andamento.
- Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui. → Abra a ficha de um jogo e selecione Jogando.

Ficha:

- Guarde suas melhores cenas → Nenhuma captura.
- Guarde conquistas e objetivos pessoais deste jogo.
- O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.
- Os arquivos e as versões vinculadas a este jogo aparecem aqui.
- Proteja seus saves → Saves não configurados.
- Escolha a pasta de saves tradicionais para preparar seus backups. → Selecione a pasta de saves.
- Adicione capturas e vídeos deste jogo à sua galeria. → Adicione uma captura ou vídeo.
- A ficha ainda está incompleta. Adicione informações para organizar este jogo. → Ficha incompleta. Edite os dados do jogo.
- Não há texto descritivo disponível nesta ficha. A fonte pode não fornecer um resumo para este jogo. → Sem texto descritivo. Pesquise manualmente ou edite a ficha.
- O que você quer guardar desta experiência? → Anotação (rótulo do campo).

Descrições externas/Wikipédia, notas, diário, legendas digitadas, erros e estados vazios acionáveis foram preservados. Nenhum arquivo protegido foi usado para essa limpeza.

## Suíte completa definitiva — saída integral

Commit de código: `94fecc1b4bb7426503c9f492d119c353c9c68dc1`. Linux, Python 3.12.14, Qt offscreen, dados isolados em /tmp.

Comando:
```sh
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider
```

stdout:
```text
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 39%]
........................................................................ [ 53%]
........................................................................ [ 66%]
........................................................................ [ 79%]
........................................................................ [ 92%]
......................................                                   [100%]
542 passed in 353.65s (0:05:53)
```

stderr:
```text
```

Código de saída: 0.

O histórico integral de comandos, reproduções, falhas iniciais, correções de montagem dos testes novos, stdout, stderr e códigos de saída permanece em RELATORIO_0135_TESTES.md. Nenhuma saída de teste foi truncada nesse arquivo. As rodadas anteriores pertencem aos estados de código descritos no histórico, não à aprovação do commit definitivo.

## Proteções, encoding e evidências

Auditoria contra af1d3ab: dialogs.py, quick_add.py inteiro, worker.py, enrichment.py, game_import.py, completion_queue.py, test_save_lifecycle.py, test_visual_0132.py e publish-0.1.28.yml idênticos. Nenhuma alteração em workflows, tags ou releases. Schema 4 preservado. Nenhum token, JSON OAuth ou conteúdo do cofre foi impresso/versionado.

Arquivos modificados em LF; novas leituras de texto e testes usam encoding='utf-8'. O parser VDF remove BOM explicitamente após leitura UTF-8. Arquivos protegidos não foram normalizados incidentalmente. Asserções de proteção e lifecycle permanecem intactas.

Capturas Qt geradas com fixtures locais em 1280×800 e 1920×1080; fontes/contas/arte simuladas são explicitadas nos manifestos e não equivalem a validação Windows ou contas autenticadas. A referência visual foi usada para hierarquia e proporção, preservando nove temas e identidade atuais.

## Patches completos e SHA-256

Cada arquivo abaixo contém a saída integral de `git format-patch -1 <sha> --stdout`, sem resumo. Diretório local da entrega: /workspace/work/entrega-0135/patches. O manifesto SHA256SUMS acompanha os arquivos. O diretório de outputs do cliente está somente leitura neste ambiente; por isso esta entrega fica preservada no workspace, e o relatório principal é também colado integralmente no chat.

```text

98b865c38bed7dbc23c7aa96a9dc3e47be2e85942480b19fcd267da2e4b3db1c  2b43ea87886207c97397b92881c844f4c7ebbcd2.patch

32e8b4fc0ba3b452de370d05144f1fec0c154f77242f552b40ae9c9ac9cead20  5c582f2a0fe32310db49e2fd4a7c7958b1fae9d3.patch

af457644da3ef0d5b8adf8d3aaa63a25fa6686a8803b81b37d4450d81ad7a3d9  89c137b675043d3a4d6510e69f2a48da1b6066fd.patch

36db99b8bf1edcb3debe1cb071bae9de51ca2fa0a1b0c3ed92877bf583e80cfb  1d866017946cb774d0b304bb8582efe621df0ae7.patch

bf2ca2116776121e559a9a6188d121a9015aa4e7ba246fee6f5a6d92a77539b8  2f7032c354760b753268150402092713996cb13a.patch

19d8ddde1ada33c004c5313fa09c7aac11a9715a040a9f3c09a9e9bd6a6864b2  d7e171407f798131e3dc25b15ad4c5804390b67e.patch

025e74b55958f235f4ea4a728cd9975419ca82e2dfeaaa407099a65a381469a8  4888201b4e5f759d6318f466e74b1e034d44a7a2.patch

d804ff4eea092622f29b3e28f1220129791def4101682166dc13a61094699dba  7b5798d24eeb6748755c6ef799c8e11efdbaeaec.patch

36b59f68781b66a3e19d5eedc2f614baf64771c5e9632366507c850544356dac  278692b653c3dc95315f9e87240077e8dea8d62e.patch

e47708bc47c34b71f6d52fc162a7c1129a433912b74529eeaf7e7db35064558d  677e852d14c69a3a6ca95b06768af15c0368c420.patch

a19b044a5bcc845006d30ae6a0b83c29c9305c23af9d1dc95890ae6f9a166aa2  872b33279e0ed4233a6211480d2174a6656c8001.patch

b7443739e1ea6dbffab9e63881431ce896f6b1160c3f327c3bb7cec6fa397c38  59b8f995fe1dbf991ab2d1172a9c2b11ca07f990.patch

3869255c4a7a41092487d8574c2c48766d6b699d15e68631409fd4b2a972b208  14392949df8e759d29ad1fd435ada09019327d88.patch

95d256732632b97e3c68853b2b390c7321c0cb7a52d3827d532a21506831a04c  981910d1889f5f07308d42adbaa315c15a702973.patch

37dd4cc40e187d5e78756688709aed83d67d310912365b1e2d4f5b98f60ede10  414b8d0341f39b11413bc2f6b33bdd6586b13192.patch

b06f228af3d7f5a05b09bcc491c4c21ea3dea462b35cf3e8b570c873a3cb1be5  e68f9c78adfede37d0236b56aa14cf197806ef92.patch

83a90218e524a00df872bf7fa2c0c3d289b9961e2754514184029788da43702d  4b0ce3eb1de2d88c8517d19a119a6fdafec7d307.patch

e8efd98dae00aee098c5f645a572a6deb98d0e3aededbda14734b40e42dc5a02  09b1047b4dbf8dd4b01bdc3806da1edc0565ccf1.patch

6f13593a09f8cd9d93a48026417de07780d573db55493243fcef49896c27da1c  643c66e2af82efab98ed7a71b701a3a0e8912c26.patch

e1177bf9264fffcdfeec327dd806810ffb9515db2b0418a97ff33d738eaafcd0  d4623212ed4f4f2ba7ffec223704d7642166b816.patch

0508f6b5532f11e0694f1ceab010344562d13c5ec6ce4064da4ab95f37abee35  3b776d862e815a4627a40830cd50877befbf237f.patch

b94904b666098eb5381fca3ab6711d29907455d3057c0c5dfb49d8c4d2063942  117f362d0a8b66c53910a36b54b8688875d00f7a.patch

acb4560f88733309f3affa0c9eefd0ce8174ef23618de94f8ce69eb4077ec2c5  335d5375d7d6d7448bb950fb06344d9e3254d1fa.patch

caabb38b0c75922e3550858cb71f1fac2386df12406e3a671afd4d27244918c4  8dddbc3cec3bfe8660c56afc841911aeba4a9e83.patch

5b3a2945b1a8d42a0720d9cf2baab4880e1bd22691b4203107c50e59d28e0e08  3281c286bbb9696ed17593f00fe1b1254df123e1.patch

240bc2b8b31aeb244cc0dfbfd5423982d2e58267748e2690bca43e2772969beb  0c8b119625aec169a06eef8b18a2cb7076fe2526.patch

24c4c42d7c13e2076bdfafd6deb4a95799ddc60c1bb040a768dfe69cc4d689b5  1d67c155cbf5274911b83b08ec1d154af9dbb554.patch

bfa25b114122bbcddbe397854a3fb8c2b5d2e9c0f6ccce78e2d8ab34a6c32372  f5df459eea328f4746da22c9e3c6c102ee2b0391.patch

2dad9a883e3c83556825bdcc31b9fe5b1268a3d8689b20d266cb3b6e6dfd46ad  a2e7f605afb07122676e67b050bee9f2f0421657.patch

be75a79d22065c7b0256ad477472283d7f9ba80978e38f22efaef7788986cb32  94fecc1b4bb7426503c9f492d119c353c9c68dc1.patch

```

O commit de fechamento documental é listado no manifesto externo após sua criação, com patch e SHA-256, para evitar referência circular no próprio relatório.

## Não validado no Windows e bloqueios

- Captura real de janela no Windows não foi validada. O primeiro uso real será no PC do dono. Cobertura Linux usa adaptador controlado. Processo-filho, janela minimizada, múltiplas janelas, renderização exclusiva e restrições de captura podem exigir adaptação específica; o app recusa identificação ambígua.
- Item 2: encerramento do processo coberto com subprocessos reais de teste em dois jogos. Encerrar apenas a ROM mantendo o emulador aberto não tem detecção validada por perfil; permanece bloqueado, com ação manual e aviso existentes preservados. Não declarar esse subcaso concluído.
- A4 permanece bloqueado e intacto; não houve mudança do cadastro protegido do Drive.
- Executável congelado, runner/build Windows, DPI/fontes do PC do dono, registro/bibliotecas Steam reais, emuladores reais, contas Drive/Steam/GG.deals, OAuth e downloads reais de ROMs não foram validados nesta entrega.
- A origem exata do registro de data no banco pessoal do dono não foi acessada. A correção de fuso é comprovada para o caso isolado documentado, sem manipular os dados gravados.
- A versão declarada do pacote continua 0.1.34; não houve preparação/publicação de release 0.1.35 nem alteração de schema.

Sem push porque o conjunto ainda contém o bloqueio do item 2. Nenhuma publicação externa foi feita.

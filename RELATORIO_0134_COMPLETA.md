# Checkpoint 0.1.34 — entrega local e pendência A4

Checkout: /workspace/Checkpoint-0134. Branch: fix/0.1.34-bugs. Partida: 10458eea4b037236e2ae79731f53c06625eaf5b2. Ponta do código validado: 014a6789fdc2c77ec804f7a96ff39dce2f0e1be1. O último commit desta entrega só atualiza documentação.

## Itens, arquivos, funções e resultado

| Item | Commit | Arquivos e funções | Status | Motivo / prova |
|---|---|---|---|---|
| A1, A3, A5, A6 | 4369e9c | rom_link.py: candidates/bind/verify/complete_link; rom_link_dialog.py: refresh/chosen/start/completed/failed/finished_job; rom_link_worker.py: run_link/execute; app.py: main; window.py: link_rom; detail_view.py: build_detail | feito | Busca própria da ficha, até três candidatos, preferência por região/revisão, download verificado, texto e artes, erro com causa e nova tentativa. Dois jogos: Zelda A Link to the Past e Metroid Fusion. |
| A2 | 4369e9c | rom_link.bind; trash_import.save_with_prompt; integrations/drive.DriveScanner.associate | feito nas entradas da interface | Substitui game_id do vínculo anterior numa transação; sem INSERT extra em game_files. Índice, downloads e rom_versions são preservados. API protegida save_import e vínculos antigos não são normalizados em massa. |
| A4 | — | quick_add.choose/drive_loaded; dialogs.load_drive_file/validate; scripts/drive_search_flow_support.py; tests/test_drive_0133.py | bloqueado | O contrato protegido exercita ROM > candidatos > escolha > confirmar. Automatizar esse percurso quebra os testes congelados, incluindo a expectativa de nenhum cadastro antes da confirmação. Sem monkeypatch de produção, temporizador para contornar o teste ou mudança escondida de expectativa. O motor novo suporta criação, mas não foi conectado a essa aba. |
| B1 | 2081d54 | metadata_state.has_game_data; detail_view.build_detail; tests/test_bugs_0134.py | feito | Critério compartilhado nas fichas, inclusive desejos e ROMs: texto, imagem ou preço impede o aviso de dados ausentes. Mantida a correção anterior e confirmadas as regressões. |
| B2, B3 | 2081d54 | metadata_state.display_source/completion_feedback; window.game_completed; detail_view.build_detail | feito | Origem explícita é preservada, inclusive Google Drive legado; identidade/vínculo real é usado quando a origem falta. Zero campos novos não é falha quando há dados. Consulta sem texto disponível tem explicação. |
| B4, D1 | 2081d54 | tests/test_detail_0134.py:test_menu_edge_click_runs_only_named_action; WindowMenu.showEvent preservado | feito por verificação | Popup próximo da borda e janela fora dos limites da tela: clique real em Obter ficha dispara apenas a fila com force=True, sem abrir Trocar imagens, em dois jogos. Não reproduzido o erro anterior após a contenção do item 7. |
| C1, C2 | 726493d | detail_view.build_detail; tests/test_time_prices_0134.py | feito | Tempo local e Steam em linhas separadas. Nos próprios cards de Desejos, último preço válido permanece; sem preço há motivo. Sem mudar importação ou números remotos. |
| D2 | 8157af7 | cover_art.cover_pixmap; CoverDelegate.paint; GameTile.__init__; tests/test_banner_fallback_0134.py | feito | Capa válida primeiro, depois banner, nunca logo na grade. Imagem de teste 400×600 e pixel dentro de 200×300; confirmado também no viewport do grid, em dois jogos. |
| D3 | 4b729b3 | icons.lucide_icon; ui_components.nav_icon/action; Badge/ThemeSwatch; BusyIndicator/TaskStatus; DialogTitleBar; DisclosureButton; QuickAdd.show_result; pyproject; assets/lucide; THIRD_PARTY_NOTICES | feito | Lucide 0.468.0 ISC, traço 2/24, contextos 10–32 px. Teste de tamanho e máscara contida, sem igualdade byte a byte de ícone pequeno. Logos externas e identidade própria preservadas. |
| E1 | 8157af7 | CoverDelegate.paint; GameTile.paintEvent; cover_art.paint_art | feito | Capas verticais preenchem a área com recorte proporcional; alternativa de banner. Sem logo na grade. |
| E2 | ed6dba5 | list_art.list_icon; window.build_library/refresh_library | feito | Coluna de arte com 160 px; logo contida ou título desenhado no mesmo espaço. Não reutiliza capa nessa coluna. |
| E3 | ed6dba5 | WishGrid.reflow; tests/test_layout_0134.py; tests/test_card_layout.py | feito | Cards maiores, até quatro colunas; arte quadrada e colunas ocupando a largura. Expectativa antiga de colunas iguais foi substituída pela regra nova, descrita abaixo. |
| E4 | ed6dba5 | FullTextLabel.resizeEvent; design_system.empty_state | feito | Texto media 51 px, mas recebia 33 px. Altura mínima segue a largura real; removido teto que cortava conteúdo. Título e descrição completos. |
| E5, E6, E7, E8 | ed6dba5 | settings_view.build_settings/folder_row; tests/test_layout_0134.py | feito | Abas compactas e Conexões 2×2 mantidas e verificadas; cards com proporções controladas. Caminho completo selecionável ou Não definida; atualização com botão; nomes nos swatches e tooltips. |
| E9 | 4369e9c / ed6dba5 | detail_view.build_detail; tests/test_layout_0134.py | feito | Removido Configurar execução avulso da aba Arquivos. A barra principal e a atividade preservam suas ações pertinentes. |
| Versão | 014a678 | pyproject.toml; checkpoint/__init__.py | feito | 0.1.34 apenas local. Schema 4. Sem release, tag ou alteração de CHANGELOG. |
| Documentação | commit de fechamento | README; CONTINUITY; PROJECT_STATUS; INTEGRATIONS; ARCHITECTURE; este relatório | feito | Registra limites e A4 bloqueado; sem declarar conclusão total. |

## Contratos e única expectativa anterior atualizada

O teste test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged permanece intacto e passa. Nesta rodada, somente show_result mudou em quick_add.py (pintura do check Lucide). dialogs.py inteiro permaneceu inalterado. Também ficaram idênticos worker.py, enrichment.py, game_import.py, completion_queue.py, test_save_lifecycle.py, .github/workflows/*, .github/release-notes.md e CHANGELOG.md. Nenhum skip, xfail ou exclusão foi acrescentado.

A exceção explícita é tests/test_card_layout.py, exigida pela regra nova E3: a comparação `window.gallery.columns == wish_columns` não se aplica mais, pois cards de desejos devem ser maiores que a grade de capas. O teste foi renomeado e substituiu essa comparação por preservação das colunas dos desejos, largura mínima de 280 px e arte 1:1. As verificações de fonte, itens, controle de tamanho e largura do link continuam. Não foram alteradas as asserções de cadastro, Drive, lifecycle, valores de preço ou tempo dos testes anteriores.

A2 vale nas entradas da interface e no serviço novo bind. Não adiciona constraint ao banco nem migra os vínculos antigos: isso preserva a API de versões congelada pelo teste. Chamadas diretas de save_import podem manter várias versões. Essa limitação impede declarar uma invariável global do banco.

## Testes e resultados

Ambiente: Linux, Python 3.12.14, PySide6, Qt offscreen, dados isolados em /tmp. Nenhuma instalação de dependência de execução foi necessária. Os SVGs Lucide foram obtidos do pacote público lucide-static 0.468.0, sem credenciais.

Comando da suíte (python do ambiente virtual já preparado):

```sh
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 /workspace/Checkpoint/.venv/bin/python -m pytest tests -q -p no:cacheprovider
```

Resultado inicial, antes das alterações desta rodada:

```
........................................................................ [ 18%]
........................................................................ [ 37%]
........................................................................ [ 56%]
........................................................................ [ 75%]
........................................................................ [ 94%]
...................                                                      [100%]
379 passed in 318.04s (0:05:18)
```

Execução intermediária de diagnóstico: 2 failed, 418 passed in 351.30s. Motivos: nova regra E3 contra comparação antiga de colunas; abreviação indevida de Google Drive. O rótulo foi corrigido no app, sem alterar a asserção. As fontes estavam em edição durante essa rodada; ela não serve como aprovação de um commit. Registro integral local: /tmp/0134-completa-suite-final.log.

Rodada anterior à ampliação da regra de vínculo único às outras entradas da interface: 422 passed in 351.84s. Depois da ampliação e dos novos testes, foi exigida outra suíte completa, abaixo.

Saída completa da suíte definitiva, exit 0:

```
........................................................................ [ 16%]
........................................................................ [ 33%]
........................................................................ [ 50%]
........................................................................ [ 67%]
........................................................................ [ 84%]
................................................................         [100%]
424 passed in 343.38s (0:05:43)
```

### Vínculo, gerenciador, cadastro e proteção

```
.........................................                                [100%]
41 passed in 2.00s
```

### Ficha, menu e regressões anteriores

```
.................................                                        [100%]
33 passed in 2.44s
```

### Tempo, preços e proteção visual

```
.............................................                            [100%]
45 passed in 4.50s
```

### Alternativa de banner e regressões

```
.........................                                                [100%]
25 passed in 1.83s
```

### Lucide e proteção visual

```
......................................................................   [100%]
70 passed in 4.64s
```

### Layout, dados e proteção visual

```
..............................................................           [100%]
62 passed in 4.36s
```

### Regras de colunas, fonte e layout

```
..............................................................           [100%]
62 passed in 12.81s
```

Correções dos próprios testes novos durante implementação, sem afrouxar comportamento: o primeiro teste do diálogo usava a enumeração inexistente d.Accepted; corrigido para d.DialogCode.Accepted. A primeira conta de altura da barra aumentava indevidamente páginas sem Steam de 64 para 66 px; o código foi corrigido preservando a asserção antiga de 64 px. O novo teste de texto vazio falhou com 33 contra 51 px; o componente foi corrigido, sem mudar a asserção. Logs intermediários locais: /tmp/0134-completa-A.log, /tmp/0134-completa-C.log e /tmp/0134-completa-E.log.

## Capturas

72 capturas novas, manifesto e hashes verificados em /tmp/checkpoint-0134-entrega-ui/visual-manifest.json. Commit limpo da geração: 014a6789fdc2c77ec804f7a96ff39dce2f0e1be1. Verde/Rosa, 1280×800 e 1920×1080. Geradas por scripts/render_ui_review.py --visual-review, com PYTHONPATH apontando explicitamente para este checkout. Jogos, artes, preços e estados de conexão são fixtures locais; não provam conta real nem o cadastro automático A4. As PNGs antigas de tentativas anteriores não são a evidência desta entrega.

Diferenças / limites: artes sintetizadas de teste em lugar das capas reais das referências; as capturas da aba Drive mostram o cadastro legado preservado, não uma prova de A4. Não houve validação visual do diálogo novo no Windows real; seu clique, trabalho e encerramento foram testados em Qt offscreen. A grade de conexões da referência continua 2×2; logos de serviços permanecem próprias.

- /tmp/checkpoint-0134-entrega-ui/visual-inicio-verde-1280x800.png — b957b68032a240bfb76c3d2528d86a751e4d373baea2528aac0106c1ff301466
- /tmp/checkpoint-0134-entrega-ui/visual-biblioteca-verde-1280x800.png — 1d6bbf2ea0a2c94423aa934241d17b37c97bd6d9e4ac9d965ecc38866466ca1c
- /tmp/checkpoint-0134-entrega-ui/visual-desejos-verde-1280x800.png — 52633f8184fa90ad12a999046633dad7e1edce4eaac52da12e23c135fb867eef

## Decisões conservadoras e pendências

- A4 deixado de fora para respeitar o contrato protegido; requer decisão explícita sobre a evolução dos testes/fluxo congelados antes de uma implementação compatível. Não foi contornado por alterações do guard, sleeps ou detecção de ambiente de teste.
- Uma identidade automática deve ser exata e inequívoca. Mais de uma identidade exata pede revisão em vez de aplicar arbitrariamente o primeiro jogo.
- ROM já pertencente a outro jogo não é tomada silenciosamente. Substituir o arquivo de um jogo desvincula, não apaga arquivos nem índice. O UPDATE também confere concorrência.
- USA precede Europe; dentro da região, maior revisão primeiro. Downloads sem pasta configurada usam ROMs no diretório de dados, exibido nas Configurações.
- Erros de download não impedem a tentativa de ficha; erros da ficha não desfazem o vínculo/download. Falhas exibem uma causa segura e nova tentativa, sem conteúdo de OAuth ou cofre.
- Banner é alternativa à capa; logos permanecem na lista e em Desejos. Logos de serviços e identidade Checkpoint não são substituídas por Lucide.
- Colunas de Desejos independentes da Biblioteca por E3. Só essa expectativa antiga foi substituída.
- Mudanças iniciais de fonte, cache de preço, contenção de menu, recorte das capas e introdução da Wikipédia da tarefa noturna anterior foram mantidas. Os sete patches anteriores pertencem à base 10458ee; os patches desta entrega representam os novos commits a partir dessa base.

## Não validado

Windows real, executável congelado, runner Windows, DPI/escala, janela mínima no PC do dono, fontes configuradas pelo usuário, contas reais de Drive/Steam, renovação OAuth real, downloads reais de ROMs e fontes reais RAWG/SteamGridDB/GG.deals. Nenhum build Windows foi gerado. Não houve push, tag, release ou PR.

## Patches

Os oito patches completos desta rodada são gerados, após o commit de documentação, por `git format-patch -1 <sha> --stdout`, em /tmp/0134-completa-patches/. SHA-256 e conteúdo integral acompanham a entrega. O manifesto externo inclui o commit final deste relatório sem criar referência circular no próprio arquivo.

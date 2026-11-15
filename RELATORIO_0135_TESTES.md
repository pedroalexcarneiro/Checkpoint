# RELATORIO_0135 — verificação inicial e planejamento

Implementação não iniciada. Nenhum teste executado ou asserção alterada.

Conta conectada confirmada pelo conector GitHub: pedroalexcarneiro (id 318648220). get_repo retornou push=true, admin=true, maintain=true, pull=true, triage=true.


## git ls-remote https://github.com/pedroalexcarneiro/Checkpoint.git refs/heads/fix/0.1.34-bugs

stdout:
```text
af1d3ab56492cba56b541ddb971759d9c15b015b	refs/heads/fix/0.1.34-bugs
```

stderr:
```text
```

Código de saída: 0


## gh release list --repo pedroalexcarneiro/Checkpoint --limit 100

stdout:
```text
Checkpoint 0.1.34 · Interface e PT-BR	Pre-release	v0.1.34	2026-11-14T18:52:19Z
Checkpoint 0.1.33 · Interface e PT-BR	Pre-release	v0.1.33	2026-11-14T04:09:33Z
Checkpoint 0.1.32 · Revisão visual	Pre-release	v0.1.32	2026-11-13T22:32:42Z
Checkpoint 0.1.30 · Ficha de ROMs do Drive	Pre-release	v0.1.30	2026-11-13T18:37:51Z
Checkpoint 0.1.29 · Biblioteca e cadastro	Pre-release	v0.1.29	2026-11-13T16:56:28Z
Checkpoint 0.1.28 · Migração e interface	Pre-release	v0.1.28	2026-11-13T10:32:37Z
Checkpoint 0.1.27 · Interface e PT-BR	Pre-release	v0.1.27	2026-11-13T03:21:36Z
Checkpoint 0.1.26 · Interface e PT-BR	Pre-release	v0.1.26	2026-11-13T03:08:57Z
Checkpoint 0.1.25 · Interface e PT-BR	Pre-release	v0.1.25	2026-11-13T02:44:30Z
Checkpoint 0.1.24 · Interface e PT-BR	Pre-release	v0.1.24	2026-11-13T01:55:56Z
Checkpoint 0.1.23 · Interface completa	Pre-release	v0.1.23	2026-11-12T18:26:27Z
Checkpoint 0.1.22 · Interface completa	Pre-release	v0.1.22	2026-11-12T18:20:15Z
Checkpoint 0.1.21 · Revisão visual e banners Steam	Pre-release	v0.1.21	2026-11-12T17:45:21Z
Checkpoint 0.1.20 · Revisão visual e banners Steam	Pre-release	v0.1.20	2026-11-12T17:06:21Z
Checkpoint 0.1.19 · Revisão visual e banners Steam	Pre-release	v0.1.19	2026-11-12T16:34:22Z
Checkpoint 0.1.18 · Nova interface e identidade	Pre-release	v0.1.18	2026-11-12T15:59:38Z
Checkpoint 0.1.17 · Correção do carregamento ao salvar	Pre-release	v0.1.17	2026-11-12T12:28:07Z
Checkpoint 0.1.16 · Cadastro simples e downloads isolados	Pre-release	v0.1.16	2026-11-12T12:11:17Z
Checkpoint 0.1.15 · Ficha e imagens no cadastro	Pre-release	v0.1.15	2026-11-12T11:39:16Z
Checkpoint 0.1.14 · Steam e correção do Qt	Pre-release	v0.1.14	2026-11-12T11:03:09Z
Checkpoint 0.1.13 · Cadastro pelo Drive e capas sem corte	Pre-release	v0.1.13	2026-11-11T19:06:05Z
Checkpoint 0.1.12 · Capa, banner e logo automáticos	Pre-release	v0.1.12	2026-11-11T16:44:11Z
Checkpoint 0.1.11 · Pesquisa nas ROMs do Drive	Pre-release	v0.1.11	2026-11-11T13:35:21Z
Checkpoint 0.1.10 · Pastas personalizadas e capas	Pre-release	v0.1.10	2026-11-11T13:27:54Z
Checkpoint 0.1.9 · Reconhecimento de plataformas	Pre-release	v0.1.9	2026-11-11T12:45:26Z
Checkpoint 0.1.8 · Correção da conexão HTTPS	Pre-release	v0.1.8	2026-11-11T12:20:04Z
Checkpoint 0.1.7 · Teste de conexão do Google Drive	Pre-release	v0.1.7	2026-11-11T11:32:08Z
Checkpoint 0.1.6 · Diagnóstico da autenticação Drive	Pre-release	v0.1.6	2026-11-10T19:01:05Z
Checkpoint 0.1.5 — Paletas de cores	Pre-release	v0.1.5	2026-11-10T18:17:10Z
Checkpoint 0.1.4 — Correção da consulta de atualizações	Pre-release	v0.1.4	2026-11-10T17:59:35Z
Checkpoint 0.1.3 — Atualizações pelo aplicativo	Pre-release	v0.1.3	2026-11-10T17:43:37Z
Checkpoint 0.1.2 — Saves por jogo	Pre-release	v0.1.2	2026-11-10T16:53:42Z
```

stderr:
```text
```

Código de saída: 0


## git rev-parse HEAD

stdout:
```text
af1d3ab56492cba56b541ddb971759d9c15b015b
```

stderr:
```text
```

Código de saída: 0


## git status --short

stdout:
```text
?? PLANO_0135.md
```

stderr:
```text
```

Código de saída: 0


Plano: PLANO_0135.md. Aguardando aprovação; conflitos específicos nos testes de tempo e layout descritos no plano. O diretório de outputs do cliente está em filesystem somente leitura neste ambiente; arquivos preservados no checkout e conteúdo entregue no chat.

## Aprovação parcial do dono — antes de qualquer commit

O dono aprovou explicitamente duas mudanças de expectativa de teste:

1. Item 4 — `tests/test_time_prices_0134.py::test_app_and_steam_times_are_separate` pode ser atualizado para exigir a soma de app e Steam em um número só. Motivo: a expectativa anterior de tempos separados contradiz o requisito aprovado do item 4. A cobertura dos valores de origem será preservada; apresentação no formato XhXXmin, sem espaços.
2. Item 3 e E3 anterior — `tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art` pode ser atualizado para largura máxima de 360 px, mantendo cobertura de arte quadrada, largura e colunas. Motivo: exigir preenchimento integral da largura pode contradizer o teto aprovado para cards e o aumento de colunas em janelas largas. A autorização cobre a expectativa de preenchimento integral relacionada a essa regra, não o enfraquecimento de outras verificações.

Estas autorizações não são autorização para iniciar a implementação agora. O dono solicitou o conteúdo integral de PLANO_0135.md na conversa e determinou aguardar a resposta literal “pode seguir” antes de qualquer commit. Nenhum código ou teste foi alterado nesta etapa.

Restrições reafirmadas: nenhuma publicação agora; sem push intermediário, tag, release ou PR. A4 e arquivos protegidos intactos. Após “pode seguir”, executar na ordem do plano, um commit por item, testes antes/depois com dois jogos diferentes. Push de fix/0.1.35-ajustes somente depois de todos os itens prontos e da suíte completa passando em Linux com QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp. Release requer autorização explícita.

O plano transcrito mantém seu texto original, inclusive os pedidos de autorização que agora estão atendidos por este registro específico.

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_launch_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_main_play_routes_linked_rom[sample0-Zelda: A Link to the Past-SNES-.sfc] _
tests/test_launch_0135.py:16: in test_main_play_routes_linked_rom
    w.start_game(w.library.get(i))
checkpoint/window.py:534: in start_game
    self.guard(lambda:self.launcher.start(game))
checkpoint/window.py:138: in guard
    try: return callback()
                ^^^^^^^^^^
checkpoint/window.py:534: in <lambda>
    self.guard(lambda:self.launcher.start(game))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_launch_0135.py:15: in <lambda>
    monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Jogar abriu executável sem ROM
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_main_play_routes_linked_rom[sample0-Metroid Fusion-GBA-.gba] _______
tests/test_launch_0135.py:16: in test_main_play_routes_linked_rom
    w.start_game(w.library.get(i))
checkpoint/window.py:534: in start_game
    self.guard(lambda:self.launcher.start(game))
checkpoint/window.py:138: in guard
    try: return callback()
                ^^^^^^^^^^
checkpoint/window.py:534: in <lambda>
    self.guard(lambda:self.launcher.start(game))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_launch_0135.py:15: in <lambda>
    monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Jogar abriu executável sem ROM
_ test_main_play_routes_linked_rom[sample1-Zelda: A Link to the Past-SNES-.sfc] _
tests/test_launch_0135.py:16: in test_main_play_routes_linked_rom
    w.start_game(w.library.get(i))
checkpoint/window.py:534: in start_game
    self.guard(lambda:self.launcher.start(game))
checkpoint/window.py:138: in guard
    try: return callback()
                ^^^^^^^^^^
checkpoint/window.py:534: in <lambda>
    self.guard(lambda:self.launcher.start(game))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_launch_0135.py:15: in <lambda>
    monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Jogar abriu executável sem ROM
______ test_main_play_routes_linked_rom[sample1-Metroid Fusion-GBA-.gba] _______
tests/test_launch_0135.py:16: in test_main_play_routes_linked_rom
    w.start_game(w.library.get(i))
checkpoint/window.py:534: in start_game
    self.guard(lambda:self.launcher.start(game))
checkpoint/window.py:138: in guard
    try: return callback()
                ^^^^^^^^^^
checkpoint/window.py:534: in <lambda>
    self.guard(lambda:self.launcher.start(game))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_launch_0135.py:15: in <lambda>
    monkeypatch.setattr(w.launcher,'start',lambda game:pytest.fail('Jogar abriu executável sem ROM'))
                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Jogar abriu executável sem ROM
=========================== short test summary info ============================
FAILED tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Zelda: A Link to the Past-SNES-.sfc]
FAILED tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Metroid Fusion-GBA-.gba]
FAILED tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Zelda: A Link to the Past-SNES-.sfc]
FAILED tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Metroid Fusion-GBA-.gba]
4 failed in 0.59s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_launch_0135.py tests/test_services.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.....F...                                                                [100%]
=================================== FAILURES ===================================
_______________________ test_emulator_arguments_no_shell _______________________
tests/test_services.py:19: in test_emulator_arguments_no_shell
    assert command==[sys.executable,'--fullscreen',str(rom.resolve())]
E   AssertionError: assert ['/opt/codex/...h spaces.sfc'] == ['/workspace/...h spaces.sfc']
E     
E     At index 0 diff: '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3.12' != '/workspace/work/venv/bin/python'
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED tests/test_services.py::test_emulator_arguments_no_shell - AssertionEr...
1 failed, 8 passed in 0.50s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_launch_0135.py tests/test_services.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.........                                                                [100%]
9 passed in 0.48s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_launch_0135.py -k monitors --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
__ test_rom_launch_monitors_emulator_exit[sample0-Zelda: A Link to the Past] ___
tests/test_launch_0135.py:33: in test_rom_launch_monitors_emulator_exit
    assert commands[0][2] is True
E   assert False is True
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
________ test_rom_launch_monitors_emulator_exit[sample0-Metroid Fusion] ________
tests/test_launch_0135.py:33: in test_rom_launch_monitors_emulator_exit
    assert commands[0][2] is True
E   assert False is True
__ test_rom_launch_monitors_emulator_exit[sample1-Zelda: A Link to the Past] ___
tests/test_launch_0135.py:33: in test_rom_launch_monitors_emulator_exit
    assert commands[0][2] is True
E   assert False is True
________ test_rom_launch_monitors_emulator_exit[sample1-Metroid Fusion] ________
tests/test_launch_0135.py:33: in test_rom_launch_monitors_emulator_exit
    assert commands[0][2] is True
E   assert False is True
=========================== short test summary info ============================
FAILED tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Zelda: A Link to the Past]
FAILED tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Metroid Fusion]
FAILED tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Zelda: A Link to the Past]
FAILED tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Metroid Fusion]
4 failed, 4 deselected in 0.52s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_launch_0135.py tests/test_services.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.............                                                            [100%]
13 passed in 0.82s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_wishes_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.42s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_wishes_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
____________________ test_wish_maximum_and_columns[sample0] ____________________
tests/test_wishes_0135.py:16: in test_wish_maximum_and_columns
    assert card.width()<=360
E   assert 547 <= 360
E    +  where 547 = <built-in method width of WishCard object at 0x7fd1f82e0a40>()
E    +    where <built-in method width of WishCard object at 0x7fd1f82e0a40> = <checkpoint.collection_views.WishCard(0x21e39080, name="panel") at 0x7fd1f82e0a40>.width
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____________________ test_wish_maximum_and_columns[sample1] ____________________
tests/test_wishes_0135.py:16: in test_wish_maximum_and_columns
    assert card.width()<=360
E   assert 547 <= 360
E    +  where 547 = <built-in method width of WishCard object at 0x7fd1f85f0a80>()
E    +    where <built-in method width of WishCard object at 0x7fd1f85f0a80> = <checkpoint.collection_views.WishCard(0x21dcf270, name="panel") at 0x7fd1f85f0a80>.width
=========================== short test summary info ============================
FAILED tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample0] - as...
FAILED tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample1] - as...
2 failed in 0.50s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_wishes_0135.py tests/test_layout_0134.py tests/test_card_layout.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
...............                                                          [100%]
15 passed in 1.58s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_time_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_combined_time_without_join_multiplication[sample0-Zelda: A Link to the Past] _
tests/test_time_0135.py:13: in test_combined_time_without_join_multiplication
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 4h00min'
E   AssertionError: assert 'Tempo jogado: 1 h' == 'Tempo jogado: 4h00min'
E     
E     - Tempo jogado: 4h00min
E     ?               ^ -----
E     + Tempo jogado: 1 h
E     ?               ^^
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_combined_time_without_join_multiplication[sample0-Metroid Fusion] ____
tests/test_time_0135.py:13: in test_combined_time_without_join_multiplication
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 4h00min'
E   AssertionError: assert 'Tempo jogado: 1 h' == 'Tempo jogado: 4h00min'
E     
E     - Tempo jogado: 4h00min
E     ?               ^ -----
E     + Tempo jogado: 1 h
E     ?               ^^
_ test_combined_time_without_join_multiplication[sample1-Zelda: A Link to the Past] _
tests/test_time_0135.py:13: in test_combined_time_without_join_multiplication
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 4h00min'
E   AssertionError: assert 'Tempo jogado: 1 h' == 'Tempo jogado: 4h00min'
E     
E     - Tempo jogado: 4h00min
E     ?               ^ -----
E     + Tempo jogado: 1 h
E     ?               ^^
____ test_combined_time_without_join_multiplication[sample1-Metroid Fusion] ____
tests/test_time_0135.py:13: in test_combined_time_without_join_multiplication
    assert w.detail_page.findChild(QLabel,'localPlaytime').text()=='Tempo jogado: 4h00min'
E   AssertionError: assert 'Tempo jogado: 1 h' == 'Tempo jogado: 4h00min'
E     
E     - Tempo jogado: 4h00min
E     ?               ^ -----
E     + Tempo jogado: 1 h
E     ?               ^^
=========================== short test summary info ============================
FAILED tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Zelda: A Link to the Past]
FAILED tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Metroid Fusion]
FAILED tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Zelda: A Link to the Past]
FAILED tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Metroid Fusion]
4 failed in 0.56s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_time_0135.py tests/test_time_prices_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........                                                                 [100%]
8 passed in 0.85s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
____ test_empty_memory_goes_to_game_tab[sample0-Zelda: A Link to the Past] _____
tests/test_memories_0135.py:10: in test_empty_memory_goes_to_game_tab
    assert any('anotação' in t.text() and 'Memórias' in t.text() for t in w.pages[3].findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_empty_memory_goes_to_game_tab.<locals>.<genexpr> at 0x7f1d81d49b10>)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
__________ test_empty_memory_goes_to_game_tab[sample0-Metroid Fusion] __________
tests/test_memories_0135.py:10: in test_empty_memory_goes_to_game_tab
    assert any('anotação' in t.text() and 'Memórias' in t.text() for t in w.pages[3].findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_empty_memory_goes_to_game_tab.<locals>.<genexpr> at 0x7f1d81d4ab50>)
____ test_empty_memory_goes_to_game_tab[sample1-Zelda: A Link to the Past] _____
tests/test_memories_0135.py:10: in test_empty_memory_goes_to_game_tab
    assert any('anotação' in t.text() and 'Memórias' in t.text() for t in w.pages[3].findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_empty_memory_goes_to_game_tab.<locals>.<genexpr> at 0x7f1d81fdbb90>)
__________ test_empty_memory_goes_to_game_tab[sample1-Metroid Fusion] __________
tests/test_memories_0135.py:10: in test_empty_memory_goes_to_game_tab
    assert any('anotação' in t.text() and 'Memórias' in t.text() for t in w.pages[3].findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_empty_memory_goes_to_game_tab.<locals>.<genexpr> at 0x7f1d81d89cb0>)
=========================== short test summary info ============================
FAILED tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Metroid Fusion]
FAILED tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Metroid Fusion]
4 failed in 0.50s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.58s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py -k geometry --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
____ test_memory_card_geometry_and_title[sample0-Zelda: A Link to the Past] ____
tests/test_memories_0135.py:25: in test_memory_card_geometry_and_title
    assert cards[0].minimumHeight()==cards[1].minimumHeight()>=300
E   assert 146 == 289
E    +  where 146 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7bcef40>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7bcef40> = <checkpoint.design_system.CardSurface(0x22423330, name="panel") at 0x7ff9c7bcef40>.minimumHeight
E    +  and   289 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7bce640>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7bce640> = <checkpoint.design_system.CardSurface(0x2240dbf0, name="panel") at 0x7ff9c7bce640>.minimumHeight
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_________ test_memory_card_geometry_and_title[sample0-Metroid Fusion] __________
tests/test_memories_0135.py:25: in test_memory_card_geometry_and_title
    assert cards[0].minimumHeight()==cards[1].minimumHeight()>=300
E   assert 146 == 289
E    +  where 146 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7b9db00>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7b9db00> = <checkpoint.design_system.CardSurface(0x220778f0, name="panel") at 0x7ff9c7b9db00>.minimumHeight
E    +  and   289 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7bb1a40>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7bb1a40> = <checkpoint.design_system.CardSurface(0x220ccbe0, name="panel") at 0x7ff9c7bb1a40>.minimumHeight
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
____ test_memory_card_geometry_and_title[sample1-Zelda: A Link to the Past] ____
tests/test_memories_0135.py:25: in test_memory_card_geometry_and_title
    assert cards[0].minimumHeight()==cards[1].minimumHeight()>=300
E   assert 146 == 289
E    +  where 146 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7b80940>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7b80940> = <checkpoint.design_system.CardSurface(0x21f478b0, name="panel") at 0x7ff9c7b80940>.minimumHeight
E    +  and   289 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7f21b40>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7f21b40> = <checkpoint.design_system.CardSurface(0x221c3320, name="panel") at 0x7ff9c7f21b40>.minimumHeight
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_________ test_memory_card_geometry_and_title[sample1-Metroid Fusion] __________
tests/test_memories_0135.py:25: in test_memory_card_geometry_and_title
    assert cards[0].minimumHeight()==cards[1].minimumHeight()>=300
E   assert 146 == 289
E    +  where 146 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7b8acc0>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7b8acc0> = <checkpoint.design_system.CardSurface(0x2217cdd0, name="panel") at 0x7ff9c7b8acc0>.minimumHeight
E    +  and   289 = <built-in method minimumHeight of CardSurface object at 0x7ff9c7b812c0>()
E    +    where <built-in method minimumHeight of CardSurface object at 0x7ff9c7b812c0> = <checkpoint.design_system.CardSurface(0x22174ed0, name="panel") at 0x7ff9c7b812c0>.minimumHeight
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Metroid Fusion]
FAILED tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Metroid Fusion]
4 failed, 4 deselected in 0.47s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........                                                                 [100%]
8 passed in 0.90s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py -k delete --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_delete_memory_requires_confirmation[sample0-Zelda: A Link to the Past] __
tests/test_memories_0135.py:37: in test_delete_memory_requires_confirmation
    w.delete_memory(row)
    ^^^^^^^^^^^^^^^
E   AttributeError: 'MainWindow' object has no attribute 'delete_memory'
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_______ test_delete_memory_requires_confirmation[sample0-Metroid Fusion] _______
tests/test_memories_0135.py:37: in test_delete_memory_requires_confirmation
    w.delete_memory(row)
    ^^^^^^^^^^^^^^^
E   AttributeError: 'MainWindow' object has no attribute 'delete_memory'
_ test_delete_memory_requires_confirmation[sample1-Zelda: A Link to the Past] __
tests/test_memories_0135.py:37: in test_delete_memory_requires_confirmation
    w.delete_memory(row)
    ^^^^^^^^^^^^^^^
E   AttributeError: 'MainWindow' object has no attribute 'delete_memory'
_______ test_delete_memory_requires_confirmation[sample1-Metroid Fusion] _______
tests/test_memories_0135.py:37: in test_delete_memory_requires_confirmation
    w.delete_memory(row)
    ^^^^^^^^^^^^^^^
E   AttributeError: 'MainWindow' object has no attribute 'delete_memory'
=========================== short test summary info ============================
FAILED tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Metroid Fusion]
FAILED tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Zelda: A Link to the Past]
FAILED tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Metroid Fusion]
4 failed, 8 deselected in 0.49s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_memories_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
............                                                             [100%]
12 passed in 0.92s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_status_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_status_control_persists_all_choices[sample0-Zelda: A Link to the Past] __
tests/test_status_0135.py:9: in test_status_control_persists_all_choices
    assert control is not None
E   assert None is not None
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_______ test_status_control_persists_all_choices[sample0-Metroid Fusion] _______
tests/test_status_0135.py:9: in test_status_control_persists_all_choices
    assert control is not None
E   assert None is not None
_ test_status_control_persists_all_choices[sample1-Zelda: A Link to the Past] __
tests/test_status_0135.py:9: in test_status_control_persists_all_choices
    assert control is not None
E   assert None is not None
_______ test_status_control_persists_all_choices[sample1-Metroid Fusion] _______
tests/test_status_0135.py:9: in test_status_control_persists_all_choices
    assert control is not None
E   assert None is not None
=========================== short test summary info ============================
FAILED tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Zelda: A Link to the Past]
FAILED tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Metroid Fusion]
FAILED tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Zelda: A Link to the Past]
FAILED tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Metroid Fusion]
4 failed in 0.57s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_status_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.59s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_______________ test_cover_control_label_and_full_width[sample0] _______________
tests/test_settings_0135.py:10: in test_cover_control_label_and_full_width
    assert label is not None and label.text()=='Tamanho das capas'
E   assert (None is not None)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_______________ test_cover_control_label_and_full_width[sample1] _______________
tests/test_settings_0135.py:10: in test_cover_control_label_and_full_width
    assert label is not None and label.text()=='Tamanho das capas'
E   assert (None is not None)
=========================== short test summary info ============================
FAILED tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample0]
FAILED tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample1]
2 failed in 0.44s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py tests/test_layout_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
............                                                             [100%]
12 passed in 1.06s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py -k connections --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
__________________ test_connections_standard_buttons[sample0] __________________
tests/test_settings_0135.py:18: in test_connections_standard_buttons
    assert all(b.minimumWidth()==120 and b.minimumHeight()==36 for b in buttons)
E   assert False
E    +  where False = all(<generator object test_connections_standard_buttons.<locals>.<genexpr> at 0x7ff9c3e57ac0>)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
__________________ test_connections_standard_buttons[sample1] __________________
tests/test_settings_0135.py:18: in test_connections_standard_buttons
    assert all(b.minimumWidth()==120 and b.minimumHeight()==36 for b in buttons)
E   assert False
E    +  where False = all(<generator object test_connections_standard_buttons.<locals>.<genexpr> at 0x7ff9c3eac790>)
=========================== short test summary info ============================
FAILED tests/test_settings_0135.py::test_connections_standard_buttons[sample0]
FAILED tests/test_settings_0135.py::test_connections_standard_buttons[sample1]
2 failed, 2 deselected in 0.45s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py tests/test_ggdeals_connection.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.......                                                                  [100%]
7 passed in 0.75s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py -k backup --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_____________________ test_backup_action_emphasis[sample0] _____________________
tests/test_settings_0135.py:25: in test_backup_action_emphasis
    assert len(backups)==2 and all(b.objectName()=='primary' for b in backups)
E   assert (2 == 2 and False)
E    +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x3a9378d0) at 0x7f5d3f6ad8c0>, <PySide6.QtWidgets.QPushButton(0x3a94c080) at 0x7f5d3f6ae4c0>])
E    +  and   False = all(<generator object test_backup_action_emphasis.<locals>.<genexpr> at 0x7f5d3f6f4040>)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____________________ test_backup_action_emphasis[sample1] _____________________
tests/test_settings_0135.py:25: in test_backup_action_emphasis
    assert len(backups)==2 and all(b.objectName()=='primary' for b in backups)
E   assert (2 == 2 and False)
E    +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x3aa446d0) at 0x7f5d3f48e600>, <PySide6.QtWidgets.QPushButton(0x3a4befc0) at 0x7f5d3f48edc0>])
E    +  and   False = all(<generator object test_backup_action_emphasis.<locals>.<genexpr> at 0x7f5d3f6f4c70>)
=========================== short test summary info ============================
FAILED tests/test_settings_0135.py::test_backup_action_emphasis[sample0] - as...
FAILED tests/test_settings_0135.py::test_backup_action_emphasis[sample1] - as...
2 failed, 4 deselected in 0.44s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
......                                                                   [100%]
6 passed in 0.70s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_detail_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
______ test_wish_detail_only_overview[sample0-Zelda: A Link to the Past] _______
tests/test_detail_0135.py:9: in test_wish_detail_only_overview
    assert w.detail_tabs.count()==1
E   assert 4 == 1
E    +  where 4 = <built-in method count of CurrentPageTabs object at 0x7fe7d7e6d480>()
E    +    where <built-in method count of CurrentPageTabs object at 0x7fe7d7e6d480> = <checkpoint.ui_components.CurrentPageTabs(0x43bc230, name="detailTabs") at 0x7fe7d7e6d480>.count
E    +      where <checkpoint.ui_components.CurrentPageTabs(0x43bc230, name="detailTabs") at 0x7fe7d7e6d480> = <checkpoint.window.MainWindow(0x3d07eb0) at 0x7fe7d8353940>.detail_tabs
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____________ test_wish_detail_only_overview[sample0-Metroid Fusion] ____________
tests/test_detail_0135.py:9: in test_wish_detail_only_overview
    assert w.detail_tabs.count()==1
E   assert 4 == 1
E    +  where 4 = <built-in method count of CurrentPageTabs object at 0x7fe7d8144680>()
E    +    where <built-in method count of CurrentPageTabs object at 0x7fe7d8144680> = <checkpoint.ui_components.CurrentPageTabs(0x4432730, name="detailTabs") at 0x7fe7d8144680>.count
E    +      where <checkpoint.ui_components.CurrentPageTabs(0x4432730, name="detailTabs") at 0x7fe7d8144680> = <checkpoint.window.MainWindow(0x4575390) at 0x7fe7d8315580>.detail_tabs
______ test_wish_detail_only_overview[sample1-Zelda: A Link to the Past] _______
tests/test_detail_0135.py:9: in test_wish_detail_only_overview
    assert w.detail_tabs.count()==1
E   assert 4 == 1
E    +  where 4 = <built-in method count of CurrentPageTabs object at 0x7fe7d81d0640>()
E    +    where <built-in method count of CurrentPageTabs object at 0x7fe7d81d0640> = <checkpoint.ui_components.CurrentPageTabs(0x4432510, name="detailTabs") at 0x7fe7d81d0640>.count
E    +      where <checkpoint.ui_components.CurrentPageTabs(0x4432510, name="detailTabs") at 0x7fe7d81d0640> = <checkpoint.window.MainWindow(0x3f43900) at 0x7fe7d814d180>.detail_tabs
____________ test_wish_detail_only_overview[sample1-Metroid Fusion] ____________
tests/test_detail_0135.py:9: in test_wish_detail_only_overview
    assert w.detail_tabs.count()==1
E   assert 4 == 1
E    +  where 4 = <built-in method count of CurrentPageTabs object at 0x7fe7de1ec7c0>()
E    +    where <built-in method count of CurrentPageTabs object at 0x7fe7de1ec7c0> = <checkpoint.ui_components.CurrentPageTabs(0x41769a0, name="detailTabs") at 0x7fe7de1ec7c0>.count
E    +      where <checkpoint.ui_components.CurrentPageTabs(0x41769a0, name="detailTabs") at 0x7fe7de1ec7c0> = <checkpoint.window.MainWindow(0x3f49530) at 0x7fe7d8315800>.detail_tabs
=========================== short test summary info ============================
FAILED tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Zelda: A Link to the Past]
FAILED tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Metroid Fusion]
FAILED tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Zelda: A Link to the Past]
FAILED tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Metroid Fusion]
4 failed in 0.53s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_detail_0135.py tests/test_detail_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..............                                                           [100%]
14 passed in 1.20s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_banner_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
___________ test_wish_banner_fallback_preserves_proportion[sample0] ____________
tests/test_banner_0135.py:12: in test_wish_banner_fallback_preserves_proportion
    assert not wish.pixmap.isNull()
E   assert not True
E    +  where True = <built-in method isNull of PySide6.QtGui.QPixmap object at 0x7f891f8e7940>()
E    +    where <built-in method isNull of PySide6.QtGui.QPixmap object at 0x7f891f8e7940> = <PySide6.QtGui.QPixmap(null) at 0x7f891f8e7940>.isNull
E    +      where <PySide6.QtGui.QPixmap(null) at 0x7f891f8e7940> = <checkpoint.collection_views.WishLogo(0x8a291a0, name="wishLogo") at 0x7f891f8e5dc0>.pixmap
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___________ test_wish_banner_fallback_preserves_proportion[sample1] ____________
tests/test_banner_0135.py:12: in test_wish_banner_fallback_preserves_proportion
    assert not wish.pixmap.isNull()
E   assert not True
E    +  where True = <built-in method isNull of PySide6.QtGui.QPixmap object at 0x7f891f5afb00>()
E    +    where <built-in method isNull of PySide6.QtGui.QPixmap object at 0x7f891f5afb00> = <PySide6.QtGui.QPixmap(null) at 0x7f891f5afb00>.isNull
E    +      where <PySide6.QtGui.QPixmap(null) at 0x7f891f5afb00> = <checkpoint.collection_views.WishLogo(0x8719a10, name="wishLogo") at 0x7f891f5af940>.pixmap
=========================== short test summary info ============================
FAILED tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample0]
FAILED tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample1]
2 failed in 0.36s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_banner_0135.py tests/test_banner_fallback_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.55s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_wiki_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_wiki_parentheses_and_written_dates[Zelda: A Link to the Past] ______
tests/test_wiki_0135.py:7: in test_wiki_parentheses_and_written_dates
    assert '日本語' not in result and '(' not in result and ')' not in result
E   AssertionError: assert ('日本語' not in 'Zelda: A Li...is mil e um.'
E     
E     '日本語' is contained here:
E       Zelda: A Link to the Past (日本語 (nome original)) é uma aventura de exploração. Foi lançado em vinte e um de março de dois mil e um.
E     ?                            +++)
___________ test_wiki_parentheses_and_written_dates[Metroid Fusion] ____________
tests/test_wiki_0135.py:7: in test_wiki_parentheses_and_written_dates
    assert '日本語' not in result and '(' not in result and ')' not in result
E   AssertionError: assert ('日本語' not in 'Metroid Fus...is mil e um.'
E     
E     '日本語' is contained here:
E       Metroid Fusion (日本語 (nome original)) é uma aventura de exploração. Foi lançado em vinte e um de março de dois mil e um.
E     ?                 +++)
=========================== short test summary info ============================
FAILED tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Zelda: A Link to the Past]
FAILED tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Metroid Fusion]
2 failed in 0.03s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_wiki_0135.py tests/test_bugs_0134.py -k wiki --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed, 20 deselected in 0.45s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_detail_0135.py -k no_description --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_no_description_explains_and_offers_actions[sample0-Zelda: A Link to the Past] _
tests/test_detail_0135.py:21: in test_no_description_explains_and_offers_actions
    assert any('texto descritivo' in label.text() for label in w.detail_page.findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_no_description_explains_and_offers_actions.<locals>.<genexpr> at 0x7fcae1245700>)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___ test_no_description_explains_and_offers_actions[sample0-Metroid Fusion] ____
tests/test_detail_0135.py:21: in test_no_description_explains_and_offers_actions
    assert any('texto descritivo' in label.text() for label in w.detail_page.findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_no_description_explains_and_offers_actions.<locals>.<genexpr> at 0x7fcae11e2330>)
_ test_no_description_explains_and_offers_actions[sample1-Zelda: A Link to the Past] _
tests/test_detail_0135.py:21: in test_no_description_explains_and_offers_actions
    assert any('texto descritivo' in label.text() for label in w.detail_page.findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_no_description_explains_and_offers_actions.<locals>.<genexpr> at 0x7fcae1246e90>)
___ test_no_description_explains_and_offers_actions[sample1-Metroid Fusion] ____
tests/test_detail_0135.py:21: in test_no_description_explains_and_offers_actions
    assert any('texto descritivo' in label.text() for label in w.detail_page.findChildren(QLabel))
E   assert False
E    +  where False = any(<generator object test_no_description_explains_and_offers_actions.<locals>.<genexpr> at 0x7fcadfd345f0>)
=========================== short test summary info ============================
FAILED tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Zelda: A Link to the Past]
FAILED tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Metroid Fusion]
FAILED tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Zelda: A Link to the Past]
FAILED tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Metroid Fusion]
4 failed, 4 deselected in 0.54s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_detail_0135.py tests/test_bugs_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..............................                                           [100%]
30 passed in 2.11s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest /workspace/work/test_prices_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_______________ test_official_default[Zelda: A Link to the Past] _______________
../test_prices_0135.py:11: in test_official_default
    assert display_snapshot(lib,lib.get(i))['lowest']==2000
E   assert 1000 == 2000
____________________ test_official_default[Metroid Fusion] _____________________
../test_prices_0135.py:11: in test_official_default
    assert display_snapshot(lib,lib.get(i))['lowest']==2000
E   assert 1000 == 2000
=========================== short test summary info ============================
FAILED ../test_prices_0135.py::test_official_default[Zelda: A Link to the Past]
FAILED ../test_prices_0135.py::test_official_default[Metroid Fusion] - assert...
2 failed in 0.13s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_capture_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
___ test_capture_belongs_to_launched_game[sample0-Zelda: A Link to the Past] ___
tests/test_capture_0135.py:7: in test_capture_belongs_to_launched_game
    from checkpoint.game_capture import capture_game
E   ModuleNotFoundError: No module named 'checkpoint.game_capture'
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
________ test_capture_belongs_to_launched_game[sample0-Metroid Fusion] _________
tests/test_capture_0135.py:7: in test_capture_belongs_to_launched_game
    from checkpoint.game_capture import capture_game
E   ModuleNotFoundError: No module named 'checkpoint.game_capture'
___ test_capture_belongs_to_launched_game[sample1-Zelda: A Link to the Past] ___
tests/test_capture_0135.py:7: in test_capture_belongs_to_launched_game
    from checkpoint.game_capture import capture_game
E   ModuleNotFoundError: No module named 'checkpoint.game_capture'
________ test_capture_belongs_to_launched_game[sample1-Metroid Fusion] _________
tests/test_capture_0135.py:7: in test_capture_belongs_to_launched_game
    from checkpoint.game_capture import capture_game
E   ModuleNotFoundError: No module named 'checkpoint.game_capture'
=========================== short test summary info ============================
FAILED tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Zelda: A Link to the Past]
FAILED tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Metroid Fusion]
FAILED tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Zelda: A Link to the Past]
FAILED tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Metroid Fusion]
4 failed in 0.47s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_capture_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.42s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_steam_installations_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_____________ test_discover_steam_multiple_libraries[620-Portal 2] _____________
tests/test_steam_installations_0135.py:4: in test_discover_steam_multiple_libraries
    from checkpoint.steam_installations import find_executables
E   ModuleNotFoundError: No module named 'checkpoint.steam_installations'
______________ test_discover_steam_multiple_libraries[400-Portal] ______________
tests/test_steam_installations_0135.py:4: in test_discover_steam_multiple_libraries
    from checkpoint.steam_installations import find_executables
E   ModuleNotFoundError: No module named 'checkpoint.steam_installations'
=========================== short test summary info ============================
FAILED tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[620-Portal 2]
FAILED tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[400-Portal]
2 failed in 0.02s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_steam_installations_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.02s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_tabs_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_drag_does_not_select_tab_but_click_and_key_do[sample0-Zelda: A Link to the Past] _
tests/test_tabs_0135.py:12: in test_drag_does_not_select_tab_but_click_and_key_do
    assert tabs.currentIndex()==0
E   assert 1 == 0
E    +  where 1 = <built-in method currentIndex of CurrentPageTabs object at 0x7f5c0fb5d000>()
E    +    where <built-in method currentIndex of CurrentPageTabs object at 0x7f5c0fb5d000> = <checkpoint.ui_components.CurrentPageTabs(0xbe469c0, name="detailTabs") at 0x7f5c0fb5d000>.currentIndex
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
__ test_drag_does_not_select_tab_but_click_and_key_do[sample0-Metroid Fusion] __
tests/test_tabs_0135.py:12: in test_drag_does_not_select_tab_but_click_and_key_do
    assert tabs.currentIndex()==0
E   assert 1 == 0
E    +  where 1 = <built-in method currentIndex of CurrentPageTabs object at 0x7f5c15d9d000>()
E    +    where <built-in method currentIndex of CurrentPageTabs object at 0x7f5c15d9d000> = <checkpoint.ui_components.CurrentPageTabs(0xbfd3260, name="detailTabs") at 0x7f5c15d9d000>.currentIndex
_ test_drag_does_not_select_tab_but_click_and_key_do[sample1-Zelda: A Link to the Past] _
tests/test_tabs_0135.py:12: in test_drag_does_not_select_tab_but_click_and_key_do
    assert tabs.currentIndex()==0
E   assert 1 == 0
E    +  where 1 = <built-in method currentIndex of CurrentPageTabs object at 0x7f5c15f1d000>()
E    +    where <built-in method currentIndex of CurrentPageTabs object at 0x7f5c15f1d000> = <checkpoint.ui_components.CurrentPageTabs(0xbd7f430, name="detailTabs") at 0x7f5c15f1d000>.currentIndex
__ test_drag_does_not_select_tab_but_click_and_key_do[sample1-Metroid Fusion] __
tests/test_tabs_0135.py:12: in test_drag_does_not_select_tab_but_click_and_key_do
    assert tabs.currentIndex()==0
E   assert 1 == 0
E    +  where 1 = <built-in method currentIndex of CurrentPageTabs object at 0x7f5c0fb5e980>()
E    +    where <built-in method currentIndex of CurrentPageTabs object at 0x7f5c0fb5e980> = <checkpoint.ui_components.CurrentPageTabs(0xbfe2810, name="detailTabs") at 0x7f5c0fb5e980>.currentIndex
=========================== short test summary info ============================
FAILED tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Zelda: A Link to the Past]
FAILED tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Metroid Fusion]
FAILED tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Zelda: A Link to the Past]
FAILED tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Metroid Fusion]
4 failed in 0.66s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_tabs_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.55s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
________ test_daily_local_preserves_raw_utc[Zelda: A Link to the Past] _________
tests/test_dates_0135.py:7: in test_daily_local_preserves_raw_utc
    assert library.stats(display_timezone=ZoneInfo('America/Sao_Paulo'))['daily']=={'2026-11-14':600}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   TypeError: Library.stats() got an unexpected keyword argument 'display_timezone'
______________ test_daily_local_preserves_raw_utc[Metroid Fusion] ______________
tests/test_dates_0135.py:7: in test_daily_local_preserves_raw_utc
    assert library.stats(display_timezone=ZoneInfo('America/Sao_Paulo'))['daily']=={'2026-11-14':600}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   TypeError: Library.stats() got an unexpected keyword argument 'display_timezone'
=========================== short test summary info ============================
FAILED tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Zelda: A Link to the Past]
FAILED tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Metroid Fusion]
2 failed in 0.04s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py tests/test_wishlist_prices.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.....F..                                                                 [100%]
=================================== FAILURES ===================================
_______ test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips ________
tests/test_wishlist_prices.py:67: in test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
    assert chart is not None and chart.values==daily and len(chart.cells)==365
E   AssertionError: assert (<checkpoint.activity_heatmap.ActivityHeatmap(0x2e03d530) at 0x7f3bf38e21c0> is not None and {'2026-11-13': 3600.0} == {'2026-11-13'...1-14': 1800.0}
E     
E     Differing items:
E     {'2026-11-13': 3600.0} != {'2026-11-13': 1800.0}
E     Right contains 1 more item:
E     {'2026-11-14': 1800.0}
E     Use -v to get more diff)
=========================== short test summary info ============================
FAILED tests/test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
1 failed, 7 passed in 0.93s
```

stderr:
```text
```

Código de saída: 1

## Execução autorizada e base reconfirmada

O dono respondeu “Pode seguir com a execução do PLANO_0135”. Aprovações específicas: item 4, soma em XhXXmin com teste explícito contra duplicação; item 3, teto 360 px, arte 1:1 e mais colunas. Nenhuma outra asserção autorizada nesse momento. Branch criada do HEAD remoto reconfirmado e inalterado: af1d3ab56492cba56b541ddb971759d9c15b015b. Nenhum push, tag, release, PR ou workflow disparado.

Item 16: após conflito apresentado, dono respondeu “Autorizar a atualização dessas expectativas” para tests/test_prices_0129.py::test_wishlist_name_price_sort_and_scroll_survive_refresh: omitir desconto/preço original e exigir origem oficial por padrão, com opção keyshops. Há pedido separado pendente para fixtures não classificadas de outros três testes; não autorizado implicitamente.

## Item 20 — evidência anterior à proposta de correção

Banco isolado de teste, sem acesso ao banco pessoal do dono. A origem do registro real do PC não foi confirmada. Consulta usada: SELECT id,game_id,started_at,ended_at,duration_seconds,state FROM play_sessions WHERE game_id=? (para cada um dos dois jogos). A gravação real do app em library.now() usa datetime.now(timezone.utc).isoformat(); os valores desta prova foram inseridos explicitamente em UTC. Library.stats() converte para UTC antes de separar os dias; statistics_view.build_statistics repassa stats['daily'] a ActivityHeatmap, que usa a chave como data do calendário.

stdout integral da prova (python, exit 0; stderr vazio):
```text
Zelda: A Link to the Past {'id': 1, 'game_id': 1, 'started_at': '2026-11-15T00:30:00+00:00', 'ended_at': '2026-11-15T00:40:00+00:00', 'duration_seconds': 600, 'state': 'finished'}
started_at interpretado: 2026-11-14T21:30:00-03:00
Metroid Fusion {'id': 2, 'game_id': 2, 'started_at': '2026-11-15T00:30:00+00:00', 'ended_at': '2026-11-15T00:40:00+00:00', 'duration_seconds': 600, 'state': 'finished'}
started_at interpretado: 2026-11-14T21:30:00-03:00
Library.stats daily enviado à tela: {'2026-11-15': 1200.0}
```

Evidência mostrada no chat antes da proposta: converter somente apresentação/agrupamento local, sem regravar instantes. O executor usa UTC−3. O teste antigo do calendário exige igualdade com agrupamento UTC e entrou em conflito; solicitada aprovação específica para adaptar cenário à meia-noite local e comparação local, mantendo 1800+1800 segundos e 365 células. Aguardando decisão; não contornar contrato.

## Limitações já identificadas

Item 2: processo do emulador passa a ser monitorado; o serviço legado com monitor=False continua com encerramento explícito, como exige seu teste existente. Fechar apenas a ROM mantendo o processo aberto não tem sinal validado nos perfis atuais. Esse subcaso está bloqueado, não entregue. O aviso e ação manual existentes permanecem; não declarar o item inteiro resolvido.

Item 17: a captura foi testada só em Linux com adaptador controlado. A captura real no Windows não foi validada; o primeiro uso real será no PC do dono. Enumeração por PID é conservadora e recusa múltiplas janelas. Jogos com processo-filho, renderização exclusiva, janela minimizada ou captura bloqueada podem exigir adaptação após evidência real. Não se assume validação Windows por testes Qt offscreen.

Preparação do ambiente: Python 3.12.14, requirements-tested.txt e instalação editável em venv isolado. Uma regressão de ambiente em test_emulator_arguments_no_shell comparava sys.executable ao caminho resolvido de um symlink do venv. Resolvida copiando o binário Python para o venv; nenhuma asserção foi alterada.

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_banner_render_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past] _______
tests/test_banner_render_0135.py:14: in test_hero_keeps_top_and_bottom_borders
    assert top.red()>0 and top.green()>0 and top.blue()==0
E   assert (5 > 0 and 7 > 0 and 114 == 0)
E    +  where 5 = <built-in method red of PySide6.QtGui.QColor object at 0x7f83c59acd80>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f83c59acd80> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).red
E    +  and   7 = <built-in method green of PySide6.QtGui.QColor object at 0x7f83c59acd80>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f83c59acd80> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).green
E    +  and   114 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f83c59acd80>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f83c59acd80> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).blue
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
____________ test_hero_keeps_top_and_bottom_borders[Metroid Fusion] ____________
tests/test_banner_render_0135.py:14: in test_hero_keeps_top_and_bottom_borders
    assert top.red()>0 and top.green()>0 and top.blue()==0
E   assert (5 > 0 and 7 > 0 and 114 == 0)
E    +  where 5 = <built-in method red of PySide6.QtGui.QColor object at 0x7f83c59f9300>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f83c59f9300> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).red
E    +  and   7 = <built-in method green of PySide6.QtGui.QColor object at 0x7f83c59f9300>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f83c59f9300> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).green
E    +  and   114 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f83c59f9300>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f83c59f9300> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).blue
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past]
FAILED tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Metroid Fusion]
2 failed in 0.17s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_banner_render_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past] _______
tests/test_banner_render_0135.py:14: in test_hero_keeps_top_and_bottom_borders
    assert top.red()>top.blue() and top.green()>top.blue()
E   assert (5 > 114)
E    +  where 5 = <built-in method red of PySide6.QtGui.QColor object at 0x7f38a1b25000>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f38a1b25000> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).red
E    +  and   114 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f38a1b25000>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f38a1b25000> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).blue
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
____________ test_hero_keeps_top_and_bottom_borders[Metroid Fusion] ____________
tests/test_banner_render_0135.py:14: in test_hero_keeps_top_and_bottom_borders
    assert top.red()>top.blue() and top.green()>top.blue()
E   assert (5 > 114)
E    +  where 5 = <built-in method red of PySide6.QtGui.QColor object at 0x7f38a1b55f40>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f38a1b55f40> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).red
E    +  and   114 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f38a1b55f40>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f38a1b55f40> = PySide6.QtGui.QColor.fromRgbF(0.019608, 0.027451, 0.447059, 1.000000).blue
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past]
FAILED tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Metroid Fusion]
2 failed in 0.16s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest /workspace/work/base0135/tests/test_banner_render_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.14s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_sessions_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_ test_rom_session_finishes_after_real_process_exit[Zelda: A Link to the Past-SNES-.sfc] _
tests/test_sessions_0135.py:21: in test_rom_session_finishes_after_real_process_exit
    assert w.launcher.poll()==[game]
E   assert [] == [1]
E     
E     Right contains one more item: 1
E     Use -v to get more diff
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
__ test_rom_session_finishes_after_real_process_exit[Metroid Fusion-GBA-.gba] __
tests/test_sessions_0135.py:21: in test_rom_session_finishes_after_real_process_exit
    assert w.launcher.poll()==[game]
E   assert [] == [1]
E     
E     Right contains one more item: 1
E     Use -v to get more diff
=========================== short test summary info ============================
FAILED tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Zelda: A Link to the Past-SNES-.sfc]
FAILED tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Metroid Fusion-GBA-.gba]
2 failed in 0.34s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest /workspace/work/base0135/tests/test_sessions_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.37s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........................................................................ [ 14%]
........................................................................ [ 29%]
........................................................................ [ 44%]
........................................................................ [ 59%]
................F....................................................... [ 74%]
....F................................................................... [ 89%]
.................................................F..                     [100%]
=================================== FAILURES ===================================
__________ test_activity_summary_uses_singular_day_and_brazilian_date __________
tests/test_registration_0128.py:107: in test_activity_summary_uses_singular_day_and_brazilian_date
    assert '1,0 h em 1 dia de jogo' in [call.args[-1] for call in painter.drawText.call_args_list]
E   AssertionError: assert '1,0 h em 1 dia de jogo' in ['Nov', 'Dez', 'Jan', 'Fev', 'Mar', 'Abr', ...]
___ test_dialog_async_query_selection_import_achievements_and_account_change ___
tests/test_steam.py:213: in test_dialog_async_query_selection_import_achievements_and_account_change
    assert any('2.0 h na Steam' in text for text in texts)
E   assert False
E    +  where False = any(<generator object test_dialog_async_query_selection_import_achievements_and_account_change.<locals>.<genexpr> at 0x7f94832c58a0>)
_______ test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips ________
tests/test_wishlist_prices.py:67: in test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
    assert chart is not None and chart.values==daily and len(chart.cells)==365
E   AssertionError: assert (<checkpoint.activity_heatmap.ActivityHeatmap(0x42fb0350) at 0x7f9482936940> is not None and {'2026-11-13': 3600.0} == {'2026-11-13'...1-14': 1800.0}
E     
E     Differing items:
E     {'2026-11-13': 3600.0} != {'2026-11-13': 1800.0}
E     Right contains 1 more item:
E     {'2026-11-14': 1800.0}
E     Use -v to get more diff)
=========================== short test summary info ============================
FAILED tests/test_registration_0128.py::test_activity_summary_uses_singular_day_and_brazilian_date
FAILED tests/test_steam.py::test_dialog_async_query_selection_import_achievements_and_account_change
FAILED tests/test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
3 failed, 481 passed in 336.25s (0:05:36)
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py tests/test_wishlist_prices.py tests/test_registration_0128.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
...............                                                          [100%]
15 passed in 1.55s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_prices_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_______________ test_official_default[Zelda: A Link to the Past] _______________
tests/test_prices_0135.py:11: in test_official_default
    assert display_snapshot(lib,lib.get(i))['lowest']==2000
E   assert 1000 == 2000
____________________ test_official_default[Metroid Fusion] _____________________
tests/test_prices_0135.py:11: in test_official_default
    assert display_snapshot(lib,lib.get(i))['lowest']==2000
E   assert 1000 == 2000
____ test_unknown_cache_is_not_an_official_offer[Zelda: A Link to the Past] ____
tests/test_prices_0135.py:18: in test_unknown_cache_is_not_an_official_offer
    assert display_snapshot(library,library.get(i)).get('lowest') is None
E   AssertionError: assert 1000 is None
E    +  where 1000 = <built-in method get of dict object at 0x7f0bf2de54c0>('lowest')
E    +    where <built-in method get of dict object at 0x7f0bf2de54c0> = {'lowest': 1000, 'currency': 'BRL'}.get
E    +      where {'lowest': 1000, 'currency': 'BRL'} = display_snapshot(<checkpoint.library.Library object at 0x7f0bf2d56090>, {'id': 1, 'title': 'Zelda: A Link to the Past', 'description': '', 'developer': '', ...})
E    +        where {'id': 1, 'title': 'Zelda: A Link to the Past', 'description': '', 'developer': '', ...} = get(1)
E    +          where get = <checkpoint.library.Library object at 0x7f0bf2d56090>.get
_________ test_unknown_cache_is_not_an_official_offer[Metroid Fusion] __________
tests/test_prices_0135.py:18: in test_unknown_cache_is_not_an_official_offer
    assert display_snapshot(library,library.get(i)).get('lowest') is None
E   AssertionError: assert 1000 is None
E    +  where 1000 = <built-in method get of dict object at 0x7f0bf2de75c0>('lowest')
E    +    where <built-in method get of dict object at 0x7f0bf2de75c0> = {'lowest': 1000, 'currency': 'BRL'}.get
E    +      where {'lowest': 1000, 'currency': 'BRL'} = display_snapshot(<checkpoint.library.Library object at 0x7f0bf2d57cb0>, {'id': 1, 'title': 'Metroid Fusion', 'description': '', 'developer': '', ...})
E    +        where {'id': 1, 'title': 'Metroid Fusion', 'description': '', 'developer': '', ...} = get(1)
E    +          where get = <checkpoint.library.Library object at 0x7f0bf2d57cb0>.get
=========================== short test summary info ============================
FAILED tests/test_prices_0135.py::test_official_default[Zelda: A Link to the Past]
FAILED tests/test_prices_0135.py::test_official_default[Metroid Fusion] - ass...
FAILED tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Zelda: A Link to the Past]
FAILED tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Metroid Fusion]
4 failed in 0.18s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_prices_0135.py tests/test_prices_0129.py tests/test_price_display_official.py tests/test_time_prices_0134.py tests/test_bugs_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.....................................                                    [100%]
37 passed in 3.11s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_banner_render_0135.py tests/test_sessions_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.40s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_sessions_0135.py tests/test_launch_0135.py tests/test_services.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
...............                                                          [100%]
15 passed in 0.96s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_registration_0128.py tests/test_steam.py tests/test_time_0135.py tests/test_home_0129.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
............................                                             [100%]
28 passed in 1.71s
```

stderr:
```text
```

Código de saída: 0

## Capturas Qt com fixtures

Comando: /workspace/work/venv/bin/python scripts/render_ui_review.py /workspace/work/ui0135 --reference-sizes

stdout:
```text
/workspace/work/ui0135
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_logo_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past] ______
tests/test_service_logo_0135.py:20: in test_steam_logo_occupancy_matches_drive
    assert steam[0]>=5 and steam[1]>=5
E   assert (0 >= 5)
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
___________ test_steam_logo_occupancy_matches_drive[Metroid Fusion] ____________
tests/test_service_logo_0135.py:20: in test_steam_logo_occupancy_matches_drive
    assert steam[0]>=5 and steam[1]>=5
E   assert (0 >= 5)
=========================== short test summary info ============================
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past]
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Metroid Fusion]
2 failed in 0.40s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_logo_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past] ______
tests/test_service_logo_0135.py:20: in test_steam_logo_occupancy_matches_drive
    assert steam[0]>=5 and steam[1]>=5
E   assert (0 >= 5)
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
___________ test_steam_logo_occupancy_matches_drive[Metroid Fusion] ____________
tests/test_service_logo_0135.py:20: in test_steam_logo_occupancy_matches_drive
    assert steam[0]>=5 and steam[1]>=5
E   assert (0 >= 5)
=========================== short test summary info ============================
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past]
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Metroid Fusion]
2 failed in 0.42s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_logo_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past] ______
tests/test_service_logo_0135.py:21: in test_steam_logo_occupancy_matches_drive
    assert steam[2]<=drive[2]+2 and steam[3]<=drive[3]+2
E   assert (35 <= (34 + 2) and 36 <= (30 + 2))
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
___________ test_steam_logo_occupancy_matches_drive[Metroid Fusion] ____________
tests/test_service_logo_0135.py:21: in test_steam_logo_occupancy_matches_drive
    assert steam[2]<=drive[2]+2 and steam[3]<=drive[3]+2
E   assert (35 <= (34 + 2) and 36 <= (30 + 2))
=========================== short test summary info ============================
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past]
FAILED tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Metroid Fusion]
2 failed in 0.52s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_logo_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.50s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_branding_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.18s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_service_branding_0135.py tests/test_service_logo_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.50s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........................................................................ [ 14%]
........................................................................ [ 29%]
........................................................................ [ 43%]
........................................................................ [ 58%]
........................................................................ [ 73%]
........................................................................ [ 87%]
............................................................             [100%]
492 passed in 340.49s (0:05:40)
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_space_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_appearance_uses_window_and_cover_preview[sample0-Zelda: A Link to the Past] _
tests/test_settings_space_0135.py:9: in test_appearance_uses_window_and_cover_preview
    assert content.width()>w.width()-198-12
E   assert 1440 > ((1920 - 198) - 12)
E    +  where 1440 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b834240>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b834240> = <PySide6.QtWidgets.QWidget(0x393eafe0, name="mainContent") at 0x7fbe0b834240>.width
E    +  and   1920 = <built-in method width of MainWindow object at 0x7fbe0b9bd280>()
E    +    where <built-in method width of MainWindow object at 0x7fbe0b9bd280> = <checkpoint.window.MainWindow(0x38d0a0d0) at 0x7fbe0b9bd280>.width
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_appearance_uses_window_and_cover_preview[sample0-Metroid Fusion] _____
tests/test_settings_space_0135.py:9: in test_appearance_uses_window_and_cover_preview
    assert content.width()>w.width()-198-12
E   assert 1440 > ((1920 - 198) - 12)
E    +  where 1440 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0959ff40>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0959ff40> = <PySide6.QtWidgets.QWidget(0x39991da0, name="mainContent") at 0x7fbe0959ff40>.width
E    +  and   1920 = <built-in method width of MainWindow object at 0x7fbe095ad680>()
E    +    where <built-in method width of MainWindow object at 0x7fbe095ad680> = <checkpoint.window.MainWindow(0x3928dbf0) at 0x7fbe095ad680>.width
_ test_appearance_uses_window_and_cover_preview[sample1-Zelda: A Link to the Past] _
tests/test_settings_space_0135.py:9: in test_appearance_uses_window_and_cover_preview
    assert content.width()>w.width()-198-12
E   assert 1440 > ((1920 - 198) - 12)
E    +  where 1440 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b4d1fc0>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b4d1fc0> = <PySide6.QtWidgets.QWidget(0x39718720, name="mainContent") at 0x7fbe0b4d1fc0>.width
E    +  and   1920 = <built-in method width of MainWindow object at 0x7fbe0b809940>()
E    +    where <built-in method width of MainWindow object at 0x7fbe0b809940> = <checkpoint.window.MainWindow(0x3927bc20) at 0x7fbe0b809940>.width
____ test_appearance_uses_window_and_cover_preview[sample1-Metroid Fusion] _____
tests/test_settings_space_0135.py:9: in test_appearance_uses_window_and_cover_preview
    assert content.width()>w.width()-198-12
E   assert 1440 > ((1920 - 198) - 12)
E    +  where 1440 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b5429c0>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fbe0b5429c0> = <PySide6.QtWidgets.QWidget(0x394d4400, name="mainContent") at 0x7fbe0b5429c0>.width
E    +  and   1920 = <built-in method width of MainWindow object at 0x7fbe0b9bcd80>()
E    +    where <built-in method width of MainWindow object at 0x7fbe0b9bcd80> = <checkpoint.window.MainWindow(0x399f21f0) at 0x7fbe0b9bcd80>.width
=========================== short test summary info ============================
FAILED tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Zelda: A Link to the Past]
FAILED tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Metroid Fusion]
FAILED tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Zelda: A Link to the Past]
FAILED tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Metroid Fusion]
4 failed in 0.60s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_settings_space_0135.py tests/test_settings_0135.py tests/test_layout_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....................                                                     [100%]
20 passed in 1.88s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_complements_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
____ test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past] _____
tests/test_visual_complements_0135.py:9: in test_visual_a_no_official_offer_has_reason
    labels=[label.text() for label in price_summary(library,library.get(i)).findChildren(QLabel)]
            ^^^^^^^^^^^^
E   RuntimeError: Internal C++ object (PySide6.QtWidgets.QLabel) already deleted.
__________ test_visual_a_no_official_offer_has_reason[Metroid Fusion] __________
tests/test_visual_complements_0135.py:9: in test_visual_a_no_official_offer_has_reason
    labels=[label.text() for label in price_summary(library,library.get(i)).findChildren(QLabel)]
            ^^^^^^^^^^^^
E   RuntimeError: Internal C++ object (PySide6.QtWidgets.QLabel) already deleted.
=========================== short test summary info ============================
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past]
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Metroid Fusion]
2 failed in 0.13s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_complements_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
____ test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past] _____
tests/test_visual_complements_0135.py:12: in test_visual_a_no_official_offer_has_reason
    assert 'Consulta sem oferta em lojas oficiais.' in labels
E   AssertionError: assert 'Consulta sem oferta em lojas oficiais.' in ['Menor preço atual', 'Sem preço salvo', 'Preços ainda não consultados.']
__________ test_visual_a_no_official_offer_has_reason[Metroid Fusion] __________
tests/test_visual_complements_0135.py:12: in test_visual_a_no_official_offer_has_reason
    assert 'Consulta sem oferta em lojas oficiais.' in labels
E   AssertionError: assert 'Consulta sem oferta em lojas oficiais.' in ['Menor preço atual', 'Sem preço salvo', 'Preços ainda não consultados.']
=========================== short test summary info ============================
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past]
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Metroid Fusion]
2 failed in 0.14s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_complements_0135.py tests/test_prices_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........                                                                 [100%]
8 passed in 0.20s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_steam_asset_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..                                                                       [100%]
2 passed in 0.14s
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_steam_asset_0135.py tests/test_service_branding_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
....                                                                     [100%]
4 passed in 0.18s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_status_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Zelda: A Link to the Past] _
tests/test_visual_status_0135.py:16: in test_visual_c_five_statuses_highlight_current_without_rewriting_legacy
    assert font is not None and font.bold()==(combo.itemText(n)==name)
E   assert (None is not None)
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Metroid Fusion] _
tests/test_visual_status_0135.py:16: in test_visual_c_five_statuses_highlight_current_without_rewriting_legacy
    assert font is not None and font.bold()==(combo.itemText(n)==name)
E   assert (None is not None)
_ test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Zelda: A Link to the Past] _
tests/test_visual_status_0135.py:16: in test_visual_c_five_statuses_highlight_current_without_rewriting_legacy
    assert font is not None and font.bold()==(combo.itemText(n)==name)
E   assert (None is not None)
_ test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Metroid Fusion] _
tests/test_visual_status_0135.py:16: in test_visual_c_five_statuses_highlight_current_without_rewriting_legacy
    assert font is not None and font.bold()==(combo.itemText(n)==name)
E   assert (None is not None)
=========================== short test summary info ============================
FAILED tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Zelda: A Link to the Past]
FAILED tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Metroid Fusion]
FAILED tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Zelda: A Link to the Past]
FAILED tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Metroid Fusion]
4 failed in 0.57s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_visual_status_0135.py tests/test_status_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........                                                                 [100%]
8 passed in 0.88s
```

stderr:
```text
```

Código de saída: 0

## Capturas após itens 21–22 e correção adicional 9

Comando: /workspace/work/venv/bin/python scripts/render_ui_review.py /workspace/work/ui0135-ajustes --reference-sizes

stdout:
```text
/workspace/work/ui0135-ajustes
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_mockup_exclusions_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_mockup_extras_are_absent_and_theme_cards_work[sample0-Zelda: A Link to the Past] _
tests/test_mockup_exclusions_0135.py:10: in test_mockup_extras_are_absent_and_theme_cards_work
    assert not w.theme_selector.isVisible()
E   assert not True
E    +  where True = <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f7140>()
E    +    where <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f7140> = <PySide6.QtWidgets.QComboBox(0x35c4d2a0, name="themeSelector") at 0x7ff33c5f7140>.isVisible
E    +      where <PySide6.QtWidgets.QComboBox(0x35c4d2a0, name="themeSelector") at 0x7ff33c5f7140> = <checkpoint.window.MainWindow(0x353abd60) at 0x7ff33cb17d80>.theme_selector
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
__ test_mockup_extras_are_absent_and_theme_cards_work[sample0-Metroid Fusion] __
tests/test_mockup_exclusions_0135.py:10: in test_mockup_extras_are_absent_and_theme_cards_work
    assert not w.theme_selector.isVisible()
E   assert not True
E    +  where True = <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f7a40>()
E    +    where <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f7a40> = <PySide6.QtWidgets.QComboBox(0x35e212c0, name="themeSelector") at 0x7ff33c5f7a40>.isVisible
E    +      where <PySide6.QtWidgets.QComboBox(0x35e212c0, name="themeSelector") at 0x7ff33c5f7a40> = <checkpoint.window.MainWindow(0x357c8e50) at 0x7ff33cb17e40>.theme_selector
_ test_mockup_extras_are_absent_and_theme_cards_work[sample1-Zelda: A Link to the Past] _
tests/test_mockup_exclusions_0135.py:10: in test_mockup_extras_are_absent_and_theme_cards_work
    assert not w.theme_selector.isVisible()
E   assert not True
E    +  where True = <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c86ab00>()
E    +    where <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c86ab00> = <PySide6.QtWidgets.QComboBox(0x35674d80, name="themeSelector") at 0x7ff33c86ab00>.isVisible
E    +      where <PySide6.QtWidgets.QComboBox(0x35674d80, name="themeSelector") at 0x7ff33c86ab00> = <checkpoint.window.MainWindow(0x35792a80) at 0x7ff339e86ac0>.theme_selector
__ test_mockup_extras_are_absent_and_theme_cards_work[sample1-Metroid Fusion] __
tests/test_mockup_exclusions_0135.py:10: in test_mockup_extras_are_absent_and_theme_cards_work
    assert not w.theme_selector.isVisible()
E   assert not True
E    +  where True = <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f6680>()
E    +    where <built-in method isVisible of PySide6.QtWidgets.QComboBox object at 0x7ff33c5f6680> = <PySide6.QtWidgets.QComboBox(0x35f70000, name="themeSelector") at 0x7ff33c5f6680>.isVisible
E    +      where <PySide6.QtWidgets.QComboBox(0x35f70000, name="themeSelector") at 0x7ff33c5f6680> = <checkpoint.window.MainWindow(0x35aa01a0) at 0x7ff339e8ea00>.theme_selector
=========================== short test summary info ============================
FAILED tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Zelda: A Link to the Past]
FAILED tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Metroid Fusion]
FAILED tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Zelda: A Link to the Past]
FAILED tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Metroid Fusion]
4 failed in 0.63s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........................................................................ [ 14%]
........................................................................ [ 28%]
........................................................................ [ 43%]
..............F......................................................... [ 57%]
........................................................................ [ 72%]
........................................................................ [ 86%]
....................................................................     [100%]
=================================== FAILURES ===================================
___________________ test_sidebar_and_page_bounds_at_full_hd ____________________
tests/test_layout_regressions_025.py:34: in test_sidebar_and_page_bounds_at_full_hd
    assert window.header_widget.width()<=1392
E   assert 1674 <= 1392
E    +  where 1674 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f9210ba7c80>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f9210ba7c80> = <PySide6.QtWidgets.QWidget(0x35d32f60) at 0x7f9210ba7c80>.width
E    +      where <PySide6.QtWidgets.QWidget(0x35d32f60) at 0x7f9210ba7c80> = <checkpoint.window.MainWindow(0x354027a0) at 0x7f9210cc43c0>.header_widget
=========================== short test summary info ============================
FAILED tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
1 failed, 499 passed in 339.28s (0:05:39)
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_mockup_exclusions_0135.py tests/test_themes.py tests/test_layout_0134.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
...........................                                              [100%]
27 passed in 14.51s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_mockup_exclusions_0135.py tests/test_layout_regressions_025.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
......F...                                                               [100%]
=================================== FAILURES ===================================
___________________ test_sidebar_and_page_bounds_at_full_hd ____________________
tests/test_layout_regressions_025.py:35: in test_sidebar_and_page_bounds_at_full_hd
    assert window.header_widget.width()>=700
E   assert 435 >= 700
E    +  where 435 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f982abba2c0>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f982abba2c0> = <PySide6.QtWidgets.QWidget(0x384932d0) at 0x7f982abba2c0>.width
E    +      where <PySide6.QtWidgets.QWidget(0x384932d0) at 0x7f982abba2c0> = <checkpoint.window.MainWindow(0x380e7470) at 0x7f982abec840>.header_widget
=========================== short test summary info ============================
FAILED tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
1 failed, 9 passed in 9.17s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_mockup_exclusions_0135.py tests/test_layout_regressions_025.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
......F...                                                               [100%]
=================================== FAILURES ===================================
___________________ test_sidebar_and_page_bounds_at_full_hd ____________________
tests/test_layout_regressions_025.py:35: in test_sidebar_and_page_bounds_at_full_hd
    assert window.header_widget.width()>=700
E   assert 204 >= 700
E    +  where 204 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f32cd58d140>()
E    +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f32cd58d140> = <PySide6.QtWidgets.QWidget(0x576f0e0) at 0x7f32cd58d140>.width
E    +      where <PySide6.QtWidgets.QWidget(0x576f0e0) at 0x7f32cd58d140> = <checkpoint.window.MainWindow(0x4f81370) at 0x7f32cd576600>.header_widget
=========================== short test summary info ============================
FAILED tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
1 failed, 9 passed in 8.26s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_mockup_exclusions_0135.py tests/test_layout_regressions_025.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..........                                                               [100%]
10 passed in 9.89s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_cover_preview_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFFFFFF                                                                 [100%]
=================================== FAILURES ===================================
_ test_preview_stays_right_with_common_base_and_active_value[sample0-70-size0] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_preview_stays_right_with_common_base_and_active_value[sample0-70-size1] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample0-150-size0] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample0-150-size1] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample1-70-size0] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample1-70-size1] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample1-150-size0] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
_ test_preview_stays_right_with_common_base_and_active_value[sample1-150-size1] _
tests/test_cover_preview_0135.py:12: in test_preview_stays_right_with_common_base_and_active_value
    rectangles=preview.cover_rects()
               ^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'CoverSizePreview' object has no attribute 'cover_rects'
=========================== short test summary info ============================
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-70-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-70-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-150-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-150-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-70-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-70-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-150-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-150-size1]
8 failed in 1.26s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_cover_preview_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFFFFFF                                                                 [100%]
=================================== FAILURES ===================================
_ test_preview_stays_right_with_common_base_and_active_value[sample0-70-size0] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (20 > 14 and 20 > 29)
E    +  where 20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862915a040>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862915a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   14 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862915a040>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862915a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E    +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862915a040>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862915a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   29 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862915a040>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862915a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).blue
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_preview_stays_right_with_common_base_and_active_value[sample0-70-size1] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (20 > 14 and 20 > 29)
E    +  where 20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f8629175480>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f8629175480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   14 = <built-in method red of PySide6.QtGui.QColor object at 0x7f8629175480>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f8629175480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E    +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f8629175480>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f8629175480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   29 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f8629175480>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f8629175480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample0-150-size0] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (35 > 25 and 35 > 48)
E    +  where 35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862916d480>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862916d480> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   25 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862916d480>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862916d480> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).red
E    +  and   35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862916d480>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862916d480> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   48 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862916d480>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862916d480> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample0-150-size1] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (35 > 25 and 35 > 48)
E    +  where 35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862bbbd980>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862bbbd980> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   25 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862bbbd980>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862bbbd980> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).red
E    +  and   35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862bbbd980>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862bbbd980> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   48 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862bbbd980>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862bbbd980> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample1-70-size0] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (20 > 14 and 20 > 29)
E    +  where 20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862920a040>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862920a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   14 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862920a040>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862920a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E    +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862920a040>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862920a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   29 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862920a040>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862920a040> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample1-70-size1] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (20 > 14 and 20 > 29)
E    +  where 20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862b8f24c0>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862b8f24c0> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   14 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862b8f24c0>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862b8f24c0> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E    +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862b8f24c0>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862b8f24c0> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green
E    +  and   29 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862b8f24c0>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862b8f24c0> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample1-150-size0] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (35 > 25 and 35 > 48)
E    +  where 35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862bb55c80>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862bb55c80> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   25 = <built-in method red of PySide6.QtGui.QColor object at 0x7f862bb55c80>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f862bb55c80> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).red
E    +  and   35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f862bb55c80>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f862bb55c80> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   48 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f862bb55c80>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f862bb55c80> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).blue
_ test_preview_stays_right_with_common_base_and_active_value[sample1-150-size1] _
tests/test_cover_preview_0135.py:15: in test_preview_stays_right_with_common_base_and_active_value
    assert color.green()>color.red() and color.green()>color.blue()
E   assert (35 > 25 and 35 > 48)
E    +  where 35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f8631c1f400>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f8631c1f400> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   25 = <built-in method red of PySide6.QtGui.QColor object at 0x7f8631c1f400>()
E    +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f8631c1f400> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).red
E    +  and   35 = <built-in method green of PySide6.QtGui.QColor object at 0x7f8631c1f400>()
E    +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f8631c1f400> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).green
E    +  and   48 = <built-in method blue of PySide6.QtGui.QColor object at 0x7f8631c1f400>()
E    +    where <built-in method blue of PySide6.QtGui.QColor object at 0x7f8631c1f400> = PySide6.QtGui.QColor.fromRgbF(0.098039, 0.137255, 0.188235, 1.000000).blue
=========================== short test summary info ============================
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-70-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-70-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-150-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample0-150-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-70-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-70-size1]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-150-size0]
FAILED tests/test_cover_preview_0135.py::test_preview_stays_right_with_common_base_and_active_value[sample1-150-size1]
8 failed in 1.09s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_cover_preview_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........                                                                 [100%]
8 passed in 1.20s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_interface_text_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
F....FFF....FF                                                           [100%]
=================================== FAILURES ===================================
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-0] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'}
E    +  where {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'} = <built-in method intersection of set object at 0x7ff57aa38120>(['', 'Escolha seu próximo jogo', 'Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui.', 'Na sua biblioteca', 'Jogos prontos para a sua próxima escolha.', 'Sua atividade', ...])
E    +    where <built-in method intersection of set object at 0x7ff57aa38120> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-5] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...}
E    +  where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...} = <built-in method intersection of set object at 0x7ff578a18740>(['', 'Biblioteca', 'Seu banco de jogos e suas preferências.', '', 'Saves tradicionais', 'Cópias de segurança dos saves configurados.', ...])
E    +    where <built-in method intersection of set object at 0x7ff578a18740> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-6] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'}
E    +  where {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'} = <built-in method intersection of set object at 0x7ff578a1b140>(['Aurora', '●', 'Tempo jogado: 0h00min', 'Arquivos e versões', '', 'Nenhuma ROM associada', ...])
E    +    where <built-in method intersection of set object at 0x7ff578a1b140> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-0] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'}
E    +  where {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'} = <built-in method intersection of set object at 0x7ff578a1b5a0>(['', 'Escolha seu próximo jogo', 'Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui.', 'Na sua biblioteca', 'Jogos prontos para a sua próxima escolha.', 'Sua atividade', ...])
E    +    where <built-in method intersection of set object at 0x7ff578a1b5a0> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-5] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...}
E    +  where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...} = <built-in method intersection of set object at 0x7ff578a1b220>(['', 'Biblioteca', 'Seu banco de jogos e suas preferências.', '', 'Saves tradicionais', 'Cópias de segurança dos saves configurados.', ...])
E    +    where <built-in method intersection of set object at 0x7ff578a1b220> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-6] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'}
E    +  where {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'} = <built-in method intersection of set object at 0x7ff578a1a960>(['Horizonte', '●', 'Tempo jogado: 0h00min', 'Arquivos e versões', '', 'Nenhuma ROM associada', ...])
E    +    where <built-in method intersection of set object at 0x7ff578a1a960> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
=========================== short test summary info ============================
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-0]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-5]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-6]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-0]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-5]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-6]
6 failed, 8 passed in 1.13s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_interface_text_0135.py tests/test_detail_0135.py tests/test_memories_0135.py tests/test_prices_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
F....FFF....FF........................                                   [100%]
=================================== FAILURES ===================================
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-0] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'}
E    +  where {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'} = <built-in method intersection of set object at 0x7f10dc8ba340>(['', 'Escolha seu próximo jogo', 'Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui.', 'Na sua biblioteca', 'Jogos prontos para a sua próxima escolha.', 'Sua atividade', ...])
E    +    where <built-in method intersection of set object at 0x7f10dc8ba340> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-5] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...}
E    +  where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...} = <built-in method intersection of set object at 0x7f10d661f5a0>(['', 'Biblioteca', 'Seu banco de jogos e suas preferências.', '', 'Saves tradicionais', 'Cópias de segurança dos saves configurados.', ...])
E    +    where <built-in method intersection of set object at 0x7f10d661f5a0> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample0-6] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'}
E    +  where {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'} = <built-in method intersection of set object at 0x7f10d415a0a0>(['Aurora', '●', 'Tempo jogado: 0h00min', 'Arquivos e versões', '', 'Nenhuma ROM associada', ...])
E    +    where <built-in method intersection of set object at 0x7f10d415a0a0> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-0] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'}
E    +  where {'Conquistas, sessões e memórias recentes.', 'Jogos prontos para a sua próxima escolha.', 'Suas sessões, conquistas e anotações aparecerão aqui.'} = <built-in method intersection of set object at 0x7f10d415a500>(['', 'Escolha seu próximo jogo', 'Abra a biblioteca e marque um jogo como Jogando para tê-lo em destaque aqui.', 'Na sua biblioteca', 'Jogos prontos para a sua próxima escolha.', 'Sua atividade', ...])
E    +    where <built-in method intersection of set object at 0x7f10d415a500> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-5] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...}
E    +  where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Consulte as versões dis...anha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Serviços para completar fichas, imagens e arquivos.', ...} = <built-in method intersection of set object at 0x7f10d661f680>(['', 'Biblioteca', 'Seu banco de jogos e suas preferências.', '', 'Saves tradicionais', 'Cópias de segurança dos saves configurados.', ...])
E    +    where <built-in method intersection of set object at 0x7f10d661f680> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
____ test_interface_has_only_labels_data_and_actionable_absence[sample1-6] _____
tests/test_interface_text_0135.py:30: in test_interface_has_only_labels_data_and_actionable_absence
    assert not set(REMOVED).intersection(texts)
E   AssertionError: assert not {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'}
E    +  where {'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', 'O tempo jogado aparece aqui quando você inicia um jogo pelo Checkpoint.', 'Os arquivos e as versões vinculadas a este jogo aparecem aqui.'} = <built-in method intersection of set object at 0x7f10d4159d20>(['Horizonte', '●', 'Tempo jogado: 0h00min', 'Arquivos e versões', '', 'Nenhuma ROM associada', ...])
E    +    where <built-in method intersection of set object at 0x7f10d4159d20> = {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...}.intersection
E    +      where {'Com o Checkpoint em primeiro plano, salva a janela do jogo iniciado pelo app em Memórias.', 'Conquistas, sessões e m...ança dos saves configurados.', 'Guarde conquistas e objetivos pessoais deste jogo.', 'Guarde suas melhores cenas', ...} = set(('O tema acompanha todas as páginas. Ajuste abaixo o tamanho das capas.', 'Com o Checkpoint em primeiro plano, salva a...s.', 'Cópias de segurança dos saves configurados.', 'Consulte as versões disponíveis sem alterar sua biblioteca.', ...))
=========================== short test summary info ============================
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-0]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-5]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-6]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-0]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-5]
FAILED tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-6]
6 failed, 32 passed in 2.44s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_interface_text_0135.py tests/test_detail_0135.py tests/test_memories_0135.py tests/test_prices_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
......................................                                   [100%]
38 passed in 2.30s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_interface_text_0135.py tests/test_bugs_0134.py tests/test_ggdeals_connection.py tests/test_home_0129.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
..........................................                               [100%]
42 passed in 2.42s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_cover_preview_0135.py tests/test_interface_text_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
......................                                                   [100%]
22 passed in 1.81s
```

stderr:
```text
```

Código de saída: 0

## Autorizações complementares recebidas

Item 16: autorizadas fixtures explicitamente oficiais, preservando as verificações de valor/cache, em test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence, test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price e test_price_display_official.py::test_price_order_places_missing_prices_last_and_respects_name. Acrescentada cobertura contra cache sem origem. Item 20: autorizada a fixture de meia-noite local em test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips, preservando 1800+1800 segundos e 365 células. Item 4: autorizadas somente as trocas textuais 2.0 h na Steam -> 2h00min na Steam e 1,0 h em 1 dia de jogo -> 1h00min em 1 dia de jogo nos testes Steam/registration indicados no chat.

O dono confirmou o arquivo steam.ico mostrado antes da alteração. Itens 21–22 foram acrescentados, sem reescrever os commits já feitos. O item 22 e complemento B são preservação de requisito que já passava antes; não foi fabricada falha. Correção adicional do item 9 após 22 expressamente autorizada. Complementos visuais A/B/C, exclusões de mockup, posição da prévia e regra de texto foram acrescentados em novos commits ao fim da fila.

Rodadas executadas em worktrees isolados: base0135 contém af1d3ab (reprodução adicional de processo real e bordas de banner); logo0135 parte de d462321 e contém somente 21–22; complement0135 parte de 335d537 e contém os complementos novos. Os comandos de pytest acima com seus mesmos nomes de arquivo foram executados primeiro nesses diretórios de reprodução e depois no checkout corrigido; os stdout/stderr/códigos estão integralmente preservados. A incorporação à branch principal foi fast-forward, preservando os commits anteriores.

Correções de montagem de testes novos, sem relaxar asserções antigas: renderização de bordas passou a comparar predominância de cor, pois a sobreposição do banner altera os canais RGB; um teste de preço passou a manter referência ao QWidget pai, evitando destruição de seus QLabel pelo Qt; a prévia passou a ser amostrada por pixel antes de chamar o método novo, para demonstrar o defeito visual na base. O primeiro teste de grade de Desejos não atingia a largura real pretendida; a fixture passou a redimensionar explicitamente o grid, mantendo o teto e a regra de colunas.

Após ampliar Configurações, a suíte detectou quebra do limite anterior do cabeçalho em test_layout_regressions_025. O código restaurou os limites derivados do layout anterior, sem alterar a asserção. Mensagens, cabeçalho e identidade foram preservados, sem acrescentar elementos de mockup.

## Capturas após todos os complementos visuais e regra de texto

Comando: /workspace/work/venv/bin/python scripts/render_ui_review.py /workspace/work/ui0135-final --reference-sizes

stdout:
```text
/workspace/work/ui0135-final
```

stderr:
```text
Fontconfig error: No writable cache directories
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 40%]
........................................................................ [ 53%]
........................................................................ [ 67%]
........................................................................ [ 80%]
........................................................................ [ 94%]
..FFF...........................                                         [100%]
=================================== FAILURES ===================================
____________ test_empty_pages_have_title_description_and_action[0] _____________
tests/test_visual_0132.py:107: in test_empty_pages_have_title_description_and_action
    assert len(frame.findChild(QLabel,'emptyDescription').text())>20
E   assert 17 > 20
E    +  where 17 = len('Adicione um jogo.')
E    +    where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7f4425a97740>()
E    +      where <built-in method text of FullTextLabel object at 0x7f4425a97740> = <checkpoint.ui_components.FullTextLabel(0x1eb04430, name="emptyDescription") at 0x7f4425a97740>.text
E    +        where <checkpoint.ui_components.FullTextLabel(0x1eb04430, name="emptyDescription") at 0x7f4425a97740> = <built-in method findChild of CardSurface object at 0x7f4425a96b80>(QLabel, 'emptyDescription')
E    +          where <built-in method findChild of CardSurface object at 0x7f4425a96b80> = <checkpoint.design_system.CardSurface(0x2c0b2a50, name="emptyState") at 0x7f4425a96b80>.findChild
____________ test_empty_pages_have_title_description_and_action[1] _____________
tests/test_visual_0132.py:107: in test_empty_pages_have_title_description_and_action
    assert len(frame.findChild(QLabel,'emptyDescription').text())>20
E   assert 17 > 20
E    +  where 17 = len('Adicione um jogo.')
E    +    where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7f4425fa09c0>()
E    +      where <built-in method text of FullTextLabel object at 0x7f4425fa09c0> = <checkpoint.ui_components.FullTextLabel(0x1c1b0610, name="emptyDescription") at 0x7f4425fa09c0>.text
E    +        where <checkpoint.ui_components.FullTextLabel(0x1c1b0610, name="emptyDescription") at 0x7f4425fa09c0> = <built-in method findChild of CardSurface object at 0x7f4425fa3180>(QLabel, 'emptyDescription')
E    +          where <built-in method findChild of CardSurface object at 0x7f4425fa3180> = <checkpoint.design_system.CardSurface(0x2c7a62f0, name="emptyState") at 0x7f4425fa3180>.findChild
____________ test_empty_pages_have_title_description_and_action[2] _____________
tests/test_visual_0132.py:107: in test_empty_pages_have_title_description_and_action
    assert len(frame.findChild(QLabel,'emptyDescription').text())>20
E   assert 19 > 20
E    +  where 19 = len('Adicione um desejo.')
E    +    where 'Adicione um desejo.' = <built-in method text of FullTextLabel object at 0x7f4425f43240>()
E    +      where <built-in method text of FullTextLabel object at 0x7f4425f43240> = <checkpoint.ui_components.FullTextLabel(0x32e19c30, name="emptyDescription") at 0x7f4425f43240>.text
E    +        where <checkpoint.ui_components.FullTextLabel(0x32e19c30, name="emptyDescription") at 0x7f4425f43240> = <built-in method findChild of CardSurface object at 0x7f4425f43000>(QLabel, 'emptyDescription')
E    +          where <built-in method findChild of CardSurface object at 0x7f4425f43000> = <checkpoint.design_system.CardSurface(0x1645e610, name="emptyState") at 0x7f4425f43000>.findChild
=========================== short test summary info ============================
FAILED tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[0]
FAILED tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[1]
FAILED tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[2]
3 failed, 533 passed in 352.29s (0:05:52)
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_empty_copy_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
FFFFFF                                                                   [100%]
=================================== FAILURES ===================================
_ test_empty_state_identifies_destination_and_keeps_action[sample0-0-biblioteca] _
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('biblioteca' in 'Adicione um jogo.')
E    +  where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7ff5a0adc840>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a0adc840> = <checkpoint.ui_components.FullTextLabel(0x36b701c0, name="emptyDescription") at 0x7ff5a0adc840>.text
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_empty_state_identifies_destination_and_keeps_action[sample0-1-biblioteca] _
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('biblioteca' in 'Adicione um jogo.')
E    +  where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7ff5a0adfe00>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a0adfe00> = <checkpoint.ui_components.FullTextLabel(0x36abf330, name="emptyDescription") at 0x7ff5a0adfe00>.text
_ test_empty_state_identifies_destination_and_keeps_action[sample0-2-desejos] __
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('desejos' in 'Adicione um desejo.')
E    +  where 'Adicione um desejo.' = <built-in method text of FullTextLabel object at 0x7ff5a0b253c0>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a0b253c0> = <checkpoint.ui_components.FullTextLabel(0x36bf1030, name="emptyDescription") at 0x7ff5a0b253c0>.text
_ test_empty_state_identifies_destination_and_keeps_action[sample1-0-biblioteca] _
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('biblioteca' in 'Adicione um jogo.')
E    +  where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7ff5a0b4a8c0>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a0b4a8c0> = <checkpoint.ui_components.FullTextLabel(0x36c2ecd0, name="emptyDescription") at 0x7ff5a0b4a8c0>.text
_ test_empty_state_identifies_destination_and_keeps_action[sample1-1-biblioteca] _
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('biblioteca' in 'Adicione um jogo.')
E    +  where 'Adicione um jogo.' = <built-in method text of FullTextLabel object at 0x7ff5a20ea340>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a20ea340> = <checkpoint.ui_components.FullTextLabel(0x36f50dd0, name="emptyDescription") at 0x7ff5a20ea340>.text
_ test_empty_state_identifies_destination_and_keeps_action[sample1-2-desejos] __
tests/test_empty_copy_0135.py:11: in test_empty_state_identifies_destination_and_keeps_action
    assert destination in frame.text() and len(frame.text())>20
E   assert ('desejos' in 'Adicione um desejo.')
E    +  where 'Adicione um desejo.' = <built-in method text of FullTextLabel object at 0x7ff5a0b48900>()
E    +    where <built-in method text of FullTextLabel object at 0x7ff5a0b48900> = <checkpoint.ui_components.FullTextLabel(0x36cc6c50, name="emptyDescription") at 0x7ff5a0b48900>.text
=========================== short test summary info ============================
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-0-biblioteca]
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-1-biblioteca]
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-2-desejos]
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-0-biblioteca]
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-1-biblioteca]
FAILED tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-2-desejos]
6 failed in 0.53s
```

stderr:
```text
```

Código de saída: 1

## Comando: /workspace/work/venv/bin/python -m pytest tests/test_empty_copy_0135.py tests/test_visual_0132.py tests/test_interface_text_0135.py --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

stdout:
```text
.............................................................            [100%]
61 passed in 4.12s
```

stderr:
```text
```

Código de saída: 0

## Comando: /workspace/work/venv/bin/python -m pytest tests --tb=short -q -p no:cacheprovider

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp

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

Código de saída: 0

## Fechamento e diagnósticos finais

Uma tentativa de preparação do ajuste de texto ocorreu antes da criação do script: comando python /workspace/work/apply_text0135.py, stdout vazio, stderr integral:
```text
python: can't open file '/workspace/work/apply_text0135.py': [Errno 2] No such file or directory
```
Código de saída 2. O teste seguinte ainda representava o estado anterior; seu stdout integral está preservado acima. O script foi criado e a rodada de correção foi executada depois.

A rodada anterior à última falhou em três estados vazios porque descrições de 17/19 caracteres não atendiam o contrato existente do teste visual. Nenhum teste protegido foi alterado: a ação passou a identificar o destino (biblioteca/desejos), de forma direta e sem apoio decorativo. A reprodução em duas fixtures e o módulo protegido estão registrados integralmente antes da suíte definitiva.

Auditoria final contra a base, stdout integral (script Python, stderr vazio, exit 0):
```json
{
  "arquivos_protegidos_alterados": [],
  "arquivos_modificados_com_CRLF": [],
  "read_text_write_text_sem_encoding": [],
  "patches_completos": 30
}
```

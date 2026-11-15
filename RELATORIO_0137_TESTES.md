# Testes 0.1.37 — registros integrais

Ambiente: Linux, Python 3.12.14, PySide6 6.8.3, QT_QPA_PLATFORM=offscreen, CHECKPOINT_TEST_ROOT=/tmp. Dados isolados; sem conta autenticada. Resultados da 0.1.36 são históricos e não substituem esta rodada. Comandos, stdout, stderr e códigos de saída serão acrescentados integralmente.

## base-regressoes

UTC: 2026-11-15T21:22:29.280017+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_favorite_0136.py", "tests/test_wish_navigation_0136.py", "tests/test_price_integrity_0136.py", "tests/test_capture_0136.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..........................                                               [100%]
26 passed in 1.98s

```

stderr integral:
```text

```

Código de saída: 0

## rotulos-antes

UTC: 2026-11-15T21:23:09.193158+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_labels_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFFFF                                                                   [100%]
=================================== FAILURES ===================================
__ test_not_started_label_keeps_legacy_data_on_open[sample0-N\xe3o iniciado] ___

ui = (<checkpoint.window.MainWindow(0x326f3060) at 0x7fa30da57dc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x3265d950) at 0x7fa30dbd2640>
stored = 'Não iniciado'

    @pytest.mark.parametrize('stored', ['Não iniciado', 'Backlog'])
    def test_not_started_label_keeps_legacy_data_on_open(ui, app, stored):
        w, identity = ui
        w.library.save_game({'title': w.library.get(identity)['title'], 'status': stored}, identity)
        w.detail(identity); app.processEvents()
        control = w.detail_page.findChild(QComboBox, 'gameStatus')
>       assert [control.itemText(i) for i in range(control.count())] == [
            'Não iniciado', 'Jogando', 'Pausado', 'Concluído', 'Abandonado']
E       AssertionError: assert ['Backlog', '... 'Abandonado'] == ['Não iniciad... 'Abandonado']
E         
E         At index 0 diff: 'Backlog' != 'Não iniciado'
E         Use -v to get more diff

tests/test_labels_0137.py:12: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_not_started_label_keeps_legacy_data_on_open[sample0-Backlog] _______

ui = (<checkpoint.window.MainWindow(0x32ff6550) at 0x7fa30dbe9000>, 1)
app = <PySide6.QtWidgets.QApplication(0x3265d950) at 0x7fa30dbd2640>
stored = 'Backlog'

    @pytest.mark.parametrize('stored', ['Não iniciado', 'Backlog'])
    def test_not_started_label_keeps_legacy_data_on_open(ui, app, stored):
        w, identity = ui
        w.library.save_game({'title': w.library.get(identity)['title'], 'status': stored}, identity)
        w.detail(identity); app.processEvents()
        control = w.detail_page.findChild(QComboBox, 'gameStatus')
>       assert [control.itemText(i) for i in range(control.count())] == [
            'Não iniciado', 'Jogando', 'Pausado', 'Concluído', 'Abandonado']
E       AssertionError: assert ['Backlog', '... 'Abandonado'] == ['Não iniciad... 'Abandonado']
E         
E         At index 0 diff: 'Backlog' != 'Não iniciado'
E         Use -v to get more diff

tests/test_labels_0137.py:12: AssertionError
__ test_not_started_label_keeps_legacy_data_on_open[sample1-N\xe3o iniciado] ___

ui = (<checkpoint.window.MainWindow(0x32e1c5e0) at 0x7fa30d6243c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x3265d950) at 0x7fa30dbd2640>
stored = 'Não iniciado'

    @pytest.mark.parametrize('stored', ['Não iniciado', 'Backlog'])
    def test_not_started_label_keeps_legacy_data_on_open(ui, app, stored):
        w, identity = ui
        w.library.save_game({'title': w.library.get(identity)['title'], 'status': stored}, identity)
        w.detail(identity); app.processEvents()
        control = w.detail_page.findChild(QComboBox, 'gameStatus')
>       assert [control.itemText(i) for i in range(control.count())] == [
            'Não iniciado', 'Jogando', 'Pausado', 'Concluído', 'Abandonado']
E       AssertionError: assert ['Backlog', '... 'Abandonado'] == ['Não iniciad... 'Abandonado']
E         
E         At index 0 diff: 'Backlog' != 'Não iniciado'
E         Use -v to get more diff

tests/test_labels_0137.py:12: AssertionError
______ test_not_started_label_keeps_legacy_data_on_open[sample1-Backlog] _______

ui = (<checkpoint.window.MainWindow(0x32e51690) at 0x7fa30c105fc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x3265d950) at 0x7fa30dbd2640>
stored = 'Backlog'

    @pytest.mark.parametrize('stored', ['Não iniciado', 'Backlog'])
    def test_not_started_label_keeps_legacy_data_on_open(ui, app, stored):
        w, identity = ui
        w.library.save_game({'title': w.library.get(identity)['title'], 'status': stored}, identity)
        w.detail(identity); app.processEvents()
        control = w.detail_page.findChild(QComboBox, 'gameStatus')
>       assert [control.itemText(i) for i in range(control.count())] == [
            'Não iniciado', 'Jogando', 'Pausado', 'Concluído', 'Abandonado']
E       AssertionError: assert ['Backlog', '... 'Abandonado'] == ['Não iniciad... 'Abandonado']
E         
E         At index 0 diff: 'Backlog' != 'Não iniciado'
E         Use -v to get more diff

tests/test_labels_0137.py:12: AssertionError
__________ test_period_and_sort_labels_keep_underlying_keys[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x32ff65d0) at 0x7fa30d643c80>, 1)

    def test_period_and_sort_labels_keep_underlying_keys(ui):
        from checkpoint.statistics_periods import PERIODS
        w, _ = ui
>       assert PERIODS[:3] == (('Hoje', 'daily'), ('Esta semana', 'weekly'), ('Este mês', 'monthly'))
E       AssertionError: assert (('Diário', '...', 'monthly')) == (('Hoje', 'da...', 'monthly'))
E         
E         At index 0 diff: ('Diário', 'daily') != ('Hoje', 'daily')
E         Use -v to get more diff

tests/test_labels_0137.py:24: AssertionError
__________ test_period_and_sort_labels_keep_underlying_keys[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x32c912b0) at 0x7fa30d642c80>, 1)

    def test_period_and_sort_labels_keep_underlying_keys(ui):
        from checkpoint.statistics_periods import PERIODS
        w, _ = ui
>       assert PERIODS[:3] == (('Hoje', 'daily'), ('Esta semana', 'weekly'), ('Este mês', 'monthly'))
E       AssertionError: assert (('Diário', '...', 'monthly')) == (('Hoje', 'da...', 'monthly'))
E         
E         At index 0 diff: ('Diário', 'daily') != ('Hoje', 'daily')
E         Use -v to get more diff

tests/test_labels_0137.py:24: AssertionError
=========================== short test summary info ============================
FAILED tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-N\xe3o iniciado]
FAILED tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-Backlog]
FAILED tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-N\xe3o iniciado]
FAILED tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-Backlog]
FAILED tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample0]
FAILED tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample1]
6 failed in 0.64s

```

stderr integral:
```text

```

Código de saída: 1

## rotulos-depois

UTC: 2026-11-15T21:23:35.434645+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_labels_0137.py", "tests/test_status_0135.py", "tests/test_visual_status_0135.py", "tests/test_status_pill_0136.py", "tests/test_statistics_0136.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..........................                                               [100%]
26 passed in 2.53s

```

stderr integral:
```text

```

Código de saída: 0

## inicio-dados-antes

UTC: 2026-11-15T21:24:45.226571+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_data_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
______ test_recent_games_use_real_start_not_status_or_updated_at[titles0] ______

library = <checkpoint.library.Library object at 0x7fb815e4e540>
titles = ('Portal 2', 'Hades')

    @pytest.mark.parametrize('titles', [('Portal 2', 'Hades'), ('Celeste', 'Metroid Fusion')])
    def test_recent_games_use_real_start_not_status_or_updated_at(library, titles):
>       from checkpoint.home_data import recent_games, execution_history
E       ModuleNotFoundError: No module named 'checkpoint.home_data'

tests/test_home_data_0137.py:13: ModuleNotFoundError
______ test_recent_games_use_real_start_not_status_or_updated_at[titles1] ______

library = <checkpoint.library.Library object at 0x7fb815e4dbb0>
titles = ('Celeste', 'Metroid Fusion')

    @pytest.mark.parametrize('titles', [('Portal 2', 'Hades'), ('Celeste', 'Metroid Fusion')])
    def test_recent_games_use_real_start_not_status_or_updated_at(library, titles):
>       from checkpoint.home_data import recent_games, execution_history
E       ModuleNotFoundError: No module named 'checkpoint.home_data'

tests/test_home_data_0137.py:13: ModuleNotFoundError
_____ test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed _____

library = <checkpoint.library.Library object at 0x7fb815e4ff50>

    def test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed(library):
>       from checkpoint.home_data import week_summary
E       ModuleNotFoundError: No module named 'checkpoint.home_data'

tests/test_home_data_0137.py:30: ModuleNotFoundError
_ test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache __

library = <checkpoint.library.Library object at 0x7fb815cbb5f0>

    def test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache(library):
>       from checkpoint.home_data import wish_offers
E       ModuleNotFoundError: No module named 'checkpoint.home_data'

tests/test_home_data_0137.py:47: ModuleNotFoundError
=========================== short test summary info ============================
FAILED tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles0]
FAILED tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles1]
FAILED tests/test_home_data_0137.py::test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed
FAILED tests/test_home_data_0137.py::test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache
4 failed in 0.07s

```

stderr integral:
```text

```

Código de saída: 1

## inicio-dados-depois

UTC: 2026-11-15T21:25:53.876739+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_data_0137.py", "tests/test_statistics_0136.py", "tests/test_price_integrity_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
......................                                                   [100%]
22 passed in 1.37s

```

stderr integral:
```text

```

Código de saída: 0

## capturas-antes

UTC: 2026-11-15T21:26:32.940654+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/antes"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/antes

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-primeira-captura

UTC: 2026-11-15T21:30:14.502311+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-capas-captura

UTC: 2026-11-15T21:32:17.137345+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-capas-v2"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-capas-v2

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-capas-alinhadas

UTC: 2026-11-15T21:33:15.304214+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-capas-v3"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-capas-v3

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-ofertas-lista

UTC: 2026-11-15T21:34:17.585108+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-ofertas-v4"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-ofertas-v4

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-layout-depois

UTC: 2026-11-15T21:34:44.708206+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_layout_0137.py", "tests/test_home_data_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
............                                                             [100%]
12 passed in 1.25s

```

stderr integral:
```text

```

Código de saída: 0

## inicio-regressoes

UTC: 2026-11-15T21:35:27.817677+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_reference_layout_0128.py", "tests/test_home_layout_0137.py", "tests/test_favorite_0136.py", "tests/test_wish_navigation_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...F.....................                                                [100%]
=================================== FAILURES ===================================
______ test_home_does_not_paint_description_but_detail_keeps_it[sample0] _______

ui = (<checkpoint.window.MainWindow(0x28652830) at 0x7f4f91a22c00>, 1)
app = <PySide6.QtWidgets.QApplication(0x28da7cb0) at 0x7f4f934ad940>

    def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
        w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
        w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
        from datetime import datetime,timezone
        with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(i,datetime.now(timezone.utc).isoformat()))
        w.navigate(0);app.processEvents();hero=w.pages[0].findChild(RecentArtwork)
        assert hero and w.pages[0].findChild(RecentGameCard).findChildren(QPushButton)
        before=hero.grab().toImage();hero.game={**hero.game,'description':''};hero.update();app.processEvents()
>       assert before==hero.grab().toImage()
E       assert <PySide6.QtGui.QImage(QSize(374, 180),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=1496,sizeInBytes=269280) at 0x7f4f93294f40> == <PySide6.QtGui.QImage(QSize(680, 180),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2720,sizeInBytes=489600) at 0x7f4f919bf9c0>
E        +  where <PySide6.QtGui.QImage(QSize(680, 180),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2720,sizeInBytes=489600) at 0x7f4f919bf9c0> = <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7f4f919a58c0>()
E        +    where <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7f4f919a58c0> = <PySide6.QtGui.QPixmap(QSize(680, 180),depth=32,devicePixelRatio=1,cacheKey=0x3b00000003) at 0x7f4f919a58c0>.toImage
E        +      where <PySide6.QtGui.QPixmap(QSize(680, 180),depth=32,devicePixelRatio=1,cacheKey=0x3b00000003) at 0x7f4f919a58c0> = <built-in method grab of RecentArtwork object at 0x7f4f919ed440>()
E        +        where <built-in method grab of RecentArtwork object at 0x7f4f919ed440> = <checkpoint.home_components.RecentArtwork(0x2a5c07c0, name="recentGameArtwork") at 0x7f4f919ed440>.grab

tests/test_home_description_0136.py:14: AssertionError
=========================== short test summary info ============================
FAILED tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample0]
1 failed, 24 passed in 3.51s

```

stderr integral:
```text

```

Código de saída: 1

## inicio-carrossel-tres

UTC: 2026-11-15T21:36:41.533798+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-carrossel-v5"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-carrossel-v5

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-ofertas-no-topo

UTC: 2026-11-15T21:37:41.950483+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-ofertas-v6"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-ofertas-v6

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-capas-regressoes

UTC: 2026-11-15T21:38:38.520480+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_layout_0137.py", "tests/test_home_data_0137.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_reference_layout_0128.py", "tests/test_favorite_0136.py", "tests/test_wish_navigation_0136.py", "tests/test_ui_review_lifecycle_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
................................                                         [100%]
32 passed in 13.31s

```

stderr integral:
```text

```

Código de saída: 0

## inicio-ofertas-logos

UTC: 2026-11-15T21:39:07.906832+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-ofertas-v7"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-ofertas-v7

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-informacoes-uma-linha

UTC: 2026-11-15T21:40:22.093211+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-v8"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-v8

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-final-regressoes

UTC: 2026-11-15T21:40:47.024465+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_layout_0137.py", "tests/test_home_data_0137.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_reference_layout_0128.py", "tests/test_favorite_0136.py", "tests/test_wish_navigation_0136.py", "tests/test_ui_review_lifecycle_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.................................                                        [100%]
33 passed in 13.09s

```

stderr integral:
```text

```

Código de saída: 0

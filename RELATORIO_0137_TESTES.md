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

## grade-benchmark-antes

UTC: 2026-11-15T21:42:25.073092+00:00

Comando: `["/workspace/work/venv/bin/python", "/workspace/work/evidence-0137/bench_grid.py", "/workspace/work/evidence-0137/bench-antes"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
{
  "games": 500,
  "distinct_images": 100,
  "image_size": [
    300,
    450
  ],
  "window": [
    1280,
    800
  ],
  "initialization_seconds": 1.746569217000797,
  "refresh_seconds": [
    0.7873271179996664,
    0.7594353940003202,
    0.7884724640025524
  ],
  "refresh_sql_statements": [
    10,
    10,
    10
  ],
  "frame_seconds": [
    0.01957371000025887,
    0.03425789999892004,
    0.03018155500103603,
    0.0337869690010848,
    0.03296220199990785,
    0.024321164000866702,
    0.02194282900018152,
    0.03249420499923872,
    0.033179494999785675,
    0.022936576999200042,
    0.02425610099817277,
    0.03297773500162293,
    0.03478646899748128,
    0.022543536997545743,
    0.023715177998383297,
    0.022761446998629253
  ],
  "median_frame_ms": 27.251359500951366,
  "scroll_before_refresh": 25693,
  "scroll_after_refresh": 25693,
  "max_rss_kib": 389916
}

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## inicio-ofertas-quatro-campos

UTC: 2026-11-15T21:44:23.612878+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-v9"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-v9

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## inicio-ofertas-dados-confiaveis

UTC: 2026-11-15T21:44:33.286775+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_layout_0137.py", "tests/test_home_data_0137.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.....................                                                    [100%]
21 passed in 1.92s

```

stderr integral:
```text

```

Código de saída: 0

## lista-antes

UTC: 2026-11-15T21:45:33.759998+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_library_list_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_____ test_horizontal_list_has_logo_time_and_independent_favorite[sample0] _____

ui = (<checkpoint.window.MainWindow(0x1df0f300) at 0x7f28524d7c00>, 1)
app = <PySide6.QtWidgets.QApplication(0x1e2479d0) at 0x7f2852648e40>
folder = PosixPath('/tmp/bd0d6442c689451ca7861e7d8474ad87')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f2852667920>

    def test_horizontal_list_has_logo_time_and_independent_favorite(ui,app,folder,monkeypatch):
>       from checkpoint.library_list import LibraryList
E       ModuleNotFoundError: No module named 'checkpoint.library_list'

tests/test_library_list_0137.py:9: ModuleNotFoundError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_horizontal_list_has_logo_time_and_independent_favorite[sample1] _____

ui = (<checkpoint.window.MainWindow(0x1e0c0420) at 0x7f28524a6ac0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1e2479d0) at 0x7f2852648e40>
folder = PosixPath('/tmp/2ffb6bd1a727407bbe1230c839507132')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f2851feb770>

    def test_horizontal_list_has_logo_time_and_independent_favorite(ui,app,folder,monkeypatch):
>       from checkpoint.library_list import LibraryList
E       ModuleNotFoundError: No module named 'checkpoint.library_list'

tests/test_library_list_0137.py:9: ModuleNotFoundError
____________ test_list_search_and_sort_preserve_filtering[sample0] _____________

ui = (<checkpoint.window.MainWindow(0x1e445440) at 0x7f2851fe2740>, 1)
app = <PySide6.QtWidgets.QApplication(0x1e2479d0) at 0x7f2852648e40>

    def test_list_search_and_sort_preserve_filtering(ui,app):
        w,i=ui;j=w.library.save_game({'title':'ZZZ Segundo jogo','favorite':1})
        w.navigate(1);w.view.setCurrentIndex(1);app.processEvents()
>       assert w.game_list.count()==2
               ^^^^^^^^^^^
E       AttributeError: 'MainWindow' object has no attribute 'game_list'

tests/test_library_list_0137.py:38: AttributeError
____________ test_list_search_and_sort_preserve_filtering[sample1] _____________

ui = (<checkpoint.window.MainWindow(0x1e4eda80) at 0x7f2851ff5c00>, 1)
app = <PySide6.QtWidgets.QApplication(0x1e2479d0) at 0x7f2852648e40>

    def test_list_search_and_sort_preserve_filtering(ui,app):
        w,i=ui;j=w.library.save_game({'title':'ZZZ Segundo jogo','favorite':1})
        w.navigate(1);w.view.setCurrentIndex(1);app.processEvents()
>       assert w.game_list.count()==2
               ^^^^^^^^^^^
E       AttributeError: 'MainWindow' object has no attribute 'game_list'

tests/test_library_list_0137.py:38: AttributeError
=========================== short test summary info ============================
FAILED tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample0]
FAILED tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample1]
FAILED tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample0]
FAILED tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample1]
4 failed in 0.53s

```

stderr integral:
```text

```

Código de saída: 1

## lista-depois

UTC: 2026-11-15T21:46:17.953195+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_library_list_0137.py", "tests/test_favorite_0136.py", "tests/test_ui_redesign.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text

==================================== ERRORS ====================================
_______________ ERROR collecting tests/test_library_list_0137.py _______________
../venv/lib/python3.12/site-packages/_pytest/python.py:528: in importtestmodule
    mod = import_path(
../venv/lib/python3.12/site-packages/_pytest/pathlib.py:640: in import_path
    importlib.import_module(module_name)
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
../venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_library_list_0137.py:5: in <module>
    from test_bugs_0134 import ui,sample
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
../venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_bugs_0134.py:6: in <module>
    from checkpoint.window import MainWindow
E     File "/workspace/work/Checkpoint/checkpoint/window.py", line 328
E       self.statusBar().showMessage(message)
E   IndentationError: unexpected indent
_________________ ERROR collecting tests/test_favorite_0136.py _________________
../venv/lib/python3.12/site-packages/_pytest/python.py:528: in importtestmodule
    mod = import_path(
../venv/lib/python3.12/site-packages/_pytest/pathlib.py:640: in import_path
    importlib.import_module(module_name)
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
../venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_favorite_0136.py:4: in <module>
    from test_bugs_0134 import ui,sample
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
../venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_bugs_0134.py:6: in <module>
    from checkpoint.window import MainWindow
E     File "/workspace/work/Checkpoint/checkpoint/window.py", line 328
E       self.statusBar().showMessage(message)
E   IndentationError: unexpected indent
__________________ ERROR collecting tests/test_ui_redesign.py __________________
../venv/lib/python3.12/site-packages/_pytest/python.py:528: in importtestmodule
    mod = import_path(
../venv/lib/python3.12/site-packages/_pytest/pathlib.py:640: in import_path
    importlib.import_module(module_name)
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<frozen importlib._bootstrap>:1387: in _gcd_import
    ???
<frozen importlib._bootstrap>:1360: in _find_and_load
    ???
<frozen importlib._bootstrap>:1331: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:935: in _load_unlocked
    ???
../venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:185: in exec_module
    exec(co, module.__dict__)
tests/test_ui_redesign.py:5: in <module>
    from checkpoint.window import MainWindow
E     File "/workspace/work/Checkpoint/checkpoint/window.py", line 328
E       self.statusBar().showMessage(message)
E   IndentationError: unexpected indent
=========================== short test summary info ============================
ERROR tests/test_library_list_0137.py
ERROR tests/test_favorite_0136.py
ERROR tests/test_ui_redesign.py
!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!!
3 errors in 0.38s

```

stderr integral:
```text

```

Código de saída: 2

## lista-depois-correcao

UTC: 2026-11-15T21:47:02.468535+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_library_list_0137.py", "tests/test_favorite_0136.py", "tests/test_ui_redesign.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
............F..F                                                         [100%]
=================================== FAILURES ===================================
______________ test_home_tiles_are_full_height_and_open_real_game ______________

library = <checkpoint.library.Library object at 0x7f4864b830b0>
app = <PySide6.QtWidgets.QApplication(0x2d1e54f0) at 0x7f4864ab6940>

    def test_home_tiles_are_full_height_and_open_real_game(library,app):
        identity=library.save_game({'title':'Fixture','status':'Jogando'})
        window=MainWindow(library);window.show();app.processEvents()
        tiles=window.pages[0].findChildren(GameTile)
>       assert tiles and all(tile.height()==tile.art_height+48 for tile in tiles)
E       assert ([])

tests/test_ui_redesign.py:70: AssertionError
_________________ test_home_places_activity_beside_continuity __________________

library = <checkpoint.library.Library object at 0x7f486262b920>
app = <PySide6.QtWidgets.QApplication(0x2d1e54f0) at 0x7f4864ab6940>

    def test_home_places_activity_beside_continuity(library,app):
        from PySide6.QtWidgets import QWidget
        library.save_game({'title':'Fixture','status':'Jogando'})
        window=MainWindow(library);window.resize(1440,980);window.show();app.processEvents()
        continuation=window.pages[0].findChild(QWidget,'homeContinuation')
        activity=window.pages[0].findChild(QWidget,'homeActivity')
>       assert continuation.geometry().top()==activity.geometry().top()
               ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'geometry'

tests/test_ui_redesign.py:110: AttributeError
=========================== short test summary info ============================
FAILED tests/test_ui_redesign.py::test_home_tiles_are_full_height_and_open_real_game
FAILED tests/test_ui_redesign.py::test_home_places_activity_beside_continuity
2 failed, 14 passed in 3.00s

```

stderr integral:
```text

```

Código de saída: 1

## inicio-ofertas-banner-previa

UTC: 2026-11-15T21:47:36.103210+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/inicio-v10"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/inicio-v10

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## ofertas-banner-regressao

UTC: 2026-11-15T21:48:27.706455+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_layout_0137.py", "tests/test_home_data_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..................                                                       [100%]
18 passed in 1.60s

```

stderr integral:
```text

```

Código de saída: 0

## lista-regressoes

UTC: 2026-11-15T21:50:10.834702+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_library_list_0137.py", "tests/test_layout_0134.py", "tests/test_folder_platforms.py", "tests/test_ui.py::test_navigate_and_game_detail_with_real_database", "tests/test_ui_redesign.py", "tests/test_favorite_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.................................F....                                   [100%]
=================================== FAILURES ===================================
_________________ test_home_places_activity_beside_continuity __________________

library = <checkpoint.library.Library object at 0x7f13cc33dd00>
app = <PySide6.QtWidgets.QApplication(0x2a2d3420) at 0x7f13ccb4c340>

    def test_home_places_activity_beside_continuity(library,app):
        from PySide6.QtWidgets import QWidget
        library.save_game({'title':'Fixture','status':'Jogando'})
        window=MainWindow(library);window.resize(1440,980);window.show();app.processEvents()
        continuation=window.pages[0].findChild(QWidget,'homeRecentSection')
        activity=window.pages[0].findChild(QWidget,'homeWeekSummary')
        assert continuation.geometry().top()==activity.geometry().top()
>       assert activity.geometry().left()>continuation.geometry().right()
E       assert 0 > 697
E        +  where 0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f13c9c005c0>()
E        +    where <built-in method left of PySide6.QtCore.QRect object at 0x7f13c9c005c0> = PySide6.QtCore.QRect(0, 0, 466, 200).left
E        +      where PySide6.QtCore.QRect(0, 0, 466, 200) = <built-in method geometry of CardSurface object at 0x7f13c9b3e6c0>()
E        +        where <built-in method geometry of CardSurface object at 0x7f13c9b3e6c0> = <checkpoint.design_system.CardSurface(0x2e4f8e90, name="homeWeekSummary") at 0x7f13c9b3e6c0>.geometry
E        +  and   697 = <built-in method right of PySide6.QtCore.QRect object at 0x7f13c9bdba80>()
E        +    where <built-in method right of PySide6.QtCore.QRect object at 0x7f13c9bdba80> = PySide6.QtCore.QRect(0, 0, 698, 360).right
E        +      where PySide6.QtCore.QRect(0, 0, 698, 360) = <built-in method geometry of CardSurface object at 0x7f13c9b3de40>()
E        +        where <built-in method geometry of CardSurface object at 0x7f13c9b3de40> = <checkpoint.design_system.CardSurface(0x2e4d8b60, name="homeRecentSection") at 0x7f13c9b3de40>.geometry

tests/test_ui_redesign.py:116: AssertionError
=========================== short test summary info ============================
FAILED tests/test_ui_redesign.py::test_home_places_activity_beside_continuity
1 failed, 37 passed in 4.76s

```

stderr integral:
```text

```

Código de saída: 1

## lista-regressoes-finais

UTC: 2026-11-15T21:50:39.615748+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_library_list_0137.py", "tests/test_layout_0134.py", "tests/test_folder_platforms.py", "tests/test_ui.py::test_navigate_and_game_detail_with_real_database", "tests/test_ui_redesign.py", "tests/test_favorite_0136.py", "tests/test_home_layout_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
....................................................                     [100%]
52 passed in 6.22s

```

stderr integral:
```text

```

Código de saída: 0

## grade-desempenho-antes

UTC: 2026-11-15T21:51:49.196676+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_grid_performance_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
____ test_collection_totals_use_bounded_queries_without_duplicate_snapshots ____

library = <checkpoint.library.Library object at 0x7f84257d7560>

    def test_collection_totals_use_bounded_queries_without_duplicate_snapshots(library):
        ids=[library.save_game({'title':f'Jogo {n}'}) for n in range(100)]
        with library.sql:
            library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-01-01',1200,'finished')",(ids[0],))
            for account,minutes in [('1',20),('2',30)]:
                library.sql.execute("INSERT INTO steam_owned_games(steam_id,app_id,game_id,title,minutes,checked_at) VALUES(?,'620',?,'Jogo',?,'2026-01-01')",(account,ids[0],minutes))
        queries=[];library.sql.set_trace_callback(queries.append)
        try:totals=collection_times(library)
        finally:library.sql.set_trace_callback(None)
        assert totals[ids[0]]==3000 and all(totals[i]==0 for i in ids[1:])
>       assert len(queries)<=8
E       assert 401 <= 8
E        +  where 401 = len(['SELECT * FROM games WHERE deleted_at IS NULL ORDER BY title COLLATE NOCASE', "SELECT value FROM settings WHERE key='...inutes),0) FROM steam_owned_games WHERE game_id=1', "SELECT value FROM settings WHERE key='collection.unowned.2'", ...])

tests/test_grid_performance_0137.py:17: AssertionError
_____________ test_cache_is_bounded_and_invalidates_changed_files ______________

app = <PySide6.QtWidgets.QApplication(0x2a81c930) at 0x7f84257ff280>
folder = PosixPath('/tmp/343b1a5090714625a8fdac612816479c')

    def test_cache_is_bounded_and_invalidates_changed_files(app,folder):
>       from checkpoint.artwork_cache import ArtworkCache
E       ModuleNotFoundError: No module named 'checkpoint.artwork_cache'

tests/test_grid_performance_0137.py:21: ModuleNotFoundError
___ test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0] ___

ui = (<checkpoint.window.MainWindow(0x2a94d030) at 0x7f84256f3bc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2a81c930) at 0x7f84257ff280>

    def test_refresh_preserves_items_and_scroll_with_equal_grid_margins(ui,app):
        w,i=ui
        for n in range(100):w.library.save_game({'title':f'Jogo {n:03}'})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(1)
            for _ in range(6):app.processEvents()
            grid=w.gallery;bar=grid.verticalScrollBar();bar.setValue(bar.maximum()//2);position=bar.value();item=grid.item(0)
            w.refresh_library()
            for _ in range(4):app.processEvents()
            assert grid.item(0) is item and bar.value()==position
>           first=grid.art_rect(grid.visualItemRect(grid.item(0)))
                  ^^^^^^^^^^^^^
E           AttributeError: 'CoverGrid' object has no attribute 'art_rect'

tests/test_grid_performance_0137.py:43: AttributeError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___ test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1] ___

ui = (<checkpoint.window.MainWindow(0x2ac08e00) at 0x7f8425523a40>, 1)
app = <PySide6.QtWidgets.QApplication(0x2a81c930) at 0x7f84257ff280>

    def test_refresh_preserves_items_and_scroll_with_equal_grid_margins(ui,app):
        w,i=ui
        for n in range(100):w.library.save_game({'title':f'Jogo {n:03}'})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(1)
            for _ in range(6):app.processEvents()
            grid=w.gallery;bar=grid.verticalScrollBar();bar.setValue(bar.maximum()//2);position=bar.value();item=grid.item(0)
            w.refresh_library()
            for _ in range(4):app.processEvents()
            assert grid.item(0) is item and bar.value()==position
>           first=grid.art_rect(grid.visualItemRect(grid.item(0)))
                  ^^^^^^^^^^^^^
E           AttributeError: 'CoverGrid' object has no attribute 'art_rect'

tests/test_grid_performance_0137.py:43: AttributeError
=========================== short test summary info ============================
FAILED tests/test_grid_performance_0137.py::test_collection_totals_use_bounded_queries_without_duplicate_snapshots
FAILED tests/test_grid_performance_0137.py::test_cache_is_bounded_and_invalidates_changed_files
FAILED tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0]
FAILED tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1]
4 failed in 0.58s

```

stderr integral:
```text

```

Código de saída: 1

## grade-desempenho-depois

UTC: 2026-11-15T21:52:39.426169+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_grid_performance_0137.py", "tests/test_card_layout.py", "tests/test_smooth_scroll.py", "tests/test_ui_polish.py", "tests/test_registration_0128.py", "tests/test_library_list_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..FF...................                                                  [100%]
=================================== FAILURES ===================================
___ test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0] ___

ui = (<checkpoint.window.MainWindow(0x8c8ae50) at 0x7f41cf695380>, 1)
app = <PySide6.QtWidgets.QApplication(0x8b996a0) at 0x7f41cf85c300>

    def test_refresh_preserves_items_and_scroll_with_equal_grid_margins(ui,app):
        w,i=ui
        for n in range(100):w.library.save_game({'title':f'Jogo {n:03}'})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(1)
            for _ in range(6):app.processEvents()
            grid=w.gallery;bar=grid.verticalScrollBar();bar.setValue(bar.maximum()//2);position=bar.value();item=grid.item(0)
            w.refresh_library()
            for _ in range(4):app.processEvents()
            assert grid.item(0) is item and bar.value()==position
            first=grid.art_rect(grid.visualItemRect(grid.item(0)))
            last=grid.art_rect(grid.visualItemRect(grid.item(grid.columns-1)))
>           assert abs(first.left()-(grid.viewport().width()-last.right()))<=2
E           assert 771.0 <= 2
E            +  where 771.0 = abs((14.0 - (1028 - 243.0)))
E            +    where 14.0 = <built-in method left of PySide6.QtCore.QRectF object at 0x7f41cea7ab40>()
E            +      where <built-in method left of PySide6.QtCore.QRectF object at 0x7f41cea7ab40> = PySide6.QtCore.QRectF(14.000000, -6865.000000, 229.000000, 343.500000).left
E            +    and   1028 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f41d5914940>()
E            +      where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f41d5914940> = <PySide6.QtWidgets.QWidget(0x8b4c000, name="qt_scrollarea_viewport") at 0x7f41d5914940>.width
E            +        where <PySide6.QtWidgets.QWidget(0x8b4c000, name="qt_scrollarea_viewport") at 0x7f41d5914940> = <built-in method viewport of CoverGrid object at 0x7f41cea9f840>()
E            +          where <built-in method viewport of CoverGrid object at 0x7f41cea9f840> = <checkpoint.cover_grid.CoverGrid(0x8e5ed70, name="coverGrid") at 0x7f41cea9f840>.viewport
E            +    and   243.0 = <built-in method right of PySide6.QtCore.QRectF object at 0x7f41ce804500>()
E            +      where <built-in method right of PySide6.QtCore.QRectF object at 0x7f41ce804500> = PySide6.QtCore.QRectF(14.000000, -6443.000000, 229.000000, 343.500000).right

tests/test_grid_performance_0137.py:45: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___ test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1] ___

ui = (<checkpoint.window.MainWindow(0x8bd5a80) at 0x7f41cf695440>, 1)
app = <PySide6.QtWidgets.QApplication(0x8b996a0) at 0x7f41cf85c300>

    def test_refresh_preserves_items_and_scroll_with_equal_grid_margins(ui,app):
        w,i=ui
        for n in range(100):w.library.save_game({'title':f'Jogo {n:03}'})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(1)
            for _ in range(6):app.processEvents()
            grid=w.gallery;bar=grid.verticalScrollBar();bar.setValue(bar.maximum()//2);position=bar.value();item=grid.item(0)
            w.refresh_library()
            for _ in range(4):app.processEvents()
            assert grid.item(0) is item and bar.value()==position
            first=grid.art_rect(grid.visualItemRect(grid.item(0)))
            last=grid.art_rect(grid.visualItemRect(grid.item(grid.columns-1)))
>           assert abs(first.left()-(grid.viewport().width()-last.right()))<=2
E           assert 771.0 <= 2
E            +  where 771.0 = abs((14.0 - (1028 - 243.0)))
E            +    where 14.0 = <built-in method left of PySide6.QtCore.QRectF object at 0x7f41d6457c00>()
E            +      where <built-in method left of PySide6.QtCore.QRectF object at 0x7f41d6457c00> = PySide6.QtCore.QRectF(14.000000, -6865.000000, 229.000000, 343.500000).left
E            +    and   1028 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f41d58577c0>()
E            +      where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f41d58577c0> = <PySide6.QtWidgets.QWidget(0x90972e0, name="qt_scrollarea_viewport") at 0x7f41d58577c0>.width
E            +        where <PySide6.QtWidgets.QWidget(0x90972e0, name="qt_scrollarea_viewport") at 0x7f41d58577c0> = <built-in method viewport of CoverGrid object at 0x7f41ce821e80>()
E            +          where <built-in method viewport of CoverGrid object at 0x7f41ce821e80> = <checkpoint.cover_grid.CoverGrid(0x8e60d30, name="coverGrid") at 0x7f41ce821e80>.viewport
E            +    and   243.0 = <built-in method right of PySide6.QtCore.QRectF object at 0x7f41d5961200>()
E            +      where <built-in method right of PySide6.QtCore.QRectF object at 0x7f41d5961200> = PySide6.QtCore.QRectF(14.000000, -6443.000000, 229.000000, 343.500000).right

tests/test_grid_performance_0137.py:45: AssertionError
=========================== short test summary info ============================
FAILED tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0]
FAILED tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1]
2 failed, 21 passed in 2.62s

```

stderr integral:
```text

```

Código de saída: 1

## grade-benchmark-depois

UTC: 2026-11-15T21:52:45.119562+00:00

Comando: `["/workspace/work/venv/bin/python", "/workspace/work/evidence-0137/bench_grid.py", "/workspace/work/evidence-0137/bench-depois"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
{
  "games": 500,
  "distinct_images": 100,
  "image_size": [
    300,
    450
  ],
  "window": [
    1280,
    800
  ],
  "initialization_seconds": 0.1754999780023354,
  "refresh_seconds": [
    0.037296402999345446,
    0.03442418199847452,
    0.03322569200099679
  ],
  "refresh_sql_statements": [
    15,
    15,
    15
  ],
  "frame_seconds": [
    0.010084289002406877,
    0.017297159000008833,
    0.01608193300126004,
    0.006626524998864625,
    0.006460222000896465,
    0.006279310000536498,
    0.006162944002426229,
    0.006620304000534816,
    0.009715853000670904,
    0.011750978002964985,
    0.006764232999557862,
    0.007066539001243655,
    0.006949442002223805,
    0.0068786849988100585,
    0.0070865600027900655,
    0.006077925001591211
  ],
  "median_frame_ms": 6.9140635005169315,
  "scroll_before_refresh": 34930,
  "scroll_after_refresh": 34930,
  "max_rss_kib": 104380
}

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## grade-desempenho-regressoes

UTC: 2026-11-15T21:54:24.526993+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_grid_performance_0137.py", "tests/test_card_layout.py", "tests/test_smooth_scroll.py", "tests/test_ui_polish.py", "tests/test_complete_layout.py", "tests/test_registration_0128.py", "tests/test_library_list_0137.py", "tests/test_layout_0134.py", "tests/test_folder_platforms.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
........................................................................ [ 79%]
...................                                                      [100%]
91 passed in 48.34s

```

stderr integral:
```text

```

Código de saída: 0

## grade-benchmark-final

UTC: 2026-11-15T21:54:25.984193+00:00

Comando: `["/workspace/work/venv/bin/python", "/workspace/work/evidence-0137/bench_grid.py", "/workspace/work/evidence-0137/bench-final"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
{
  "games": 500,
  "distinct_images": 100,
  "image_size": [
    300,
    450
  ],
  "window": [
    1280,
    800
  ],
  "initialization_seconds": 0.15071668699965812,
  "refresh_seconds": [
    0.036365174000820844,
    0.03456521500265808,
    0.03507108900157618
  ],
  "refresh_sql_statements": [
    15,
    15,
    15
  ],
  "frame_seconds": [
    0.005398475997935748,
    0.02069255899914424,
    0.020401169000251684,
    0.015599505000864156,
    0.01572859899897594,
    0.00797658000010415,
    0.006690537000395125,
    0.008557927998481318,
    0.015311560000554891,
    0.006854395000118529,
    0.006797748999815667,
    0.008191283999622101,
    0.015136574998905417,
    0.00679625699922326,
    0.006733932998031378,
    0.006657156998699065
  ],
  "median_frame_ms": 8.083931999863125,
  "scroll_before_refresh": 25943,
  "scroll_after_refresh": 25943,
  "max_rss_kib": 107904
}

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## grade-lista-capturas

UTC: 2026-11-15T21:54:39.603908+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/biblioteca-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/biblioteca-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## rotulo-alfabeticamente

UTC: 2026-11-15T21:54:54.580407+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_labels_0137.py", "tests/test_prices_0129.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.........                                                                [100%]
9 passed in 1.20s

```

stderr integral:
```text

```

Código de saída: 0

## estatisticas-periodos-antes

UTC: 2026-11-15T21:57:42.311386+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_period_chart_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
________ test_week_chart_uses_width_and_months_keep_real_days[sample0] _________

ui = (<checkpoint.window.MainWindow(0x132e7690) at 0x7f2b26a10fc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1320b480) at 0x7f2b26b37940>

    def test_week_chart_uses_width_and_months_keep_real_days(ui,app):
        w,i=ui
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(4);combo=w.pages[4].findChild(QComboBox,'statisticsPeriod')
            combo.setCurrentIndex(combo.findData('weekly'))
            for _ in range(6):app.processEvents()
            from checkpoint.statistics_view import TimeChart
            chart=w.pages[4].findChild(TimeChart);chart.grab()
>           assert chart.period=='weekly' and chart.cells
                   ^^^^^^^^^^^^
E           AttributeError: 'ActivityHeatmap' object has no attribute 'period'

tests/test_period_chart_0137.py:14: AttributeError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
________ test_week_chart_uses_width_and_months_keep_real_days[sample1] _________

ui = (<checkpoint.window.MainWindow(0x1388a340) at 0x7f2b265b6e40>, 1)
app = <PySide6.QtWidgets.QApplication(0x1320b480) at 0x7f2b26b37940>

    def test_week_chart_uses_width_and_months_keep_real_days(ui,app):
        w,i=ui
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(4);combo=w.pages[4].findChild(QComboBox,'statisticsPeriod')
            combo.setCurrentIndex(combo.findData('weekly'))
            for _ in range(6):app.processEvents()
            from checkpoint.statistics_view import TimeChart
            chart=w.pages[4].findChild(TimeChart);chart.grab()
>           assert chart.period=='weekly' and chart.cells
                   ^^^^^^^^^^^^
E           AttributeError: 'ActivityHeatmap' object has no attribute 'period'

tests/test_period_chart_0137.py:14: AttributeError
______________ test_hourly_day_uses_real_local_session_boundaries ______________

library = <checkpoint.library.Library object at 0x7f2b2ca6cf50>

    def test_hourly_day_uses_real_local_session_boundaries(library):
>       from checkpoint.statistics_periods import day_hours
E       ImportError: cannot import name 'day_hours' from 'checkpoint.statistics_periods' (/workspace/work/Checkpoint/checkpoint/statistics_periods.py)

tests/test_period_chart_0137.py:25: ImportError
____________ test_day_hours_respect_dst_and_do_not_change_instants _____________

library = <checkpoint.library.Library object at 0x7f2b2c8acad0>

    def test_day_hours_respect_dst_and_do_not_change_instants(library):
        from zoneinfo import ZoneInfo
>       from checkpoint.statistics_periods import day_hours
E       ImportError: cannot import name 'day_hours' from 'checkpoint.statistics_periods' (/workspace/work/Checkpoint/checkpoint/statistics_periods.py)

tests/test_period_chart_0137.py:36: ImportError
=========================== short test summary info ============================
FAILED tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample0]
FAILED tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample1]
FAILED tests/test_period_chart_0137.py::test_hourly_day_uses_real_local_session_boundaries
FAILED tests/test_period_chart_0137.py::test_day_hours_respect_dst_and_do_not_change_instants
4 failed in 0.49s

```

stderr integral:
```text

```

Código de saída: 1

## estatisticas-periodos-depois

UTC: 2026-11-15T21:59:38.753376+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_period_chart_0137.py", "tests/test_statistics_0136.py", "tests/test_statistics_list_0136.py", "tests/test_wishlist_prices.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...................                                                      [100%]
19 passed in 2.81s

```

stderr integral:
```text

```

Código de saída: 0

## estatisticas-capturas

UTC: 2026-11-15T22:00:07.699525+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/estatisticas-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/estatisticas-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## perfil-recorte-antes

UTC: 2026-11-15T22:02:11.834328+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_avatar_crop_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFF.                                                                     [100%]
=================================== FAILURES ===================================
_________ test_crop_zoom_cancel_and_persistence_keep_original[shape0] __________

library = <checkpoint.library.Library object at 0x7f6139d9e6f0>
app = <PySide6.QtWidgets.QApplication(0x3f039090) at 0x7f6139f396c0>
folder = PosixPath('/tmp/a3864d7403774ab498e5f412e911f5fc')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f6139d9e660>
shape = (400, 200)

    @pytest.mark.parametrize('shape',[(400,200),(200,400),(24,16)])
    def test_crop_zoom_cancel_and_persistence_keep_original(library,app,folder,monkeypatch,shape):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('red'));p=QPainter(image);p.fillRect(shape[0]//2,0,shape[0]//2,shape[1],QColor('blue'));p.end()
        path=folder/'Foto com espaço e acentuação.png';assert image.save(str(path));before=path.read_bytes()
        monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(path),''))
        dialog=ProfileDialog(library);dialog.choose_photo()
>       assert hasattr(dialog,'crop')
E       AssertionError: assert False
E        +  where False = hasattr(<checkpoint.profile_dialog.ProfileDialog(0x3f256490) at 0x7f6139dee640>, 'crop')

tests/test_avatar_crop_0137.py:13: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
_________ test_crop_zoom_cancel_and_persistence_keep_original[shape1] __________

library = <checkpoint.library.Library object at 0x7f6139039430>
app = <PySide6.QtWidgets.QApplication(0x3f039090) at 0x7f6139f396c0>
folder = PosixPath('/tmp/f5bb7f077fbb4181b3c4e44bc855be2a')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f6139038e00>
shape = (200, 400)

    @pytest.mark.parametrize('shape',[(400,200),(200,400),(24,16)])
    def test_crop_zoom_cancel_and_persistence_keep_original(library,app,folder,monkeypatch,shape):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('red'));p=QPainter(image);p.fillRect(shape[0]//2,0,shape[0]//2,shape[1],QColor('blue'));p.end()
        path=folder/'Foto com espaço e acentuação.png';assert image.save(str(path));before=path.read_bytes()
        monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(path),''))
        dialog=ProfileDialog(library);dialog.choose_photo()
>       assert hasattr(dialog,'crop')
E       AssertionError: assert False
E        +  where False = hasattr(<checkpoint.profile_dialog.ProfileDialog(0x3f427ee0) at 0x7f613904fe40>, 'crop')

tests/test_avatar_crop_0137.py:13: AssertionError
_________ test_crop_zoom_cancel_and_persistence_keep_original[shape2] __________

library = <checkpoint.library.Library object at 0x7f6139038da0>
app = <PySide6.QtWidgets.QApplication(0x3f039090) at 0x7f6139f396c0>
folder = PosixPath('/tmp/c279fa4d907f46c2aa5dbb78d0d482e9')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f61390394f0>
shape = (24, 16)

    @pytest.mark.parametrize('shape',[(400,200),(200,400),(24,16)])
    def test_crop_zoom_cancel_and_persistence_keep_original(library,app,folder,monkeypatch,shape):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('red'));p=QPainter(image);p.fillRect(shape[0]//2,0,shape[0]//2,shape[1],QColor('blue'));p.end()
        path=folder/'Foto com espaço e acentuação.png';assert image.save(str(path));before=path.read_bytes()
        monkeypatch.setattr('checkpoint.profile_dialog.QFileDialog.getOpenFileName',lambda *a,**k:(str(path),''))
        dialog=ProfileDialog(library);dialog.choose_photo()
>       assert hasattr(dialog,'crop')
E       AssertionError: assert False
E        +  where False = hasattr(<checkpoint.profile_dialog.ProfileDialog(0x3f42a410) at 0x7f613906b6c0>, 'crop')

tests/test_avatar_crop_0137.py:13: AssertionError
=========================== short test summary info ============================
FAILED tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape0]
FAILED tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape1]
FAILED tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape2]
3 failed, 1 passed in 0.24s

```

stderr integral:
```text

```

Código de saída: 1

## estatisticas-regressoes

UTC: 2026-11-15T22:02:27.072651+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_period_chart_0137.py", "tests/test_statistics_0136.py", "tests/test_statistics_list_0136.py", "tests/test_statistics_visible_0136.py", "tests/test_wishlist_prices.py", "tests/test_ui_polish.py", "tests/test_labels_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...............................                                          [100%]
31 passed in 3.67s

```

stderr integral:
```text

```

Código de saída: 0

## estatisticas-heatmap-compacto

UTC: 2026-11-15T22:04:53.475078+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/estatisticas-v2"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/estatisticas-v2

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## estatisticas-compactas-regressao

UTC: 2026-11-15T22:05:51.991421+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_period_chart_0137.py", "tests/test_statistics_0136.py", "tests/test_statistics_list_0136.py", "tests/test_statistics_visible_0136.py", "tests/test_wishlist_prices.py", "tests/test_ui_polish.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.........................                                                [100%]
25 passed in 3.51s

```

stderr integral:
```text

```

Código de saída: 0

## perfil-recorte-depois

UTC: 2026-11-15T22:06:50.885324+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_avatar_crop_0137.py", "tests/test_profile.py", "tests/test_complete_layout.py::test_theme_swatches_and_profile_apply_without_losing_data", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.......                                                                  [100%]
7 passed in 1.14s

```

stderr integral:
```text

```

Código de saída: 0

## perfil-orientacao-arrasto

UTC: 2026-11-15T22:07:40.882694+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_avatar_crop_0137.py", "tests/test_profile.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.......                                                                  [100%]
7 passed in 0.59s

```

stderr integral:
```text

```

Código de saída: 0

## perfil-captura

UTC: 2026-11-15T22:07:45.029152+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/perfil-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/perfil-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## rom-local-antes

UTC: 2026-11-15T22:13:05.849530+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFFFFFFF                                                                [100%]
=================================== FAILURES ===================================
_______ test_bind_launch_and_reopen_local_rom_without_drive[local_rom0] ________

library = <checkpoint.library.Library object at 0x7fbd34c7d250>
local_rom = (1, PosixPath('/tmp/27c7773f8bb644b3ae96ea30e00f0bde/ROMs com espaço/Programa Á.ch8'), 1, b'\x00\xe0\x12\x00')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fbd34c7d2b0>

    def test_bind_launch_and_reopen_local_rom_without_drive(library,local_rom,monkeypatch):
>       from checkpoint.local_rom import bind_local,compatible_profiles
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:23: ModuleNotFoundError
_______ test_bind_launch_and_reopen_local_rom_without_drive[local_rom1] ________

library = <checkpoint.library.Library object at 0x7fbd34e0f110>
local_rom = (1, PosixPath('/tmp/41b7df57865c4402a78750c9f081f102/ROMs com espaço/Programa Bê.ch8'), 1, b'\x00\xe0`\x01p\x01\x12\x04')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fbd34e0f1a0>

    def test_bind_launch_and_reopen_local_rom_without_drive(library,local_rom,monkeypatch):
>       from checkpoint.local_rom import bind_local,compatible_profiles
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:23: ModuleNotFoundError
_ test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom0] _

library = <checkpoint.library.Library object at 0x7fbd34c7e810>
local_rom = (1, PosixPath('/tmp/77ecf4e2c0dd4216ae4b0bd60c7b7376/ROMs com espaço/Programa Á.ch8'), 1, b'\x00\xe0\x12\x00')

    def test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic(library,local_rom):
>       from checkpoint.local_rom import bind_local
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:46: ModuleNotFoundError
_ test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom1] _

library = <checkpoint.library.Library object at 0x7fbd34c7e0f0>
local_rom = (1, PosixPath('/tmp/aeaa7286e9984c6b9e8c49f015cedea6/ROMs com espaço/Programa Bê.ch8'), 1, b'\x00\xe0`\x01p\x01\x12\x04')

    def test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic(library,local_rom):
>       from checkpoint.local_rom import bind_local
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:46: ModuleNotFoundError
_ test_local_link_requires_explicit_profile_capability_and_read_access[local_rom0] _

library = <checkpoint.library.Library object at 0x7fbd34e0eb70>
local_rom = (1, PosixPath('/tmp/73e96a85133a4426bcaaf3a7d58e6b64/ROMs com espaço/Programa Á.ch8'), 1, b'\x00\xe0\x12\x00')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fbd34e0e810>

    def test_local_link_requires_explicit_profile_capability_and_read_access(library,local_rom,monkeypatch):
>       from checkpoint.local_rom import bind_local,compatible_profiles
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:59: ModuleNotFoundError
_ test_local_link_requires_explicit_profile_capability_and_read_access[local_rom1] _

library = <checkpoint.library.Library object at 0x7fbd34c7e690>
local_rom = (1, PosixPath('/tmp/befc1af72e344806a352044b0d9bca83/ROMs com espaço/Programa Bê.ch8'), 1, b'\x00\xe0`\x01p\x01\x12\x04')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fbd34c7dd60>

    def test_local_link_requires_explicit_profile_capability_and_read_access(library,local_rom,monkeypatch):
>       from checkpoint.local_rom import bind_local,compatible_profiles
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:59: ModuleNotFoundError
________ test_distinct_ocarina_platform_and_edition_are_not_equivalent _________

library = <checkpoint.library.Library object at 0x7fbd34c7ddc0>
folder = PosixPath('/tmp/ff120da24c5a4191a73b294312e3e4cc')

    def test_distinct_ocarina_platform_and_edition_are_not_equivalent(library,folder):
>       from checkpoint.local_rom import identity_problem
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:75: ModuleNotFoundError
__________ test_cancel_local_dialog_does_not_change_link[local_rom0] ___________

library = <checkpoint.library.Library object at 0x7fbd34a83f50>
local_rom = (1, PosixPath('/tmp/98cf347b650f46cfae248d19ee109870/ROMs com espaço/Programa Á.ch8'), 1, b'\x00\xe0\x12\x00')
app = <PySide6.QtWidgets.QApplication(0x21b2cda0) at 0x7fbd34cb2b40>

    def test_cancel_local_dialog_does_not_change_link(library,local_rom,app):
>       from checkpoint.local_rom import bind_local
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:84: ModuleNotFoundError
__________ test_cancel_local_dialog_does_not_change_link[local_rom1] ___________

library = <checkpoint.library.Library object at 0x7fbd34ab3050>
local_rom = (1, PosixPath('/tmp/1c606dee4e484e378d006e7140bca437/ROMs com espaço/Programa Bê.ch8'), 1, b'\x00\xe0`\x01p\x01\x12\x04')
app = <PySide6.QtWidgets.QApplication(0x21b2cda0) at 0x7fbd34cb2b40>

    def test_cancel_local_dialog_does_not_change_link(library,local_rom,app):
>       from checkpoint.local_rom import bind_local
E       ModuleNotFoundError: No module named 'checkpoint.local_rom'

tests/test_local_rom_0137.py:84: ModuleNotFoundError
=========================== short test summary info ============================
FAILED tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom0]
FAILED tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom1]
FAILED tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom0]
FAILED tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom1]
FAILED tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom0]
FAILED tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom1]
FAILED tests/test_local_rom_0137.py::test_distinct_ocarina_platform_and_edition_are_not_equivalent
FAILED tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom0]
FAILED tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom1]
9 failed in 0.28s

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 1

## perfil-zoom-redondo

UTC: 2026-11-15T22:15:20.621007+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/perfil-v2"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/perfil-v2

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## rom-local-servico-depois

UTC: 2026-11-15T22:17:28.342174+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.........                                                                [100%]
9 passed in 0.34s

```

stderr integral:
```text

```

Código de saída: 0

## rom-local-ficha-execucao

UTC: 2026-11-15T22:19:44.846327+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "tests/test_launch_0135.py", "tests/test_sessions_0135.py", "tests/test_layout_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.............
```

stderr integral:
```text

```

Código de saída: -15

## rom-edicao-antes

UTC: 2026-11-15T22:20:37.347960+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_rom_edition_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFF                                                                      [100%]
=================================== FAILURES ===================================
_____ test_drive_worker_rejects_distinct_ocarina_edition_before_binding[] ______

library = <checkpoint.library.Library object at 0x7fa8df398140>, platform = ''

    @pytest.mark.parametrize('platform',['','Nintendo 64'])
    def test_drive_worker_rejects_distinct_ocarina_edition_before_binding(library,platform):
        game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time','platform':platform,'description':'Manter original'})
        DriveScanner(library,None).record({'id':'edition-3d','name':'The Legend of Zelda - Ocarina of Time 3D.3ds'},'/Nintendo 3DS');library.sql.commit()
        file=library.sql.execute('SELECT * FROM game_files').fetchone();before=library.get(game)
        class NoDownload:
            def download(self,*args):pytest.fail('Não baixar uma edição divergente')
>       with pytest.raises(ValueError):complete_link(library,file['id'],game,client=NoDownload(),sources={})
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_rom_edition_0137.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
checkpoint/rom_link.py:68: in complete_link
    DriveScanner(library,client or GoogleDriveClient.authenticate(None,CredentialVault())).download(file_id,directory)
checkpoint/integrations/drive.py:305: in download
    self.client.download(row['drive_id'],partial)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_rom_edition_0137.test_drive_worker_rejects_distinct_ocarina_edition_before_binding.<locals>.NoDownload object at 0x7fa8df398650>
args = ('edition-3d', PosixPath('/tmp/9551f34979eb4077a40a4e6d55e00273/ROMs/edition-3d.3ds.b636145762cf41279310561917076f00.partial'))

>   def download(self,*args):pytest.fail('Não baixar uma edição divergente')
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Não baixar uma edição divergente

tests/test_rom_edition_0137.py:14: Failed
_ test_drive_worker_rejects_distinct_ocarina_edition_before_binding[Nintendo 64] _

library = <checkpoint.library.Library object at 0x7fa8df0a2b40>
platform = 'Nintendo 64'

    @pytest.mark.parametrize('platform',['','Nintendo 64'])
    def test_drive_worker_rejects_distinct_ocarina_edition_before_binding(library,platform):
        game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time','platform':platform,'description':'Manter original'})
        DriveScanner(library,None).record({'id':'edition-3d','name':'The Legend of Zelda - Ocarina of Time 3D.3ds'},'/Nintendo 3DS');library.sql.commit()
        file=library.sql.execute('SELECT * FROM game_files').fetchone();before=library.get(game)
        class NoDownload:
            def download(self,*args):pytest.fail('Não baixar uma edição divergente')
>       with pytest.raises(ValueError):complete_link(library,file['id'],game,client=NoDownload(),sources={})
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_rom_edition_0137.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
checkpoint/rom_link.py:68: in complete_link
    DriveScanner(library,client or GoogleDriveClient.authenticate(None,CredentialVault())).download(file_id,directory)
checkpoint/integrations/drive.py:305: in download
    self.client.download(row['drive_id'],partial)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_rom_edition_0137.test_drive_worker_rejects_distinct_ocarina_edition_before_binding.<locals>.NoDownload object at 0x7fa8df0a3530>
args = ('edition-3d', PosixPath('/tmp/2a51fe4f5549499985c8aa3b6ae301ca/ROMs/edition-3d.3ds.8b1f3e1bcbc241a0bd6bb8332d755207.partial'))

>   def download(self,*args):pytest.fail('Não baixar uma edição divergente')
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Não baixar uma edição divergente

tests/test_rom_edition_0137.py:14: Failed
____________ test_drive_sheet_shows_divergence_without_starting_job ____________

library = <checkpoint.library.Library object at 0x7fa8df398680>
app = <PySide6.QtWidgets.QApplication(0x37251560) at 0x7fa8df157d40>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7fa8df16cf20>

    def test_drive_sheet_shows_divergence_without_starting_job(library,app,monkeypatch):
        from checkpoint.rom_link_dialog import RomLinkDialog
        game=library.save_game({'title':'The Legend of Zelda: Ocarina of Time'})
        DriveScanner(library,None).record({'id':'edition-3d','name':'The Legend of Zelda - Ocarina of Time 3D.3ds'},'/Nintendo 3DS');library.sql.commit()
        called=[];monkeypatch.setattr('checkpoint.rom_link_dialog.run_link',lambda *a:called.append(a) or {'errors':[],'message':'fixture'})
>       dialog=RomLinkDialog(library,game);dialog.show();app.processEvents();assert dialog.results.count()==1
                                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       assert 0 == 1
E        +  where 0 = <built-in method count of PySide6.QtWidgets.QListWidget object at 0x7fa8df01e440>()
E        +    where <built-in method count of PySide6.QtWidgets.QListWidget object at 0x7fa8df01e440> = <PySide6.QtWidgets.QListWidget(0x37454910, name="romLinkResults") at 0x7fa8df01e440>.count
E        +      where <PySide6.QtWidgets.QListWidget(0x37454910, name="romLinkResults") at 0x7fa8df01e440> = <checkpoint.rom_link_dialog.RomLinkDialog(0x3733b8d0) at 0x7fa8defd97c0>.results

tests/test_rom_edition_0137.py:25: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[]
FAILED tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[Nintendo 64]
FAILED tests/test_rom_edition_0137.py::test_drive_sheet_shows_divergence_without_starting_job
3 failed in 0.26s

```

stderr integral:
```text

```

Código de saída: 1

## rom-local-ficha-execucao-corrigida

UTC: 2026-11-15T22:21:33.268820+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "tests/test_launch_0135.py", "tests/test_sessions_0135.py", "tests/test_layout_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.............
```

stderr integral:
```text

```

Código de saída: -15

## rom-local-ficha-regressao

UTC: 2026-11-15T22:21:35.527473+00:00

Comando: `["timeout", "60s", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "tests/test_launch_0135.py", "tests/test_sessions_0135.py", "tests/test_layout_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.............................                                            [100%]
29 passed in 1.72s

```

stderr integral:
```text

```

Código de saída: 0

## rom-edicao-depois

UTC: 2026-11-15T22:22:08.524068+00:00

Comando: `["timeout", "60s", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_rom_edition_0137.py", "tests/test_rom_link_0134.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
................                                                         [100%]
16 passed in 1.99s

```

stderr integral:
```text

```

Código de saída: 0

## rom-local-capturas

UTC: 2026-11-15T22:23:23.971030+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/rom-local-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/rom-local-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## rom-local-regressoes-completas

UTC: 2026-11-15T22:24:56.066542+00:00

Comando: `["timeout", "90s", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_local_rom_0137.py", "tests/test_rom_edition_0137.py", "tests/test_rom_link_0134.py", "tests/test_launch_0135.py", "tests/test_sessions_0135.py", "tests/test_layout_0134.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.................................................                        [100%]
49 passed in 3.73s

```

stderr integral:
```text

```

Código de saída: 0

## elevacao-antes

UTC: 2026-11-15T22:30:44.368184+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_elevation_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFF                                                                      [100%]
=================================== FAILURES ===================================
_______ test_uac_handoff_preserves_arguments_paths_and_original_identity _______

folder = PosixPath('/tmp/0c2ff207976a47239b494128dbd20342')

    def test_uac_handoff_preserves_arguments_paths_and_original_identity(folder):
>       from checkpoint.elevation import elevate_startup
E       ModuleNotFoundError: No module named 'checkpoint.elevation'

tests/test_elevation_0137.py:17: ModuleNotFoundError
________ test_uac_cancel_and_other_account_never_retry_or_prepare_data _________

folder = PosixPath('/tmp/4388d7a7863e483aaf3ed0ea8e25446b')

    def test_uac_cancel_and_other_account_never_retry_or_prepare_data(folder):
>       from checkpoint.elevation import elevate_startup,ElevationCancelled
E       ModuleNotFoundError: No module named 'checkpoint.elevation'

tests/test_elevation_0137.py:30: ModuleNotFoundError
_______ test_already_elevated_same_account_continues_without_new_prompt ________

folder = PosixPath('/tmp/978517783cf2447a9467c2a3d7d16db5')

    def test_already_elevated_same_account_continues_without_new_prompt(folder):
>       from checkpoint.elevation import elevate_startup
E       ModuleNotFoundError: No module named 'checkpoint.elevation'

tests/test_elevation_0137.py:40: ModuleNotFoundError
=========================== short test summary info ============================
FAILED tests/test_elevation_0137.py::test_uac_handoff_preserves_arguments_paths_and_original_identity
FAILED tests/test_elevation_0137.py::test_uac_cancel_and_other_account_never_retry_or_prepare_data
FAILED tests/test_elevation_0137.py::test_already_elevated_same_account_continues_without_new_prompt
3 failed in 0.04s

```

stderr integral:
```text

```

Código de saída: 1

## previa-carregando-antes

UTC: 2026-11-16T01:02:54.228848+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_loading_preview_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_ test_loading_preview_text_fits_without_cutting[Pok\xe9mon FireRed and LeafGreen+] _

library = <checkpoint.library.Library object at 0x7f85bcad7ef0>
app = <PySide6.QtWidgets.QApplication(0x1ee11a60) at 0x7f85bcaa7140>
title = 'Pokémon FireRed and LeafGreen+'

    @pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
    def test_loading_preview_text_fits_without_cutting(library,app,title):
        dialog=GameDialog(library=library);quick=dialog.quick_add
        quick.timer.stop();quick.art.setText('Carregando prévia…')
        quick.show_result(MetadataResult('rawg','1',title,platforms=('Game Boy Advance',)))
        dialog.show()
        try:
            for _ in range(6):app.processEvents()
            metrics=QFontMetrics(quick.art.font())
            required=metrics.boundingRect(QRect(0,0,quick.art.width(),1000),Qt.TextWordWrap,quick.art.text())
>           assert quick.art.wordWrap()
E           assert False
E            +  where False = <built-in method wordWrap of PySide6.QtWidgets.QLabel object at 0x7f85bbc40c80>()
E            +    where <built-in method wordWrap of PySide6.QtWidgets.QLabel object at 0x7f85bbc40c80> = <PySide6.QtWidgets.QLabel(0x1f3d61c0, name="addPreviewArt") at 0x7f85bbc40c80>.wordWrap
E            +      where <PySide6.QtWidgets.QLabel(0x1f3d61c0, name="addPreviewArt") at 0x7f85bbc40c80> = <checkpoint.quick_add.QuickAdd(0x1f36b2e0) at 0x7f85bc828bc0>.art

tests/test_loading_preview_0137.py:18: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
_ test_loading_preview_text_fits_without_cutting[The Legend of Zelda: Ocarina of Time 3D] _

library = <checkpoint.library.Library object at 0x7f85bbadc200>
app = <PySide6.QtWidgets.QApplication(0x1ee11a60) at 0x7f85bcaa7140>
title = 'The Legend of Zelda: Ocarina of Time 3D'

    @pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
    def test_loading_preview_text_fits_without_cutting(library,app,title):
        dialog=GameDialog(library=library);quick=dialog.quick_add
        quick.timer.stop();quick.art.setText('Carregando prévia…')
        quick.show_result(MetadataResult('rawg','1',title,platforms=('Game Boy Advance',)))
        dialog.show()
        try:
            for _ in range(6):app.processEvents()
            metrics=QFontMetrics(quick.art.font())
            required=metrics.boundingRect(QRect(0,0,quick.art.width(),1000),Qt.TextWordWrap,quick.art.text())
>           assert quick.art.wordWrap()
E           assert False
E            +  where False = <built-in method wordWrap of PySide6.QtWidgets.QLabel object at 0x7f85bbad9100>()
E            +    where <built-in method wordWrap of PySide6.QtWidgets.QLabel object at 0x7f85bbad9100> = <PySide6.QtWidgets.QLabel(0x1f706120, name="addPreviewArt") at 0x7f85bbad9100>.wordWrap
E            +      where <PySide6.QtWidgets.QLabel(0x1f706120, name="addPreviewArt") at 0x7f85bbad9100> = <checkpoint.quick_add.QuickAdd(0x1f6cc8b0) at 0x7f85bbad8dc0>.art

tests/test_loading_preview_0137.py:18: AssertionError
=========================== short test summary info ============================
FAILED tests/test_loading_preview_0137.py::test_loading_preview_text_fits_without_cutting[Pok\xe9mon FireRed and LeafGreen+]
FAILED tests/test_loading_preview_0137.py::test_loading_preview_text_fits_without_cutting[The Legend of Zelda: Ocarina of Time 3D]
2 failed in 0.44s

```

stderr integral:
```text

```

Código de saída: 1

## previa-carregando-depois

UTC: 2026-11-16T01:03:22.647098+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_loading_preview_0137.py", "tests/test_reference_layout_0128.py", "tests/test_quick_add.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..................                                                       [100%]
18 passed in 1.79s

```

stderr integral:
```text

```

Código de saída: 0

## desejos-filtro-antes

UTC: 2026-11-16T01:09:38.942955+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_platform_filter_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_wish_platform_dropdown_filters_families_without_changing_games[sample0] _

ui = (<checkpoint.window.MainWindow(0xccb4930) at 0x7f2d9548fb00>, 1)
app = <PySide6.QtWidgets.QApplication(0xc8e6090) at 0x7f2d95432c80>

    def test_wish_platform_dropdown_filters_families_without_changing_games(ui,app):
        w,_=ui;ids={}
        for platform in ('PC','Nintendo Switch','PlayStation 5','PlayStation 2','Xbox Series X/S','Game Boy Advance'):
            i=w.library.save_game({'title':'Desejo '+platform,'platform':platform});ids[platform]=i
            with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        before=[tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(2);app.processEvents()
        for key,expected in [('pc',{'PC'}),('switch',{'Nintendo Switch'}),('playstation',{'PlayStation 5','PlayStation 2'}),('xbox',{'Xbox Series X/S'})]:
>           combo=w.pages[2].findChild(QComboBox,'wishlistPlatform');assert combo is not None
                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
E           assert None is not None

tests/test_wish_platform_filter_0137.py:14: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_wish_platform_dropdown_filters_families_without_changing_games[sample1] _

ui = (<checkpoint.window.MainWindow(0xce2ba70) at 0x7f2d9548f980>, 1)
app = <PySide6.QtWidgets.QApplication(0xc8e6090) at 0x7f2d95432c80>

    def test_wish_platform_dropdown_filters_families_without_changing_games(ui,app):
        w,_=ui;ids={}
        for platform in ('PC','Nintendo Switch','PlayStation 5','PlayStation 2','Xbox Series X/S','Game Boy Advance'):
            i=w.library.save_game({'title':'Desejo '+platform,'platform':platform});ids[platform]=i
            with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        before=[tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(2);app.processEvents()
        for key,expected in [('pc',{'PC'}),('switch',{'Nintendo Switch'}),('playstation',{'PlayStation 5','PlayStation 2'}),('xbox',{'Xbox Series X/S'})]:
>           combo=w.pages[2].findChild(QComboBox,'wishlistPlatform');assert combo is not None
                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
E           assert None is not None

tests/test_wish_platform_filter_0137.py:14: AssertionError
_____ test_empty_platform_filter_keeps_controls_and_clear_action[sample0] ______

ui = (<checkpoint.window.MainWindow(0xd46c3a0) at 0x7f2d95011d40>, 1)
app = <PySide6.QtWidgets.QApplication(0xc8e6090) at 0x7f2d95432c80>

    def test_empty_platform_filter_keeps_controls_and_clear_action(ui,app):
        w,i=ui
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        w.navigate(2);app.processEvents();combo=w.pages[2].findChild(QComboBox,'wishlistPlatform')
>       assert combo is not None
E       assert None is not None

tests/test_wish_platform_filter_0137.py:32: AssertionError
_____ test_empty_platform_filter_keeps_controls_and_clear_action[sample1] ______

ui = (<checkpoint.window.MainWindow(0xcf0b780) at 0x7f2d933bfe40>, 1)
app = <PySide6.QtWidgets.QApplication(0xc8e6090) at 0x7f2d95432c80>

    def test_empty_platform_filter_keeps_controls_and_clear_action(ui,app):
        w,i=ui
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
        w.navigate(2);app.processEvents();combo=w.pages[2].findChild(QComboBox,'wishlistPlatform')
>       assert combo is not None
E       assert None is not None

tests/test_wish_platform_filter_0137.py:32: AssertionError
=========================== short test summary info ============================
FAILED tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample0]
FAILED tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample1]
FAILED tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample0]
FAILED tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample1]
4 failed in 0.65s

```

stderr integral:
```text

```

Código de saída: 1

## desejos-filtro-depois

UTC: 2026-11-16T01:10:31.321553+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_platform_filter_0137.py", "tests/test_prices_0129.py", "tests/test_layout_0134.py", "tests/test_wish_navigation_0136.py", "tests/test_price_integrity_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
................................                                         [100%]
32 passed in 5.61s

```

stderr integral:
```text

```

Código de saída: 0

## desejos-filtro-captura

UTC: 2026-11-16T01:11:20.771430+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/desejos-filtro-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/desejos-filtro-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## desejos-espaco-antes

UTC: 2026-11-16T01:16:39.920397+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_spacing_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_offer_link_follows_discount_without_large_fixed_gap[sample0] _______

ui = (<checkpoint.window.MainWindow(0x37b2be20) at 0x7f5fe24f84c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x37735b30) at 0x7f5fe27dcbc0>

    def test_offer_link_follows_discount_without_large_fixed_gap(ui,app):
        w,i=ui
        with w.library.sql:
            w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
            w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
        w.library.set_setting(f'prices.ggdeals.{i}',{'state':'ready','currency':'BRL','retail':3000,'offer_context':{'platform':'PC','steam':str(i)},'offers':[{'cents':3000,'original':6000,'kind':'retail','shop':'Loja teste','url':'https://gg.deals/br/redirect/test/'}]})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(2)
            for _ in range(7):app.processEvents()
            card=w.pages[2].findChild(WishCard)
            discount=card.findChild(QLabel,'priceDiscount')
            link=next(b for b in card.findChildren(QPushButton) if b.text().startswith('Ver ofertas'))
            bottom=discount.mapTo(card,discount.rect().bottomLeft()).y();top=link.mapTo(card,QPoint()).y()
>           assert 0<=top-bottom<=28
E           assert (507 - 456) <= 28

tests/test_wish_spacing_0137.py:20: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_offer_link_follows_discount_without_large_fixed_gap[sample1] _______

ui = (<checkpoint.window.MainWindow(0x3781e9b0) at 0x7f5fe2660100>, 1)
app = <PySide6.QtWidgets.QApplication(0x37735b30) at 0x7f5fe27dcbc0>

    def test_offer_link_follows_discount_without_large_fixed_gap(ui,app):
        w,i=ui
        with w.library.sql:
            w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,))
            w.library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
        w.library.set_setting(f'prices.ggdeals.{i}',{'state':'ready','currency':'BRL','retail':3000,'offer_context':{'platform':'PC','steam':str(i)},'offers':[{'cents':3000,'original':6000,'kind':'retail','shop':'Loja teste','url':'https://gg.deals/br/redirect/test/'}]})
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(2)
            for _ in range(7):app.processEvents()
            card=w.pages[2].findChild(WishCard)
            discount=card.findChild(QLabel,'priceDiscount')
            link=next(b for b in card.findChildren(QPushButton) if b.text().startswith('Ver ofertas'))
            bottom=discount.mapTo(card,discount.rect().bottomLeft()).y();top=link.mapTo(card,QPoint()).y()
>           assert 0<=top-bottom<=28
E           assert (507 - 456) <= 28

tests/test_wish_spacing_0137.py:20: AssertionError
=========================== short test summary info ============================
FAILED tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample0]
FAILED tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample1]
2 failed in 0.42s

```

stderr integral:
```text

```

Código de saída: 1

## desejos-espaco-depois

UTC: 2026-11-16T01:17:16.614140+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_spacing_0137.py", "tests/test_wish_platform_filter_0137.py", "tests/test_prices_0129.py", "tests/test_wishlist_prices.py", "tests/test_wishes_0135.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..........................................................               [100%]
58 passed in 21.19s

```

stderr integral:
```text

```

Código de saída: 0

## elevacao-depois

UTC: 2026-11-16T01:17:41.185057+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_elevation_0137.py", "tests/test_migration.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text

no tests ran in 0.00s

```

stderr integral:
```text
ERROR: file or directory not found: tests/test_migration.py


```

Código de saída: 4

## elevacao-contrato

UTC: 2026-11-16T01:17:50.883312+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_elevation_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...                                                                      [100%]
3 passed in 0.02s

```

stderr integral:
```text

```

Código de saída: 0

## desejos-compactos-capturas

UTC: 2026-11-16T01:17:55.372780+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/desejos-compactos-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/desejos-compactos-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## elevacao-migracao-ordem

UTC: 2026-11-16T01:19:37.710326+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_elevation_0137.py", "tests/test_data_migration.py", "tests/test_migrations.py", "tests/test_updates.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
......................................                                   [100%]
38 passed in 1.22s

```

stderr integral:
```text

```

Código de saída: 0

## desejos-previa-regressoes

UTC: 2026-11-16T01:20:59.625823+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_spacing_0137.py", "tests/test_wish_platform_filter_0137.py", "tests/test_loading_preview_0137.py", "tests/test_price_integrity_0136.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
....................                                                     [100%]
20 passed in 1.55s

```

stderr integral:
```text

```

Código de saída: 0

## janela-controles-antes

UTC: 2026-11-16T01:24:16.288171+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_window_controls_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FFF                                                                      [100%]
=================================== FAILURES ===================================
______ test_window_controls_use_regular_window_close_and_restore[sample0] ______

ui = (<checkpoint.window.MainWindow(0x3e68fc80) at 0x7f1ed7ab8d00>, 1)
app = <PySide6.QtWidgets.QApplication(0x3e5f4780) at 0x7f1ed7c713c0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f1ed7c7dc40>

    def test_window_controls_use_regular_window_close_and_restore(ui,app,monkeypatch):
        w,_=ui
        bar=w.findChild(type(w.menuWidget()),'windowControls')
>       assert bar is not None
E       assert None is not None

tests/test_window_controls_0137.py:9: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_window_controls_use_regular_window_close_and_restore[sample1] ______

ui = (<checkpoint.window.MainWindow(0x3ed23d30) at 0x7f1ed7ab8bc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x3e5f4780) at 0x7f1ed7c713c0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f1ed7609eb0>

    def test_window_controls_use_regular_window_close_and_restore(ui,app,monkeypatch):
        w,_=ui
        bar=w.findChild(type(w.menuWidget()),'windowControls')
>       assert bar is not None
E       assert None is not None

tests/test_window_controls_0137.py:9: AssertionError
_________ test_native_hit_regions_preserve_resize_and_caption_controls _________

    def test_native_hit_regions_preserve_resize_and_caption_controls():
>       from checkpoint.window_controls import border_hit
E       ModuleNotFoundError: No module named 'checkpoint.window_controls'

tests/test_window_controls_0137.py:21: ModuleNotFoundError
=========================== short test summary info ============================
FAILED tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample0]
FAILED tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample1]
FAILED tests/test_window_controls_0137.py::test_native_hit_regions_preserve_resize_and_caption_controls
3 failed in 0.36s

```

stderr integral:
```text

```

Código de saída: 1

## janela-controles-depois

UTC: 2026-11-16T01:26:49.180507+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_window_controls_0137.py", "tests/test_banner_resize_0136.py", "tests/test_home_layout_0137.py", "tests/test_capture_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...............................                                          [100%]
31 passed in 3.55s

```

stderr integral:
```text

```

Código de saída: 0

## janela-integrada-capturas

UTC: 2026-11-16T01:27:46.503786+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/janela-v1"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/janela-v1

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## scroll-async-antes

UTC: 2026-11-16T01:36:34.235183+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_artwork_async_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_________ test_cold_images_decode_outside_gui_and_do_not_block_events __________

app = <PySide6.QtWidgets.QApplication(0x92adfe0) at 0x7f99eb2215c0>
folder = PosixPath('/tmp/62ecaf8f24124413bc71af4935a8eea1')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f99e651d490>

    def test_cold_images_decode_outside_gui_and_do_not_block_events(app, folder, monkeypatch):
        from checkpoint import artwork_cache
    
>       original = artwork_cache._read_image
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: module 'checkpoint.artwork_cache' has no attribute '_read_image'

tests/test_artwork_async_0137.py:20: AttributeError
__________ test_async_cache_bounds_queue_and_preserves_changed_image ___________

app = <PySide6.QtWidgets.QApplication(0x92adfe0) at 0x7f99eb2215c0>
folder = PosixPath('/tmp/68f21cd9aa4947e5af1fa97e3ac59658')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f99e5421d30>

    def test_async_cache_bounds_queue_and_preserves_changed_image(app, folder, monkeypatch):
        from checkpoint import artwork_cache
    
>       original = artwork_cache._read_image
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: module 'checkpoint.artwork_cache' has no attribute '_read_image'

tests/test_artwork_async_0137.py:60: AttributeError
=========================== short test summary info ============================
FAILED tests/test_artwork_async_0137.py::test_cold_images_decode_outside_gui_and_do_not_block_events
FAILED tests/test_artwork_async_0137.py::test_async_cache_bounds_queue_and_preserves_changed_image
2 failed in 0.25s

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 1

## scroll-async-depois

UTC: 2026-11-16T01:37:29.877326+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_artwork_async_0137.py", "tests/test_grid_performance_0137.py", "tests/test_library_list_0137.py", "tests/test_banner_fallback_0134.py", "tests/test_layout_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..........FFFF........                                                   [100%]
=================================== FAILURES ===================================
____________ test_banner_fills_grid_and_home_without_cover[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x1d1e2ed0) at 0x7f3a45552dc0>, 1)
folder = PosixPath('/tmp/fdda67cbb21345fe83bf49b5f73fdc93')
app = <PySide6.QtWidgets.QApplication(0x1cda6c30) at 0x7f3a3f62b940>

    def test_banner_fills_grid_and_home_without_cover(ui,folder,app):
        from checkpoint.ui_components import GameTile
        from checkpoint.cover_art import cover_pixmap
        w,i=ui;image=QImage(400,600,QImage.Format_RGB32);color=QColor('#a63772');image.fill(color)
        path=folder/'banner.png';assert image.save(str(path))
        w.library.save_game({'title':w.library.get(i)['title'],'banner':str(path)},i)
        game=w.library.get(i);pix=cover_pixmap(game)
        assert pix.width()==400 and pix.height()==600
        tile=GameTile(game,lambda:None,width=200);tile.show();app.processEvents()
        try:
            result=tile.grab().toImage();assert result.width()>=200 and result.height()>=300
            assert result.pixelColor(20,20)==color and result.pixelColor(180,280)==color
            w.navigate(1);app.processEvents();cell=w.gallery.visualItemRect(w.gallery.item(0));view=w.gallery.viewport().grab().toImage()
>           assert view.pixelColor(cell.left()+20,cell.top()+20)==color
E           assert PySide6.QtGui.QColor.fromRgbF(0.125490, 0.172549, 0.227451, 1.000000) == PySide6.QtGui.QColor.fromRgbF(0.650980, 0.215686, 0.447059, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.125490, 0.172549, 0.227451, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a45550640>((0 + 20), (0 + 20))
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a45550640> = <PySide6.QtGui.QImage(QSize(748, 544),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2992,sizeInBytes=1627648) at 0x7f3a45550640>.pixelColor
E            +    and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f3a3c5f4bc0>()
E            +      where <built-in method left of PySide6.QtCore.QRect object at 0x7f3a3c5f4bc0> = PySide6.QtCore.QRect(0, 0, 249, 410).left
E            +    and   0 = <built-in method top of PySide6.QtCore.QRect object at 0x7f3a3c5f4bc0>()
E            +      where <built-in method top of PySide6.QtCore.QRect object at 0x7f3a3c5f4bc0> = PySide6.QtCore.QRect(0, 0, 249, 410).top

tests/test_banner_fallback_0134.py:17: AssertionError
____________ test_banner_fills_grid_and_home_without_cover[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x1d6cc360) at 0x7f3a45576180>, 1)
folder = PosixPath('/tmp/2cc80aa2fd674d56a8fc7ca80455a173')
app = <PySide6.QtWidgets.QApplication(0x1cda6c30) at 0x7f3a3f62b940>

    def test_banner_fills_grid_and_home_without_cover(ui,folder,app):
        from checkpoint.ui_components import GameTile
        from checkpoint.cover_art import cover_pixmap
        w,i=ui;image=QImage(400,600,QImage.Format_RGB32);color=QColor('#a63772');image.fill(color)
        path=folder/'banner.png';assert image.save(str(path))
        w.library.save_game({'title':w.library.get(i)['title'],'banner':str(path)},i)
        game=w.library.get(i);pix=cover_pixmap(game)
        assert pix.width()==400 and pix.height()==600
        tile=GameTile(game,lambda:None,width=200);tile.show();app.processEvents()
        try:
            result=tile.grab().toImage();assert result.width()>=200 and result.height()>=300
            assert result.pixelColor(20,20)==color and result.pixelColor(180,280)==color
            w.navigate(1);app.processEvents();cell=w.gallery.visualItemRect(w.gallery.item(0));view=w.gallery.viewport().grab().toImage()
>           assert view.pixelColor(cell.left()+20,cell.top()+20)==color
E           assert PySide6.QtGui.QColor.fromRgbF(0.125490, 0.172549, 0.227451, 1.000000) == PySide6.QtGui.QColor.fromRgbF(0.650980, 0.215686, 0.447059, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.125490, 0.172549, 0.227451, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a3c4fc300>((0 + 20), (0 + 20))
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a3c4fc300> = <PySide6.QtGui.QImage(QSize(1148, 582),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=4592,sizeInBytes=2672544) at 0x7f3a3c4fc300>.pixelColor
E            +    and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f3a3f4c2180>()
E            +      where <built-in method left of PySide6.QtCore.QRect object at 0x7f3a3f4c2180> = PySide6.QtCore.QRect(0, 0, 229, 380).left
E            +    and   0 = <built-in method top of PySide6.QtCore.QRect object at 0x7f3a3f4c2180>()
E            +      where <built-in method top of PySide6.QtCore.QRect object at 0x7f3a3f4c2180> = PySide6.QtCore.QRect(0, 0, 229, 380).top

tests/test_banner_fallback_0134.py:17: AssertionError
_______________ test_list_uses_fixed_logo_area_or_title[sample0] _______________

ui = (<checkpoint.window.MainWindow(0x1dbfc470) at 0x7f3a45481200>, 1)
app = <PySide6.QtWidgets.QApplication(0x1cda6c30) at 0x7f3a3f62b940>
folder = PosixPath('/tmp/1cf5ba2dec5a4cd19090cfd6ee58d852')

    def test_list_uses_fixed_logo_area_or_title(ui,app,folder):
        w,i=ui;image=QImage(240,80,QImage.Format_RGB32);image.fill(QColor('#18aa60'));logo=folder/'logo.png';assert image.save(str(logo))
        image.fill(QColor('#ff0000'));cover=folder/'cover.png';assert image.save(str(cover))
        w.library.save_game({'title':w.library.get(i)['title'],'logo':str(logo),'cover':str(cover)},i)
        w.view.setCurrentIndex(1);w.refresh_library();app.processEvents()
        assert w.game_list.item(0).text()==w.library.get(i)['title']
        rect=w.game_list.visualItemRect(w.game_list.item(0))
        frame=w.game_list.viewport().grab(rect).toImage()
>       assert frame.pixelColor(62,36)==QColor('#18aa60')
E       AssertionError: assert PySide6.QtGui.QColor.fromRgbF(0.219608, 0.266667, 0.321569, 1.000000) == PySide6.QtGui.QColor.fromRgbF(0.094118, 0.666667, 0.376471, 1.000000)
E        +  where PySide6.QtGui.QColor.fromRgbF(0.219608, 0.266667, 0.321569, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a3c399e80>(62, 36)
E        +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a3c399e80> = <PySide6.QtGui.QImage(QSize(620, 84),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2480,sizeInBytes=208320) at 0x7f3a3c399e80>.pixelColor
E        +  and   PySide6.QtGui.QColor.fromRgbF(0.094118, 0.666667, 0.376471, 1.000000) = QColor('#18aa60')

tests/test_layout_0134.py:16: AssertionError
_______________ test_list_uses_fixed_logo_area_or_title[sample1] _______________

ui = (<checkpoint.window.MainWindow(0x1d55c4d0) at 0x7f3a3c378680>, 1)
app = <PySide6.QtWidgets.QApplication(0x1cda6c30) at 0x7f3a3f62b940>
folder = PosixPath('/tmp/e6e12e2befc54cc8b9e5d64809dd4ee8')

    def test_list_uses_fixed_logo_area_or_title(ui,app,folder):
        w,i=ui;image=QImage(240,80,QImage.Format_RGB32);image.fill(QColor('#18aa60'));logo=folder/'logo.png';assert image.save(str(logo))
        image.fill(QColor('#ff0000'));cover=folder/'cover.png';assert image.save(str(cover))
        w.library.save_game({'title':w.library.get(i)['title'],'logo':str(logo),'cover':str(cover)},i)
        w.view.setCurrentIndex(1);w.refresh_library();app.processEvents()
        assert w.game_list.item(0).text()==w.library.get(i)['title']
        rect=w.game_list.visualItemRect(w.game_list.item(0))
        frame=w.game_list.viewport().grab(rect).toImage()
>       assert frame.pixelColor(62,36)==QColor('#18aa60')
E       AssertionError: assert PySide6.QtGui.QColor.fromRgbF(0.219608, 0.266667, 0.321569, 1.000000) == PySide6.QtGui.QColor.fromRgbF(0.094118, 0.666667, 0.376471, 1.000000)
E        +  where PySide6.QtGui.QColor.fromRgbF(0.219608, 0.266667, 0.321569, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a45587f40>(62, 36)
E        +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f3a45587f40> = <PySide6.QtGui.QImage(QSize(620, 84),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2480,sizeInBytes=208320) at 0x7f3a45587f40>.pixelColor
E        +  and   PySide6.QtGui.QColor.fromRgbF(0.094118, 0.666667, 0.376471, 1.000000) = QColor('#18aa60')

tests/test_layout_0134.py:16: AssertionError
=========================== short test summary info ============================
FAILED tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample0]
FAILED tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample1]
FAILED tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample0]
FAILED tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample1]
4 failed, 18 passed in 2.36s

```

stderr integral:
```text

```

Código de saída: 1

## scroll-async-regressao

UTC: 2026-11-16T01:38:31.157078+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_artwork_async_0137.py", "tests/test_grid_performance_0137.py", "tests/test_library_list_0137.py", "tests/test_banner_fallback_0134.py", "tests/test_layout_0134.py", "tests/test_visual_0132.py", "tests/test_cover_preview_0135.py", "tests/test_cover_sizes_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text

no tests ran in 0.00s

```

stderr integral:
```text
ERROR: file or directory not found: tests/test_cover_sizes_0136.py


```

Código de saída: 4

## scroll-async-regressao-final

UTC: 2026-11-16T01:38:55.862970+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_artwork_async_0137.py", "tests/test_grid_performance_0137.py", "tests/test_library_list_0137.py", "tests/test_banner_fallback_0134.py", "tests/test_layout_0134.py", "tests/test_visual_0132.py", "tests/test_cover_preview_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
........................................................................ [ 93%]
.....                                                                    [100%]
77 passed in 8.08s

```

stderr integral:
```text

```

Código de saída: 0

## scroll-async-extra

UTC: 2026-11-16T01:40:25.485054+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_artwork_async_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...                                                                      [100%]
3 passed in 0.50s

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## controles-uac-filtro-final

UTC: 2026-11-16T01:42:46.323390+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_window_controls_0137.py", "tests/test_elevation_0137.py", "tests/test_wish_platform_filter_0137.py", "tests/test_wish_spacing_0137.py", "tests/test_loading_preview_0137.py", "tests/test_banner_resize_0136.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
..................................................................       [100%]
66 passed in 7.14s

```

stderr integral:
```text

```

Código de saída: 0

## capturas-revisao-final

UTC: 2026-11-16T01:43:43.428818+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/revisao-final"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/revisao-final

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## suite-completa-0137

UTC: 2026-11-16T01:51:54.909000+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
........................................................................ [ 10%]
........................................................................ [ 20%]
........................................................................ [ 31%]
........................................................................ [ 41%]
........................................................................ [ 52%]
........................................................................ [ 62%]
........................................................................ [ 73%]
........................................................................ [ 83%]
........................................................................ [ 93%]
..........................................                               [100%]
690 passed in 476.40s (0:07:56)

```

stderr integral:
```text

```

Código de saída: 0

## previa-vazia-antes

UTC: 2026-11-16T01:52:49.294795+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_loading_preview_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_ test_loading_preview_is_blank_until_cover_arrives[Pok\xe9mon FireRed and LeafGreen+] _

library = <checkpoint.library.Library object at 0x7f2f2d8a3e90>
app = <PySide6.QtWidgets.QApplication(0x11d400d0) at 0x7f2f2d89d4c0>
folder = PosixPath('/tmp/4d6a92d4684843c69b637eba2465ebaa')
title = 'Pokémon FireRed and LeafGreen+'

    @pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
    def test_loading_preview_is_blank_until_cover_arrives(library,app,folder,title):
        dialog=GameDialog(library=library);quick=dialog.quick_add
        quick.timer.stop();quick.art.setText('Carregando prévia…')
        result=MetadataResult('rawg','1',title,platforms=('Game Boy Advance',))
        quick.show_result(result)
        dialog.show()
        try:
            for _ in range(6):app.processEvents()
>           assert quick.art.text()=='' and quick.art.pixmap().isNull()
E           AssertionError: assert ('Carregando' == ''
E             
E             + Carregando)

tests/test_loading_preview_0137.py:18: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
_ test_loading_preview_is_blank_until_cover_arrives[The Legend of Zelda: Ocarina of Time 3D] _

library = <checkpoint.library.Library object at 0x7f2f2c8fd310>
app = <PySide6.QtWidgets.QApplication(0x11d400d0) at 0x7f2f2d89d4c0>
folder = PosixPath('/tmp/a5fe29a07024436b8877ace3d00ea6e8')
title = 'The Legend of Zelda: Ocarina of Time 3D'

    @pytest.mark.parametrize('title',['Pokémon FireRed and LeafGreen+','The Legend of Zelda: Ocarina of Time 3D'])
    def test_loading_preview_is_blank_until_cover_arrives(library,app,folder,title):
        dialog=GameDialog(library=library);quick=dialog.quick_add
        quick.timer.stop();quick.art.setText('Carregando prévia…')
        result=MetadataResult('rawg','1',title,platforms=('Game Boy Advance',))
        quick.show_result(result)
        dialog.show()
        try:
            for _ in range(6):app.processEvents()
>           assert quick.art.text()=='' and quick.art.pixmap().isNull()
E           AssertionError: assert ('Carregando' == ''
E             
E             + Carregando)

tests/test_loading_preview_0137.py:18: AssertionError
=========================== short test summary info ============================
FAILED tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[Pok\xe9mon FireRed and LeafGreen+]
FAILED tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[The Legend of Zelda: Ocarina of Time 3D]
2 failed in 0.34s

```

stderr integral:
```text

```

Código de saída: 1

## previa-vazia-depois

UTC: 2026-11-16T01:53:28.033512+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_loading_preview_0137.py", "tests/test_quick_add.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
......................................................                   [100%]
54 passed in 14.07s

```

stderr integral:
```text

```

Código de saída: 0

## capturas-previa-vazia

UTC: 2026-11-16T01:54:01.471976+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_0137_review.py", "/workspace/work/evidence-0137/revisao-previa-vazia"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
/workspace/work/evidence-0137/revisao-previa-vazia

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## ofertas-cache-temporal-antes

UTC: 2026-11-16T01:55:32.416432+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_data_0137.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
....FFFFF                                                                [100%]
=================================== FAILURES ===================================
_ test_home_does_not_present_unknown_expired_or_future_cache_as_current[None] __

library = <checkpoint.library.Library object at 0x7fdfa0fd2ba0>
checked_at = None

    @pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
    def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
        from checkpoint.home_data import wish_offers
        end=datetime(2026,11,16,12,tzinfo=timezone.utc)
        identities=[]
        for title in ('Portal 2','Hades'):
            identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
            with library.sql:
                library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
            library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
        before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
>       assert wish_offers(library,now=end)==[]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: wish_offers() got an unexpected keyword argument 'now'

tests/test_home_data_0137.py:77: TypeError
_ test_home_does_not_present_unknown_expired_or_future_cache_as_current[inv\xe1lida] _

library = <checkpoint.library.Library object at 0x7fdfa0fd7f80>
checked_at = 'inválida'

    @pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
    def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
        from checkpoint.home_data import wish_offers
        end=datetime(2026,11,16,12,tzinfo=timezone.utc)
        identities=[]
        for title in ('Portal 2','Hades'):
            identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
            with library.sql:
                library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
            library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
        before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
>       assert wish_offers(library,now=end)==[]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: wish_offers() got an unexpected keyword argument 'now'

tests/test_home_data_0137.py:77: TypeError
_ test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:00] _

library = <checkpoint.library.Library object at 0x7fdfa0fd78f0>
checked_at = '2026-11-16T12:00:00'

    @pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
    def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
        from checkpoint.home_data import wish_offers
        end=datetime(2026,11,16,12,tzinfo=timezone.utc)
        identities=[]
        for title in ('Portal 2','Hades'):
            identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
            with library.sql:
                library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
            library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
        before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
>       assert wish_offers(library,now=end)==[]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: wish_offers() got an unexpected keyword argument 'now'

tests/test_home_data_0137.py:77: TypeError
_ test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T11:00:00+00:00] _

library = <checkpoint.library.Library object at 0x7fdfa10604a0>
checked_at = '2026-11-16T11:00:00+00:00'

    @pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
    def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
        from checkpoint.home_data import wish_offers
        end=datetime(2026,11,16,12,tzinfo=timezone.utc)
        identities=[]
        for title in ('Portal 2','Hades'):
            identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
            with library.sql:
                library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
            library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
        before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
>       assert wish_offers(library,now=end)==[]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: wish_offers() got an unexpected keyword argument 'now'

tests/test_home_data_0137.py:77: TypeError
_ test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:01+00:00] _

library = <checkpoint.library.Library object at 0x7fdfa10603e0>
checked_at = '2026-11-16T12:00:01+00:00'

    @pytest.mark.parametrize('checked_at',[None,'inválida','2026-11-16T12:00:00','2026-11-16T11:00:00+00:00','2026-11-16T12:00:01+00:00'])
    def test_home_does_not_present_unknown_expired_or_future_cache_as_current(library,checked_at):
        from checkpoint.home_data import wish_offers
        end=datetime(2026,11,16,12,tzinfo=timezone.utc)
        identities=[]
        for title in ('Portal 2','Hades'):
            identity=library.save_game({'title':title,'platform':'PC'});identities.append(identity)
            with library.sql:
                library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(identity,))
                library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(identity,str(identity)))
            library.set_setting(f'prices.ggdeals.{identity}',{'state':'ready','retail':3000,'currency':'BRL','checked_at':checked_at,'offer_context':{'steam':str(identity),'platform':'PC'}})
        before=[library.setting(f'prices.ggdeals.{identity}') for identity in identities]
>       assert wish_offers(library,now=end)==[]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: wish_offers() got an unexpected keyword argument 'now'

tests/test_home_data_0137.py:77: TypeError
=========================== short test summary info ============================
FAILED tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[None]
FAILED tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[inv\xe1lida]
FAILED tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:00]
FAILED tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T11:00:00+00:00]
FAILED tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:01+00:00]
5 failed, 4 passed in 0.13s

```

stderr integral:
```text

```

Código de saída: 1

## ofertas-cache-temporal-depois

UTC: 2026-11-16T01:56:05.034149+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_data_0137.py", "tests/test_home_layout_0137.py", "tests/test_price_display_official.py", "tests/test_discount_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text

no tests ran in 0.00s

```

stderr integral:
```text
ERROR: file or directory not found: tests/test_discount_0136.py


```

Código de saída: 4

## ofertas-cache-temporal-final

UTC: 2026-11-16T01:56:15.378298+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_data_0137.py", "tests/test_home_layout_0137.py", "tests/test_price_display_official.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
...........................                                              [100%]
27 passed in 2.08s

```

stderr integral:
```text

```

Código de saída: 0

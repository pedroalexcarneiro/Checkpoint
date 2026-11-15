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

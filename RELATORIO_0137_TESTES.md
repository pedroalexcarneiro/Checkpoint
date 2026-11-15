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

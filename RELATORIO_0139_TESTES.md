# Checkpoint 0.1.39 — comandos e saídas integrais

Registros atuais desta rodada. Tentativas com erro/interrupção são preservadas e não contam como aprovação.
Qt offscreen/Linux e fixtures isoladas não homologam Windows do dono. Resultados Windows serão acrescentados ao relatório de lançamento.
Os blocos abaixo contêm stdout/stderr completos dos arquivos de evidência, sem o corte usado nas prévias do chat.

| Registro | Exit | Duração (s) |
|---|---:|---:|
| baseline | 0 | 559.901 |
| visual-before | 0 | 6.100 |
| regressions-before | 1 | 2.750 |
| regressions-before-corrected | 1 | 3.260 |
| extra-before | 0 | 1.083 |
| detail-before | 1 | 1.289 |
| home-after-first | 1 | 3.537 |
| home-visual-first | 0 | 5.529 |
| home-after | 0 | 5.208 |
| home-visual-second | 0 | 6.525 |
| wishes-after | 0 | 4.542 |
| home-letterbox-after | 0 | 4.185 |
| home-rounded-visual | 0 | 3.171 |
| memories-after | 0 | 2.890 |
| memories-visual | 0 | 1.402 |
| completions-after | 0 | 3.372 |
| cover-focus-after | 0 | 3.660 |
| memories-alignment-after | 0 | 3.526 |
| library-gutter-after | 1 | 3.459 |
| primary-icon-after | 1 | 0.983 |
| local-components-after | 0 | 4.781 |
| memories-preview-visual | 0 | 1.432 |
| black-after | 0 | 18.086 |
| appearance-visual | 0 | 2.415 |
| mixed-preview-after | 0 | 0.893 |
| icon-states-after | 1 | 0.800 |
| files-saves-after | 1 | 4.093 |
| files-saves-visual | 0 | 1.586 |
| settings-tabs-after | 0 | 19.770 |
| dialog-core-after | 0 | 4.478 |
| dialogs-management-after | -15 | 63.299 |
| dialog-trace | -15 | 35.728 |
| dialogs-management-retry | -11 | 75.144 |
| dialog-trace-second | -11 | 10.129 |
| dialogs-explicit-after | -15 | 87.975 |
| navigation-after | -15 | 33.691 |
| dialogs-navigation-final | 0 | 21.366 |
| navigation-visual | 0 | 1.347 |
| icon-and-trash-final | 0 | 2.226 |
| navigation-visual-updated | 0 | 1.567 |
| dialog-additional-after | 0 | 9.046 |
| startup-preserved-after | 1 | 65.035 |
| all-new-before-final | 0 | 6.453 |
| visual-final | 0 | 5.099 |
| startup-final | 0 | 3.824 |
| regressions-base-final | 1 | 4.581 |
| emulator-actions-after | 0 | 3.733 |
| emulator-actions-visual | 0 | 1.799 |
| session-dialog-spacing-after | 1 | 3.168 |
| session-dialog-spacing-visual | 0 | 1.699 |
| dialog-layout-final | 0 | 7.814 |
| dpi-150 | 0 | 5.229 |
| dpi-200 | 0 | 6.607 |
| full-linux | -15 | 385.593 |
| smoke-source | 0 | 1.094 |
| smoke-save | 0 | 0.865 |
| collect-final | 0 | 1.041 |
| verification | 0 | 0.337 |
| full-failures-isolated | 1 | 1.183 |
| full-regressions-fixed | 0 | 19.504 |
| full-linux-final | 1 | 579.505 |
| verification-final | 0 | 0.518 |
| visual-code-final | 0 | 5.900 |
| collect-current | 0 | 1.550 |
| remaining-failures-isolated | 1 | 1.557 |
| approved-expectations-after | 0 | 10.818 |
| full-linux-approved | 0 | 580.496 |
| verification-prepublish | 0 | 0.456 |

## baseline

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794849921.8456411,
  "exit_code": 0,
  "elapsed": 559.9005291461945
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 832 bytes; SHA-256 fb0b05894b362172dd1bcefa993f1918001647783498da638dc9844eec72b913:

````text
........................................................................ [ 10%]
........................................................................ [ 20%]
........................................................................ [ 30%]
........................................................................ [ 41%]
........................................................................ [ 51%]
........................................................................ [ 61%]
........................................................................ [ 72%]
........................................................................ [ 82%]
........................................................................ [ 92%]
....................................................                     [100%]
700 passed in 557.77s (0:09:17)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## visual-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0137_review.py",
    "/workspace/work/evidence-0139/antes"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794849947.5288055,
  "exit_code": 0,
  "elapsed": 6.100472688674927
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0137_review.py /workspace/work/evidence-0139/antes
```

stdout integral — 36 bytes; SHA-256 26fb16b66c29146e10d67701fd1b37b701168915791d7f2e543289ce69d4f90d:

````text
/workspace/work/evidence-0139/antes
````

stderr integral — 286 bytes; SHA-256 e4dd96b236e73919f55e2570ea325d645ed48b502c4bfc98945503b2dc2a85e1:

````text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## regressions-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850093.2939565,
  "exit_code": 1,
  "elapsed": 2.749879837036133
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 28008 bytes; SHA-256 1cfe1d250689ef66252a80590ad25ac3bd8d32124851bd6ec72fe6ab3d08b0a9:

````text
FFFFFFFFFFFFFFFFFFFFFFF                                                  [100%]
=================================== FAILURES ===================================
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0] ______

ui = (<checkpoint.window.MainWindow(0x13cb5ff0) at 0x7fb7607c7240>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/Checkpoint/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1] ______

ui = (<checkpoint.window.MainWindow(0x1435ff30) at 0x7fb7607c7780>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/Checkpoint/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
______ test_recent_cards_height_follows_content_and_button_fits[sample0] _______

ui = (<checkpoint.window.MainWindow(0x13ee5040) at 0x7fb760726f00>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7fb7602fa190>)

tests/test_home_polish_0139.py:60: AssertionError
______ test_recent_cards_height_follows_content_and_button_fits[sample1] _______

ui = (<checkpoint.window.MainWindow(0x14282e40) at 0x7fb760725f40>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7fb76041f5e0>)

tests/test_home_polish_0139.py:60: AssertionError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0] _____

ui = (<checkpoint.window.MainWindow(0x141205d0) at 0x7fb760700480>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1] _____

ui = (<checkpoint.window.MainWindow(0x13f01270) at 0x7fb760726fc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0] _

ui = (<checkpoint.window.MainWindow(0x14001150) at 0x7fb760732080>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>
folder = PosixPath('/tmp/e20ee3c1bebb47f4aa2d9dce97a2c321')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb760197f40>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb760197f40> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fb760197f40>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb760197f40>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb760197f40> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fb760197f40>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1] _

ui = (<checkpoint.window.MainWindow(0x13f4ddb0) at 0x7fb76044e780>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>
folder = PosixPath('/tmp/860c92f1bcb148e4ad731e5c122cfd75')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb7602dc740>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb7602dc740> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fb7602dc740>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb7602dc740>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fb7602dc740> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fb7602dc740>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0] _____

ui = (<checkpoint.window.MainWindow(0x1428d650) at 0x7fb7601996c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7fb76031e400>()
E                +    where <built-in method width of WishCard object at 0x7fb76031e400> = <checkpoint.collection_views.WishCard(0x14605df0, name="panel") at 0x7fb76031e400>.width

tests/test_polish_0139.py:28: AssertionError
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1] _____

ui = (<checkpoint.window.MainWindow(0x14b80550) at 0x7fb760385d40>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7fb7601d9bc0>()
E                +    where <built-in method width of WishCard object at 0x7fb7601d9bc0> = <checkpoint.collection_views.WishCard(0x1447c870, name="panel") at 0x7fb7601d9bc0>.width

tests/test_polish_0139.py:28: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x14794310) at 0x7fb7601b04c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        for game_id in (identity, other):
            w.library.add_diary(game_id, 'Texto curto que deve permanecer íntegro.')
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7fb7601b8040>)

tests/test_polish_0139.py:49: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x1461d490) at 0x7fb76032d140>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        for game_id in (identity, other):
            w.library.add_diary(game_id, 'Texto curto que deve permanecer íntegro.')
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7fb7601bb850>)

tests/test_polish_0139.py:49: AssertionError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0] ______

ui = (<checkpoint.window.MainWindow(0x14276090) at 0x7fb76032f100>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:68: AttributeError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1] ______

ui = (<checkpoint.window.MainWindow(0x13b67fb0) at 0x7fb760221c00>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:68: AttributeError
_______________ test_black_is_neutral_and_other_themes_preserved _______________

    def test_black_is_neutral_and_other_themes_preserved():
        from checkpoint.theme import THEMES
        from PySide6.QtGui import QColor
        black = THEMES['black'].colors
        for key in ('background', 'sidebar', 'surface', 'elevated', 'card', 'panel', 'input', 'button', 'border', 'border_subtle'):
            c = QColor(black[key])
>           assert c.red() == c.green() == c.blue(), (key, black[key])
E           AssertionError: ('background', '#0e141d')
E           assert 14 == 20
E            +  where 14 = <built-in method red of PySide6.QtGui.QColor object at 0x7fb7601d9380>()
E            +    where <built-in method red of PySide6.QtGui.QColor object at 0x7fb7601d9380> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E            +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7fb7601d9380>()
E            +    where <built-in method green of PySide6.QtGui.QColor object at 0x7fb7601d9380> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green

tests/test_polish_0139.py:82: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x1410c940) at 0x7fb75de4f1c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7fb75dc91d20>)

tests/test_polish_0139.py:99: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x14936c00) at 0x7fb75de42040>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7fb75dc92880>)

tests/test_polish_0139.py:99: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample0] _______________

ui = (<checkpoint.window.MainWindow(0x144abe00) at 0x7fb75de3c840>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 737)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fb75dc8c680>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fb75dc8c680> = <PySide6.QtWidgets.QScrollBar(0x14736bc0) at 0x7fb75dc8c680>.x

tests/test_polish_0139.py:116: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample1] _______________

ui = (<checkpoint.window.MainWindow(0x1442c020) at 0x7fb75dd76f80>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 1137)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fb75dcbeb40>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fb75dcbeb40> = <PySide6.QtWidgets.QScrollBar(0x14838700) at 0x7fb75dcbeb40>.x

tests/test_polish_0139.py:116: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample0] ________

ui = (<checkpoint.window.MainWindow(0x14252520) at 0x7fb75dc8fd00>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x14915ba0) at 0x7fb75dc0d440>, <PySide6.QtWidgets.QPushButton(0x14915b30) at 0x7fb75de31940>])

tests/test_polish_0139.py:127: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample1] ________

ui = (<checkpoint.window.MainWindow(0x140128c0) at 0x7fb76044e1c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x14460a80) at 0x7fb75dc60e00>, <PySide6.QtWidgets.QPushButton(0x1478b710) at 0x7fb75dc620c0>])

tests/test_polish_0139.py:127: AssertionError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample0] __

ui = (<checkpoint.window.MainWindow(0x145d2400) at 0x7fb75dc0ec40>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
>       w.library.soft_delete(identity)
        ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'soft_delete'

tests/test_polish_0139.py:135: AttributeError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample1] __

ui = (<checkpoint.window.MainWindow(0x14502730) at 0x7fb75de1bbc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x13cf0ce0) at 0x7fb7607f3b40>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
>       w.library.soft_delete(identity)
        ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'soft_delete'

tests/test_polish_0139.py:135: AttributeError
=========================== short test summary info ============================
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample1]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample0]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample1]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1]
FAILED tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample0]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample1]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample0]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample1]
23 failed in 2.31s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## regressions-before-corrected

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850123.5926433,
  "exit_code": 1,
  "elapsed": 3.259516477584839
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 28618 bytes; SHA-256 8a9f3ae05844d8b7d5a4b171db801bb0f2e1a52c194399c037d40ad1dc3bb09d:

````text
FFFFFFFFFFFFFFFFFFFFFFF                                                  [100%]
=================================== FAILURES ===================================
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0] ______

ui = (<checkpoint.window.MainWindow(0x2b72be10) at 0x7f7a7fb75680>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/Checkpoint/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1] ______

ui = (<checkpoint.window.MainWindow(0x2bb97d30) at 0x7f7a7fb87940>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/Checkpoint/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
______ test_recent_cards_height_follows_content_and_button_fits[sample0] _______

ui = (<checkpoint.window.MainWindow(0x2baed600) at 0x7f7a7fb23c40>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7f7a7dbe6190>)

tests/test_home_polish_0139.py:60: AssertionError
______ test_recent_cards_height_follows_content_and_button_fits[sample1] _______

ui = (<checkpoint.window.MainWindow(0x2be74290) at 0x7f7a7fb09b80>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7f7a7f7f75e0>)

tests/test_home_polish_0139.py:60: AssertionError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0] _____

ui = (<checkpoint.window.MainWindow(0x2b92f660) at 0x7f7a7fbd6640>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1] _____

ui = (<checkpoint.window.MainWindow(0x2b9c0770) at 0x7f7a7faff040>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0] _

ui = (<checkpoint.window.MainWindow(0x2b9d69b0) at 0x7f7a7f7e4600>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>
folder = PosixPath('/tmp/254b0d15bb754937a8c2855b2108c08a')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dbfa9c0>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dbfa9c0> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7f7a7dbfa9c0>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dbfa9c0>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dbfa9c0> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7f7a7dbfa9c0>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1] _

ui = (<checkpoint.window.MainWindow(0x2b26dc20) at 0x7f7a7dbf9440>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>
folder = PosixPath('/tmp/22e48af1225c4fd29e313215c269970b')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dc5dd40>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dc5dd40> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7f7a7dc5dd40>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dc5dd40>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7f7a7dc5dd40> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7f7a7dc5dd40>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0] _____

ui = (<checkpoint.window.MainWindow(0x2bdaa830) at 0x7f7a7dbfa600>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7f7a7f7e6dc0>()
E                +    where <built-in method width of WishCard object at 0x7f7a7f7e6dc0> = <checkpoint.collection_views.WishCard(0x2c086340, name="panel") at 0x7f7a7f7e6dc0>.width

tests/test_polish_0139.py:28: AssertionError
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1] _____

ui = (<checkpoint.window.MainWindow(0x2bb2ae50) at 0x7f7a7fadad00>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7f7a7f68af40>()
E                +    where <built-in method width of WishCard object at 0x7f7a7f68af40> = <checkpoint.collection_views.WishCard(0x2c1c71a0, name="panel") at 0x7f7a7f68af40>.width

tests/test_polish_0139.py:28: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x2becd490) at 0x7f7a7dbb25c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        for game_id in (identity, other):
            w.library.add_diary(game_id, 'Texto curto que deve permanecer íntegro.')
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7f7a7f690040>)

tests/test_polish_0139.py:49: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x2be72a50) at 0x7f7a7f68b100>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        for game_id in (identity, other):
            w.library.add_diary(game_id, 'Texto curto que deve permanecer íntegro.')
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7f7a7f693850>)

tests/test_polish_0139.py:49: AssertionError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0] ______

ui = (<checkpoint.window.MainWindow(0x2bd894a0) at 0x7f7a7f827a40>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:68: AttributeError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1] ______

ui = (<checkpoint.window.MainWindow(0x2be2c770) at 0x7f7a7f780ac0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:68: AttributeError
_______________ test_black_is_neutral_and_other_themes_preserved _______________

    def test_black_is_neutral_and_other_themes_preserved():
        from checkpoint.theme import THEMES
        from PySide6.QtGui import QColor
        black = THEMES['black'].colors
        for key in ('background', 'sidebar', 'surface', 'elevated', 'card', 'panel', 'input', 'button', 'border', 'border_subtle'):
            c = QColor(black[key])
>           assert c.red() == c.green() == c.blue(), (key, black[key])
E           AssertionError: ('background', '#0e141d')
E           assert 14 == 20
E            +  where 14 = <built-in method red of PySide6.QtGui.QColor object at 0x7f7a7d22dd00>()
E            +    where <built-in method red of PySide6.QtGui.QColor object at 0x7f7a7d22dd00> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E            +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7f7a7d22dd00>()
E            +    where <built-in method green of PySide6.QtGui.QColor object at 0x7f7a7d22dd00> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green

tests/test_polish_0139.py:82: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x2be9e300) at 0x7f7a7d21d100>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7f7a7d061d20>)

tests/test_polish_0139.py:99: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x2bb48050) at 0x7f7a7d20bd80>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7f7a7d062880>)

tests/test_polish_0139.py:99: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample0] _______________

ui = (<checkpoint.window.MainWindow(0x2bc1e860) at 0x7f7a7dc44cc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 737)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7f7a7d2049c0>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7f7a7d2049c0> = <PySide6.QtWidgets.QScrollBar(0x2c12ce50) at 0x7f7a7d2049c0>.x

tests/test_polish_0139.py:116: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample1] _______________

ui = (<checkpoint.window.MainWindow(0x2bd521e0) at 0x7f7a7d2053c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 1137)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7f7a7d09ebc0>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7f7a7d09ebc0> = <PySide6.QtWidgets.QScrollBar(0x2c4b06d0) at 0x7f7a7d09ebc0>.x

tests/test_polish_0139.py:116: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample0] ________

ui = (<checkpoint.window.MainWindow(0x2be24380) at 0x7f7a7d06ea00>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x2c49a420) at 0x7f7a7f749440>, <PySide6.QtWidgets.QPushButton(0x2c49a3b0) at 0x7f7a7dc4e7c0>])

tests/test_polish_0139.py:127: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample1] ________

ui = (<checkpoint.window.MainWindow(0x2c12cee0) at 0x7f7a7d239980>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x2c2b9900) at 0x7f7a7d079f80>, <PySide6.QtWidgets.QPushButton(0x2be973a0) at 0x7f7a7d079d40>])

tests/test_polish_0139.py:127: AssertionError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample0] __

ui = (<checkpoint.window.MainWindow(0x2b927020) at 0x7f7a7f6b60c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
        w.library.delete(identity)
        w.library.delete(other)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(5)
        settle(app)
        titles = [w.settings_tabs.tabText(i) for i in range(w.settings_tabs.count())]
>       assert 'Emuladores' in titles and 'Lixeira' in titles
E       AssertionError: assert ('Emuladores' in ['Aparência', 'Conexões', 'Downloads', 'Dados e backup'])

tests/test_polish_0139.py:141: AssertionError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample1] __

ui = (<checkpoint.window.MainWindow(0x2bfb0f10) at 0x7f7a7d071100>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6efd50) at 0x7f7a7fbc9c40>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
        w.library.delete(identity)
        w.library.delete(other)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(5)
        settle(app)
        titles = [w.settings_tabs.tabText(i) for i in range(w.settings_tabs.count())]
>       assert 'Emuladores' in titles and 'Lixeira' in titles
E       AssertionError: assert ('Emuladores' in ['Aparência', 'Conexões', 'Downloads', 'Dados e backup'])

tests/test_polish_0139.py:141: AssertionError
=========================== short test summary info ============================
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample1]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample0]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample1]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1]
FAILED tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample0]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample1]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample0]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample1]
23 failed in 2.85s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## extra-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "/workspace/work/evidence-0139/probe_before.py"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850259.7943468,
  "exit_code": 0,
  "elapsed": 1.0831034183502197
}
```

Comando:

```sh
/workspace/work/venv/bin/python /workspace/work/evidence-0139/probe_before.py
```

stdout integral — 42 bytes; SHA-256 5aed656e7cec6266085c49eca70a58430ea554aa75c500a362de77a654cf830f:

````text
/workspace/work/evidence-0139/antes-extra
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## detail-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_detail_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850416.6682923,
  "exit_code": 1,
  "elapsed": 1.2887911796569824
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_detail_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 5475 bytes; SHA-256 4cf29b3e4406a605ff961a3636b9470d532cddd65d451dbc493ccf82a992a03c:

````text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample0] ______

ui = (<checkpoint.window.MainWindow(0x2fd23840) at 0x7f79110cb980>, 1)
app = <PySide6.QtWidgets.QApplication(0x2fc75a30) at 0x7f7911055380>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
>           assert label is not None
E           assert None is not None

tests/test_detail_polish_0139.py:25: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample1] ______

ui = (<checkpoint.window.MainWindow(0x305e96c0) at 0x7f79110cbb00>, 1)
app = <PySide6.QtWidgets.QApplication(0x2fc75a30) at 0x7f7911055380>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
>           assert label is not None
E           assert None is not None

tests/test_detail_polish_0139.py:25: AssertionError
_____ test_completions_use_recorded_timestamp_not_current_status[sample0] ______

ui = (<checkpoint.window.MainWindow(0x304093b0) at 0x7f7916e0eec0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2fc75a30) at 0x7f7911055380>

    def test_completions_use_recorded_timestamp_not_current_status(ui, app):
        from checkpoint.statistics_periods import period_stats
        w, identity = ui
        other = w.library.save_game({'title': 'Hades', 'status': 'Concluído'})
        now = datetime.now(timezone.utc)
        with w.library.sql:
            w.library.sql.execute("UPDATE games SET status='Concluído',completed_at=NULL WHERE id=?", (identity,))
            w.library.sql.execute("UPDATE games SET completed_at=? WHERE id=?", ((now-timedelta(days=1)).isoformat(), other))
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        assert sum(period_stats(w.library, 'all')['completions'].values()) == 1
        w.navigate(4)
        period = w.pages[4].findChild(QComboBox, 'statisticsPeriod')
        period.setCurrentIndex(period.findData('all'))
        settle(app)
        frame = w.pages[4].findChild(QWidget, 'completionMetrics')
>       assert frame is not None
E       assert None is not None

tests/test_detail_polish_0139.py:52: AssertionError
_____ test_completions_use_recorded_timestamp_not_current_status[sample1] ______

ui = (<checkpoint.window.MainWindow(0x2ff35d00) at 0x7f7916d18d40>, 1)
app = <PySide6.QtWidgets.QApplication(0x2fc75a30) at 0x7f7911055380>

    def test_completions_use_recorded_timestamp_not_current_status(ui, app):
        from checkpoint.statistics_periods import period_stats
        w, identity = ui
        other = w.library.save_game({'title': 'Hades', 'status': 'Concluído'})
        now = datetime.now(timezone.utc)
        with w.library.sql:
            w.library.sql.execute("UPDATE games SET status='Concluído',completed_at=NULL WHERE id=?", (identity,))
            w.library.sql.execute("UPDATE games SET completed_at=? WHERE id=?", ((now-timedelta(days=1)).isoformat(), other))
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        assert sum(period_stats(w.library, 'all')['completions'].values()) == 1
        w.navigate(4)
        period = w.pages[4].findChild(QComboBox, 'statisticsPeriod')
        period.setCurrentIndex(period.findData('all'))
        settle(app)
        frame = w.pages[4].findChild(QWidget, 'completionMetrics')
>       assert frame is not None
E       assert None is not None

tests/test_detail_polish_0139.py:52: AssertionError
=========================== short test summary info ============================
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample0]
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample1]
FAILED tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample0]
FAILED tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample1]
4 failed in 0.92s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## home-after-first

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850597.960784,
  "exit_code": 1,
  "elapsed": 3.5366311073303223
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_home_data_0137.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 7745 bytes; SHA-256 d345918819855fe1633572ca3d49de9f917a714970f9dc18d9131b16511d221f:

````text
...................FF....FF....                                          [100%]
=================================== FAILURES ===================================
__________ test_home_columns_share_base_and_art_is_contained[sample0] __________

ui = (<checkpoint.window.MainWindow(0x18257c60) at 0x7f446e6eba40>, 1)
app = <PySide6.QtWidgets.QApplication(0x177aaa90) at 0x7f446ed81580>

    def test_home_columns_share_base_and_art_is_contained(ui,app):
        w,i=ui;seed_recent(w,i)
        for size in ((1280,800),(1920,1080),(1000,700)):
            w.resize(*size);w.navigate(0)
            for _ in range(8):app.processEvents()
            page=w.pages[0];left=page.findChild(QWidget,'homeRecentSection');offers=page.findChild(QWidget,'homeWishOffers')
            if size[0]>=1280:
                a=left.mapTo(page,left.rect().bottomLeft()).y();b=offers.mapTo(page,offers.rect().bottomLeft()).y()
>               assert abs(a-b)<=2
E               assert 200 <= 2
E                +  where 200 = abs((519 - 319))

tests/test_home_layout_0137.py:41: AssertionError
__________ test_home_columns_share_base_and_art_is_contained[sample1] __________

ui = (<checkpoint.window.MainWindow(0x17e342c0) at 0x7f446e7fcd00>, 1)
app = <PySide6.QtWidgets.QApplication(0x177aaa90) at 0x7f446ed81580>

    def test_home_columns_share_base_and_art_is_contained(ui,app):
        w,i=ui;seed_recent(w,i)
        for size in ((1280,800),(1920,1080),(1000,700)):
            w.resize(*size);w.navigate(0)
            for _ in range(8):app.processEvents()
            page=w.pages[0];left=page.findChild(QWidget,'homeRecentSection');offers=page.findChild(QWidget,'homeWishOffers')
            if size[0]>=1280:
                a=left.mapTo(page,left.rect().bottomLeft()).y();b=offers.mapTo(page,offers.rect().bottomLeft()).y()
>               assert abs(a-b)<=2
E               assert 200 <= 2
E                +  where 200 = abs((519 - 319))

tests/test_home_layout_0137.py:41: AssertionError
_____ test_three_recent_games_carousel_preserves_every_cover_edge[sample0] _____

ui = (<checkpoint.window.MainWindow(0x17df1e80) at 0x7f446e88ac40>, 1)
app = <PySide6.QtWidgets.QApplication(0x177aaa90) at 0x7f446ed81580>
folder = PosixPath('/tmp/d0e94fad585f4a10bb3325a9ca66500d')

    def test_three_recent_games_carousel_preserves_every_cover_edge(ui,app,folder):
        from PySide6.QtGui import QImage,QColor,QPainter
        from checkpoint.home_components import GameStrip
        w,i=ui;identities=[i]
        for title in ('Hades','Celeste','Metroid Fusion'):
            identities.append(w.library.save_game({'title':title,'platform':'PC'}))
        for n,identity in enumerate(identities):
            image=QImage(200,300,QImage.Format_RGB32);image.fill(QColor('blue'));p=QPainter(image)
            p.fillRect(0,0,200,12,QColor('yellow'));p.fillRect(0,288,200,12,QColor('magenta'))
            p.fillRect(0,12,12,276,QColor('cyan'));p.fillRect(188,12,12,276,QColor('red'));p.end()
            path=folder/f'cover-{n}.png';assert image.save(str(path))
            w.library.save_game({'title':w.library.get(identity)['title'],'cover':str(path)},identity)
            with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'finished',?)",(identity,(datetime.now(timezone.utc)-timedelta(hours=n+1)).isoformat(),100+n))
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(0)
            for _ in range(8):app.processEvents()
            strip=w.pages[0].findChild(GameStrip);assert len(strip.tiles)==3
            assert not strip.previous.isEnabled() and strip.next.isEnabled()
            for card in strip.tiles:
                art=card.findChild(RecentArtwork);target=art.image_target()
>               assert abs(target.width()-art.width())<=1 and abs(target.height()-art.height())<=1
E               assert (14.0 <= 1)
E                +  where 14.0 = abs((140.0 - 154))
E                +    where 140.0 = <built-in method width of PySide6.QtCore.QRectF object at 0x7f446e82fc00>()
E                +      where <built-in method width of PySide6.QtCore.QRectF object at 0x7f446e82fc00> = PySide6.QtCore.QRectF(7.000000, 0.000000, 140.000000, 210.000000).width
E                +    and   154 = <built-in method width of RecentArtwork object at 0x7f446e82ea80>()
E                +      where <built-in method width of RecentArtwork object at 0x7f446e82ea80> = <checkpoint.home_components.RecentArtwork(0x1822a640, name="recentGameArtwork") at 0x7f446e82ea80>.width

tests/test_home_layout_0137.py:96: AssertionError
_____ test_three_recent_games_carousel_preserves_every_cover_edge[sample1] _____

ui = (<checkpoint.window.MainWindow(0x17bdaf80) at 0x7f446e875d40>, 1)
app = <PySide6.QtWidgets.QApplication(0x177aaa90) at 0x7f446ed81580>
folder = PosixPath('/tmp/1598e208117449169cd98fa493e6747a')

    def test_three_recent_games_carousel_preserves_every_cover_edge(ui,app,folder):
        from PySide6.QtGui import QImage,QColor,QPainter
        from checkpoint.home_components import GameStrip
        w,i=ui;identities=[i]
        for title in ('Hades','Celeste','Metroid Fusion'):
            identities.append(w.library.save_game({'title':title,'platform':'PC'}))
        for n,identity in enumerate(identities):
            image=QImage(200,300,QImage.Format_RGB32);image.fill(QColor('blue'));p=QPainter(image)
            p.fillRect(0,0,200,12,QColor('yellow'));p.fillRect(0,288,200,12,QColor('magenta'))
            p.fillRect(0,12,12,276,QColor('cyan'));p.fillRect(188,12,12,276,QColor('red'));p.end()
            path=folder/f'cover-{n}.png';assert image.save(str(path))
            w.library.save_game({'title':w.library.get(identity)['title'],'cover':str(path)},identity)
            with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'finished',?)",(identity,(datetime.now(timezone.utc)-timedelta(hours=n+1)).isoformat(),100+n))
        for size in ((1280,800),(1920,1080)):
            w.resize(*size);w.navigate(0)
            for _ in range(8):app.processEvents()
            strip=w.pages[0].findChild(GameStrip);assert len(strip.tiles)==3
            assert not strip.previous.isEnabled() and strip.next.isEnabled()
            for card in strip.tiles:
                art=card.findChild(RecentArtwork);target=art.image_target()
>               assert abs(target.width()-art.width())<=1 and abs(target.height()-art.height())<=1
E               assert (14.0 <= 1)
E                +  where 14.0 = abs((140.0 - 154))
E                +    where 140.0 = <built-in method width of PySide6.QtCore.QRectF object at 0x7f446e722b00>()
E                +      where <built-in method width of PySide6.QtCore.QRectF object at 0x7f446e722b00> = PySide6.QtCore.QRectF(7.000000, 0.000000, 140.000000, 210.000000).width
E                +    and   154 = <built-in method width of RecentArtwork object at 0x7f446e7293c0>()
E                +      where <built-in method width of RecentArtwork object at 0x7f446e7293c0> = <checkpoint.home_components.RecentArtwork(0x17bcfb90, name="recentGameArtwork") at 0x7f446e7293c0>.width

tests/test_home_layout_0137.py:96: AssertionError
=========================== short test summary info ============================
FAILED tests/test_home_layout_0137.py::test_home_columns_share_base_and_art_is_contained[sample0]
FAILED tests/test_home_layout_0137.py::test_home_columns_share_base_and_art_is_contained[sample1]
FAILED tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample0]
FAILED tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample1]
4 failed, 27 passed in 3.13s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## home-visual-first

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0137_review.py",
    "/workspace/work/evidence-0139/proposta-inicio"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850599.384982,
  "exit_code": 0,
  "elapsed": 5.529425621032715
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0137_review.py /workspace/work/evidence-0139/proposta-inicio
```

stdout integral — 46 bytes; SHA-256 48ba12839e5b928491663fadc2cbeb0a01e7a0f2206e9b82f4c9fb560a040ec8:

````text
/workspace/work/evidence-0139/proposta-inicio
````

stderr integral — 286 bytes; SHA-256 e4dd96b236e73919f55e2570ea325d645ed48b502c4bfc98945503b2dc2a85e1:

````text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## home-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "tests/test_icons_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850676.528073,
  "exit_code": 0,
  "elapsed": 5.20811915397644
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_home_data_0137.py tests/test_home_layout_0137.py tests/test_icons_0134.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 efb849336eab17cb9038066cef3ad70d7dab748eef333792d3dc2fcc876b1cdf:

````text
........................................                                 [100%]
40 passed in 4.80s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## home-visual-second

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0137_review.py",
    "/workspace/work/evidence-0139/proposta-inicio-2"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850677.9556656,
  "exit_code": 0,
  "elapsed": 6.525097846984863
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0137_review.py /workspace/work/evidence-0139/proposta-inicio-2
```

stdout integral — 48 bytes; SHA-256 ce1c5584cd4dfe87f2bf94736c159e95a596ddc3569db84576c5389f1a7fe4d5:

````text
/workspace/work/evidence-0139/proposta-inicio-2
````

stderr integral — 286 bytes; SHA-256 e4dd96b236e73919f55e2570ea325d645ed48b502c4bfc98945503b2dc2a85e1:

````text
Fontconfig error: No writable cache directories
This plugin does not support raise()
This plugin does not support grabbing the keyboard
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## wishes-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns",
    "tests/test_wishes_0135.py",
    "tests/test_wish_spacing_0137.py",
    "tests/test_wish_platform_filter_0137.py",
    "tests/test_wish_navigation_0136.py",
    "tests/test_wish_time_0136.py",
    "tests/test_prices_0129.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850738.4202313,
  "exit_code": 0,
  "elapsed": 4.542374849319458
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns tests/test_wishes_0135.py tests/test_wish_spacing_0137.py tests/test_wish_platform_filter_0137.py tests/test_wish_navigation_0136.py tests/test_wish_time_0136.py tests/test_prices_0129.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 7c6578d720091684c1930da7105808c6d29fbd2b47f2df14d4c25a0914741141:

````text
....................                                                     [100%]
20 passed in 4.02s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## home-letterbox-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850833.8439198,
  "exit_code": 0,
  "elapsed": 4.184992074966431
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 c7c066885aa8cc255cb6bd24f8bf51299899bfa5360f926d56f2cf441a69b7fb:

````text
..........................                                               [100%]
26 passed in 3.85s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## home-rounded-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/inicio-sem-faixa",
    "--only",
    "home,wishes"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850908.7744772,
  "exit_code": 0,
  "elapsed": 3.1709611415863037
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/inicio-sem-faixa --only home,wishes
```

stdout integral — 47 bytes; SHA-256 ff196f3c3b6ef0ee5d6c3b33c7fc57e6350d59a84efce835e7ba8505900f1a89:

````text
/workspace/work/evidence-0139/inicio-sem-faixa
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## memories-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align",
    "tests/test_memories_0135.py",
    "tests/test_visual_audit_0136.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850962.680633,
  "exit_code": 0,
  "elapsed": 2.8903396129608154
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align tests/test_memories_0135.py tests/test_visual_audit_0136.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 d91c1ceb48d361914c06c29ad9c0e7b759d2e336e39b7580802ec68471afc552:

````text
..................                                                       [100%]
18 passed in 2.53s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## memories-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/memorias",
    "--only",
    "memories"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850964.0746033,
  "exit_code": 0,
  "elapsed": 1.4022595882415771
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/memorias --only memories
```

stdout integral — 39 bytes; SHA-256 8d3f534367b73db297f7ffe16b8ddacee8536ff20b0912ed1d40c8f1eba9f6cf:

````text
/workspace/work/evidence-0139/memorias
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## completions-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status",
    "tests/test_statistics_visible_0136.py",
    "tests/test_statistics_0136.py",
    "tests/test_period_chart_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794850995.7292767,
  "exit_code": 0,
  "elapsed": 3.371594190597534
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status tests/test_statistics_visible_0136.py tests/test_statistics_0136.py tests/test_period_chart_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 b6acb33c7472c02ca4d224db84cc1c359f7ae71ac5a608002c25c6f10cd984c2:

````text
...............                                                          [100%]
15 passed in 3.00s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## cover-focus-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art",
    "tests/test_cover_preview_0135.py",
    "tests/test_visual_complements_0135.py",
    "tests/test_settings_space_0135.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851017.8934681,
  "exit_code": 0,
  "elapsed": 3.6599786281585693
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art tests/test_cover_preview_0135.py tests/test_visual_complements_0135.py tests/test_settings_space_0135.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 250e2b70a5fcd67e5b9a0c0bba0344f5f7e51c699df8cd82527fb3c9b6ed345d:

````text
........................                                                 [100%]
24 passed in 3.34s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## memories-alignment-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align",
    "tests/test_memories_0135.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851073.1174514,
  "exit_code": 0,
  "elapsed": 3.5255229473114014
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align tests/test_memories_0135.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 3ada6a4ac13e811743f7111414edab4cfa308325886a9941432db1f275efa747:

````text
............................                                             [100%]
28 passed in 3.17s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## library-gutter-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter",
    "tests/test_library_list_0137.py",
    "tests/test_favorite_0136.py",
    "tests/test_grid_performance_0137.py",
    "tests/test_smooth_scroll.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851101.8687632,
  "exit_code": 1,
  "elapsed": 3.4587061405181885
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter tests/test_library_list_0137.py tests/test_favorite_0136.py tests/test_grid_performance_0137.py tests/test_smooth_scroll.py -q -p no:cacheprovider
```

stdout integral — 2703 bytes; SHA-256 1a582ab8797c01bf1c1ef31d31ce22dde420a2bdc0df99d404732926867364c3:

````text
FF.............                                                          [100%]
=================================== FAILURES ===================================
______________ test_library_scrollbar_has_stable_gutter[sample0] _______________

ui = (<checkpoint.window.MainWindow(0xab24fc0) at 0x7fa1aa117380>, 1)
app = <PySide6.QtWidgets.QApplication(0xaac4ac0) at 0x7fa1aa040500>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 721)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fa1a9b17f40>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fa1a9b17f40> = <PySide6.QtWidgets.QScrollBar(0xaa4c570) at 0x7fa1a9b17f40>.x

tests/test_polish_0139.py:117: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______________ test_library_scrollbar_has_stable_gutter[sample1] _______________

ui = (<checkpoint.window.MainWindow(0xb1698c0) at 0x7fa1a9b17dc0>, 1)
app = <PySide6.QtWidgets.QApplication(0xaac4ac0) at 0x7fa1aa040500>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.x() - right <= 24
E       assert 12 <= (0 - 1121)
E        +  where 0 = <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fa1a9990580>()
E        +    where <built-in method x of PySide6.QtWidgets.QScrollBar object at 0x7fa1a9990580> = <PySide6.QtWidgets.QScrollBar(0xb073c70) at 0x7fa1a9990580>.x

tests/test_polish_0139.py:117: AssertionError
=========================== short test summary info ============================
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
2 failed, 13 passed in 3.08s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## primary-icon-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground",
    "tests/test_icons_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851104.3643613,
  "exit_code": 1,
  "elapsed": 0.9826617240905762
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground tests/test_icons_0134.py -q -p no:cacheprovider
```

stdout integral — 3285 bytes; SHA-256 41742c06441bc3119433438a0f6bda5db4261efe5e4a9c4211eb39aa096b7c4f:

````text
FF.......                                                                [100%]
=================================== FAILURES ===================================
____________ test_add_wish_icon_matches_primary_foreground[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x13cb20e0) at 0x7f6e4f5bdb00>, 1)
app = <PySide6.QtWidgets.QApplication(0x13c3a970) at 0x7f6e4f69ae00>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.064515, 0.104845, 0.133059, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.064515, 0.1048...romRgbF(0.064515, 0.104845, 0.133059, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.064515, 0.104845, 0.133059, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7f6e554e35a0>)

tests/test_polish_0139.py:100: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____________ test_add_wish_icon_matches_primary_foreground[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x140cfe40) at 0x7f6e4f5bd440>, 1)
app = <PySide6.QtWidgets.QApplication(0x13c3a970) at 0x7f6e4f69ae00>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            pix = button.icon().pixmap(20, 20).toImage()
            expected = QColor(w.theme.colors['on_accent'])
            opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>           assert opaque and all(c.rgb() == expected.rgb() for c in opaque)
E           assert ([PySide6.QtGui.QColor.fromRgbF(0.064515, 0.104845, 0.133059, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.064515, 0.1048...romRgbF(0.064515, 0.104845, 0.133059, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.064515, 0.104845, 0.133059, 0.972549)] and False)
E            +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7f6e554e2340>)

tests/test_polish_0139.py:100: AssertionError
=========================== short test summary info ============================
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
2 failed, 7 passed in 0.59s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## local-components-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align",
    "tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter",
    "tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground",
    "tests/test_memories_0135.py",
    "tests/test_home_layout_0137.py",
    "tests/test_library_list_0137.py",
    "tests/test_icons_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851190.8768418,
  "exit_code": 0,
  "elapsed": 4.781414270401001
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground tests/test_memories_0135.py tests/test_home_layout_0137.py tests/test_library_list_0137.py tests/test_icons_0134.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 92ca09963c79e781dfe64c1b6cd04118f4d226a3e67ac0478b4bad4d097e2a22:

````text
...........................................                              [100%]
43 passed in 4.41s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## memories-preview-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/memorias-preview",
    "--only",
    "memories"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851192.2869954,
  "exit_code": 0,
  "elapsed": 1.4321260452270508
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/memorias-preview --only memories
```

stdout integral — 47 bytes; SHA-256 1bac6cde8045e951563b7f33ef6806ccd22d90939ff525bc66d88342817ca1fd:

````text
/workspace/work/evidence-0139/memorias-preview
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## black-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved",
    "tests/test_themes.py",
    "tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851222.9324417,
  "exit_code": 0,
  "elapsed": 18.085701942443848
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved tests/test_themes.py tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast -q -p no:cacheprovider
```

stdout integral — 100 bytes; SHA-256 12ca4fe9eb1e0a801347bd7ea5dac67810837096737d474409315883a756c2c6:

````text
.......................                                                  [100%]
23 passed in 17.54s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## appearance-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/aparencia",
    "--only",
    "appearance"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851224.3439445,
  "exit_code": 0,
  "elapsed": 2.4147777557373047
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/aparencia --only appearance
```

stdout integral — 40 bytes; SHA-256 ebb3016548b64f837d197db24fc91c1982aabe016932781d4bd02ed2e975a079:

````text
/workspace/work/evidence-0139/aparencia
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## mixed-preview-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area",
    "tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851251.145426,
  "exit_code": 0,
  "elapsed": 0.8928203582763672
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align -q -p no:cacheprovider
```

stdout integral — 98 bytes; SHA-256 0d16a77e1e864d97e14ae2195796d95b327c649378aaefbb2afbd3fd17b71aa7:

````text
....                                                                     [100%]
4 passed in 0.59s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## icon-states-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground",
    "tests/test_icons_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851284.2378964,
  "exit_code": 1,
  "elapsed": 0.8001911640167236
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground tests/test_icons_0134.py -q -p no:cacheprovider
```

stdout integral — 2249 bytes; SHA-256 1c5115f3e0204457b49f9c73e8431d9ca48690de8368238f01b0932e1d928862:

````text
FF.......                                                                [100%]
=================================== FAILURES ===================================
____________ test_add_wish_icon_matches_primary_foreground[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x121eff20) at 0x7f53f4ae79c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x121cfd30) at 0x7f53f4aa9f40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
>           for enabled, mode, foreground in ((True, QIcon.Normal, 'on_accent'), (False, QIcon.Disabled, 'disabled')):
                                                     ^^^^^
E           NameError: name 'QIcon' is not defined

tests/test_polish_0139.py:97: NameError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____________ test_add_wish_icon_matches_primary_foreground[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x128eb450) at 0x7f53f46a0ec0>, 1)
app = <PySide6.QtWidgets.QApplication(0x121cfd30) at 0x7f53f4aa9f40>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
>           for enabled, mode, foreground in ((True, QIcon.Normal, 'on_accent'), (False, QIcon.Disabled, 'disabled')):
                                                     ^^^^^
E           NameError: name 'QIcon' is not defined

tests/test_polish_0139.py:97: NameError
=========================== short test summary info ============================
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
2 failed, 7 passed in 0.50s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## files-saves-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_detail_polish_0139.py",
    "tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action",
    "tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground",
    "tests/test_detail_0134.py",
    "tests/test_game_saves.py",
    "tests/test_save_profiles.py",
    "tests/test_icons_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851317.1833599,
  "exit_code": 1,
  "elapsed": 4.092643976211548
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_detail_polish_0139.py tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground tests/test_detail_0134.py tests/test_game_saves.py tests/test_save_profiles.py tests/test_icons_0134.py -q -p no:cacheprovider
```

stdout integral — 3306 bytes; SHA-256 70e5b7edb96c27f87783abad1ad88563a1e1872297c42f5fd248dd05259c2505:

````text
FF...........................                                            [100%]
=================================== FAILURES ===================================
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample0] ______

ui = (<checkpoint.window.MainWindow(0xa05b9d0) at 0x7ff38cef5a00>, 1)
app = <PySide6.QtWidgets.QApplication(0xa009a00) at 0x7ff38cff4680>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
            assert label is not None
            assert label.toolTip() == filename
            assert not label.wordWrap()
            frame = label.parentWidget()
>           button = next(b for b in frame.findChildren(QPushButton) if b.text() == 'Baixar ROM')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           StopIteration

tests/test_detail_polish_0139.py:29: StopIteration
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample1] ______

ui = (<checkpoint.window.MainWindow(0xa275ad0) at 0x7ff38cef5900>, 1)
app = <PySide6.QtWidgets.QApplication(0xa009a00) at 0x7ff38cff4680>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
            assert label is not None
            assert label.toolTip() == filename
            assert not label.wordWrap()
            frame = label.parentWidget()
>           button = next(b for b in frame.findChildren(QPushButton) if b.text() == 'Baixar ROM')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           StopIteration

tests/test_detail_polish_0139.py:29: StopIteration
=========================== short test summary info ============================
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample0]
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample1]
2 failed, 27 passed in 3.68s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## files-saves-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/arquivos-saves",
    "--only",
    "files"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851318.5621154,
  "exit_code": 0,
  "elapsed": 1.585961103439331
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/arquivos-saves --only files
```

stdout integral — 45 bytes; SHA-256 95f7a69eadc172ccd343c38d3f851b49c06d042529227c877f57b4644944d259:

````text
/workspace/work/evidence-0139/arquivos-saves
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## settings-tabs-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records",
    "tests/test_detail_polish_0139.py",
    "tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action",
    "tests/test_settings_0135.py",
    "tests/test_trash_import.py",
    "tests/test_themes.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851382.9145362,
  "exit_code": 0,
  "elapsed": 19.769568920135498
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records tests/test_detail_polish_0139.py tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action tests/test_settings_0135.py tests/test_trash_import.py tests/test_themes.py -q -p no:cacheprovider
```

stdout integral — 100 bytes; SHA-256 33d2fab6e4b0ca13f6bf2540cf71925471abcb0374f02ea421a1f2236e768031:

````text
................................                                         [100%]
32 passed in 19.28s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dialog-core-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_sessions_0135.py",
    "tests/test_launch_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_rom_edition_0137.py",
    "tests/test_rom_link_0134.py",
    "tests/test_memories_0135.py",
    "tests/test_window_controls_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851616.8620007,
  "exit_code": 0,
  "elapsed": 4.4783384799957275
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_sessions_0135.py tests/test_launch_0135.py tests/test_local_rom_0137.py tests/test_rom_edition_0137.py tests/test_rom_link_0134.py tests/test_memories_0135.py tests/test_window_controls_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 b4e6862214878020dbf513b2a1890e5cb3cb87fa58807cc6c7307f04bd68569d:

````text
.....................................................                    [100%]
53 passed in 4.14s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dialogs-management-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_dialog_polish_0139.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_local_rom_0137.py",
    "tests/test_sessions_0135.py",
    "tests/test_save_lifecycle.py",
    "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851750.1539502,
  "exit_code": -15,
  "elapsed": 63.29868125915527
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_dialog_polish_0139.py tests/test_settings_navigation_0139.py tests/test_local_rom_0137.py tests/test_sessions_0135.py tests/test_save_lifecycle.py tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged -q -p no:cacheprovider
```

stdout integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dialog-trace

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-u",
    "-c",
    "import faulthandler,pytest; faulthandler.dump_traceback_later(8,repeat=True); raise SystemExit(pytest.main([\"tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation\", \"-vv\", \"-s\", \"-p\", \"no:cacheprovider\"]))"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851813.7351015,
  "exit_code": -15,
  "elapsed": 35.72848463058472
}
```

Comando:

```sh
/workspace/work/venv/bin/python -u -c 'import faulthandler,pytest; faulthandler.dump_traceback_later(8,repeat=True); raise SystemExit(pytest.main(["tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation", "-vv", "-s", "-p", "no:cacheprovider"]))'
```

stdout integral — 382 bytes; SHA-256 cf399db7d694d1f867125dae15edf078044c79ad58a25a84bfc1769f5e3e00e4:

````text
============================= test session starts ==============================
platform linux -- Python 3.12.14, pytest-9.2.0, pluggy-1.7.0 -- /workspace/work/venv/bin/python
rootdir: /workspace/work/Checkpoint
configfile: pyproject.toml
collecting ... collected 2 items

tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample0] 
````

stderr integral — 15435 bytes; SHA-256 632afba6433f9be00364f9a1127f1be369f89fc733a7e7d549a07965d7490b5e:

````text
Fontconfig error: No writable cache directories
Timeout (0:00:08)!
Thread 0x00007fdd20b04740 (most recent call first):
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 62 in prepare_dialog
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 74 in prepare
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 83 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 111 in question
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in <lambda>
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 26 in observe_modal
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in test_standard_question_theme_portuguese_default_and_cancellation
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 187 in pytest_pyfunc_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 1798 in runtest
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 361 in from_call
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 411 in pytest_runtestloop
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 387 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 333 in wrap_session
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 231 in main
  File "<string>", line 1 in <module>
Timeout (0:00:08)!
Thread 0x00007fdd20b04740 (most recent call first):
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 62 in prepare_dialog
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 74 in prepare
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 83 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 111 in question
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in <lambda>
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 26 in observe_modal
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in test_standard_question_theme_portuguese_default_and_cancellation
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 187 in pytest_pyfunc_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 1798 in runtest
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 361 in from_call
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 411 in pytest_runtestloop
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 387 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 333 in wrap_session
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 231 in main
  File "<string>", line 1 in <module>
Timeout (0:00:08)!
Thread 0x00007fdd20b04740 (most recent call first):
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 62 in prepare_dialog
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 74 in prepare
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 83 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 111 in question
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in <lambda>
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 26 in observe_modal
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in test_standard_question_theme_portuguese_default_and_cancellation
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 187 in pytest_pyfunc_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 1798 in runtest
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 361 in from_call
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 411 in pytest_runtestloop
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 387 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 333 in wrap_session
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 231 in main
  File "<string>", line 1 in <module>
Timeout (0:00:08)!
Thread 0x00007fdd20b04740 (most recent call first):
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/enum.py", line 1132 in __new__
  File "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/enum.py", line 751 in __call__
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 18 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 62 in prepare_dialog
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 74 in prepare
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 83 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 111 in question
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in <lambda>
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 26 in observe_modal
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in test_standard_question_theme_portuguese_default_and_cancellation
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 187 in pytest_pyfunc_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 1798 in runtest
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 361 in from_call
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 411 in pytest_runtestloop
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 387 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 333 in wrap_session
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 231 in main
  File "<string>", line 1 in <module>
````

## dialogs-management-retry

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-u",
    "-c",
    "import faulthandler,pytest; faulthandler.dump_traceback_later(15,repeat=True); raise SystemExit(pytest.main([\"tests/test_dialog_polish_0139.py\", \"tests/test_settings_navigation_0139.py\", \"tests/test_local_rom_0137.py\", \"tests/test_sessions_0135.py\", \"tests/test_save_lifecycle.py\", \"tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged\", \"-q\", \"-p\", \"no:cacheprovider\"]))"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851850.574642,
  "exit_code": -11,
  "elapsed": 75.14391803741455
}
```

Comando:

```sh
/workspace/work/venv/bin/python -u -c 'import faulthandler,pytest; faulthandler.dump_traceback_later(15,repeat=True); raise SystemExit(pytest.main(["tests/test_dialog_polish_0139.py", "tests/test_settings_navigation_0139.py", "tests/test_local_rom_0137.py", "tests/test_sessions_0135.py", "tests/test_save_lifecycle.py", "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged", "-q", "-p", "no:cacheprovider"]))'
```

stdout integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dialog-trace-second

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-u",
    "-c",
    "import faulthandler,pytest; faulthandler.dump_traceback_later(5,repeat=True); raise SystemExit(pytest.main([\"tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation\", \"-vv\", \"-s\", \"-p\", \"no:cacheprovider\"]))"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794851934.46997,
  "exit_code": -11,
  "elapsed": 10.129265308380127
}
```

Comando:

```sh
/workspace/work/venv/bin/python -u -c 'import faulthandler,pytest; faulthandler.dump_traceback_later(5,repeat=True); raise SystemExit(pytest.main(["tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation", "-vv", "-s", "-p", "no:cacheprovider"]))'
```

stdout integral — 382 bytes; SHA-256 cf399db7d694d1f867125dae15edf078044c79ad58a25a84bfc1769f5e3e00e4:

````text
============================= test session starts ==============================
platform linux -- Python 3.12.14, pytest-9.2.0, pluggy-1.7.0 -- /workspace/work/venv/bin/python
rootdir: /workspace/work/Checkpoint
configfile: pyproject.toml
collecting ... collected 2 items

tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample0] 
````

stderr integral — 3997 bytes; SHA-256 370219faab45ab5e07c77d31dcac587d2b77d43e24d7d9e79ca3910626829ca1:

````text
Fontconfig error: No writable cache directories
Timeout (0:00:05)!
Thread 0x00007f012e68f740 (most recent call first):
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 64 in prepare_dialog
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 76 in prepare
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 85 in eventFilter
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 113 in question
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in <lambda>
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 26 in observe_modal
  File "/workspace/work/Checkpoint/tests/test_dialog_polish_0139.py", line 34 in test_standard_question_theme_portuguese_default_and_cancellation
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 187 in pytest_pyfunc_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/python.py", line 1798 in runtest
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 361 in from_call
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 411 in pytest_runtestloop
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 387 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 333 in wrap_session
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/work/venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/work/venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 231 in main
  File "<string>", line 1 in <module>
Timeout (0:00:05)!
Thread 0x00007f012e68f740 (most recent call first):
  File "/workspace/work/Checkpoint/checkpoint/dialog_style.py", line 18 in eventFilter
  File ???, line ??? in 
````

## dialogs-explicit-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests/test_dialog_polish_0139.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_local_rom_0137.py",
    "tests/test_sessions_0135.py",
    "tests/test_save_lifecycle.py",
    "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852022.9750705,
  "exit_code": -15,
  "elapsed": 87.97528886795044
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests/test_dialog_polish_0139.py tests/test_settings_navigation_0139.py tests/test_local_rom_0137.py tests/test_sessions_0135.py tests/test_save_lifecycle.py tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged -q -p no:cacheprovider
```

stdout integral — 28 bytes; SHA-256 3c7551fd6bda7a118d0617a267726ec06532ebe983164355ed69fd8a04b04658:

````text
............................
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## navigation-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_settings_navigation_0139.py",
    "tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records",
    "tests/test_sessions_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_launch_0135.py",
    "tests/test_memories_0135.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852077.2537897,
  "exit_code": -15,
  "elapsed": 33.69092559814453
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_settings_navigation_0139.py tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records tests/test_sessions_0135.py tests/test_local_rom_0137.py tests/test_launch_0135.py tests/test_memories_0135.py -q -p no:cacheprovider
```

stdout integral — 8 bytes; SHA-256 d09f0ad06d6e59b908037317d6c044f7ababd3466cb46d5b901cf6f0855baf04:

````text
........
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dialogs-navigation-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests/test_dialog_polish_0139.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records",
    "tests/test_sessions_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_launch_0135.py",
    "tests/test_memories_0135.py",
    "tests/test_save_lifecycle.py",
    "tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852111.2724817,
  "exit_code": 0,
  "elapsed": 21.365633964538574
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests/test_dialog_polish_0139.py tests/test_settings_navigation_0139.py tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records tests/test_sessions_0135.py tests/test_local_rom_0137.py tests/test_launch_0135.py tests/test_memories_0135.py tests/test_save_lifecycle.py tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged -q -p no:cacheprovider
```

stdout integral — 100 bytes; SHA-256 400fab8a02f3b7d01c042343f55f69ec9893c1dad4f77c51015186467b644c55:

````text
.........................................................                [100%]
57 passed in 21.03s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## navigation-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/navegacao",
    "--only",
    "settings,dialogs"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852112.6403294,
  "exit_code": 0,
  "elapsed": 1.346935510635376
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/navegacao --only settings,dialogs
```

stdout integral — 40 bytes; SHA-256 6a2eb4fd6b5c99812a230bfdb171677b66f62b468a517d9516309bccf8ae9779:

````text
/workspace/work/evidence-0139/navegacao
````

stderr integral — 448 bytes; SHA-256 2fc093e841b3d12aae2a412d7f62b33bfa56685ae9236d516edbe9b3e4e38c74:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## icon-and-trash-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground",
    "tests/test_icons_0134.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852232.5409076,
  "exit_code": 0,
  "elapsed": 2.2264697551727295
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground tests/test_icons_0134.py tests/test_settings_navigation_0139.py tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 befe997bc27b18fd0590118fd712f5c645d0719894ef6a72a36406f8aa818747:

````text
...................                                                      [100%]
19 passed in 1.86s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## navigation-visual-updated

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/navegacao-logo",
    "--only",
    "settings,dialogs"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852233.9234326,
  "exit_code": 0,
  "elapsed": 1.5672285556793213
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/navegacao-logo --only settings,dialogs
```

stdout integral — 45 bytes; SHA-256 40a013d63af4a44f7e5d58500c7448ba5bab7bab037764ce8a116796923c26e4:

````text
/workspace/work/evidence-0139/navegacao-logo
````

stderr integral — 448 bytes; SHA-256 2fc093e841b3d12aae2a412d7f62b33bfa56685ae9236d516edbe9b3e4e38c74:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## dialog-additional-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests/test_steam.py",
    "tests/test_profile.py",
    "tests/test_avatar_crop_0137.py",
    "tests/test_updates.py",
    "tests/test_catalog.py",
    "tests/test_folder_platforms.py",
    "tests/test_auto_artwork.py",
    "tests/test_trash_import.py",
    "tests/test_add_from_search_flow.py",
    "tests/test_drive_search_flow.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852235.368388,
  "exit_code": 0,
  "elapsed": 9.046127080917358
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests/test_steam.py tests/test_profile.py tests/test_avatar_crop_0137.py tests/test_updates.py tests/test_catalog.py tests/test_folder_platforms.py tests/test_auto_artwork.py tests/test_trash_import.py tests/test_add_from_search_flow.py tests/test_drive_search_flow.py -q -p no:cacheprovider
```

stdout integral — 179 bytes; SHA-256 ffef529e20e8607b6cd338c1fde2dd70823175364332b4eb2748d1f297b6f805:

````text
........................................................................ [ 98%]
.                                                                        [100%]
73 passed in 8.63s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## startup-preserved-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_native_startup_0138.py",
    "tests/test_elevation_0137.py",
    "tests/test_dialog_polish_0139.py",
    "tests/test_home_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852315.2719846,
  "exit_code": 1,
  "elapsed": 65.03470849990845
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_native_startup_0138.py tests/test_elevation_0137.py tests/test_dialog_polish_0139.py tests/test_home_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 10296 bytes; SHA-256 04bdef6152e4531c9230c927711523cd1a02e267ed029dee1f95d388de1cf6a2:

````text
.........FF.....................                                         [100%]
=================================== FAILURES ===================================
_________ test_frozen_startup_handles_uac_before_opening_data[cancel] __________

folder = PosixPath('/tmp/c8dbcfb3f1de497c924befbec4324e30'), outcome = 'cancel'

    @pytest.mark.parametrize('outcome',['handoff','cancel','different_account'])
    def test_frozen_startup_handles_uac_before_opening_data(folder,outcome):
        import subprocess,sys,os
        code=r'''
    import sys
    from pathlib import Path
    import checkpoint.app as entry
    import checkpoint.elevation as elevation
    import checkpoint.data_migration as migration
    from PySide6.QtWidgets import QMessageBox
    root=Path(sys.argv[1]);outcome=sys.argv[2];calls=[]
    def forbidden(*args,**kwargs):raise AssertionError('Dados ou cofre abertos antes da decisão UAC')
    migration.prepare_data_directory=forbidden
    def handoff(*args,**kwargs):
        calls.append(kwargs)
        if outcome=='cancel':raise elevation.ElevationCancelled()
        if outcome=='different_account':raise ValueError('Conta diferente')
        return 0
    elevation.elevate_startup=handoff
    QMessageBox.information=lambda *args:None
    QMessageBox.critical=lambda *args:None
    sys.frozen=True;sys.platform='win32';sys.argv=['Checkpoint.exe','--data-dir',str(root)]
    assert entry.main()==(2 if outcome=='different_account' else 0)
    assert len(calls)==1 and not root.exists()
    '''
>       result=subprocess.run([sys.executable,'-c',code,str(folder/'dados-preservados'),outcome],cwd=Path(__file__).resolve().parents[1],env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_elevation_0137.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:550: in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:1209: in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:2116: in _communicate
    self._check_timeout(endtime, orig_timeout, stdout, stderr)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Popen: returncode: -9 args: ['/workspace/work/venv/bin/python', '-c', "\nim...>
endtime = 25728.248524209, orig_timeout = 30, stdout_seq = []
stderr_seq = [b'Fontconfig error: No writable cache directories\n', b'This plugin does not support propagateSizeHints()\n', b'This plugin does not support propagateSizeHints()\n', b'This plugin does not support propagateSizeHints()\n']
skip_check_and_raise = False

    def _check_timeout(self, endtime, orig_timeout, stdout_seq, stderr_seq,
                       skip_check_and_raise=False):
        """Convenience for checking if a timeout has expired."""
        if endtime is None:
            return
        if skip_check_and_raise or _time() > endtime:
>           raise TimeoutExpired(
                    self.args, orig_timeout,
                    output=b''.join(stdout_seq) if stdout_seq else None,
                    stderr=b''.join(stderr_seq) if stderr_seq else None)
E           subprocess.TimeoutExpired: Command '['/workspace/work/venv/bin/python', '-c', "\nimport sys\nfrom pathlib import Path\nimport checkpoint.app as entry\nimport checkpoint.elevation as elevation\nimport checkpoint.data_migration as migration\nfrom PySide6.QtWidgets import QMessageBox\nroot=Path(sys.argv[1]);outcome=sys.argv[2];calls=[]\ndef forbidden(*args,**kwargs):raise AssertionError('Dados ou cofre abertos antes da decisão UAC')\nmigration.prepare_data_directory=forbidden\ndef handoff(*args,**kwargs):\n    calls.append(kwargs)\n    if outcome=='cancel':raise elevation.ElevationCancelled()\n    if outcome=='different_account':raise ValueError('Conta diferente')\n    return 0\nelevation.elevate_startup=handoff\nQMessageBox.information=lambda *args:None\nQMessageBox.critical=lambda *args:None\nsys.frozen=True;sys.platform='win32';sys.argv=['Checkpoint.exe','--data-dir',str(root)]\nassert entry.main()==(2 if outcome=='different_account' else 0)\nassert len(calls)==1 and not root.exists()\n", '/tmp/c8dbcfb3f1de497c924befbec4324e30/dados-preservados', 'cancel']' timed out after 30 seconds

/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:1253: TimeoutExpired
____ test_frozen_startup_handles_uac_before_opening_data[different_account] ____

folder = PosixPath('/tmp/17355097473b40f88cf39b54ce53db75')
outcome = 'different_account'

    @pytest.mark.parametrize('outcome',['handoff','cancel','different_account'])
    def test_frozen_startup_handles_uac_before_opening_data(folder,outcome):
        import subprocess,sys,os
        code=r'''
    import sys
    from pathlib import Path
    import checkpoint.app as entry
    import checkpoint.elevation as elevation
    import checkpoint.data_migration as migration
    from PySide6.QtWidgets import QMessageBox
    root=Path(sys.argv[1]);outcome=sys.argv[2];calls=[]
    def forbidden(*args,**kwargs):raise AssertionError('Dados ou cofre abertos antes da decisão UAC')
    migration.prepare_data_directory=forbidden
    def handoff(*args,**kwargs):
        calls.append(kwargs)
        if outcome=='cancel':raise elevation.ElevationCancelled()
        if outcome=='different_account':raise ValueError('Conta diferente')
        return 0
    elevation.elevate_startup=handoff
    QMessageBox.information=lambda *args:None
    QMessageBox.critical=lambda *args:None
    sys.frozen=True;sys.platform='win32';sys.argv=['Checkpoint.exe','--data-dir',str(root)]
    assert entry.main()==(2 if outcome=='different_account' else 0)
    assert len(calls)==1 and not root.exists()
    '''
>       result=subprocess.run([sys.executable,'-c',code,str(folder/'dados-preservados'),outcome],cwd=Path(__file__).resolve().parents[1],env={**os.environ,'QT_QPA_PLATFORM':'offscreen'},capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_elevation_0137.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:550: in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:1209: in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:2116: in _communicate
    self._check_timeout(endtime, orig_timeout, stdout, stderr)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Popen: returncode: -9 args: ['/workspace/work/venv/bin/python', '-c', "\nim...>
endtime = 25758.331088436, orig_timeout = 30, stdout_seq = []
stderr_seq = [b'Fontconfig error: No writable cache directories\n', b'This plugin does not support propagateSizeHints()\n', b'This plugin does not support propagateSizeHints()\n', b'This plugin does not support propagateSizeHints()\n']
skip_check_and_raise = False

    def _check_timeout(self, endtime, orig_timeout, stdout_seq, stderr_seq,
                       skip_check_and_raise=False):
        """Convenience for checking if a timeout has expired."""
        if endtime is None:
            return
        if skip_check_and_raise or _time() > endtime:
>           raise TimeoutExpired(
                    self.args, orig_timeout,
                    output=b''.join(stdout_seq) if stdout_seq else None,
                    stderr=b''.join(stderr_seq) if stderr_seq else None)
E           subprocess.TimeoutExpired: Command '['/workspace/work/venv/bin/python', '-c', "\nimport sys\nfrom pathlib import Path\nimport checkpoint.app as entry\nimport checkpoint.elevation as elevation\nimport checkpoint.data_migration as migration\nfrom PySide6.QtWidgets import QMessageBox\nroot=Path(sys.argv[1]);outcome=sys.argv[2];calls=[]\ndef forbidden(*args,**kwargs):raise AssertionError('Dados ou cofre abertos antes da decisão UAC')\nmigration.prepare_data_directory=forbidden\ndef handoff(*args,**kwargs):\n    calls.append(kwargs)\n    if outcome=='cancel':raise elevation.ElevationCancelled()\n    if outcome=='different_account':raise ValueError('Conta diferente')\n    return 0\nelevation.elevate_startup=handoff\nQMessageBox.information=lambda *args:None\nQMessageBox.critical=lambda *args:None\nsys.frozen=True;sys.platform='win32';sys.argv=['Checkpoint.exe','--data-dir',str(root)]\nassert entry.main()==(2 if outcome=='different_account' else 0)\nassert len(calls)==1 and not root.exists()\n", '/tmp/17355097473b40f88cf39b54ce53db75/dados-preservados', 'different_account']' timed out after 30 seconds

/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/subprocess.py:1253: TimeoutExpired
=========================== short test summary info ============================
FAILED tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[cancel]
FAILED tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[different_account]
2 failed, 30 passed in 64.58s (0:01:04)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## all-new-before-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "tests/test_detail_polish_0139.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_dialog_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852316.661697,
  "exit_code": 0,
  "elapsed": 6.452728986740112
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_polish_0139.py tests/test_detail_polish_0139.py tests/test_settings_navigation_0139.py tests/test_dialog_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 2271b95c009210469c9375b2be1e0d0c7fb1a27b5b847f86ffbb19415e6a2a35:

````text
..................................................                       [100%]
50 passed in 6.05s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## visual-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/revisao-final"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852677.7131996,
  "exit_code": 0,
  "elapsed": 5.099299907684326
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/revisao-final
```

stdout integral — 44 bytes; SHA-256 ce1eb6b370b56932e9f433334a80e4a9189d177906fc70db1e23cdf8d5cd655f:

````text
/workspace/work/evidence-0139/revisao-final
````

stderr integral — 598 bytes; SHA-256 17c9ba146e5c6e87b9e190b905dce09f47023f9f97b78dba6b6277a9e276633b:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## startup-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_native_startup_0138.py",
    "tests/test_elevation_0137.py",
    "tests/test_dialog_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852719.7030199,
  "exit_code": 0,
  "elapsed": 3.823854923248291
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_native_startup_0138.py tests/test_elevation_0137.py tests/test_dialog_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 7727bcef8141e00baa2c97b7ef1eb8f48e22ee33b63ad4360f610a10d0a0556c:

````text
....................                                                     [100%]
20 passed in 3.37s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## regressions-base-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "tests/test_detail_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/base-0139-repro",
  "commit": "9dd9c93ce7baf0051bbc783323b401d4ba8c7059",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "exit_code": 1,
  "elapsed": 4.5805535316467285
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_home_polish_0139.py tests/test_polish_0139.py tests/test_detail_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 44655 bytes; SHA-256 528c9f43d34b16042fbfaf327ef748d943b5ca5ffb57cc2dc62a08e75480af4e:

````text
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF                                        [100%]
=================================== FAILURES ===================================
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0] ______

ui = (<checkpoint.window.MainWindow(0x390eae30) at 0x7fa73498e200>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/base-0139-repro/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_____ test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1] ______

ui = (<checkpoint.window.MainWindow(0x392b37f0) at 0x7fa7349e6440>, 1)

    def test_recent_sessions_keep_repeat_game_and_exclude_failures(ui):
>       from checkpoint.home_data import recent_sessions
E       ImportError: cannot import name 'recent_sessions' from 'checkpoint.home_data' (/workspace/work/base-0139-repro/checkpoint/home_data.py)

tests/test_home_polish_0139.py:30: ImportError
______ test_recent_cards_height_follows_content_and_button_fits[sample0] _______

ui = (<checkpoint.window.MainWindow(0x39454ec0) at 0x7fa734774980>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7fa7344dadc0>)

tests/test_home_polish_0139.py:60: AssertionError
______ test_recent_cards_height_follows_content_and_button_fits[sample1] _______

ui = (<checkpoint.window.MainWindow(0x39438870) at 0x7fa73479d180>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_recent_cards_height_follows_content_and_button_fits(ui, app):
        w, identity = ui
        sessions(w, identity)
        for size in ((1280, 800), (1920, 1080), (1000, 700), (1280, 800)):
            w.resize(*size)
            w.navigate(0)
            settle(app)
            section = w.pages[0].findChild(QWidget, 'homeRecentSection')
            right = w.pages[0].findChild(QWidget, 'homeWeekSummary')
            if size[0] >= 1280:
                assert section.mapTo(w, QPoint()).y() == right.mapTo(w, QPoint()).y()
            strip = section.findChild(GameStrip)
            assert strip.tiles
            for tile in strip.tiles:
                play = next(b for b in tile.findChildren(QPushButton) if b.property('homeContinue'))
                assert play.width() >= play.sizeHint().width()
                labels = tile.findChildren(SingleLineInfo)
                gaps = [b.y() - a.geometry().bottom() for a, b in zip(labels, labels[1:])]
                assert all(0 <= gap <= 13 for gap in gaps)
                assert 0 <= tile.height() - labels[-1].geometry().bottom() <= 16
>           assert any(l.text() == 'Últimas sessões' for l in section.findChildren(QLabel))
E           assert False
E            +  where False = any(<generator object test_recent_cards_height_follows_content_and_button_fits.<locals>.<genexpr> at 0x7fa734508110>)

tests/test_home_polish_0139.py:60: AssertionError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0] _____

ui = (<checkpoint.window.MainWindow(0x39676570) at 0x7fa7346eb580>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1] _____

ui = (<checkpoint.window.MainWindow(0x39262400) at 0x7fa734785c80>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
>       before = [tile.session_id for tile in strip.tiles]
                  ^^^^^^^^^^^^^^^
E       AttributeError: 'RecentGameCard' object has no attribute 'session_id'

tests/test_home_polish_0139.py:70: AttributeError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0] _

ui = (<checkpoint.window.MainWindow(0x3944e3d0) at 0x7fa734439a40>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/61f469cc66024559b2c42efdf519f50a')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa73435a340>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa73435a340> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fa73435a340>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa73435a340>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa73435a340> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fa73435a340>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
_ test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1] _

ui = (<checkpoint.window.MainWindow(0x3940eed0) at 0x7fa7343a0dc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/88ea88031e3649b4a5832119aa87e802')

    def test_recent_art_has_rounded_transparent_corners_without_losing_edges(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        w, identity = ui
        path = folder / 'cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        art = RecentArtwork({**w.library.get(identity), 'cover': str(path)}, w)
        art.resize(200, 300)
        art.show()
        settle(app)
        try:
            pixels = art.grab().toImage()
>           assert pixels.pixelColor(0, 0) != pixels.pixelColor(100, 2)
E           assert PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) != PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000)
E            +  where PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa7343b2800>(0, 0)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa7343b2800> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fa7343b2800>.pixelColor
E            +  and   PySide6.QtGui.QColor.fromRgbF(0.941176, 0.627451, 0.188235, 1.000000) = <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa7343b2800>(100, 2)
E            +    where <built-in method pixelColor of PySide6.QtGui.QImage object at 0x7fa7343b2800> = <PySide6.QtGui.QImage(QSize(200, 300),format=QImage::Format_RGB32,depth=32,devicePixelRatio=1,bytesPerLine=800,sizeInBytes=240000) at 0x7fa7343b2800>.pixelColor

tests/test_home_polish_0139.py:98: AssertionError
__ test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample0] ___

ui = (<checkpoint.window.MainWindow(0x394aecb0) at 0x7fa7343bdbc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/856a17cb344649b2b741213c0aedb07b')

    def test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
>       from checkpoint.home_components import HomeOfferRow, OfferThumbnail
E       ImportError: cannot import name 'HomeOfferRow' from 'checkpoint.home_components' (/workspace/work/base-0139-repro/checkpoint/home_components.py)

tests/test_home_polish_0139.py:110: ImportError
__ test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample1] ___

ui = (<checkpoint.window.MainWindow(0x39b9b450) at 0x7fa734514080>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/354df244b172407b96c064affc844da7')

    def test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
>       from checkpoint.home_components import HomeOfferRow, OfferThumbnail
E       ImportError: cannot import name 'HomeOfferRow' from 'checkpoint.home_components' (/workspace/work/base-0139-repro/checkpoint/home_components.py)

tests/test_home_polish_0139.py:110: ImportError
_____________ test_restricted_cover_has_no_dark_letterbox[sample0] _____________

ui = (<checkpoint.window.MainWindow(0x38caf6e0) at 0x7fa734515400>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/b2a0a6c14ed64e35a1b0767162eade97')

    def test_restricted_cover_has_no_dark_letterbox(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        from checkpoint.design_system import CardSurface
        from checkpoint.home_components import RecentGameCard
        w, identity = ui
        path = folder / 'letterbox-cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        game = {**w.library.get(identity), 'cover': str(path), 'last_played': datetime.now(timezone.utc).isoformat(), 'seconds': 0}
        tile = RecentGameCard(w, game)
        tile.resize(240, tile.sizeHint().height())
        tile.show()
        settle(app)
        try:
            art = tile.findChild(RecentArtwork)
            target = art.image_target()
>           assert target.width() < art.width()
E           assert 214.0 < 214
E            +  where 214.0 = <built-in method width of PySide6.QtCore.QRectF object at 0x7fa73438f7c0>()
E            +    where <built-in method width of PySide6.QtCore.QRectF object at 0x7fa73438f7c0> = PySide6.QtCore.QRectF(0.000000, 0.000000, 214.000000, 321.000000).width
E            +  and   214 = <built-in method width of RecentArtwork object at 0x7fa73436ebc0>()
E            +    where <built-in method width of RecentArtwork object at 0x7fa73436ebc0> = <checkpoint.home_components.RecentArtwork(0x39b51020, name="recentGameArtwork") at 0x7fa73436ebc0>.width

tests/test_home_polish_0139.py:154: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_____________ test_restricted_cover_has_no_dark_letterbox[sample1] _____________

ui = (<checkpoint.window.MainWindow(0x3935c840) at 0x7fa734390a80>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/5323ad9206bf40b9b6939a5f48b72efe')

    def test_restricted_cover_has_no_dark_letterbox(ui, app, folder):
        from PySide6.QtGui import QImage, QColor
        from checkpoint.design_system import CardSurface
        from checkpoint.home_components import RecentGameCard
        w, identity = ui
        path = folder / 'letterbox-cover.png'
        image = QImage(200, 300, QImage.Format_RGB32)
        image.fill(QColor('#f0a030'))
        assert image.save(str(path))
        game = {**w.library.get(identity), 'cover': str(path), 'last_played': datetime.now(timezone.utc).isoformat(), 'seconds': 0}
        tile = RecentGameCard(w, game)
        tile.resize(240, tile.sizeHint().height())
        tile.show()
        settle(app)
        try:
            art = tile.findChild(RecentArtwork)
            target = art.image_target()
>           assert target.width() < art.width()
E           assert 214.0 < 214
E            +  where 214.0 = <built-in method width of PySide6.QtCore.QRectF object at 0x7fa734515040>()
E            +    where <built-in method width of PySide6.QtCore.QRectF object at 0x7fa734515040> = PySide6.QtCore.QRectF(0.000000, 0.000000, 214.000000, 321.000000).width
E            +  and   214 = <built-in method width of RecentArtwork object at 0x7fa734392140>()
E            +    where <built-in method width of RecentArtwork object at 0x7fa734392140> = <checkpoint.home_components.RecentArtwork(0x39afc620, name="recentGameArtwork") at 0x7fa734392140>.width

tests/test_home_polish_0139.py:154: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0] _____

ui = (<checkpoint.window.MainWindow(0x391125c0) at 0x7fa7344eb580>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7fa73436fbc0>()
E                +    where <built-in method width of WishCard object at 0x7fa73436fbc0> = <checkpoint.collection_views.WishCard(0x3990b250, name="panel") at 0x7fa73436fbc0>.width

tests/test_polish_0139.py:29: AssertionError
_____ test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1] _____

ui = (<checkpoint.window.MainWindow(0x392532d0) at 0x7fa734343dc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_two_wishes_remain_compact_and_wide_window_adds_columns(ui, app):
        from checkpoint.collection_views import WishGrid, WishLogo
        w, identity = ui
        other = w.library.save_game({'title': 'Metroid Fusion', 'platform': 'GBA'})
        with w.library.sql:
            for game_id in (identity, other):
                w.library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)', (game_id,))
        columns = []
        for size in ((1280, 800), (1920, 1080)):
            w.resize(*size)
            w.navigate(2)
            settle(app)
            grid = w.pages[2].findChild(WishGrid)
            columns.append(grid.columns)
            for card in grid.cards:
>               assert card.width() <= 280
E               assert 326 <= 280
E                +  where 326 = <built-in method width of WishCard object at 0x7fa73441ae80>()
E                +    where <built-in method width of WishCard object at 0x7fa73441ae80> = <checkpoint.collection_views.WishCard(0x393a3d40, name="panel") at 0x7fa73441ae80>.width

tests/test_polish_0139.py:29: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x396be880) at 0x7fa734439a80>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        notes = ('Texto curto que deve permanecer íntegro.', 'Texto próprio de outra extensão para conferir o alinhamento superior dos cards de Diário na mesma linha da grade.')
        for game_id, note in zip((identity, other), notes):
            w.library.add_diary(game_id, note)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7fa731f20450>)

tests/test_polish_0139.py:51: AssertionError
__________ test_diary_only_is_compact_and_mixed_cards_align[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x398a47f0) at 0x7fa7344182c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_diary_only_is_compact_and_mixed_cards_align(ui, app):
        from checkpoint.collection_views import build_memories
        from checkpoint.design_system import CardGrid
        w, identity = ui
        other = w.library.save_game({'title': 'Hades'})
        notes = ('Texto curto que deve permanecer íntegro.', 'Texto próprio de outra extensão para conferir o alinhamento superior dos cards de Diário na mesma linha da grade.')
        for game_id, note in zip((identity, other), notes):
            w.library.add_diary(game_id, note)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM diary_entries')]
        w.navigate(3)
        settle(app)
        tabs = w.pages[3].findChild(QWidget, 'memoryTabs')
        tabs.setCurrentIndex(1)
        settle(app)
        grid = tabs.currentWidget().findChild(CardGrid, 'memoriesGrid')
>       assert all(card.height() < 240 for card in grid.cards)
E       assert False
E        +  where False = all(<generator object test_diary_only_is_compact_and_mixed_cards_align.<locals>.<genexpr> at 0x7fa731f212f0>)

tests/test_polish_0139.py:51: AssertionError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0] ______

ui = (<checkpoint.window.MainWindow(0x392383b0) at 0x7fa734520840>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:70: AttributeError
______ test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1] ______

ui = (<checkpoint.window.MainWindow(0x393ac5a0) at 0x7fa731dd7680>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_cover_mouse_selection_and_keyboard_focus_stay_on_art(ui, app):
        from checkpoint.settings_previews import CoverSizeChoices
        w, _ = ui
        w.navigate(5)
        choices = w.pages[5].findChild(CoverSizeChoices)
        choices.show()
        settle(app)
        choice = choices.group.button(70)
        QTest.mouseClick(choice, Qt.LeftButton, pos=choice.artwork_rect().center().toPoint())
        assert choice.isChecked()
>       assert not choice.keyboard_focus
                   ^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'CoverChoice' object has no attribute 'keyboard_focus'

tests/test_polish_0139.py:70: AttributeError
_______________ test_black_is_neutral_and_other_themes_preserved _______________

    def test_black_is_neutral_and_other_themes_preserved():
        from checkpoint.theme import THEMES
        from PySide6.QtGui import QColor, QIcon
        black = THEMES['black'].colors
        for key in ('background', 'sidebar', 'surface', 'elevated', 'card', 'panel', 'input', 'button', 'border', 'border_subtle'):
            c = QColor(black[key])
>           assert c.red() == c.green() == c.blue(), (key, black[key])
E           AssertionError: ('background', '#0e141d')
E           assert 14 == 20
E            +  where 14 = <built-in method red of PySide6.QtGui.QColor object at 0x7fa734708480>()
E            +    where <built-in method red of PySide6.QtGui.QColor object at 0x7fa734708480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).red
E            +  and   20 = <built-in method green of PySide6.QtGui.QColor object at 0x7fa734708480>()
E            +    where <built-in method green of PySide6.QtGui.QColor object at 0x7fa734708480> = PySide6.QtGui.QColor.fromRgbF(0.054902, 0.078431, 0.113725, 1.000000).green

tests/test_polish_0139.py:84: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x39b45310) at 0x7fa731e8fc80>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            for enabled, mode, foreground in ((True, QIcon.Normal, 'on_accent'), (False, QIcon.Disabled, 'disabled')):
                button.setEnabled(enabled)
                pix = button.icon().pixmap(20, 20, mode).toImage()
                expected = QColor(w.theme.colors[foreground])
                opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>               assert opaque and all(max(abs(a-b) for a,b in zip(c.getRgb()[:3], expected.getRgb()[:3])) <= 1 for c in opaque)
E               assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E                +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7fa731dfcf20>)

tests/test_polish_0139.py:103: AssertionError
____________ test_add_wish_icon_matches_primary_foreground[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x39bdccb0) at 0x7fa731e5fbc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_add_wish_icon_matches_primary_foreground(ui, app):
        from checkpoint.ui_components import action
        from checkpoint.theme import get_theme
        from PySide6.QtGui import QColor
        w, _ = ui
        button = action('+ Adicionar desejo', lambda: None, True)
        button.show()
        settle(app)
        try:
            for enabled, mode, foreground in ((True, QIcon.Normal, 'on_accent'), (False, QIcon.Disabled, 'disabled')):
                button.setEnabled(enabled)
                pix = button.icon().pixmap(20, 20, mode).toImage()
                expected = QColor(w.theme.colors[foreground])
                opaque = [pix.pixelColor(x, y) for x in range(pix.width()) for y in range(pix.height()) if pix.pixelColor(x, y).alpha() > 240]
>               assert opaque and all(max(abs(a-b) for a,b in zip(c.getRgb()[:3], expected.getRgb()[:3])) <= 1 for c in opaque)
E               assert ([PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.9556...romRgbF(0.943542, 0.955642, 0.971771, 0.972549), PySide6.QtGui.QColor.fromRgbF(0.943542, 0.955642, 0.971771, 0.972549)] and False)
E                +  where False = all(<generator object test_add_wish_icon_matches_primary_foreground.<locals>.<genexpr> at 0x7fa731dfd140>)

tests/test_polish_0139.py:103: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample0] _______________

ui = (<checkpoint.window.MainWindow(0x3a02d0b0) at 0x7fa731e19d00>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.mapTo(view, QPoint()).x() - right <= 24
E       assert 12 <= (738 - 737)
E        +  where 738 = <built-in method x of PySide6.QtCore.QPoint object at 0x7fa731e1a800>()
E        +    where <built-in method x of PySide6.QtCore.QPoint object at 0x7fa731e1a800> = PySide6.QtCore.QPoint(738, 7).x
E        +      where PySide6.QtCore.QPoint(738, 7) = <built-in method mapTo of PySide6.QtWidgets.QScrollBar object at 0x7fa731e0b480>(<checkpoint.library_list.LibraryList(0x39d16410, name="libraryList") at 0x7fa731e0b300>, PySide6.QtCore.QPoint(0, 0))
E        +        where <built-in method mapTo of PySide6.QtWidgets.QScrollBar object at 0x7fa731e0b480> = <PySide6.QtWidgets.QScrollBar(0x393a4de0) at 0x7fa731e0b480>.mapTo
E        +        and   PySide6.QtCore.QPoint(0, 0) = QPoint()

tests/test_polish_0139.py:120: AssertionError
______________ test_library_scrollbar_has_stable_gutter[sample1] _______________

ui = (<checkpoint.window.MainWindow(0x39883b40) at 0x7fa73441b5c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_library_scrollbar_has_stable_gutter(ui, app):
        w, identity = ui
        for n in range(30):
            w.library.save_game({'title': f'Outro jogo {n}'})
        w.navigate(1)
        w.view.setCurrentIndex(1)
        settle(app)
        view = w.game_list
        bar = view.verticalScrollBar()
        assert bar.maximum() > 0
        rect = view.visualItemRect(view.item(0))
        right = view.viewport().mapTo(view, rect.topRight()).x()
>       assert 12 <= bar.mapTo(view, QPoint()).x() - right <= 24
E       assert 12 <= (1138 - 1137)
E        +  where 1138 = <built-in method x of PySide6.QtCore.QPoint object at 0x7fa7343bff40>()
E        +    where <built-in method x of PySide6.QtCore.QPoint object at 0x7fa7343bff40> = PySide6.QtCore.QPoint(1138, 7).x
E        +      where PySide6.QtCore.QPoint(1138, 7) = <built-in method mapTo of PySide6.QtWidgets.QScrollBar object at 0x7fa731e5d740>(<checkpoint.library_list.LibraryList(0x39977190, name="libraryList") at 0x7fa731e5d140>, PySide6.QtCore.QPoint(0, 0))
E        +        where <built-in method mapTo of PySide6.QtWidgets.QScrollBar object at 0x7fa731e5d740> = <PySide6.QtWidgets.QScrollBar(0x39be19f0) at 0x7fa731e5d740>.mapTo
E        +        and   PySide6.QtCore.QPoint(0, 0) = QPoint()

tests/test_polish_0139.py:120: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample0] ________

ui = (<checkpoint.window.MainWindow(0x3974bbc0) at 0x7fa731f3cc40>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x39bab1e0) at 0x7fa731c1f000>, <PySide6.QtWidgets.QPushButton(0x39bab170) at 0x7fa731c3c940>])

tests/test_polish_0139.py:131: AssertionError
________ test_saves_empty_has_one_compact_configuration_action[sample1] ________

ui = (<checkpoint.window.MainWindow(0x397bdcc0) at 0x7fa73451e040>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_saves_empty_has_one_compact_configuration_action(ui, app):
        w, identity = ui
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        tab = w.detail_tabs.currentWidget()
        buttons = [b for b in tab.findChildren(QPushButton) if b.text() == 'Configurar saves']
>       assert len(buttons) == 1
E       assert 2 == 1
E        +  where 2 = len([<PySide6.QtWidgets.QPushButton(0x39ddd8e0) at 0x7fa73441b400>, <PySide6.QtWidgets.QPushButton(0x39ddd870) at 0x7fa731c17040>])

tests/test_polish_0139.py:131: AssertionError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample0] __

ui = (<checkpoint.window.MainWindow(0x39349ae0) at 0x7fa731e092c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
        w.library.delete(identity)
        w.library.delete(other)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(5)
        settle(app)
        titles = [w.settings_tabs.tabText(i) for i in range(w.settings_tabs.count())]
>       assert 'Emuladores' in titles and 'Lixeira' in titles
E       AssertionError: assert ('Emuladores' in ['Aparência', 'Conexões', 'Downloads', 'Dados e backup'])

tests/test_polish_0139.py:145: AssertionError
_ test_settings_exposes_emulators_and_trash_without_changing_records[sample1] __

ui = (<checkpoint.window.MainWindow(0x3941e790) at 0x7fa731c3c940>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_settings_exposes_emulators_and_trash_without_changing_records(ui, app):
        w, identity = ui
        other = w.library.save_game({'title': w.library.get(identity)['title'], 'platform': 'Switch'})
        w.library.delete(identity)
        w.library.delete(other)
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        w.navigate(5)
        settle(app)
        titles = [w.settings_tabs.tabText(i) for i in range(w.settings_tabs.count())]
>       assert 'Emuladores' in titles and 'Lixeira' in titles
E       AssertionError: assert ('Emuladores' in ['Aparência', 'Conexões', 'Downloads', 'Dados e backup'])

tests/test_polish_0139.py:145: AssertionError
____________ test_mixed_diary_preview_matches_capture_area[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x3921c9f0) at 0x7fa731c0f880>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/e28a2b9a5ee34980a01d6aa1d19c024c')

    def test_mixed_diary_preview_matches_capture_area(ui, app, folder):
        from checkpoint.collection_views import memory_card
        from checkpoint.design_system import ArtworkButton
        from PySide6.QtWidgets import QTextEdit
        from PySide6.QtGui import QImage
        w, identity = ui
        path = folder/'capture.png'
        picture = QImage(400, 240, QImage.Format_RGB32);picture.fill(0)
        assert picture.save(str(path))
        common = {'id': 1, 'game_id': identity, 'title': w.library.get(identity)['title'],
            'created_at': '2026-11-16T12:00:00+00:00', 'text': 'Minha nota curta.',
            'path': str(path), 'caption': ''}
        diary = memory_card(w, {**common, 'kind': 'diary'})
        media = memory_card(w, {**common, 'kind': 'image'})
        for widget in (diary, media):
            widget.resize(320, 320);widget.show()
        settle(app)
        try:
            note = diary.findChild(QTextEdit, 'memoryTextArea')
            art = media.findChild(ArtworkButton)
>           assert note is not None and art is not None
E           assert (None is not None)

tests/test_polish_0139.py:174: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
____________ test_mixed_diary_preview_matches_capture_area[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x3937b180) at 0x7fa731f3ccc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>
folder = PosixPath('/tmp/99e83e878e704c129720ed1cef17b03b')

    def test_mixed_diary_preview_matches_capture_area(ui, app, folder):
        from checkpoint.collection_views import memory_card
        from checkpoint.design_system import ArtworkButton
        from PySide6.QtWidgets import QTextEdit
        from PySide6.QtGui import QImage
        w, identity = ui
        path = folder/'capture.png'
        picture = QImage(400, 240, QImage.Format_RGB32);picture.fill(0)
        assert picture.save(str(path))
        common = {'id': 1, 'game_id': identity, 'title': w.library.get(identity)['title'],
            'created_at': '2026-11-16T12:00:00+00:00', 'text': 'Minha nota curta.',
            'path': str(path), 'caption': ''}
        diary = memory_card(w, {**common, 'kind': 'diary'})
        media = memory_card(w, {**common, 'kind': 'image'})
        for widget in (diary, media):
            widget.resize(320, 320);widget.show()
        settle(app)
        try:
            note = diary.findChild(QTextEdit, 'memoryTextArea')
            art = media.findChild(ArtworkButton)
>           assert note is not None and art is not None
E           assert (None is not None)

tests/test_polish_0139.py:174: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample0] ______

ui = (<checkpoint.window.MainWindow(0x39790710) at 0x7fa731e11900>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
>           assert label is not None
E           assert None is not None

tests/test_detail_polish_0139.py:25: AssertionError
_____ test_long_file_name_uses_central_width_and_keeps_full_name[sample1] ______

ui = (<checkpoint.window.MainWindow(0x392b3770) at 0x7fa734386480>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
        w, identity = ui
        filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
        with w.library.sql:
            w.library.sql.execute(
                'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
                (identity, 'isolated-0139', filename, 'N64'))
        for width in (1000, 1280, 1920):
            w.resize(width, 800)
            w.detail(identity)
            w.detail_tabs.setCurrentIndex(3)
            settle(app)
            label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
>           assert label is not None
E           assert None is not None

tests/test_detail_polish_0139.py:25: AssertionError
_____ test_completions_use_recorded_timestamp_not_current_status[sample0] ______

ui = (<checkpoint.window.MainWindow(0x39dc6fb0) at 0x7fa731f68340>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_completions_use_recorded_timestamp_not_current_status(ui, app):
        from checkpoint.statistics_periods import period_stats
        w, identity = ui
        other = w.library.save_game({'title': 'Hades', 'status': 'Concluído'})
        now = datetime.now(timezone.utc)
        with w.library.sql:
            w.library.sql.execute("UPDATE games SET status='Concluído',completed_at=NULL WHERE id=?", (identity,))
            w.library.sql.execute("UPDATE games SET completed_at=? WHERE id=?", ((now-timedelta(days=1)).isoformat(), other))
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        assert sum(period_stats(w.library, 'all')['completions'].values()) == 1
        w.navigate(4)
        period = w.pages[4].findChild(QComboBox, 'statisticsPeriod')
        period.setCurrentIndex(period.findData('all'))
        settle(app)
        frame = w.pages[4].findChild(QWidget, 'completionMetrics')
>       assert frame is not None
E       assert None is not None

tests/test_detail_polish_0139.py:52: AssertionError
_____ test_completions_use_recorded_timestamp_not_current_status[sample1] ______

ui = (<checkpoint.window.MainWindow(0x39741df0) at 0x7fa73479f480>, 1)
app = <PySide6.QtWidgets.QApplication(0x38f60ed0) at 0x7fa734993400>

    def test_completions_use_recorded_timestamp_not_current_status(ui, app):
        from checkpoint.statistics_periods import period_stats
        w, identity = ui
        other = w.library.save_game({'title': 'Hades', 'status': 'Concluído'})
        now = datetime.now(timezone.utc)
        with w.library.sql:
            w.library.sql.execute("UPDATE games SET status='Concluído',completed_at=NULL WHERE id=?", (identity,))
            w.library.sql.execute("UPDATE games SET completed_at=? WHERE id=?", ((now-timedelta(days=1)).isoformat(), other))
        before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
        assert sum(period_stats(w.library, 'all')['completions'].values()) == 1
        w.navigate(4)
        period = w.pages[4].findChild(QComboBox, 'statisticsPeriod')
        period.setCurrentIndex(period.findData('all'))
        settle(app)
        frame = w.pages[4].findChild(QWidget, 'completionMetrics')
>       assert frame is not None
E       assert None is not None

tests/test_detail_polish_0139.py:52: AssertionError
=========================== short test summary info ============================
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample1]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0]
FAILED tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1]
FAILED tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample0]
FAILED tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample1]
FAILED tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample0]
FAILED tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample1]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0]
FAILED tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample0]
FAILED tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample1]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0]
FAILED tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1]
FAILED tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
FAILED tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
FAILED tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample0]
FAILED tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample1]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample0]
FAILED tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample1]
FAILED tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample0]
FAILED tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample1]
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample0]
FAILED tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample1]
FAILED tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample0]
FAILED tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample1]
33 failed in 4.12s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## emulator-actions-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_settings_navigation_0139.py",
    "tests/test_local_rom_0137.py",
    "tests/test_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852863.2815228,
  "exit_code": 0,
  "elapsed": 3.733006477355957
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_settings_navigation_0139.py tests/test_local_rom_0137.py tests/test_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 fed5b4ba794fed02f1ca39fa664bc76ec7b3b228621f52acc2262bd0aeffa52a:

````text
......................................                                   [100%]
38 passed in 3.39s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## emulator-actions-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/emuladores-botoes",
    "--only",
    "settings,files"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852864.673201,
  "exit_code": 0,
  "elapsed": 1.7990121841430664
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/emuladores-botoes --only settings,files
```

stdout integral — 48 bytes; SHA-256 b8b82b7ca377d6edd3bb9da9016d986747ba67ae47e27b664166cdf182043fc6:

````text
/workspace/work/evidence-0139/emuladores-botoes
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## session-dialog-spacing-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_dialog_polish_0139.py",
    "tests/test_sessions_0135.py",
    "tests/test_launch_0135.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852948.6792264,
  "exit_code": 1,
  "elapsed": 3.168259859085083
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_dialog_polish_0139.py tests/test_sessions_0135.py tests/test_launch_0135.py -q -p no:cacheprovider
```

stdout integral — 1572 bytes; SHA-256 e2a480ddf1767ecff846da86b6889b9dbb50dddad05a963718737d338d701b00:

````text
.F.................                                                      [100%]
=================================== FAILURES ===================================
__ test_standard_question_theme_portuguese_default_and_cancellation[sample1] ___

ui = (<checkpoint.window.MainWindow(0xcee57e0) at 0x7f8f8291bdc0>, 1)

    def test_standard_question_theme_portuguese_default_and_cancellation(ui):
        w,_=ui
        result,captured=observe_modal(w,lambda:AppMessages.question(w,'Remover registro','Confirmar ação de teste?'))
        assert result==QMessageBox.No
        assert set(captured['buttons'])=={'Sim','Não'}
        assert captured['default']=='Não' and captured['prepared']
>       assert captured['screen'].contains(captured['geometry'])
E       assert False
E        +  where False = <built-in method contains of PySide6.QtCore.QRect object at 0x7f8f8874b2c0>(PySide6.QtCore.QRect(550, 352, 264, 132))
E        +    where <built-in method contains of PySide6.QtCore.QRect object at 0x7f8f8874b2c0> = PySide6.QtCore.QRect(0, 0, 800, 800).contains

tests/test_dialog_polish_0139.py:40: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample1]
1 failed, 18 passed in 2.68s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## session-dialog-spacing-visual

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/dialogo-espacamento",
    "--only",
    "dialogs"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794852950.0727975,
  "exit_code": 0,
  "elapsed": 1.69919753074646
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/dialogo-espacamento --only dialogs
```

stdout integral — 50 bytes; SHA-256 ed7c06212965fab041924da5b61a34641a4d58fdb56386478e76c15fdfe20f16:

````text
/workspace/work/evidence-0139/dialogo-espacamento
````

stderr integral — 598 bytes; SHA-256 17c9ba146e5c6e87b9e190b905dce09f47023f9f97b78dba6b6277a9e276633b:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## dialog-layout-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_dialog_polish_0139.py",
    "tests/test_elevation_0137.py",
    "tests/test_sessions_0135.py",
    "tests/test_launch_0135.py",
    "tests/test_settings_navigation_0139.py",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853082.9339855,
  "exit_code": 0,
  "elapsed": 7.813979625701904
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_dialog_polish_0139.py tests/test_elevation_0137.py tests/test_sessions_0135.py tests/test_launch_0135.py tests/test_settings_navigation_0139.py tests/test_home_polish_0139.py tests/test_polish_0139.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 2d97079d44f0e9a7dfc657d3c944e832e986417e029756f78a30e4d7885bbe48:

````text
..............................................................           [100%]
62 passed in 7.41s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## dpi-150

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/dpi-150",
    "--screen-width",
    "2880",
    "--screen-height",
    "1620",
    "--only",
    "home,wishes,appearance,settings,dialogs"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853113.6946557,
  "exit_code": 0,
  "elapsed": 5.2294676303863525
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/dpi-150 --screen-width 2880 --screen-height 1620 --only home,wishes,appearance,settings,dialogs
```

stdout integral — 38 bytes; SHA-256 bf952c32e8e5d5073925857d77c0144cc92f01a53dcea518ee138ae00cfc270f:

````text
/workspace/work/evidence-0139/dpi-150
````

stderr integral — 698 bytes; SHA-256 3664ca416e7f5fefb138b283f0537946e0f14e2c9df58cd7b2284cbd205a4f71:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## dpi-200

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/dpi-200",
    "--screen-width",
    "3840",
    "--screen-height",
    "2160",
    "--only",
    "home,wishes,appearance,settings,dialogs"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853115.094178,
  "exit_code": 0,
  "elapsed": 6.606802940368652
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/dpi-200 --screen-width 3840 --screen-height 2160 --only home,wishes,appearance,settings,dialogs
```

stdout integral — 38 bytes; SHA-256 00eb77c752d9e66dc8e686e672840942118b888eefb5580892c5aa04e3bd5d79:

````text
/workspace/work/evidence-0139/dpi-200
````

stderr integral — 698 bytes; SHA-256 3664ca416e7f5fefb138b283f0537946e0f14e2c9df58cd7b2284cbd205a4f71:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## full-linux

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853293.1794245,
  "exit_code": -15,
  "elapsed": 385.59299063682556
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 366 bytes; SHA-256 02766b7801083fff3a1817a94ddba62c75a88c770747b7db2b452808819f1215:

````text
........................................................................ [  9%]
.......F..F............................................................. [ 19%]
........................................................................ [ 28%]
.................................................F.........F............ [ 38%]
..............................................
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## smoke-source

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "checkpoint.app",
    "--smoke-test",
    "--data-dir",
    "/workspace/work/evidence-0139/smoke-source-data"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853426.1604688,
  "exit_code": 0,
  "elapsed": 1.093796968460083
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m checkpoint.app --smoke-test --data-dir /workspace/work/evidence-0139/smoke-source-data
```

stdout integral — 50 bytes; SHA-256 21079070cb6b0ffbec368584ab7b5ce39d68facddbbe2c030e21bb38c87e71c5:

````text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## smoke-save

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "checkpoint.app",
    "--save-smoke-test",
    "--data-dir",
    "/workspace/work/evidence-0139/smoke-save-data"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853427.451592,
  "exit_code": 0,
  "elapsed": 0.8645734786987305
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /workspace/work/evidence-0139/smoke-save-data
```

stdout integral — 61 bytes; SHA-256 8890c130538d7fa1fcec658a22c44907c1c6a61300d8cf9298440208eac67e5d:

````text
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## collect-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests",
    "--collect-only",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853469.1777263,
  "exit_code": 0,
  "elapsed": 1.0405499935150146
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests --collect-only -q -p no:cacheprovider
```

stdout integral — 67586 bytes; SHA-256 82910990767c035bdceaf1f0944c1383deda6141184b8581e4e737b8150d8ddf:

````text
tests/test_add_dialog_0129.py::test_add_dialog_has_one_internal_close_and_no_local_automation_option
tests/test_add_dialog_entrypoints.py::test_wishlist_add_keeps_button_signal_separate_from_drive_file
tests/test_add_from_search_flow.py::test_search_selection_persists_text_source_and_images
tests/test_add_from_search_flow.py::test_ready_search_result_saves_all_text
tests/test_artwork_async_0137.py::test_cold_images_decode_outside_gui_and_do_not_block_events
tests/test_artwork_async_0137.py::test_async_cache_bounds_queue_and_preserves_changed_image
tests/test_artwork_async_0137.py::test_async_transparent_logo_matches_original_raster
tests/test_auto_artwork.py::test_three_kinds_cached_with_provenance_and_no_redownload
tests/test_auto_artwork.py::test_unknown_identity_never_searches_or_guesses
tests/test_auto_artwork.py::test_preserves_manual_cover_and_fetches_other_kinds
tests/test_auto_artwork.py::test_partial_failure_keeps_game_and_successful_art
tests/test_auto_artwork.py::test_changed_cover_during_download_is_not_overwritten
tests/test_auto_artwork.py::test_identity_collision_is_rejected
tests/test_auto_artwork.py::test_disabled_auto_and_manual_retry
tests/test_auto_artwork.py::test_exact_steam_id_resolution_without_title_search
tests/test_auto_artwork.py::test_provider_steam_mapping_and_safe_art_ranking
tests/test_auto_artwork.py::test_background_failure_does_not_raise_into_rom_operation
tests/test_auto_artwork.py::test_missing_key_is_explicit_and_does_not_mutate_game
tests/test_auto_artwork.py::test_identifying_dialog_has_automatic_action_and_preference
tests/test_auto_artwork.py::test_confirmed_catalog_name_standardizes_display_title
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape0]
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape1]
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape2]
tests/test_avatar_crop_0137.py::test_invalid_profile_photo_keeps_existing_selection
tests/test_avatar_crop_0137.py::test_photo_orientation_and_drag_are_applied_without_modifying_source
tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample0]
tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample1]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1]
tests/test_banner_aspect_0136.py::test_all_four_edges_remain_visible[Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_all_four_edges_remain_visible[Hades-shape1]
tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample0]
tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample1]
tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past]
tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Metroid Fusion]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1]
tests/test_bugs_0134.py::test_selected_drive_result_is_not_not_found[sample0]
tests/test_bugs_0134.py::test_selected_drive_result_is_not_not_found[sample1]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-description-Um mundo para explorar.]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-cover-imagem-local.png]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-price-2490]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-description-Um mundo para explorar.]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-cover-imagem-local.png]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-price-2490]
tests/test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence[sample0]
tests/test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence[sample1]
tests/test_bugs_0134.py::test_artwork_close_refreshes_library_without_restart[sample0]
tests/test_bugs_0134.py::test_artwork_close_refreshes_library_without_restart[sample1]
tests/test_bugs_0134.py::test_detail_menu_stays_inside_window[sample0]
tests/test_bugs_0134.py::test_detail_menu_stays_inside_window[sample1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size0]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size2]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size0]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size2]
tests/test_bugs_0134.py::test_wikipedia_detail_has_only_short_intro[sample0]
tests/test_bugs_0134.py::test_wikipedia_detail_has_only_short_intro[sample1]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Zelda: A Link to the Past]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Metroid Fusion]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Zelda: A Link to the Past]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Metroid Fusion]
tests/test_capture_0136.py::test_registration_is_atomic_and_released
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[S]
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[Ctrl+S, Ctrl+P]
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[Ctrl+Left]
tests/test_capture_0136.py::test_foreground_selects_session_not_open_detail[sample0]
tests/test_capture_0136.py::test_foreground_selects_session_not_open_detail[sample1]
tests/test_card_layout.py::test_six_columns_at_default_and_responsive_scaling
tests/test_card_layout.py::test_density_preference_preserved_in_settings_without_schema_change
tests/test_card_layout.py::test_grids_keep_their_proportions_and_size_control_keeps_font_and_items
tests/test_catalog.py::test_catalog_exact_checksum_platform_and_import_idempotence
tests/test_complete_layout.py::test_wishlist_uses_current_prices_and_removal_preserves_game
tests/test_complete_layout.py::test_memories_excludes_removed_games_and_filters_diary
tests/test_complete_layout.py::test_editor_all_tabs_keep_values_and_manual_images
tests/test_complete_layout.py::test_favorite_action_keeps_detail_draft
tests/test_complete_layout.py::test_layout_header_and_library_fit_small_window
tests/test_complete_layout.py::test_theme_swatches_and_profile_apply_without_losing_data
tests/test_completion_queue.py::test_queue_is_serial_and_continues_after_failure
tests/test_completion_queue.py::test_cancel_drops_pending_games_without_destroying_running_job
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-70-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-70-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-150-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-150-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-70-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-70-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-150-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-150-size1]
tests/test_cover_preview_0135.py::test_old_percent_preserved_and_keyboard_selects[sample0]
tests/test_cover_preview_0135.py::test_old_percent_preserved_and_keyboard_selects[sample1]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size0]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size1]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size0]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size1]
tests/test_data_migration.py::test_first_open_copies_complete_library_and_wal_snapshot
tests/test_data_migration.py::test_first_open_without_legacy_creates_only_new_directory
tests/test_data_migration.py::test_existing_new_directory_is_not_overwritten
tests/test_data_migration.py::test_integrity_failure_never_publishes_or_opens_copied_database
tests/test_data_migration.py::test_credentials_copy_without_overwriting_or_logging_values
tests/test_data_migration.py::test_legacy_light_preference_becomes_default_without_losing_others
tests/test_data_migration.py::test_instance_lock_also_prevents_concurrent_migration
tests/test_data_migration.py::test_explicit_directory_never_uses_real_localappdata
tests/test_data_migration.py::test_corrupt_source_and_empty_existing_destination_are_preserved
tests/test_data_migration.py::test_vault_failure_preserves_source_without_logging_error_payload
tests/test_data_migration.py::test_running_legacy_instance_blocks_copy
tests/test_data_migration.py::test_regular_files_with_similar_names_are_not_discarded
tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Zelda: A Link to the Past]
tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Metroid Fusion]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-rawg]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-steam]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-drive]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-rawg]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-steam]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-drive]
tests/test_detail_0134.py::test_zero_new_fields_is_not_reported_as_search_failure[sample0]
tests/test_detail_0134.py::test_zero_new_fields_is_not_reported_as_search_failure[sample1]
tests/test_detail_0134.py::test_menu_edge_click_runs_only_named_action[sample0]
tests/test_detail_0134.py::test_menu_edge_click_runs_only_named_action[sample1]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Metroid Fusion]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Metroid Fusion]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Metroid Fusion]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Metroid Fusion]
tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample0]
tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample1]
tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample0]
tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample1]
tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample0]
tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample1]
tests/test_dialog_polish_0139.py::test_session_prompt_has_explicit_actions_and_safe_default[sample0]
tests/test_dialog_polish_0139.py::test_session_prompt_has_explicit_actions_and_safe_default[sample1]
tests/test_dialog_polish_0139.py::test_standard_input_translates_cancel_without_changing_selection[sample0]
tests/test_dialog_polish_0139.py::test_standard_input_translates_cancel_without_changing_selection[sample1]
tests/test_dialog_polish_0139.py::test_authorized_image_viewer_keeps_image_proportions_and_original[sample0]
tests/test_dialog_polish_0139.py::test_authorized_image_viewer_keeps_image_proportions_and_original[sample1]
tests/test_dialog_polish_0139.py::test_only_authorized_protected_constructor_changed
tests/test_drive.py::test_scan_never_downloads_and_keeps_versions
tests/test_drive.py::test_failed_scan_does_not_advance_cursor
tests/test_drive.py::test_failed_download_not_available
tests/test_drive.py::test_full_rescan_marks_missing_without_deleting_local
tests/test_drive.py::test_folder_platform_aliases[/Nintendo Game Boy Advanced/Pok\xe9mon-Game Boy Advance]
tests/test_drive.py::test_folder_platform_aliases[/Super Nintendo (SNES)/Extras-SNES]
tests/test_drive.py::test_folder_platform_aliases[/  super_nintendo (snes) /Extras-SNES]
tests/test_drive.py::test_folder_platform_aliases[/Switch-Nintendo Switch]
tests/test_drive.py::test_folder_platform_aliases[/Nintendo DS/MelonDS-Nintendo DS]
tests/test_drive.py::test_folder_platform_aliases[/Temas-]
tests/test_drive.py::test_folder_platform_aliases[/Switch Games-]
tests/test_drive.py::test_folder_platform_aliases[/Nintendo DS/PSP-]
tests/test_drive.py::test_folder_platform_aliases[C:\\ROMs\\Nintendo 3DS-Nintendo 3DS]
tests/test_drive.py::test_reclassification_preserves_existing_metadata
tests/test_drive.py::test_root_themes_are_not_roms
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - Spirit Tracks (USA) (Rev 1).nds-The Legend of Zelda: Spirit Tracks-Nintendo DS]
tests/test_drive_0133.py::test_no_intro_identity[Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip-Yu-Gi-Oh! - Ultimate Masters 2006-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Zelda (Game & Watch).zip-Zelda (Game & Watch)-]
tests/test_drive_0133.py::test_no_intro_identity[Mother 3 [!].gba-Mother 3-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - The Minish Cap (USA).gba-The Legend of Zelda: The Minish Cap-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Little Mermaid, The (USA).nes-The Little Mermaid-NES]
tests/test_drive_0133.py::test_no_intro_identity[Amazing Spider-Man, The (USA).gb-The Amazing Spider-Man-Game Boy]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - Oracle of Ages (USA, Australia).gbc-The Legend of Zelda: Oracle of Ages-Game Boy Color]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - A Link to the Past (USA).sfc-The Legend of Zelda: A Link to the Past-SNES]
tests/test_drive_0133.py::test_no_intro_identity[Incredible Hulk, The (Europe).md.zip-The Incredible Hulk-Mega Drive]
tests/test_drive_0133.py::test_drive_normalized_search_click_flow
tests/test_drive_0133.py::test_drive_no_results_is_explicit_and_link_survives
tests/test_drive_0133.py::test_articles_and_subtitle_separator
tests/test_drive_auth.py::test_token_exchange_failure_reports_stage_without_secrets
tests/test_drive_auth.py::test_vault_failure_is_distinct_from_oauth_failure
tests/test_drive_auth.py::test_success_initializes_drive_after_persisting_token
tests/test_drive_auth.py::test_initial_token_exchange_has_network_timeout
tests/test_drive_metadata_policy.py::test_drive_enrichment_uses_text_but_not_rawg_images
tests/test_drive_metadata_policy.py::test_manual_search_recovers_existing_rom_without_duplicate
tests/test_drive_search.py::test_rom_search_platform_and_literal_query
tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[False]
tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[True]
tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[sem-resultado]
tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[fonte-indisponivel]
tests/test_elevation_0137.py::test_uac_handoff_preserves_arguments_paths_and_original_identity
tests/test_elevation_0137.py::test_uac_cancel_and_other_account_never_retry_or_prepare_data
tests/test_elevation_0137.py::test_already_elevated_same_account_continues_without_new_prompt
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[handoff]
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[cancel]
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[different_account]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-0-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-1-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-2-desejos]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-0-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-1-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-2-desejos]
tests/test_enrichment.py::test_steam_details_validate_appid_and_parse_fields
tests/test_enrichment.py::test_fill_missing_preserves_personal_values_and_tracks_images
tests/test_enrichment.py::test_unknown_game_never_searches_by_name
tests/test_enrichment.py::test_download_failure_keeps_metadata_and_game
tests/test_enrichment.py::test_concurrent_edit_during_download_is_preserved
tests/test_enrichment.py::test_wrong_identity_response_never_applied
tests/test_enrichment.py::test_rawg_confirmed_rom_uses_its_own_identity
tests/test_enrichment.py::test_form_saves_without_network_or_nested_loading_dialog
tests/test_enrichment.py::test_unknown_game_requires_selection
tests/test_enrichment.py::test_batch_cancellation_keeps_existing_library
tests/test_enrichment.py::test_steam_header_is_fallback_after_library_hero
tests/test_enrichment.py::test_existing_automatic_header_upgrades_and_keeps_old_cache
tests/test_enrichment.py::test_missing_hero_does_not_replace_existing_header_with_another_header
tests/test_enrichment.py::test_modified_header_content_is_preserved_as_user_choice
tests/test_enrichment.py::test_manual_confirmation_during_header_download_wins
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-False]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-True]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-False]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-True]
tests/test_folder_platforms.py::test_persistent_rules_inherit_and_specific_override
tests/test_folder_platforms.py::test_rule_applies_to_new_files_and_renamed_folder_id
tests/test_folder_platforms.py::test_bad_rules_leave_saved_data_unchanged
tests/test_folder_platforms.py::test_new_console_aliases[PS1-PlayStation]
tests/test_folder_platforms.py::test_new_console_aliases[PSX-PlayStation]
tests/test_folder_platforms.py::test_new_console_aliases[PS2-PlayStation 2]
tests/test_folder_platforms.py::test_new_console_aliases[Nintendo GameCube-GameCube]
tests/test_folder_platforms.py::test_new_console_aliases[NGC-GameCube]
tests/test_folder_platforms.py::test_new_console_aliases[Nintendo Wii-Wii]
tests/test_folder_platforms.py::test_create_confirmed_game_and_link_version
tests/test_folder_platforms.py::test_folder_dialog_saves_rule_and_gallery_has_cover_icons
tests/test_game_import.py::test_catalog_title_is_separate_from_original_rom_name
tests/test_game_import.py::test_second_version_reuses_confirmed_identity
tests/test_game_import.py::test_wrong_existing_link_is_not_silently_replaced
tests/test_game_import.py::test_failed_import_does_not_create_orphan
tests/test_game_import.py::test_add_form_drive_search_and_metadata_prefill
tests/test_game_import.py::test_fit_preserves_entire_vertical_art
tests/test_game_import.py::test_artwork_progress_finishes_and_closes
tests/test_game_import.py::test_catalog_selection_closes_with_confirmed_result
tests/test_game_saves.py::test_game_backup_worker_history_restore_and_profile_versions
tests/test_game_saves.py::test_missing_profile_or_destination_is_explicit
tests/test_game_saves.py::test_changing_save_does_not_publish_backup
tests/test_ggdeals_api.py::test_api_parser_current_and_history_are_distinct_not_a_discount
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload0]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload1]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload2]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload3]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload4]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload5]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload6]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload7]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload8]
tests/test_ggdeals_api.py::test_api_missing_one_current_field_does_not_invent_zero
tests/test_ggdeals_api.py::test_transport_parameters_and_failures_never_reveal_in_memory_secret
tests/test_ggdeals_api.py::test_api_reflected_secret_response_is_rejected_without_storage
tests/test_ggdeals_api.py::test_missing_steam_id_does_not_call_provider
tests/test_ggdeals_api.py::test_factory_selects_api_or_configured_public_fallback
tests/test_ggdeals_api.py::test_api_failure_keeps_previous_price_and_null_is_not_zero
tests/test_ggdeals_connection.py::test_connection_key_is_masked_transient_and_only_saved_to_vault
tests/test_ggdeals_connection.py::test_vault_errors_never_echo_input_or_exception
tests/test_ggdeals_connection.py::test_configuration_change_rechecks_prices_without_discarding_cache
tests/test_grid_performance_0137.py::test_collection_totals_use_bounded_queries_without_duplicate_snapshots
tests/test_grid_performance_0137.py::test_cache_is_bounded_and_invalidates_changed_files
tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0]
tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1]
tests/test_home_0129.py::test_home_only_in_progress_and_latest_session_hero
tests/test_home_0129.py::test_home_without_started_games_has_no_invented_hero
tests/test_home_0129.py::test_home_hero_button_remains_inside_banner_after_resizing
tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles0]
tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles1]
tests/test_home_data_0137.py::test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed
tests/test_home_data_0137.py::test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[None]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[inv\xe1lida]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:00]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T11:00:00+00:00]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:01+00:00]
tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample0]
tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample1]
tests/test_home_layout_0137.py::test_home_actions_are_distinct_and_week_opens_correct_period[sample0]
tests/test_home_layout_0137.py::test_home_actions_are_distinct_and_week_opens_correct_period[sample1]
tests/test_home_layout_0137.py::test_home_columns_align_top_and_art_is_contained[sample0]
tests/test_home_layout_0137.py::test_home_columns_align_top_and_art_is_contained[sample1]
tests/test_home_layout_0137.py::test_memory_carousel_bounds_keyboard_and_no_data_changes[sample0]
tests/test_home_layout_0137.py::test_memory_carousel_bounds_keyboard_and_no_data_changes[sample1]
tests/test_home_layout_0137.py::test_status_change_does_not_create_recent_card[sample0]
tests/test_home_layout_0137.py::test_status_change_does_not_create_recent_card[sample1]
tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample0]
tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample1]
tests/test_home_layout_0137.py::test_offers_show_only_same_offer_original_discount_and_current[sample0]
tests/test_home_layout_0137.py::test_offers_show_only_same_offer_original_discount_and_current[sample1]
tests/test_home_layout_0137.py::test_offer_banner_uses_entire_banner_instead_of_cover[sample0]
tests/test_home_layout_0137.py::test_offer_banner_uses_entire_banner_instead_of_cover[sample1]
tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0]
tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1]
tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample0]
tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample1]
tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0]
tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1]
tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample0]
tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample1]
tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample0]
tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample1]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[10]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[16]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[18]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[20]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[22]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[24]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[32]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-0]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-1]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-2]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-3]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-4]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-5]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-6]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-0]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-1]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-2]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-3]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-4]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-5]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-6]
tests/test_isolated_operations.py::test_real_worker_entry_does_not_open_gui_or_require_credentials
tests/test_isolated_operations.py::test_abrupt_child_exit_is_reported_without_terminating_parent
tests/test_isolated_operations.py::test_real_transfer_child_adds_library_preserves_original_and_local_file
tests/test_isolated_operations.py::test_drive_ui_survives_art_child_failure_after_real_transfer
tests/test_isolated_operations.py::test_platform_and_ambiguous_matches_do_not_silently_choose_wrong_edition
tests/test_isolated_operations.py::test_automatic_title_lookup_combines_same_title_sources_without_manual_picker
tests/test_isolated_operations.py::test_conflicting_combined_identities_roll_back_import
tests/test_isolated_operations.py::test_binding_automatic_result_keeps_personal_fields
tests/test_isolated_operations.py::test_new_game_form_keeps_optional_configuration_collapsed
tests/test_isolated_operations.py::test_transfer_child_exit_preserves_partial_without_publishing_corrupt_rom
tests/test_isolated_operations.py::test_main_window_close_waits_for_child_operation
tests/test_isolated_operations.py::test_automatic_name_does_not_confuse_sequels
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-N\xe3o iniciado]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-Backlog]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-N\xe3o iniciado]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-Backlog]
tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample0]
tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample1]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Zelda: A Link to the Past-SNES-.sfc]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Metroid Fusion-GBA-.gba]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Zelda: A Link to the Past-SNES-.sfc]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Metroid Fusion-GBA-.gba]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Zelda: A Link to the Past]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Metroid Fusion]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Zelda: A Link to the Past]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Metroid Fusion]
tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample0]
tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample1]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1280]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1920]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1280]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1920]
tests/test_layout_0134.py::test_settings_paths_labels_grid_and_update_action[sample0]
tests/test_layout_0134.py::test_settings_paths_labels_grid_and_update_action[sample1]
tests/test_layout_0134.py::test_home_empty_text_and_files_action[sample0]
tests/test_layout_0134.py::test_home_empty_text_and_files_action[sample1]
tests/test_layout_regressions_025.py::test_home_search_opens_library_results
tests/test_layout_regressions_025.py::test_empty_state_shows_instructional_description
tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
tests/test_layout_regressions_025.py::test_add_game_uses_library_from_home_and_library
tests/test_layout_regressions_025.py::test_large_steam_import_keeps_dialog_bounded_without_per_game_log
tests/test_layout_regressions_025.py::test_wishlist_fetches_missing_logo_once_and_updates_card
tests/test_library.py::test_crud_persistence_filters_and_recovery
tests/test_library.py::test_validation_sql_and_literal_search
tests/test_library.py::test_diary_settings_and_stats
tests/test_library.py::test_database_backup_and_foreign_keys
tests/test_library.py::test_filter_individual_genre_from_imported_metadata
tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample0]
tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample1]
tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample0]
tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample1]
tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[Pok\xe9mon FireRed and LeafGreen+]
tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[The Legend of Zelda: Ocarina of Time 3D]
tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom0]
tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom1]
tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom0]
tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom1]
tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom0]
tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom1]
tests/test_local_rom_0137.py::test_distinct_ocarina_platform_and_edition_are_not_equivalent
tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom0]
tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom1]
tests/test_local_rom_0137.py::test_play_missing_local_file_offers_relocation_without_session[local_rom0]
tests/test_local_rom_0137.py::test_play_missing_local_file_offers_relocation_without_session[local_rom1]
tests/test_local_rom_0137.py::test_local_confirm_button_persists_only_after_click[local_rom0]
tests/test_local_rom_0137.py::test_local_confirm_button_persists_only_after_click[local_rom1]
tests/test_localized_metadata.py::test_portuguese_description_requires_exact_game_platform_and_not_ambiguous
tests/test_localized_metadata.py::test_localization_rejects_disambiguation_and_missing_translation
tests/test_localized_metadata.py::test_steam_requests_brazilian_and_parses_brazilian_release_date
tests/test_localized_metadata.py::test_rom_with_art_identity_gets_portuguese_description_and_attribution
tests/test_localized_metadata.py::test_localization_preserves_manual_text_and_replaces_exact_legacy_source
tests/test_localized_metadata.py::test_release_date_roundtrip_and_information_always_visible
tests/test_localized_metadata.py::test_legacy_steam_english_is_replaced_only_on_exact_source_match
tests/test_localized_metadata.py::test_enrichment_fetches_rom_description_even_when_all_art_exists
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Metroid Fusion]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Metroid Fusion]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Metroid Fusion]
tests/test_migrations.py::test_upgrade_v1_keeps_user_data
tests/test_migrations.py::test_newer_schema_refused_without_mutation
tests/test_migrations.py::test_failed_migration_rolls_back_all_ddl
tests/test_migrations.py::test_upgrade_v2_preserves_covers_and_ids
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Zelda: A Link to the Past]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Metroid Fusion]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Zelda: A Link to the Past]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Metroid Fusion]
tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4660]
tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4886718345]
tests/test_native_startup_0138.py::test_invalid_native_message_does_not_create_a_window
tests/test_native_startup_0138.py::test_real_platform_window_opens_and_closes_in_isolated_process[Portal 2]
tests/test_native_startup_0138.py::test_real_platform_window_opens_and_closes_in_isolated_process[Hades]
tests/test_network.py::test_safe_nested_diagnosis[error0-proxy]
tests/test_network.py::test_safe_nested_diagnosis[error1-tls]
tests/test_network.py::test_safe_nested_diagnosis[error2-dns]
tests/test_network.py::test_safe_nested_diagnosis[error3-timeout]
tests/test_network.py::test_safe_nested_diagnosis[error4-reset]
tests/test_network.py::test_safe_nested_diagnosis[error5-refused]
tests/test_network.py::test_safe_nested_diagnosis[error6-connection]
tests/test_network.py::test_safe_nested_diagnosis[error7-unknown]
tests/test_network.py::test_chain_handles_cycles
tests/test_network.py::test_probe_does_not_send_oauth_data
tests/test_network.py::test_probe_reports_tls_without_error_contents
tests/test_network.py::test_safe_details_exclude_exception_messages
tests/test_network.py::test_remote_disconnect_is_recognized
tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample0]
tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample1]
tests/test_period_chart_0137.py::test_hourly_day_uses_real_local_session_boundaries
tests/test_period_chart_0137.py::test_day_hours_respect_dst_and_do_not_change_instants
tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0]
tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1]
tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample0]
tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample1]
tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0]
tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1]
tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved
tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample0]
tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample1]
tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample0]
tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample1]
tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample0]
tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample1]
tests/test_price_display_official.py::test_official_history_is_never_struck_out_or_used_as_discount
tests/test_price_display_official.py::test_price_order_places_missing_prices_last_and_respects_name
tests/test_price_display_official.py::test_wishlist_and_detail_have_active_attribution_and_no_steam_queue
tests/test_price_display_official.py::test_foreign_currency_cache_never_renders_as_reais
tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Zelda Phantom Hourglass-Nintendo DS]
tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Metroid Dread-Nintendo Switch]
tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Portal 2]
tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Hades II]
tests/test_price_integrity_0136.py::test_discount_sort_and_keyshop_policy
tests/test_price_integrity_0136.py::test_comparison_has_reason_instead_of_bare_unavailable
tests/test_price_integrity_0136.py::test_discount_visible_only_for_offer_and_rounds_half_up
tests/test_price_integrity_0136.py::test_discount_follows_active_theme
tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Portal 2]
tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Hades]
tests/test_price_integrity_0136.py::test_price_store_and_original_do_not_mix_tied_offers
tests/test_prices_0129.py::test_original_price_and_discount_come_from_same_offer
tests/test_prices_0129.py::test_official_api_without_saved_key_never_calls_transport
tests/test_prices_0129.py::test_wishlist_name_price_sort_and_scroll_survive_refresh
tests/test_prices_0135.py::test_official_default[Zelda: A Link to the Past]
tests/test_prices_0135.py::test_official_default[Metroid Fusion]
tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Zelda: A Link to the Past]
tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Metroid Fusion]
tests/test_profile.py::test_nickname_and_photo_are_local_persistent_and_preserve_original
tests/test_profile.py::test_profile_cancel_and_remove_photo_keep_saved_name
tests/test_quick_add.py::test_unified_catalog_combines_details_without_provider_selection
tests/test_quick_add.py::test_console_search_does_not_match_pc_edition
tests/test_quick_add.py::test_search_failure_keeps_other_sources_usable
tests/test_quick_add.py::test_search_prefills_form_and_can_save_without_advanced_step
tests/test_quick_add.py::test_stale_lookup_cannot_overwrite_new_query
tests/test_quick_add.py::test_drive_choice_preserves_original_and_searches_platform
tests/test_quick_add.py::test_same_title_across_sources_is_one_result_not_a_provider_choice
tests/test_quick_add.py::test_standalone_dialog_finishes_query_before_destruction
tests/test_quick_add.py::test_source_change_rejects_inflight_catalog_and_steam_uses_import
tests/test_quick_add.py::test_drive_source_displays_versions_and_preserves_original
tests/test_quick_add.py::test_nested_dialog_keeps_query_receiver_alive_until_job_finishes
tests/test_reference_layout_0128.py::test_sidebar_keeps_identity_navigation_footer_and_profile_chevron
tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections
tests/test_reference_layout_0128.py::test_detail_play_and_secondary_setup_obey_execution_configuration
tests/test_reference_layout_0128.py::test_connections_match_two_by_two_cards_help_and_green_configured_dot
tests/test_registration_0128.py::test_empty_tabs_search_and_empty_library_have_distinct_actions
tests/test_registration_0128.py::test_quick_add_requires_selection_and_has_exclusive_search_state
tests/test_registration_0128.py::test_wish_reusing_owned_identity_does_not_remove_game
tests/test_registration_0128.py::test_new_wish_has_visible_confirmation
tests/test_registration_0128.py::test_selected_preview_does_not_overlap_other_result_link
tests/test_registration_0128.py::test_missing_cover_draws_full_title_instead_of_two_letters
tests/test_registration_0128.py::test_activity_summary_uses_singular_day_and_brazilian_date
tests/test_revision_0128.py::test_wishlist_one_and_five_cards_keep_same_fixed_square_art_area
tests/test_revision_0128.py::test_library_has_responsive_vertical_columns_at_minimum_and_full_hd
tests/test_revision_0128.py::test_count_helper_handles_zero_singular_plural_and_irregular
tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[]
tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[Nintendo 64]
tests/test_rom_edition_0137.py::test_drive_sheet_shows_divergence_without_starting_job
tests/test_rom_link_0134.py::test_exact_rom_ranking_and_unique_replacement[rom0]
tests/test_rom_link_0134.py::test_exact_rom_ranking_and_unique_replacement[rom1]
tests/test_rom_link_0134.py::test_rom_pipeline_download_text_and_art[rom0]
tests/test_rom_link_0134.py::test_rom_pipeline_download_text_and_art[rom1]
tests/test_rom_link_0134.py::test_missing_catalog_keeps_link_and_cause[rom0]
tests/test_rom_link_0134.py::test_missing_catalog_keeps_link_and_cause[rom1]
tests/test_rom_link_0134.py::test_files_dialog_click_runs_and_finishes[rom0]
tests/test_rom_link_0134.py::test_files_dialog_click_runs_and_finishes[rom1]
tests/test_rom_link_0134.py::test_failed_link_exposes_cause_and_retry[rom0]
tests/test_rom_link_0134.py::test_failed_link_exposes_cause_and_retry[rom1]
tests/test_rom_link_0134.py::test_existing_add_and_manager_also_replace_unique_link[rom0]
tests/test_rom_link_0134.py::test_existing_add_and_manager_also_replace_unique_link[rom1]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip-Yu-Gi-Oh! - Ultimate Masters 2006-Game Boy Advance]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Pokemon - Platinum (USA) (Rev 1).nds-Pokemon: Platinum-Nintendo DS]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Metroid_Fusion [!].gba.zip-Metroid Fusion-Game Boy Advance]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Zelda (Europe) (En,Fr,De).sfc-Zelda-SNES]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[A Game (The Return).gba-A Game (The Return)-Game Boy Advance]
tests/test_rom_titles_0129.py::test_drive_records_platform_without_changing_original_name
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[success]
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[failure]
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[drive]
tests/test_save_lifecycle.py::test_save_smoke_refuses_existing_database
tests/test_save_profiles.py::test_profiles_persist_and_reject_states
tests/test_saves.py::test_backup_restore_preserves_previous_and_ignores_states
tests/test_saves.py::test_rejects_traversal_and_broad_patterns
tests/test_saves.py::test_legacy_backup_manifest_remains_readable
tests/test_search_save_0129.py::test_accept_during_selected_details_waits_and_saves_full_record
tests/test_service_branding_0135.py::test_service_brands_do_not_use_lucide[Zelda: A Link to the Past]
tests/test_service_branding_0135.py::test_service_brands_do_not_use_lucide[Metroid Fusion]
tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past]
tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Metroid Fusion]
tests/test_service_optical_0136.py::test_steam_white_mark_optically_centered_and_asset_unchanged
tests/test_services.py::test_metadata_requires_selection_and_parses_without_network
tests/test_services.py::test_emulator_arguments_no_shell
tests/test_services.py::test_sessions_recover_without_inventing_duration
tests/test_services.py::test_spawn_and_poll_actual_process
tests/test_services.py::test_emulator_exit_does_not_infer_rom_session_end
tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Zelda: A Link to the Past-SNES-.sfc]
tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Metroid Fusion-GBA-.gba]
tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample0]
tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample1]
tests/test_settings_0135.py::test_connections_standard_buttons[sample0]
tests/test_settings_0135.py::test_connections_standard_buttons[sample1]
tests/test_settings_0135.py::test_backup_action_emphasis[sample0]
tests/test_settings_0135.py::test_backup_action_emphasis[sample1]
tests/test_settings_navigation_0139.py::test_profile_edit_keeps_id_and_remove_preserves_files_and_used_profile[sample0]
tests/test_settings_navigation_0139.py::test_profile_edit_keeps_id_and_remove_preserves_files_and_used_profile[sample1]
tests/test_settings_navigation_0139.py::test_execution_profile_filters_preserves_on_cancel_and_survives_reopen[sample0]
tests/test_settings_navigation_0139.py::test_execution_profile_filters_preserves_on_cancel_and_survives_reopen[sample1]
tests/test_settings_navigation_0139.py::test_trash_restores_only_chosen_homonym_and_keeps_navigation[sample0]
tests/test_settings_navigation_0139.py::test_trash_restores_only_chosen_homonym_and_keeps_navigation[sample1]
tests/test_settings_navigation_0139.py::test_trash_unknown_date_does_not_invent_timestamp[sample0]
tests/test_settings_navigation_0139.py::test_trash_unknown_date_does_not_invent_timestamp[sample1]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Zelda: A Link to the Past]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Metroid Fusion]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Zelda: A Link to the Past]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Metroid Fusion]
tests/test_smooth_scroll.py::test_wheel_with_500_games_uses_pixel_animation_and_remains_responsive
tests/test_statistics_0136.py::test_calendar_bounds_clamp_and_monday
tests/test_statistics_0136.py::test_period_clips_local_midnight_without_altering_data[Portal 2]
tests/test_statistics_0136.py::test_period_clips_local_midnight_without_altering_data[Metroid Fusion]
tests/test_statistics_0136.py::test_dst_and_empty_do_not_distribute_steam
tests/test_statistics_0136.py::test_equivalent_metrics_and_period_selector[sample0]
tests/test_statistics_0136.py::test_equivalent_metrics_and_period_selector[sample1]
tests/test_statistics_0136.py::test_fall_dst_is_25_hours_and_year_boundary
tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample0]
tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample1]
tests/test_statistics_visible_0136.py::test_genres_are_removed_from_statistics_and_completions_remain[sample0]
tests/test_statistics_visible_0136.py::test_genres_are_removed_from_statistics_and_completions_remain[sample1]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Zelda: A Link to the Past]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Metroid Fusion]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Zelda: A Link to the Past]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Metroid Fusion]
tests/test_status_pill_0136.py::test_status_is_one_themed_control_without_annotation[sample0]
tests/test_status_pill_0136.py::test_status_is_one_themed_control_without_annotation[sample1]
tests/test_status_pill_0136.py::test_click_on_status_dot_opens_menu_and_keyboard_saves_choice[sample0]
tests/test_status_pill_0136.py::test_click_on_status_dot_opens_menu_and_keyboard_saves_choice[sample1]
tests/test_steam.py::test_owned_games_contract_and_hidden_hours
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response0]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response1]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response2]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response3]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response4]
tests/test_steam.py::test_input_validation_before_network_and_safe_provider_error
tests/test_steam.py::test_achievements_keep_locked_and_unknown_unlock_date_distinct
tests/test_steam.py::test_import_is_repeatable_and_preserves_local_data_and_separate_accounts
tests/test_steam.py::test_same_name_does_not_merge_without_explicit_choice
tests/test_steam.py::test_conflicting_or_trashed_identity_rolls_back_entire_batch
tests/test_steam.py::test_achievement_snapshot_is_idempotent_and_preserves_personal_records
tests/test_steam.py::test_v3_upgrade_keeps_library_and_creates_recoverable_backup
tests/test_steam.py::test_dialog_async_query_selection_import_achievements_and_account_change
tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[620-Portal 2]
tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[400-Portal]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Zelda: A Link to the Past]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Metroid Fusion]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Zelda: A Link to the Past]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Metroid Fusion]
tests/test_themes.py::test_palette_normal_text_contrast[blue]
tests/test_themes.py::test_palette_normal_text_contrast[green]
tests/test_themes.py::test_palette_normal_text_contrast[yellow]
tests/test_themes.py::test_palette_normal_text_contrast[red]
tests/test_themes.py::test_palette_normal_text_contrast[black]
tests/test_themes.py::test_palette_normal_text_contrast[purple]
tests/test_themes.py::test_palette_normal_text_contrast[pink]
tests/test_themes.py::test_palette_normal_text_contrast[orange]
tests/test_themes.py::test_palette_normal_text_contrast[cyan]
tests/test_themes.py::test_theme_selection_is_immediate_and_survives_reopening
tests/test_themes.py::test_unknown_theme_falls_back_to_green
tests/test_themes.py::test_unknown_saved_preference_falls_back_without_losing_library
tests/test_themes.py::test_exactly_nine_themes_and_swatches
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Zelda: A Link to the Past]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Metroid Fusion]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Zelda: A Link to the Past]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Metroid Fusion]
tests/test_time_prices_0134.py::test_app_and_steam_times_are_combined[sample0]
tests/test_time_prices_0134.py::test_app_and_steam_times_are_combined[sample1]
tests/test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price[sample0]
tests/test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price[sample1]
tests/test_trash_import.py::test_restore_retains_history_and_art
tests/test_trash_import.py::test_new_entry_preserves_trash_and_does_not_steal_identity_on_restore
tests/test_trash_import.py::test_cancel_and_failed_new_leave_trash_unchanged
tests/test_trash_import.py::test_title_matching_is_exact_and_platform_specific
tests/test_trash_import.py::test_explicit_new_does_not_repeat_late_catalog_prompt
tests/test_ui.py::test_navigate_and_game_detail_with_real_database
tests/test_ui.py::test_game_form_validation_and_round_trip
tests/test_ui.py::test_game_form_file_buttons_keep_their_field
tests/test_ui.py::test_parentless_game_form_process_exits_cleanly
tests/test_ui.py::test_image_cache_validates_and_deduplicates
tests/test_ui.py::test_session_end_triggers_background_game_backup
tests/test_ui.py::test_updates_dialog_starts_without_network_or_credentials
tests/test_ui.py::test_updates_require_saving_typed_credential_before_network
tests/test_ui_polish.py::test_banner_is_bounded_at_desktop_width
tests/test_ui_polish.py::test_compact_loading_and_centered_name
tests/test_ui_polish.py::test_statistics_chart_uses_library_totals
tests/test_ui_polish.py::test_library_caption_starts_at_visible_cover_edge
tests/test_ui_redesign.py::test_game_detail_uses_banner_logo_tabs_and_preserves_files
tests/test_ui_redesign.py::test_settings_are_compact_and_restore_selected_section
tests/test_ui_redesign.py::test_library_shortcuts_size_and_theme_update
tests/test_ui_redesign.py::test_add_sources_do_not_start_network_or_nested_loading
tests/test_ui_redesign.py::test_home_tiles_are_full_height_and_open_real_game
tests/test_ui_redesign.py::test_detail_refresh_preserves_diary_draft_and_save_clears_it
tests/test_ui_redesign.py::test_cover_grid_uses_width_at_desktop_and_compact_window
tests/test_ui_redesign.py::test_home_places_activity_beside_continuity
tests/test_ui_review_lifecycle_0136.py::test_review_releases_global_shortcut_between_windows
tests/test_updates.py::test_versions_skip_old_drafts_previews_and_unverified_assets
tests/test_updates.py::test_extract_and_swap_preserves_previous
tests/test_updates.py::test_unsafe_archives_rejected[../outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/../outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[C:/outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/file.txt:ads]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/CON.txt]
tests/test_updates.py::test_copy_failure_rolls_back
tests/test_updates.py::test_private_download_strips_token_on_cdn_and_verifies
tests/test_updates.py::test_corrupt_download_never_extracts
tests/test_updates.py::test_check_decodes_gzip_response_before_json
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[ProxyError-proxy]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[SSLError-certificado]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[Timeout-demorou]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[ConnectionError-firewall]
tests/test_updates.py::test_invalid_json_reports_response_not_network
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[blue]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[green]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[yellow]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[red]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[black]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[purple]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[pink]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[orange]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[cyan]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[home-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[home-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[library-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[library-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[wish-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[wish-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[detail-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[detail-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[sparse-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[sparse-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-0-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-0-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-1-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-1-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-2-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-2-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-3-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-3-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[add-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[add-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[drive-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[drive-pink]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[0]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[1]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[2]
tests/test_visual_0132.py::test_library_and_wishes_reuse_art_component_and_dimensions
tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged
tests/test_visual_0132.py::test_sparse_detail_and_gallery_explain_missing_content
tests/test_visual_0132.py::test_settings_without_accounts_still_has_states_and_actions
tests/test_visual_0132.py::test_empty_drive_list_has_explanation_and_existing_refresh_action
tests/test_visual_0132.py::test_empty_search_dialog_keeps_instruction_and_disabled_save
tests/test_visual_0132.py::test_reapplying_same_theme_does_not_repolish_all_widgets
tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample0]
tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample1]
tests/test_visual_audit_0136.py::test_wide_wishes_and_existing_identity_are_preserved[sample0]
tests/test_visual_audit_0136.py::test_wide_wishes_and_existing_identity_are_preserved[sample1]
tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past]
tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Metroid Fusion]
tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Zelda: A Link to the Past]
tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Metroid Fusion]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Zelda: A Link to the Past]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Metroid Fusion]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Zelda: A Link to the Past]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Metroid Fusion]
tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Zelda: A Link to the Past]
tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Metroid Fusion]
tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Zelda: A Link to the Past]
tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Metroid Fusion]
tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample0]
tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample1]
tests/test_window_controls_0137.py::test_native_hit_regions_preserve_resize_and_caption_controls
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-False]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-True]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-False]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-True]
tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample0]
tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample1]
tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample0]
tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample1]
tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample0]
tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample1]
tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample0]
tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample1]
tests/test_wish_time_0136.py::test_nullable_legacy_ownership_flag_agrees_with_collection
tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample0]
tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample1]
tests/test_wishlist_prices.py::test_prices_use_visible_brl_not_internal_dollar_values_and_keep_links
tests/test_wishlist_prices.py::test_prices_cache_failure_keeps_last_good_price
tests/test_wishlist_prices.py::test_wishlist_has_no_owned_status_and_is_excluded_from_owned_statistics
tests/test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
tests/test_wishlist_prices.py::test_wishlist_logos_titles_and_prices_share_fixed_alignment
tests/test_wishlist_prices.py::test_artwork_cache_rejects_gif

750 tests collected in 0.67s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## verification

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "/workspace/work/evidence-0139/verify_0139.py"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853470.4841447,
  "exit_code": 0,
  "elapsed": 0.33684635162353516
}
```

Comando:

```sh
/workspace/work/venv/bin/python /workspace/work/evidence-0139/verify_0139.py
```

stdout integral — 1087 bytes; SHA-256 f4293e867f147aa579de8771d0a0f0e7bfbcec683c6f2e74e0a0a20de8ce4c13:

````text
{
  "version": "0.1.39",
  "schema": 4,
  "protected_bytes_equal": [
    "tests/test_save_lifecycle.py",
    "checkpoint/worker.py",
    "checkpoint/enrichment.py",
    "checkpoint/game_import.py",
    "checkpoint/completion_queue.py",
    "checkpoint/quick_add.py",
    "tests/test_visual_0132.py",
    "checkpoint/database.py",
    "checkpoint/elevation.py",
    "checkpoint/windows_frame.py"
  ],
  "ImageDialog_prefix_equal": true,
  "workflows_unchanged": true,
  "assets_unchanged": true,
  "eight_palettes_equal": true,
  "legacy_test_assertions_equal": [
    "tests/test_elevation_0137.py",
    "tests/test_launch_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_memories_0135.py",
    "tests/test_sessions_0135.py"
  ],
  "bootstrap_main_ast_equal": true,
  "captures": [
    {
      "folder": "revisao-final",
      "count": 27,
      "dpr": [
        1.0
      ]
    },
    {
      "folder": "dpi-150",
      "count": 20,
      "dpr": [
        1.5
      ]
    },
    {
      "folder": "dpi-200",
      "count": 20,
      "dpr": [
        2.0
      ]
    }
  ]
}
````

stderr integral — 582 bytes; SHA-256 41ce12277233aaa35ff9e3a5430ebc24f32b9095533f3b9b6843596122ce9676:

````text
fatal: path 'tests/test_detail_polish_0139.py' exists on disk, but not in '9dd9c93ce7baf0051bbc783323b401d4ba8c7059'
fatal: path 'tests/test_dialog_polish_0139.py' exists on disk, but not in '9dd9c93ce7baf0051bbc783323b401d4ba8c7059'
fatal: path 'tests/test_home_polish_0139.py' exists on disk, but not in '9dd9c93ce7baf0051bbc783323b401d4ba8c7059'
fatal: path 'tests/test_polish_0139.py' exists on disk, but not in '9dd9c93ce7baf0051bbc783323b401d4ba8c7059'
fatal: path 'tests/test_settings_navigation_0139.py' exists on disk, but not in '9dd9c93ce7baf0051bbc783323b401d4ba8c7059'
````

## full-failures-isolated

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_card_layout.py::test_grids_keep_their_proportions_and_size_control_keeps_font_and_items",
    "tests/test_complete_layout.py::test_memories_excludes_removed_games_and_filters_diary",
    "tests/test_home_0129.py::test_home_hero_button_remains_inside_banner_after_resizing",
    "tests/test_home_description_0136.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853491.4809885,
  "exit_code": 1,
  "elapsed": 1.18269944190979
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_card_layout.py::test_grids_keep_their_proportions_and_size_control_keeps_font_and_items tests/test_complete_layout.py::test_memories_excludes_removed_games_and_filters_diary tests/test_home_0129.py::test_home_hero_button_remains_inside_banner_after_resizing tests/test_home_description_0136.py -q -p no:cacheprovider
```

stdout integral — 7969 bytes; SHA-256 ce32149571123b31511f110786a73219a64b363c359a630d7699501d162e4731:

````text
FFFF.                                                                    [100%]
=================================== FAILURES ===================================
___ test_grids_keep_their_proportions_and_size_control_keeps_font_and_items ____

library = <checkpoint.library.Library object at 0x7f94e2bc6870>
app = <PySide6.QtWidgets.QApplication(0xc3e93e0) at 0x7f94e2b848c0>

    def test_grids_keep_their_proportions_and_size_control_keeps_font_and_items(library,app):
        from checkpoint.collection_views import WishGrid
        for index in range(12):
            identity=library.save_game({'title':f'Fixture {index}'})
            if index>=6:
                with library.sql:library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(identity,))
        library.set_setting('artwork.auto',False);library.set_setting('prices.auto',False)
        window=MainWindow(library);window.show();window.navigate(2);font=app.font()
        for width in (1280,1920):
            window.resize(width,800)
            for percent in (70,100,150):
                item=window.gallery.item(0)
                window.set_cover_size(percent)
                assert window.gallery.item(0) is item and app.font()==font
                for _ in range(4):app.processEvents()
                wishes=window.pages[2].findChild(WishGrid,'wishlistGrid');wish_columns=wishes.columns
                from PySide6.QtWidgets import QPushButton
                link=wishes.cards[0].findChild(QPushButton,'quiet')
                assert link.width()>=link.fontMetrics().horizontalAdvance(link.text())
                window.navigate(1)
                for _ in range(4):app.processEvents()
                # E3 da 0.1.34: Desejos tem cards maiores, com arte 1:1;
                # quantidade de colunas não precisa coincidir com capas verticais.
                from checkpoint.collection_views import WishLogo
>               assert wishes.columns==wish_columns and wishes.cards[0].width()>=280
E               assert (4 == 4 and 245 >= 280)
E                +  where 4 = <checkpoint.collection_views.WishGrid(0xce5ae40, name="wishlistGrid") at 0x7f94e2685500>.columns
E                +  and   245 = <built-in method width of WishCard object at 0x7f94e27c8240>()
E                +    where <built-in method width of WishCard object at 0x7f94e27c8240> = <checkpoint.collection_views.WishCard(0xce5be30, name="panel") at 0x7f94e27c8240>.width

tests/test_card_layout.py:54: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
____________ test_memories_excludes_removed_games_and_filters_diary ____________

library = <checkpoint.library.Library object at 0x7f94e2bc6690>
app = <PySide6.QtWidgets.QApplication(0xc3e93e0) at 0x7f94e2b848c0>
tmp_path = PosixPath('/tmp/pytest-of-agent/pytest-49/test_memories_excludes_removed0')

    def test_memories_excludes_removed_games_and_filters_diary(library,app,tmp_path):
        visible=library.save_game({'title':'Visible'});removed=library.save_game({'title':'Removed'})
        library.add_diary(visible,'Visible memory');library.add_diary(removed,'Private removed memory');library.delete(removed)
        window=MainWindow(library);window.navigate(3);window.show();app.processEvents()
        from PySide6.QtWidgets import QTabWidget
        tabs=window.pages[3].findChild(QTabWidget,'memoryTabs')
        assert tabs.count()==3
        labels=[label.text() for label in tabs.currentWidget().findChildren(QLabel)]
>       assert 'Visible memory' in labels and 'Private removed memory' not in labels
E       AssertionError: assert ('Visible memory' in ['', 'Diário', 'agora'])

tests/test_complete_layout.py:33: AssertionError
__________ test_home_hero_button_remains_inside_banner_after_resizing __________

library = <checkpoint.library.Library object at 0x7f94e272ec60>
app = <PySide6.QtWidgets.QApplication(0xc3e93e0) at 0x7f94e2b848c0>

    def test_home_hero_button_remains_inside_banner_after_resizing(library,app):
        from PySide6.QtWidgets import QPushButton
        library.save_game({'title':'Jogo atual','status':'Jogando','description':'Descrição curta. '*50})
        from datetime import datetime,timezone
        with library.sql:
            library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(1,?,'interrupted',123)",(datetime.now(timezone.utc).isoformat(),))
        window=MainWindow(library);window.show()
        for width,height in ((1280,800),(1920,1080),(1280,800)):
            window.resize(width,height)
            for _ in range(5):app.processEvents()
            card=window.pages[0].findChild(RecentGameCard);art=card.findChild(RecentArtwork)
            button=next(b for b in card.findChildren(QPushButton) if b.property('homeContinue'))
            assert card.rect().contains(button.geometry())
>           assert button.geometry().top()>art.geometry().bottom()
E           assert 61 > 192
E            +  where 61 = <built-in method top of PySide6.QtCore.QRect object at 0x7f94e28049c0>()
E            +    where <built-in method top of PySide6.QtCore.QRect object at 0x7f94e28049c0> = PySide6.QtCore.QRect(13, 61, 163, 40).top
E            +      where PySide6.QtCore.QRect(13, 61, 163, 40) = <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f94e11d0ac0>()
E            +        where <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f94e11d0ac0> = <PySide6.QtWidgets.QPushButton(0xd763c20, name="primary") at 0x7f94e11d0ac0>.geometry
E            +  and   192 = <built-in method bottom of PySide6.QtCore.QRect object at 0x7f94e27fe940>()
E            +    where <built-in method bottom of PySide6.QtCore.QRect object at 0x7f94e27fe940> = PySide6.QtCore.QRect(13, 13, 163, 180).bottom
E            +      where PySide6.QtCore.QRect(13, 13, 163, 180) = <built-in method geometry of RecentArtwork object at 0x7f94e11c93c0>()
E            +        where <built-in method geometry of RecentArtwork object at 0x7f94e11c93c0> = <checkpoint.home_components.RecentArtwork(0xd763c90, name="recentGameArtwork") at 0x7f94e11c93c0>.geometry

tests/test_home_0129.py:48: AssertionError
______ test_home_does_not_paint_description_but_detail_keeps_it[sample0] _______

ui = (<checkpoint.window.MainWindow(0xc3e8570) at 0x7f94e272b400>, 1)
app = <PySide6.QtWidgets.QApplication(0xc3e93e0) at 0x7f94e2b848c0>

    def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
        w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
        w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
        from datetime import datetime,timezone
        with w.library.sql:w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(i,datetime.now(timezone.utc).isoformat()))
        w.navigate(0);app.processEvents();hero=w.pages[0].findChild(RecentArtwork)
        assert hero and w.pages[0].findChild(RecentGameCard).findChildren(QPushButton)
        for _ in range(6):app.processEvents()
>       before=hero.grab().toImage();hero.game={**hero.game,'description':''};hero.update();app.processEvents()
               ^^^^^^^^^^^
E       RuntimeError: Internal C++ object (RecentArtwork) already deleted.

tests/test_home_description_0136.py:14: RuntimeError
=========================== short test summary info ============================
FAILED tests/test_card_layout.py::test_grids_keep_their_proportions_and_size_control_keeps_font_and_items
FAILED tests/test_complete_layout.py::test_memories_excludes_removed_games_and_filters_diary
FAILED tests/test_home_0129.py::test_home_hero_button_remains_inside_banner_after_resizing
FAILED tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample0]
4 failed, 1 passed in 0.85s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-regressions-fixed

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_card_layout.py",
    "tests/test_complete_layout.py",
    "tests/test_home_0129.py",
    "tests/test_home_description_0136.py",
    "tests/test_home_polish_0139.py",
    "tests/test_isolated_operations.py::test_main_window_close_waits_for_child_operation",
    "tests/test_ui_review_lifecycle_0136.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853744.4689562,
  "exit_code": 0,
  "elapsed": 19.5035982131958
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_card_layout.py tests/test_complete_layout.py tests/test_home_0129.py tests/test_home_description_0136.py tests/test_home_polish_0139.py tests/test_isolated_operations.py::test_main_window_close_waits_for_child_operation tests/test_ui_review_lifecycle_0136.py -q -p no:cacheprovider
```

stdout integral — 100 bytes; SHA-256 8e5ff156277586047032d2481c18b056af6ff61394b2407a4c194f090c29c635:

````text
..............................                                           [100%]
30 passed in 18.95s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-linux-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853835.8426194,
  "exit_code": 1,
  "elapsed": 579.5049192905426
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 7555 bytes; SHA-256 de8ab051f4e9e359d47b305557e5fc583d834b1e0b937fced667cf5b98222c0e:

````text
........................................................................ [  9%]
........................................................................ [ 19%]
........................................................................ [ 28%]
........................................................................ [ 38%]
...................................................................F.F.. [ 47%]
....F................................................................... [ 57%]
...............................................................F........ [ 67%]
........................................................................ [ 76%]
........................................................................ [ 86%]
........................................................................ [ 95%]
................................                                         [100%]
=================================== FAILURES ===================================
____________ test_wishes_fill_columns_with_square_art[sample0-1920] ____________

ui = (<checkpoint.window.MainWindow(0x17f0af30) at 0x7f42e01b0ac0>, 1)
app = <PySide6.QtWidgets.QApplication(0x96ce630) at 0x7f42f2fd4e00>
width = 1920

    @pytest.mark.parametrize('width',[1280,1920])
    def test_wishes_fill_columns_with_square_art(ui,app,width):
        from checkpoint.collection_views import WishGrid,WishLogo,WishCard
        w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
        w.resize(width,800);w.navigate(2)
        for _ in range(4):app.processEvents()
        grid=w.pages[2].findChild(WishGrid);card=grid.findChild(WishCard);art=card.findChild(WishLogo)
>       assert art.width()==art.height() and 280<=card.width()<=360
E       assert (226 == 226 and 280 <= 258)
E        +  where 226 = <built-in method width of WishLogo object at 0x7f42e03556c0>()
E        +    where <built-in method width of WishLogo object at 0x7f42e03556c0> = <checkpoint.collection_views.WishLogo(0x18c7a940, name="wishLogo") at 0x7f42e03556c0>.width
E        +  and   226 = <built-in method height of WishLogo object at 0x7f42e03556c0>()
E        +    where <built-in method height of WishLogo object at 0x7f42e03556c0> = <checkpoint.collection_views.WishLogo(0x18c7a940, name="wishLogo") at 0x7f42e03556c0>.height
E        +  and   258 = <built-in method width of WishCard object at 0x7f42e01f2e80>()
E        +    where <built-in method width of WishCard object at 0x7f42e01f2e80> = <checkpoint.collection_views.WishCard(0x188c2470, name="panel") at 0x7f42e01f2e80>.width

tests/test_layout_0134.py:32: AssertionError
____________ test_wishes_fill_columns_with_square_art[sample1-1920] ____________

ui = (<checkpoint.window.MainWindow(0x190a35e0) at 0x7f42e01aea40>, 1)
app = <PySide6.QtWidgets.QApplication(0x96ce630) at 0x7f42f2fd4e00>
width = 1920

    @pytest.mark.parametrize('width',[1280,1920])
    def test_wishes_fill_columns_with_square_art(ui,app,width):
        from checkpoint.collection_views import WishGrid,WishLogo,WishCard
        w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
        w.resize(width,800);w.navigate(2)
        for _ in range(4):app.processEvents()
        grid=w.pages[2].findChild(WishGrid);card=grid.findChild(WishCard);art=card.findChild(WishLogo)
>       assert art.width()==art.height() and 280<=card.width()<=360
E       assert (226 == 226 and 280 <= 258)
E        +  where 226 = <built-in method width of WishLogo object at 0x7f42e00bd3c0>()
E        +    where <built-in method width of WishLogo object at 0x7f42e00bd3c0> = <checkpoint.collection_views.WishLogo(0x18a747f0, name="wishLogo") at 0x7f42e00bd3c0>.width
E        +  and   226 = <built-in method height of WishLogo object at 0x7f42e00bd3c0>()
E        +    where <built-in method height of WishLogo object at 0x7f42e00bd3c0> = <checkpoint.collection_views.WishLogo(0x18a747f0, name="wishLogo") at 0x7f42e00bd3c0>.height
E        +  and   258 = <built-in method width of WishCard object at 0x7f42e00b4b00>()
E        +    where <built-in method width of WishCard object at 0x7f42e00b4b00> = <checkpoint.collection_views.WishCard(0x18937ab0, name="panel") at 0x7f42e00b4b00>.width

tests/test_layout_0134.py:32: AssertionError
___________________ test_sidebar_and_page_bounds_at_full_hd ____________________

library = <checkpoint.library.Library object at 0x7f42e05b2ed0>
app = <PySide6.QtWidgets.QApplication(0x96ce630) at 0x7f42f2fd4e00>

    def test_sidebar_and_page_bounds_at_full_hd(library,app):
        library.save_game({'title':'Layout'})
        window=MainWindow(library);window.resize(1920,1080);window.show()
        for page in range(6):
            window.navigate(page);app.processEvents()
            assert window.add_button.isVisible()==(page in (0,1))
            sidebar=window.centralWidget().findChild(__import__('PySide6.QtWidgets',fromlist=['QWidget']).QWidget,'sidebar')
            assert sidebar.x()==0
>           assert window.header_widget.width()<=1392
E           assert 1674 <= 1392
E            +  where 1674 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f42e01c6dc0>()
E            +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7f42e01c6dc0> = <PySide6.QtWidgets.QWidget(0x19b5c6e0) at 0x7f42e01c6dc0>.width
E            +      where <PySide6.QtWidgets.QWidget(0x19b5c6e0) at 0x7f42e01c6dc0> = <checkpoint.window.MainWindow(0x17bd9160) at 0x7f42e02008c0>.header_widget

tests/test_layout_regressions_025.py:34: AssertionError
____________ test_home_has_reference_hero_cta_and_personal_sections ____________

library = <checkpoint.library.Library object at 0x7f42f3127140>
app = <PySide6.QtWidgets.QApplication(0x96ce630) at 0x7f42f2fd4e00>

    def test_home_has_reference_hero_cta_and_personal_sections(library,app):
        identity=library.save_game({'title':'Meu jogo','status':'Jogando'})
        from datetime import datetime,timezone
        with library.sql:library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(identity,datetime.now(timezone.utc).isoformat()))
        window=MainWindow(library);window.show();app.processEvents()
        from checkpoint.home_components import RecentArtwork
        assert len(window.pages[0].findChildren(RecentArtwork))==1
        cta=next(button for button in window.pages[0].findChildren(QPushButton) if button.text()=='Continuar jogando')
        labels=[label.text() for label in window.pages[0].findChildren(QLabel)]
>       assert 'Últimos jogos abertos' in labels and 'Resumo da semana' in labels and 'Memórias recentes' in labels
E       AssertionError: assert ('Últimos jogos abertos' in ['Últimas sessões', 'Jogando', 'Última vez: hoje, 15:33', 'Tempo total: 0h00min', 'Resumo da semana', '', ...])

tests/test_reference_layout_0128.py:28: AssertionError
=========================== short test summary info ============================
FAILED tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1920]
FAILED tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1920]
FAILED tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
FAILED tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections
4 failed, 748 passed in 577.49s (0:09:37)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## verification-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "/workspace/work/evidence-0139/verify_0139.py"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794853837.2566147,
  "exit_code": 0,
  "elapsed": 0.51841139793396
}
```

Comando:

```sh
/workspace/work/venv/bin/python /workspace/work/evidence-0139/verify_0139.py
```

stdout integral — 1211 bytes; SHA-256 81188e467bbb4ecb74af25ac6919e93e0c75497343e0041e97181adfa30371a3:

````text
{
  "version": "0.1.39",
  "schema": 4,
  "protected_bytes_equal": [
    "tests/test_save_lifecycle.py",
    "checkpoint/worker.py",
    "checkpoint/enrichment.py",
    "checkpoint/game_import.py",
    "checkpoint/completion_queue.py",
    "checkpoint/quick_add.py",
    "tests/test_visual_0132.py",
    "checkpoint/database.py",
    "checkpoint/elevation.py",
    "checkpoint/windows_frame.py"
  ],
  "ImageDialog_prefix_equal": true,
  "workflows_unchanged": true,
  "assets_unchanged": true,
  "eight_palettes_equal": true,
  "legacy_test_assertions_equal": [
    "tests/test_complete_layout.py",
    "tests/test_elevation_0137.py",
    "tests/test_isolated_operations.py",
    "tests/test_launch_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_memories_0135.py",
    "tests/test_sessions_0135.py",
    "tests/test_ui_review_lifecycle_0136.py"
  ],
  "bootstrap_main_ast_equal": true,
  "captures": [
    {
      "folder": "revisao-final",
      "count": 27,
      "dpr": [
        1.0
      ]
    },
    {
      "folder": "dpi-150",
      "count": 20,
      "dpr": [
        1.5
      ]
    },
    {
      "folder": "dpi-200",
      "count": 20,
      "dpr": [
        2.0
      ]
    }
  ]
}
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## visual-code-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "scripts/render_0139_review.py",
    "/workspace/work/evidence-0139/codigo-final-9856afc"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794854058.7838712,
  "exit_code": 0,
  "elapsed": 5.8997437953948975
}
```

Comando:

```sh
/workspace/work/venv/bin/python scripts/render_0139_review.py /workspace/work/evidence-0139/codigo-final-9856afc
```

stdout integral — 51 bytes; SHA-256 eb62dd58843922469b28d411993d56dfe315b07ffcf76d717147527cef5c716f:

````text
/workspace/work/evidence-0139/codigo-final-9856afc
````

stderr integral — 698 bytes; SHA-256 3664ca416e7f5fefb138b283f0537946e0f14e2c9df58cd7b2284cbd205a4f71:

````text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
````

## collect-current

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests",
    "--collect-only",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794854077.6159983,
  "exit_code": 0,
  "elapsed": 1.5501744747161865
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests --collect-only -q -p no:cacheprovider
```

stdout integral — 67778 bytes; SHA-256 6f12ebb6554f9add3eebc31fa8f637a5947e53ab90192dfe35bfef7e24ba7d99:

````text
tests/test_add_dialog_0129.py::test_add_dialog_has_one_internal_close_and_no_local_automation_option
tests/test_add_dialog_entrypoints.py::test_wishlist_add_keeps_button_signal_separate_from_drive_file
tests/test_add_from_search_flow.py::test_search_selection_persists_text_source_and_images
tests/test_add_from_search_flow.py::test_ready_search_result_saves_all_text
tests/test_artwork_async_0137.py::test_cold_images_decode_outside_gui_and_do_not_block_events
tests/test_artwork_async_0137.py::test_async_cache_bounds_queue_and_preserves_changed_image
tests/test_artwork_async_0137.py::test_async_transparent_logo_matches_original_raster
tests/test_auto_artwork.py::test_three_kinds_cached_with_provenance_and_no_redownload
tests/test_auto_artwork.py::test_unknown_identity_never_searches_or_guesses
tests/test_auto_artwork.py::test_preserves_manual_cover_and_fetches_other_kinds
tests/test_auto_artwork.py::test_partial_failure_keeps_game_and_successful_art
tests/test_auto_artwork.py::test_changed_cover_during_download_is_not_overwritten
tests/test_auto_artwork.py::test_identity_collision_is_rejected
tests/test_auto_artwork.py::test_disabled_auto_and_manual_retry
tests/test_auto_artwork.py::test_exact_steam_id_resolution_without_title_search
tests/test_auto_artwork.py::test_provider_steam_mapping_and_safe_art_ranking
tests/test_auto_artwork.py::test_background_failure_does_not_raise_into_rom_operation
tests/test_auto_artwork.py::test_missing_key_is_explicit_and_does_not_mutate_game
tests/test_auto_artwork.py::test_identifying_dialog_has_automatic_action_and_preference
tests/test_auto_artwork.py::test_confirmed_catalog_name_standardizes_display_title
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape0]
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape1]
tests/test_avatar_crop_0137.py::test_crop_zoom_cancel_and_persistence_keep_original[shape2]
tests/test_avatar_crop_0137.py::test_invalid_profile_photo_keeps_existing_selection
tests/test_avatar_crop_0137.py::test_photo_orientation_and_drag_are_applied_without_modifying_source
tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample0]
tests/test_banner_0135.py::test_wish_banner_fallback_preserves_proportion[sample1]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1]
tests/test_banner_aspect_0136.py::test_all_four_edges_remain_visible[Portal 2-shape0]
tests/test_banner_aspect_0136.py::test_all_four_edges_remain_visible[Hades-shape1]
tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample0]
tests/test_banner_fallback_0134.py::test_banner_fills_grid_and_home_without_cover[sample1]
tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Zelda: A Link to the Past]
tests/test_banner_render_0135.py::test_hero_keeps_top_and_bottom_borders[Metroid Fusion]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape1]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0]
tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1]
tests/test_bugs_0134.py::test_selected_drive_result_is_not_not_found[sample0]
tests/test_bugs_0134.py::test_selected_drive_result_is_not_not_found[sample1]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-description-Um mundo para explorar.]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-cover-imagem-local.png]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample0-price-2490]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-description-Um mundo para explorar.]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-cover-imagem-local.png]
tests/test_bugs_0134.py::test_any_metadata_prevents_empty_notice[sample1-price-2490]
tests/test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence[sample0]
tests/test_bugs_0134.py::test_price_keeps_last_valid_or_explains_absence[sample1]
tests/test_bugs_0134.py::test_artwork_close_refreshes_library_without_restart[sample0]
tests/test_bugs_0134.py::test_artwork_close_refreshes_library_without_restart[sample1]
tests/test_bugs_0134.py::test_detail_menu_stays_inside_window[sample0]
tests/test_bugs_0134.py::test_detail_menu_stays_inside_window[sample1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size0]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample0-size2]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size0]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size1]
tests/test_bugs_0134.py::test_vertical_cover_fills_its_art_area[sample1-size2]
tests/test_bugs_0134.py::test_wikipedia_detail_has_only_short_intro[sample0]
tests/test_bugs_0134.py::test_wikipedia_detail_has_only_short_intro[sample1]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Zelda: A Link to the Past]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample0-Metroid Fusion]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Zelda: A Link to the Past]
tests/test_capture_0135.py::test_capture_belongs_to_launched_game[sample1-Metroid Fusion]
tests/test_capture_0136.py::test_registration_is_atomic_and_released
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[S]
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[Ctrl+S, Ctrl+P]
tests/test_capture_0136.py::test_invalid_shortcuts_rejected[Ctrl+Left]
tests/test_capture_0136.py::test_foreground_selects_session_not_open_detail[sample0]
tests/test_capture_0136.py::test_foreground_selects_session_not_open_detail[sample1]
tests/test_card_layout.py::test_six_columns_at_default_and_responsive_scaling
tests/test_card_layout.py::test_density_preference_preserved_in_settings_without_schema_change
tests/test_card_layout.py::test_grids_keep_their_proportions_and_size_control_keeps_font_and_items
tests/test_catalog.py::test_catalog_exact_checksum_platform_and_import_idempotence
tests/test_complete_layout.py::test_wishlist_uses_current_prices_and_removal_preserves_game
tests/test_complete_layout.py::test_memories_excludes_removed_games_and_filters_diary
tests/test_complete_layout.py::test_editor_all_tabs_keep_values_and_manual_images
tests/test_complete_layout.py::test_favorite_action_keeps_detail_draft
tests/test_complete_layout.py::test_layout_header_and_library_fit_small_window
tests/test_complete_layout.py::test_theme_swatches_and_profile_apply_without_losing_data
tests/test_completion_queue.py::test_queue_is_serial_and_continues_after_failure
tests/test_completion_queue.py::test_cancel_drops_pending_games_without_destroying_running_job
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-70-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-70-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-150-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample0-150-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-70-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-70-size1]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-150-size0]
tests/test_cover_preview_0135.py::test_five_clickable_covers_have_common_base_and_active_value[sample1-150-size1]
tests/test_cover_preview_0135.py::test_old_percent_preserved_and_keyboard_selects[sample0]
tests/test_cover_preview_0135.py::test_old_percent_preserved_and_keyboard_selects[sample1]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size0]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size1]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size0]
tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size1]
tests/test_data_migration.py::test_first_open_copies_complete_library_and_wal_snapshot
tests/test_data_migration.py::test_first_open_without_legacy_creates_only_new_directory
tests/test_data_migration.py::test_existing_new_directory_is_not_overwritten
tests/test_data_migration.py::test_integrity_failure_never_publishes_or_opens_copied_database
tests/test_data_migration.py::test_credentials_copy_without_overwriting_or_logging_values
tests/test_data_migration.py::test_legacy_light_preference_becomes_default_without_losing_others
tests/test_data_migration.py::test_instance_lock_also_prevents_concurrent_migration
tests/test_data_migration.py::test_explicit_directory_never_uses_real_localappdata
tests/test_data_migration.py::test_corrupt_source_and_empty_existing_destination_are_preserved
tests/test_data_migration.py::test_vault_failure_preserves_source_without_logging_error_payload
tests/test_data_migration.py::test_running_legacy_instance_blocks_copy
tests/test_data_migration.py::test_regular_files_with_similar_names_are_not_discarded
tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Zelda: A Link to the Past]
tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Metroid Fusion]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-rawg]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-steam]
tests/test_detail_0134.py::test_real_source_is_shown[sample0-drive]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-rawg]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-steam]
tests/test_detail_0134.py::test_real_source_is_shown[sample1-drive]
tests/test_detail_0134.py::test_zero_new_fields_is_not_reported_as_search_failure[sample0]
tests/test_detail_0134.py::test_zero_new_fields_is_not_reported_as_search_failure[sample1]
tests/test_detail_0134.py::test_menu_edge_click_runs_only_named_action[sample0]
tests/test_detail_0134.py::test_menu_edge_click_runs_only_named_action[sample1]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample0-Metroid Fusion]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_wish_detail_only_overview[sample1-Metroid Fusion]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample0-Metroid Fusion]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Zelda: A Link to the Past]
tests/test_detail_0135.py::test_no_description_explains_and_offers_actions[sample1-Metroid Fusion]
tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample0]
tests/test_detail_polish_0139.py::test_long_file_name_uses_central_width_and_keeps_full_name[sample1]
tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample0]
tests/test_detail_polish_0139.py::test_completions_use_recorded_timestamp_not_current_status[sample1]
tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample0]
tests/test_dialog_polish_0139.py::test_standard_question_theme_portuguese_default_and_cancellation[sample1]
tests/test_dialog_polish_0139.py::test_session_prompt_has_explicit_actions_and_safe_default[sample0]
tests/test_dialog_polish_0139.py::test_session_prompt_has_explicit_actions_and_safe_default[sample1]
tests/test_dialog_polish_0139.py::test_standard_input_translates_cancel_without_changing_selection[sample0]
tests/test_dialog_polish_0139.py::test_standard_input_translates_cancel_without_changing_selection[sample1]
tests/test_dialog_polish_0139.py::test_authorized_image_viewer_keeps_image_proportions_and_original[sample0]
tests/test_dialog_polish_0139.py::test_authorized_image_viewer_keeps_image_proportions_and_original[sample1]
tests/test_dialog_polish_0139.py::test_only_authorized_protected_constructor_changed
tests/test_drive.py::test_scan_never_downloads_and_keeps_versions
tests/test_drive.py::test_failed_scan_does_not_advance_cursor
tests/test_drive.py::test_failed_download_not_available
tests/test_drive.py::test_full_rescan_marks_missing_without_deleting_local
tests/test_drive.py::test_folder_platform_aliases[/Nintendo Game Boy Advanced/Pok\xe9mon-Game Boy Advance]
tests/test_drive.py::test_folder_platform_aliases[/Super Nintendo (SNES)/Extras-SNES]
tests/test_drive.py::test_folder_platform_aliases[/  super_nintendo (snes) /Extras-SNES]
tests/test_drive.py::test_folder_platform_aliases[/Switch-Nintendo Switch]
tests/test_drive.py::test_folder_platform_aliases[/Nintendo DS/MelonDS-Nintendo DS]
tests/test_drive.py::test_folder_platform_aliases[/Temas-]
tests/test_drive.py::test_folder_platform_aliases[/Switch Games-]
tests/test_drive.py::test_folder_platform_aliases[/Nintendo DS/PSP-]
tests/test_drive.py::test_folder_platform_aliases[C:\\ROMs\\Nintendo 3DS-Nintendo 3DS]
tests/test_drive.py::test_reclassification_preserves_existing_metadata
tests/test_drive.py::test_root_themes_are_not_roms
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - Spirit Tracks (USA) (Rev 1).nds-The Legend of Zelda: Spirit Tracks-Nintendo DS]
tests/test_drive_0133.py::test_no_intro_identity[Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip-Yu-Gi-Oh! - Ultimate Masters 2006-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Zelda (Game & Watch).zip-Zelda (Game & Watch)-]
tests/test_drive_0133.py::test_no_intro_identity[Mother 3 [!].gba-Mother 3-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - The Minish Cap (USA).gba-The Legend of Zelda: The Minish Cap-Game Boy Advance]
tests/test_drive_0133.py::test_no_intro_identity[Little Mermaid, The (USA).nes-The Little Mermaid-NES]
tests/test_drive_0133.py::test_no_intro_identity[Amazing Spider-Man, The (USA).gb-The Amazing Spider-Man-Game Boy]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - Oracle of Ages (USA, Australia).gbc-The Legend of Zelda: Oracle of Ages-Game Boy Color]
tests/test_drive_0133.py::test_no_intro_identity[Legend of Zelda, The - A Link to the Past (USA).sfc-The Legend of Zelda: A Link to the Past-SNES]
tests/test_drive_0133.py::test_no_intro_identity[Incredible Hulk, The (Europe).md.zip-The Incredible Hulk-Mega Drive]
tests/test_drive_0133.py::test_drive_normalized_search_click_flow
tests/test_drive_0133.py::test_drive_no_results_is_explicit_and_link_survives
tests/test_drive_0133.py::test_articles_and_subtitle_separator
tests/test_drive_auth.py::test_token_exchange_failure_reports_stage_without_secrets
tests/test_drive_auth.py::test_vault_failure_is_distinct_from_oauth_failure
tests/test_drive_auth.py::test_success_initializes_drive_after_persisting_token
tests/test_drive_auth.py::test_initial_token_exchange_has_network_timeout
tests/test_drive_metadata_policy.py::test_drive_enrichment_uses_text_but_not_rawg_images
tests/test_drive_metadata_policy.py::test_manual_search_recovers_existing_rom_without_duplicate
tests/test_drive_search.py::test_rom_search_platform_and_literal_query
tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[False]
tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[True]
tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[sem-resultado]
tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[fonte-indisponivel]
tests/test_elevation_0137.py::test_uac_handoff_preserves_arguments_paths_and_original_identity
tests/test_elevation_0137.py::test_uac_cancel_and_other_account_never_retry_or_prepare_data
tests/test_elevation_0137.py::test_already_elevated_same_account_continues_without_new_prompt
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[handoff]
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[cancel]
tests/test_elevation_0137.py::test_frozen_startup_handles_uac_before_opening_data[different_account]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-0-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-1-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample0-2-desejos]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-0-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-1-biblioteca]
tests/test_empty_copy_0135.py::test_empty_state_identifies_destination_and_keeps_action[sample1-2-desejos]
tests/test_enrichment.py::test_steam_details_validate_appid_and_parse_fields
tests/test_enrichment.py::test_fill_missing_preserves_personal_values_and_tracks_images
tests/test_enrichment.py::test_unknown_game_never_searches_by_name
tests/test_enrichment.py::test_download_failure_keeps_metadata_and_game
tests/test_enrichment.py::test_concurrent_edit_during_download_is_preserved
tests/test_enrichment.py::test_wrong_identity_response_never_applied
tests/test_enrichment.py::test_rawg_confirmed_rom_uses_its_own_identity
tests/test_enrichment.py::test_form_saves_without_network_or_nested_loading_dialog
tests/test_enrichment.py::test_unknown_game_requires_selection
tests/test_enrichment.py::test_batch_cancellation_keeps_existing_library
tests/test_enrichment.py::test_steam_header_is_fallback_after_library_hero
tests/test_enrichment.py::test_existing_automatic_header_upgrades_and_keeps_old_cache
tests/test_enrichment.py::test_missing_hero_does_not_replace_existing_header_with_another_header
tests/test_enrichment.py::test_modified_header_content_is_preserved_as_user_choice
tests/test_enrichment.py::test_manual_confirmation_during_header_download_wins
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-False]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-True]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-False]
tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-True]
tests/test_folder_platforms.py::test_persistent_rules_inherit_and_specific_override
tests/test_folder_platforms.py::test_rule_applies_to_new_files_and_renamed_folder_id
tests/test_folder_platforms.py::test_bad_rules_leave_saved_data_unchanged
tests/test_folder_platforms.py::test_new_console_aliases[PS1-PlayStation]
tests/test_folder_platforms.py::test_new_console_aliases[PSX-PlayStation]
tests/test_folder_platforms.py::test_new_console_aliases[PS2-PlayStation 2]
tests/test_folder_platforms.py::test_new_console_aliases[Nintendo GameCube-GameCube]
tests/test_folder_platforms.py::test_new_console_aliases[NGC-GameCube]
tests/test_folder_platforms.py::test_new_console_aliases[Nintendo Wii-Wii]
tests/test_folder_platforms.py::test_create_confirmed_game_and_link_version
tests/test_folder_platforms.py::test_folder_dialog_saves_rule_and_gallery_has_cover_icons
tests/test_game_import.py::test_catalog_title_is_separate_from_original_rom_name
tests/test_game_import.py::test_second_version_reuses_confirmed_identity
tests/test_game_import.py::test_wrong_existing_link_is_not_silently_replaced
tests/test_game_import.py::test_failed_import_does_not_create_orphan
tests/test_game_import.py::test_add_form_drive_search_and_metadata_prefill
tests/test_game_import.py::test_fit_preserves_entire_vertical_art
tests/test_game_import.py::test_artwork_progress_finishes_and_closes
tests/test_game_import.py::test_catalog_selection_closes_with_confirmed_result
tests/test_game_saves.py::test_game_backup_worker_history_restore_and_profile_versions
tests/test_game_saves.py::test_missing_profile_or_destination_is_explicit
tests/test_game_saves.py::test_changing_save_does_not_publish_backup
tests/test_ggdeals_api.py::test_api_parser_current_and_history_are_distinct_not_a_discount
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload0]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload1]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload2]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload3]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload4]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload5]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload6]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload7]
tests/test_ggdeals_api.py::test_api_rejects_invalid_response_and_foreign_currency[payload8]
tests/test_ggdeals_api.py::test_api_missing_one_current_field_does_not_invent_zero
tests/test_ggdeals_api.py::test_transport_parameters_and_failures_never_reveal_in_memory_secret
tests/test_ggdeals_api.py::test_api_reflected_secret_response_is_rejected_without_storage
tests/test_ggdeals_api.py::test_missing_steam_id_does_not_call_provider
tests/test_ggdeals_api.py::test_factory_selects_api_or_configured_public_fallback
tests/test_ggdeals_api.py::test_api_failure_keeps_previous_price_and_null_is_not_zero
tests/test_ggdeals_connection.py::test_connection_key_is_masked_transient_and_only_saved_to_vault
tests/test_ggdeals_connection.py::test_vault_errors_never_echo_input_or_exception
tests/test_ggdeals_connection.py::test_configuration_change_rechecks_prices_without_discarding_cache
tests/test_grid_performance_0137.py::test_collection_totals_use_bounded_queries_without_duplicate_snapshots
tests/test_grid_performance_0137.py::test_cache_is_bounded_and_invalidates_changed_files
tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample0]
tests/test_grid_performance_0137.py::test_refresh_preserves_items_and_scroll_with_equal_grid_margins[sample1]
tests/test_home_0129.py::test_home_only_in_progress_and_latest_session_hero
tests/test_home_0129.py::test_home_without_started_games_has_no_invented_hero
tests/test_home_0129.py::test_home_hero_button_remains_inside_banner_after_resizing
tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles0]
tests/test_home_data_0137.py::test_recent_games_use_real_start_not_status_or_updated_at[titles1]
tests/test_home_data_0137.py::test_week_summary_clips_boundaries_and_excludes_steam_and_unreviewed
tests/test_home_data_0137.py::test_home_offers_follow_same_discount_policy_and_do_not_promote_stale_cache
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[None]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[inv\xe1lida]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:00]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T11:00:00+00:00]
tests/test_home_data_0137.py::test_home_does_not_present_unknown_expired_or_future_cache_as_current[2026-11-16T12:00:01+00:00]
tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample0]
tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample1]
tests/test_home_layout_0137.py::test_home_actions_are_distinct_and_week_opens_correct_period[sample0]
tests/test_home_layout_0137.py::test_home_actions_are_distinct_and_week_opens_correct_period[sample1]
tests/test_home_layout_0137.py::test_home_columns_align_top_and_art_is_contained[sample0]
tests/test_home_layout_0137.py::test_home_columns_align_top_and_art_is_contained[sample1]
tests/test_home_layout_0137.py::test_memory_carousel_bounds_keyboard_and_no_data_changes[sample0]
tests/test_home_layout_0137.py::test_memory_carousel_bounds_keyboard_and_no_data_changes[sample1]
tests/test_home_layout_0137.py::test_status_change_does_not_create_recent_card[sample0]
tests/test_home_layout_0137.py::test_status_change_does_not_create_recent_card[sample1]
tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample0]
tests/test_home_layout_0137.py::test_three_recent_games_carousel_preserves_every_cover_edge[sample1]
tests/test_home_layout_0137.py::test_offers_show_only_same_offer_original_discount_and_current[sample0]
tests/test_home_layout_0137.py::test_offers_show_only_same_offer_original_discount_and_current[sample1]
tests/test_home_layout_0137.py::test_offer_banner_uses_entire_banner_instead_of_cover[sample0]
tests/test_home_layout_0137.py::test_offer_banner_uses_entire_banner_instead_of_cover[sample1]
tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample0]
tests/test_home_polish_0139.py::test_recent_sessions_keep_repeat_game_and_exclude_failures[sample1]
tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample0]
tests/test_home_polish_0139.py::test_recent_cards_height_follows_content_and_button_fits[sample1]
tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample0]
tests/test_home_polish_0139.py::test_recent_art_has_rounded_transparent_corners_without_losing_edges[sample1]
tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample0]
tests/test_home_polish_0139.py::test_offer_thumbnail_rounds_four_corners_and_never_overlaps_text[sample1]
tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample0]
tests/test_home_polish_0139.py::test_restricted_cover_has_no_dark_letterbox[sample1]
tests/test_home_polish_0139.py::test_resizing_preserves_visible_session_focus_and_card[sample0]
tests/test_home_polish_0139.py::test_resizing_preserves_visible_session_focus_and_card[sample1]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[10]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[16]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[18]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[20]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[22]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[24]
tests/test_icons_0134.py::test_lucide_uses_context_size_and_one_stroke[32]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-0]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-1]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-2]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-3]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-4]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-5]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample0-6]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-0]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-1]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-2]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-3]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-4]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-5]
tests/test_interface_text_0135.py::test_interface_has_only_labels_data_and_actionable_absence[sample1-6]
tests/test_isolated_operations.py::test_real_worker_entry_does_not_open_gui_or_require_credentials
tests/test_isolated_operations.py::test_abrupt_child_exit_is_reported_without_terminating_parent
tests/test_isolated_operations.py::test_real_transfer_child_adds_library_preserves_original_and_local_file
tests/test_isolated_operations.py::test_drive_ui_survives_art_child_failure_after_real_transfer
tests/test_isolated_operations.py::test_platform_and_ambiguous_matches_do_not_silently_choose_wrong_edition
tests/test_isolated_operations.py::test_automatic_title_lookup_combines_same_title_sources_without_manual_picker
tests/test_isolated_operations.py::test_conflicting_combined_identities_roll_back_import
tests/test_isolated_operations.py::test_binding_automatic_result_keeps_personal_fields
tests/test_isolated_operations.py::test_new_game_form_keeps_optional_configuration_collapsed
tests/test_isolated_operations.py::test_transfer_child_exit_preserves_partial_without_publishing_corrupt_rom
tests/test_isolated_operations.py::test_main_window_close_waits_for_child_operation
tests/test_isolated_operations.py::test_automatic_name_does_not_confuse_sequels
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-N\xe3o iniciado]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample0-Backlog]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-N\xe3o iniciado]
tests/test_labels_0137.py::test_not_started_label_keeps_legacy_data_on_open[sample1-Backlog]
tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample0]
tests/test_labels_0137.py::test_period_and_sort_labels_keep_underlying_keys[sample1]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Zelda: A Link to the Past-SNES-.sfc]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample0-Metroid Fusion-GBA-.gba]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Zelda: A Link to the Past-SNES-.sfc]
tests/test_launch_0135.py::test_main_play_routes_linked_rom[sample1-Metroid Fusion-GBA-.gba]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Zelda: A Link to the Past]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample0-Metroid Fusion]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Zelda: A Link to the Past]
tests/test_launch_0135.py::test_rom_launch_monitors_emulator_exit[sample1-Metroid Fusion]
tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample0]
tests/test_layout_0134.py::test_list_uses_fixed_logo_area_or_title[sample1]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1280]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1920]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1280]
tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1920]
tests/test_layout_0134.py::test_settings_paths_labels_grid_and_update_action[sample0]
tests/test_layout_0134.py::test_settings_paths_labels_grid_and_update_action[sample1]
tests/test_layout_0134.py::test_home_empty_text_and_files_action[sample0]
tests/test_layout_0134.py::test_home_empty_text_and_files_action[sample1]
tests/test_layout_regressions_025.py::test_home_search_opens_library_results
tests/test_layout_regressions_025.py::test_empty_state_shows_instructional_description
tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
tests/test_layout_regressions_025.py::test_add_game_uses_library_from_home_and_library
tests/test_layout_regressions_025.py::test_large_steam_import_keeps_dialog_bounded_without_per_game_log
tests/test_layout_regressions_025.py::test_wishlist_fetches_missing_logo_once_and_updates_card
tests/test_library.py::test_crud_persistence_filters_and_recovery
tests/test_library.py::test_validation_sql_and_literal_search
tests/test_library.py::test_diary_settings_and_stats
tests/test_library.py::test_database_backup_and_foreign_keys
tests/test_library.py::test_filter_individual_genre_from_imported_metadata
tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample0]
tests/test_library_list_0137.py::test_horizontal_list_has_logo_time_and_independent_favorite[sample1]
tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample0]
tests/test_library_list_0137.py::test_list_search_and_sort_preserve_filtering[sample1]
tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[Pok\xe9mon FireRed and LeafGreen+]
tests/test_loading_preview_0137.py::test_loading_preview_is_blank_until_cover_arrives[The Legend of Zelda: Ocarina of Time 3D]
tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom0]
tests/test_local_rom_0137.py::test_bind_launch_and_reopen_local_rom_without_drive[local_rom1]
tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom0]
tests/test_local_rom_0137.py::test_local_replacement_keeps_previous_file_and_failed_selection_is_atomic[local_rom1]
tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom0]
tests/test_local_rom_0137.py::test_local_link_requires_explicit_profile_capability_and_read_access[local_rom1]
tests/test_local_rom_0137.py::test_distinct_ocarina_platform_and_edition_are_not_equivalent
tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom0]
tests/test_local_rom_0137.py::test_cancel_local_dialog_does_not_change_link[local_rom1]
tests/test_local_rom_0137.py::test_play_missing_local_file_offers_relocation_without_session[local_rom0]
tests/test_local_rom_0137.py::test_play_missing_local_file_offers_relocation_without_session[local_rom1]
tests/test_local_rom_0137.py::test_local_confirm_button_persists_only_after_click[local_rom0]
tests/test_local_rom_0137.py::test_local_confirm_button_persists_only_after_click[local_rom1]
tests/test_localized_metadata.py::test_portuguese_description_requires_exact_game_platform_and_not_ambiguous
tests/test_localized_metadata.py::test_localization_rejects_disambiguation_and_missing_translation
tests/test_localized_metadata.py::test_steam_requests_brazilian_and_parses_brazilian_release_date
tests/test_localized_metadata.py::test_rom_with_art_identity_gets_portuguese_description_and_attribution
tests/test_localized_metadata.py::test_localization_preserves_manual_text_and_replaces_exact_legacy_source
tests/test_localized_metadata.py::test_release_date_roundtrip_and_information_always_visible
tests/test_localized_metadata.py::test_legacy_steam_english_is_replaced_only_on_exact_source_match
tests/test_localized_metadata.py::test_enrichment_fetches_rom_description_even_when_all_art_exists
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_empty_memory_goes_to_game_tab[sample1-Metroid Fusion]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_memory_card_geometry_and_title[sample1-Metroid Fusion]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample0-Metroid Fusion]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Zelda: A Link to the Past]
tests/test_memories_0135.py::test_delete_memory_requires_confirmation[sample1-Metroid Fusion]
tests/test_migrations.py::test_upgrade_v1_keeps_user_data
tests/test_migrations.py::test_newer_schema_refused_without_mutation
tests/test_migrations.py::test_failed_migration_rolls_back_all_ddl
tests/test_migrations.py::test_upgrade_v2_preserves_covers_and_ids
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Zelda: A Link to the Past]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample0-Metroid Fusion]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Zelda: A Link to the Past]
tests/test_mockup_exclusions_0135.py::test_mockup_extras_are_absent_and_theme_cards_work[sample1-Metroid Fusion]
tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4660]
tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4886718345]
tests/test_native_startup_0138.py::test_invalid_native_message_does_not_create_a_window
tests/test_native_startup_0138.py::test_real_platform_window_opens_and_closes_in_isolated_process[Portal 2]
tests/test_native_startup_0138.py::test_real_platform_window_opens_and_closes_in_isolated_process[Hades]
tests/test_network.py::test_safe_nested_diagnosis[error0-proxy]
tests/test_network.py::test_safe_nested_diagnosis[error1-tls]
tests/test_network.py::test_safe_nested_diagnosis[error2-dns]
tests/test_network.py::test_safe_nested_diagnosis[error3-timeout]
tests/test_network.py::test_safe_nested_diagnosis[error4-reset]
tests/test_network.py::test_safe_nested_diagnosis[error5-refused]
tests/test_network.py::test_safe_nested_diagnosis[error6-connection]
tests/test_network.py::test_safe_nested_diagnosis[error7-unknown]
tests/test_network.py::test_chain_handles_cycles
tests/test_network.py::test_probe_does_not_send_oauth_data
tests/test_network.py::test_probe_reports_tls_without_error_contents
tests/test_network.py::test_safe_details_exclude_exception_messages
tests/test_network.py::test_remote_disconnect_is_recognized
tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample0]
tests/test_period_chart_0137.py::test_week_chart_uses_width_and_months_keep_real_days[sample1]
tests/test_period_chart_0137.py::test_hourly_day_uses_real_local_session_boundaries
tests/test_period_chart_0137.py::test_day_hours_respect_dst_and_do_not_change_instants
tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample0]
tests/test_polish_0139.py::test_two_wishes_remain_compact_and_wide_window_adds_columns[sample1]
tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample0]
tests/test_polish_0139.py::test_diary_only_is_compact_and_mixed_cards_align[sample1]
tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample0]
tests/test_polish_0139.py::test_cover_mouse_selection_and_keyboard_focus_stay_on_art[sample1]
tests/test_polish_0139.py::test_black_is_neutral_and_other_themes_preserved
tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample0]
tests/test_polish_0139.py::test_add_wish_icon_matches_primary_foreground[sample1]
tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample0]
tests/test_polish_0139.py::test_library_scrollbar_has_stable_gutter[sample1]
tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample0]
tests/test_polish_0139.py::test_saves_empty_has_one_compact_configuration_action[sample1]
tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample0]
tests/test_polish_0139.py::test_settings_exposes_emulators_and_trash_without_changing_records[sample1]
tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample0]
tests/test_polish_0139.py::test_mixed_diary_preview_matches_capture_area[sample1]
tests/test_price_display_official.py::test_official_history_is_never_struck_out_or_used_as_discount
tests/test_price_display_official.py::test_price_order_places_missing_prices_last_and_respects_name
tests/test_price_display_official.py::test_wishlist_and_detail_have_active_attribution_and_no_steam_queue
tests/test_price_display_official.py::test_foreign_currency_cache_never_renders_as_reais
tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Zelda Phantom Hourglass-Nintendo DS]
tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Metroid Dread-Nintendo Switch]
tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Portal 2]
tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Hades II]
tests/test_price_integrity_0136.py::test_discount_sort_and_keyshop_policy
tests/test_price_integrity_0136.py::test_comparison_has_reason_instead_of_bare_unavailable
tests/test_price_integrity_0136.py::test_discount_visible_only_for_offer_and_rounds_half_up
tests/test_price_integrity_0136.py::test_discount_follows_active_theme
tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Portal 2]
tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Hades]
tests/test_price_integrity_0136.py::test_price_store_and_original_do_not_mix_tied_offers
tests/test_prices_0129.py::test_original_price_and_discount_come_from_same_offer
tests/test_prices_0129.py::test_official_api_without_saved_key_never_calls_transport
tests/test_prices_0129.py::test_wishlist_name_price_sort_and_scroll_survive_refresh
tests/test_prices_0135.py::test_official_default[Zelda: A Link to the Past]
tests/test_prices_0135.py::test_official_default[Metroid Fusion]
tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Zelda: A Link to the Past]
tests/test_prices_0135.py::test_unknown_cache_is_not_an_official_offer[Metroid Fusion]
tests/test_profile.py::test_nickname_and_photo_are_local_persistent_and_preserve_original
tests/test_profile.py::test_profile_cancel_and_remove_photo_keep_saved_name
tests/test_quick_add.py::test_unified_catalog_combines_details_without_provider_selection
tests/test_quick_add.py::test_console_search_does_not_match_pc_edition
tests/test_quick_add.py::test_search_failure_keeps_other_sources_usable
tests/test_quick_add.py::test_search_prefills_form_and_can_save_without_advanced_step
tests/test_quick_add.py::test_stale_lookup_cannot_overwrite_new_query
tests/test_quick_add.py::test_drive_choice_preserves_original_and_searches_platform
tests/test_quick_add.py::test_same_title_across_sources_is_one_result_not_a_provider_choice
tests/test_quick_add.py::test_standalone_dialog_finishes_query_before_destruction
tests/test_quick_add.py::test_source_change_rejects_inflight_catalog_and_steam_uses_import
tests/test_quick_add.py::test_drive_source_displays_versions_and_preserves_original
tests/test_quick_add.py::test_nested_dialog_keeps_query_receiver_alive_until_job_finishes
tests/test_reference_layout_0128.py::test_sidebar_keeps_identity_navigation_footer_and_profile_chevron
tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections
tests/test_reference_layout_0128.py::test_detail_play_and_secondary_setup_obey_execution_configuration
tests/test_reference_layout_0128.py::test_connections_match_two_by_two_cards_help_and_green_configured_dot
tests/test_registration_0128.py::test_empty_tabs_search_and_empty_library_have_distinct_actions
tests/test_registration_0128.py::test_quick_add_requires_selection_and_has_exclusive_search_state
tests/test_registration_0128.py::test_wish_reusing_owned_identity_does_not_remove_game
tests/test_registration_0128.py::test_new_wish_has_visible_confirmation
tests/test_registration_0128.py::test_selected_preview_does_not_overlap_other_result_link
tests/test_registration_0128.py::test_missing_cover_draws_full_title_instead_of_two_letters
tests/test_registration_0128.py::test_activity_summary_uses_singular_day_and_brazilian_date
tests/test_revision_0128.py::test_wishlist_one_and_five_cards_keep_same_fixed_square_art_area
tests/test_revision_0128.py::test_library_has_responsive_vertical_columns_at_minimum_and_full_hd
tests/test_revision_0128.py::test_count_helper_handles_zero_singular_plural_and_irregular
tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[]
tests/test_rom_edition_0137.py::test_drive_worker_rejects_distinct_ocarina_edition_before_binding[Nintendo 64]
tests/test_rom_edition_0137.py::test_drive_sheet_shows_divergence_without_starting_job
tests/test_rom_link_0134.py::test_exact_rom_ranking_and_unique_replacement[rom0]
tests/test_rom_link_0134.py::test_exact_rom_ranking_and_unique_replacement[rom1]
tests/test_rom_link_0134.py::test_rom_pipeline_download_text_and_art[rom0]
tests/test_rom_link_0134.py::test_rom_pipeline_download_text_and_art[rom1]
tests/test_rom_link_0134.py::test_missing_catalog_keeps_link_and_cause[rom0]
tests/test_rom_link_0134.py::test_missing_catalog_keeps_link_and_cause[rom1]
tests/test_rom_link_0134.py::test_files_dialog_click_runs_and_finishes[rom0]
tests/test_rom_link_0134.py::test_files_dialog_click_runs_and_finishes[rom1]
tests/test_rom_link_0134.py::test_failed_link_exposes_cause_and_retry[rom0]
tests/test_rom_link_0134.py::test_failed_link_exposes_cause_and_retry[rom1]
tests/test_rom_link_0134.py::test_existing_add_and_manager_also_replace_unique_link[rom0]
tests/test_rom_link_0134.py::test_existing_add_and_manager_also_replace_unique_link[rom1]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Yu-Gi-Oh! - Ultimate Masters 2006 # GBA.zip-Yu-Gi-Oh! - Ultimate Masters 2006-Game Boy Advance]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Pokemon - Platinum (USA) (Rev 1).nds-Pokemon: Platinum-Nintendo DS]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Metroid_Fusion [!].gba.zip-Metroid Fusion-Game Boy Advance]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[Zelda (Europe) (En,Fr,De).sfc-Zelda-SNES]
tests/test_rom_titles_0129.py::test_rom_identity_cleans_file_metadata_only[A Game (The Return).gba-A Game (The Return)-Game Boy Advance]
tests/test_rom_titles_0129.py::test_drive_records_platform_without_changing_original_name
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[success]
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[failure]
tests/test_save_lifecycle.py::test_full_save_and_loading_process_exits_cleanly[drive]
tests/test_save_lifecycle.py::test_save_smoke_refuses_existing_database
tests/test_save_profiles.py::test_profiles_persist_and_reject_states
tests/test_saves.py::test_backup_restore_preserves_previous_and_ignores_states
tests/test_saves.py::test_rejects_traversal_and_broad_patterns
tests/test_saves.py::test_legacy_backup_manifest_remains_readable
tests/test_search_save_0129.py::test_accept_during_selected_details_waits_and_saves_full_record
tests/test_service_branding_0135.py::test_service_brands_do_not_use_lucide[Zelda: A Link to the Past]
tests/test_service_branding_0135.py::test_service_brands_do_not_use_lucide[Metroid Fusion]
tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Zelda: A Link to the Past]
tests/test_service_logo_0135.py::test_steam_logo_occupancy_matches_drive[Metroid Fusion]
tests/test_service_optical_0136.py::test_steam_white_mark_optically_centered_and_asset_unchanged
tests/test_services.py::test_metadata_requires_selection_and_parses_without_network
tests/test_services.py::test_emulator_arguments_no_shell
tests/test_services.py::test_sessions_recover_without_inventing_duration
tests/test_services.py::test_spawn_and_poll_actual_process
tests/test_services.py::test_emulator_exit_does_not_infer_rom_session_end
tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Zelda: A Link to the Past-SNES-.sfc]
tests/test_sessions_0135.py::test_rom_session_finishes_after_real_process_exit[Metroid Fusion-GBA-.gba]
tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample0]
tests/test_settings_0135.py::test_cover_control_label_and_full_width[sample1]
tests/test_settings_0135.py::test_connections_standard_buttons[sample0]
tests/test_settings_0135.py::test_connections_standard_buttons[sample1]
tests/test_settings_0135.py::test_backup_action_emphasis[sample0]
tests/test_settings_0135.py::test_backup_action_emphasis[sample1]
tests/test_settings_navigation_0139.py::test_profile_edit_keeps_id_and_remove_preserves_files_and_used_profile[sample0]
tests/test_settings_navigation_0139.py::test_profile_edit_keeps_id_and_remove_preserves_files_and_used_profile[sample1]
tests/test_settings_navigation_0139.py::test_execution_profile_filters_preserves_on_cancel_and_survives_reopen[sample0]
tests/test_settings_navigation_0139.py::test_execution_profile_filters_preserves_on_cancel_and_survives_reopen[sample1]
tests/test_settings_navigation_0139.py::test_trash_restores_only_chosen_homonym_and_keeps_navigation[sample0]
tests/test_settings_navigation_0139.py::test_trash_restores_only_chosen_homonym_and_keeps_navigation[sample1]
tests/test_settings_navigation_0139.py::test_trash_unknown_date_does_not_invent_timestamp[sample0]
tests/test_settings_navigation_0139.py::test_trash_unknown_date_does_not_invent_timestamp[sample1]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Zelda: A Link to the Past]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample0-Metroid Fusion]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Zelda: A Link to the Past]
tests/test_settings_space_0135.py::test_appearance_uses_window_and_cover_preview[sample1-Metroid Fusion]
tests/test_smooth_scroll.py::test_wheel_with_500_games_uses_pixel_animation_and_remains_responsive
tests/test_statistics_0136.py::test_calendar_bounds_clamp_and_monday
tests/test_statistics_0136.py::test_period_clips_local_midnight_without_altering_data[Portal 2]
tests/test_statistics_0136.py::test_period_clips_local_midnight_without_altering_data[Metroid Fusion]
tests/test_statistics_0136.py::test_dst_and_empty_do_not_distribute_steam
tests/test_statistics_0136.py::test_equivalent_metrics_and_period_selector[sample0]
tests/test_statistics_0136.py::test_equivalent_metrics_and_period_selector[sample1]
tests/test_statistics_0136.py::test_fall_dst_is_25_hours_and_year_boundary
tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample0]
tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample1]
tests/test_statistics_visible_0136.py::test_genres_are_removed_from_statistics_and_completions_remain[sample0]
tests/test_statistics_visible_0136.py::test_genres_are_removed_from_statistics_and_completions_remain[sample1]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Zelda: A Link to the Past]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample0-Metroid Fusion]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Zelda: A Link to the Past]
tests/test_status_0135.py::test_status_control_persists_all_choices[sample1-Metroid Fusion]
tests/test_status_pill_0136.py::test_status_is_one_themed_control_without_annotation[sample0]
tests/test_status_pill_0136.py::test_status_is_one_themed_control_without_annotation[sample1]
tests/test_status_pill_0136.py::test_click_on_status_dot_opens_menu_and_keyboard_saves_choice[sample0]
tests/test_status_pill_0136.py::test_click_on_status_dot_opens_menu_and_keyboard_saves_choice[sample1]
tests/test_steam.py::test_owned_games_contract_and_hidden_hours
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response0]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response1]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response2]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response3]
tests/test_steam.py::test_private_or_malformed_library_is_not_treated_as_empty[response4]
tests/test_steam.py::test_input_validation_before_network_and_safe_provider_error
tests/test_steam.py::test_achievements_keep_locked_and_unknown_unlock_date_distinct
tests/test_steam.py::test_import_is_repeatable_and_preserves_local_data_and_separate_accounts
tests/test_steam.py::test_same_name_does_not_merge_without_explicit_choice
tests/test_steam.py::test_conflicting_or_trashed_identity_rolls_back_entire_batch
tests/test_steam.py::test_achievement_snapshot_is_idempotent_and_preserves_personal_records
tests/test_steam.py::test_v3_upgrade_keeps_library_and_creates_recoverable_backup
tests/test_steam.py::test_dialog_async_query_selection_import_achievements_and_account_change
tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[620-Portal 2]
tests/test_steam_installations_0135.py::test_discover_steam_multiple_libraries[400-Portal]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Zelda: A Link to the Past]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample0-Metroid Fusion]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Zelda: A Link to the Past]
tests/test_tabs_0135.py::test_drag_does_not_select_tab_but_click_and_key_do[sample1-Metroid Fusion]
tests/test_themes.py::test_palette_normal_text_contrast[blue]
tests/test_themes.py::test_palette_normal_text_contrast[green]
tests/test_themes.py::test_palette_normal_text_contrast[yellow]
tests/test_themes.py::test_palette_normal_text_contrast[red]
tests/test_themes.py::test_palette_normal_text_contrast[black]
tests/test_themes.py::test_palette_normal_text_contrast[purple]
tests/test_themes.py::test_palette_normal_text_contrast[pink]
tests/test_themes.py::test_palette_normal_text_contrast[orange]
tests/test_themes.py::test_palette_normal_text_contrast[cyan]
tests/test_themes.py::test_theme_selection_is_immediate_and_survives_reopening
tests/test_themes.py::test_unknown_theme_falls_back_to_green
tests/test_themes.py::test_unknown_saved_preference_falls_back_without_losing_library
tests/test_themes.py::test_exactly_nine_themes_and_swatches
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Zelda: A Link to the Past]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample0-Metroid Fusion]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Zelda: A Link to the Past]
tests/test_time_0135.py::test_combined_time_without_join_multiplication[sample1-Metroid Fusion]
tests/test_time_prices_0134.py::test_app_and_steam_times_are_combined[sample0]
tests/test_time_prices_0134.py::test_app_and_steam_times_are_combined[sample1]
tests/test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price[sample0]
tests/test_time_prices_0134.py::test_wish_card_keeps_price_and_explains_no_price[sample1]
tests/test_trash_import.py::test_restore_retains_history_and_art
tests/test_trash_import.py::test_new_entry_preserves_trash_and_does_not_steal_identity_on_restore
tests/test_trash_import.py::test_cancel_and_failed_new_leave_trash_unchanged
tests/test_trash_import.py::test_title_matching_is_exact_and_platform_specific
tests/test_trash_import.py::test_explicit_new_does_not_repeat_late_catalog_prompt
tests/test_ui.py::test_navigate_and_game_detail_with_real_database
tests/test_ui.py::test_game_form_validation_and_round_trip
tests/test_ui.py::test_game_form_file_buttons_keep_their_field
tests/test_ui.py::test_parentless_game_form_process_exits_cleanly
tests/test_ui.py::test_image_cache_validates_and_deduplicates
tests/test_ui.py::test_session_end_triggers_background_game_backup
tests/test_ui.py::test_updates_dialog_starts_without_network_or_credentials
tests/test_ui.py::test_updates_require_saving_typed_credential_before_network
tests/test_ui_polish.py::test_banner_is_bounded_at_desktop_width
tests/test_ui_polish.py::test_compact_loading_and_centered_name
tests/test_ui_polish.py::test_statistics_chart_uses_library_totals
tests/test_ui_polish.py::test_library_caption_starts_at_visible_cover_edge
tests/test_ui_redesign.py::test_game_detail_uses_banner_logo_tabs_and_preserves_files
tests/test_ui_redesign.py::test_settings_are_compact_and_restore_selected_section
tests/test_ui_redesign.py::test_library_shortcuts_size_and_theme_update
tests/test_ui_redesign.py::test_add_sources_do_not_start_network_or_nested_loading
tests/test_ui_redesign.py::test_home_tiles_are_full_height_and_open_real_game
tests/test_ui_redesign.py::test_detail_refresh_preserves_diary_draft_and_save_clears_it
tests/test_ui_redesign.py::test_cover_grid_uses_width_at_desktop_and_compact_window
tests/test_ui_redesign.py::test_home_places_activity_beside_continuity
tests/test_ui_review_lifecycle_0136.py::test_review_releases_global_shortcut_between_windows
tests/test_updates.py::test_versions_skip_old_drafts_previews_and_unverified_assets
tests/test_updates.py::test_extract_and_swap_preserves_previous
tests/test_updates.py::test_unsafe_archives_rejected[../outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/../outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[C:/outside.exe]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/file.txt:ads]
tests/test_updates.py::test_unsafe_archives_rejected[Checkpoint/CON.txt]
tests/test_updates.py::test_copy_failure_rolls_back
tests/test_updates.py::test_private_download_strips_token_on_cdn_and_verifies
tests/test_updates.py::test_corrupt_download_never_extracts
tests/test_updates.py::test_check_decodes_gzip_response_before_json
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[ProxyError-proxy]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[SSLError-certificado]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[Timeout-demorou]
tests/test_updates.py::test_connection_errors_are_specific_and_hide_secrets[ConnectionError-firewall]
tests/test_updates.py::test_invalid_json_reports_response_not_network
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[blue]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[green]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[yellow]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[red]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[black]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[purple]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[pink]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[orange]
tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[cyan]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[home-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[home-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[library-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[library-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[wish-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[wish-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[detail-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[detail-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[sparse-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[sparse-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-0-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-0-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-1-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-1-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-2-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-2-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-3-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[settings-3-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[add-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[add-pink]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[drive-green]
tests/test_visual_0132.py::test_scope_fits_1280_without_horizontal_overflow[drive-pink]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[0]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[1]
tests/test_visual_0132.py::test_empty_pages_have_title_description_and_action[2]
tests/test_visual_0132.py::test_library_and_wishes_reuse_art_component_and_dimensions
tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged
tests/test_visual_0132.py::test_sparse_detail_and_gallery_explain_missing_content
tests/test_visual_0132.py::test_settings_without_accounts_still_has_states_and_actions
tests/test_visual_0132.py::test_empty_drive_list_has_explanation_and_existing_refresh_action
tests/test_visual_0132.py::test_empty_search_dialog_keeps_instruction_and_disabled_save
tests/test_visual_0132.py::test_reapplying_same_theme_does_not_repolish_all_widgets
tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample0]
tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample1]
tests/test_visual_audit_0136.py::test_wide_wishes_and_existing_identity_are_preserved[sample0]
tests/test_visual_audit_0136.py::test_wide_wishes_and_existing_identity_are_preserved[sample1]
tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past]
tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Metroid Fusion]
tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Zelda: A Link to the Past]
tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Metroid Fusion]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Zelda: A Link to the Past]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample0-Metroid Fusion]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Zelda: A Link to the Past]
tests/test_visual_status_0135.py::test_visual_c_five_statuses_highlight_current_without_rewriting_legacy[sample1-Metroid Fusion]
tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Zelda: A Link to the Past]
tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Metroid Fusion]
tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Zelda: A Link to the Past]
tests/test_wiki_0135.py::test_wiki_parentheses_and_written_dates[Metroid Fusion]
tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample0]
tests/test_window_controls_0137.py::test_window_controls_use_regular_window_close_and_restore[sample1]
tests/test_window_controls_0137.py::test_native_hit_regions_preserve_resize_and_caption_controls
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-False]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-True]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-False]
tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-True]
tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample0]
tests/test_wish_platform_filter_0137.py::test_wish_platform_dropdown_filters_families_without_changing_games[sample1]
tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample0]
tests/test_wish_platform_filter_0137.py::test_empty_platform_filter_keeps_controls_and_clear_action[sample1]
tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample0]
tests/test_wish_spacing_0137.py::test_offer_link_follows_discount_without_large_fixed_gap[sample1]
tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample0]
tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample1]
tests/test_wish_time_0136.py::test_nullable_legacy_ownership_flag_agrees_with_collection
tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample0]
tests/test_wishes_0135.py::test_wish_maximum_and_columns[sample1]
tests/test_wishlist_prices.py::test_prices_use_visible_brl_not_internal_dollar_values_and_keep_links
tests/test_wishlist_prices.py::test_prices_cache_failure_keeps_last_good_price
tests/test_wishlist_prices.py::test_wishlist_has_no_owned_status_and_is_excluded_from_owned_statistics
tests/test_wishlist_prices.py::test_heatmap_uses_real_daily_sessions_and_has_calendar_tooltips
tests/test_wishlist_prices.py::test_wishlist_logos_titles_and_prices_share_fixed_alignment
tests/test_wishlist_prices.py::test_artwork_cache_rejects_gif

752 tests collected in 1.01s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## remaining-failures-isolated

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art",
    "tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd",
    "tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794854105.7497194,
  "exit_code": 1,
  "elapsed": 1.557476282119751
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections -q -p no:cacheprovider
```

stdout integral — 6745 bytes; SHA-256 a8d02ee8da422b014adbdddfc5c7a077eb331016d5f6c8ef587e55a792ffb327:

````text
.F.FFF                                                                   [100%]
=================================== FAILURES ===================================
____________ test_wishes_fill_columns_with_square_art[sample0-1920] ____________

ui = (<checkpoint.window.MainWindow(0x299267b0) at 0x7fec44452340>, 1)
app = <PySide6.QtWidgets.QApplication(0x294304d0) at 0x7fec44823d00>
width = 1920

    @pytest.mark.parametrize('width',[1280,1920])
    def test_wishes_fill_columns_with_square_art(ui,app,width):
        from checkpoint.collection_views import WishGrid,WishLogo,WishCard
        w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
        w.resize(width,800);w.navigate(2)
        for _ in range(4):app.processEvents()
        grid=w.pages[2].findChild(WishGrid);card=grid.findChild(WishCard);art=card.findChild(WishLogo)
>       assert art.width()==art.height() and 280<=card.width()<=360
E       assert (226 == 226 and 280 <= 258)
E        +  where 226 = <built-in method width of WishLogo object at 0x7fec440b8b80>()
E        +    where <built-in method width of WishLogo object at 0x7fec440b8b80> = <checkpoint.collection_views.WishLogo(0x297440e0, name="wishLogo") at 0x7fec440b8b80>.width
E        +  and   226 = <built-in method height of WishLogo object at 0x7fec440b8b80>()
E        +    where <built-in method height of WishLogo object at 0x7fec440b8b80> = <checkpoint.collection_views.WishLogo(0x297440e0, name="wishLogo") at 0x7fec440b8b80>.height
E        +  and   258 = <built-in method width of WishCard object at 0x7fec440a41c0>()
E        +    where <built-in method width of WishCard object at 0x7fec440a41c0> = <checkpoint.collection_views.WishCard(0x29a74430, name="panel") at 0x7fec440a41c0>.width

tests/test_layout_0134.py:32: AssertionError
____________ test_wishes_fill_columns_with_square_art[sample1-1920] ____________

ui = (<checkpoint.window.MainWindow(0x29de5b20) at 0x7fec443e4e80>, 1)
app = <PySide6.QtWidgets.QApplication(0x294304d0) at 0x7fec44823d00>
width = 1920

    @pytest.mark.parametrize('width',[1280,1920])
    def test_wishes_fill_columns_with_square_art(ui,app,width):
        from checkpoint.collection_views import WishGrid,WishLogo,WishCard
        w,i=ui;w.library.set_setting(f'collection.unowned.{i}',True)
        with w.library.sql:w.library.sql.execute('INSERT INTO wishlist(game_id,target_cents) VALUES(?,0)',(i,))
        w.resize(width,800);w.navigate(2)
        for _ in range(4):app.processEvents()
        grid=w.pages[2].findChild(WishGrid);card=grid.findChild(WishCard);art=card.findChild(WishLogo)
>       assert art.width()==art.height() and 280<=card.width()<=360
E       assert (226 == 226 and 280 <= 258)
E        +  where 226 = <built-in method width of WishLogo object at 0x7fec440bbd80>()
E        +    where <built-in method width of WishLogo object at 0x7fec440bbd80> = <checkpoint.collection_views.WishLogo(0x29ab6c20, name="wishLogo") at 0x7fec440bbd80>.width
E        +  and   226 = <built-in method height of WishLogo object at 0x7fec440bbd80>()
E        +    where <built-in method height of WishLogo object at 0x7fec440bbd80> = <checkpoint.collection_views.WishLogo(0x29ab6c20, name="wishLogo") at 0x7fec440bbd80>.height
E        +  and   258 = <built-in method width of WishCard object at 0x7fec44033e00>()
E        +    where <built-in method width of WishCard object at 0x7fec44033e00> = <checkpoint.collection_views.WishCard(0x29f399a0, name="panel") at 0x7fec44033e00>.width

tests/test_layout_0134.py:32: AssertionError
___________________ test_sidebar_and_page_bounds_at_full_hd ____________________

library = <checkpoint.library.Library object at 0x7fec44011100>
app = <PySide6.QtWidgets.QApplication(0x294304d0) at 0x7fec44823d00>

    def test_sidebar_and_page_bounds_at_full_hd(library,app):
        library.save_game({'title':'Layout'})
        window=MainWindow(library);window.resize(1920,1080);window.show()
        for page in range(6):
            window.navigate(page);app.processEvents()
            assert window.add_button.isVisible()==(page in (0,1))
            sidebar=window.centralWidget().findChild(__import__('PySide6.QtWidgets',fromlist=['QWidget']).QWidget,'sidebar')
            assert sidebar.x()==0
>           assert window.header_widget.width()<=1392
E           assert 1674 <= 1392
E            +  where 1674 = <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fec43f2ed00>()
E            +    where <built-in method width of PySide6.QtWidgets.QWidget object at 0x7fec43f2ed00> = <PySide6.QtWidgets.QWidget(0x29d530f0) at 0x7fec43f2ed00>.width
E            +      where <PySide6.QtWidgets.QWidget(0x29d530f0) at 0x7fec43f2ed00> = <checkpoint.window.MainWindow(0x29619550) at 0x7fec43f3f600>.header_widget

tests/test_layout_regressions_025.py:34: AssertionError
____________ test_home_has_reference_hero_cta_and_personal_sections ____________

library = <checkpoint.library.Library object at 0x7fec4a4d72c0>
app = <PySide6.QtWidgets.QApplication(0x294304d0) at 0x7fec44823d00>

    def test_home_has_reference_hero_cta_and_personal_sections(library,app):
        identity=library.save_game({'title':'Meu jogo','status':'Jogando'})
        from datetime import datetime,timezone
        with library.sql:library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid) VALUES(?,?,'interrupted',123)",(identity,datetime.now(timezone.utc).isoformat()))
        window=MainWindow(library);window.show();app.processEvents()
        from checkpoint.home_components import RecentArtwork
        assert len(window.pages[0].findChildren(RecentArtwork))==1
        cta=next(button for button in window.pages[0].findChildren(QPushButton) if button.text()=='Continuar jogando')
        labels=[label.text() for label in window.pages[0].findChildren(QLabel)]
>       assert 'Últimos jogos abertos' in labels and 'Resumo da semana' in labels and 'Memórias recentes' in labels
E       AssertionError: assert ('Últimos jogos abertos' in ['Últimas sessões', 'Jogando', 'Última vez: hoje, 15:35', 'Tempo total: 0h00min', 'Resumo da semana', '', ...])

tests/test_reference_layout_0128.py:28: AssertionError
=========================== short test summary info ============================
FAILED tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample0-1920]
FAILED tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art[sample1-1920]
FAILED tests/test_layout_regressions_025.py::test_sidebar_and_page_bounds_at_full_hd
FAILED tests/test_reference_layout_0128.py::test_home_has_reference_hero_cta_and_personal_sections
4 failed, 2 passed in 1.14s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## approved-expectations-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_layout_0134.py",
    "tests/test_layout_regressions_025.py",
    "tests/test_reference_layout_0128.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794854454.815175,
  "exit_code": 0,
  "elapsed": 10.817580938339233
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_layout_0134.py tests/test_layout_regressions_025.py tests/test_reference_layout_0128.py -q -p no:cacheprovider
```

stdout integral — 100 bytes; SHA-256 dab4205c9e7dc529f5f9e4f161ea023695810f64f4c2734a3edaeec45592b661:

````text
....................                                                     [100%]
20 passed in 10.41s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-linux-approved

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794854510.0943675,
  "exit_code": 0,
  "elapsed": 580.495945930481
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 912 bytes; SHA-256 6bed33f8d665c9457277ad2bd3bdff323dd08128b4346398739bab6bb36fb0fd:

````text
........................................................................ [  9%]
........................................................................ [ 19%]
........................................................................ [ 28%]
........................................................................ [ 38%]
........................................................................ [ 47%]
........................................................................ [ 57%]
........................................................................ [ 67%]
........................................................................ [ 76%]
........................................................................ [ 86%]
........................................................................ [ 95%]
................................                                         [100%]
752 passed in 577.63s (0:09:37)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## verification-prepublish

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "/workspace/work/evidence-0139/verify_0139.py"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1794855089.536504,
  "exit_code": 0,
  "elapsed": 0.456249475479126
}
```

Comando:

```sh
/workspace/work/venv/bin/python /workspace/work/evidence-0139/verify_0139.py
```

stdout integral — 1211 bytes; SHA-256 81188e467bbb4ecb74af25ac6919e93e0c75497343e0041e97181adfa30371a3:

````text
{
  "version": "0.1.39",
  "schema": 4,
  "protected_bytes_equal": [
    "tests/test_save_lifecycle.py",
    "checkpoint/worker.py",
    "checkpoint/enrichment.py",
    "checkpoint/game_import.py",
    "checkpoint/completion_queue.py",
    "checkpoint/quick_add.py",
    "tests/test_visual_0132.py",
    "checkpoint/database.py",
    "checkpoint/elevation.py",
    "checkpoint/windows_frame.py"
  ],
  "ImageDialog_prefix_equal": true,
  "workflows_unchanged": true,
  "assets_unchanged": true,
  "eight_palettes_equal": true,
  "legacy_test_assertions_equal": [
    "tests/test_complete_layout.py",
    "tests/test_elevation_0137.py",
    "tests/test_isolated_operations.py",
    "tests/test_launch_0135.py",
    "tests/test_local_rom_0137.py",
    "tests/test_memories_0135.py",
    "tests/test_sessions_0135.py",
    "tests/test_ui_review_lifecycle_0136.py"
  ],
  "bootstrap_main_ast_equal": true,
  "captures": [
    {
      "folder": "revisao-final",
      "count": 27,
      "dpr": [
        1.0
      ]
    },
    {
      "folder": "dpi-150",
      "count": 20,
      "dpr": [
        1.5
      ]
    },
    {
      "folder": "dpi-200",
      "count": 20,
      "dpr": [
        2.0
      ]
    }
  ]
}
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

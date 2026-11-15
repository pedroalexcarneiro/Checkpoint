# Testes da rodada 0.1.36 — saídas integrais

Linux, Python 3.12.14; dados isolados em /tmp, Qt offscreen. Adaptadores controlados não validam conta autenticada nem Windows real. Mídia pessoal recebida permanece fora do repositório.

## antes-06-04

UTC: 2026-11-15T15:51:28.584968+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_capture_0135.py", "tests/test_banner_render_0135.py", "tests/test_banner_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........                                                                 [100%]
8 passed in 0.82s

```

stderr integral:
```text

```

Código de saída: 0

## depois-06

UTC: 2026-11-15T15:52:49.868668+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_capture_0135.py", "tests/test_capture_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
..........                                                               [100%]
10 passed in 0.53s

```

stderr integral:
```text

```

Código de saída: 0

## antes-04-geometria

UTC: 2026-11-15T15:54:31.206745+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_resize_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFFFFFF                                                                 [100%]
=================================== FAILURES ===================================
___ test_detail_repeated_resize_contains_entire_banner[sample0-False-shape0] ___

ui = (<checkpoint.window.MainWindow(0x1ba6ec70) at 0x7fb77438b180>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/f31e03171fbf432b8bdf2bb47bee58c4'), shape = (1200, 250)
wish = False

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
        if wish:w.library.add_wish(i)
        for initial in [(1280,800),(1920,1080)]:
            w.resize(*initial);w.detail(i)
            for size in [(1920,1080),(1280,800),(1600,900),(1280,800)]:
                w.resize(*size)
                for _ in range(4):app.processEvents()
>               hero=w.detail_page.findChild(Hero);r=hero.banner_rect()
                                                     ^^^^^^^^^^^^^^^^
E               AttributeError: 'Hero' object has no attribute 'banner_rect'

tests/test_banner_resize_0136.py:20: AttributeError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___ test_detail_repeated_resize_contains_entire_banner[sample0-False-shape1] ___

ui = (<checkpoint.window.MainWindow(0x1bd1a0b0) at 0x7fb773f27100>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/df20ae891a3b410f92dbbc906513dcc8'), shape = (600, 400)
wish = False

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
        if wish:w.library.add_wish(i)
        for initial in [(1280,800),(1920,1080)]:
            w.resize(*initial);w.detail(i)
            for size in [(1920,1080),(1280,800),(1600,900),(1280,800)]:
                w.resize(*size)
                for _ in range(4):app.processEvents()
>               hero=w.detail_page.findChild(Hero);r=hero.banner_rect()
                                                     ^^^^^^^^^^^^^^^^
E               AttributeError: 'Hero' object has no attribute 'banner_rect'

tests/test_banner_resize_0136.py:20: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0] ____

ui = (<checkpoint.window.MainWindow(0x1b985d80) at 0x7fb7741e37c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/6a662b7c8d4844dda753707ab93db1b9'), shape = (1200, 250)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1] ____

ui = (<checkpoint.window.MainWindow(0x1bf063e0) at 0x7fb773f927c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/c5e6b82b1e744c198e7e9051330501ac'), shape = (600, 400)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-False-shape0] ___

ui = (<checkpoint.window.MainWindow(0x1c2c0280) at 0x7fb773f03c80>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/78bd2ee053164945a1cfc325810e48f5'), shape = (1200, 250)
wish = False

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
        if wish:w.library.add_wish(i)
        for initial in [(1280,800),(1920,1080)]:
            w.resize(*initial);w.detail(i)
            for size in [(1920,1080),(1280,800),(1600,900),(1280,800)]:
                w.resize(*size)
                for _ in range(4):app.processEvents()
>               hero=w.detail_page.findChild(Hero);r=hero.banner_rect()
                                                     ^^^^^^^^^^^^^^^^
E               AttributeError: 'Hero' object has no attribute 'banner_rect'

tests/test_banner_resize_0136.py:20: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-False-shape1] ___

ui = (<checkpoint.window.MainWindow(0x1bf0bc60) at 0x7fb773f01280>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/9d9a197f95334b28ad95b11aa80fad9b'), shape = (600, 400)
wish = False

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
        if wish:w.library.add_wish(i)
        for initial in [(1280,800),(1920,1080)]:
            w.resize(*initial);w.detail(i)
            for size in [(1920,1080),(1280,800),(1600,900),(1280,800)]:
                w.resize(*size)
                for _ in range(4):app.processEvents()
>               hero=w.detail_page.findChild(Hero);r=hero.banner_rect()
                                                     ^^^^^^^^^^^^^^^^
E               AttributeError: 'Hero' object has no attribute 'banner_rect'

tests/test_banner_resize_0136.py:20: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0] ____

ui = (<checkpoint.window.MainWindow(0x1bcf9ff0) at 0x7fb77432a7c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/68380cd7ca9d4056973acb89eb84a3e9'), shape = (1200, 250)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1] ____

ui = (<checkpoint.window.MainWindow(0x1bca20e0) at 0x7fb77a2529c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x1b833ff0) at 0x7fb774317140>
folder = PosixPath('/tmp/6245fa7f3f08465a9f760bf14adb15a0'), shape = (600, 400)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
=========================== short test summary info ============================
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-False-shape1]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-False-shape1]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1]
8 failed in 0.92s

```

stderr integral:
```text

```

Código de saída: 1

## depois-04

UTC: 2026-11-15T15:54:46.132547+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_render_0135.py", "tests/test_banner_resize_0136.py", "tests/test_banner_0135.py", "tests/test_banner_fallback_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
....FF..FF....                                                           [100%]
=================================== FAILURES ===================================
___ test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0] ____

ui = (<checkpoint.window.MainWindow(0x3170ca70) at 0x7f9ce9bcac80>, 1)
app = <PySide6.QtWidgets.QApplication(0x31319150) at 0x7f9cf2449700>
folder = PosixPath('/tmp/6566537dd6084c6d8701d00c5d1bbf3c'), shape = (1200, 250)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1] ____

ui = (<checkpoint.window.MainWindow(0x31390450) at 0x7f9cf231c300>, 1)
app = <PySide6.QtWidgets.QApplication(0x31319150) at 0x7f9cf2449700>
folder = PosixPath('/tmp/732eb21ece364ed68a998617a072448e'), shape = (600, 400)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0] ____

ui = (<checkpoint.window.MainWindow(0x31717d50) at 0x7f9cec677700>, 1)
app = <PySide6.QtWidgets.QApplication(0x31319150) at 0x7f9cf2449700>
folder = PosixPath('/tmp/a848b160449e487280ba0b45b48c109e'), shape = (1200, 250)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
___ test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1] ____

ui = (<checkpoint.window.MainWindow(0x31360b50) at 0x7f9ce9eb4680>, 1)
app = <PySide6.QtWidgets.QApplication(0x31319150) at 0x7f9cf2449700>
folder = PosixPath('/tmp/a2d0787231f0471cb642c189fee55680'), shape = (600, 400)
wish = True

    @pytest.mark.parametrize('shape',[(1200,250),(600,400)])
    @pytest.mark.parametrize('wish',[False,True])
    def test_detail_repeated_resize_contains_entire_banner(ui,app,folder,shape,wish):
        w,i=ui
        im=QImage(*shape,QImage.Format_RGB32);im.fill(QColor('#0033cc'))
        p=QPainter(im);p.fillRect(0,0,shape[0],20,QColor('yellow'));p.fillRect(0,shape[1]-20,shape[0],20,QColor('magenta'));p.end()
        path=folder/'banner.png';im.save(str(path));g=w.library.get(i)
        w.library.save_game({'title':g['title'],'banner':str(path),'description':'Descrição externa'},i)
>       if wish:w.library.add_wish(i)
                ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Library' object has no attribute 'add_wish'

tests/test_banner_resize_0136.py:14: AttributeError
=========================== short test summary info ============================
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample0-True-shape1]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape0]
FAILED tests/test_banner_resize_0136.py::test_detail_repeated_resize_contains_entire_banner[sample1-True-shape1]
4 failed, 10 passed in 1.40s

```

stderr integral:
```text

```

Código de saída: 1

## depois-04-corrigido

UTC: 2026-11-15T15:55:11.701504+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_render_0135.py", "tests/test_banner_resize_0136.py", "tests/test_banner_0135.py", "tests/test_banner_fallback_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
..............                                                           [100%]
14 passed in 1.70s

```

stderr integral:
```text

```

Código de saída: 0

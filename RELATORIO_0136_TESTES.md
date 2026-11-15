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

## antes-02-03

UTC: 2026-11-15T15:55:34.660105+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_prices_0135.py", "tests/test_price_display_official.py", "tests/test_prices_0129.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...........                                                              [100%]
11 passed in 0.95s

```

stderr integral:
```text

```

Código de saída: 0

## antes-02-03-novos

UTC: 2026-11-15T15:56:32.705010+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFFFF                                                                   [100%]
=================================== FAILURES ===================================
_ test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Zelda Phantom Hourglass-Nintendo DS] _

library = <checkpoint.library.Library object at 0x7f0d68421c40>
title = 'Zelda Phantom Hourglass', platform = 'Nintendo DS'

    @pytest.mark.parametrize('title,platform',[('Zelda Phantom Hourglass','Nintendo DS'),('Metroid Dread','Nintendo Switch')])
    def test_non_pc_never_uses_steam_cache_or_calls_pc_provider(library,title,platform):
        i=library.save_game({'title':title,'platform':platform})
        library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','42'));library.sql.commit()
        previous={'lowest':1200,'current_kind':'retail','currency':'BRL'};library.set_setting(f'prices.ggdeals.{i}',previous)
        class Provider:
            def prices(self,*a,**k):raise AssertionError('Não consultar preço PC para console')
>       assert selected_quote(library,i).get('lowest') is None
E       AssertionError: assert 1200 is None
E        +  where 1200 = <built-in method get of dict object at 0x7f0d6846a780>('lowest')
E        +    where <built-in method get of dict object at 0x7f0d6846a780> = {'lowest': 1200, 'current_kind': 'retail', 'currency': 'BRL', 'current': 1200, ...}.get
E        +      where {'lowest': 1200, 'current_kind': 'retail', 'currency': 'BRL', 'current': 1200, ...} = selected_quote(<checkpoint.library.Library object at 0x7f0d68421c40>, 1)

tests/test_price_integrity_0136.py:14: AssertionError
_ test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Metroid Dread-Nintendo Switch] _

library = <checkpoint.library.Library object at 0x7f0d68421cd0>
title = 'Metroid Dread', platform = 'Nintendo Switch'

    @pytest.mark.parametrize('title,platform',[('Zelda Phantom Hourglass','Nintendo DS'),('Metroid Dread','Nintendo Switch')])
    def test_non_pc_never_uses_steam_cache_or_calls_pc_provider(library,title,platform):
        i=library.save_game({'title':title,'platform':platform})
        library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','42'));library.sql.commit()
        previous={'lowest':1200,'current_kind':'retail','currency':'BRL'};library.set_setting(f'prices.ggdeals.{i}',previous)
        class Provider:
            def prices(self,*a,**k):raise AssertionError('Não consultar preço PC para console')
>       assert selected_quote(library,i).get('lowest') is None
E       AssertionError: assert 1200 is None
E        +  where 1200 = <built-in method get of dict object at 0x7f0d684938c0>('lowest')
E        +    where <built-in method get of dict object at 0x7f0d684938c0> = {'lowest': 1200, 'current_kind': 'retail', 'currency': 'BRL', 'current': 1200, ...}.get
E        +      where {'lowest': 1200, 'current_kind': 'retail', 'currency': 'BRL', 'current': 1200, ...} = selected_quote(<checkpoint.library.Library object at 0x7f0d68421cd0>, 1)

tests/test_price_integrity_0136.py:14: AssertionError
______ test_discount_requires_same_offer_and_confirmed_context[Portal 2] _______

library = <checkpoint.library.Library object at 0x7f0d684238c0>
title = 'Portal 2'

    @pytest.mark.parametrize('title',['Portal 2','Hades II'])
    def test_discount_requires_same_offer_and_confirmed_context(library,title):
        i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)));library.sql.commit()
        quote={'lowest':6000,'retail':6000,'currency':'BRL','original':10000,'discount':40,'historical':1000,'current_kind':'retail','offers':[{'cents':6000,'original':10000,'kind':'retail','shop':'Loja','url':'https://gg.deals/br/redirect/store/'}]}
        library.set_setting(f'prices.ggdeals.{i}',quote)
        assert selected_quote(library,i).get('discount') is None
        quote['offer_context']={'platform':'PC','steam':str(i)};library.set_setting(f'prices.ggdeals.{i}',quote)
>       assert selected_quote(library,i)['discount']==40
E       assert None == 40

tests/test_price_integrity_0136.py:26: AssertionError
______ test_discount_requires_same_offer_and_confirmed_context[Hades II] _______

library = <checkpoint.library.Library object at 0x7f0d684239e0>
title = 'Hades II'

    @pytest.mark.parametrize('title',['Portal 2','Hades II'])
    def test_discount_requires_same_offer_and_confirmed_context(library,title):
        i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)));library.sql.commit()
        quote={'lowest':6000,'retail':6000,'currency':'BRL','original':10000,'discount':40,'historical':1000,'current_kind':'retail','offers':[{'cents':6000,'original':10000,'kind':'retail','shop':'Loja','url':'https://gg.deals/br/redirect/store/'}]}
        library.set_setting(f'prices.ggdeals.{i}',quote)
        assert selected_quote(library,i).get('discount') is None
        quote['offer_context']={'platform':'PC','steam':str(i)};library.set_setting(f'prices.ggdeals.{i}',quote)
>       assert selected_quote(library,i)['discount']==40
E       assert None == 40

tests/test_price_integrity_0136.py:26: AssertionError
____________________ test_discount_sort_and_keyshop_policy _____________________

library = <checkpoint.library.Library object at 0x7f0d68423e90>

    def test_discount_sort_and_keyshop_policy(library):
        ids=[]
        for n,title in enumerate(['Portal 2','Hades II','Sem oferta']):
            i=library.save_game({'title':title});ids.append(i)
            library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam',str(i)))
            library.set_setting(f'prices.ggdeals.{i}',{'currency':'BRL','retail':6000,'keyshop':2000 if n else 4000,'offer_context':{'platform':'PC','steam':str(i)},'offers':[] if n==2 else [{'kind':'retail','cents':6000,'original':10000 if n==0 else 8000,'shop':'Oficial','url':'https://gg.deals/br/redirect/retail/'},{'kind':'keyshop','cents':2000 if n else 4000,'original':10000,'shop':'Keys','url':'https://gg.deals/br/redirect/keys/'}]})
>       assert [g['id'] for g in wishlist_order(library,library.games(),'discount')]==ids
E       assert [2, 1, 3] == [1, 2, 3]
E         
E         At index 0 diff: 2 != 1
E         Use -v to get more diff

tests/test_price_integrity_0136.py:39: AssertionError
____________ test_comparison_has_reason_instead_of_bare_unavailable ____________

library = <checkpoint.library.Library object at 0x7f0d6850cf80>
app = <PySide6.QtWidgets.QApplication(0x20f26290) at 0x7f0d6849d6c0>

    def test_comparison_has_reason_instead_of_bare_unavailable(library,app):
        for title,platform in [('Portal 2','PC'),('Zelda','Nintendo DS')]:
            i=library.save_game({'title':title,'platform':platform});frame=comparison(SimpleNamespace(library=library),library.get(i))
            labels=[l.text() for l in frame.findChildren(QLabel)]
>           assert 'Sem preço salvo' in labels and 'Indisponível' not in labels
E           assert ('Sem preço salvo' in ['Preços atuais', '<a href="https://gg.deals/">Preços: GG.deals</a>', 'Sem ID da Steam para consulta', 'Lojas oficiais', 'Indisponível', 'Lojas de chaves', ...])

tests/test_price_integrity_0136.py:48: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
=========================== short test summary info ============================
FAILED tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Zelda Phantom Hourglass-Nintendo DS]
FAILED tests/test_price_integrity_0136.py::test_non_pc_never_uses_steam_cache_or_calls_pc_provider[Metroid Dread-Nintendo Switch]
FAILED tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Portal 2]
FAILED tests/test_price_integrity_0136.py::test_discount_requires_same_offer_and_confirmed_context[Hades II]
FAILED tests/test_price_integrity_0136.py::test_discount_sort_and_keyshop_policy
FAILED tests/test_price_integrity_0136.py::test_comparison_has_reason_instead_of_bare_unavailable
6 failed in 0.22s

```

stderr integral:
```text

```

Código de saída: 1

## depois-02-03

UTC: 2026-11-15T15:57:19.867382+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0135.py", "tests/test_price_display_official.py", "tests/test_prices_0129.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.................                                                        [100%]
17 passed in 0.99s

```

stderr integral:
```text

```

Código de saída: 0

## depois-02-03-final

UTC: 2026-11-15T15:58:03.724807+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0135.py", "tests/test_price_display_official.py", "tests/test_prices_0129.py", "tests/test_wishlist_prices.py", "tests/test_time_prices_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
......F.....................                                             [100%]
=================================== FAILURES ===================================
___________ test_discount_visible_only_for_offer_and_rounds_half_up ____________

library = <checkpoint.library.Library object at 0x7f2c421b4740>
app = <PySide6.QtWidgets.QApplication(0x19ba2280) at 0x7f2c41e802c0>

    def test_discount_visible_only_for_offer_and_rounds_half_up(library,app):
        from checkpoint.price_view import price_summary
        i=library.save_game({'title':'Portal 2'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
        quote={'currency':'BRL','retail':9950,'offer_context':{'platform':'PC','steam':'620'},'offers':[{'kind':'retail','cents':9950,'original':10000,'shop':'Loja','url':'https://gg.deals/br/redirect/shop/'}]}
        library.set_setting(f'prices.ggdeals.{i}',quote)
        labels=price_summary(library,library.get(i)).findChildren(QLabel)
>       assert any(l.text()=='-1%' for l in labels)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_price_integrity_0136.py:58: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f2c421b5de0>

>   assert any(l.text()=='-1%' for l in labels)
               ^^^^^^^^
E   RuntimeError: Internal C++ object (PySide6.QtWidgets.QLabel) already deleted.

tests/test_price_integrity_0136.py:58: RuntimeError
=========================== short test summary info ============================
FAILED tests/test_price_integrity_0136.py::test_discount_visible_only_for_offer_and_rounds_half_up
1 failed, 27 passed in 4.24s

```

stderr integral:
```text

```

Código de saída: 1

## antes-07-08

UTC: 2026-11-15T15:58:35.904720+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_0136.py", "tests/test_ui_polish.py::test_statistics_chart_uses_library_totals", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text

==================================== ERRORS ====================================
________________ ERROR collecting tests/test_statistics_0136.py ________________
ImportError while importing test module '/workspace/work/Checkpoint/tests/test_statistics_0136.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_statistics_0136.py:4: in <module>
    from checkpoint.statistics_periods import period_bounds,period_stats
E   ModuleNotFoundError: No module named 'checkpoint.statistics_periods'
=========================== short test summary info ============================
ERROR tests/test_statistics_0136.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.24s

```

stderr integral:
```text

```

Código de saída: 2

## depois-02-03-verificado

UTC: 2026-11-15T15:59:58.029430+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0135.py", "tests/test_price_display_official.py", "tests/test_prices_0129.py", "tests/test_wishlist_prices.py", "tests/test_time_prices_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
............................                                             [100%]
28 passed in 3.83s

```

stderr integral:
```text

```

Código de saída: 0

## depois-07-08

UTC: 2026-11-15T16:00:48.021630+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_0136.py", "tests/test_ui_polish.py", "tests/test_wishlist_prices.py", "tests/test_library.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....................                                                    [100%]
21 passed in 2.38s

```

stderr integral:
```text

```

Código de saída: 0

## depois-07-08-final

UTC: 2026-11-15T16:02:38.717145+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_0136.py", "tests/test_ui_polish.py", "tests/test_wishlist_prices.py", "tests/test_library.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
......................                                                   [100%]
22 passed in 2.32s

```

stderr integral:
```text

```

Código de saída: 0

## antes-09

UTC: 2026-11-15T16:03:19.510725+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_visible_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_________ test_genres_and_completions_are_directly_available[sample0] __________

ui = (<checkpoint.window.MainWindow(0x249f6880) at 0x7f3035cffa80>, 1)
app = <PySide6.QtWidgets.QApplication(0x24866ad0) at 0x7f3035e9ba00>

    def test_genres_and_completions_are_directly_available(ui,app):
        w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'genre':'Aventura','status':'Concluído'},i)
        w.navigate(4);app.processEvents()
>       assert not any(b.text()=='Mais estatísticas' for b in w.pages[4].findChildren(QToolButton))
E       assert not True
E        +  where True = any(<generator object test_genres_and_completions_are_directly_available.<locals>.<genexpr> at 0x7f303583d560>)

tests/test_statistics_visible_0136.py:8: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_________ test_genres_and_completions_are_directly_available[sample1] __________

ui = (<checkpoint.window.MainWindow(0x24b13540) at 0x7f3035cff840>, 1)
app = <PySide6.QtWidgets.QApplication(0x24866ad0) at 0x7f3035e9ba00>

    def test_genres_and_completions_are_directly_available(ui,app):
        w,i=ui;w.library.save_game({'title':w.library.get(i)['title'],'genre':'Aventura','status':'Concluído'},i)
        w.navigate(4);app.processEvents()
>       assert not any(b.text()=='Mais estatísticas' for b in w.pages[4].findChildren(QToolButton))
E       assert not True
E        +  where True = any(<generator object test_genres_and_completions_are_directly_available.<locals>.<genexpr> at 0x7f30357ef1d0>)

tests/test_statistics_visible_0136.py:8: AssertionError
=========================== short test summary info ============================
FAILED tests/test_statistics_visible_0136.py::test_genres_and_completions_are_directly_available[sample0]
FAILED tests/test_statistics_visible_0136.py::test_genres_and_completions_are_directly_available[sample1]
2 failed in 0.37s

```

stderr integral:
```text

```

Código de saída: 1

## depois-09

UTC: 2026-11-15T16:03:30.215215+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_visible_0136.py", "tests/test_statistics_0136.py", "tests/test_ui_polish.py::test_statistics_chart_uses_library_totals", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
..........                                                               [100%]
10 passed in 1.38s

```

stderr integral:
```text

```

Código de saída: 0

## antes-10-11

UTC: 2026-11-15T16:03:31.654636+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_cover_preview_0135.py", "tests/test_card_layout.py", "tests/test_service_logo_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.............                                                            [100%]
13 passed in 1.38s

```

stderr integral:
```text

```

Código de saída: 0

## depois-09-calor-ajustado

UTC: 2026-11-15T16:04:29.889393+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_visible_0136.py", "tests/test_statistics_0136.py", "tests/test_ui_polish.py::test_statistics_chart_uses_library_totals", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
..........                                                               [100%]
10 passed in 1.46s

```

stderr integral:
```text

```

Código de saída: 0

## depois-10

UTC: 2026-11-15T16:06:09.031017+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_cover_preview_0135.py", "tests/test_card_layout.py", "tests/test_settings_0135.py", "tests/test_settings_space_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.......................                                                  [100%]
23 passed in 2.72s

```

stderr integral:
```text

```

Código de saída: 0

## antes-lista-mais-jogados

UTC: 2026-11-15T16:07:26.066784+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
____________ test_top_list_logo_name_and_time_are_separate[sample0] ____________

ui = (<checkpoint.window.MainWindow(0x417402a0) at 0x7f7ca0673980>, 1)
app = <PySide6.QtWidgets.QApplication(0x41678ac0) at 0x7f7ca650a200>
folder = PosixPath('/tmp/0112c6f73a77423da77480fcb3a04a3e')

    def test_top_list_logo_name_and_time_are_separate(ui,app,folder):
        w,i=ui
        for n,title in enumerate(['Portal 2','Metroid Fusion com um nome longo '*10]):
            path=folder/f'logo{n}.png';im=QImage(300,100,QImage.Format_RGB32);im.fill(QColor('cyan' if n else 'yellow'));im.save(str(path))
            identity=w.library.save_game({'title':title,'logo':str(path)})
            start=datetime.now(timezone.utc)-timedelta(hours=4)
            w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,?,?,'finished')",(identity,start.isoformat(),3600+n*600))
        w.library.sql.commit()
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(4)
            for _ in range(4):app.processEvents()
>           rows=w.pages[4].findChildren(QWidget,'statisticsGameRow');assert len(rows)==2
                                                                      ^^^^^^^^^^^^^^^^^^^
E           assert 0 == 2
E            +  where 0 = len([])

tests/test_statistics_list_0136.py:18: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____________ test_top_list_logo_name_and_time_are_separate[sample1] ____________

ui = (<checkpoint.window.MainWindow(0x41968220) at 0x7f7ca0673900>, 1)
app = <PySide6.QtWidgets.QApplication(0x41678ac0) at 0x7f7ca650a200>
folder = PosixPath('/tmp/7620c5456c5b438da7c2121f97de22cd')

    def test_top_list_logo_name_and_time_are_separate(ui,app,folder):
        w,i=ui
        for n,title in enumerate(['Portal 2','Metroid Fusion com um nome longo '*10]):
            path=folder/f'logo{n}.png';im=QImage(300,100,QImage.Format_RGB32);im.fill(QColor('cyan' if n else 'yellow'));im.save(str(path))
            identity=w.library.save_game({'title':title,'logo':str(path)})
            start=datetime.now(timezone.utc)-timedelta(hours=4)
            w.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,?,?,'finished')",(identity,start.isoformat(),3600+n*600))
        w.library.sql.commit()
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(4)
            for _ in range(4):app.processEvents()
>           rows=w.pages[4].findChildren(QWidget,'statisticsGameRow');assert len(rows)==2
                                                                      ^^^^^^^^^^^^^^^^^^^
E           assert 0 == 2
E            +  where 0 = len([])

tests/test_statistics_list_0136.py:18: AssertionError
=========================== short test summary info ============================
FAILED tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample0]
FAILED tests/test_statistics_list_0136.py::test_top_list_logo_name_and_time_are_separate[sample1]
2 failed in 0.39s

```

stderr integral:
```text

```

Código de saída: 1

## depois-lista-mais-jogados

UTC: 2026-11-15T16:07:51.756958+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_statistics_0136.py", "tests/test_statistics_visible_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...........                                                              [100%]
11 passed in 1.55s

```

stderr integral:
```text

```

Código de saída: 0

## depois-11

UTC: 2026-11-15T16:08:47.808087+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_service_logo_0135.py", "tests/test_service_optical_0136.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
..F......                                                                [100%]
=================================== FAILURES ===================================
_________ test_steam_white_mark_optically_centered_and_asset_unchanged _________

app = <PySide6.QtWidgets.QApplication(0xf414550) at 0x7fcc44f60a80>

    def test_steam_white_mark_optically_centered_and_asset_unchanged(app):
        path=Path('checkpoint/assets/services/steam.ico')
        import subprocess
        original=subprocess.check_output(['git','show','818ec80a492a29936782ddb3a43eecaf3ef996e3:checkpoint/assets/services/steam.ico'])
        assert sha256(path.read_bytes()).digest()==sha256(original).digest()
        image=service_icon('Steam').toImage()
        points=[(x,y) for y in range(48) for x in range(48) if min(image.pixelColor(x,y).getRgb()[:3])>180]
        assert points
        x=sum(p[0] for p in points)/len(points);y=sum(p[1] for p in points)/len(points)
>       assert abs(x-23.5)<.6 and abs(y-23.5)<.6
E       assert (0.6153846153846168 < 0.6)
E        +  where 0.6153846153846168 = abs((22.884615384615383 - 23.5))

tests/test_service_optical_0136.py:15: AssertionError
=========================== short test summary info ============================
FAILED tests/test_service_optical_0136.py::test_steam_white_mark_optically_centered_and_asset_unchanged
1 failed, 8 passed in 1.06s

```

stderr integral:
```text

```

Código de saída: 1

## depois-11-medida-final

UTC: 2026-11-15T16:09:40.159979+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_service_logo_0135.py", "tests/test_service_optical_0136.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.........                                                                [100%]
9 passed in 0.98s

```

stderr integral:
```text

```

Código de saída: 0

## antes-01

UTC: 2026-11-15T16:12:00.383576+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_time_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_ test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample0] _

ui = (<checkpoint.window.MainWindow(0x1fdc6390) at 0x7f8394d3b840>, 1)
app = <PySide6.QtWidgets.QApplication(0x1fd61cd0) at 0x7f8394eaec80>

    def test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time(ui,app):
        w,i=ui;lib=w.library
        lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-11-10T12:00:00Z',8100,'finished')",(i,));lib.sql.commit()
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM play_sessions')]
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        card=w.pages[2].findChild(WishCard)
>       assert not any(l.text()=='2h15min' for l in card.findChildren(QLabel))
E       assert not True
E        +  where True = any(<generator object test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time.<locals>.<genexpr> at 0x7f839485dd80>)

tests/test_wish_time_0136.py:13: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample1] _

ui = (<checkpoint.window.MainWindow(0x1ffb5a90) at 0x7f8394d0e740>, 1)
app = <PySide6.QtWidgets.QApplication(0x1fd61cd0) at 0x7f8394eaec80>

    def test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time(ui,app):
        w,i=ui;lib=w.library
        lib.sql.execute("INSERT INTO play_sessions(game_id,started_at,duration_seconds,state) VALUES(?,'2026-11-10T12:00:00Z',8100,'finished')",(i,));lib.sql.commit()
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM play_sessions')]
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        card=w.pages[2].findChild(WishCard)
>       assert not any(l.text()=='2h15min' for l in card.findChildren(QLabel))
E       assert not True
E        +  where True = any(<generator object test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time.<locals>.<genexpr> at 0x7f839343cfb0>)

tests/test_wish_time_0136.py:13: AssertionError
=========================== short test summary info ============================
FAILED tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample0]
FAILED tests/test_wish_time_0136.py::test_wish_exclusive_and_owned_keep_sessions_but_only_library_shows_time[sample1]
2 failed in 0.37s

```

stderr integral:
```text

```

Código de saída: 1

## depois-lista-tempo-destacado

UTC: 2026-11-15T16:12:34.109108+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_statistics_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.........                                                                [100%]
9 passed in 1.51s

```

stderr integral:
```text

```

Código de saída: 0

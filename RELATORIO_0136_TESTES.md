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

## depois-01

UTC: 2026-11-15T16:13:22.345488+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_time_0136.py", "tests/test_wishlist_prices.py", "tests/test_registration_0128.py", "tests/test_time_0135.py", "tests/test_time_prices_0134.py", "tests/test_complete_layout.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.............................                                            [100%]
29 passed in 4.33s

```

stderr integral:
```text

```

Código de saída: 0

## antes-10-espacamento

UTC: 2026-11-15T16:14:16.991215+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_______ test_cover_outline_spacing_is_equal_at_both_edges[sample0-size0] _______

ui = (<checkpoint.window.MainWindow(0x36bea2f0) at 0x7ff99defd540>, 1)
app = <PySide6.QtWidgets.QApplication(0x36a7d060) at 0x7ff99dea1900>
size = (1280, 800)

    @pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
    def test_cover_outline_spacing_is_equal_at_both_edges(ui,app,size):
     w,i=ui;w.resize(*size);w.navigate(5)
     for _ in range(5):app.processEvents()
     preview=w.pages[5].findChild(CoverSizeChoices);rects=preview.cover_rects()
     left=rects[0].left();right=preview.width()-rects[-1].right()
     gaps=[b.left()-a.right() for a,b in zip(rects,rects[1:])]
>    assert abs(left-right)<=1
E    assert 31.288888888888962 <= 1
E     +  where 31.288888888888962 = abs((66.62222222222222 - 35.33333333333326))

tests/test_cover_preview_0135.py:48: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_______ test_cover_outline_spacing_is_equal_at_both_edges[sample0-size1] _______

ui = (<checkpoint.window.MainWindow(0x370634d0) at 0x7ff9972ca780>, 1)
app = <PySide6.QtWidgets.QApplication(0x36a7d060) at 0x7ff99dea1900>
size = (1920, 1080)

    @pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
    def test_cover_outline_spacing_is_equal_at_both_edges(ui,app,size):
     w,i=ui;w.resize(*size);w.navigate(5)
     for _ in range(5):app.processEvents()
     preview=w.pages[5].findChild(CoverSizeChoices);rects=preview.cover_rects()
     left=rects[0].left();right=preview.width()-rects[-1].right()
     gaps=[b.left()-a.right() for a,b in zip(rects,rects[1:])]
>    assert abs(left-right)<=1
E    assert 31.28888888888872 <= 1
E     +  where 31.28888888888872 = abs((130.6222222222222 - 99.33333333333348))

tests/test_cover_preview_0135.py:48: AssertionError
_______ test_cover_outline_spacing_is_equal_at_both_edges[sample1-size0] _______

ui = (<checkpoint.window.MainWindow(0x36a0db50) at 0x7ff99defd280>, 1)
app = <PySide6.QtWidgets.QApplication(0x36a7d060) at 0x7ff99dea1900>
size = (1280, 800)

    @pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
    def test_cover_outline_spacing_is_equal_at_both_edges(ui,app,size):
     w,i=ui;w.resize(*size);w.navigate(5)
     for _ in range(5):app.processEvents()
     preview=w.pages[5].findChild(CoverSizeChoices);rects=preview.cover_rects()
     left=rects[0].left();right=preview.width()-rects[-1].right()
     gaps=[b.left()-a.right() for a,b in zip(rects,rects[1:])]
>    assert abs(left-right)<=1
E    assert 31.288888888888962 <= 1
E     +  where 31.288888888888962 = abs((66.62222222222222 - 35.33333333333326))

tests/test_cover_preview_0135.py:48: AssertionError
_______ test_cover_outline_spacing_is_equal_at_both_edges[sample1-size1] _______

ui = (<checkpoint.window.MainWindow(0x374f4320) at 0x7ff9972fe3c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x36a7d060) at 0x7ff99dea1900>
size = (1920, 1080)

    @pytest.mark.parametrize('size',[(1280,800),(1920,1080)])
    def test_cover_outline_spacing_is_equal_at_both_edges(ui,app,size):
     w,i=ui;w.resize(*size);w.navigate(5)
     for _ in range(5):app.processEvents()
     preview=w.pages[5].findChild(CoverSizeChoices);rects=preview.cover_rects()
     left=rects[0].left();right=preview.width()-rects[-1].right()
     gaps=[b.left()-a.right() for a,b in zip(rects,rects[1:])]
>    assert abs(left-right)<=1
E    assert 31.28888888888872 <= 1
E     +  where 31.28888888888872 = abs((130.6222222222222 - 99.33333333333348))

tests/test_cover_preview_0135.py:48: AssertionError
=========================== short test summary info ============================
FAILED tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size0]
FAILED tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample0-size1]
FAILED tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size0]
FAILED tests/test_cover_preview_0135.py::test_cover_outline_spacing_is_equal_at_both_edges[sample1-size1]
4 failed in 0.73s

```

stderr integral:
```text

```

Código de saída: 1

## depois-10-espacamento

UTC: 2026-11-15T16:14:46.018689+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_cover_preview_0135.py", "tests/test_card_layout.py", "tests/test_settings_space_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....................                                                    [100%]
21 passed in 2.64s

```

stderr integral:
```text

```

Código de saída: 0

## antes-05

UTC: 2026-11-15T16:15:13.324255+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_description_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
______ test_home_does_not_paint_description_but_detail_keeps_it[sample0] _______

ui = (<checkpoint.window.MainWindow(0x1dfec7c0) at 0x7fd5b6836240>, 1)
app = <PySide6.QtWidgets.QApplication(0x1df282c0) at 0x7fd5b6998380>

    def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
        w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
        w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
        w.navigate(0);app.processEvents();hero=w.pages[0].findChild(Hero)
        assert hero and hero.findChildren(QPushButton)
        before=hero.grab().toImage();hero.game={**hero.game,'description':''};hero.update();app.processEvents()
>       assert before==hero.grab().toImage()
E       assert <PySide6.QtGui.QImage(QSize(746, 300),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2984,sizeInBytes=895200) at 0x7fd5b638bcc0> == <PySide6.QtGui.QImage(QSize(746, 300),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2984,sizeInBytes=895200) at 0x7fd5b6683040>
E        +  where <PySide6.QtGui.QImage(QSize(746, 300),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=2984,sizeInBytes=895200) at 0x7fd5b6683040> = <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7fd5b66e32c0>()
E        +    where <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7fd5b66e32c0> = <PySide6.QtGui.QPixmap(QSize(746, 300),depth=32,devicePixelRatio=1,cacheKey=0x1d00000004) at 0x7fd5b66e32c0>.toImage
E        +      where <PySide6.QtGui.QPixmap(QSize(746, 300),depth=32,devicePixelRatio=1,cacheKey=0x1d00000004) at 0x7fd5b66e32c0> = <built-in method grab of Hero object at 0x7fd5b639ea00>()
E        +        where <built-in method grab of Hero object at 0x7fd5b639ea00> = <checkpoint.ui_components.Hero(0x1e695110, name="gameHero") at 0x7fd5b639ea00>.grab

tests/test_home_description_0136.py:12: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_home_does_not_paint_description_but_detail_keeps_it[sample1] _______

ui = (<checkpoint.window.MainWindow(0x1e4cc030) at 0x7fd5b63ac380>, 1)
app = <PySide6.QtWidgets.QApplication(0x1df282c0) at 0x7fd5b6998380>

    def test_home_does_not_paint_description_but_detail_keeps_it(ui,app):
        w,i=ui;game=w.library.get(i);description='Descrição externa que deve permanecer somente em Sobre o jogo. '*4
        w.library.save_game({'title':game['title'],'description':description,'status':'Jogando'},i)
        w.navigate(0);app.processEvents();hero=w.pages[0].findChild(Hero)
        assert hero and hero.findChildren(QPushButton)
        before=hero.grab().toImage();hero.game={**hero.game,'description':''};hero.update();app.processEvents()
>       assert before==hero.grab().toImage()
E       assert <PySide6.QtGui.QImage(QSize(1146, 327),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=4584,sizeInBytes=1498968) at 0x7fd5b6683c40> == <PySide6.QtGui.QImage(QSize(1146, 327),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=4584,sizeInBytes=1498968) at 0x7fd5b639ccc0>
E        +  where <PySide6.QtGui.QImage(QSize(1146, 327),format=QImage::Format_ARGB32_Premultiplied,depth=32,devicePixelRatio=1,bytesPerLine=4584,sizeInBytes=1498968) at 0x7fd5b639ccc0> = <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7fd5b63af040>()
E        +    where <built-in method toImage of PySide6.QtGui.QPixmap object at 0x7fd5b63af040> = <PySide6.QtGui.QPixmap(QSize(1146, 327),depth=32,devicePixelRatio=1,cacheKey=0x2700000004) at 0x7fd5b63af040>.toImage
E        +      where <PySide6.QtGui.QPixmap(QSize(1146, 327),depth=32,devicePixelRatio=1,cacheKey=0x2700000004) at 0x7fd5b63af040> = <built-in method grab of Hero object at 0x7fd5b64107c0>()
E        +        where <built-in method grab of Hero object at 0x7fd5b64107c0> = <checkpoint.ui_components.Hero(0x1e3aba10, name="gameHero") at 0x7fd5b64107c0>.grab

tests/test_home_description_0136.py:12: AssertionError
=========================== short test summary info ============================
FAILED tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample0]
FAILED tests/test_home_description_0136.py::test_home_does_not_paint_description_but_detail_keeps_it[sample1]
2 failed in 0.37s

```

stderr integral:
```text

```

Código de saída: 1

## depois-05

UTC: 2026-11-15T16:15:40.189701+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_home_description_0136.py", "tests/test_home_0129.py", "tests/test_banner_render_0135.py", "tests/test_banner_resize_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...............                                                          [100%]
15 passed in 1.94s

```

stderr integral:
```text

```

Código de saída: 0

## antes-12-auditoria

UTC: 2026-11-15T16:16:15.202105+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_audit_0136.py", "tests/test_mockup_exclusions_0135.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF............                                                           [100%]
=================================== FAILURES ===================================
___________ test_long_memory_titles_keep_delete_inside_card[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x327153c0) at 0x7f70f7ecf1c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x32678110) at 0x7f70f7e4f240>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grid=w.pages[3].findChild(CardGrid,'memoriesGrid');assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
>               assert title.geometry().right()<delete.geometry().left()
E               assert 639 < 0
E                +  where 639 = <built-in method right of PySide6.QtCore.QRect object at 0x7f70f7a97200>()
E                +    where <built-in method right of PySide6.QtCore.QRect object at 0x7f70f7a97200> = PySide6.QtCore.QRect(0, 0, 640, 480).right
E                +      where PySide6.QtCore.QRect(0, 0, 640, 480) = <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f70f7abe1c0>()
E                +        where <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f70f7abe1c0> = <PySide6.QtWidgets.QPushButton(0x32d96650, name="activityLink") at 0x7f70f7abe1c0>.geometry
E                +  and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f70f7a85f00>()
E                +    where <built-in method left of PySide6.QtCore.QRect object at 0x7f70f7a85f00> = PySide6.QtCore.QRect(0, 0, 34, 34).left
E                +      where PySide6.QtCore.QRect(0, 0, 34, 34) = <built-in method geometry of IconButton object at 0x7f70f7abe480>()
E                +        where <built-in method geometry of IconButton object at 0x7f70f7abe480> = <checkpoint.design_system.IconButton(0x32d96500, name="iconButton") at 0x7f70f7abe480>.geometry

tests/test_visual_audit_0136.py:20: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___________ test_long_memory_titles_keep_delete_inside_card[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x32d82550) at 0x7f70f7ecf100>, 1)
app = <PySide6.QtWidgets.QApplication(0x32678110) at 0x7f70f7e4f240>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grid=w.pages[3].findChild(CardGrid,'memoriesGrid');assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
>               assert title.geometry().right()<delete.geometry().left()
E               assert 639 < 0
E                +  where 639 = <built-in method right of PySide6.QtCore.QRect object at 0x7f70f7a96ec0>()
E                +    where <built-in method right of PySide6.QtCore.QRect object at 0x7f70f7a96ec0> = PySide6.QtCore.QRect(0, 0, 640, 480).right
E                +      where PySide6.QtCore.QRect(0, 0, 640, 480) = <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f70f7a21900>()
E                +        where <built-in method geometry of PySide6.QtWidgets.QPushButton object at 0x7f70f7a21900> = <PySide6.QtWidgets.QPushButton(0x32dd9950, name="activityLink") at 0x7f70f7a21900>.geometry
E                +  and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f70f7a85f00>()
E                +    where <built-in method left of PySide6.QtCore.QRect object at 0x7f70f7a85f00> = PySide6.QtCore.QRect(0, 0, 34, 34).left
E                +      where PySide6.QtCore.QRect(0, 0, 34, 34) = <built-in method geometry of IconButton object at 0x7f70f7ad42c0>()
E                +        where <built-in method geometry of IconButton object at 0x7f70f7ad42c0> = <checkpoint.design_system.IconButton(0x32aa1f30, name="iconButton") at 0x7f70f7ad42c0>.geometry

tests/test_visual_audit_0136.py:20: AssertionError
=========================== short test summary info ============================
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample0]
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample1]
2 failed, 12 passed in 2.27s

```

stderr integral:
```text

```

Código de saída: 1

## depois-12

UTC: 2026-11-15T16:17:35.585588+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_audit_0136.py", "tests/test_mockup_exclusions_0135.py", "tests/test_settings_0135.py", "tests/test_complete_layout.py", "tests/test_memories_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF..............................                                         [100%]
=================================== FAILURES ===================================
___________ test_long_memory_titles_keep_delete_inside_card[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x21a43a90) at 0x7f641c5f1880>, 1)
app = <PySide6.QtWidgets.QApplication(0x21987a50) at 0x7f64224e1bc0>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grid=w.pages[3].findChild(CardGrid,'memoriesGrid');assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
>               assert title.geometry().right()<delete.geometry().left()
E               assert 639 < 0
E                +  where 639 = <built-in method right of PySide6.QtCore.QRect object at 0x7f641c4551c0>()
E                +    where <built-in method right of PySide6.QtCore.QRect object at 0x7f641c4551c0> = PySide6.QtCore.QRect(0, 0, 640, 480).right
E                +      where PySide6.QtCore.QRect(0, 0, 640, 480) = <built-in method geometry of ElidedAction object at 0x7f641c1177c0>()
E                +        where <built-in method geometry of ElidedAction object at 0x7f641c1177c0> = <checkpoint.ui_components.ElidedAction(0x220fd590, name="activityLink") at 0x7f641c1177c0>.geometry
E                +  and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f641c456c80>()
E                +    where <built-in method left of PySide6.QtCore.QRect object at 0x7f641c456c80> = PySide6.QtCore.QRect(0, 0, 34, 34).left
E                +      where PySide6.QtCore.QRect(0, 0, 34, 34) = <built-in method geometry of IconButton object at 0x7f641c117b40>()
E                +        where <built-in method geometry of IconButton object at 0x7f641c117b40> = <checkpoint.design_system.IconButton(0x221089f0, name="iconButton") at 0x7f641c117b40>.geometry

tests/test_visual_audit_0136.py:20: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
___________ test_long_memory_titles_keep_delete_inside_card[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x21ca75c0) at 0x7f641c5f19c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x21987a50) at 0x7f64224e1bc0>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grid=w.pages[3].findChild(CardGrid,'memoriesGrid');assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
>               assert title.geometry().right()<delete.geometry().left()
E               assert 639 < 0
E                +  where 639 = <built-in method right of PySide6.QtCore.QRect object at 0x7f641c0f11c0>()
E                +    where <built-in method right of PySide6.QtCore.QRect object at 0x7f641c0f11c0> = PySide6.QtCore.QRect(0, 0, 640, 480).right
E                +      where PySide6.QtCore.QRect(0, 0, 640, 480) = <built-in method geometry of ElidedAction object at 0x7f642250b600>()
E                +        where <built-in method geometry of ElidedAction object at 0x7f642250b600> = <checkpoint.ui_components.ElidedAction(0x21f7ef20, name="activityLink") at 0x7f642250b600>.geometry
E                +  and   0 = <built-in method left of PySide6.QtCore.QRect object at 0x7f641c1455c0>()
E                +    where <built-in method left of PySide6.QtCore.QRect object at 0x7f641c1455c0> = PySide6.QtCore.QRect(0, 0, 34, 34).left
E                +      where PySide6.QtCore.QRect(0, 0, 34, 34) = <built-in method geometry of IconButton object at 0x7f641c0f3ec0>()
E                +        where <built-in method geometry of IconButton object at 0x7f641c0f3ec0> = <checkpoint.design_system.IconButton(0x22031850, name="iconButton") at 0x7f641c0f3ec0>.geometry

tests/test_visual_audit_0136.py:20: AssertionError
=========================== short test summary info ============================
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample0]
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample1]
2 failed, 30 passed in 5.16s

```

stderr integral:
```text

```

Código de saída: 1

## diagnostico-12-grade-visivel

UTC: 2026-11-15T16:17:53.459023+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card", "-q", "-s", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
GEOMETRIA (1280, 800) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1030, 320), [(True, (327, 320)), (True, (327, 320))])]
GEOMETRIA (1920, 1080) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1388, 320), [(True, (329, 320)), (True, (329, 320))])]
.GEOMETRIA (1280, 800) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1030, 320), [(True, (327, 320)), (True, (327, 320))])]
GEOMETRIA (1920, 1080) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1388, 320), [(True, (329, 320)), (True, (329, 320))])]
.
2 passed in 0.48s

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## antes-12-corrigido-na-base

UTC: 2026-11-15T16:18:30.842703+00:00

Comando: `["bash", "-c", "cd /workspace/work/base-0136-visual && /workspace/work/venv/bin/python -m pytest tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card -q -p no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
___________ test_long_memory_titles_keep_delete_inside_card[sample0] ___________

ui = (<checkpoint.window.MainWindow(0x24ee5e00) at 0x7f5922f41000>, 1)
app = <PySide6.QtWidgets.QApplication(0x24f4bfb0) at 0x7f5922f1ba80>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grids=w.pages[3].findChildren(CardGrid,'memoriesGrid')
            print('GEOMETRIA',size,[(g.isVisible(),g.size().toTuple(),[(c.isVisible(),c.size().toTuple()) for c in g.cards]) for g in grids])
            grid=next(g for g in grids if g.isVisible());assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
                assert title.geometry().right()<delete.geometry().left()
>               assert title.toolTip() and title.accessibleName()
E               assert ('')
E                +  where '' = <built-in method toolTip of PySide6.QtWidgets.QPushButton object at 0x7f5922a50980>()
E                +    where <built-in method toolTip of PySide6.QtWidgets.QPushButton object at 0x7f5922a50980> = <PySide6.QtWidgets.QPushButton(0x2560f860, name="activityLink") at 0x7f5922a50980>.toolTip

tests/test_visual_audit_0136.py:23: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
----------------------------- Captured stdout call -----------------------------
GEOMETRIA (1280, 800) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1030, 320), [(True, (327, 320)), (True, (327, 320))])]
___________ test_long_memory_titles_keep_delete_inside_card[sample1] ___________

ui = (<checkpoint.window.MainWindow(0x25219c30) at 0x7f5922f41080>, 1)
app = <PySide6.QtWidgets.QApplication(0x24f4bfb0) at 0x7f5922f1ba80>

    def test_long_memory_titles_keep_delete_inside_card(ui,app):
        w,i=ui
        for title in ['Portal 2 com título longo '*12,'Metroid Fusion com título longo '*12]:
            identity=w.library.save_game({'title':title});w.library.add_diary(identity,'Nota curta do usuário.')
        for size in [(1280,800),(1920,1080)]:
            w.resize(*size);w.navigate(3)
            for _ in range(5):app.processEvents()
            grids=w.pages[3].findChildren(CardGrid,'memoriesGrid')
            print('GEOMETRIA',size,[(g.isVisible(),g.size().toTuple(),[(c.isVisible(),c.size().toTuple()) for c in g.cards]) for g in grids])
            grid=next(g for g in grids if g.isVisible());assert len(grid.cards)==2
            for card in grid.cards:
                delete=card.findChild(IconButton)
                assert card.rect().contains(delete.geometry())
                title=card.findChild(QPushButton,'activityLink')
                assert title.geometry().right()<delete.geometry().left()
>               assert title.toolTip() and title.accessibleName()
E               assert ('')
E                +  where '' = <built-in method toolTip of PySide6.QtWidgets.QPushButton object at 0x7f5922acad80>()
E                +    where <built-in method toolTip of PySide6.QtWidgets.QPushButton object at 0x7f5922acad80> = <PySide6.QtWidgets.QPushButton(0x2560a460, name="activityLink") at 0x7f5922acad80>.toolTip

tests/test_visual_audit_0136.py:23: AssertionError
----------------------------- Captured stdout call -----------------------------
GEOMETRIA (1280, 800) [(False, (640, 480), [(False, (308, 480)), (False, (308, 480))]), (True, (1030, 320), [(True, (327, 320)), (True, (327, 320))])]
=========================== short test summary info ============================
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample0]
FAILED tests/test_visual_audit_0136.py::test_long_memory_titles_keep_delete_inside_card[sample1]
2 failed in 0.41s

```

stderr integral:
```text

```

Código de saída: 1

## depois-12-corrigido

UTC: 2026-11-15T16:18:36.013639+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_audit_0136.py", "tests/test_mockup_exclusions_0135.py", "tests/test_settings_0135.py", "tests/test_complete_layout.py", "tests/test_memories_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
................................                                         [100%]
32 passed in 4.62s

```

stderr integral:
```text

```

Código de saída: 0

## depois-desconto-cor-tema

UTC: 2026-11-15T16:19:20.615099+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0129.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...........                                                              [100%]
11 passed in 0.87s

```

stderr integral:
```text

```

Código de saída: 0

## escala-150-geometria

UTC: 2026-11-15T16:20:57.366357+00:00

Comando: `["/usr/bin/env", "QT_SCALE_FACTOR=1.5", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_visual_audit_0136.py", "tests/test_service_optical_0136.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
......F......                                                            [100%]
=================================== FAILURES ===================================
_________ test_steam_white_mark_optically_centered_and_asset_unchanged _________

app = <PySide6.QtWidgets.QApplication(0x87d5830) at 0x7f5a8cfd28c0>

    def test_steam_white_mark_optically_centered_and_asset_unchanged(app):
        path=Path('checkpoint/assets/services/steam.ico')
        assert sha256(path.read_bytes()).hexdigest()=='9f890a9debcdfccc339149a7943be9aff9e4c9203c2fa37d5671a5b2c88503ad'
        image=service_icon('Steam').toImage()
        points=[(x,y) for y in range(48) for x in range(48) if min(image.pixelColor(x,y).getRgb()[:3])>180]
        assert points
        x=sum(p[0] for p in points)/len(points);y=sum(p[1] for p in points)/len(points)
>       assert abs(x-23.5)<.6 and abs(y-23.5)<.6
E       assert (0.84375 < 0.6)
E        +  where 0.84375 = abs((24.34375 - 23.5))

tests/test_service_optical_0136.py:13: AssertionError
=========================== short test summary info ============================
FAILED tests/test_service_optical_0136.py::test_steam_white_mark_optically_centered_and_asset_unchanged
1 failed, 12 passed in 3.10s

```

stderr integral:
```text

```

Código de saída: 1

## smoke-fonte

UTC: 2026-11-15T16:21:42.811761+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "checkpoint.app", "--smoke-test", "--data-dir", "/tmp/checkpoint-0136-smoke-01"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## smoke-cadastro

UTC: 2026-11-15T16:21:43.787086+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "checkpoint.app", "--save-smoke-test", "--data-dir", "/tmp/checkpoint-0136-save-smoke-01"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## escala-150-corrigida

UTC: 2026-11-15T16:21:43.802135+00:00

Comando: `["/usr/bin/env", "QT_SCALE_FACTOR=1.5", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_visual_audit_0136.py", "tests/test_service_optical_0136.py", "tests/test_service_logo_0135.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...............                                                          [100%]
15 passed in 2.77s

```

stderr integral:
```text

```

Código de saída: 0

## escala-200

UTC: 2026-11-15T16:21:46.229088+00:00

Comando: `["/usr/bin/env", "QT_SCALE_FACTOR=2", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_visual_audit_0136.py", "tests/test_service_optical_0136.py", "tests/test_service_logo_0135.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...............                                                          [100%]
15 passed in 2.15s

```

stderr integral:
```text

```

Código de saída: 0

## antes-banner-proporcao-exata

UTC: 2026-11-15T16:23:53.817165+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_aspect_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_ test_banner_area_matches_original_aspect_at_every_window_size[False-Portal 2-shape0] _

app = <PySide6.QtWidgets.QApplication(0x54f8400) at 0x7f9b74a30140>
folder = PosixPath('/tmp/1ca2e6b23d9e49b4afcca317730f5ad4'), title = 'Portal 2'
shape = (1920, 620), detail = False

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
>               assert abs(hero.height()-expected)<=1
E               assert 58 <= 1
E                +  where 58 = abs((300 - 242))
E                +    where 300 = <built-in method height of Hero object at 0x7f9b74a87d40>()
E                +      where <built-in method height of Hero object at 0x7f9b74a87d40> = <checkpoint.ui_components.Hero(0x54a0c40, name="gameHero") at 0x7f9b74a87d40>.height

tests/test_banner_aspect_0136.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
Fontconfig error: No writable cache directories
_ test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1] _

app = <PySide6.QtWidgets.QApplication(0x54f8400) at 0x7f9b74a30140>
folder = PosixPath('/tmp/74a02440d1f64c3fb8533a13dc1eeb5d'), title = 'Hades'
shape = (1920, 500), detail = False

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
>               assert abs(hero.height()-expected)<=1
E               assert 105 <= 1
E                +  where 105 = abs((300 - 195))
E                +    where 300 = <built-in method height of Hero object at 0x7f9b71a64e00>()
E                +      where <built-in method height of Hero object at 0x7f9b71a64e00> = <checkpoint.ui_components.Hero(0x55cffb0, name="gameHero") at 0x7f9b71a64e00>.height

tests/test_banner_aspect_0136.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_ test_banner_area_matches_original_aspect_at_every_window_size[True-Portal 2-shape0] _

app = <PySide6.QtWidgets.QApplication(0x54f8400) at 0x7f9b74a30140>
folder = PosixPath('/tmp/f80d7721449f4467ac33da97b94ba2ea'), title = 'Portal 2'
shape = (1920, 620), detail = True

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
>               assert abs(hero.height()-expected)<=1
E               assert 2 <= 1
E                +  where 2 = abs((240 - 242))
E                +    where 240 = <built-in method height of Hero object at 0x7f9b71a58b00>()
E                +      where <built-in method height of Hero object at 0x7f9b71a58b00> = <checkpoint.ui_components.Hero(0x56c1020, name="gameHero") at 0x7f9b71a58b00>.height

tests/test_banner_aspect_0136.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_ test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1] _

app = <PySide6.QtWidgets.QApplication(0x54f8400) at 0x7f9b74a30140>
folder = PosixPath('/tmp/add8c1e1594740d58080b48effbac85f'), title = 'Hades'
shape = (1920, 500), detail = True

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
>               assert abs(hero.height()-expected)<=1
E               assert 45 <= 1
E                +  where 45 = abs((240 - 195))
E                +    where 240 = <built-in method height of Hero object at 0x7f9b74aaebc0>()
E                +      where <built-in method height of Hero object at 0x7f9b74aaebc0> = <checkpoint.ui_components.Hero(0x569fde0, name="gameHero") at 0x7f9b74aaebc0>.height

tests/test_banner_aspect_0136.py:16: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Portal 2-shape0]
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1]
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Portal 2-shape0]
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1]
4 failed in 0.34s

```

stderr integral:
```text

```

Código de saída: 1

## depois-banner-proporcao-exata

UTC: 2026-11-15T16:24:52.993660+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_aspect_0136.py", "tests/test_banner_resize_0136.py", "tests/test_banner_render_0135.py", "tests/test_ui_polish.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_tabs_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.F.F..........F............                                              [100%]
=================================== FAILURES ===================================
_ test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1] _

app = <PySide6.QtWidgets.QApplication(0xd40ecc0) at 0x7f5dbd7bec00>
folder = PosixPath('/tmp/3efc960698b94b548e776e61253789e4'), title = 'Hades'
shape = (1920, 500), detail = False

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
                assert abs(hero.height()-expected)<=1
                assert abs(target.left())<=1 and abs(target.top())<=1
>               assert abs(target.width()-hero.width())<=1 and abs(target.height()-hero.height())<=1
E               assert (2 <= 1)
E                +  where 2 = abs((748 - 750))
E                +    where 748 = <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd778ec0>()
E                +      where <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd778ec0> = PySide6.QtCore.QRect(1, 0, 748, 195).width
E                +    and   750 = <built-in method width of Hero object at 0x7f5dbd778cc0>()
E                +      where <built-in method width of Hero object at 0x7f5dbd778cc0> = <checkpoint.ui_components.Hero(0xd1e18f0, name="gameHero") at 0x7f5dbd778cc0>.width

tests/test_banner_aspect_0136.py:18: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
_ test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1] _

app = <PySide6.QtWidgets.QApplication(0xd40ecc0) at 0x7f5dbd7bec00>
folder = PosixPath('/tmp/afa4fece045447a3b0d2b0b26336c1d6'), title = 'Hades'
shape = (1920, 500), detail = True

    @pytest.mark.parametrize('title,shape',[('Portal 2',(1920,620)),('Hades',(1920,500))])
    @pytest.mark.parametrize('detail',[False,True])
    def test_banner_area_matches_original_aspect_at_every_window_size(app,folder,title,shape,detail):
        image=QImage(*shape,QImage.Format_RGB32);image.fill(QColor('#50a070'));path=folder/'banner.png';image.save(str(path))
        hero=Hero({'title':title,'banner':str(path)},get_theme('green'));hero.detail_mode=detail;hero.show()
        try:
            for width in [750,1026,1388,1700,1026,750]:
                hero.resize(width,hero.height())
                for _ in range(4):app.processEvents()
                expected=round(width*shape[1]/shape[0]);target=hero.banner_rect()
                assert abs(hero.height()-expected)<=1
                assert abs(target.left())<=1 and abs(target.top())<=1
>               assert abs(target.width()-hero.width())<=1 and abs(target.height()-hero.height())<=1
E               assert (2 <= 1)
E                +  where 2 = abs((748 - 750))
E                +    where 748 = <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd788140>()
E                +      where <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd788140> = PySide6.QtCore.QRect(1, 0, 748, 195).width
E                +    and   750 = <built-in method width of Hero object at 0x7f5dbd788700>()
E                +      where <built-in method width of Hero object at 0x7f5dbd788700> = <checkpoint.ui_components.Hero(0xd4dd810, name="gameHero") at 0x7f5dbd788700>.width

tests/test_banner_aspect_0136.py:18: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
___________________ test_banner_is_bounded_at_desktop_width ____________________

library = <checkpoint.library.Library object at 0x7f5dbd445a30>
app = <PySide6.QtWidgets.QApplication(0xd40ecc0) at 0x7f5dbd7bec00>
tmp_path = PosixPath('/tmp/pytest-of-agent/pytest-24/test_banner_is_bounded_at_desk0')

    def test_banner_is_bounded_at_desktop_width(library,app,tmp_path):
        image=QImage(900,240,QImage.Format_RGB32);image.fill(QColor('red'));path=tmp_path/'wide.png';image.save(str(path))
        hero=Hero({'title':'Teste','banner':str(path)},__import__('checkpoint.theme',fromlist=['get_theme']).get_theme('green'))
        hero.resize(750,300);hero.show();app.processEvents()
        assert abs(hero.height()-round(hero.width()*240/900))<=1
        assert hero.grab().toImage().pixelColor(hero.width()-20,hero.height()//2).red()>240
        hero.resize(1700,hero.height());app.processEvents()
        assert abs(hero.height()-round(hero.width()*240/900))<=1
>       assert abs(hero.banner_rect().width()-hero.width())<=1 and abs(hero.banner_rect().height()-hero.height())<=1
E       assert (2 <= 1)
E        +  where 2 = abs((1698 - 1700))
E        +    where 1698 = <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd3aa5c0>()
E        +      where <built-in method width of PySide6.QtCore.QRect object at 0x7f5dbd3aa5c0> = PySide6.QtCore.QRect(1, 0, 1698, 453).width
E        +        where PySide6.QtCore.QRect(1, 0, 1698, 453) = banner_rect()
E        +          where banner_rect = <checkpoint.ui_components.Hero(0xd5aeee0, name="gameHero") at 0x7f5dbd49d500>.banner_rect
E        +    and   1700 = <built-in method width of Hero object at 0x7f5dbd49d500>()
E        +      where <built-in method width of Hero object at 0x7f5dbd49d500> = <checkpoint.ui_components.Hero(0xd5aeee0, name="gameHero") at 0x7f5dbd49d500>.width

tests/test_ui_polish.py:17: AssertionError
----------------------------- Captured stderr call -----------------------------
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
=========================== short test summary info ============================
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[False-Hades-shape1]
FAILED tests/test_banner_aspect_0136.py::test_banner_area_matches_original_aspect_at_every_window_size[True-Hades-shape1]
FAILED tests/test_ui_polish.py::test_banner_is_bounded_at_desktop_width - ass...
3 failed, 24 passed in 2.82s

```

stderr integral:
```text

```

Código de saída: 1

## depois-banner-geometria-fracionaria

UTC: 2026-11-15T16:25:46.514759+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_aspect_0136.py", "tests/test_banner_resize_0136.py", "tests/test_banner_render_0135.py", "tests/test_ui_polish.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_tabs_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...........................                                              [100%]
27 passed in 2.76s

```

stderr integral:
```text

```

Código de saída: 0

## suite-integral-0136

UTC: 2026-11-15T16:26:44.083371+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........................................................................ [ 12%]
........................................................................ [ 24%]
........................................................................ [ 36%]
........................................................................ [ 48%]
........................................................................ [ 61%]
........................................................................ [ 73%]
........................................................................ [ 85%]
........................................................................ [ 97%]
FF............                                                           [100%]
=================================== FAILURES ===================================
_ test_visual_b_steam_has_real_asset_instead_of_initials[Zelda: A Link to the Past] _

app = <PySide6.QtWidgets.QApplication(0x2ac0a070) at 0x7f427c1b5d00>
library = <checkpoint.library.Library object at 0x7f4270e4c470>
title = 'Zelda: A Link to the Past'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_b_steam_has_real_asset_instead_of_initials(app,library,title):
     library.save_game({'title':title})
     asset=Path(checkpoint.__file__).parent/'assets/services/steam.ico'
     source=QIcon(str(asset)).pixmap(48,48).scaled(32,32,Qt.KeepAspectRatio,Qt.SmoothTransformation).toImage()
     rendered=service_icon('Steam').toImage();checked=0
     for x in range(source.width()):
      for y in range(source.height()):
       pixel=source.pixelColor(x,y)
       if pixel.alpha()==255 and min(pixel.red(),pixel.green(),pixel.blue())>220:
        actual=rendered.pixelColor(x+8,y+8)
>       assert actual==pixel
E       assert PySide6.QtGui.QColor.fromRgbF(0.082353, 0.168627, 0.286275, 1.000000) == PySide6.QtGui.QColor.fromRgbF(1.000000, 1.000000, 1.000000, 1.000000)

tests/test_visual_steam_asset_0135.py:18: AssertionError
____ test_visual_b_steam_has_real_asset_instead_of_initials[Metroid Fusion] ____

app = <PySide6.QtWidgets.QApplication(0x2ac0a070) at 0x7f427c1b5d00>
library = <checkpoint.library.Library object at 0x7f4271bf1ca0>
title = 'Metroid Fusion'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_b_steam_has_real_asset_instead_of_initials(app,library,title):
     library.save_game({'title':title})
     asset=Path(checkpoint.__file__).parent/'assets/services/steam.ico'
     source=QIcon(str(asset)).pixmap(48,48).scaled(32,32,Qt.KeepAspectRatio,Qt.SmoothTransformation).toImage()
     rendered=service_icon('Steam').toImage();checked=0
     for x in range(source.width()):
      for y in range(source.height()):
       pixel=source.pixelColor(x,y)
       if pixel.alpha()==255 and min(pixel.red(),pixel.green(),pixel.blue())>220:
        actual=rendered.pixelColor(x+8,y+8)
>       assert actual==pixel
E       assert PySide6.QtGui.QColor.fromRgbF(0.082353, 0.168627, 0.286275, 1.000000) == PySide6.QtGui.QColor.fromRgbF(1.000000, 1.000000, 1.000000, 1.000000)

tests/test_visual_steam_asset_0135.py:18: AssertionError
=========================== short test summary info ============================
FAILED tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Zelda: A Link to the Past]
FAILED tests/test_visual_steam_asset_0135.py::test_visual_b_steam_has_real_asset_instead_of_initials[Metroid Fusion]
2 failed, 588 passed in 398.91s (0:06:38)

```

stderr integral:
```text

```

Código de saída: 1

## banner-quatro-bordas-estados

UTC: 2026-11-15T16:27:28.159229+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_banner_aspect_0136.py", "tests/test_banner_resize_0136.py", "tests/test_banner_render_0135.py", "tests/test_ui_polish.py", "tests/test_home_0129.py", "tests/test_home_description_0136.py", "tests/test_tabs_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.............................                                            [100%]
29 passed in 2.91s

```

stderr integral:
```text

```

Código de saída: 0

## depois-pixels-steam-aprovados

UTC: 2026-11-15T16:28:42.754286+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_steam_asset_0135.py", "tests/test_service_optical_0136.py", "tests/test_service_logo_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....                                                                    [100%]
5 passed in 0.56s

```

stderr integral:
```text

```

Código de saída: 0

## depois-pixels-steam-150

UTC: 2026-11-15T16:28:43.630534+00:00

Comando: `["/usr/bin/env", "QT_SCALE_FACTOR=1.5", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_steam_asset_0135.py", "tests/test_service_optical_0136.py", "tests/test_service_logo_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....                                                                    [100%]
5 passed in 0.55s

```

stderr integral:
```text

```

Código de saída: 0

## antes-cache-edicao

UTC: 2026-11-15T16:30:30.490762+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FF                                                                       [100%]
=================================== FAILURES ===================================
_______ test_cached_quote_from_different_edition_is_not_shown[Portal 2] ________

library = <checkpoint.library.Library object at 0x7f4364d73a70>
title = 'Portal 2'

    @pytest.mark.parametrize('title',['Portal 2','Hades'])
    def test_cached_quote_from_different_edition_is_not_shown(library,title):
        i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
        cached={'currency':'BRL','retail':6000,'offer_context':{'platform':'PC','steam':'620'}};library.set_setting(f'prices.ggdeals.{i}',cached)
        assert selected_quote(library,i)['lowest']==6000
        library.sql.execute("UPDATE external_identifiers SET external_id='999' WHERE game_id=? AND provider='steam'",(i,));library.sql.commit()
        quote=selected_quote(library,i)
>       assert quote.get('lowest') is None and 'identidade' in quote.get('message','').lower()
E       AssertionError: assert (6000 is None)
E        +  where 6000 = <built-in method get of dict object at 0x7f4364d9b4c0>('lowest')
E        +    where <built-in method get of dict object at 0x7f4364d9b4c0> = {'currency': 'BRL', 'retail': 6000, 'offer_context': {'platform': 'PC', 'steam': '620'}, 'lowest': 6000, ...}.get

tests/test_price_integrity_0136.py:87: AssertionError
_________ test_cached_quote_from_different_edition_is_not_shown[Hades] _________

library = <checkpoint.library.Library object at 0x7f4364d73950>, title = 'Hades'

    @pytest.mark.parametrize('title',['Portal 2','Hades'])
    def test_cached_quote_from_different_edition_is_not_shown(library,title):
        i=library.save_game({'title':title,'platform':'PC'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
        cached={'currency':'BRL','retail':6000,'offer_context':{'platform':'PC','steam':'620'}};library.set_setting(f'prices.ggdeals.{i}',cached)
        assert selected_quote(library,i)['lowest']==6000
        library.sql.execute("UPDATE external_identifiers SET external_id='999' WHERE game_id=? AND provider='steam'",(i,));library.sql.commit()
        quote=selected_quote(library,i)
>       assert quote.get('lowest') is None and 'identidade' in quote.get('message','').lower()
E       AssertionError: assert (6000 is None)
E        +  where 6000 = <built-in method get of dict object at 0x7f4364dbac80>('lowest')
E        +    where <built-in method get of dict object at 0x7f4364dbac80> = {'currency': 'BRL', 'retail': 6000, 'offer_context': {'platform': 'PC', 'steam': '620'}, 'lowest': 6000, ...}.get

tests/test_price_integrity_0136.py:87: AssertionError
=========================== short test summary info ============================
FAILED tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Portal 2]
FAILED tests/test_price_integrity_0136.py::test_cached_quote_from_different_edition_is_not_shown[Hades]
2 failed in 0.20s

```

stderr integral:
```text

```

Código de saída: 1

## depois-cache-edicao

UTC: 2026-11-15T16:30:52.361442+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0135.py", "tests/test_prices_0129.py", "tests/test_price_display_official.py", "tests/test_wishlist_prices.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
...........................                                              [100%]
27 passed in 3.38s

```

stderr integral:
```text

```

Código de saída: 0

## verificacao-contratos

UTC: 2026-11-15T16:33:27.380793+00:00

Comando: `["/workspace/work/venv/bin/python", "-c", "import subprocess,hashlib;from pathlib import Path;base='818ec80a492a29936782ddb3a43eecaf3ef996e3';files=['tests/test_save_lifecycle.py','checkpoint/worker.py','checkpoint/enrichment.py','checkpoint/game_import.py','checkpoint/completion_queue.py','checkpoint/dialogs.py','checkpoint/quick_add.py','tests/test_visual_0132.py','checkpoint/assets/services/steam.ico','checkpoint/assets/services/google-drive.png','release-notes.md'];files += subprocess.check_output(['git','ls-files','.github/workflows'],text=True,encoding='utf-8').splitlines();[(print(name,hashlib.sha256(Path(name).read_bytes()).hexdigest(),'INTACTO'),None if Path(name).read_bytes()==subprocess.check_output(['git','show',base+':'+name]) else (_ for _ in ()).throw(AssertionError(name))) for name in files if Path(name).exists()];changed=subprocess.check_output(['git','diff','--name-only',base],text=True,encoding='utf-8').splitlines();[(Path(name).read_text(encoding='utf-8'),None if b'\\r' not in Path(name).read_bytes() else (_ for _ in ()).throw(AssertionError('CR em '+name))) for name in changed if Path(name).is_file()];subprocess.run(['git','diff','--check'],check=True);print('UTF-8/LF e diff --check OK; contratos e workflows intactos')"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
tests/test_save_lifecycle.py cef7190411246741cc418df6d9e9f7a8faa72343b0268079f33fc017c98069ab INTACTO
checkpoint/worker.py d5bd6ee0eb977466ba604afc06be1a29ec109aa81f306e45d98f42c6fa8a331a INTACTO
checkpoint/enrichment.py bc81557c2230f82ddaee166a2b3df237caee4d14550e5df0281b8df713f75811 INTACTO
checkpoint/game_import.py 5e82553fc7059b6530f2a9f832ac52e08ebd928964e2e57d9b8c12510d9d74ca INTACTO
checkpoint/completion_queue.py d6f66be83feb3891c65d93a6bb7ea9e728b604c024339077d44f2218cf4d70d5 INTACTO
checkpoint/dialogs.py ef86cc4b503340dd141519a4a47ab573a3a1fa373caac04f943120296747ccff INTACTO
checkpoint/quick_add.py ea3468a6aa45fef65f567e097e881a4eeb36d15a286c77a650eb2697a2c1634a INTACTO
tests/test_visual_0132.py 0f89dc3ce676756a505e80c6bb37c46c45b08c226594ea5f4737b21881e74ac3 INTACTO
checkpoint/assets/services/steam.ico 9f890a9debcdfccc339149a7943be9aff9e4c9203c2fa37d5671a5b2c88503ad INTACTO
checkpoint/assets/services/google-drive.png 72ea8d2de5e0568158cf48029cb9121564ab20c275465a65453776baf1160ebd INTACTO
.github/workflows/publish-0.1.28.yml f4679399903233c471550b751fd8b78984e812c2775e7ab908f344f5939dd547 INTACTO
.github/workflows/windows-release.yml 575522aac5608bd07b1142db96e9fc1b5860337088d1f560a6ad0852332ca4f4 INTACTO
.github/workflows/windows-ui-validation.yml 83d552e70b56a173ebbe436feab6fbd3a23c2bba2831cc34114f8b5d758232e4 INTACTO
UTF-8/LF e diff --check OK; contratos e workflows intactos

```

stderr integral:
```text

```

Código de saída: 0

## wheel-local

UTC: 2026-11-15T16:33:27.796245+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pip", "wheel", ".", "--no-deps", "--no-build-isolation", "--wheel-dir", "/workspace/work/entrega-0136/wheels"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Processing /workspace/work/Checkpoint
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: checkpoint-desktop
  Building wheel for checkpoint-desktop (pyproject.toml): started
  Building wheel for checkpoint-desktop (pyproject.toml): finished with status 'done'
  Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.36-py3-none-any.whl size=233033 sha256=0e7e6a335ce1a0d7cf1bee5facd1dc58f91af6f6d5a27c99ab0bdd97148d26dd
  Stored in directory: /tmp/pip-ephem-wheel-cache-94234t1e/wheels/83/77/53/5eb720791fc6f82eaa0f682bd5e5adf7478efb3a3363bfee14
Successfully built checkpoint-desktop

```

stderr integral:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip

```

Código de saída: 0

## geometria-final-150

UTC: 2026-11-15T16:33:29.034811+00:00

Comando: `["/usr/bin/env", "QT_SCALE_FACTOR=1.5", "/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_statistics_list_0136.py", "tests/test_visual_audit_0136.py", "tests/test_service_optical_0136.py", "tests/test_visual_steam_asset_0135.py", "tests/test_service_logo_0135.py", "tests/test_settings_0135.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.................                                                        [100%]
17 passed in 2.67s

```

stderr integral:
```text

```

Código de saída: 0

## antes-ofertas-empatadas

UTC: 2026-11-15T16:35:45.503543+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py::test_price_store_and_original_do_not_mix_tied_offers", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
F                                                                        [100%]
=================================== FAILURES ===================================
_____________ test_price_store_and_original_do_not_mix_tied_offers _____________

library = <checkpoint.library.Library object at 0x7f6504c6b260>
app = <PySide6.QtWidgets.QApplication(0x114687b0) at 0x7f6504c4cc40>

    def test_price_store_and_original_do_not_mix_tied_offers(library,app):
        from checkpoint.price_view import price_summary
        i=library.save_game({'title':'Portal 2'});library.sql.execute('INSERT INTO external_identifiers VALUES(?,?,?)',(i,'steam','620'));library.sql.commit()
        offers=[{'kind':'keyshop','cents':6000,'original':10000,'shop':'Chaves','url':'https://gg.deals/br/redirect/keys/'},
                {'kind':'retail','cents':6000,'original':None,'shop':'Oficial A','url':'https://gg.deals/br/redirect/a/'},
                {'kind':'retail','cents':6000,'original':10000,'shop':'Oficial B','url':'https://gg.deals/br/redirect/b/'}]
        library.set_setting(f'prices.ggdeals.{i}',{'currency':'BRL','retail':6000,'keyshop':6000,'offer_context':{'platform':'PC','steam':'620'},'offers':offers})
        frame=price_summary(library,library.get(i));labels=[l.text() for l in frame.findChildren(QLabel)]
>       assert 'Loja oficial · Oficial A' in labels
E       AssertionError: assert 'Loja oficial · Oficial A' in ['Menor preço atual', 'R$ 60,00', 'Loja oficial · Chaves', 'R$ 100,00', '-40%']

tests/test_price_integrity_0136.py:99: AssertionError
=========================== short test summary info ============================
FAILED tests/test_price_integrity_0136.py::test_price_store_and_original_do_not_mix_tied_offers
1 failed in 0.13s

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 1

## depois-ofertas-empatadas

UTC: 2026-11-15T16:36:01.081868+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_price_integrity_0136.py", "tests/test_prices_0129.py", "tests/test_prices_0135.py", "tests/test_price_display_official.py", "tests/test_wishlist_prices.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
............................                                             [100%]
28 passed in 2.54s

```

stderr integral:
```text

```

Código de saída: 0

## antes-posse-nula

UTC: 2026-11-15T16:37:11.159124+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_time_0136.py::test_nullable_legacy_ownership_flag_agrees_with_collection", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
F                                                                        [100%]
=================================== FAILURES ===================================
__________ test_nullable_legacy_ownership_flag_agrees_with_collection __________

library = <checkpoint.library.Library object at 0x7f81d2c36ff0>

    def test_nullable_legacy_ownership_flag_agrees_with_collection(library):
        i=library.save_game({'title':'Portal 2'})
        library.sql.execute('INSERT INTO wishlist(game_id) VALUES(?)',(i,));library.sql.commit()
        for flag,owned in [(None,False),(True,False),(False,True)]:
            library.set_setting(f'collection.unowned.{i}',flag)
            assert library.is_owned(i)==owned
>           assert (i in {g['id'] for g in library.owned_games()})==owned
E           assert (1 in {1}) == False

tests/test_wish_time_0136.py:32: AssertionError
=========================== short test summary info ============================
FAILED tests/test_wish_time_0136.py::test_nullable_legacy_ownership_flag_agrees_with_collection
1 failed in 0.14s

```

stderr integral:
```text

```

Código de saída: 1

## depois-posse-nula

UTC: 2026-11-15T16:37:41.704951+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_time_0136.py", "tests/test_wishlist_prices.py", "tests/test_registration_0128.py", "tests/test_library.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....................                                                    [100%]
21 passed in 1.87s

```

stderr integral:
```text

```

Código de saída: 0

## wheel-local-final

UTC: 2026-11-15T16:38:30.489102+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pip", "wheel", ".", "--no-deps", "--no-build-isolation", "--wheel-dir", "/workspace/work/entrega-0136/wheels"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Processing /workspace/work/Checkpoint
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: checkpoint-desktop
  Building wheel for checkpoint-desktop (pyproject.toml): started
  Building wheel for checkpoint-desktop (pyproject.toml): finished with status 'done'
  Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.36-py3-none-any.whl size=233066 sha256=213ae54d46872dc84228be08f7b75821313eac8f30b123b393f7eeda560cfa12
  Stored in directory: /tmp/pip-ephem-wheel-cache-6pkawvfs/wheels/83/77/53/5eb720791fc6f82eaa0f682bd5e5adf7478efb3a3363bfee14
Successfully built checkpoint-desktop

```

stderr integral:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip

```

Código de saída: 0

## suite-integral-final-0136

UTC: 2026-11-15T16:38:54.932407+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........................................................................ [ 12%]
........................................................................ [ 24%]
........................................................................ [ 36%]
........................................................................ [ 48%]
........................................................................ [ 60%]
........................................................................ [ 72%]
........................................................................ [ 84%]
........................................................................ [ 96%]
......................                                                   [100%]
598 passed in 414.93s (0:06:54)

```

stderr integral:
```text

```

Código de saída: 0

## instalar-wheel-isolado

UTC: 2026-11-15T16:39:56.922687+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pip", "install", "--no-deps", "--no-index", "--target", "/workspace/work/wheel-0136-installed", "/workspace/work/entrega-0136/wheels/checkpoint_desktop-0.1.36-py3-none-any.whl"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Processing /workspace/work/entrega-0136/wheels/checkpoint_desktop-0.1.36-py3-none-any.whl
Installing collected packages: checkpoint-desktop
Successfully installed checkpoint-desktop-0.1.36

```

stderr integral:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

```

Código de saída: 0

## smoke-wheel-instalado

UTC: 2026-11-15T16:39:57.617927+00:00

Comando: `["bash", "-c", "cd /workspace/work/wheel-0136-installed && /workspace/work/venv/bin/python -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-0136-wheel-smoke-01"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## smoke-wheel-cadastro

UTC: 2026-11-15T16:39:58.285073+00:00

Comando: `["bash", "-c", "cd /workspace/work/wheel-0136-installed && /workspace/work/venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-0136-wheel-save-smoke-01"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## remoto-sem-publicacao

UTC: 2026-11-15T16:41:13.618492+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.35-ajustes", "refs/heads/fix/0.1.36-ajustes", "refs/tags/v0.1.35"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
818ec80a492a29936782ddb3a43eecaf3ef996e3	refs/heads/fix/0.1.35-ajustes
df5ff41e74b36cea4e2abd160e1172f4166bf32a	refs/tags/v0.1.35

```

stderr integral:
```text

```

Código de saída: 0

## metadados-visuais

UTC: 2026-11-15T16:41:13.822218+00:00

Comando: `["/workspace/work/venv/bin/python", "-c", "from PySide6.QtWidgets import QApplication,QLabel;from PySide6.QtGui import QFontInfo;from checkpoint.theme import apply_theme;app=QApplication([]);apply_theme(app,'green');label=QLabel('Revisão visual');label.ensurePolished();screen=app.primaryScreen();print('Fonte solicitada:',label.font().family());print('Fonte resolvida:',QFontInfo(label.font()).family());print('Tamanho corpo px:',label.font().pixelSize());print('DPR:',screen.devicePixelRatio());print('DPI lógico:',screen.logicalDotsPerInch());print('Tela virtual:',screen.geometry().width(),screen.geometry().height());print('Janelas sintéticas capturadas: 1280x800 e 1920x1080 lógicos; escalas adicionais de geometria: 1.5 e 2.0')"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Fonte solicitada: Segoe UI
Fonte resolvida: OpenAI Sans
Tamanho corpo px: 14
DPR: 1.0
DPI lógico: 96.0
Tela virtual: 800 800
Janelas sintéticas capturadas: 1280x800 e 1920x1080 lógicos; escalas adicionais de geometria: 1.5 e 2.0

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## antes-hifen-sem-preco

UTC: 2026-11-15T16:42:25.991673+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_complements_0135.py", "tests/test_price_integrity_0136.py::test_comparison_has_reason_instead_of_bare_unavailable", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFFF                                                                    [100%]
=================================== FAILURES ===================================
____ test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past] _____

app = <PySide6.QtWidgets.QApplication(0x2f6ea2a0) at 0x7f4d4122f4c0>
library = <checkpoint.library.Library object at 0x7f4d4122b8f0>
title = 'Zelda: A Link to the Past'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_a_no_official_offer_has_reason(app,library,title):
     i=library.save_game({'title':title})
     with library.sql:library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
     library.set_setting(f'prices.ggdeals.{i}',{'lowest':None,'retail':None,'currency':'BRL','state':'ready','checked_at':'2026-11-14T12:00:00+00:00'})
     frame=price_summary(library,library.get(i))
     labels=[label.text() for label in frame.findChildren(QLabel)]
>    assert '-' in labels and 'Indisponível' not in labels
E    AssertionError: assert ('-' in ['Menor preço atual', 'Sem preço salvo', 'Consulta sem oferta em lojas oficiais.'])

tests/test_visual_complements_0135.py:11: AssertionError
__________ test_visual_a_no_official_offer_has_reason[Metroid Fusion] __________

app = <PySide6.QtWidgets.QApplication(0x2f6ea2a0) at 0x7f4d4122f4c0>
library = <checkpoint.library.Library object at 0x7f4d4122b8c0>
title = 'Metroid Fusion'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_a_no_official_offer_has_reason(app,library,title):
     i=library.save_game({'title':title})
     with library.sql:library.sql.execute("INSERT INTO external_identifiers VALUES(?,'steam',?)",(i,str(i)))
     library.set_setting(f'prices.ggdeals.{i}',{'lowest':None,'retail':None,'currency':'BRL','state':'ready','checked_at':'2026-11-14T12:00:00+00:00'})
     frame=price_summary(library,library.get(i))
     labels=[label.text() for label in frame.findChildren(QLabel)]
>    assert '-' in labels and 'Indisponível' not in labels
E    AssertionError: assert ('-' in ['Menor preço atual', 'Sem preço salvo', 'Consulta sem oferta em lojas oficiais.'])

tests/test_visual_complements_0135.py:11: AssertionError
__________ test_visual_a_no_id_is_explicit[Zelda: A Link to the Past] __________

app = <PySide6.QtWidgets.QApplication(0x2f6ea2a0) at 0x7f4d4122f4c0>
library = <checkpoint.library.Library object at 0x7f4d41191820>
title = 'Zelda: A Link to the Past'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_a_no_id_is_explicit(app,library,title):
     i=library.save_game({'title':title});frame=price_summary(library,library.get(i))
     labels=[label.text() for label in frame.findChildren(QLabel)]
>    assert '-' in labels and 'Sem ID da Steam para consultar ofertas.' in labels
E    AssertionError: assert ('-' in ['Menor preço atual', 'Sem preço salvo', 'Sem ID da Steam para consultar ofertas.'])

tests/test_visual_complements_0135.py:18: AssertionError
_______________ test_visual_a_no_id_is_explicit[Metroid Fusion] ________________

app = <PySide6.QtWidgets.QApplication(0x2f6ea2a0) at 0x7f4d4122f4c0>
library = <checkpoint.library.Library object at 0x7f4d4125c950>
title = 'Metroid Fusion'

    @pytest.mark.parametrize('title',['Zelda: A Link to the Past','Metroid Fusion'])
    def test_visual_a_no_id_is_explicit(app,library,title):
     i=library.save_game({'title':title});frame=price_summary(library,library.get(i))
     labels=[label.text() for label in frame.findChildren(QLabel)]
>    assert '-' in labels and 'Sem ID da Steam para consultar ofertas.' in labels
E    AssertionError: assert ('-' in ['Menor preço atual', 'Sem preço salvo', 'Sem ID da Steam para consultar ofertas.'])

tests/test_visual_complements_0135.py:18: AssertionError
____________ test_comparison_has_reason_instead_of_bare_unavailable ____________

library = <checkpoint.library.Library object at 0x7f4d4125cb90>
app = <PySide6.QtWidgets.QApplication(0x2f6ea2a0) at 0x7f4d4122f4c0>

    def test_comparison_has_reason_instead_of_bare_unavailable(library,app):
        for title,platform in [('Portal 2','PC'),('Zelda','Nintendo DS')]:
            i=library.save_game({'title':title,'platform':platform});frame=comparison(SimpleNamespace(library=library),library.get(i))
            labels=[l.text() for l in frame.findChildren(QLabel)]
>           assert '-' in labels and 'Indisponível' not in labels
E           assert ('-' in ['Preços atuais', '<a href="https://gg.deals/">Preços: GG.deals</a>', 'Menor preço atual', 'Sem preço salvo', 'Sem ID da Steam para consultar ofertas.'])

tests/test_price_integrity_0136.py:48: AssertionError
----------------------------- Captured stderr call -----------------------------
Fontconfig error: No writable cache directories
=========================== short test summary info ============================
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Zelda: A Link to the Past]
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_official_offer_has_reason[Metroid Fusion]
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Zelda: A Link to the Past]
FAILED tests/test_visual_complements_0135.py::test_visual_a_no_id_is_explicit[Metroid Fusion]
FAILED tests/test_price_integrity_0136.py::test_comparison_has_reason_instead_of_bare_unavailable
5 failed in 0.22s

```

stderr integral:
```text

```

Código de saída: 1

## depois-hifen-sem-preco

UTC: 2026-11-15T16:42:37.383835+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_visual_complements_0135.py", "tests/test_price_integrity_0136.py", "tests/test_prices_0129.py", "tests/test_time_prices_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
......................                                                   [100%]
22 passed in 1.26s

```

stderr integral:
```text

```

Código de saída: 0

## suite-definitiva-0136

UTC: 2026-11-15T16:45:36.139977+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........................................................................ [ 12%]
........................................................................ [ 24%]
........................................................................ [ 36%]
........................................................................ [ 48%]
........................................................................ [ 60%]
........................................................................ [ 72%]
........................................................................ [ 84%]
.......................................................
```

stderr integral:
```text

```

Código de saída: -15

## wheel-head-7015fef

UTC: 2026-11-15T16:46:21.973853+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pip", "wheel", ".", "--no-deps", "--no-build-isolation", "--wheel-dir", "/workspace/work/entrega-0136/wheels"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Processing /workspace/work/Checkpoint
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: checkpoint-desktop
  Building wheel for checkpoint-desktop (pyproject.toml): started
  Building wheel for checkpoint-desktop (pyproject.toml): finished with status 'done'
  Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.36-py3-none-any.whl size=233069 sha256=17bde2b571378ddb3a27aa0c8258762473312618e887f59b6b57a46c1a7acc57
  Stored in directory: /tmp/pip-ephem-wheel-cache-4lfifjxw/wheels/83/77/53/5eb720791fc6f82eaa0f682bd5e5adf7478efb3a3363bfee14
Successfully built checkpoint-desktop

```

stderr integral:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip

```

Código de saída: 0

## instalar-wheel-head-7015fef

UTC: 2026-11-15T16:46:22.488903+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pip", "install", "--upgrade", "--no-deps", "--no-index", "--target", "/workspace/work/wheel-0136-installed", "/workspace/work/entrega-0136/wheels/checkpoint_desktop-0.1.36-py3-none-any.whl"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Processing /workspace/work/entrega-0136/wheels/checkpoint_desktop-0.1.36-py3-none-any.whl
Installing collected packages: checkpoint-desktop
Successfully installed checkpoint-desktop-0.1.36

```

stderr integral:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

```

Código de saída: 0

## smoke-wheel-head-7015fef

UTC: 2026-11-15T16:46:23.197627+00:00

Comando: `["bash", "-c", "cd /workspace/work/wheel-0136-installed && /workspace/work/venv/bin/python -m checkpoint.app --smoke-test --data-dir /tmp/checkpoint-0136-head7015-smoke"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## cadastro-wheel-head-7015fef

UTC: 2026-11-15T16:46:23.872555+00:00

Comando: `["bash", "-c", "cd /workspace/work/wheel-0136-installed && /workspace/work/venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /tmp/checkpoint-0136-head7015-save-smoke"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Cadastro smoke: salvar, auxiliar, renderização e SQLite OK

```

stderr integral:
```text
Fontconfig error: No writable cache directories

```

Código de saída: 0

## correspondencia-wheel-fonte

UTC: 2026-11-15T16:49:44.871371+00:00

Comando: `["/workspace/work/venv/bin/python", "-c", "from pathlib import Path;from zipfile import ZipFile;import hashlib;root=Path('.');wheel=Path('/workspace/work/entrega-0136/wheels/checkpoint_desktop-0.1.36-py3-none-any.whl');z=ZipFile(wheel);files=[n for n in z.namelist() if n.startswith('checkpoint/') and not n.endswith('/')];assert 'checkpoint/global_hotkey.py' in files and 'checkpoint/statistics_periods.py' in files;[(None if z.read(n)==(root/n).read_bytes() else (_ for _ in ()).throw(AssertionError(n))) for n in files];print('Conteúdo do wheel idêntico ao fonte/assets:',len(files),'arquivos');print('SHA-256 wheel:',hashlib.sha256(wheel.read_bytes()).hexdigest());print('Pacote técnico local; Windows não homologado.')"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
Conteúdo do wheel idêntico ao fonte/assets: 121 arquivos
SHA-256 wheel: 17bde2b571378ddb3a27aa0c8258762473312618e887f59b6b57a46c1a7acc57
Pacote técnico local; Windows não homologado.

```

stderr integral:
```text

```

Código de saída: 0

## suite-head-7015fef-0136

UTC: 2026-11-15T16:52:25.937216+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........................................................................ [ 12%]
........................................................................ [ 24%]
........................................................................ [ 36%]
........................................................................ [ 48%]
........................................................................ [ 60%]
........................................................................ [ 72%]
........................................................................ [ 84%]
........................................................................ [ 96%]
........................                                                 [100%]
600 passed in 408.20s (0:06:48)

```

stderr integral:
```text

```

Código de saída: 0

## antes-navegacao-desejos

UTC: 2026-11-15T16:53:56.312408+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_navigation_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
______ test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-False] ______

ui = (<checkpoint.window.MainWindow(0xb765c80) at 0x7efcf178f340>, 1)
app = <PySide6.QtWidgets.QApplication(0xb6f7430) at 0x7efcf1742c80>
folder = PosixPath('/tmp/caf7ea84409c4346b27a4cc8c288d822'), has_banner = False

    @pytest.mark.parametrize('has_banner',[False,True])
    def test_open_wish_stays_in_wishes_and_does_not_acquire(ui,app,folder,has_banner):
        w,i=ui;lib=w.library
        if has_banner:
            path=folder/'banner.png';im=QImage(1920,620,QImage.Format_RGB32);im.fill(QColor('blue'));im.save(str(path));lib.save_game({'title':lib.get(i)['title'],'banner':str(path)},i)
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        before=lib.get(i);wishlist=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        card=next(c for c in w.pages[2].findChildren(WishCard) if c.isVisible())
        card.findChild(WishLogo).click();app.processEvents()
>       assert w.current_page==2 and w.nav_buttons[2].isChecked() and not w.nav_buttons[1].isChecked()
E       assert (1 == 2)
E        +  where 1 = <checkpoint.window.MainWindow(0xb765c80) at 0x7efcf178f340>.current_page

tests/test_wish_navigation_0136.py:16: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
______ test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-True] _______

ui = (<checkpoint.window.MainWindow(0xb9b8100) at 0x7efcf178f380>, 1)
app = <PySide6.QtWidgets.QApplication(0xb6f7430) at 0x7efcf1742c80>
folder = PosixPath('/tmp/b5f89f2a489b4a5e831aed16ddd1ffba'), has_banner = True

    @pytest.mark.parametrize('has_banner',[False,True])
    def test_open_wish_stays_in_wishes_and_does_not_acquire(ui,app,folder,has_banner):
        w,i=ui;lib=w.library
        if has_banner:
            path=folder/'banner.png';im=QImage(1920,620,QImage.Format_RGB32);im.fill(QColor('blue'));im.save(str(path));lib.save_game({'title':lib.get(i)['title'],'banner':str(path)},i)
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        before=lib.get(i);wishlist=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        card=next(c for c in w.pages[2].findChildren(WishCard) if c.isVisible())
        card.findChild(WishLogo).click();app.processEvents()
>       assert w.current_page==2 and w.nav_buttons[2].isChecked() and not w.nav_buttons[1].isChecked()
E       assert (1 == 2)
E        +  where 1 = <checkpoint.window.MainWindow(0xb9b8100) at 0x7efcf178f380>.current_page

tests/test_wish_navigation_0136.py:16: AssertionError
______ test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-False] ______

ui = (<checkpoint.window.MainWindow(0xbe11060) at 0x7efcf1377dc0>, 1)
app = <PySide6.QtWidgets.QApplication(0xb6f7430) at 0x7efcf1742c80>
folder = PosixPath('/tmp/63402f98052f48838ff4651689e2b04c'), has_banner = False

    @pytest.mark.parametrize('has_banner',[False,True])
    def test_open_wish_stays_in_wishes_and_does_not_acquire(ui,app,folder,has_banner):
        w,i=ui;lib=w.library
        if has_banner:
            path=folder/'banner.png';im=QImage(1920,620,QImage.Format_RGB32);im.fill(QColor('blue'));im.save(str(path));lib.save_game({'title':lib.get(i)['title'],'banner':str(path)},i)
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        before=lib.get(i);wishlist=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        card=next(c for c in w.pages[2].findChildren(WishCard) if c.isVisible())
        card.findChild(WishLogo).click();app.processEvents()
>       assert w.current_page==2 and w.nav_buttons[2].isChecked() and not w.nav_buttons[1].isChecked()
E       assert (1 == 2)
E        +  where 1 = <checkpoint.window.MainWindow(0xbe11060) at 0x7efcf1377dc0>.current_page

tests/test_wish_navigation_0136.py:16: AssertionError
______ test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-True] _______

ui = (<checkpoint.window.MainWindow(0xb984980) at 0x7efcf767b800>, 1)
app = <PySide6.QtWidgets.QApplication(0xb6f7430) at 0x7efcf1742c80>
folder = PosixPath('/tmp/3a77929a13d744a98130864c348bf866'), has_banner = True

    @pytest.mark.parametrize('has_banner',[False,True])
    def test_open_wish_stays_in_wishes_and_does_not_acquire(ui,app,folder,has_banner):
        w,i=ui;lib=w.library
        if has_banner:
            path=folder/'banner.png';im=QImage(1920,620,QImage.Format_RGB32);im.fill(QColor('blue'));im.save(str(path));lib.save_game({'title':lib.get(i)['title'],'banner':str(path)},i)
        lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2);app.processEvents()
        before=lib.get(i);wishlist=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        card=next(c for c in w.pages[2].findChildren(WishCard) if c.isVisible())
        card.findChild(WishLogo).click();app.processEvents()
>       assert w.current_page==2 and w.nav_buttons[2].isChecked() and not w.nav_buttons[1].isChecked()
E       assert (1 == 2)
E        +  where 1 = <checkpoint.window.MainWindow(0xb984980) at 0x7efcf767b800>.current_page

tests/test_wish_navigation_0136.py:16: AssertionError
=========================== short test summary info ============================
FAILED tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-False]
FAILED tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample0-True]
FAILED tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-False]
FAILED tests/test_wish_navigation_0136.py::test_open_wish_stays_in_wishes_and_does_not_acquire[sample1-True]
4 failed in 0.72s

```

stderr integral:
```text

```

Código de saída: 1

## depois-navegacao-desejos

UTC: 2026-11-15T16:54:59.541660+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_navigation_0136.py", "tests/test_detail_0135.py", "tests/test_wishlist_prices.py", "tests/test_registration_0128.py", "tests/test_wish_time_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
............................                                             [100%]
28 passed in 3.32s

```

stderr integral:
```text

```

Código de saída: 0

## depois-ficha-contexto-desejos

UTC: 2026-11-15T16:57:13.011495+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_wish_navigation_0136.py", "tests/test_detail_0135.py", "tests/test_wishlist_prices.py", "tests/test_registration_0128.py", "tests/test_wish_time_0136.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.....................................................................    [100%]
69 passed in 17.34s

```

stderr integral:
```text

```

Código de saída: 0

## antes-favorito-feedback

UTC: 2026-11-15T17:04:03.245667+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_favorite_0136.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
___ test_favorite_click_is_visible_persistent_and_reversible[sample0-False] ____

ui = (<checkpoint.window.MainWindow(0x3c553240) at 0x7f9d284cd980>, 1)
app = <PySide6.QtWidgets.QApplication(0x3c4f4bc0) at 0x7f9d28485580>
wish = False

    @pytest.mark.parametrize('wish',[False,True])
    def test_favorite_click_is_visible_persistent_and_reversible(ui,app,wish):
        w,i=ui;lib=w.library
        lib.save_game({'title':lib.get(i)['title'],'notes':'Nota preservada','description':'Descrição externa'},i)
        if wish:lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2)
        else:w.navigate(1)
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        w.detail(i);app.processEvents()
        def heart():return next(b for b in w.detail_page.findChildren(IconButton) if b.name=='heart')
        for enabled in [True,False]:
            heart().click();app.processEvents()
            assert lib.get(i)['favorite']==int(enabled)
>           control=heart();assert control.isCheckable() and control.isChecked()==enabled
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           assert (False)
E            +  where False = <built-in method isCheckable of IconButton object at 0x7f9d26ba1440>()
E            +    where <built-in method isCheckable of IconButton object at 0x7f9d26ba1440> = <checkpoint.design_system.IconButton(0x3ce03190, name="iconButton") at 0x7f9d26ba1440>.isCheckable

tests/test_favorite_0136.py:18: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_favorite_click_is_visible_persistent_and_reversible[sample0-True] ____

ui = (<checkpoint.window.MainWindow(0x3c42c290) at 0x7f9d284cd900>, 1)
app = <PySide6.QtWidgets.QApplication(0x3c4f4bc0) at 0x7f9d28485580>
wish = True

    @pytest.mark.parametrize('wish',[False,True])
    def test_favorite_click_is_visible_persistent_and_reversible(ui,app,wish):
        w,i=ui;lib=w.library
        lib.save_game({'title':lib.get(i)['title'],'notes':'Nota preservada','description':'Descrição externa'},i)
        if wish:lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2)
        else:w.navigate(1)
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        w.detail(i);app.processEvents()
        def heart():return next(b for b in w.detail_page.findChildren(IconButton) if b.name=='heart')
        for enabled in [True,False]:
            heart().click();app.processEvents()
            assert lib.get(i)['favorite']==int(enabled)
>           control=heart();assert control.isCheckable() and control.isChecked()==enabled
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           assert (False)
E            +  where False = <built-in method isCheckable of IconButton object at 0x7f9d26bd0e00>()
E            +    where <built-in method isCheckable of IconButton object at 0x7f9d26bd0e00> = <checkpoint.design_system.IconButton(0x3c87aa90, name="iconButton") at 0x7f9d26bd0e00>.isCheckable

tests/test_favorite_0136.py:18: AssertionError
___ test_favorite_click_is_visible_persistent_and_reversible[sample1-False] ____

ui = (<checkpoint.window.MainWindow(0x3c78b900) at 0x7f9d28320d00>, 1)
app = <PySide6.QtWidgets.QApplication(0x3c4f4bc0) at 0x7f9d28485580>
wish = False

    @pytest.mark.parametrize('wish',[False,True])
    def test_favorite_click_is_visible_persistent_and_reversible(ui,app,wish):
        w,i=ui;lib=w.library
        lib.save_game({'title':lib.get(i)['title'],'notes':'Nota preservada','description':'Descrição externa'},i)
        if wish:lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2)
        else:w.navigate(1)
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        w.detail(i);app.processEvents()
        def heart():return next(b for b in w.detail_page.findChildren(IconButton) if b.name=='heart')
        for enabled in [True,False]:
            heart().click();app.processEvents()
            assert lib.get(i)['favorite']==int(enabled)
>           control=heart();assert control.isCheckable() and control.isChecked()==enabled
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           assert (False)
E            +  where False = <built-in method isCheckable of IconButton object at 0x7f9d26c2a540>()
E            +    where <built-in method isCheckable of IconButton object at 0x7f9d26c2a540> = <checkpoint.design_system.IconButton(0x3cc7c030, name="iconButton") at 0x7f9d26c2a540>.isCheckable

tests/test_favorite_0136.py:18: AssertionError
____ test_favorite_click_is_visible_persistent_and_reversible[sample1-True] ____

ui = (<checkpoint.window.MainWindow(0x3cb73660) at 0x7f9d27fc06c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x3c4f4bc0) at 0x7f9d28485580>
wish = True

    @pytest.mark.parametrize('wish',[False,True])
    def test_favorite_click_is_visible_persistent_and_reversible(ui,app,wish):
        w,i=ui;lib=w.library
        lib.save_game({'title':lib.get(i)['title'],'notes':'Nota preservada','description':'Descrição externa'},i)
        if wish:lib.set_setting(f'collection.unowned.{i}',True);w.add_wish(i);w.navigate(2)
        else:w.navigate(1)
        original=[tuple(r) for r in lib.sql.execute('SELECT * FROM wishlist')]
        w.detail(i);app.processEvents()
        def heart():return next(b for b in w.detail_page.findChildren(IconButton) if b.name=='heart')
        for enabled in [True,False]:
            heart().click();app.processEvents()
            assert lib.get(i)['favorite']==int(enabled)
>           control=heart();assert control.isCheckable() and control.isChecked()==enabled
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           assert (False)
E            +  where False = <built-in method isCheckable of IconButton object at 0x7f9d26bb1780>()
E            +    where <built-in method isCheckable of IconButton object at 0x7f9d26bb1780> = <checkpoint.design_system.IconButton(0x3cf14f60, name="iconButton") at 0x7f9d26bb1780>.isCheckable

tests/test_favorite_0136.py:18: AssertionError
=========================== short test summary info ============================
FAILED tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-False]
FAILED tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample0-True]
FAILED tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-False]
FAILED tests/test_favorite_0136.py::test_favorite_click_is_visible_persistent_and_reversible[sample1-True]
4 failed in 0.71s

```

stderr integral:
```text

```

Código de saída: 1

## depois-favorito-feedback

UTC: 2026-11-15T17:04:59.447224+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_favorite_0136.py", "tests/test_wish_navigation_0136.py", "tests/test_ui_redesign.py", "tests/test_icons_0134.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
.......................                                                  [100%]
23 passed in 3.45s

```

stderr integral:
```text

```

Código de saída: 0

## suite-final-contexto-desejos-0136

UTC: 2026-11-15T17:06:01.806349+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp; Linux, Python 3.12.14.

stdout integral:
```text
........................................................................ [ 11%]
........................................................................ [ 23%]
........................................................................ [ 35%]
........................................................................ [ 47%]
........................................................................ [ 59%]
........................................................................ [ 71%]
........................................................................ [ 83%]
........................................................................ [ 95%]
............................                                             [100%]
604 passed in 405.37s (0:06:45)

```

stderr integral:
```text

```

Código de saída: 0

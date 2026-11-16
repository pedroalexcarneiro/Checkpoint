# Saídas integrais 0.1.38

Linux: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp. Windows nativo só será declarado após execução própria. Saídas anteriores e posteriores sem truncamento, com exit e ambiente.

## Mensagens nativas antes da correção

Comando: QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp python -m pytest tests/test_native_startup_0138.py -q -p no:cacheprovider

stdout integral:
```text
FFF                                                                      [100%]
=================================== FAILURES ===================================
______ test_creation_message_never_asks_qt_to_create_a_window_again[4660] ______

handle = 4660

    @pytest.mark.parametrize('handle',[0x1234,0x123456789])
    def test_creation_message_never_asks_qt_to_create_a_window_again(handle):
        from checkpoint.windows_frame import IntegratedFrame
        class CreatingWindow:
            def winId(self):raise AssertionError('winId recria a janela durante a mensagem de criação')
            def isMaximized(self):return False
        frame=object.__new__(IntegratedFrame)
        frame.window=CreatingWindow();frame.failed=False
        frame.api=SimpleNamespace(c=ctypes,w=wintypes)
        message=wintypes.MSG();message.hWnd=handle;message.message=0x83
>       assert frame.handle(ctypes.addressof(message))==(True,0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_native_startup_0138.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
checkpoint/windows_frame.py:66: in handle
    msg=c.cast(int(message),c.POINTER(w.MSG)).contents;handle=int(self.window.winId())
                                                                  ^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_native_startup_0138.test_creation_message_never_asks_qt_to_create_a_window_again.<locals>.CreatingWindow object at 0x7fb12fc516a0>

>   def winId(self):raise AssertionError('winId recria a janela durante a mensagem de criação')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: winId recria a janela durante a mensagem de criação

tests/test_native_startup_0138.py:11: AssertionError
___ test_creation_message_never_asks_qt_to_create_a_window_again[4886718345] ___

handle = 4886718345

    @pytest.mark.parametrize('handle',[0x1234,0x123456789])
    def test_creation_message_never_asks_qt_to_create_a_window_again(handle):
        from checkpoint.windows_frame import IntegratedFrame
        class CreatingWindow:
            def winId(self):raise AssertionError('winId recria a janela durante a mensagem de criação')
            def isMaximized(self):return False
        frame=object.__new__(IntegratedFrame)
        frame.window=CreatingWindow();frame.failed=False
        frame.api=SimpleNamespace(c=ctypes,w=wintypes)
        message=wintypes.MSG();message.hWnd=handle;message.message=0x83
>       assert frame.handle(ctypes.addressof(message))==(True,0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_native_startup_0138.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
checkpoint/windows_frame.py:66: in handle
    msg=c.cast(int(message),c.POINTER(w.MSG)).contents;handle=int(self.window.winId())
                                                                  ^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_native_startup_0138.test_creation_message_never_asks_qt_to_create_a_window_again.<locals>.CreatingWindow object at 0x7fb129f1b500>

>   def winId(self):raise AssertionError('winId recria a janela durante a mensagem de criação')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: winId recria a janela durante a mensagem de criação

tests/test_native_startup_0138.py:11: AssertionError
_____________ test_invalid_native_message_does_not_create_a_window _____________

    def test_invalid_native_message_does_not_create_a_window():
        from checkpoint.windows_frame import IntegratedFrame
        class CreatingWindow:
            def winId(self):raise AssertionError('Não criar HWND para mensagem sem destinatário')
        frame=object.__new__(IntegratedFrame)
        frame.window=CreatingWindow();frame.failed=False
        frame.api=SimpleNamespace(c=ctypes,w=wintypes)
        message=wintypes.MSG();message.message=0x83
>       assert frame.handle(ctypes.addressof(message))==(False,0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_native_startup_0138.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
checkpoint/windows_frame.py:66: in handle
    msg=c.cast(int(message),c.POINTER(w.MSG)).contents;handle=int(self.window.winId())
                                                                  ^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_native_startup_0138.test_invalid_native_message_does_not_create_a_window.<locals>.CreatingWindow object at 0x7fb129f1be30>

>   def winId(self):raise AssertionError('Não criar HWND para mensagem sem destinatário')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Não criar HWND para mensagem sem destinatário

tests/test_native_startup_0138.py:23: AssertionError
=========================== short test summary info ============================
FAILED tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4660]
FAILED tests/test_native_startup_0138.py::test_creation_message_never_asks_qt_to_create_a_window_again[4886718345]
FAILED tests/test_native_startup_0138.py::test_invalid_native_message_does_not_create_a_window
3 failed in 0.21s

```

stderr integral:
```text

```

Exit: 1

## regressao-abertura-depois

UTC: 2026-11-16T03:20:17.856238+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_native_startup_0138.py", "tests/test_window_controls_0137.py", "tests/test_elevation_0137.py", "tests/test_visual_0132.py", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
.......................................................                  [100%]
55 passed in 5.70s

```

stderr integral:
```text

```

Código de saída: 0

## suite-completa-0138

UTC: 2026-11-16T03:30:10.632165+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

Ambiente: QT_QPA_PLATFORM=offscreen; CHECKPOINT_TEST_ROOT=/tmp

stdout integral:
```text
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
700 passed in 483.81s (0:08:03)

```

stderr integral:
```text

```

Código de saída: 0

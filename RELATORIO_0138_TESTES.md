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

## logs-primeiro-windows

UTC: 2026-11-16T03:38:30.989144+00:00

Comando: `["gh", "run", "view", "43797801516", "--job", "133070504590", "--log"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
validate	Set up job	﻿2026-11-16T03:22:32.7108854Z Current runner version: '2.338.2'
validate	Set up job	2026-11-16T03:22:32.7150337Z ##[group]Runner Image Provisioner
validate	Set up job	2026-11-16T03:22:32.7151213Z Hosted Compute Agent
validate	Set up job	2026-11-16T03:22:32.7151743Z Version: 20261103.629
validate	Set up job	2026-11-16T03:22:32.7152301Z Commit: 15dbd9ccb5dbf34fae002b6ed1a2670f52df37bc
validate	Set up job	2026-11-16T03:22:32.7152989Z Build Date: 2026-11-03T17:26:59Z
validate	Set up job	2026-11-16T03:22:32.7153610Z Worker ID: {9263c07f-1335-4e28-94f0-69781efc75ac}
validate	Set up job	2026-11-16T03:22:32.7154244Z Region: eastus2
validate	Set up job	2026-11-16T03:22:32.7155081Z Cloud: Azure
validate	Set up job	2026-11-16T03:22:32.7155857Z ##[endgroup]
validate	Set up job	2026-11-16T03:22:32.7157538Z ##[group]Operating System
validate	Set up job	2026-11-16T03:22:32.7158189Z Microsoft Windows Server 2022
validate	Set up job	2026-11-16T03:22:32.7158777Z 10.0.20348
validate	Set up job	2026-11-16T03:22:32.7159249Z Datacenter
validate	Set up job	2026-11-16T03:22:32.7159721Z ##[endgroup]
validate	Set up job	2026-11-16T03:22:32.7160213Z ##[group]Runner Image
validate	Set up job	2026-11-16T03:22:32.7160757Z Image: windows-2022
validate	Set up job	2026-11-16T03:22:32.7161256Z Version: 20261112.366.7
validate	Set up job	2026-11-16T03:22:32.7162284Z Included Software: https://github.com/actions/runner-images/blob/win22/20261112.366/images/windows/Windows2022-Readme.md
validate	Set up job	2026-11-16T03:22:32.7164210Z Image Release: https://github.com/actions/runner-images/releases/tag/win22%2F20261112.366
validate	Set up job	2026-11-16T03:22:32.7165093Z ##[endgroup]
validate	Set up job	2026-11-16T03:22:32.7166098Z ##[group]GITHUB_TOKEN Permissions
validate	Set up job	2026-11-16T03:22:32.7167853Z Contents: read
validate	Set up job	2026-11-16T03:22:32.7168417Z Metadata: read
validate	Set up job	2026-11-16T03:22:32.7168941Z ##[endgroup]
validate	Set up job	2026-11-16T03:22:32.7170886Z Secret source: Actions
validate	Set up job	2026-11-16T03:22:32.7171785Z Cache mode: write
validate	Set up job	2026-11-16T03:22:32.7172430Z Prepare workflow directory
validate	Set up job	2026-11-16T03:22:32.7634050Z Prepare all required actions
validate	Set up job	2026-11-16T03:22:32.7680384Z Getting action download info
validate	Set up job	2026-11-16T03:22:32.9782789Z Download action repository 'actions/checkout@11d5960a326750d5838078e36cf38b85af677262' (SHA:11d5960a326750d5838078e36cf38b85af677262)
validate	Set up job	2026-11-16T03:22:33.0957109Z Download action repository 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
validate	Set up job	2026-11-16T03:22:33.2259180Z Download action repository 'actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
validate	Set up job	2026-11-16T03:22:33.5460790Z Complete job name: validate
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T03:22:33.7058494Z ##[group]Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7059754Z with:
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7060181Z   persist-credentials: false
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7060703Z   repository: pedroalexcarneiro/Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7064426Z   token: ***
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7064821Z   ssh-strict: true
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7065225Z   ssh-user: git
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7065612Z   clean: true
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7066025Z   sparse-checkout-cone-mode: true
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7066514Z   fetch-depth: 1
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7066904Z   fetch-tags: false
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7067315Z   show-progress: true
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7067720Z   lfs: false
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7068095Z   submodules: false
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7068536Z   set-safe-directory: true
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7069009Z   allow-unsafe-pr-checkout: false
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7069738Z env:
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7070148Z   QT_QPA_PLATFORM: offscreen
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.7070603Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.8532695Z Syncing repository: pedroalexcarneiro/Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.8534506Z ##[group]Getting Git version info
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.8535148Z Working directory is 'D:\a\Checkpoint\Checkpoint'
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:33.9499931Z [command]"C:\Program Files\Git\bin\git.exe" version
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2367323Z git version 2.56.1.windows.1
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2404698Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2422519Z Temporarily overriding HOME='D:\a\_temp\772fa4ee-9530-4048-9422-6eccaf08d0ca' before making global git config changes
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2424389Z Adding repository directory to the temporary git global config as a safe directory
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2433062Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2980454Z Deleting the contents of 'D:\a\Checkpoint\Checkpoint'
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2986458Z ##[group]Initializing the repository
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.2994745Z [command]"C:\Program Files\Git\bin\git.exe" init D:\a\Checkpoint\Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.3762577Z Initialized empty Git repository in D:/a/Checkpoint/Checkpoint/.git/
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.3795796Z [command]"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/pedroalexcarneiro/Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4435294Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4436733Z ##[group]Disabling automatic garbage collection
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4442937Z [command]"C:\Program Files\Git\bin\git.exe" config --local gc.auto 0
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4717168Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4718670Z ##[group]Setting up auth
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.4729309Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:34.5007087Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:35.6756420Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:35.7058678Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.1722426Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.2016216Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.6731474Z [command]"C:\Program Files\Git\bin\git.exe" config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ***"
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.7037228Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.7038652Z ##[group]Fetching the repository
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:36.7050857Z [command]"C:\Program Files\Git\bin\git.exe" -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +5e77741ae7e1450033390e644ddfc9b56299e627:refs/remotes/origin/fix/0.1.38-abertura
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7297052Z From https://github.com/pedroalexcarneiro/Checkpoint
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7298068Z  * [new ref]         5e77741ae7e1450033390e644ddfc9b56299e627 -> origin/fix/0.1.38-abertura
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7324882Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7325504Z ##[group]Determining the checkout info
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7327983Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7337103Z [command]"C:\Program Files\Git\bin\git.exe" sparse-checkout disable
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.7734841Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all extensions.worktreeConfig
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.8019792Z ##[group]Checking out the ref
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:37.8028834Z [command]"C:\Program Files\Git\bin\git.exe" checkout --progress --force -B fix/0.1.38-abertura refs/remotes/origin/fix/0.1.38-abertura
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0174118Z Switched to a new branch 'fix/0.1.38-abertura'
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0194374Z branch 'fix/0.1.38-abertura' set up to track 'origin/fix/0.1.38-abertura'.
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0236117Z ##[endgroup]
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0654176Z [command]"C:\Program Files\Git\bin\git.exe" log -1 --format=%H
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0919969Z 5e77741ae7e1450033390e644ddfc9b56299e627
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0949897Z ##[group]Removing auth
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.0957282Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.1233576Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.5692485Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.5956025Z http.https://github.com/.extraheader
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.5986266Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:38.6267901Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:39.0686470Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:39.0968724Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
validate	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:22:39.5566335Z ##[endgroup]
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	﻿2026-11-16T03:22:39.5994402Z ##[group]Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5994903Z with:
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5995108Z   python-version: 3.12
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5995320Z   architecture: x64
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5995504Z   cache: pip
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5995726Z   cache-dependency-path: requirements-tested.txt
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5996024Z   check-latest: false
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5998382Z   token: ***
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5998584Z   update-environment: true
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5998813Z   allow-prereleases: false
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5999018Z   freethreaded: false
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5999226Z env:
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5999417Z   QT_QPA_PLATFORM: offscreen
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.5999628Z ##[endgroup]
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.7497097Z ##[group]Installed versions
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.7684144Z (node:5360) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.7684888Z (Use `node --trace-deprecation ...` to show where the warning was created)
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.7686087Z Successfully set up CPython (3.12.10)
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:39.7686619Z ##[endgroup]
validate	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T03:22:41.9926196Z pip cache is not found
validate	Install tested dependencies	﻿2026-11-16T03:22:42.0191272Z ##[group]Run python -m pip install -r requirements-tested.txt
validate	Install tested dependencies	2026-11-16T03:22:42.0191903Z [36;1mpython -m pip install -r requirements-tested.txt[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0192400Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências Windows indisponíveis.' }[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0192919Z [36;1mpython -m pip install --no-deps --no-build-isolation -e .[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0193352Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Projeto não instalado.' }[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0193701Z [36;1mpython -m pip check[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0194033Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências inconsistentes.' }[0m
validate	Install tested dependencies	2026-11-16T03:22:42.0314639Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
validate	Install tested dependencies	2026-11-16T03:22:42.0315140Z env:
validate	Install tested dependencies	2026-11-16T03:22:42.0315391Z   QT_QPA_PLATFORM: offscreen
validate	Install tested dependencies	2026-11-16T03:22:42.0315858Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Install tested dependencies	2026-11-16T03:22:42.0316519Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
validate	Install tested dependencies	2026-11-16T03:22:42.0317225Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Install tested dependencies	2026-11-16T03:22:42.0317734Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Install tested dependencies	2026-11-16T03:22:42.0318223Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Install tested dependencies	2026-11-16T03:22:42.0318603Z ##[endgroup]
validate	Install tested dependencies	2026-11-16T03:22:44.7171039Z Collecting altgraph==0.17.5 (from -r requirements-tested.txt (line 1))
validate	Install tested dependencies	2026-11-16T03:22:44.9138749Z   Downloading altgraph-0.17.5-py2.py3-none-any.whl.metadata (7.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:44.9973545Z Collecting certifi==2026.10.23 (from -r requirements-tested.txt (line 2))
validate	Install tested dependencies	2026-11-16T03:22:45.0155984Z   Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.2259080Z Collecting cffi==2.1.1 (from -r requirements-tested.txt (line 3))
validate	Install tested dependencies	2026-11-16T03:22:45.2491848Z   Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.4233095Z Collecting charset-normalizer==3.5.2 (from -r requirements-tested.txt (line 4))
validate	Install tested dependencies	2026-11-16T03:22:45.4467942Z   Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.5058419Z Requirement already satisfied: colorama==0.4.6 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 5)) (0.4.6)
validate	Install tested dependencies	2026-11-16T03:22:45.7133204Z Collecting cryptography==50.0.2 (from -r requirements-tested.txt (line 6))
validate	Install tested dependencies	2026-11-16T03:22:45.7362249Z   Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl.metadata (4.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.8010986Z Collecting google-api-core==2.44.0 (from -r requirements-tested.txt (line 7))
validate	Install tested dependencies	2026-11-16T03:22:45.8206140Z   Downloading google_api_core-2.44.0-py3-none-any.whl.metadata (3.2 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.9002691Z Collecting google-api-python-client==2.202.0 (from -r requirements-tested.txt (line 8))
validate	Install tested dependencies	2026-11-16T03:22:45.9185652Z   Downloading google_api_python_client-2.202.0-py3-none-any.whl.metadata (6.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:45.9693744Z Collecting google-auth-httplib2==0.4.4 (from -r requirements-tested.txt (line 9))
validate	Install tested dependencies	2026-11-16T03:22:45.9903907Z   Downloading google_auth_httplib2-0.4.4-py3-none-any.whl.metadata (3.0 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.0433031Z Collecting google-auth-oauthlib==1.5.0 (from -r requirements-tested.txt (line 10))
validate	Install tested dependencies	2026-11-16T03:22:46.0622179Z   Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl.metadata (2.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.1279807Z Collecting google-auth==2.62.2 (from -r requirements-tested.txt (line 11))
validate	Install tested dependencies	2026-11-16T03:22:46.1607277Z   Downloading google_auth-2.62.2-py3-none-any.whl.metadata (6.0 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.2221791Z Collecting googleapis-common-protos==1.76.0 (from -r requirements-tested.txt (line 12))
validate	Install tested dependencies	2026-11-16T03:22:46.2419075Z   Downloading googleapis_common_protos-1.76.0-py3-none-any.whl.metadata (8.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.2990885Z Collecting httplib2==0.32.1 (from -r requirements-tested.txt (line 13))
validate	Install tested dependencies	2026-11-16T03:22:46.3165351Z   Downloading httplib2-0.32.1-py3-none-any.whl.metadata (2.2 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.3690935Z Collecting idna==3.20 (from -r requirements-tested.txt (line 14))
validate	Install tested dependencies	2026-11-16T03:22:46.3870417Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.4388672Z Collecting iniconfig==2.3.1 (from -r requirements-tested.txt (line 15))
validate	Install tested dependencies	2026-11-16T03:22:46.4568539Z   Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.5271693Z Collecting jaraco-classes==3.4.0 (from -r requirements-tested.txt (line 16))
validate	Install tested dependencies	2026-11-16T03:22:46.5473245Z   Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.6018348Z Collecting jaraco-context==6.1.2 (from -r requirements-tested.txt (line 17))
validate	Install tested dependencies	2026-11-16T03:22:46.6238715Z   Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.6811132Z Collecting jaraco-functools==4.6.0 (from -r requirements-tested.txt (line 18))
validate	Install tested dependencies	2026-11-16T03:22:46.7015216Z   Downloading jaraco_functools-4.6.0-py3-none-any.whl.metadata (2.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.7652362Z Collecting keyring==25.7.0 (from -r requirements-tested.txt (line 19))
validate	Install tested dependencies	2026-11-16T03:22:46.7900549Z   Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.8547479Z Collecting more-itertools==11.2.1 (from -r requirements-tested.txt (line 20))
validate	Install tested dependencies	2026-11-16T03:22:46.8757886Z   Downloading more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
validate	Install tested dependencies	2026-11-16T03:22:46.9477405Z Collecting oauthlib==4.0.1 (from -r requirements-tested.txt (line 21))
validate	Install tested dependencies	2026-11-16T03:22:46.9710350Z   Downloading oauthlib-4.0.1-py3-none-any.whl.metadata (8.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.0297501Z Collecting opentelemetry-api==1.45.2 (from -r requirements-tested.txt (line 22))
validate	Install tested dependencies	2026-11-16T03:22:47.0529787Z   Downloading opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.0745659Z Requirement already satisfied: packaging==26.3 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 23)) (26.3)
validate	Install tested dependencies	2026-11-16T03:22:47.1074488Z Collecting pefile==2024.8.26 (from -r requirements-tested.txt (line 24))
validate	Install tested dependencies	2026-11-16T03:22:47.1317871Z   Downloading pefile-2024.8.26-py3-none-any.whl.metadata (1.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.1843325Z Collecting pluggy==1.7.0 (from -r requirements-tested.txt (line 25))
validate	Install tested dependencies	2026-11-16T03:22:47.2025633Z   Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.2640067Z Collecting proto-plus==1.29.0 (from -r requirements-tested.txt (line 26))
validate	Install tested dependencies	2026-11-16T03:22:47.2822543Z   Downloading proto_plus-1.29.0-py3-none-any.whl.metadata (2.2 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.4857339Z Collecting protobuf==7.36.2 (from -r requirements-tested.txt (line 27))
validate	Install tested dependencies	2026-11-16T03:22:47.5037724Z   Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
validate	Install tested dependencies	2026-11-16T03:22:47.5607903Z Collecting pyasn1-modules==0.4.2 (from -r requirements-tested.txt (line 28))
validate	Install tested dependencies	2026-11-16T03:22:47.5815007Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.6402222Z Collecting pyasn1==0.6.5 (from -r requirements-tested.txt (line 29))
validate	Install tested dependencies	2026-11-16T03:22:47.6591113Z   Downloading pyasn1-0.6.5-py3-none-any.whl.metadata (8.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.7162662Z Collecting pycparser==3.12 (from -r requirements-tested.txt (line 30))
validate	Install tested dependencies	2026-11-16T03:22:47.7349182Z   Downloading pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.7955727Z Collecting pygments==2.21.0 (from -r requirements-tested.txt (line 31))
validate	Install tested dependencies	2026-11-16T03:22:47.8161176Z   Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.8717096Z Collecting pyinstaller-hooks-contrib==2026.10 (from -r requirements-tested.txt (line 32))
validate	Install tested dependencies	2026-11-16T03:22:47.8941849Z   Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl.metadata (16 kB)
validate	Install tested dependencies	2026-11-16T03:22:47.9758385Z Collecting pyinstaller==6.22.3 (from -r requirements-tested.txt (line 33))
validate	Install tested dependencies	2026-11-16T03:22:48.0091085Z   Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl.metadata (8.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.0798451Z Collecting pyparsing==3.3.3 (from -r requirements-tested.txt (line 34))
validate	Install tested dependencies	2026-11-16T03:22:48.1038597Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.1848845Z Collecting pyside6-addons==6.8.3 (from -r requirements-tested.txt (line 35))
validate	Install tested dependencies	2026-11-16T03:22:48.2040861Z   Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.2707146Z Collecting pyside6-essentials==6.8.3 (from -r requirements-tested.txt (line 36))
validate	Install tested dependencies	2026-11-16T03:22:48.2964421Z   Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.1 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.3622822Z Collecting pyside6==6.8.3 (from -r requirements-tested.txt (line 37))
validate	Install tested dependencies	2026-11-16T03:22:48.3815993Z   Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl.metadata (5.7 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.4463189Z Collecting pytest==9.2.0 (from -r requirements-tested.txt (line 38))
validate	Install tested dependencies	2026-11-16T03:22:48.4644480Z   Downloading pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.5266966Z Collecting pywin32-ctypes==0.2.3 (from -r requirements-tested.txt (line 39))
validate	Install tested dependencies	2026-11-16T03:22:48.5459704Z   Downloading pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.5971941Z Collecting requests-oauthlib==2.0.0 (from -r requirements-tested.txt (line 40))
validate	Install tested dependencies	2026-11-16T03:22:48.6161078Z   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.6818844Z Collecting requests==2.34.2 (from -r requirements-tested.txt (line 41))
validate	Install tested dependencies	2026-11-16T03:22:48.7007386Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.8228122Z Collecting setuptools==84.2.1 (from -r requirements-tested.txt (line 42))
validate	Install tested dependencies	2026-11-16T03:22:48.8414372Z   Downloading setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.9087549Z Collecting shiboken6==6.8.3 (from -r requirements-tested.txt (line 43))
validate	Install tested dependencies	2026-11-16T03:22:48.9295334Z   Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl.metadata (2.8 kB)
validate	Install tested dependencies	2026-11-16T03:22:48.9854807Z Collecting typing-extensions==4.16.0 (from -r requirements-tested.txt (line 44))
validate	Install tested dependencies	2026-11-16T03:22:49.0079667Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.0662990Z Collecting tzdata==2026.6 (from -r requirements-tested.txt (line 45))
validate	Install tested dependencies	2026-11-16T03:22:49.0847302Z   Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.1336816Z Collecting uritemplate==4.2.0 (from -r requirements-tested.txt (line 46))
validate	Install tested dependencies	2026-11-16T03:22:49.1515173Z   Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.2073255Z Collecting urllib3==2.8.0 (from -r requirements-tested.txt (line 47))
validate	Install tested dependencies	2026-11-16T03:22:49.2257779Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.3276563Z Downloading altgraph-0.17.5-py2.py3-none-any.whl (21 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.3650275Z Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.4205082Z Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl (185 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.4625006Z Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.5065840Z Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl (3.8 MB)
validate	Install tested dependencies	2026-11-16T03:22:49.5868997Z    ---------------------------------------- 3.8/3.8 MB 57.5 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:49.6061516Z Downloading google_api_core-2.44.0-py3-none-any.whl (225 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.6405861Z Downloading google_auth-2.62.2-py3-none-any.whl (270 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.6762738Z Downloading googleapis_common_protos-1.76.0-py3-none-any.whl (307 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.7168006Z Downloading opentelemetry_api-1.45.2-py3-none-any.whl (60 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.7518956Z Downloading proto_plus-1.29.0-py3-none-any.whl (50 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.7865769Z Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.8509406Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.8889440Z Downloading idna-3.20-py3-none-any.whl (69 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.9202539Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
validate	Install tested dependencies	2026-11-16T03:22:49.9538593Z Downloading google_api_python_client-2.202.0-py3-none-any.whl (17.1 MB)
validate	Install tested dependencies	2026-11-16T03:22:50.0758551Z    ---------------------------------------- 17.1/17.1 MB 135.1 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:50.1006678Z Downloading google_auth_httplib2-0.4.4-py3-none-any.whl (9.5 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.1386684Z Downloading httplib2-0.32.1-py3-none-any.whl (92 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.1698075Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.2098261Z Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.2407702Z Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl (20 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.2740696Z Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.3054710Z Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.3385534Z Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.3781261Z Downloading jaraco_functools-4.6.0-py3-none-any.whl (11 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.4112544Z Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.4434272Z Downloading more_itertools-11.2.1-py3-none-any.whl (74 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.4769826Z Downloading oauthlib-4.0.1-py3-none-any.whl (161 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.5174875Z Downloading pefile-2024.8.26-py3-none-any.whl (74 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.5526226Z Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.5827075Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.6207715Z Downloading pyasn1-0.6.5-py3-none-any.whl (84 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.6544270Z Downloading pycparser-3.12-py3-none-any.whl (62 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.7003174Z Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
validate	Install tested dependencies	2026-11-16T03:22:50.7316761Z    ---------------------------------------- 1.3/1.3 MB 31.9 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:50.7531553Z Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl (463 kB)
validate	Install tested dependencies	2026-11-16T03:22:50.7990779Z Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl (1.5 MB)
validate	Install tested dependencies	2026-11-16T03:22:50.8341118Z    ---------------------------------------- 1.5/1.5 MB 37.3 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:50.8575940Z Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl (127.9 MB)
validate	Install tested dependencies	2026-11-16T03:22:54.7801500Z    ---------------------------------------- 127.9/127.9 MB 32.4 MB/s  0:00:03
validate	Install tested dependencies	2026-11-16T03:22:54.8625168Z Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl (72.2 MB)
validate	Install tested dependencies	2026-11-16T03:22:56.1208703Z    ---------------------------------------- 72.2/72.2 MB 57.5 MB/s  0:00:01
validate	Install tested dependencies	2026-11-16T03:22:56.1456569Z Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl (561 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.1635452Z    ---------------------------------------- 561.1/561.1 kB 18.7 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:56.1811064Z Downloading pytest-9.2.0-py3-none-any.whl (411 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.2159283Z Downloading pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.2519283Z Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.2827685Z Downloading setuptools-84.2.1-py3-none-any.whl (876 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.3051629Z    ---------------------------------------- 876.3/876.3 kB 40.9 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:56.3256026Z Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl (1.2 MB)
validate	Install tested dependencies	2026-11-16T03:22:56.3499290Z    ---------------------------------------- 1.2/1.2 MB 59.3 MB/s  0:00:00
validate	Install tested dependencies	2026-11-16T03:22:56.3678339Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
validate	Install tested dependencies	2026-11-16T03:22:56.4049087Z Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
validate	Install tested dependencies	2026-11-16T03:22:57.0884603Z Installing collected packages: altgraph, urllib3, uritemplate, tzdata, typing-extensions, shiboken6, setuptools, pywin32-ctypes, pyparsing, pyinstaller-hooks-contrib, pygments, pycparser, pyasn1, protobuf, pluggy, pefile, oauthlib, more-itertools, jaraco-context, iniconfig, idna, charset-normalizer, certifi, requests, pytest, pyside6-essentials, pyinstaller, pyasn1-modules, proto-plus, opentelemetry-api, jaraco-functools, jaraco-classes, httplib2, googleapis-common-protos, cffi, requests-oauthlib, pyside6-addons, keyring, cryptography, pyside6, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-core, google-api-python-client
validate	Install tested dependencies	2026-11-16T03:23:22.2148208Z 
validate	Install tested dependencies	2026-11-16T03:23:22.2198598Z Successfully installed altgraph-0.17.5 certifi-2026.10.23 cffi-2.1.1 charset-normalizer-3.5.2 cryptography-50.0.2 google-api-core-2.44.0 google-api-python-client-2.202.0 google-auth-2.62.2 google-auth-httplib2-0.4.4 google-auth-oauthlib-1.5.0 googleapis-common-protos-1.76.0 httplib2-0.32.1 idna-3.20 iniconfig-2.3.1 jaraco-classes-3.4.0 jaraco-context-6.1.2 jaraco-functools-4.6.0 keyring-25.7.0 more-itertools-11.2.1 oauthlib-4.0.1 opentelemetry-api-1.45.2 pefile-2024.8.26 pluggy-1.7.0 proto-plus-1.29.0 protobuf-7.36.2 pyasn1-0.6.5 pyasn1-modules-0.4.2 pycparser-3.12 pygments-2.21.0 pyinstaller-6.22.3 pyinstaller-hooks-contrib-2026.10 pyparsing-3.3.3 pyside6-6.8.3 pyside6-addons-6.8.3 pyside6-essentials-6.8.3 pytest-9.2.0 pywin32-ctypes-0.2.3 requests-2.34.2 requests-oauthlib-2.0.0 setuptools-84.2.1 shiboken6-6.8.3 typing-extensions-4.16.0 tzdata-2026.6 uritemplate-4.2.0 urllib3-2.8.0
validate	Install tested dependencies	2026-11-16T03:23:23.4604768Z Obtaining file:///D:/a/Checkpoint/Checkpoint
validate	Install tested dependencies	2026-11-16T03:23:23.4624771Z   Checking if build backend supports build_editable: started
validate	Install tested dependencies	2026-11-16T03:23:23.7857822Z   Checking if build backend supports build_editable: finished with status 'done'
validate	Install tested dependencies	2026-11-16T03:23:23.7879649Z   Preparing editable metadata (pyproject.toml): started
validate	Install tested dependencies	2026-11-16T03:23:25.4393758Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
validate	Install tested dependencies	2026-11-16T03:23:25.4457691Z Building wheels for collected packages: checkpoint-desktop
validate	Install tested dependencies	2026-11-16T03:23:25.4480296Z   Building editable for checkpoint-desktop (pyproject.toml): started
validate	Install tested dependencies	2026-11-16T03:23:25.9039426Z   Building editable for checkpoint-desktop (pyproject.toml): finished with status 'done'
validate	Install tested dependencies	2026-11-16T03:23:25.9055268Z   C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\setuptools\command\editable_wheel.py:354: BuildBackendWarning: Editable installation.
validate	Install tested dependencies	2026-11-16T03:23:25.9056489Z   !!
validate	Install tested dependencies	2026-11-16T03:23:25.9056738Z   
validate	Install tested dependencies	2026-11-16T03:23:25.9057054Z           ********************************************************************************
validate	Install tested dependencies	2026-11-16T03:23:25.9057921Z           Please be careful with folders in your working directory with the same
validate	Install tested dependencies	2026-11-16T03:23:25.9058671Z           name as your package as they may take precedence during imports.
validate	Install tested dependencies	2026-11-16T03:23:25.9059297Z           ********************************************************************************
validate	Install tested dependencies	2026-11-16T03:23:25.9059768Z   
validate	Install tested dependencies	2026-11-16T03:23:25.9059988Z   !!
validate	Install tested dependencies	2026-11-16T03:23:25.9060317Z     with strategy, WheelFile(wheel_path, "w") as wheel_obj:
validate	Install tested dependencies	2026-11-16T03:23:25.9085533Z   Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.38-0.editable-py3-none-any.whl size=3272 sha256=a90eeb2424a8f59c9cc050771771ac290e58faa8309a1f08bb56a69175ef0007
validate	Install tested dependencies	2026-11-16T03:23:25.9088020Z   Stored in directory: C:\Users\runneradmin\AppData\Local\Temp\pip-ephem-wheel-cache-_fbxf4kz\wheels\a2\38\6e\88ad7ec70fd74394064971fa20d15ccdcdb6f76505932df31d
validate	Install tested dependencies	2026-11-16T03:23:25.9117128Z Successfully built checkpoint-desktop
validate	Install tested dependencies	2026-11-16T03:23:25.9341491Z Installing collected packages: checkpoint-desktop
validate	Install tested dependencies	2026-11-16T03:23:25.9674788Z Successfully installed checkpoint-desktop-0.1.38
validate	Install tested dependencies	2026-11-16T03:23:26.3653246Z No broken requirements found.
validate	Test on Windows	﻿2026-11-16T03:23:26.4884540Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-ui-tests'
validate	Test on Windows	2026-11-16T03:23:26.4885292Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-ui-tests'[0m
validate	Test on Windows	2026-11-16T03:23:26.4885942Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
validate	Test on Windows	2026-11-16T03:23:26.4886534Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
validate	Test on Windows	2026-11-16T03:23:26.4925267Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
validate	Test on Windows	2026-11-16T03:23:26.4925610Z env:
validate	Test on Windows	2026-11-16T03:23:26.4925788Z   QT_QPA_PLATFORM: offscreen
validate	Test on Windows	2026-11-16T03:23:26.4926094Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Test on Windows	2026-11-16T03:23:26.4926542Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
validate	Test on Windows	2026-11-16T03:23:26.4926989Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Test on Windows	2026-11-16T03:23:26.4927383Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Test on Windows	2026-11-16T03:23:26.4927806Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Test on Windows	2026-11-16T03:23:26.4928125Z ##[endgroup]
validate	Test on Windows	2026-11-16T03:23:40.4798921Z ........................................................................ [ 10%]
validate	Test on Windows	2026-11-16T03:23:52.1869391Z ........................................................................ [ 20%]
validate	Test on Windows	2026-11-16T03:24:06.7615985Z ........................................................................ [ 30%]
validate	Test on Windows	2026-11-16T03:24:11.5100934Z ........................................................................ [ 41%]
validate	Test on Windows	2026-11-16T03:24:35.6243700Z ........................................................................ [ 51%]
validate	Test on Windows	2026-11-16T03:26:14.0751268Z ........................................................................ [ 61%]
validate	Test on Windows	2026-11-16T03:26:54.2469187Z ........................................................................ [ 72%]
validate	Test on Windows	2026-11-16T03:28:49.2844742Z ........................................................................ [ 82%]
validate	Test on Windows	2026-11-16T03:32:57.1995174Z ........................................................................ [ 92%]
validate	Test on Windows	2026-11-16T03:34:10.5005361Z ......F.............................................                     [100%]
validate	Test on Windows	2026-11-16T03:34:10.5006420Z ================================== FAILURES ===================================
validate	Test on Windows	2026-11-16T03:34:10.5007641Z __________ test_protected_drive_and_registration_logic_is_unchanged ___________
validate	Test on Windows	2026-11-16T03:34:10.5008110Z 
validate	Test on Windows	2026-11-16T03:34:10.5008403Z     def test_protected_drive_and_registration_logic_is_unchanged():
validate	Test on Windows	2026-11-16T03:34:10.5009031Z         import ast,subprocess
validate	Test on Windows	2026-11-16T03:34:10.5009441Z         from pathlib import Path
validate	Test on Windows	2026-11-16T03:34:10.5011468Z         # A 0.1.33 muda somente a apresenta��o dos candidatos e da aus�ncia de dados.
validate	Test on Windows	2026-11-16T03:34:10.5012576Z         # Os demais m�todos e os caminhos de persist�ncia/lifecycle continuam congelados.
validate	Test on Windows	2026-11-16T03:34:10.5013587Z         names={'apply_catalog','validate','finish_or_wait','accept','reject','load_drive_file','source_changed','data'}
validate	Test on Windows	2026-11-16T03:34:10.5014592Z         for filename in ('checkpoint/quick_add.py','checkpoint/dialogs.py'):
validate	Test on Windows	2026-11-16T03:34:10.5015555Z >           original=ast.parse(subprocess.check_output(['git','show',f'c51c245:{filename}'],text=True,encoding='utf-8'))
validate	Test on Windows	2026-11-16T03:34:10.5016504Z                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
validate	Test on Windows	2026-11-16T03:34:10.5016943Z 
validate	Test on Windows	2026-11-16T03:34:10.5017083Z tests\test_visual_0132.py:136: 
validate	Test on Windows	2026-11-16T03:34:10.5017550Z _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
validate	Test on Windows	2026-11-16T03:34:10.5018292Z C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\subprocess.py:466: in check_output
validate	Test on Windows	2026-11-16T03:34:10.5019082Z     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
validate	Test on Windows	2026-11-16T03:34:10.5019740Z _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
validate	Test on Windows	2026-11-16T03:34:10.5020102Z 
validate	Test on Windows	2026-11-16T03:34:10.5022667Z input = None, capture_output = False, timeout = None, check = True
validate	Test on Windows	2026-11-16T03:34:10.5023363Z popenargs = (['git', 'show', 'c51c245:checkpoint/quick_add.py'],)
validate	Test on Windows	2026-11-16T03:34:10.5023990Z kwargs = {'stdout': -1, 'text': True, 'encoding': 'utf-8'}
validate	Test on Windows	2026-11-16T03:34:10.5024368Z 
validate	Test on Windows	2026-11-16T03:34:10.5024511Z     def run(*popenargs,
validate	Test on Windows	2026-11-16T03:34:10.5025026Z             input=None, capture_output=False, timeout=None, check=False, **kwargs):
validate	Test on Windows	2026-11-16T03:34:10.5025782Z         """Run command with arguments and return a CompletedProcess instance.
validate	Test on Windows	2026-11-16T03:34:10.5026340Z     
validate	Test on Windows	2026-11-16T03:34:10.5026834Z         The returned instance will have attributes args, returncode, stdout and
validate	Test on Windows	2026-11-16T03:34:10.5027608Z         stderr. By default, stdout and stderr are not captured, and those attributes
validate	Test on Windows	2026-11-16T03:34:10.5028406Z         will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
validate	Test on Windows	2026-11-16T03:34:10.5029067Z         or pass capture_output=True to capture both.
validate	Test on Windows	2026-11-16T03:34:10.5029520Z     
validate	Test on Windows	2026-11-16T03:34:10.5029922Z         If check is True and the exit code was non-zero, it raises a
validate	Test on Windows	2026-11-16T03:34:10.5030686Z         CalledProcessError. The CalledProcessError object will have the return code
validate	Test on Windows	2026-11-16T03:34:10.5031508Z         in the returncode attribute, and output & stderr attributes if those streams
validate	Test on Windows	2026-11-16T03:34:10.5032176Z         were captured.
validate	Test on Windows	2026-11-16T03:34:10.5032554Z     
validate	Test on Windows	2026-11-16T03:34:10.5033061Z         If timeout (seconds) is given and the process takes too long,
validate	Test on Windows	2026-11-16T03:34:10.5033663Z          a TimeoutExpired exception will be raised.
validate	Test on Windows	2026-11-16T03:34:10.5034122Z     
validate	Test on Windows	2026-11-16T03:34:10.5034507Z         There is an optional argument "input", allowing you to
validate	Test on Windows	2026-11-16T03:34:10.5035180Z         pass bytes or a string to the subprocess's stdin.  If you use this argument
validate	Test on Windows	2026-11-16T03:34:10.5035923Z         you may not also use the Popen constructor's "stdin" argument, as
validate	Test on Windows	2026-11-16T03:34:10.5036536Z         it will be used internally.
validate	Test on Windows	2026-11-16T03:34:10.5036912Z     
validate	Test on Windows	2026-11-16T03:34:10.5037382Z         By default, all communication is in bytes, and therefore any "input" should
validate	Test on Windows	2026-11-16T03:34:10.5038147Z         be bytes, and the stdout and stderr will be bytes. If in text mode, any
validate	Test on Windows	2026-11-16T03:34:10.5039872Z         "input" should be a string, and stdout and stderr will be strings decoded
validate	Test on Windows	2026-11-16T03:34:10.5040634Z         according to locale encoding, or by "encoding" if set. Text mode is
validate	Test on Windows	2026-11-16T03:34:10.5041384Z         triggered by setting any of text, encoding, errors or universal_newlines.
validate	Test on Windows	2026-11-16T03:34:10.5041962Z     
validate	Test on Windows	2026-11-16T03:34:10.5042396Z         The other arguments are the same as for the Popen constructor.
validate	Test on Windows	2026-11-16T03:34:10.5042953Z         """
validate	Test on Windows	2026-11-16T03:34:10.5043259Z         if input is not None:
validate	Test on Windows	2026-11-16T03:34:10.5043662Z             if kwargs.get('stdin') is not None:
validate	Test on Windows	2026-11-16T03:34:10.5044264Z                 raise ValueError('stdin and input arguments may not both be used.')
validate	Test on Windows	2026-11-16T03:34:10.5044872Z             kwargs['stdin'] = PIPE
validate	Test on Windows	2026-11-16T03:34:10.5045244Z     
validate	Test on Windows	2026-11-16T03:34:10.5045549Z         if capture_output:
validate	Test on Windows	2026-11-16T03:34:10.5046079Z             if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
validate	Test on Windows	2026-11-16T03:34:10.5046810Z                 raise ValueError('stdout and stderr arguments may not be used '
validate	Test on Windows	2026-11-16T03:34:10.5047438Z                                  'with capture_output.')
validate	Test on Windows	2026-11-16T03:34:10.5047891Z             kwargs['stdout'] = PIPE
validate	Test on Windows	2026-11-16T03:34:10.5048335Z             kwargs['stderr'] = PIPE
validate	Test on Windows	2026-11-16T03:34:10.5048696Z     
validate	Test on Windows	2026-11-16T03:34:10.5049046Z         with Popen(*popenargs, **kwargs) as process:
validate	Test on Windows	2026-11-16T03:34:10.5049546Z             try:
validate	Test on Windows	2026-11-16T03:34:10.5049999Z                 stdout, stderr = process.communicate(input, timeout=timeout)
validate	Test on Windows	2026-11-16T03:34:10.5050586Z             except TimeoutExpired as exc:
validate	Test on Windows	2026-11-16T03:34:10.5051013Z                 process.kill()
validate	Test on Windows	2026-11-16T03:34:10.5052141Z                 if _mswindows:
validate	Test on Windows	2026-11-16T03:34:10.5052624Z                     # Windows accumulates the output in a single blocking
validate	Test on Windows	2026-11-16T03:34:10.5053309Z                     # read() call run on child threads, with the timeout
validate	Test on Windows	2026-11-16T03:34:10.5053925Z                     # being done in a join() on those threads.  communicate()
validate	Test on Windows	2026-11-16T03:34:10.5054558Z                     # _after_ kill() is required to collect that and add it
validate	Test on Windows	2026-11-16T03:34:10.5055110Z                     # to the exception.
validate	Test on Windows	2026-11-16T03:34:10.5055602Z                     exc.stdout, exc.stderr = process.communicate()
validate	Test on Windows	2026-11-16T03:34:10.5056090Z                 else:
validate	Test on Windows	2026-11-16T03:34:10.5056516Z                     # POSIX _communicate already populated the output so
validate	Test on Windows	2026-11-16T03:34:10.5057126Z                     # far into the TimeoutExpired exception.
validate	Test on Windows	2026-11-16T03:34:10.5057601Z                     process.wait()
validate	Test on Windows	2026-11-16T03:34:10.5057969Z                 raise
validate	Test on Windows	2026-11-16T03:34:10.5058450Z             except:  # Including KeyboardInterrupt, communicate handled that.
validate	Test on Windows	2026-11-16T03:34:10.5059025Z                 process.kill()
validate	Test on Windows	2026-11-16T03:34:10.5059504Z                 # We don't call process.wait() as .__exit__ does that for us.
validate	Test on Windows	2026-11-16T03:34:10.5060053Z                 raise
validate	Test on Windows	2026-11-16T03:34:10.5060425Z             retcode = process.poll()
validate	Test on Windows	2026-11-16T03:34:10.5060869Z             if check and retcode:
validate	Test on Windows	2026-11-16T03:34:10.5061335Z >               raise CalledProcessError(retcode, process.args,
validate	Test on Windows	2026-11-16T03:34:10.5061887Z                                          output=stdout, stderr=stderr)
validate	Test on Windows	2026-11-16T03:34:10.5062845Z E               subprocess.CalledProcessError: Command '['git', 'show', 'c51c245:checkpoint/quick_add.py']' returned non-zero exit status 128.
validate	Test on Windows	2026-11-16T03:34:10.5063636Z 
validate	Test on Windows	2026-11-16T03:34:10.5064002Z C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\subprocess.py:571: CalledProcessError
validate	Test on Windows	2026-11-16T03:34:10.5064916Z ---------------------------- Captured stderr call -----------------------------
validate	Test on Windows	2026-11-16T03:34:10.5065623Z fatal: invalid object name 'c51c245'.
validate	Test on Windows	2026-11-16T03:34:10.5066134Z =========================== short test summary info ===========================
validate	Test on Windows	2026-11-16T03:34:10.5067723Z FAILED tests/test_visual_0132.py::test_protected_drive_and_registration_logic_is_unchanged - subprocess.CalledProcessError: Command '['git', 'show', 'c51c245:checkpoint/quick_add.py']' returned non-zero exit status 128.
validate	Test on Windows	2026-11-16T03:34:10.5069351Z 1 failed, 699 passed in 642.86s (0:10:42)
validate	Test on Windows	2026-11-16T03:34:11.6124685Z [31;1mException: [0mD:\a\_temp\e8777d42-ca39-44f6-baec-9eb601bdbc4b.ps1:4[0m
validate	Test on Windows	2026-11-16T03:34:11.6125923Z [31;1m[0m[36;1mLine |[0m
validate	Test on Windows	2026-11-16T03:34:11.6126693Z [31;1m[0m[36;1m[36;1m   4 | [0m if ($LASTEXITCODE -ne 0) { [36;1mthrow 'Testes Windows falharam.'[0m }[0m
validate	Test on Windows	2026-11-16T03:34:11.6127628Z [31;1m[0m[36;1m[36;1m[0m[36;1m[0m[36;1m     | [31;1m                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[0m
validate	Test on Windows	2026-11-16T03:34:11.6128543Z [31;1m[0m[36;1m[36;1m[0m[36;1m[0m[36;1m[31;1m[31;1m[36;1m     | [31;1mTestes Windows falharam.[0m
validate	Test on Windows	2026-11-16T03:34:11.6295798Z ##[error]Process completed with exit code 1.
validate	Preserve test report	﻿2026-11-16T03:34:11.6515061Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
validate	Preserve test report	2026-11-16T03:34:11.6515974Z with:
validate	Preserve test report	2026-11-16T03:34:11.6516390Z   name: checkpoint-windows-ui-tests
validate	Preserve test report	2026-11-16T03:34:11.6516966Z   path: .ci-results/pytest.xml
validate	Preserve test report	2026-11-16T03:34:11.6517445Z   if-no-files-found: ignore
validate	Preserve test report	2026-11-16T03:34:11.6517907Z   retention-days: 14
validate	Preserve test report	2026-11-16T03:34:11.6518393Z   compression-level: 6
validate	Preserve test report	2026-11-16T03:34:11.6518802Z   overwrite: false
validate	Preserve test report	2026-11-16T03:34:11.6519204Z   include-hidden-files: false
validate	Preserve test report	2026-11-16T03:34:11.6519778Z env:
validate	Preserve test report	2026-11-16T03:34:11.6520136Z   QT_QPA_PLATFORM: offscreen
validate	Preserve test report	2026-11-16T03:34:11.6520774Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Preserve test report	2026-11-16T03:34:11.6521629Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
validate	Preserve test report	2026-11-16T03:34:11.6522477Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Preserve test report	2026-11-16T03:34:11.6523284Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Preserve test report	2026-11-16T03:34:11.6524114Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
validate	Preserve test report	2026-11-16T03:34:11.6524705Z ##[endgroup]
validate	Preserve test report	2026-11-16T03:34:11.8305749Z (node:8016) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
validate	Preserve test report	2026-11-16T03:34:11.8306561Z (Use `node --trace-deprecation ...` to show where the warning was created)
validate	Preserve test report	2026-11-16T03:34:11.8356983Z With the provided path, there will be 1 file uploaded
validate	Preserve test report	2026-11-16T03:34:11.8362060Z Artifact name is valid!
validate	Preserve test report	2026-11-16T03:34:11.8364923Z Root directory input is valid!
validate	Preserve test report	2026-11-16T03:34:12.0463251Z Beginning upload of artifact content to blob storage
validate	Preserve test report	2026-11-16T03:34:12.0687731Z (node:8016) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
validate	Preserve test report	2026-11-16T03:34:12.1147548Z Uploaded bytes 16144
validate	Preserve test report	2026-11-16T03:34:12.1353421Z Finished uploading artifact content to blob storage!
validate	Preserve test report	2026-11-16T03:34:12.1354810Z SHA256 digest of uploaded artifact zip is 19c907fa9c0ccdb6c5d8d5bab1800e247729d613c5bd88e3728eafd747344e57
validate	Preserve test report	2026-11-16T03:34:12.1357566Z Finalizing artifact upload
validate	Preserve test report	2026-11-16T03:34:12.4612192Z Artifact checkpoint-windows-ui-tests.zip successfully finalized. Artifact ID 14195124929
validate	Preserve test report	2026-11-16T03:34:12.4614113Z Artifact checkpoint-windows-ui-tests has been successfully uploaded! Final size is 16144 bytes. Artifact ID is 14195124929
validate	Preserve test report	2026-11-16T03:34:12.4622453Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43797801516/artifacts/14195124929
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T03:34:12.4931894Z Post job cleanup.
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.6798714Z [command]"C:\Program Files\Git\bin\git.exe" version
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7068402Z git version 2.56.1.windows.1
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7137740Z Temporarily overriding HOME='D:\a\_temp\3b747668-3ebd-44af-877b-3ebf8c385d40' before making global git config changes
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7157506Z Adding repository directory to the temporary git global config as a safe directory
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7159259Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7454375Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:12.7738508Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:13.2343046Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:13.2626109Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:13.7341274Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
validate	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T03:34:13.7626370Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
validate	Complete job	﻿2026-11-16T03:34:14.2355130Z Cleaning up orphan processes
validate	Complete job	2026-11-16T03:34:14.2524690Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@11d5960a326750d5838078e36cf38b85af677262, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

```

stderr integral:
```text

```

Código de saída: 0

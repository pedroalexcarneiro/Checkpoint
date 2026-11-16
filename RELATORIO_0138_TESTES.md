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

## status-windows-repeticao

UTC: 2026-11-16T03:45:14.000970+00:00

Comando: `["gh", "run", "view", "43799707113", "--json", "status,conclusion,createdAt,headSha,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"conclusion":"","createdAt":"2026-11-16T03:41:48Z","headSha":"ff136584974b55989c10598612235717508ec25a","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43799707113"}

```

stderr integral:
```text

```

Código de saída: 0

## logs-windows-final

UTC: 2026-11-16T11:03:08.721672+00:00

Comando: `["gh", "run", "view", "43799707113", "--job", "133076641841", "--log"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## Log Windows integral recuperado pelo conector GitHub

Run 43799707113, job 133076641841; resposta bem-sucedida da API de logs. A chamada gh run view --log registrada acima retornou stdout vazio e exit 0; o log foi então recuperado pelo conector, sem tratar saída vazia como evidência.

```text
﻿2026-11-16T03:41:52.1195152Z Current runner version: '2.338.2'
2026-11-16T03:41:52.1226551Z ##[group]Runner Image Provisioner
2026-11-16T03:41:52.1227712Z Hosted Compute Agent
2026-11-16T03:41:52.1228486Z Version: 20261103.629
2026-11-16T03:41:52.1229486Z Commit: 15dbd9ccb5dbf34fae002b6ed1a2670f52df37bc
2026-11-16T03:41:52.1230652Z Build Date: 2026-11-03T17:26:59Z
2026-11-16T03:41:52.1231660Z Worker ID: {588d545e-4ddd-4b4e-a70f-2c003aa08ade}
2026-11-16T03:41:52.1232826Z Region: centralus
2026-11-16T03:41:52.1233635Z Cloud: Azure
2026-11-16T03:41:52.1234421Z ##[endgroup]
2026-11-16T03:41:52.1236423Z ##[group]Operating System
2026-11-16T03:41:52.1237426Z Microsoft Windows Server 2022
2026-11-16T03:41:52.1238444Z 10.0.20348
2026-11-16T03:41:52.1239241Z Datacenter
2026-11-16T03:41:52.1240038Z ##[endgroup]
2026-11-16T03:41:52.1240867Z ##[group]Runner Image
2026-11-16T03:41:52.1241747Z Image: windows-2022
2026-11-16T03:41:52.1242631Z Version: 20261112.366.7
2026-11-16T03:41:52.1244866Z Included Software: https://github.com/actions/runner-images/blob/win22/20261112.366/images/windows/Windows2022-Readme.md
2026-11-16T03:41:52.1247536Z Image Release: https://github.com/actions/runner-images/releases/tag/win22%2F20261112.366
2026-11-16T03:41:52.1249097Z ##[endgroup]
2026-11-16T03:41:52.1250804Z ##[group]GITHUB_TOKEN Permissions
2026-11-16T03:41:52.1253178Z Contents: read
2026-11-16T03:41:52.1254102Z Metadata: read
2026-11-16T03:41:52.1254920Z ##[endgroup]
2026-11-16T03:41:52.1257631Z Secret source: Actions
2026-11-16T03:41:52.1259048Z Cache mode: write
2026-11-16T03:41:52.1260182Z Prepare workflow directory
2026-11-16T03:41:52.1665487Z Prepare all required actions
2026-11-16T03:41:52.1711625Z Getting action download info
2026-11-16T03:41:52.4217271Z Download action repository 'actions/checkout@11d5960a326750d5838078e36cf38b85af677262' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-11-16T03:41:52.5402154Z Download action repository 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-11-16T03:41:52.6777776Z Download action repository 'actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-11-16T03:41:53.0006799Z Complete job name: validate
2026-11-16T03:41:53.1878237Z ##[group]Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262
2026-11-16T03:41:53.1879419Z with:
2026-11-16T03:41:53.1879819Z   fetch-depth: 0
2026-11-16T03:41:53.1880244Z   persist-credentials: false
2026-11-16T03:41:53.1880751Z   repository: pedroalexcarneiro/Checkpoint
2026-11-16T03:41:53.1884837Z   token: ***
2026-11-16T03:41:53.1885231Z   ssh-strict: true
2026-11-16T03:41:53.1885627Z   ssh-user: git
2026-11-16T03:41:53.1886010Z   clean: true
2026-11-16T03:41:53.1886417Z   sparse-checkout-cone-mode: true
2026-11-16T03:41:53.1886909Z   fetch-tags: false
2026-11-16T03:41:53.1887307Z   show-progress: true
2026-11-16T03:41:53.1887717Z   lfs: false
2026-11-16T03:41:53.1888087Z   submodules: false
2026-11-16T03:41:53.1888533Z   set-safe-directory: true
2026-11-16T03:41:53.1889023Z   allow-unsafe-pr-checkout: false
2026-11-16T03:41:53.1889715Z env:
2026-11-16T03:41:53.1890104Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:41:53.1890555Z ##[endgroup]
2026-11-16T03:41:53.3277512Z Syncing repository: pedroalexcarneiro/Checkpoint
2026-11-16T03:41:53.3279315Z ##[group]Getting Git version info
2026-11-16T03:41:53.3279956Z Working directory is 'D:\a\Checkpoint\Checkpoint'
2026-11-16T03:41:53.4246002Z [command]"C:\Program Files\Git\bin\git.exe" version
2026-11-16T03:41:53.7653584Z git version 2.56.1.windows.1
2026-11-16T03:41:53.7699708Z ##[endgroup]
2026-11-16T03:41:53.7722224Z Temporarily overriding HOME='D:\a\_temp\de411c1b-bf6f-40cd-b442-e59a33651ca0' before making global git config changes
2026-11-16T03:41:53.7723700Z Adding repository directory to the temporary git global config as a safe directory
2026-11-16T03:41:53.7736871Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
2026-11-16T03:41:53.8361434Z Deleting the contents of 'D:\a\Checkpoint\Checkpoint'
2026-11-16T03:41:53.8366577Z ##[group]Initializing the repository
2026-11-16T03:41:53.8375836Z [command]"C:\Program Files\Git\bin\git.exe" init D:\a\Checkpoint\Checkpoint
2026-11-16T03:41:53.9290055Z Initialized empty Git repository in D:/a/Checkpoint/Checkpoint/.git/
2026-11-16T03:41:53.9331458Z [command]"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/pedroalexcarneiro/Checkpoint
2026-11-16T03:41:53.9902355Z ##[endgroup]
2026-11-16T03:41:53.9903924Z ##[group]Disabling automatic garbage collection
2026-11-16T03:41:53.9911566Z [command]"C:\Program Files\Git\bin\git.exe" config --local gc.auto 0
2026-11-16T03:41:54.0215557Z ##[endgroup]
2026-11-16T03:41:54.0217460Z ##[group]Setting up auth
2026-11-16T03:41:54.0225597Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T03:41:54.0507880Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T03:41:55.4610216Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T03:41:55.4890008Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T03:41:55.9526479Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T03:41:55.9811970Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T03:41:56.4394081Z [command]"C:\Program Files\Git\bin\git.exe" config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ***"
2026-11-16T03:41:56.4711207Z ##[endgroup]
2026-11-16T03:41:56.4711753Z ##[group]Fetching the repository
2026-11-16T03:41:56.4733245Z [command]"C:\Program Files\Git\bin\git.exe" -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
2026-11-16T03:41:57.9414483Z From https://github.com/pedroalexcarneiro/Checkpoint
2026-11-16T03:41:57.9415582Z  * [new branch]      codex/design-fidelity-pt-br -> origin/codex/design-fidelity-pt-br
2026-11-16T03:41:57.9416603Z  * [new branch]      codex/steam-library-import -> origin/codex/steam-library-import
2026-11-16T03:41:57.9417352Z  * [new branch]      fix/0.1.29          -> origin/fix/0.1.29
2026-11-16T03:41:57.9417999Z  * [new branch]      fix/0.1.30          -> origin/fix/0.1.30
2026-11-16T03:41:57.9418714Z  * [new branch]      fix/0.1.32-visual   -> origin/fix/0.1.32-visual
2026-11-16T03:41:57.9419473Z  * [new branch]      fix/0.1.33-drive    -> origin/fix/0.1.33-drive
2026-11-16T03:41:57.9420284Z  * [new branch]      fix/0.1.34-bugs     -> origin/fix/0.1.34-bugs
2026-11-16T03:41:57.9421488Z  * [new branch]      fix/0.1.35-ajustes  -> origin/fix/0.1.35-ajustes
2026-11-16T03:41:57.9422375Z  * [new branch]      fix/0.1.36-ajustes  -> origin/fix/0.1.36-ajustes
2026-11-16T03:41:57.9423055Z  * [new branch]      fix/0.1.37-ajustes  -> origin/fix/0.1.37-ajustes
2026-11-16T03:41:57.9423817Z  * [new branch]      fix/0.1.38-abertura -> origin/fix/0.1.38-abertura
2026-11-16T03:41:57.9424824Z  * [new branch]      fix/rename-redesign-0.1.28 -> origin/fix/rename-redesign-0.1.28
2026-11-16T03:41:57.9425606Z  * [new branch]      main                -> origin/main
2026-11-16T03:41:57.9426173Z  * [new tag]         v0.1.10             -> v0.1.10
2026-11-16T03:41:57.9426741Z  * [new tag]         v0.1.11             -> v0.1.11
2026-11-16T03:41:57.9446126Z  * [new tag]         v0.1.12             -> v0.1.12
2026-11-16T03:41:57.9447466Z  * [new tag]         v0.1.13             -> v0.1.13
2026-11-16T03:41:57.9447782Z  * [new tag]         v0.1.14             -> v0.1.14
2026-11-16T03:41:57.9448083Z  * [new tag]         v0.1.15             -> v0.1.15
2026-11-16T03:41:57.9448389Z  * [new tag]         v0.1.16             -> v0.1.16
2026-11-16T03:41:57.9448673Z  * [new tag]         v0.1.17             -> v0.1.17
2026-11-16T03:41:57.9448943Z  * [new tag]         v0.1.18             -> v0.1.18
2026-11-16T03:41:57.9449210Z  * [new tag]         v0.1.19             -> v0.1.19
2026-11-16T03:41:57.9449542Z  * [new tag]         v0.1.2              -> v0.1.2
2026-11-16T03:41:57.9449836Z  * [new tag]         v0.1.20             -> v0.1.20
2026-11-16T03:41:57.9450107Z  * [new tag]         v0.1.21             -> v0.1.21
2026-11-16T03:41:57.9450374Z  * [new tag]         v0.1.22             -> v0.1.22
2026-11-16T03:41:57.9450649Z  * [new tag]         v0.1.23             -> v0.1.23
2026-11-16T03:41:57.9450930Z  * [new tag]         v0.1.24             -> v0.1.24
2026-11-16T03:41:57.9451202Z  * [new tag]         v0.1.25             -> v0.1.25
2026-11-16T03:41:57.9451470Z  * [new tag]         v0.1.26             -> v0.1.26
2026-11-16T03:41:57.9451745Z  * [new tag]         v0.1.27             -> v0.1.27
2026-11-16T03:41:57.9452024Z  * [new tag]         v0.1.28             -> v0.1.28
2026-11-16T03:41:57.9452298Z  * [new tag]         v0.1.29             -> v0.1.29
2026-11-16T03:41:57.9452580Z  * [new tag]         v0.1.3              -> v0.1.3
2026-11-16T03:41:57.9452857Z  * [new tag]         v0.1.30             -> v0.1.30
2026-11-16T03:41:57.9453125Z  * [new tag]         v0.1.32             -> v0.1.32
2026-11-16T03:41:57.9453387Z  * [new tag]         v0.1.33             -> v0.1.33
2026-11-16T03:41:57.9453656Z  * [new tag]         v0.1.34             -> v0.1.34
2026-11-16T03:41:57.9453922Z  * [new tag]         v0.1.35             -> v0.1.35
2026-11-16T03:41:57.9454188Z  * [new tag]         v0.1.36             -> v0.1.36
2026-11-16T03:41:57.9454463Z  * [new tag]         v0.1.37             -> v0.1.37
2026-11-16T03:41:57.9454731Z  * [new tag]         v0.1.4              -> v0.1.4
2026-11-16T03:41:57.9455002Z  * [new tag]         v0.1.5              -> v0.1.5
2026-11-16T03:41:57.9455805Z  * [new tag]         v0.1.6              -> v0.1.6
2026-11-16T03:41:57.9456138Z  * [new tag]         v0.1.7              -> v0.1.7
2026-11-16T03:41:57.9456416Z  * [new tag]         v0.1.8              -> v0.1.8
2026-11-16T03:41:57.9456682Z  * [new tag]         v0.1.9              -> v0.1.9
2026-11-16T03:41:57.9458198Z [command]"C:\Program Files\Git\bin\git.exe" branch --list --remote origin/fix/0.1.38-abertura
2026-11-16T03:41:57.9818834Z   origin/fix/0.1.38-abertura
2026-11-16T03:41:57.9852571Z [command]"C:\Program Files\Git\bin\git.exe" rev-parse refs/remotes/origin/fix/0.1.38-abertura
2026-11-16T03:41:58.0184993Z ff136584974b55989c10598612235717508ec25a
2026-11-16T03:41:58.0187490Z ##[endgroup]
2026-11-16T03:41:58.0188143Z ##[group]Determining the checkout info
2026-11-16T03:41:58.0188854Z ##[endgroup]
2026-11-16T03:41:58.0189339Z [command]"C:\Program Files\Git\bin\git.exe" sparse-checkout disable
2026-11-16T03:41:58.0559517Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all extensions.worktreeConfig
2026-11-16T03:41:58.0843827Z ##[group]Checking out the ref
2026-11-16T03:41:58.0852806Z [command]"C:\Program Files\Git\bin\git.exe" checkout --progress --force -B fix/0.1.38-abertura refs/remotes/origin/fix/0.1.38-abertura
2026-11-16T03:41:58.3048352Z Switched to a new branch 'fix/0.1.38-abertura'
2026-11-16T03:41:58.3068867Z branch 'fix/0.1.38-abertura' set up to track 'origin/fix/0.1.38-abertura'.
2026-11-16T03:41:58.3114205Z ##[endgroup]
2026-11-16T03:41:58.3525246Z [command]"C:\Program Files\Git\bin\git.exe" log -1 --format=%H
2026-11-16T03:41:58.3793553Z ff136584974b55989c10598612235717508ec25a
2026-11-16T03:41:58.3826360Z ##[group]Removing auth
2026-11-16T03:41:58.3834555Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T03:41:58.4115532Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T03:41:58.8972275Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T03:41:58.9260059Z http.https://github.com/.extraheader
2026-11-16T03:41:58.9294762Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
2026-11-16T03:41:58.9576297Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T03:41:59.4154483Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T03:41:59.4432916Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T03:41:59.8989715Z ##[endgroup]
2026-11-16T03:41:59.9353727Z ##[group]Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
2026-11-16T03:41:59.9354191Z with:
2026-11-16T03:41:59.9354386Z   python-version: 3.12
2026-11-16T03:41:59.9354597Z   architecture: x64
2026-11-16T03:41:59.9354776Z   cache: pip
2026-11-16T03:41:59.9354999Z   cache-dependency-path: requirements-tested.txt
2026-11-16T03:41:59.9355289Z   check-latest: false
2026-11-16T03:41:59.9358031Z   token: ***
2026-11-16T03:41:59.9358230Z   update-environment: true
2026-11-16T03:41:59.9358457Z   allow-prereleases: false
2026-11-16T03:41:59.9358667Z   freethreaded: false
2026-11-16T03:41:59.9358853Z env:
2026-11-16T03:41:59.9359033Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:41:59.9359245Z ##[endgroup]
2026-11-16T03:42:00.0947678Z ##[group]Installed versions
2026-11-16T03:42:00.1173761Z (node:1012) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T03:42:00.1174762Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T03:42:00.1175489Z Successfully set up CPython (3.12.10)
2026-11-16T03:42:00.1176210Z ##[endgroup]
2026-11-16T03:42:02.7588011Z pip cache is not found
2026-11-16T03:42:02.7850635Z ##[group]Run python -m pip install -r requirements-tested.txt
2026-11-16T03:42:02.7851203Z [36;1mpython -m pip install -r requirements-tested.txt[0m
2026-11-16T03:42:02.7851711Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências Windows indisponíveis.' }[0m
2026-11-16T03:42:02.7852237Z [36;1mpython -m pip install --no-deps --no-build-isolation -e .[0m
2026-11-16T03:42:02.7852670Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Projeto não instalado.' }[0m
2026-11-16T03:42:02.7853009Z [36;1mpython -m pip check[0m
2026-11-16T03:42:02.7853358Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências inconsistentes.' }[0m
2026-11-16T03:42:02.7956325Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T03:42:02.7956771Z env:
2026-11-16T03:42:02.7956998Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:42:02.7957506Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:02.7958209Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:42:02.7958812Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:02.7959359Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:02.7959885Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:02.7960299Z ##[endgroup]
2026-11-16T03:42:05.7177650Z Collecting altgraph==0.17.5 (from -r requirements-tested.txt (line 1))
2026-11-16T03:42:05.9054228Z   Downloading altgraph-0.17.5-py2.py3-none-any.whl.metadata (7.5 kB)
2026-11-16T03:42:05.9950453Z Collecting certifi==2026.10.23 (from -r requirements-tested.txt (line 2))
2026-11-16T03:42:06.0135696Z   Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
2026-11-16T03:42:06.2328626Z Collecting cffi==2.1.1 (from -r requirements-tested.txt (line 3))
2026-11-16T03:42:06.2522956Z   Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
2026-11-16T03:42:06.4582349Z Collecting charset-normalizer==3.5.2 (from -r requirements-tested.txt (line 4))
2026-11-16T03:42:06.4815254Z   Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
2026-11-16T03:42:06.5424859Z Requirement already satisfied: colorama==0.4.6 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 5)) (0.4.6)
2026-11-16T03:42:06.7851939Z Collecting cryptography==50.0.2 (from -r requirements-tested.txt (line 6))
2026-11-16T03:42:06.8061528Z   Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl.metadata (4.4 kB)
2026-11-16T03:42:06.8858023Z Collecting google-api-core==2.44.0 (from -r requirements-tested.txt (line 7))
2026-11-16T03:42:06.9056963Z   Downloading google_api_core-2.44.0-py3-none-any.whl.metadata (3.2 kB)
2026-11-16T03:42:07.0003654Z Collecting google-api-python-client==2.202.0 (from -r requirements-tested.txt (line 8))
2026-11-16T03:42:07.0236134Z   Downloading google_api_python_client-2.202.0-py3-none-any.whl.metadata (6.9 kB)
2026-11-16T03:42:07.0876166Z Collecting google-auth-httplib2==0.4.4 (from -r requirements-tested.txt (line 9))
2026-11-16T03:42:07.1073662Z   Downloading google_auth_httplib2-0.4.4-py3-none-any.whl.metadata (3.0 kB)
2026-11-16T03:42:07.1742641Z Collecting google-auth-oauthlib==1.5.0 (from -r requirements-tested.txt (line 10))
2026-11-16T03:42:07.1921123Z   Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T03:42:07.2754175Z Collecting google-auth==2.62.2 (from -r requirements-tested.txt (line 11))
2026-11-16T03:42:07.2936056Z   Downloading google_auth-2.62.2-py3-none-any.whl.metadata (6.0 kB)
2026-11-16T03:42:07.3686864Z Collecting googleapis-common-protos==1.76.0 (from -r requirements-tested.txt (line 12))
2026-11-16T03:42:07.3875774Z   Downloading googleapis_common_protos-1.76.0-py3-none-any.whl.metadata (8.5 kB)
2026-11-16T03:42:07.4464047Z Collecting httplib2==0.32.1 (from -r requirements-tested.txt (line 13))
2026-11-16T03:42:07.4653222Z   Downloading httplib2-0.32.1-py3-none-any.whl.metadata (2.2 kB)
2026-11-16T03:42:07.5279282Z Collecting idna==3.20 (from -r requirements-tested.txt (line 14))
2026-11-16T03:42:07.5447733Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
2026-11-16T03:42:07.6058959Z Collecting iniconfig==2.3.1 (from -r requirements-tested.txt (line 15))
2026-11-16T03:42:07.6227393Z   Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
2026-11-16T03:42:07.6886752Z Collecting jaraco-classes==3.4.0 (from -r requirements-tested.txt (line 16))
2026-11-16T03:42:07.7059173Z   Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T03:42:07.7660564Z Collecting jaraco-context==6.1.2 (from -r requirements-tested.txt (line 17))
2026-11-16T03:42:07.7840850Z   Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
2026-11-16T03:42:07.8502380Z Collecting jaraco-functools==4.6.0 (from -r requirements-tested.txt (line 18))
2026-11-16T03:42:07.8673845Z   Downloading jaraco_functools-4.6.0-py3-none-any.whl.metadata (2.9 kB)
2026-11-16T03:42:07.9461239Z Collecting keyring==25.7.0 (from -r requirements-tested.txt (line 19))
2026-11-16T03:42:07.9672247Z   Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
2026-11-16T03:42:08.0378898Z Collecting more-itertools==11.2.1 (from -r requirements-tested.txt (line 20))
2026-11-16T03:42:08.0548541Z   Downloading more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
2026-11-16T03:42:08.1226321Z Collecting oauthlib==4.0.1 (from -r requirements-tested.txt (line 21))
2026-11-16T03:42:08.1425254Z   Downloading oauthlib-4.0.1-py3-none-any.whl.metadata (8.6 kB)
2026-11-16T03:42:08.2179640Z Collecting opentelemetry-api==1.45.2 (from -r requirements-tested.txt (line 22))
2026-11-16T03:42:08.2375544Z   Downloading opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB)
2026-11-16T03:42:08.2597331Z Requirement already satisfied: packaging==26.3 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 23)) (26.3)
2026-11-16T03:42:08.2971050Z Collecting pefile==2024.8.26 (from -r requirements-tested.txt (line 24))
2026-11-16T03:42:08.3149374Z   Downloading pefile-2024.8.26-py3-none-any.whl.metadata (1.4 kB)
2026-11-16T03:42:08.3815629Z Collecting pluggy==1.7.0 (from -r requirements-tested.txt (line 25))
2026-11-16T03:42:08.3988042Z   Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
2026-11-16T03:42:08.4632968Z Collecting proto-plus==1.29.0 (from -r requirements-tested.txt (line 26))
2026-11-16T03:42:08.4822619Z   Downloading proto_plus-1.29.0-py3-none-any.whl.metadata (2.2 kB)
2026-11-16T03:42:08.7152095Z Collecting protobuf==7.36.2 (from -r requirements-tested.txt (line 27))
2026-11-16T03:42:08.7328886Z   Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
2026-11-16T03:42:08.7982796Z Collecting pyasn1-modules==0.4.2 (from -r requirements-tested.txt (line 28))
2026-11-16T03:42:08.8155285Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
2026-11-16T03:42:08.8899871Z Collecting pyasn1==0.6.5 (from -r requirements-tested.txt (line 29))
2026-11-16T03:42:08.9086472Z   Downloading pyasn1-0.6.5-py3-none-any.whl.metadata (8.4 kB)
2026-11-16T03:42:08.9685410Z Collecting pycparser==3.12 (from -r requirements-tested.txt (line 30))
2026-11-16T03:42:08.9850446Z   Downloading pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
2026-11-16T03:42:09.0554324Z Collecting pygments==2.21.0 (from -r requirements-tested.txt (line 31))
2026-11-16T03:42:09.0729654Z   Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
2026-11-16T03:42:09.1384350Z Collecting pyinstaller-hooks-contrib==2026.10 (from -r requirements-tested.txt (line 32))
2026-11-16T03:42:09.1556078Z   Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl.metadata (16 kB)
2026-11-16T03:42:09.2517821Z Collecting pyinstaller==6.22.3 (from -r requirements-tested.txt (line 33))
2026-11-16T03:42:09.2688747Z   Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl.metadata (8.5 kB)
2026-11-16T03:42:09.3413720Z Collecting pyparsing==3.3.3 (from -r requirements-tested.txt (line 34))
2026-11-16T03:42:09.3629299Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
2026-11-16T03:42:09.4414942Z Collecting pyside6-addons==6.8.3 (from -r requirements-tested.txt (line 35))
2026-11-16T03:42:09.4628878Z   Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.4 kB)
2026-11-16T03:42:09.5369808Z Collecting pyside6-essentials==6.8.3 (from -r requirements-tested.txt (line 36))
2026-11-16T03:42:09.5559869Z   Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.1 kB)
2026-11-16T03:42:09.6273444Z Collecting pyside6==6.8.3 (from -r requirements-tested.txt (line 37))
2026-11-16T03:42:09.6469054Z   Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl.metadata (5.7 kB)
2026-11-16T03:42:09.7285364Z Collecting pytest==9.2.0 (from -r requirements-tested.txt (line 38))
2026-11-16T03:42:09.7787104Z   Downloading pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
2026-11-16T03:42:09.8460935Z Collecting pywin32-ctypes==0.2.3 (from -r requirements-tested.txt (line 39))
2026-11-16T03:42:09.8733059Z   Downloading pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
2026-11-16T03:42:09.9408832Z Collecting requests-oauthlib==2.0.0 (from -r requirements-tested.txt (line 40))
2026-11-16T03:42:09.9589064Z   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
2026-11-16T03:42:10.0247687Z Collecting requests==2.34.2 (from -r requirements-tested.txt (line 41))
2026-11-16T03:42:10.0450514Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-11-16T03:42:10.1938104Z Collecting setuptools==84.2.1 (from -r requirements-tested.txt (line 42))
2026-11-16T03:42:10.2139272Z   Downloading setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
2026-11-16T03:42:10.3074227Z Collecting shiboken6==6.8.3 (from -r requirements-tested.txt (line 43))
2026-11-16T03:42:10.3368609Z   Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl.metadata (2.8 kB)
2026-11-16T03:42:10.4105882Z Collecting typing-extensions==4.16.0 (from -r requirements-tested.txt (line 44))
2026-11-16T03:42:10.4280030Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-11-16T03:42:10.4939012Z Collecting tzdata==2026.6 (from -r requirements-tested.txt (line 45))
2026-11-16T03:42:10.5136334Z   Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
2026-11-16T03:42:10.5715563Z Collecting uritemplate==4.2.0 (from -r requirements-tested.txt (line 46))
2026-11-16T03:42:10.5887702Z   Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T03:42:10.6654109Z Collecting urllib3==2.8.0 (from -r requirements-tested.txt (line 47))
2026-11-16T03:42:10.6842547Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
2026-11-16T03:42:10.8000462Z Downloading altgraph-0.17.5-py2.py3-none-any.whl (21 kB)
2026-11-16T03:42:10.8381208Z Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
2026-11-16T03:42:10.8898085Z Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl (185 kB)
2026-11-16T03:42:10.9386688Z Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
2026-11-16T03:42:11.0267967Z Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl (3.8 MB)
2026-11-16T03:42:11.1229348Z    ---------------------------------------- 3.8/3.8 MB 45.7 MB/s  0:00:00
2026-11-16T03:42:11.1399618Z Downloading google_api_core-2.44.0-py3-none-any.whl (225 kB)
2026-11-16T03:42:11.1794409Z Downloading google_auth-2.62.2-py3-none-any.whl (270 kB)
2026-11-16T03:42:11.2272210Z Downloading googleapis_common_protos-1.76.0-py3-none-any.whl (307 kB)
2026-11-16T03:42:11.2782906Z Downloading opentelemetry_api-1.45.2-py3-none-any.whl (60 kB)
2026-11-16T03:42:11.3227495Z Downloading proto_plus-1.29.0-py3-none-any.whl (50 kB)
2026-11-16T03:42:11.3671127Z Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
2026-11-16T03:42:11.4137183Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-11-16T03:42:11.4503534Z Downloading idna-3.20-py3-none-any.whl (69 kB)
2026-11-16T03:42:11.4914714Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
2026-11-16T03:42:11.5355991Z Downloading google_api_python_client-2.202.0-py3-none-any.whl (17.1 MB)
2026-11-16T03:42:11.7644615Z    ---------------------------------------- 17.1/17.1 MB 77.1 MB/s  0:00:00
2026-11-16T03:42:11.7838679Z Downloading google_auth_httplib2-0.4.4-py3-none-any.whl (9.5 kB)
2026-11-16T03:42:11.8240825Z Downloading httplib2-0.32.1-py3-none-any.whl (92 kB)
2026-11-16T03:42:11.8732588Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
2026-11-16T03:42:11.9311628Z Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
2026-11-16T03:42:11.9809888Z Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl (20 kB)
2026-11-16T03:42:12.0199278Z Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
2026-11-16T03:42:12.0570575Z Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
2026-11-16T03:42:12.0978623Z Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
2026-11-16T03:42:12.1535400Z Downloading jaraco_functools-4.6.0-py3-none-any.whl (11 kB)
2026-11-16T03:42:12.2816788Z Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
2026-11-16T03:42:12.3164043Z Downloading more_itertools-11.2.1-py3-none-any.whl (74 kB)
2026-11-16T03:42:12.3605298Z Downloading oauthlib-4.0.1-py3-none-any.whl (161 kB)
2026-11-16T03:42:12.4006536Z Downloading pefile-2024.8.26-py3-none-any.whl (74 kB)
2026-11-16T03:42:12.4459640Z Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
2026-11-16T03:42:12.5060300Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
2026-11-16T03:42:12.5467605Z Downloading pyasn1-0.6.5-py3-none-any.whl (84 kB)
2026-11-16T03:42:12.6072579Z Downloading pycparser-3.12-py3-none-any.whl (62 kB)
2026-11-16T03:42:12.6465523Z Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
2026-11-16T03:42:12.6815446Z    ---------------------------------------- 1.3/1.3 MB 31.9 MB/s  0:00:00
2026-11-16T03:42:12.7013240Z Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl (463 kB)
2026-11-16T03:42:12.7680214Z Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl (1.5 MB)
2026-11-16T03:42:12.8055886Z    ---------------------------------------- 1.5/1.5 MB 37.3 MB/s  0:00:00
2026-11-16T03:42:12.8325287Z Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl (127.9 MB)
2026-11-16T03:42:16.7839054Z    ---------------------------------------- 127.9/127.9 MB 32.3 MB/s  0:00:03
2026-11-16T03:42:16.8035210Z Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl (72.2 MB)
2026-11-16T03:42:19.0840949Z    ---------------------------------------- 72.2/72.2 MB 31.7 MB/s  0:00:02
2026-11-16T03:42:19.1023916Z Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl (561 kB)
2026-11-16T03:42:19.1371252Z    ---------------------------------------- 561.1/561.1 kB 9.3 MB/s  0:00:00
2026-11-16T03:42:19.1555033Z Downloading pytest-9.2.0-py3-none-any.whl (411 kB)
2026-11-16T03:42:19.2780357Z Downloading pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
2026-11-16T03:42:19.3897193Z Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
2026-11-16T03:42:19.4281013Z Downloading setuptools-84.2.1-py3-none-any.whl (876 kB)
2026-11-16T03:42:19.4587112Z    ---------------------------------------- 876.3/876.3 kB 19.8 MB/s  0:00:00
2026-11-16T03:42:19.4792278Z Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl (1.2 MB)
2026-11-16T03:42:19.5163215Z    ---------------------------------------- 1.2/1.2 MB 28.7 MB/s  0:00:00
2026-11-16T03:42:19.5345975Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-11-16T03:42:19.5728103Z Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
2026-11-16T03:42:20.3246061Z Installing collected packages: altgraph, urllib3, uritemplate, tzdata, typing-extensions, shiboken6, setuptools, pywin32-ctypes, pyparsing, pyinstaller-hooks-contrib, pygments, pycparser, pyasn1, protobuf, pluggy, pefile, oauthlib, more-itertools, jaraco-context, iniconfig, idna, charset-normalizer, certifi, requests, pytest, pyside6-essentials, pyinstaller, pyasn1-modules, proto-plus, opentelemetry-api, jaraco-functools, jaraco-classes, httplib2, googleapis-common-protos, cffi, requests-oauthlib, pyside6-addons, keyring, cryptography, pyside6, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-core, google-api-python-client
2026-11-16T03:42:50.1487485Z 
2026-11-16T03:42:50.1540756Z Successfully installed altgraph-0.17.5 certifi-2026.10.23 cffi-2.1.1 charset-normalizer-3.5.2 cryptography-50.0.2 google-api-core-2.44.0 google-api-python-client-2.202.0 google-auth-2.62.2 google-auth-httplib2-0.4.4 google-auth-oauthlib-1.5.0 googleapis-common-protos-1.76.0 httplib2-0.32.1 idna-3.20 iniconfig-2.3.1 jaraco-classes-3.4.0 jaraco-context-6.1.2 jaraco-functools-4.6.0 keyring-25.7.0 more-itertools-11.2.1 oauthlib-4.0.1 opentelemetry-api-1.45.2 pefile-2024.8.26 pluggy-1.7.0 proto-plus-1.29.0 protobuf-7.36.2 pyasn1-0.6.5 pyasn1-modules-0.4.2 pycparser-3.12 pygments-2.21.0 pyinstaller-6.22.3 pyinstaller-hooks-contrib-2026.10 pyparsing-3.3.3 pyside6-6.8.3 pyside6-addons-6.8.3 pyside6-essentials-6.8.3 pytest-9.2.0 pywin32-ctypes-0.2.3 requests-2.34.2 requests-oauthlib-2.0.0 setuptools-84.2.1 shiboken6-6.8.3 typing-extensions-4.16.0 tzdata-2026.6 uritemplate-4.2.0 urllib3-2.8.0
2026-11-16T03:42:51.5371103Z Obtaining file:///D:/a/Checkpoint/Checkpoint
2026-11-16T03:42:51.5395389Z   Checking if build backend supports build_editable: started
2026-11-16T03:42:51.9129634Z   Checking if build backend supports build_editable: finished with status 'done'
2026-11-16T03:42:51.9155138Z   Preparing editable metadata (pyproject.toml): started
2026-11-16T03:42:52.3450730Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
2026-11-16T03:42:52.3520916Z Building wheels for collected packages: checkpoint-desktop
2026-11-16T03:42:52.3546202Z   Building editable for checkpoint-desktop (pyproject.toml): started
2026-11-16T03:42:52.8687488Z   Building editable for checkpoint-desktop (pyproject.toml): finished with status 'done'
2026-11-16T03:42:52.8703242Z   C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\setuptools\command\editable_wheel.py:354: BuildBackendWarning: Editable installation.
2026-11-16T03:42:52.8704398Z   !!
2026-11-16T03:42:52.8704630Z   
2026-11-16T03:42:52.8705215Z           ********************************************************************************
2026-11-16T03:42:52.8706021Z           Please be careful with folders in your working directory with the same
2026-11-16T03:42:52.8706815Z           name as your package as they may take precedence during imports.
2026-11-16T03:42:52.8707538Z           ********************************************************************************
2026-11-16T03:42:52.8708077Z   
2026-11-16T03:42:52.8708330Z   !!
2026-11-16T03:42:52.8708726Z     with strategy, WheelFile(wheel_path, "w") as wheel_obj:
2026-11-16T03:42:52.8742729Z   Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.38-0.editable-py3-none-any.whl size=3272 sha256=c5018ff004334ae06e1dbd76aa49c4f54bd5048f5e2d2941575e731f0f66e535
2026-11-16T03:42:52.8744823Z   Stored in directory: C:\Users\runneradmin\AppData\Local\Temp\pip-ephem-wheel-cache-ol6_pua1\wheels\a2\38\6e\88ad7ec70fd74394064971fa20d15ccdcdb6f76505932df31d
2026-11-16T03:42:52.8774167Z Successfully built checkpoint-desktop
2026-11-16T03:42:52.9020889Z Installing collected packages: checkpoint-desktop
2026-11-16T03:42:52.9467731Z Successfully installed checkpoint-desktop-0.1.38
2026-11-16T03:42:53.3970449Z No broken requirements found.
2026-11-16T03:42:53.5444211Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-ui-tests'
2026-11-16T03:42:53.5444956Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-ui-tests'[0m
2026-11-16T03:42:53.5445600Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
2026-11-16T03:42:53.5446173Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
2026-11-16T03:42:53.5487810Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T03:42:53.5488169Z env:
2026-11-16T03:42:53.5488369Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:42:53.5488690Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:53.5489151Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:42:53.5489623Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:53.5490092Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:53.5490542Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:42:53.5490858Z ##[endgroup]
2026-11-16T03:43:08.5469059Z ........................................................................ [ 10%]
2026-11-16T03:43:20.3267854Z ........................................................................ [ 20%]
2026-11-16T03:43:35.8553185Z ........................................................................ [ 30%]
2026-11-16T03:43:41.0145097Z ........................................................................ [ 41%]
2026-11-16T03:44:10.7922342Z ........................................................................ [ 51%]
2026-11-16T03:45:52.8232406Z ........................................................................ [ 61%]
2026-11-16T03:46:34.6411738Z ........................................................................ [ 72%]
2026-11-16T03:48:35.3230962Z ........................................................................ [ 82%]
2026-11-16T03:52:50.9225563Z ........................................................................ [ 92%]
2026-11-16T03:54:08.0454344Z ....................................................                     [100%]
2026-11-16T03:54:08.0455070Z 700 passed in 673.05s (0:11:13)
2026-11-16T03:54:09.0124023Z ##[group]Run ./scripts/build.ps1 -Python (Get-Command python).Source
2026-11-16T03:54:09.0124694Z [36;1m./scripts/build.ps1 -Python (Get-Command python).Source[0m
2026-11-16T03:54:09.0165463Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T03:54:09.0165877Z env:
2026-11-16T03:54:09.0166121Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:54:09.0166491Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:54:09.0167023Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:54:09.0167538Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:54:09.0167999Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:54:09.0168477Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:54:09.0168881Z ##[endgroup]
2026-11-16T03:54:10.0457410Z 218 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
2026-11-16T03:54:10.0460181Z 218 INFO: Python: 3.12.10
2026-11-16T03:54:10.0673309Z 234 INFO: Platform: Windows-2022Server-10.0.20348-SP0
2026-11-16T03:54:10.0673916Z 234 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:54:10.0679620Z 234 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint.spec
2026-11-16T03:54:10.1180162Z 296 INFO: Module search paths (PYTHONPATH):
2026-11-16T03:54:10.1181069Z ['D:\\a\\Checkpoint\\Checkpoint',
2026-11-16T03:54:10.1181863Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
2026-11-16T03:54:10.1182652Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
2026-11-16T03:54:10.1183156Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
2026-11-16T03:54:10.1183656Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
2026-11-16T03:54:10.1184199Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
2026-11-16T03:54:10.1184807Z  '__editable__.checkpoint_desktop-0.1.38.finder.__path_hook__',
2026-11-16T03:54:10.1185273Z  'D:\\a\\Checkpoint\\Checkpoint']
2026-11-16T03:54:10.3679982Z 547 INFO: Appending 'datas' from .spec
2026-11-16T03:54:10.3702629Z 547 INFO: checking Analysis
2026-11-16T03:54:10.3703739Z 547 INFO: Building Analysis because Analysis-00.toc is non existent
2026-11-16T03:54:10.3704600Z 547 INFO: Looking for Python shared library...
2026-11-16T03:54:10.3705618Z 547 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
2026-11-16T03:54:10.3706406Z 547 INFO: Running Analysis Analysis-00.toc
2026-11-16T03:54:10.3707073Z 547 INFO: Target bytecode optimization level: 0
2026-11-16T03:54:10.3707707Z 547 INFO: Initializing module dependency graph...
2026-11-16T03:54:10.3716576Z 547 INFO: Initializing module graph hook caches...
2026-11-16T03:54:10.3875821Z 562 INFO: Analyzing modules for base_library.zip ...
2026-11-16T03:54:11.3016179Z 1469 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:11.8245572Z 2001 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:12.8601516Z 3033 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:13.7618578Z 3940 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:14.3285702Z 4504 INFO: Caching module dependency graph...
2026-11-16T03:54:14.3681241Z 4535 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_checkpoint.py
2026-11-16T03:54:14.5345368Z 4708 INFO: Processing standard module hook 'hook-PySide6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:14.6953197Z 4864 INFO: Processing standard module hook 'hook-shiboken6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:14.8217268Z 4989 INFO: Processing standard module hook 'hook-PySide6.QtNetwork.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:17.2829518Z 7460 INFO: Processing standard module hook 'hook-PySide6.QtCore.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:20.6752870Z 10839 INFO: Processing standard module hook 'hook-PySide6.QtWidgets.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:24.1107641Z 14281 INFO: Processing standard module hook 'hook-PySide6.QtGui.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:57.7540806Z 47926 INFO: Processing standard module hook 'hook-sqlite3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:58.0362188Z 48208 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:58.2087128Z 48380 INFO: Processing standard module hook 'hook-keyring.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:58.6741935Z 48848 INFO: Processing pre-safe-import-module hook 'hook-jaraco.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:58.6749708Z 48848 INFO: SetuptoolsInfo: initializing cached setuptools info...
2026-11-16T03:54:59.1707243Z 49349 INFO: Setuptools: 'jaraco' appears to be a partial setuptools-vendored copy - extending search paths to ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\jaraco', 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\setuptools\\_vendor\\jaraco']!
2026-11-16T03:54:59.1715380Z 49349 INFO: Processing pre-safe-import-module hook 'hook-jaraco.context.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.3982455Z 49568 INFO: Processing pre-safe-import-module hook 'hook-backports.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.3984569Z 49568 INFO: Setuptools: 'backports' appears to be a full setuptools-vendored copy - creating alias to 'setuptools._vendor.backports'!
2026-11-16T03:54:59.4040014Z 49584 INFO: Processing standard module hook 'hook-setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:59.4152932Z 49584 INFO: Processing pre-safe-import-module hook 'hook-distutils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.4703921Z 49646 INFO: Processing standard module hook 'hook-sysconfig.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:59.4810609Z 49646 INFO: Processing pre-safe-import-module hook 'hook-jaraco.functools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.4914721Z 49662 INFO: Processing pre-safe-import-module hook 'hook-more_itertools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.6647896Z 49834 INFO: Processing standard module hook 'hook-_osx_support.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:54:59.6690687Z 49834 INFO: Processing pre-safe-import-module hook 'hook-typing_extensions.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:54:59.9409681Z 50115 INFO: Processing standard module hook 'hook-multiprocessing.util.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:00.0290284Z 50209 INFO: Processing standard module hook 'hook-xml.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:00.2626033Z 50428 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:00.6143431Z 50787 INFO: Processing pre-safe-import-module hook 'hook-packaging.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:00.9774733Z 51147 INFO: Processing pre-safe-import-module hook 'hook-jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:00.9776861Z 51147 INFO: Setuptools: 'jaraco.text' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.jaraco.text'!
2026-11-16T03:55:00.9893164Z 51162 INFO: Processing standard module hook 'hook-setuptools._vendor.jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:00.9906845Z 51162 INFO: Processing pre-safe-import-module hook 'hook-importlib_resources.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:01.4004475Z 51569 INFO: Processing pre-safe-import-module hook 'hook-tomli.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:01.4006522Z 51569 INFO: Setuptools: 'tomli' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.tomli'!
2026-11-16T03:55:02.0072832Z 52179 INFO: Processing pre-safe-import-module hook 'hook-wheel.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:02.0074956Z 52179 INFO: Setuptools: 'wheel' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.wheel'!
2026-11-16T03:55:02.1305783Z 52310 INFO: Processing pre-safe-import-module hook 'hook-importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:02.1307626Z 52310 INFO: Setuptools: 'importlib_metadata' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.importlib_metadata'!
2026-11-16T03:55:02.1533891Z 52325 INFO: Processing standard module hook 'hook-setuptools._vendor.importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:02.1738695Z 52352 INFO: Processing pre-safe-import-module hook 'hook-zipp.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:02.1740537Z 52352 INFO: Setuptools: 'zipp' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.zipp'!
2026-11-16T03:55:02.2222707Z 52399 INFO: Processing standard module hook 'hook-win32ctypes.core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:03.0042868Z 53180 INFO: Processing standard module hook 'hook-pycparser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:03.4752908Z 53649 INFO: Processing standard module hook 'hook-webbrowser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:03.7530245Z 53930 INFO: Processing standard module hook 'hook-cryptography.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:04.9593188Z 55134 INFO: hook-cryptography: cryptography does not seem to be using dynamically linked OpenSSL.
2026-11-16T03:55:05.7021571Z 55869 INFO: Processing standard module hook 'hook-urllib3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:06.1911788Z 56370 INFO: Processing standard module hook 'hook-certifi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:06.2382378Z 56417 INFO: Processing standard module hook 'hook-charset_normalizer.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:06.9177547Z 57090 INFO: Processing standard module hook 'hook-google.api_core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:06.9434809Z 57121 INFO: Processing standard module hook 'hook-opentelemetry.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:07.2547323Z 57419 INFO: Processing standard module hook 'hook-httplib2.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:07.5934948Z 57763 INFO: Processing standard module hook 'hook-difflib.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:07.8231003Z 57997 INFO: Processing standard module hook 'hook-googleapiclient.model.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T03:55:08.3153472Z 58483 INFO: Processing standard module hook 'hook-PySide6.QtSvg.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:09.1614863Z 59329 INFO: Processing standard module hook 'hook-xml.etree.cElementTree.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:09.4627748Z 59641 INFO: Processing module hooks (post-graph stage)...
2026-11-16T03:55:09.4829401Z 59656 WARNING: Hidden import "pycparser.lextab" not found!
2026-11-16T03:55:09.4830614Z 59656 WARNING: Hidden import "pycparser.yacctab" not found!
2026-11-16T03:55:09.5087722Z 59688 INFO: Processing pre-safe-import-module hook 'hook-gi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T03:55:09.6591504Z 59828 INFO: Performing binary vs. data reclassification (813 entries)
2026-11-16T03:55:09.7305740Z 59906 INFO: Looking for ctypes DLLs
2026-11-16T03:55:09.7664546Z 59938 INFO: Analyzing run-time hooks ...
2026-11-16T03:55:09.7711007Z 59938 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:09.7735943Z 59938 INFO: Including run-time hook 'pyi_rth_pkgutil.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:09.7755274Z 59953 INFO: Including run-time hook 'pyi_rth_multiprocessing.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:09.7776080Z 59953 INFO: Including run-time hook 'pyi_rth_setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:09.7788216Z 59953 INFO: Including run-time hook 'pyi_rth_pyside6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:09.7805190Z 59953 INFO: Processing pre-find-module-path hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path'
2026-11-16T03:55:09.7818591Z 59953 INFO: Processing standard module hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:09.7844785Z 59953 INFO: Including run-time hook 'pyi_rth_cryptography_openssl.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\rthooks'
2026-11-16T03:55:09.8175128Z 59985 INFO: Creating base_library.zip...
2026-11-16T03:55:09.8389221Z 60016 INFO: Looking for dynamic libraries
2026-11-16T03:55:10.6062587Z 60782 INFO: Extra DLL search directories (AddDllDirectory): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\shiboken6']
2026-11-16T03:55:10.6063627Z 60782 INFO: Extra DLL search directories (PATH): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PySide6']
2026-11-16T03:55:12.4521552Z 62627 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\warn-Checkpoint.txt
2026-11-16T03:55:12.5391834Z 62706 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\xref-Checkpoint.html
2026-11-16T03:55:12.5894254Z 62768 INFO: checking PYZ
2026-11-16T03:55:12.5895514Z 62768 INFO: Building PYZ because PYZ-00.toc is non existent
2026-11-16T03:55:12.5896892Z 62768 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz
2026-11-16T03:55:13.3252313Z 63503 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz completed successfully.
2026-11-16T03:55:13.3522759Z 63518 INFO: checking PKG
2026-11-16T03:55:13.3523615Z 63518 INFO: Building PKG because PKG-00.toc is non existent
2026-11-16T03:55:13.3524619Z 63518 INFO: Building PKG (CArchive) Checkpoint.pkg
2026-11-16T03:55:13.3707530Z 63550 INFO: Building PKG (CArchive) Checkpoint.pkg completed successfully.
2026-11-16T03:55:13.3715556Z 63550 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\runw.exe
2026-11-16T03:55:13.3716837Z 63550 INFO: checking EXE
2026-11-16T03:55:13.3717298Z 63550 INFO: Building EXE because EXE-00.toc is non existent
2026-11-16T03:55:13.3718343Z 63550 INFO: Building EXE from EXE-00.toc
2026-11-16T03:55:13.3719957Z 63550 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\Checkpoint.exe
2026-11-16T03:55:13.3748784Z 63550 INFO: Copying icon to EXE
2026-11-16T03:55:13.3766312Z 63550 INFO: Copying 0 resources to EXE
2026-11-16T03:55:13.3767158Z 63550 INFO: Embedding manifest in EXE
2026-11-16T03:55:13.3781037Z 63550 INFO: Appending PKG archive to EXE
2026-11-16T03:55:13.3823034Z 63550 INFO: Fixing EXE headers
2026-11-16T03:55:13.4612176Z 63628 INFO: Building EXE from EXE-00.toc completed successfully.
2026-11-16T03:55:13.4710404Z 63644 INFO: checking COLLECT
2026-11-16T03:55:13.4711239Z 63644 INFO: Building COLLECT because COLLECT-00.toc is non existent
2026-11-16T03:55:13.4714316Z 63644 INFO: Building COLLECT COLLECT-00.toc
2026-11-16T03:55:14.1114454Z 64284 INFO: Building COLLECT COLLECT-00.toc completed successfully.
2026-11-16T03:55:14.1303445Z 64300 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\dist
2026-11-16T03:55:14.4895266Z 142 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
2026-11-16T03:55:14.4899749Z 142 INFO: Python: 3.12.10
2026-11-16T03:55:14.5116774Z 157 INFO: Platform: Windows-2022Server-10.0.20348-SP0
2026-11-16T03:55:14.5123042Z 157 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:14.5124665Z 157 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\CheckpointUpdater.spec
2026-11-16T03:55:14.5160557Z 173 INFO: Module search paths (PYTHONPATH):
2026-11-16T03:55:14.5161192Z ['D:\\a\\Checkpoint\\Checkpoint',
2026-11-16T03:55:14.5161999Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
2026-11-16T03:55:14.5162936Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
2026-11-16T03:55:14.5163624Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
2026-11-16T03:55:14.5164132Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
2026-11-16T03:55:14.5164716Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
2026-11-16T03:55:14.5165337Z  '__editable__.checkpoint_desktop-0.1.38.finder.__path_hook__',
2026-11-16T03:55:14.5165836Z  'D:\\a\\Checkpoint\\Checkpoint']
2026-11-16T03:55:14.7516203Z 407 INFO: checking Analysis
2026-11-16T03:55:14.7516897Z 407 INFO: Building Analysis because Analysis-00.toc is non existent
2026-11-16T03:55:14.7517672Z 407 INFO: Looking for Python shared library...
2026-11-16T03:55:14.7519310Z 407 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
2026-11-16T03:55:14.7520044Z 407 INFO: Running Analysis Analysis-00.toc
2026-11-16T03:55:14.7520878Z 407 INFO: Target bytecode optimization level: 0
2026-11-16T03:55:14.7521608Z 407 INFO: Initializing module dependency graph...
2026-11-16T03:55:14.7531710Z 407 INFO: Initializing module graph hook caches...
2026-11-16T03:55:14.7683415Z 423 INFO: Analyzing modules for base_library.zip ...
2026-11-16T03:55:15.6259844Z 1283 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:15.7133788Z 1361 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:16.9855829Z 2643 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:17.1789373Z 2831 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:18.6030257Z 4255 INFO: Caching module dependency graph...
2026-11-16T03:55:18.6428022Z 4302 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_updater.py
2026-11-16T03:55:18.6659249Z 4317 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:18.7377137Z 4395 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T03:55:18.7485646Z 4395 INFO: Processing module hooks (post-graph stage)...
2026-11-16T03:55:18.7547875Z 4411 INFO: Performing binary vs. data reclassification (1 entries)
2026-11-16T03:55:18.7557988Z 4411 INFO: Looking for ctypes DLLs
2026-11-16T03:55:18.7622714Z 4411 INFO: Analyzing run-time hooks ...
2026-11-16T03:55:18.7631767Z 4411 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T03:55:18.7680937Z 4427 INFO: Creating base_library.zip...
2026-11-16T03:55:18.7881933Z 4442 INFO: Looking for dynamic libraries
2026-11-16T03:55:18.8993713Z 4552 INFO: Extra DLL search directories (AddDllDirectory): []
2026-11-16T03:55:18.8994384Z 4552 INFO: Extra DLL search directories (PATH): []
2026-11-16T03:55:19.2070483Z 4864 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\warn-CheckpointUpdater.txt
2026-11-16T03:55:19.2232120Z 4880 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\xref-CheckpointUpdater.html
2026-11-16T03:55:19.2379573Z 4896 INFO: checking PYZ
2026-11-16T03:55:19.2380591Z 4896 INFO: Building PYZ because PYZ-00.toc is non existent
2026-11-16T03:55:19.2381515Z 4896 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz
2026-11-16T03:55:19.3904129Z 5036 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz completed successfully.
2026-11-16T03:55:19.3943003Z 5052 INFO: checking PKG
2026-11-16T03:55:19.3943852Z 5052 INFO: Building PKG because PKG-00.toc is non existent
2026-11-16T03:55:19.3945171Z 5052 INFO: Building PKG (CArchive) CheckpointUpdater.pkg
2026-11-16T03:55:19.4062357Z 5060 INFO: Building PKG (CArchive) CheckpointUpdater.pkg completed successfully.
2026-11-16T03:55:19.4069256Z 5060 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\run.exe
2026-11-16T03:55:19.4070717Z 5060 INFO: checking EXE
2026-11-16T03:55:19.4071163Z 5060 INFO: Building EXE because EXE-00.toc is non existent
2026-11-16T03:55:19.4071689Z 5060 INFO: Building EXE from EXE-00.toc
2026-11-16T03:55:19.4072832Z 5060 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\CheckpointUpdater.exe
2026-11-16T03:55:19.4091373Z 5068 INFO: Copying icon to EXE
2026-11-16T03:55:19.4109252Z 5068 INFO: Copying 0 resources to EXE
2026-11-16T03:55:19.4110045Z 5068 INFO: Embedding manifest in EXE
2026-11-16T03:55:19.4124432Z 5068 INFO: Appending PKG archive to EXE
2026-11-16T03:55:19.4132967Z 5068 INFO: Fixing EXE headers
2026-11-16T03:55:19.4805147Z 5131 INFO: Building EXE from EXE-00.toc completed successfully.
2026-11-16T03:55:19.4819644Z 5131 INFO: checking COLLECT
2026-11-16T03:55:19.4821016Z 5131 INFO: Building COLLECT because COLLECT-00.toc is non existent
2026-11-16T03:55:19.4822824Z 5131 INFO: Building COLLECT COLLECT-00.toc
2026-11-16T03:55:19.5195369Z 5178 INFO: Building COLLECT COLLECT-00.toc completed successfully.
2026-11-16T03:55:19.5210440Z 5178 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-dist
2026-11-16T03:55:19.6580657Z ##[group]Run python scripts/package_windows_release.py --test-report .ci-results/pytest.xml
2026-11-16T03:55:19.6581737Z [36;1mpython scripts/package_windows_release.py --test-report .ci-results/pytest.xml[0m
2026-11-16T03:55:19.6582348Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Smokes Windows falharam.' }[0m
2026-11-16T03:55:19.6621882Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T03:55:19.6622303Z env:
2026-11-16T03:55:19.6622546Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:55:19.6622902Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:19.6623406Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:55:19.6623907Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:19.6624353Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:19.6624767Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:19.6625183Z ##[endgroup]
2026-11-16T03:55:33.6918075Z Checkpoint smoke: 6 pages OK; SQLite integrity=ok
2026-11-16T03:55:34.9170915Z Cadastro smoke: salvar, auxiliar, renderiza��o e SQLite OK
2026-11-16T03:55:42.9194761Z Checkpoint 0.1.38 � Windows x64
2026-11-16T03:55:42.9195496Z Commit: ff136584974b55989c10598612235717508ec25a
2026-11-16T03:55:42.9196147Z Python: 3.12.10
2026-11-16T03:55:42.9196741Z Testes: {'tests': 700, 'failures': 0, 'errors': 0, 'skipped': 0}
2026-11-16T03:55:42.9197724Z Smoke do fonte: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
2026-11-16T03:55:42.9198847Z Smoke do ZIP extra�do: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
2026-11-16T03:55:42.9201076Z Auxiliar isolado do fonte e do ZIP extra�do: resposta e schema verificados.
2026-11-16T03:55:42.9203533Z Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
2026-11-16T03:55:42.9204779Z CheckpointUpdater.exe --check: sa�da 0.
2026-11-16T03:55:42.9207615Z Inicializa��o normal nativa Windows do fonte e do execut�vel extra�do: HWND vis�vel, resposta, captura, fechamento e SQLite verificados; executor j� elevado, sem automatizar consentimento UAC.
2026-11-16T03:55:42.9209871Z ZIP SHA-256: 9f2238c621d0fb5fc9ed22106bee34b938283ef3f8b0cd7e96770a757496cfce
2026-11-16T03:55:42.9211383Z Steam autenticada e homologa��o Windows 10/11 pessoal n�o est�o cobertas.
2026-11-16T03:55:43.0506010Z ##[group]Run python scripts/render_ui_review.py work/ui-review
2026-11-16T03:55:43.0506661Z [36;1mpython scripts/render_ui_review.py work/ui-review[0m
2026-11-16T03:55:43.0507139Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Capturas Windows falharam.' }[0m
2026-11-16T03:55:43.0507733Z [36;1mpython scripts/package_ui_review.py work/ui-review release-assets[0m
2026-11-16T03:55:43.0508336Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Empacotamento visual falhou.' }[0m
2026-11-16T03:55:43.0549172Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T03:55:43.0549611Z env:
2026-11-16T03:55:43.0549846Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:55:43.0550217Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:43.0550729Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:55:43.0551227Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:43.0551768Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:43.0552218Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:43.0552581Z ##[endgroup]
2026-11-16T03:55:45.0037394Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
2026-11-16T03:55:53.9615481Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
2026-11-16T03:55:54.2139710Z D:\a\Checkpoint\Checkpoint\work\ui-review
2026-11-16T03:55:54.5228360Z Revis�o visual: 61 PNGs e �ndice HTML; bases e logs exclu�dos.
2026-11-16T03:55:54.6521533Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
2026-11-16T03:55:54.6521993Z with:
2026-11-16T03:55:54.6522203Z   name: checkpoint-windows-ui-review
2026-11-16T03:55:54.6522472Z   path: release-assets/*
2026-11-16T03:55:54.6522700Z   if-no-files-found: error
2026-11-16T03:55:54.6522917Z   retention-days: 14
2026-11-16T03:55:54.6523118Z   compression-level: 6
2026-11-16T03:55:54.6523320Z   overwrite: false
2026-11-16T03:55:54.6523525Z   include-hidden-files: false
2026-11-16T03:55:54.6523751Z env:
2026-11-16T03:55:54.6523931Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:55:54.6524232Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:54.6524792Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:55:54.6525244Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:54.6525642Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:54.6526066Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:54.6526372Z ##[endgroup]
2026-11-16T03:55:54.8404723Z (node:3784) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T03:55:54.8405471Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T03:55:54.8501924Z With the provided path, there will be 10 files uploaded
2026-11-16T03:55:54.8507126Z Artifact name is valid!
2026-11-16T03:55:54.8509842Z Root directory input is valid!
2026-11-16T03:55:55.1538874Z Beginning upload of artifact content to blob storage
2026-11-16T03:55:55.4428766Z (node:3784) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T03:55:55.9556140Z Uploaded bytes 8388608
2026-11-16T03:55:56.1407481Z Uploaded bytes 16777216
2026-11-16T03:55:56.2653669Z Uploaded bytes 25165824
2026-11-16T03:55:56.4654647Z Uploaded bytes 33554432
2026-11-16T03:55:56.7188348Z Uploaded bytes 41943040
2026-11-16T03:55:56.9436400Z Uploaded bytes 50331648
2026-11-16T03:55:57.1946507Z Uploaded bytes 58720256
2026-11-16T03:55:57.4630538Z Uploaded bytes 67108864
2026-11-16T03:55:57.7412487Z Uploaded bytes 75497472
2026-11-16T03:55:58.0066304Z Uploaded bytes 83886080
2026-11-16T03:55:58.1270033Z Uploaded bytes 88049666
2026-11-16T03:55:58.1694490Z Finished uploading artifact content to blob storage!
2026-11-16T03:55:58.1699889Z SHA256 digest of uploaded artifact zip is 9f82a60919ca6a8c5b4faa09cae3397f301ddd002bddef64e42ea8f98d465c64
2026-11-16T03:55:58.1702971Z Finalizing artifact upload
2026-11-16T03:55:58.5134709Z Artifact checkpoint-windows-ui-review.zip successfully finalized. Artifact ID 14196740155
2026-11-16T03:55:58.5136202Z Artifact checkpoint-windows-ui-review has been successfully uploaded! Final size is 88049666 bytes. Artifact ID is 14196740155
2026-11-16T03:55:58.5147975Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43799707113/artifacts/14196740155
2026-11-16T03:55:58.5442347Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
2026-11-16T03:55:58.5442829Z with:
2026-11-16T03:55:58.5443035Z   name: checkpoint-windows-ui-tests
2026-11-16T03:55:58.5443311Z   path: .ci-results/pytest.xml
2026-11-16T03:55:58.5443547Z   if-no-files-found: ignore
2026-11-16T03:55:58.5443760Z   retention-days: 14
2026-11-16T03:55:58.5443960Z   compression-level: 6
2026-11-16T03:55:58.5444161Z   overwrite: false
2026-11-16T03:55:58.5444361Z   include-hidden-files: false
2026-11-16T03:55:58.5444592Z env:
2026-11-16T03:55:58.5444764Z   QT_QPA_PLATFORM: offscreen
2026-11-16T03:55:58.5445078Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:58.5445546Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T03:55:58.5445997Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:58.5446459Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:58.5446856Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T03:55:58.5447221Z ##[endgroup]
2026-11-16T03:55:58.7467297Z (node:3172) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T03:55:58.7468498Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T03:55:58.7526593Z With the provided path, there will be 1 file uploaded
2026-11-16T03:55:58.7533001Z Artifact name is valid!
2026-11-16T03:55:58.7535795Z Root directory input is valid!
2026-11-16T03:55:59.0616603Z Beginning upload of artifact content to blob storage
2026-11-16T03:55:59.0919634Z (node:3172) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T03:55:59.2388687Z Uploaded bytes 14333
2026-11-16T03:55:59.2839417Z Finished uploading artifact content to blob storage!
2026-11-16T03:55:59.2840529Z SHA256 digest of uploaded artifact zip is 77c9c53ad70d43c1c566a7ded9f8c53d7a94d0f942ff8deb94069a24eebf6f37
2026-11-16T03:55:59.2843585Z Finalizing artifact upload
2026-11-16T03:55:59.7046789Z Artifact checkpoint-windows-ui-tests.zip successfully finalized. Artifact ID 14196412237
2026-11-16T03:55:59.7048169Z Artifact checkpoint-windows-ui-tests has been successfully uploaded! Final size is 14333 bytes. Artifact ID is 14196412237
2026-11-16T03:55:59.7057726Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43799707113/artifacts/14196412237
2026-11-16T03:55:59.7384318Z Post job cleanup.
2026-11-16T03:55:59.8860832Z (node:3708) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T03:55:59.8861572Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T03:56:00.0142774Z [command]"C:\Program Files\Git\usr\bin\tar.exe" --posix -cf cache.tzst --exclude cache.tzst -P -C D:/a/Checkpoint/Checkpoint --files-from manifest.txt --force-local --use-compress-program "zstd -T0"
2026-11-16T03:56:00.9403481Z (node:3708) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T03:56:01.9271949Z Sent 30283249 of 231609841 (13.1%), 28.9 MBs/sec
2026-11-16T03:56:02.7785666Z Sent 231609841 of 231609841 (100.0%), 119.3 MBs/sec
2026-11-16T03:56:02.9719937Z Cache saved with the key: setup-python-Windows-x64-python-3.12.10-pip-eb71efc05b2754f3c8048b82aafb5b6c4b1d694285a4ae18da9e58d103e7bab6
2026-11-16T03:56:02.9970921Z Post job cleanup.
2026-11-16T03:56:03.1837636Z [command]"C:\Program Files\Git\bin\git.exe" version
2026-11-16T03:56:03.2109235Z git version 2.56.1.windows.1
2026-11-16T03:56:03.2167438Z Temporarily overriding HOME='D:\a\_temp\e7bfdae8-fa27-43bc-9b56-0728e44612aa' before making global git config changes
2026-11-16T03:56:03.2168336Z Adding repository directory to the temporary git global config as a safe directory
2026-11-16T03:56:03.2179043Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
2026-11-16T03:56:03.2472458Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T03:56:03.2763113Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T03:56:03.7691351Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T03:56:03.7980481Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T03:56:04.2683448Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T03:56:04.2973214Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T03:56:04.7856173Z Cleaning up orphan processes
2026-11-16T03:56:04.8156938Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@11d5960a326750d5838078e36cf38b85af677262, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/


```

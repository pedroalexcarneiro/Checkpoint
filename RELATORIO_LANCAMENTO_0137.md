# Lançamento 0.1.37 — publicado e arquivos verificados

## Resultado final da publicação

Pré-release publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37

- Tag/código: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52, conferido por ls-remote.
- Workflow 43793047592: build e publish success, nenhuma falha/skip/erro na suíte final Windows.
- Windows/Python 3.12.10: 695 passed in 638.21s (0:10:38).
- Linux/Python 3.12.14: 695 passed in 478.98s (0:07:58), após a correção de limpeza do teste.
- Fonte e executável realmente extraído: smokes de seis páginas, cadastro, auxiliar, SQLite e atualizador aprovados.
- Oito arquivos publicados baixados e conferidos por tamanho e digest GitHub SHA-256; CRC dos dois ZIPs válido.
- ZIP Windows: 84312887 bytes; SHA-256 54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a.

Primeiro candidato a33f48a foi substituído antes da publicação por correção restrita ao teste; o run interrompido não é apresentado como aprovado. A tag 0.1.36 continua em 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Não houve force, alteração de workflow/asset/protegido, PR ou movimento de tag anterior. Atualizações documentais posteriores não mudam a tag lançada.

Permanecem as limitações de capacidade da fonte console/original individual, uso real com UAC/moldura/captura/launchers/contas/emuladores/DPI/monitores no PC do dono, A4 e fechar só a ROM. Runner Windows/pacote aprovados não homologam esses cenários pessoais. Elevação para outra conta é recusada para preservar dados/cofre. Isso está nas notas públicas; a rodada inteira não é chamada de concluída com pendências importantes.

Registros de preparação, comandos integrais e execução interrompida abaixo são históricos.

Autorização posterior do dono: “dps de acabar tu lanca a versao ta”. Essa instrução substitui a restrição de publicação da fase inicial desta rodada. Não reutilizada autorização antiga da 0.1.36.

Plano: terminar verificações locais, enviar fix/0.1.37-ajustes sem force, conferir SHA remoto e disparar Windows release existente nessa branch. O workflow testa no Windows, builda, valida fonte e executável extraído, captura a interface e só então publica a pré-release v0.1.37. Nenhum workflow será modificado; nenhuma tag/release anterior será movida ou substituída. Notas públicas atualizadas para esta versão após a autorização, incluindo limitações.

Código local congelado para a suíte final: f543166037e545aad99c6aef21bf6ed95fe4bb10. Commit posterior de documentação/notas preserva esse código. Resultado e SHA efetivamente enviado serão registrados abaixo. Preparação não equivale a versão publicada.

Pendências explicitadas nas notas: fonte autenticada console/original individual não comprovados; moldura, UAC, captura elevada, emuladores/contas/DPI/monitores reais no PC do dono não homologados; A4 protegido e fechar apenas ROM mantêm seus limites. Runner Windows não certifica uso pessoal real. A rodada não é apresentada como inteiramente concluída com essas pendências.

Comandos registrados com stdout/stderr/código de saída, sem tokens. Testes locais e antes/depois completos em RELATORIO_0137_TESTES.md; detalhes por item em RELATORIO_0137.md.

## push-0137

UTC: 2026-11-16T02:07:53.585557+00:00

Comando: `["git", "push", "origin", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text
remote: 
remote: Create a pull request for 'fix/0.1.37-ajustes' on GitHub by visiting:        
remote:      https://github.com/pedroalexcarneiro/Checkpoint/pull/new/fix/0.1.37-ajustes        
remote: 
To https://github.com/pedroalexcarneiro/Checkpoint.git
 * [new branch]      fix/0.1.37-ajustes -> fix/0.1.37-ajustes

```

Código de saída: 0

## confirmar-remoto-0137

UTC: 2026-11-16T02:08:00.977998+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
a33f48afbb8502a2f128de453451f326e8c988c2	refs/heads/fix/0.1.37-ajustes

```

stderr integral:
```text

```

Código de saída: 0

## actions-antes-dispatch

UTC: 2026-11-16T02:08:17.276178+00:00

Comando: `["gh", "run", "list", "--branch", "fix/0.1.37-ajustes", "--limit", "5", "--json", "databaseId,headSha,status,conclusion,name,event,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
[]

```

stderr integral:
```text

```

Código de saída: 0

## dispatch-release-0137

UTC: 2026-11-16T02:08:26.114508+00:00

Comando: `["gh", "workflow", "run", "windows-release.yml", "--ref", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## localizar-run-0137

UTC: 2026-11-16T02:08:55.346135+00:00

Comando: `["gh", "run", "list", "--branch", "fix/0.1.37-ajustes", "--workflow", "windows-release.yml", "--limit", "3", "--json", "databaseId,headSha,status,conclusion,name,event,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
[{"conclusion":"","databaseId":43790327035,"event":"workflow_dispatch","headSha":"a33f48afbb8502a2f128de453451f326e8c988c2","name":"Windows release","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035"}]

```

stderr integral:
```text

```

Código de saída: 0

## Pré-envio e execução disparada

```text
HEAD local: a33f48afbb8502a2f128de453451f326e8c988c2
git status --porcelain: vazio
ls-remote stdout:

ls-remote stderr:

exit: 0
```

Branch enviada sem force em a33f48afbb8502a2f128de453451f326e8c988c2. ls-remote confirmou o mesmo SHA. Nenhuma execução automática foi criada pelo push; uma única execução manual Windows release foi iniciada após a autorização.

Execução: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035 — workflow_dispatch, SHA a33f48afbb8502a2f128de453451f326e8c988c2. Testes Windows em andamento; nenhuma publicação confirmada neste ponto.

## Primeira execução bloqueada — corrigido o próprio teste

A execução manual 43790327035 foi encerrada pelo implementador depois de reproduzir uma falha na limpeza do teste novo dos controles. Build/publish não foram executados e nenhuma tag/release foi criada. Não era uma execução inesperada do push; o cancelamento desta execução manual evitou aguardar o limite com um modal bloqueado.

Logs Windows: 648 testes completos (93%) e mais 24 pontos, ou seja, 672 completos, sem conclusão da suíte. A ordem de coleta coloca test_window_controls_use_regular_window_close_and_restore[sample0] em 672 e sample1 em 673. O teste substituía window.close por um spy e o mantinha durante a limpeza da fixture; a janela era destruída com o hotkey ainda registrado. A próxima janela podia abrir o modal de conflito e bloquear. Não se trata de 672 aprovações finais nem de falha comprovada do aplicativo em uso real.

Reprodução local com adaptador de atalho exclusivo confirmou dois erros na limpeza, um por jogo. Correção somente em tests/test_window_controls_0137.py: spy limitado a monkeypatch.context; depois o botão fecha realmente a janela e verifica liberação do atalho. Todas as asserções anteriores preservadas; verificações de fechamento/liberação acrescentadas. Depois: três testes aprovados em 0,35 s com o adaptador que antes detectava vazamento. Aplicativo, fontes protegidas, workflows e versão permanecem intactos. Nova execução será de um commit posterior, sem reescrever o candidato anterior.

## andamento-windows-0137

UTC: 2026-11-16T02:17:38.409119+00:00

Comando: `["gh", "run", "view", "43790327035", "--json", "createdAt,updatedAt,headSha,status,conclusion,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"conclusion":"","createdAt":"2026-11-16T02:08:25Z","headSha":"a33f48afbb8502a2f128de453451f326e8c988c2","status":"in_progress","updatedAt":"2026-11-16T02:08:29Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035"}

```

stderr integral:
```text

```

Código de saída: 0

## encerrar-run-bloqueado

UTC: 2026-11-16T02:25:13.989074+00:00

Comando: `["gh", "run", "cancel", "43790327035"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
✓ Request to cancel workflow 43790327035 submitted.

```

stderr integral:
```text

```

Código de saída: 0

## push-correcao-limpeza

UTC: 2026-11-16T02:28:31.551533+00:00

Comando: `["git", "push", "origin", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text
To https://github.com/pedroalexcarneiro/Checkpoint.git
   a33f48a..c526cb4  fix/0.1.37-ajustes -> fix/0.1.37-ajustes

```

Código de saída: 0

## confirmar-correcao-remota

UTC: 2026-11-16T02:34:54.849613+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
c526cb4bc5e8721dfdfdf20222c8c1c41562ce52	refs/heads/fix/0.1.37-ajustes

```

stderr integral:
```text

```

Código de saída: 0

## dispatch-release-correcao-0137

UTC: 2026-11-16T02:35:01.583943+00:00

Comando: `["gh", "workflow", "run", "windows-release.yml", "--ref", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## localizar-segunda-execucao

UTC: 2026-11-16T02:35:12.692869+00:00

Comando: `["gh", "run", "list", "--branch", "fix/0.1.37-ajustes", "--workflow", "windows-release.yml", "--limit", "3", "--json", "databaseId,headSha,status,conclusion,name,event,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
[{"conclusion":"","databaseId":43793047592,"event":"workflow_dispatch","headSha":"c526cb4bc5e8721dfdfdf20222c8c1c41562ce52","name":"Windows release","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592"},{"conclusion":"cancelled","databaseId":43790327035,"event":"workflow_dispatch","headSha":"a33f48afbb8502a2f128de453451f326e8c988c2","name":"Windows release","status":"completed","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035"}]

```

stderr integral:
```text

```

Código de saída: 0

## logs-primeira-execucao

UTC: 2026-11-16T02:35:41.550600+00:00

Comando: `["gh", "run", "view", "43790327035", "--job", "133047051145", "--log"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
build	Set up job	﻿2026-11-16T02:08:29.9332532Z Current runner version: '2.338.2'
build	Set up job	2026-11-16T02:08:29.9382013Z ##[group]Runner Image Provisioner
build	Set up job	2026-11-16T02:08:29.9382791Z Hosted Compute Agent
build	Set up job	2026-11-16T02:08:29.9383352Z Version: 20261103.629
build	Set up job	2026-11-16T02:08:29.9383918Z Commit: 15dbd9ccb5dbf34fae002b6ed1a2670f52df37bc
build	Set up job	2026-11-16T02:08:29.9384598Z Build Date: 2026-11-03T17:26:59Z
build	Set up job	2026-11-16T02:08:29.9385225Z Worker ID: {146f31aa-baf8-4a9a-9f2e-d952cb19ed02}
build	Set up job	2026-11-16T02:08:29.9385865Z Region: eastus
build	Set up job	2026-11-16T02:08:29.9386438Z Cloud: Azure
build	Set up job	2026-11-16T02:08:29.9386926Z ##[endgroup]
build	Set up job	2026-11-16T02:08:29.9388291Z ##[group]Operating System
build	Set up job	2026-11-16T02:08:29.9388987Z Microsoft Windows Server 2022
build	Set up job	2026-11-16T02:08:29.9389539Z 10.0.20348
build	Set up job	2026-11-16T02:08:29.9390020Z Datacenter
build	Set up job	2026-11-16T02:08:29.9390506Z ##[endgroup]
build	Set up job	2026-11-16T02:08:29.9390988Z ##[group]Runner Image
build	Set up job	2026-11-16T02:08:29.9391600Z Image: windows-2022
build	Set up job	2026-11-16T02:08:29.9392100Z Version: 20261112.366.7
build	Set up job	2026-11-16T02:08:29.9393113Z Included Software: https://github.com/actions/runner-images/blob/win22/20261112.366/images/windows/Windows2022-Readme.md
build	Set up job	2026-11-16T02:08:29.9394972Z Image Release: https://github.com/actions/runner-images/releases/tag/win22%2F20261112.366
build	Set up job	2026-11-16T02:08:29.9395849Z ##[endgroup]
build	Set up job	2026-11-16T02:08:29.9396899Z ##[group]GITHUB_TOKEN Permissions
build	Set up job	2026-11-16T02:08:29.9398848Z Contents: read
build	Set up job	2026-11-16T02:08:29.9399406Z Metadata: read
build	Set up job	2026-11-16T02:08:29.9399938Z ##[endgroup]
build	Set up job	2026-11-16T02:08:29.9402045Z Secret source: Actions
build	Set up job	2026-11-16T02:08:29.9402932Z Cache mode: write
build	Set up job	2026-11-16T02:08:29.9403812Z Prepare workflow directory
build	Set up job	2026-11-16T02:08:29.9782721Z Prepare all required actions
build	Set up job	2026-11-16T02:08:29.9829830Z Getting action download info
build	Set up job	2026-11-16T02:08:30.1787822Z Download action repository 'actions/checkout@11d5960a326750d5838078e36cf38b85af677262' (SHA:11d5960a326750d5838078e36cf38b85af677262)
build	Set up job	2026-11-16T02:08:30.2972423Z Download action repository 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
build	Set up job	2026-11-16T02:08:30.4396898Z Download action repository 'actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
build	Set up job	2026-11-16T02:08:30.7803654Z Complete job name: build
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T02:08:30.9507009Z ##[group]Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9508604Z with:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9509164Z   persist-credentials: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9509796Z   fetch-depth: 0
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9510391Z   repository: pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9515285Z   token: ***
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9515825Z   ssh-strict: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9516357Z   ssh-user: git
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9516879Z   clean: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9517369Z   sparse-checkout-cone-mode: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9517891Z   fetch-tags: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9518330Z   show-progress: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9518785Z   lfs: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9519223Z   submodules: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9519714Z   set-safe-directory: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9520227Z   allow-unsafe-pr-checkout: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9520956Z env:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9521383Z   QT_QPA_PLATFORM: offscreen
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:30.9521878Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.0954846Z Syncing repository: pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.0956848Z ##[group]Getting Git version info
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.0957569Z Working directory is 'D:\a\Checkpoint\Checkpoint'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.1949642Z [command]"C:\Program Files\Git\bin\git.exe" version
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5110942Z git version 2.56.1.windows.1
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5152951Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5171458Z Temporarily overriding HOME='D:\a\_temp\ae9c0b9f-a541-4fef-9efe-485f212c6e45' before making global git config changes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5173395Z Adding repository directory to the temporary git global config as a safe directory
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5182706Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5773027Z Deleting the contents of 'D:\a\Checkpoint\Checkpoint'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5778417Z ##[group]Initializing the repository
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.5787371Z [command]"C:\Program Files\Git\bin\git.exe" init D:\a\Checkpoint\Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.6651134Z Initialized empty Git repository in D:/a/Checkpoint/Checkpoint/.git/
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.6691421Z [command]"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7287371Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7288866Z ##[group]Disabling automatic garbage collection
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7296241Z [command]"C:\Program Files\Git\bin\git.exe" config --local gc.auto 0
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7584426Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7586187Z ##[group]Setting up auth
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7595975Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:31.7893379Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:33.2336855Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:33.2636043Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:33.7096277Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:33.7388485Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:34.2116432Z [command]"C:\Program Files\Git\bin\git.exe" config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ***"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:34.2432944Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:34.2433703Z ##[group]Fetching the repository
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:34.2453056Z [command]"C:\Program Files\Git\bin\git.exe" -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4226137Z From https://github.com/pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4227496Z  * [new branch]      codex/design-fidelity-pt-br -> origin/codex/design-fidelity-pt-br
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4228917Z  * [new branch]      codex/steam-library-import -> origin/codex/steam-library-import
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4229766Z  * [new branch]      fix/0.1.29         -> origin/fix/0.1.29
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4230342Z  * [new branch]      fix/0.1.30         -> origin/fix/0.1.30
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4230997Z  * [new branch]      fix/0.1.32-visual  -> origin/fix/0.1.32-visual
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4231629Z  * [new branch]      fix/0.1.33-drive   -> origin/fix/0.1.33-drive
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4232346Z  * [new branch]      fix/0.1.34-bugs    -> origin/fix/0.1.34-bugs
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4232988Z  * [new branch]      fix/0.1.35-ajustes -> origin/fix/0.1.35-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4233751Z  * [new branch]      fix/0.1.36-ajustes -> origin/fix/0.1.36-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4234457Z  * [new branch]      fix/0.1.37-ajustes -> origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4235469Z  * [new branch]      fix/rename-redesign-0.1.28 -> origin/fix/rename-redesign-0.1.28
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4236018Z  * [new branch]      main               -> origin/main
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4236351Z  * [new tag]         v0.1.10            -> v0.1.10
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4236650Z  * [new tag]         v0.1.11            -> v0.1.11
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4236938Z  * [new tag]         v0.1.12            -> v0.1.12
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4237266Z  * [new tag]         v0.1.13            -> v0.1.13
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4237546Z  * [new tag]         v0.1.14            -> v0.1.14
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4238790Z  * [new tag]         v0.1.15            -> v0.1.15
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4239108Z  * [new tag]         v0.1.16            -> v0.1.16
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4239385Z  * [new tag]         v0.1.17            -> v0.1.17
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4239711Z  * [new tag]         v0.1.18            -> v0.1.18
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4240035Z  * [new tag]         v0.1.19            -> v0.1.19
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4240303Z  * [new tag]         v0.1.2             -> v0.1.2
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4240573Z  * [new tag]         v0.1.20            -> v0.1.20
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4240841Z  * [new tag]         v0.1.21            -> v0.1.21
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4241106Z  * [new tag]         v0.1.22            -> v0.1.22
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4241367Z  * [new tag]         v0.1.23            -> v0.1.23
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4241627Z  * [new tag]         v0.1.24            -> v0.1.24
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4241884Z  * [new tag]         v0.1.25            -> v0.1.25
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4242146Z  * [new tag]         v0.1.26            -> v0.1.26
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4242411Z  * [new tag]         v0.1.27            -> v0.1.27
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4242670Z  * [new tag]         v0.1.28            -> v0.1.28
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4242956Z  * [new tag]         v0.1.29            -> v0.1.29
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4243323Z  * [new tag]         v0.1.3             -> v0.1.3
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4243593Z  * [new tag]         v0.1.30            -> v0.1.30
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4243857Z  * [new tag]         v0.1.32            -> v0.1.32
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4244421Z  * [new tag]         v0.1.33            -> v0.1.33
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4245204Z  * [new tag]         v0.1.34            -> v0.1.34
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4245716Z  * [new tag]         v0.1.35            -> v0.1.35
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4246181Z  * [new tag]         v0.1.36            -> v0.1.36
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4246622Z  * [new tag]         v0.1.4             -> v0.1.4
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4247098Z  * [new tag]         v0.1.5             -> v0.1.5
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4247599Z  * [new tag]         v0.1.6             -> v0.1.6
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4327622Z  * [new tag]         v0.1.7             -> v0.1.7
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4328267Z  * [new tag]         v0.1.8             -> v0.1.8
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4328738Z  * [new tag]         v0.1.9             -> v0.1.9
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4331510Z [command]"C:\Program Files\Git\bin\git.exe" branch --list --remote origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4649211Z   origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4683264Z [command]"C:\Program Files\Git\bin\git.exe" rev-parse refs/remotes/origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4942514Z a33f48afbb8502a2f128de453451f326e8c988c2
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4966445Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4966838Z ##[group]Determining the checkout info
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4968515Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.4977108Z [command]"C:\Program Files\Git\bin\git.exe" sparse-checkout disable
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.5385776Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all extensions.worktreeConfig
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.5669978Z ##[group]Checking out the ref
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.5679400Z [command]"C:\Program Files\Git\bin\git.exe" checkout --progress --force -B fix/0.1.37-ajustes refs/remotes/origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.7913045Z Switched to a new branch 'fix/0.1.37-ajustes'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.7934347Z branch 'fix/0.1.37-ajustes' set up to track 'origin/fix/0.1.37-ajustes'.
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.7980607Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.8401997Z [command]"C:\Program Files\Git\bin\git.exe" log -1 --format=%H
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.8669230Z a33f48afbb8502a2f128de453451f326e8c988c2
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.8700725Z ##[group]Removing auth
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.8708735Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:35.8990833Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.3842803Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.4114159Z http.https://github.com/.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.4155538Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.4481788Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.9493208Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:36.9783624Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:08:37.4469355Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	﻿2026-11-16T02:08:37.4832946Z ##[group]Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4833424Z with:
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4833609Z   python-version: 3.12
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4833817Z   architecture: x64
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4833995Z   cache: pip
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4834216Z   cache-dependency-path: requirements-tested.txt
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4834503Z   check-latest: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4836742Z   token: ***
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4836944Z   update-environment: true
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4837163Z   allow-prereleases: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4837366Z   freethreaded: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4837545Z env:
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4837705Z   QT_QPA_PLATFORM: offscreen
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.4837907Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.6369137Z ##[group]Installed versions
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.6577892Z (node:5760) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.6579174Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.6579970Z Successfully set up CPython (3.12.10)
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:37.6580707Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:08:40.3055876Z pip cache is not found
build	Check release version	﻿2026-11-16T02:08:40.3309181Z ##[group]Run $version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'
build	Check release version	2026-11-16T02:08:40.3310860Z [36;1m$version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'[0m
build	Check release version	2026-11-16T02:08:40.3311823Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao ler a versão.' }[0m
build	Check release version	2026-11-16T02:08:40.3312290Z [36;1mif ($version -notmatch '^\d+\.\d+\.\d+$') { throw 'Versão inválida.' }[0m
build	Check release version	2026-11-16T02:08:40.3312683Z [36;1m"version=$version" >> $env:GITHUB_OUTPUT[0m
build	Check release version	2026-11-16T02:08:40.3429391Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Check release version	2026-11-16T02:08:40.3429757Z env:
build	Check release version	2026-11-16T02:08:40.3429940Z   QT_QPA_PLATFORM: offscreen
build	Check release version	2026-11-16T02:08:40.3430267Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:08:40.3430803Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Check release version	2026-11-16T02:08:40.3431275Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:08:40.3431688Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:08:40.3432101Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:08:40.3432423Z ##[endgroup]
build	Install tested Windows dependencies	﻿2026-11-16T02:08:40.8581564Z ##[group]Run python -m pip install -r requirements-tested.txt
build	Install tested Windows dependencies	2026-11-16T02:08:40.8582108Z [36;1mpython -m pip install -r requirements-tested.txt[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8582572Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependências.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8583242Z [36;1mpython -m pip install --no-deps --no-build-isolation -e .[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8583684Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar o projeto.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8584048Z [36;1mpython -m pip check[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8584372Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências inconsistentes.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:08:40.8624565Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Install tested Windows dependencies	2026-11-16T02:08:40.8624909Z env:
build	Install tested Windows dependencies	2026-11-16T02:08:40.8625093Z   QT_QPA_PLATFORM: offscreen
build	Install tested Windows dependencies	2026-11-16T02:08:40.8625417Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:08:40.8625872Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Install tested Windows dependencies	2026-11-16T02:08:40.8626357Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:08:40.8626748Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:08:40.8627142Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:08:40.8627461Z ##[endgroup]
build	Install tested Windows dependencies	2026-11-16T02:08:43.8418228Z Collecting altgraph==0.17.5 (from -r requirements-tested.txt (line 1))
build	Install tested Windows dependencies	2026-11-16T02:08:44.0909901Z   Downloading altgraph-0.17.5-py2.py3-none-any.whl.metadata (7.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:44.1855760Z Collecting certifi==2026.10.23 (from -r requirements-tested.txt (line 2))
build	Install tested Windows dependencies	2026-11-16T02:08:44.2163997Z   Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:44.4358811Z Collecting cffi==2.1.1 (from -r requirements-tested.txt (line 3))
build	Install tested Windows dependencies	2026-11-16T02:08:44.4680083Z   Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:44.6518615Z Collecting charset-normalizer==3.5.2 (from -r requirements-tested.txt (line 4))
build	Install tested Windows dependencies	2026-11-16T02:08:44.6873622Z   Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:44.7630446Z Requirement already satisfied: colorama==0.4.6 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 5)) (0.4.6)
build	Install tested Windows dependencies	2026-11-16T02:08:44.9819766Z Collecting cryptography==50.0.2 (from -r requirements-tested.txt (line 6))
build	Install tested Windows dependencies	2026-11-16T02:08:45.0162030Z   Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl.metadata (4.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.0919107Z Collecting google-api-core==2.44.0 (from -r requirements-tested.txt (line 7))
build	Install tested Windows dependencies	2026-11-16T02:08:45.1277254Z   Downloading google_api_core-2.44.0-py3-none-any.whl.metadata (3.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.2179251Z Collecting google-api-python-client==2.202.0 (from -r requirements-tested.txt (line 8))
build	Install tested Windows dependencies	2026-11-16T02:08:45.2485253Z   Downloading google_api_python_client-2.202.0-py3-none-any.whl.metadata (6.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.3072627Z Collecting google-auth-httplib2==0.4.4 (from -r requirements-tested.txt (line 9))
build	Install tested Windows dependencies	2026-11-16T02:08:45.3392537Z   Downloading google_auth_httplib2-0.4.4-py3-none-any.whl.metadata (3.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.4039039Z Collecting google-auth-oauthlib==1.5.0 (from -r requirements-tested.txt (line 10))
build	Install tested Windows dependencies	2026-11-16T02:08:45.4341390Z   Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.5180052Z Collecting google-auth==2.62.2 (from -r requirements-tested.txt (line 11))
build	Install tested Windows dependencies	2026-11-16T02:08:45.5482729Z   Downloading google_auth-2.62.2-py3-none-any.whl.metadata (6.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.6184072Z Collecting googleapis-common-protos==1.76.0 (from -r requirements-tested.txt (line 12))
build	Install tested Windows dependencies	2026-11-16T02:08:45.6493809Z   Downloading googleapis_common_protos-1.76.0-py3-none-any.whl.metadata (8.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.7104797Z Collecting httplib2==0.32.1 (from -r requirements-tested.txt (line 13))
build	Install tested Windows dependencies	2026-11-16T02:08:45.7417385Z   Downloading httplib2-0.32.1-py3-none-any.whl.metadata (2.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.8056980Z Collecting idna==3.20 (from -r requirements-tested.txt (line 14))
build	Install tested Windows dependencies	2026-11-16T02:08:45.8362962Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.8947557Z Collecting iniconfig==2.3.1 (from -r requirements-tested.txt (line 15))
build	Install tested Windows dependencies	2026-11-16T02:08:45.9261532Z   Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:45.9848269Z Collecting jaraco-classes==3.4.0 (from -r requirements-tested.txt (line 16))
build	Install tested Windows dependencies	2026-11-16T02:08:46.0237688Z   Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.0905545Z Collecting jaraco-context==6.1.2 (from -r requirements-tested.txt (line 17))
build	Install tested Windows dependencies	2026-11-16T02:08:46.1252304Z   Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.1956915Z Collecting jaraco-functools==4.6.0 (from -r requirements-tested.txt (line 18))
build	Install tested Windows dependencies	2026-11-16T02:08:46.2412003Z   Downloading jaraco_functools-4.6.0-py3-none-any.whl.metadata (2.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.3172801Z Collecting keyring==25.7.0 (from -r requirements-tested.txt (line 19))
build	Install tested Windows dependencies	2026-11-16T02:08:46.3527911Z   Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.4268608Z Collecting more-itertools==11.2.1 (from -r requirements-tested.txt (line 20))
build	Install tested Windows dependencies	2026-11-16T02:08:46.4572564Z   Downloading more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.5286644Z Collecting oauthlib==4.0.1 (from -r requirements-tested.txt (line 21))
build	Install tested Windows dependencies	2026-11-16T02:08:46.5600272Z   Downloading oauthlib-4.0.1-py3-none-any.whl.metadata (8.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.6317634Z Collecting opentelemetry-api==1.45.2 (from -r requirements-tested.txt (line 22))
build	Install tested Windows dependencies	2026-11-16T02:08:46.6686980Z   Downloading opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.6883697Z Requirement already satisfied: packaging==26.3 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 23)) (26.3)
build	Install tested Windows dependencies	2026-11-16T02:08:46.7281342Z Collecting pefile==2024.8.26 (from -r requirements-tested.txt (line 24))
build	Install tested Windows dependencies	2026-11-16T02:08:46.7584405Z   Downloading pefile-2024.8.26-py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.8203310Z Collecting pluggy==1.7.0 (from -r requirements-tested.txt (line 25))
build	Install tested Windows dependencies	2026-11-16T02:08:46.8545318Z   Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:46.9186106Z Collecting proto-plus==1.29.0 (from -r requirements-tested.txt (line 26))
build	Install tested Windows dependencies	2026-11-16T02:08:46.9493104Z   Downloading proto_plus-1.29.0-py3-none-any.whl.metadata (2.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.1702995Z Collecting protobuf==7.36.2 (from -r requirements-tested.txt (line 27))
build	Install tested Windows dependencies	2026-11-16T02:08:47.2043007Z   Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
build	Install tested Windows dependencies	2026-11-16T02:08:47.2795572Z Collecting pyasn1-modules==0.4.2 (from -r requirements-tested.txt (line 28))
build	Install tested Windows dependencies	2026-11-16T02:08:47.3185549Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.4003884Z Collecting pyasn1==0.6.5 (from -r requirements-tested.txt (line 29))
build	Install tested Windows dependencies	2026-11-16T02:08:47.4322585Z   Downloading pyasn1-0.6.5-py3-none-any.whl.metadata (8.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.4953954Z Collecting pycparser==3.12 (from -r requirements-tested.txt (line 30))
build	Install tested Windows dependencies	2026-11-16T02:08:47.5293036Z   Downloading pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.5952543Z Collecting pygments==2.21.0 (from -r requirements-tested.txt (line 31))
build	Install tested Windows dependencies	2026-11-16T02:08:47.6257722Z   Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.6969037Z Collecting pyinstaller-hooks-contrib==2026.10 (from -r requirements-tested.txt (line 32))
build	Install tested Windows dependencies	2026-11-16T02:08:47.7272552Z   Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl.metadata (16 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.8358098Z Collecting pyinstaller==6.22.3 (from -r requirements-tested.txt (line 33))
build	Install tested Windows dependencies	2026-11-16T02:08:47.8698210Z   Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl.metadata (8.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:47.9402147Z Collecting pyparsing==3.3.3 (from -r requirements-tested.txt (line 34))
build	Install tested Windows dependencies	2026-11-16T02:08:47.9704871Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.0428057Z Collecting pyside6-addons==6.8.3 (from -r requirements-tested.txt (line 35))
build	Install tested Windows dependencies	2026-11-16T02:08:48.0937501Z   Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.1652682Z Collecting pyside6-essentials==6.8.3 (from -r requirements-tested.txt (line 36))
build	Install tested Windows dependencies	2026-11-16T02:08:48.2008016Z   Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.1 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.2804733Z Collecting pyside6==6.8.3 (from -r requirements-tested.txt (line 37))
build	Install tested Windows dependencies	2026-11-16T02:08:48.3225902Z   Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl.metadata (5.7 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.4024879Z Collecting pytest==9.2.0 (from -r requirements-tested.txt (line 38))
build	Install tested Windows dependencies	2026-11-16T02:08:48.4339069Z   Downloading pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.5033335Z Collecting pywin32-ctypes==0.2.3 (from -r requirements-tested.txt (line 39))
build	Install tested Windows dependencies	2026-11-16T02:08:48.5368707Z   Downloading pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.6025989Z Collecting requests-oauthlib==2.0.0 (from -r requirements-tested.txt (line 40))
build	Install tested Windows dependencies	2026-11-16T02:08:48.6350544Z   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.7316015Z Collecting requests==2.34.2 (from -r requirements-tested.txt (line 41))
build	Install tested Windows dependencies	2026-11-16T02:08:48.7793852Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:48.9232315Z Collecting setuptools==84.2.1 (from -r requirements-tested.txt (line 42))
build	Install tested Windows dependencies	2026-11-16T02:08:48.9627979Z   Downloading setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.0556096Z Collecting shiboken6==6.8.3 (from -r requirements-tested.txt (line 43))
build	Install tested Windows dependencies	2026-11-16T02:08:49.0906957Z   Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl.metadata (2.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.1677988Z Collecting typing-extensions==4.16.0 (from -r requirements-tested.txt (line 44))
build	Install tested Windows dependencies	2026-11-16T02:08:49.2017733Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.2651709Z Collecting tzdata==2026.6 (from -r requirements-tested.txt (line 45))
build	Install tested Windows dependencies	2026-11-16T02:08:49.2984785Z   Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.3614255Z Collecting uritemplate==4.2.0 (from -r requirements-tested.txt (line 46))
build	Install tested Windows dependencies	2026-11-16T02:08:49.3933965Z   Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.4632744Z Collecting urllib3==2.8.0 (from -r requirements-tested.txt (line 47))
build	Install tested Windows dependencies	2026-11-16T02:08:49.5078468Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.6352615Z Downloading altgraph-0.17.5-py2.py3-none-any.whl (21 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.6916218Z Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.7782001Z Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl (185 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.8570727Z Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:49.9508093Z Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl (3.8 MB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.3924742Z    ---------------------------------------- 3.8/3.8 MB 8.4 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:08:50.4230319Z Downloading google_api_core-2.44.0-py3-none-any.whl (225 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.4827822Z Downloading google_auth-2.62.2-py3-none-any.whl (270 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.5419523Z Downloading googleapis_common_protos-1.76.0-py3-none-any.whl (307 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.6065023Z Downloading opentelemetry_api-1.45.2-py3-none-any.whl (60 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.6586471Z Downloading proto_plus-1.29.0-py3-none-any.whl (50 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.7106932Z Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.7822545Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.8335302Z Downloading idna-3.20-py3-none-any.whl (69 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.8823351Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:50.9406922Z Downloading google_api_python_client-2.202.0-py3-none-any.whl (17.1 MB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.3317446Z    ---------------------------------------- 17.1/17.1 MB 7.1 MB/s  0:00:02
build	Install tested Windows dependencies	2026-11-16T02:08:53.3628648Z Downloading google_auth_httplib2-0.4.4-py3-none-any.whl (9.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.4097129Z Downloading httplib2-0.32.1-py3-none-any.whl (92 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.4603619Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.5141962Z Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.5669598Z Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl (20 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.6212396Z Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.6690259Z Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.7183096Z Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.7676280Z Downloading jaraco_functools-4.6.0-py3-none-any.whl (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.8139035Z Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.8633929Z Downloading more_itertools-11.2.1-py3-none-any.whl (74 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.9186706Z Downloading oauthlib-4.0.1-py3-none-any.whl (161 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:53.9858271Z Downloading pefile-2024.8.26-py3-none-any.whl (74 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.0367696Z Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.0860357Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.1369531Z Downloading pyasn1-0.6.5-py3-none-any.whl (84 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.1883953Z Downloading pycparser-3.12-py3-none-any.whl (62 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.2355887Z Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.2967011Z    ---------------------------------------- 1.3/1.3 MB 15.9 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:08:54.3342156Z Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl (463 kB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.4138521Z Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl (1.5 MB)
build	Install tested Windows dependencies	2026-11-16T02:08:54.4722960Z    ---------------------------------------- 1.5/1.5 MB 18.9 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:08:54.5075112Z Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl (127.9 MB)
build	Install tested Windows dependencies	2026-11-16T02:08:59.3713078Z    ---------------------------------------- 127.9/127.9 MB 26.3 MB/s  0:00:04
build	Install tested Windows dependencies	2026-11-16T02:08:59.4040177Z Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl (72.2 MB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.0399934Z    ---------------------------------------- 72.2/72.2 MB 27.2 MB/s  0:00:02
build	Install tested Windows dependencies	2026-11-16T02:09:02.0849983Z Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl (561 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.1097517Z    ---------------------------------------- 561.1/561.1 kB 18.7 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:09:02.1409084Z Downloading pytest-9.2.0-py3-none-any.whl (411 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.2094392Z Downloading pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.2612202Z Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.3092832Z Downloading setuptools-84.2.1-py3-none-any.whl (876 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.3388129Z    ---------------------------------------- 876.3/876.3 kB 19.8 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:09:02.3720883Z Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl (1.2 MB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.4217144Z    ---------------------------------------- 1.2/1.2 MB 28.7 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:09:02.4527455Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:02.5034516Z Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
build	Install tested Windows dependencies	2026-11-16T02:09:03.2349761Z Installing collected packages: altgraph, urllib3, uritemplate, tzdata, typing-extensions, shiboken6, setuptools, pywin32-ctypes, pyparsing, pyinstaller-hooks-contrib, pygments, pycparser, pyasn1, protobuf, pluggy, pefile, oauthlib, more-itertools, jaraco-context, iniconfig, idna, charset-normalizer, certifi, requests, pytest, pyside6-essentials, pyinstaller, pyasn1-modules, proto-plus, opentelemetry-api, jaraco-functools, jaraco-classes, httplib2, googleapis-common-protos, cffi, requests-oauthlib, pyside6-addons, keyring, cryptography, pyside6, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-core, google-api-python-client
build	Install tested Windows dependencies	2026-11-16T02:09:30.5532916Z 
build	Install tested Windows dependencies	2026-11-16T02:09:30.5583424Z Successfully installed altgraph-0.17.5 certifi-2026.10.23 cffi-2.1.1 charset-normalizer-3.5.2 cryptography-50.0.2 google-api-core-2.44.0 google-api-python-client-2.202.0 google-auth-2.62.2 google-auth-httplib2-0.4.4 google-auth-oauthlib-1.5.0 googleapis-common-protos-1.76.0 httplib2-0.32.1 idna-3.20 iniconfig-2.3.1 jaraco-classes-3.4.0 jaraco-context-6.1.2 jaraco-functools-4.6.0 keyring-25.7.0 more-itertools-11.2.1 oauthlib-4.0.1 opentelemetry-api-1.45.2 pefile-2024.8.26 pluggy-1.7.0 proto-plus-1.29.0 protobuf-7.36.2 pyasn1-0.6.5 pyasn1-modules-0.4.2 pycparser-3.12 pygments-2.21.0 pyinstaller-6.22.3 pyinstaller-hooks-contrib-2026.10 pyparsing-3.3.3 pyside6-6.8.3 pyside6-addons-6.8.3 pyside6-essentials-6.8.3 pytest-9.2.0 pywin32-ctypes-0.2.3 requests-2.34.2 requests-oauthlib-2.0.0 setuptools-84.2.1 shiboken6-6.8.3 typing-extensions-4.16.0 tzdata-2026.6 uritemplate-4.2.0 urllib3-2.8.0
build	Install tested Windows dependencies	2026-11-16T02:09:31.8121230Z Obtaining file:///D:/a/Checkpoint/Checkpoint
build	Install tested Windows dependencies	2026-11-16T02:09:31.8141281Z   Checking if build backend supports build_editable: started
build	Install tested Windows dependencies	2026-11-16T02:09:32.1664347Z   Checking if build backend supports build_editable: finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:09:32.1688894Z   Preparing editable metadata (pyproject.toml): started
build	Install tested Windows dependencies	2026-11-16T02:09:32.6903109Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:09:32.6969952Z Building wheels for collected packages: checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:09:32.6993747Z   Building editable for checkpoint-desktop (pyproject.toml): started
build	Install tested Windows dependencies	2026-11-16T02:09:33.3747619Z   Building editable for checkpoint-desktop (pyproject.toml): finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:09:33.3764648Z   C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\setuptools\command\editable_wheel.py:354: BuildBackendWarning: Editable installation.
build	Install tested Windows dependencies	2026-11-16T02:09:33.3765405Z   !!
build	Install tested Windows dependencies	2026-11-16T02:09:33.3765579Z   
build	Install tested Windows dependencies	2026-11-16T02:09:33.3765804Z           ********************************************************************************
build	Install tested Windows dependencies	2026-11-16T02:09:33.3766274Z           Please be careful with folders in your working directory with the same
build	Install tested Windows dependencies	2026-11-16T02:09:33.3766767Z           name as your package as they may take precedence during imports.
build	Install tested Windows dependencies	2026-11-16T02:09:33.3767176Z           ********************************************************************************
build	Install tested Windows dependencies	2026-11-16T02:09:33.3767489Z   
build	Install tested Windows dependencies	2026-11-16T02:09:33.3767644Z   !!
build	Install tested Windows dependencies	2026-11-16T02:09:33.3767880Z     with strategy, WheelFile(wheel_path, "w") as wheel_obj:
build	Install tested Windows dependencies	2026-11-16T02:09:33.3798336Z   Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.37-0.editable-py3-none-any.whl size=3269 sha256=be20dd549d0b556fe619fab5b682ea4c5e157c409c918e3a00603e7d40261b15
build	Install tested Windows dependencies	2026-11-16T02:09:33.3800331Z   Stored in directory: C:\Users\runneradmin\AppData\Local\Temp\pip-ephem-wheel-cache-d3aow8qw\wheels\a2\38\6e\88ad7ec70fd74394064971fa20d15ccdcdb6f76505932df31d
build	Install tested Windows dependencies	2026-11-16T02:09:33.3827994Z Successfully built checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:09:33.4063457Z Installing collected packages: checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:09:33.4440918Z Successfully installed checkpoint-desktop-0.1.37
build	Install tested Windows dependencies	2026-11-16T02:09:33.8553038Z No broken requirements found.
build	Test on Windows	﻿2026-11-16T02:09:33.9759462Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'
build	Test on Windows	2026-11-16T02:09:33.9760170Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'[0m
build	Test on Windows	2026-11-16T02:09:33.9760828Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
build	Test on Windows	2026-11-16T02:09:33.9761427Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
build	Test on Windows	2026-11-16T02:09:33.9800892Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Test on Windows	2026-11-16T02:09:33.9801256Z env:
build	Test on Windows	2026-11-16T02:09:33.9801445Z   QT_QPA_PLATFORM: offscreen
build	Test on Windows	2026-11-16T02:09:33.9801767Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:09:33.9802247Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Test on Windows	2026-11-16T02:09:33.9803473Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:09:33.9803888Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:09:33.9804329Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:09:33.9804642Z ##[endgroup]
build	Test on Windows	2026-11-16T02:09:47.9895604Z ........................................................................ [ 10%]
build	Test on Windows	2026-11-16T02:09:59.1900302Z ........................................................................ [ 20%]
build	Test on Windows	2026-11-16T02:10:13.9548179Z ........................................................................ [ 31%]
build	Test on Windows	2026-11-16T02:10:18.8619084Z ........................................................................ [ 41%]
build	Test on Windows	2026-11-16T02:10:46.3208859Z ........................................................................ [ 51%]
build	Test on Windows	2026-11-16T02:12:26.6677137Z ........................................................................ [ 62%]
build	Test on Windows	2026-11-16T02:13:06.8541753Z ........................................................................ [ 72%]
build	Test on Windows	2026-11-16T02:15:03.4111136Z ........................................................................ [ 82%]
build	Test on Windows	2026-11-16T02:19:48.0105669Z ........................................................................ [ 93%]
build	Test on Windows	2026-11-16T02:25:21.7137110Z ........................
build	Test on Windows	2026-11-16T02:25:21.7320787Z ##[error]The operation was canceled.
build	Preserve Windows test report	﻿2026-11-16T02:25:21.8138964Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
build	Preserve Windows test report	2026-11-16T02:25:21.8139660Z with:
build	Preserve Windows test report	2026-11-16T02:25:21.8139939Z   name: checkpoint-windows-test-report
build	Preserve Windows test report	2026-11-16T02:25:21.8140285Z   path: .ci-results/pytest.xml
build	Preserve Windows test report	2026-11-16T02:25:21.8140588Z   if-no-files-found: ignore
build	Preserve Windows test report	2026-11-16T02:25:21.8140873Z   retention-days: 14
build	Preserve Windows test report	2026-11-16T02:25:21.8141129Z   compression-level: 6
build	Preserve Windows test report	2026-11-16T02:25:21.8141388Z   overwrite: false
build	Preserve Windows test report	2026-11-16T02:25:21.8141642Z   include-hidden-files: false
build	Preserve Windows test report	2026-11-16T02:25:21.8142010Z env:
build	Preserve Windows test report	2026-11-16T02:25:21.8142240Z   QT_QPA_PLATFORM: offscreen
build	Preserve Windows test report	2026-11-16T02:25:21.8142598Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:25:21.8143110Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Preserve Windows test report	2026-11-16T02:25:21.8143619Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:25:21.8144082Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:25:21.8144636Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:25:21.8145009Z ##[endgroup]
build	Preserve Windows test report	2026-11-16T02:25:22.0634195Z (node:5432) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Preserve Windows test report	2026-11-16T02:25:22.0635551Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Preserve Windows test report	2026-11-16T02:25:22.0681343Z No files were found with the provided path: .ci-results/pytest.xml. No artifacts will be uploaded.
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T02:25:22.1727419Z Post job cleanup.
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.4692250Z [command]"C:\Program Files\Git\bin\git.exe" version
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.4999973Z git version 2.56.1.windows.1
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.5062138Z Temporarily overriding HOME='D:\a\_temp\69c6b717-7904-44e9-ab74-3d8daeda3cc9' before making global git config changes
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.5063525Z Adding repository directory to the temporary git global config as a safe directory
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.5073807Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.5388714Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:22.5698421Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:23.0895931Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:23.1287542Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:23.6388465Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:25:23.6686534Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Complete job	﻿2026-11-16T02:25:24.1638161Z Evaluate and set job outputs
build	Complete job	2026-11-16T02:25:24.1645180Z Set output 'version'
build	Complete job	2026-11-16T02:25:24.1647055Z Cleaning up orphan processes
build	Complete job	2026-11-16T02:25:24.1724952Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@11d5960a326750d5838078e36cf38b85af677262, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

```

stderr integral:
```text

```

Código de saída: 0

## Segunda execução — teste corrigido

Novo SHA enviado sem force: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52. ls-remote confirmou; nenhuma tag da 0.1.37 existia ao enviar. Código do aplicativo idêntico ao candidato anterior; alteração apenas no teste/relatórios. Execução: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592 — workflow_dispatch, SHA c526cb4.

Suíte Linux repetida no mesmo commit: 695 passed in 478.98s (0:07:58), exit 0; saída integral em RELATORIO_0137_TESTES.md. Código/testes permaneceram congelados durante a execução. Windows ainda em andamento neste registro.

## andamento-segunda-execucao

UTC: 2026-11-16T02:45:37.992147+00:00

Comando: `["gh", "run", "view", "43793047592", "--json", "status,conclusion,createdAt,updatedAt,jobs,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"conclusion":"","createdAt":"2026-11-16T02:35:01Z","jobs":[{"completedAt":"0001-01-01T00:00:00Z","conclusion":"","databaseId":133055600675,"name":"build","startedAt":"2026-11-16T02:35:04Z","status":"in_progress","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"","name":"Test on Windows","number":6,"status":"in_progress"},{"conclusion":"","name":"Build desktop and updater","number":7,"status":"pending"},{"conclusion":"","name":"Package and validate extracted executable","number":8,"status":"pending"},{"conclusion":"","name":"Render Windows interface review","number":9,"status":"pending"},{"conclusion":"","name":"Upload verified release files","number":10,"status":"pending"},{"conclusion":"","name":"Preserve Windows test report","number":11,"status":"pending"},{"conclusion":"","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"pending"},{"conclusion":"","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"pending"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592/job/133055600675"}],"status":"in_progress","updatedAt":"2026-11-16T02:35:05Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592"}

```

stderr integral:
```text

```

Código de saída: 0

## resultado-run-windows

UTC: 2026-11-16T02:49:04.810153+00:00

Comando: `["gh", "run", "view", "43793047592", "--json", "status,conclusion,headSha,url,jobs"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"conclusion":"success","headSha":"c526cb4bc5e8721dfdfdf20222c8c1c41562ce52","jobs":[{"completedAt":"2026-11-16T02:48:33Z","conclusion":"success","databaseId":133055600675,"name":"build","startedAt":"2026-11-16T02:35:04Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"success","name":"Test on Windows","number":6,"status":"completed"},{"conclusion":"success","name":"Build desktop and updater","number":7,"status":"completed"},{"conclusion":"success","name":"Package and validate extracted executable","number":8,"status":"completed"},{"conclusion":"success","name":"Render Windows interface review","number":9,"status":"completed"},{"conclusion":"success","name":"Upload verified release files","number":10,"status":"completed"},{"conclusion":"success","name":"Preserve Windows test report","number":11,"status":"completed"},{"conclusion":"success","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"completed"},{"conclusion":"success","name":"Complete job","number":23,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592/job/133055600675"},{"completedAt":"2026-11-16T02:48:55Z","conclusion":"success","databaseId":133059716070,"name":"publish","startedAt":"2026-11-16T02:48:35Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093","number":3,"status":"completed"},{"conclusion":"success","name":"Publish development release","number":4,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":8,"status":"completed"},{"conclusion":"success","name":"Complete job","number":9,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592/job/133059716070"}],"status":"completed","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592"}

```

stderr integral:
```text

```

Código de saída: 0

## release-publicada-metadados

UTC: 2026-11-16T02:49:13.037625+00:00

Comando: `["gh", "release", "view", "v0.1.37", "--json", "tagName,name,isPrerelease,isDraft,publishedAt,targetCommitish,url,assets"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"assets":[{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202069","contentType":"image/png","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POV","label":"","name":"Checkpoint-0.1.37-detail-overview.png","size":96121,"state":"uploaded","updatedAt":"2026-11-16T02:48:47Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-detail-overview.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202073","contentType":"image/png","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POZ","label":"","name":"Checkpoint-0.1.37-home.png","size":84584,"state":"uploaded","updatedAt":"2026-11-16T02:48:47Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-home.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202075","contentType":"image/png","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POb","label":"","name":"Checkpoint-0.1.37-library.png","size":137853,"state":"uploaded","updatedAt":"2026-11-16T02:48:47Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-library.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202074","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POa","label":"","name":"Checkpoint-0.1.37-ui-review.txt","size":560,"state":"uploaded","updatedAt":"2026-11-16T02:48:47Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-ui-review.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202071","contentType":"application/zip","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POX","label":"","name":"Checkpoint-0.1.37-ui-review.zip","size":3795052,"state":"uploaded","updatedAt":"2026-11-16T02:48:47Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-ui-review.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202086","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POm","label":"","name":"Checkpoint-0.1.37-validation.txt","size":684,"state":"uploaded","updatedAt":"2026-11-16T02:48:48Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-validation.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202088","contentType":"application/zip","createdAt":"2026-11-16T02:48:47Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5POo","label":"","name":"Checkpoint-0.1.37-windows-x64.zip","size":84312887,"state":"uploaded","updatedAt":"2026-11-16T02:48:51Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-windows-x64.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/753202100","contentType":"application/octet-stream","createdAt":"2026-11-16T02:48:48Z","downloadCount":0,"id":"RA_kwDOVpnrA84s5PO0","label":"","name":"Checkpoint-0.1.37-windows-x64.zip.sha256","size":101,"state":"uploaded","updatedAt":"2026-11-16T02:48:48Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.37/Checkpoint-0.1.37-windows-x64.zip.sha256"}],"isDraft":false,"isPrerelease":true,"name":"Checkpoint 0.1.37 · Interface e PT-BR","publishedAt":"2026-11-16T02:48:51Z","tagName":"v0.1.37","targetCommitish":"main","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37"}

```

stderr integral:
```text

```

Código de saída: 0

## confirmar-tag-release

UTC: 2026-11-16T02:49:40.341291+00:00

Comando: `["git", "ls-remote", "origin", "refs/tags/v0.1.37", "refs/tags/v0.1.36", "refs/heads/fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
c526cb4bc5e8721dfdfdf20222c8c1c41562ce52	refs/heads/fix/0.1.37-ajustes
4e54fc0b91ca7a4180307874f72f3b32eb3dca87	refs/tags/v0.1.36
c526cb4bc5e8721dfdfdf20222c8c1c41562ce52	refs/tags/v0.1.37

```

stderr integral:
```text

```

Código de saída: 0

## baixar-arquivos-publicados

UTC: 2026-11-16T02:49:46.423696+00:00

Comando: `["gh", "release", "download", "v0.1.37", "--dir", "/workspace/work/downloads/0137-verificado"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## digests-publicados

UTC: 2026-11-16T02:49:53.599760+00:00

Comando: `["gh", "api", "repos/pedroalexcarneiro/Checkpoint/releases/tags/v0.1.37", "--jq", "{tag_name: .tag_name, published_at: .published_at, assets: [.assets[] | {name, size, digest}]}"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"assets":[{"digest":"sha256:0049d9e10aff3cf759c781d90b736c5b8c571d624d7c1e5f99484757d4333d0e","name":"Checkpoint-0.1.37-detail-overview.png","size":96121},{"digest":"sha256:c61c2a492c2c93e146ab737e5be16e4008d84217e14d0f51103d95cff180542d","name":"Checkpoint-0.1.37-home.png","size":84584},{"digest":"sha256:19186657670ec2b8e17db3e59a27b682179105354fbceebb093748f32c79f617","name":"Checkpoint-0.1.37-library.png","size":137853},{"digest":"sha256:e3fe7008c4039fd09d774d4af05e5ee53c20243833042b7ad8677acd6d482740","name":"Checkpoint-0.1.37-ui-review.txt","size":560},{"digest":"sha256:dcac8f71c75a613905c9559816896ccaf33a6624144575ef5c0e934182ea71e8","name":"Checkpoint-0.1.37-ui-review.zip","size":3795052},{"digest":"sha256:9c24aad37a857d35844941f8ce233d36ef5313562849989edc1e89ccb62eb6d0","name":"Checkpoint-0.1.37-validation.txt","size":684},{"digest":"sha256:54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a","name":"Checkpoint-0.1.37-windows-x64.zip","size":84312887},{"digest":"sha256:d72300f38a0e3911cee1fba8f9afefcf11eea3af1262ea18df19be99dcb35d55","name":"Checkpoint-0.1.37-windows-x64.zip.sha256","size":101}],"published_at":"2026-11-16T02:48:51Z","tag_name":"v0.1.37"}

```

stderr integral:
```text

```

Código de saída: 0

## verificar-arquivos-publicados

UTC: 2026-11-16T02:50:35.191088+00:00

Comando: `["/workspace/work/venv/bin/python", "/workspace/work/evidence-0137/verify_assets.py"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{
  "assets": [
    {
      "file": "Checkpoint-0.1.37-detail-overview.png",
      "size": 96121,
      "sha256": "0049d9e10aff3cf759c781d90b736c5b8c571d624d7c1e5f99484757d4333d0e",
      "github_digest_match": true
    },
    {
      "file": "Checkpoint-0.1.37-home.png",
      "size": 84584,
      "sha256": "c61c2a492c2c93e146ab737e5be16e4008d84217e14d0f51103d95cff180542d",
      "github_digest_match": true
    },
    {
      "file": "Checkpoint-0.1.37-library.png",
      "size": 137853,
      "sha256": "19186657670ec2b8e17db3e59a27b682179105354fbceebb093748f32c79f617",
      "github_digest_match": true
    },
    {
      "file": "Checkpoint-0.1.37-ui-review.txt",
      "size": 560,
      "sha256": "e3fe7008c4039fd09d774d4af05e5ee53c20243833042b7ad8677acd6d482740",
      "github_digest_match": true
    },
    {
      "file": "Checkpoint-0.1.37-ui-review.zip",
      "size": 3795052,
      "sha256": "dcac8f71c75a613905c9559816896ccaf33a6624144575ef5c0e934182ea71e8",
      "github_digest_match": true,
      "crc_valid": true
    },
    {
      "file": "Checkpoint-0.1.37-validation.txt",
      "size": 684,
      "sha256": "9c24aad37a857d35844941f8ce233d36ef5313562849989edc1e89ccb62eb6d0",
      "github_digest_match": true
    },
    {
      "file": "Checkpoint-0.1.37-windows-x64.zip",
      "size": 84312887,
      "sha256": "54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a",
      "github_digest_match": true,
      "crc_valid": true
    },
    {
      "file": "Checkpoint-0.1.37-windows-x64.zip.sha256",
      "size": 101,
      "sha256": "d72300f38a0e3911cee1fba8f9afefcf11eea3af1262ea18df19be99dcb35d55",
      "github_digest_match": true
    }
  ],
  "windows_tests": {
    "tests": 695,
    "failures": 0,
    "errors": 0,
    "skipped": 0
  },
  "validation": "Checkpoint 0.1.37 · Windows x64\nCommit: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52\nPython: 3.12.10\nTestes: {'tests': 695, 'failures': 0, 'errors': 0, 'skipped': 0}\nSmoke do fonte: 6 páginas; SQLite íntegro; biblioteca vazia.\nSmoke do ZIP extraído: 6 páginas; SQLite íntegro; biblioteca vazia.\nAuxiliar isolado do fonte e do ZIP extraído: resposta e schema verificados.\nCadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).\nCheckpointUpdater.exe --check: saída 0.\nZIP SHA-256: 54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a\nSteam autenticada e homologação Windows 10/11 pessoal não estão cobertas.\n",
  "release_sha": "c526cb4bc5e8721dfdfdf20222c8c1c41562ce52"
}

```

stderr integral:
```text

```

Código de saída: 0

## atualizar-notas-finais

UTC: 2026-11-16T02:51:37.451618+00:00

Comando: `["gh", "release", "edit", "v0.1.37", "--notes-file", ".github/release-notes.md"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37

```

stderr integral:
```text

```

Código de saída: 0

## logs-windows-aprovado

UTC: 2026-11-16T02:51:39.769719+00:00

Comando: `["gh", "run", "view", "43793047592", "--job", "133055600675", "--log"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
build	Set up job	﻿2026-11-16T02:35:05.8603110Z Current runner version: '2.338.2'
build	Set up job	2026-11-16T02:35:05.8861477Z ##[group]Runner Image Provisioner
build	Set up job	2026-11-16T02:35:05.8862288Z Hosted Compute Agent
build	Set up job	2026-11-16T02:35:05.8862822Z Version: 20261103.629
build	Set up job	2026-11-16T02:35:05.8863397Z Commit: 15dbd9ccb5dbf34fae002b6ed1a2670f52df37bc
build	Set up job	2026-11-16T02:35:05.8864092Z Build Date: 2026-11-03T17:26:59Z
build	Set up job	2026-11-16T02:35:05.8864742Z Worker ID: {fbb3bff4-c883-40c4-9adb-174a6e67529c}
build	Set up job	2026-11-16T02:35:05.8865494Z Region: eastus
build	Set up job	2026-11-16T02:35:05.8865985Z Cloud: Azure
build	Set up job	2026-11-16T02:35:05.8866451Z ##[endgroup]
build	Set up job	2026-11-16T02:35:05.8867739Z ##[group]Operating System
build	Set up job	2026-11-16T02:35:05.8868317Z Microsoft Windows Server 2022
build	Set up job	2026-11-16T02:35:05.8868846Z 10.0.20348
build	Set up job	2026-11-16T02:35:05.8869308Z Datacenter
build	Set up job	2026-11-16T02:35:05.8869756Z ##[endgroup]
build	Set up job	2026-11-16T02:35:05.8870225Z ##[group]Runner Image
build	Set up job	2026-11-16T02:35:05.8870752Z Image: windows-2022
build	Set up job	2026-11-16T02:35:05.8871259Z Version: 20261112.366.7
build	Set up job	2026-11-16T02:35:05.8872261Z Included Software: https://github.com/actions/runner-images/blob/win22/20261112.366/images/windows/Windows2022-Readme.md
build	Set up job	2026-11-16T02:35:05.8873998Z Image Release: https://github.com/actions/runner-images/releases/tag/win22%2F20261112.366
build	Set up job	2026-11-16T02:35:05.8874884Z ##[endgroup]
build	Set up job	2026-11-16T02:35:05.8875891Z ##[group]GITHUB_TOKEN Permissions
build	Set up job	2026-11-16T02:35:05.8877897Z Contents: read
build	Set up job	2026-11-16T02:35:05.8878426Z Metadata: read
build	Set up job	2026-11-16T02:35:05.8878926Z ##[endgroup]
build	Set up job	2026-11-16T02:35:05.8880929Z Secret source: Actions
build	Set up job	2026-11-16T02:35:05.8881766Z Cache mode: write
build	Set up job	2026-11-16T02:35:05.8882427Z Prepare workflow directory
build	Set up job	2026-11-16T02:35:05.9946866Z Prepare all required actions
build	Set up job	2026-11-16T02:35:05.9996296Z Getting action download info
build	Set up job	2026-11-16T02:35:06.1839067Z Download action repository 'actions/checkout@11d5960a326750d5838078e36cf38b85af677262' (SHA:11d5960a326750d5838078e36cf38b85af677262)
build	Set up job	2026-11-16T02:35:06.3552385Z Download action repository 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
build	Set up job	2026-11-16T02:35:06.5738807Z Download action repository 'actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
build	Set up job	2026-11-16T02:35:07.3793133Z Complete job name: build
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T02:35:08.1601203Z ##[group]Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1602695Z with:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1603162Z   persist-credentials: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1603753Z   fetch-depth: 0
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1604281Z   repository: pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1612188Z   token: ***
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1612642Z   ssh-strict: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1613095Z   ssh-user: git
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1613524Z   clean: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1613998Z   sparse-checkout-cone-mode: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1614621Z   fetch-tags: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1615169Z   show-progress: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1615653Z   lfs: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1616080Z   submodules: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1616599Z   set-safe-directory: true
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1617174Z   allow-unsafe-pr-checkout: false
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1617985Z env:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1618407Z   QT_QPA_PLATFORM: offscreen
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.1618955Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.3533179Z Syncing repository: pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.3535307Z ##[group]Getting Git version info
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.3536137Z Working directory is 'D:\a\Checkpoint\Checkpoint'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.4446877Z [command]"C:\Program Files\Git\bin\git.exe" version
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.7593655Z git version 2.56.1.windows.1
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.7636397Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.7672741Z Temporarily overriding HOME='D:\a\_temp\08258330-0b25-4774-98d8-648ee57081bd' before making global git config changes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.7674969Z Adding repository directory to the temporary git global config as a safe directory
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.7677238Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.8249868Z Deleting the contents of 'D:\a\Checkpoint\Checkpoint'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.8255254Z ##[group]Initializing the repository
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.8264251Z [command]"C:\Program Files\Git\bin\git.exe" init D:\a\Checkpoint\Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.9235798Z Initialized empty Git repository in D:/a/Checkpoint/Checkpoint/.git/
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.9271929Z [command]"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.9828710Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.9830965Z ##[group]Disabling automatic garbage collection
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:08.9836409Z [command]"C:\Program Files\Git\bin\git.exe" config --local gc.auto 0
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:09.0142058Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:09.0144402Z ##[group]Setting up auth
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:09.0153795Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:09.0467025Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:10.3152370Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:10.3449326Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:10.8120415Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:10.8419460Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:11.3492008Z [command]"C:\Program Files\Git\bin\git.exe" config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ***"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:11.3790302Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:11.3791012Z ##[group]Fetching the repository
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:11.3805056Z [command]"C:\Program Files\Git\bin\git.exe" -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2001075Z From https://github.com/pedroalexcarneiro/Checkpoint
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2002245Z  * [new branch]      codex/design-fidelity-pt-br -> origin/codex/design-fidelity-pt-br
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2003270Z  * [new branch]      codex/steam-library-import -> origin/codex/steam-library-import
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2004062Z  * [new branch]      fix/0.1.29         -> origin/fix/0.1.29
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2004672Z  * [new branch]      fix/0.1.30         -> origin/fix/0.1.30
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2005293Z  * [new branch]      fix/0.1.32-visual  -> origin/fix/0.1.32-visual
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2005925Z  * [new branch]      fix/0.1.33-drive   -> origin/fix/0.1.33-drive
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2006605Z  * [new branch]      fix/0.1.34-bugs    -> origin/fix/0.1.34-bugs
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2008098Z  * [new branch]      fix/0.1.35-ajustes -> origin/fix/0.1.35-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2008856Z  * [new branch]      fix/0.1.36-ajustes -> origin/fix/0.1.36-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2009614Z  * [new branch]      fix/0.1.37-ajustes -> origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2010411Z  * [new branch]      fix/rename-redesign-0.1.28 -> origin/fix/rename-redesign-0.1.28
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2011252Z  * [new branch]      main               -> origin/main
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2011791Z  * [new tag]         v0.1.10            -> v0.1.10
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2012338Z  * [new tag]         v0.1.11            -> v0.1.11
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2012821Z  * [new tag]         v0.1.12            -> v0.1.12
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2013306Z  * [new tag]         v0.1.13            -> v0.1.13
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2013611Z  * [new tag]         v0.1.14            -> v0.1.14
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2014832Z  * [new tag]         v0.1.15            -> v0.1.15
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2015136Z  * [new tag]         v0.1.16            -> v0.1.16
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2015413Z  * [new tag]         v0.1.17            -> v0.1.17
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2016033Z  * [new tag]         v0.1.18            -> v0.1.18
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2016491Z  * [new tag]         v0.1.19            -> v0.1.19
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2016765Z  * [new tag]         v0.1.2             -> v0.1.2
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2017039Z  * [new tag]         v0.1.20            -> v0.1.20
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2017300Z  * [new tag]         v0.1.21            -> v0.1.21
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2017564Z  * [new tag]         v0.1.22            -> v0.1.22
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2017836Z  * [new tag]         v0.1.23            -> v0.1.23
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2018100Z  * [new tag]         v0.1.24            -> v0.1.24
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2018361Z  * [new tag]         v0.1.25            -> v0.1.25
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2018640Z  * [new tag]         v0.1.26            -> v0.1.26
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2018912Z  * [new tag]         v0.1.27            -> v0.1.27
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2019176Z  * [new tag]         v0.1.28            -> v0.1.28
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2019527Z  * [new tag]         v0.1.29            -> v0.1.29
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2019831Z  * [new tag]         v0.1.3             -> v0.1.3
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2020100Z  * [new tag]         v0.1.30            -> v0.1.30
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2104299Z  * [new tag]         v0.1.32            -> v0.1.32
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2104946Z  * [new tag]         v0.1.33            -> v0.1.33
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2105439Z  * [new tag]         v0.1.34            -> v0.1.34
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2105892Z  * [new tag]         v0.1.35            -> v0.1.35
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2106350Z  * [new tag]         v0.1.36            -> v0.1.36
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2106809Z  * [new tag]         v0.1.4             -> v0.1.4
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2107305Z  * [new tag]         v0.1.5             -> v0.1.5
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2107800Z  * [new tag]         v0.1.6             -> v0.1.6
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2108279Z  * [new tag]         v0.1.7             -> v0.1.7
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2108754Z  * [new tag]         v0.1.8             -> v0.1.8
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2109239Z  * [new tag]         v0.1.9             -> v0.1.9
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2111964Z [command]"C:\Program Files\Git\bin\git.exe" branch --list --remote origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2855794Z   origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.2895478Z [command]"C:\Program Files\Git\bin\git.exe" rev-parse refs/remotes/origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3236157Z c526cb4bc5e8721dfdfdf20222c8c1c41562ce52
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3261531Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3261950Z ##[group]Determining the checkout info
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3263265Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3272275Z [command]"C:\Program Files\Git\bin\git.exe" sparse-checkout disable
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.3776992Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all extensions.worktreeConfig
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.4059113Z ##[group]Checking out the ref
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.4067965Z [command]"C:\Program Files\Git\bin\git.exe" checkout --progress --force -B fix/0.1.37-ajustes refs/remotes/origin/fix/0.1.37-ajustes
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.6369279Z Switched to a new branch 'fix/0.1.37-ajustes'
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.6388373Z branch 'fix/0.1.37-ajustes' set up to track 'origin/fix/0.1.37-ajustes'.
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.6437627Z ##[endgroup]
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.6848084Z [command]"C:\Program Files\Git\bin\git.exe" log -1 --format=%H
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.7105123Z c526cb4bc5e8721dfdfdf20222c8c1c41562ce52
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.7138874Z ##[group]Removing auth
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.7150441Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:13.7432122Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.2096636Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.2354695Z http.https://github.com/.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.2392285Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.2698231Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.7274898Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:14.7554182Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:35:15.2094088Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	﻿2026-11-16T02:35:15.2477569Z ##[group]Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2478050Z with:
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2478240Z   python-version: 3.12
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2478460Z   architecture: x64
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2478646Z   cache: pip
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2478870Z   cache-dependency-path: requirements-tested.txt
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2479164Z   check-latest: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2481873Z   token: ***
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2482083Z   update-environment: true
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2482319Z   allow-prereleases: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2482553Z   freethreaded: false
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2482760Z env:
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2482933Z   QT_QPA_PLATFORM: offscreen
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.2483147Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.4005143Z ##[group]Installed versions
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.4217090Z (node:4784) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.4218011Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.4219695Z Successfully set up CPython (3.12.10)
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:15.4220816Z ##[endgroup]
build	Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:35:17.8813165Z pip cache is not found
build	Check release version	﻿2026-11-16T02:35:17.9063803Z ##[group]Run $version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'
build	Check release version	2026-11-16T02:35:17.9065463Z [36;1m$version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'[0m
build	Check release version	2026-11-16T02:35:17.9066444Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao ler a versão.' }[0m
build	Check release version	2026-11-16T02:35:17.9066916Z [36;1mif ($version -notmatch '^\d+\.\d+\.\d+$') { throw 'Versão inválida.' }[0m
build	Check release version	2026-11-16T02:35:17.9067321Z [36;1m"version=$version" >> $env:GITHUB_OUTPUT[0m
build	Check release version	2026-11-16T02:35:17.9182826Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Check release version	2026-11-16T02:35:17.9183222Z env:
build	Check release version	2026-11-16T02:35:17.9183415Z   QT_QPA_PLATFORM: offscreen
build	Check release version	2026-11-16T02:35:17.9183756Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:35:17.9184304Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Check release version	2026-11-16T02:35:17.9184794Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:35:17.9185232Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:35:17.9185661Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Check release version	2026-11-16T02:35:17.9186001Z ##[endgroup]
build	Install tested Windows dependencies	﻿2026-11-16T02:35:18.4526171Z ##[group]Run python -m pip install -r requirements-tested.txt
build	Install tested Windows dependencies	2026-11-16T02:35:18.4526710Z [36;1mpython -m pip install -r requirements-tested.txt[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4527188Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependências.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4527889Z [36;1mpython -m pip install --no-deps --no-build-isolation -e .[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4528337Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar o projeto.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4528701Z [36;1mpython -m pip check[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4529024Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências inconsistentes.' }[0m
build	Install tested Windows dependencies	2026-11-16T02:35:18.4568313Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Install tested Windows dependencies	2026-11-16T02:35:18.4568663Z env:
build	Install tested Windows dependencies	2026-11-16T02:35:18.4568845Z   QT_QPA_PLATFORM: offscreen
build	Install tested Windows dependencies	2026-11-16T02:35:18.4569162Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:35:18.4569613Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Install tested Windows dependencies	2026-11-16T02:35:18.4570092Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:35:18.4570478Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:35:18.4570871Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Install tested Windows dependencies	2026-11-16T02:35:18.4571208Z ##[endgroup]
build	Install tested Windows dependencies	2026-11-16T02:35:21.2997304Z Collecting altgraph==0.17.5 (from -r requirements-tested.txt (line 1))
build	Install tested Windows dependencies	2026-11-16T02:35:21.5350006Z   Downloading altgraph-0.17.5-py2.py3-none-any.whl.metadata (7.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:21.6248160Z Collecting certifi==2026.10.23 (from -r requirements-tested.txt (line 2))
build	Install tested Windows dependencies	2026-11-16T02:35:21.6542661Z   Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:21.8600537Z Collecting cffi==2.1.1 (from -r requirements-tested.txt (line 3))
build	Install tested Windows dependencies	2026-11-16T02:35:21.8899978Z   Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.0656662Z Collecting charset-normalizer==3.5.2 (from -r requirements-tested.txt (line 4))
build	Install tested Windows dependencies	2026-11-16T02:35:22.0932308Z   Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.1640731Z Requirement already satisfied: colorama==0.4.6 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 5)) (0.4.6)
build	Install tested Windows dependencies	2026-11-16T02:35:22.3719080Z Collecting cryptography==50.0.2 (from -r requirements-tested.txt (line 6))
build	Install tested Windows dependencies	2026-11-16T02:35:22.3999755Z   Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl.metadata (4.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.4692168Z Collecting google-api-core==2.44.0 (from -r requirements-tested.txt (line 7))
build	Install tested Windows dependencies	2026-11-16T02:35:22.4980040Z   Downloading google_api_core-2.44.0-py3-none-any.whl.metadata (3.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.5790739Z Collecting google-api-python-client==2.202.0 (from -r requirements-tested.txt (line 8))
build	Install tested Windows dependencies	2026-11-16T02:35:22.6079519Z   Downloading google_api_python_client-2.202.0-py3-none-any.whl.metadata (6.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.6622004Z Collecting google-auth-httplib2==0.4.4 (from -r requirements-tested.txt (line 9))
build	Install tested Windows dependencies	2026-11-16T02:35:22.6924389Z   Downloading google_auth_httplib2-0.4.4-py3-none-any.whl.metadata (3.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.7438918Z Collecting google-auth-oauthlib==1.5.0 (from -r requirements-tested.txt (line 10))
build	Install tested Windows dependencies	2026-11-16T02:35:22.7712308Z   Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.8422061Z Collecting google-auth==2.62.2 (from -r requirements-tested.txt (line 11))
build	Install tested Windows dependencies	2026-11-16T02:35:22.8704336Z   Downloading google_auth-2.62.2-py3-none-any.whl.metadata (6.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:22.9560868Z Collecting googleapis-common-protos==1.76.0 (from -r requirements-tested.txt (line 12))
build	Install tested Windows dependencies	2026-11-16T02:35:22.9851930Z   Downloading googleapis_common_protos-1.76.0-py3-none-any.whl.metadata (8.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.0563892Z Collecting httplib2==0.32.1 (from -r requirements-tested.txt (line 13))
build	Install tested Windows dependencies	2026-11-16T02:35:23.0845360Z   Downloading httplib2-0.32.1-py3-none-any.whl.metadata (2.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.1496345Z Collecting idna==3.20 (from -r requirements-tested.txt (line 14))
build	Install tested Windows dependencies	2026-11-16T02:35:23.1810862Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.2372470Z Collecting iniconfig==2.3.1 (from -r requirements-tested.txt (line 15))
build	Install tested Windows dependencies	2026-11-16T02:35:23.2646693Z   Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.3251695Z Collecting jaraco-classes==3.4.0 (from -r requirements-tested.txt (line 16))
build	Install tested Windows dependencies	2026-11-16T02:35:23.3527917Z   Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.4310354Z Collecting jaraco-context==6.1.2 (from -r requirements-tested.txt (line 17))
build	Install tested Windows dependencies	2026-11-16T02:35:23.4670848Z   Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.5320271Z Collecting jaraco-functools==4.6.0 (from -r requirements-tested.txt (line 18))
build	Install tested Windows dependencies	2026-11-16T02:35:23.5597293Z   Downloading jaraco_functools-4.6.0-py3-none-any.whl.metadata (2.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.6278260Z Collecting keyring==25.7.0 (from -r requirements-tested.txt (line 19))
build	Install tested Windows dependencies	2026-11-16T02:35:23.6621378Z   Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.7269645Z Collecting more-itertools==11.2.1 (from -r requirements-tested.txt (line 20))
build	Install tested Windows dependencies	2026-11-16T02:35:23.7573444Z   Downloading more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.8269377Z Collecting oauthlib==4.0.1 (from -r requirements-tested.txt (line 21))
build	Install tested Windows dependencies	2026-11-16T02:35:23.8557073Z   Downloading oauthlib-4.0.1-py3-none-any.whl.metadata (8.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.9158665Z Collecting opentelemetry-api==1.45.2 (from -r requirements-tested.txt (line 22))
build	Install tested Windows dependencies	2026-11-16T02:35:23.9430611Z   Downloading opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:23.9682190Z Requirement already satisfied: packaging==26.3 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 23)) (26.3)
build	Install tested Windows dependencies	2026-11-16T02:35:24.0061488Z Collecting pefile==2024.8.26 (from -r requirements-tested.txt (line 24))
build	Install tested Windows dependencies	2026-11-16T02:35:24.0344577Z   Downloading pefile-2024.8.26-py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.0886196Z Collecting pluggy==1.7.0 (from -r requirements-tested.txt (line 25))
build	Install tested Windows dependencies	2026-11-16T02:35:24.1275176Z   Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.2011850Z Collecting proto-plus==1.29.0 (from -r requirements-tested.txt (line 26))
build	Install tested Windows dependencies	2026-11-16T02:35:24.2289194Z   Downloading proto_plus-1.29.0-py3-none-any.whl.metadata (2.2 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.4438917Z Collecting protobuf==7.36.2 (from -r requirements-tested.txt (line 27))
build	Install tested Windows dependencies	2026-11-16T02:35:24.4715783Z   Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
build	Install tested Windows dependencies	2026-11-16T02:35:24.5424012Z Collecting pyasn1-modules==0.4.2 (from -r requirements-tested.txt (line 28))
build	Install tested Windows dependencies	2026-11-16T02:35:24.5754308Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.6428038Z Collecting pyasn1==0.6.5 (from -r requirements-tested.txt (line 29))
build	Install tested Windows dependencies	2026-11-16T02:35:24.6712401Z   Downloading pyasn1-0.6.5-py3-none-any.whl.metadata (8.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.7367533Z Collecting pycparser==3.12 (from -r requirements-tested.txt (line 30))
build	Install tested Windows dependencies	2026-11-16T02:35:24.7814256Z   Downloading pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.8630498Z Collecting pygments==2.21.0 (from -r requirements-tested.txt (line 31))
build	Install tested Windows dependencies	2026-11-16T02:35:24.8924724Z   Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:24.9599485Z Collecting pyinstaller-hooks-contrib==2026.10 (from -r requirements-tested.txt (line 32))
build	Install tested Windows dependencies	2026-11-16T02:35:25.0066069Z   Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl.metadata (16 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.1010972Z Collecting pyinstaller==6.22.3 (from -r requirements-tested.txt (line 33))
build	Install tested Windows dependencies	2026-11-16T02:35:25.1406937Z   Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl.metadata (8.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.2146146Z Collecting pyparsing==3.3.3 (from -r requirements-tested.txt (line 34))
build	Install tested Windows dependencies	2026-11-16T02:35:25.2654688Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.3484792Z Collecting pyside6-addons==6.8.3 (from -r requirements-tested.txt (line 35))
build	Install tested Windows dependencies	2026-11-16T02:35:25.3839990Z   Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.5558498Z Collecting pyside6-essentials==6.8.3 (from -r requirements-tested.txt (line 36))
build	Install tested Windows dependencies	2026-11-16T02:35:25.6028665Z   Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.1 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.6809493Z Collecting pyside6==6.8.3 (from -r requirements-tested.txt (line 37))
build	Install tested Windows dependencies	2026-11-16T02:35:25.7347648Z   Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl.metadata (5.7 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.8067888Z Collecting pytest==9.2.0 (from -r requirements-tested.txt (line 38))
build	Install tested Windows dependencies	2026-11-16T02:35:25.8864176Z   Downloading pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:25.9432572Z Collecting pywin32-ctypes==0.2.3 (from -r requirements-tested.txt (line 39))
build	Install tested Windows dependencies	2026-11-16T02:35:25.9954753Z   Downloading pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.0846596Z Collecting requests-oauthlib==2.0.0 (from -r requirements-tested.txt (line 40))
build	Install tested Windows dependencies	2026-11-16T02:35:26.1151696Z   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.1809163Z Collecting requests==2.34.2 (from -r requirements-tested.txt (line 41))
build	Install tested Windows dependencies	2026-11-16T02:35:26.2160669Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.3588156Z Collecting setuptools==84.2.1 (from -r requirements-tested.txt (line 42))
build	Install tested Windows dependencies	2026-11-16T02:35:26.3941985Z   Downloading setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.4667556Z Collecting shiboken6==6.8.3 (from -r requirements-tested.txt (line 43))
build	Install tested Windows dependencies	2026-11-16T02:35:26.5117600Z   Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl.metadata (2.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.5719577Z Collecting typing-extensions==4.16.0 (from -r requirements-tested.txt (line 44))
build	Install tested Windows dependencies	2026-11-16T02:35:26.6104406Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.6718129Z Collecting tzdata==2026.6 (from -r requirements-tested.txt (line 45))
build	Install tested Windows dependencies	2026-11-16T02:35:26.7138864Z   Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:26.9816757Z Collecting uritemplate==4.2.0 (from -r requirements-tested.txt (line 46))
build	Install tested Windows dependencies	2026-11-16T02:35:27.0104708Z   Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.0950213Z Collecting urllib3==2.8.0 (from -r requirements-tested.txt (line 47))
build	Install tested Windows dependencies	2026-11-16T02:35:27.1235633Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.2441790Z Downloading altgraph-0.17.5-py2.py3-none-any.whl (21 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.2975159Z Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.3971161Z Downloading cffi-2.1.1-cp312-cp312-win_amd64.whl (185 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.4600528Z Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.5292364Z Downloading cryptography-50.0.2-cp311-abi3-win_amd64.whl (3.8 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.6412027Z    ---------------------------------------- 3.8/3.8 MB 32.4 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:27.6813065Z Downloading google_api_core-2.44.0-py3-none-any.whl (225 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.7269033Z Downloading google_auth-2.62.2-py3-none-any.whl (270 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.7747773Z Downloading googleapis_common_protos-1.76.0-py3-none-any.whl (307 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.8231441Z Downloading opentelemetry_api-1.45.2-py3-none-any.whl (60 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.8757531Z Downloading proto_plus-1.29.0-py3-none-any.whl (50 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.9266153Z Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:27.9731893Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.0182743Z Downloading idna-3.20-py3-none-any.whl (69 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.0665359Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.1447659Z Downloading google_api_python_client-2.202.0-py3-none-any.whl (17.1 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.3297267Z    ---------------------------------------- 17.1/17.1 MB 107.6 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:28.3621760Z Downloading google_auth_httplib2-0.4.4-py3-none-any.whl (9.5 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.4052938Z Downloading httplib2-0.32.1-py3-none-any.whl (92 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.4515356Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.4965202Z Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.5416456Z Downloading google_auth_oauthlib-1.5.0-py3-none-any.whl (20 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.5947997Z Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.6395923Z Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.6943134Z Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.7555201Z Downloading jaraco_functools-4.6.0-py3-none-any.whl (11 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.8111725Z Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.8693969Z Downloading more_itertools-11.2.1-py3-none-any.whl (74 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.9158798Z Downloading oauthlib-4.0.1-py3-none-any.whl (161 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:28.9670408Z Downloading pefile-2024.8.26-py3-none-any.whl (74 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.0326266Z Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.0775668Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.1301515Z Downloading pyasn1-0.6.5-py3-none-any.whl (84 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.1753400Z Downloading pycparser-3.12-py3-none-any.whl (62 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.2213290Z Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.2495657Z    ---------------------------------------- 1.3/1.3 MB 61.8 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:29.2812309Z Downloading pyinstaller_hooks_contrib-2026.10-py3-none-any.whl (463 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.3316733Z Downloading pyinstaller-6.22.3-py3-none-win_amd64.whl (1.5 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:29.3596132Z    ---------------------------------------- 1.5/1.5 MB 74.5 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:29.3939034Z Downloading PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl (127.9 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:33.0915185Z    ---------------------------------------- 127.9/127.9 MB 34.6 MB/s  0:00:03
build	Install tested Windows dependencies	2026-11-16T02:35:33.1227718Z Downloading PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl (72.2 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:34.7833308Z    ---------------------------------------- 72.2/72.2 MB 43.4 MB/s  0:00:01
build	Install tested Windows dependencies	2026-11-16T02:35:34.8139568Z Downloading PySide6-6.8.3-cp39-abi3-win_amd64.whl (561 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:34.8390095Z    ---------------------------------------- 561.1/561.1 kB 19.9 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:34.8720577Z Downloading pytest-9.2.0-py3-none-any.whl (411 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:34.9197605Z Downloading pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:34.9632508Z Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:35.0092307Z Downloading setuptools-84.2.1-py3-none-any.whl (876 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:35.0331909Z    ---------------------------------------- 876.3/876.3 kB 19.8 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:35.0617971Z Downloading shiboken6-6.8.3-cp39-abi3-win_amd64.whl (1.2 MB)
build	Install tested Windows dependencies	2026-11-16T02:35:35.0999504Z    ---------------------------------------- 1.2/1.2 MB 28.7 MB/s  0:00:00
build	Install tested Windows dependencies	2026-11-16T02:35:35.1295229Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:35.1757947Z Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
build	Install tested Windows dependencies	2026-11-16T02:35:35.8878930Z Installing collected packages: altgraph, urllib3, uritemplate, tzdata, typing-extensions, shiboken6, setuptools, pywin32-ctypes, pyparsing, pyinstaller-hooks-contrib, pygments, pycparser, pyasn1, protobuf, pluggy, pefile, oauthlib, more-itertools, jaraco-context, iniconfig, idna, charset-normalizer, certifi, requests, pytest, pyside6-essentials, pyinstaller, pyasn1-modules, proto-plus, opentelemetry-api, jaraco-functools, jaraco-classes, httplib2, googleapis-common-protos, cffi, requests-oauthlib, pyside6-addons, keyring, cryptography, pyside6, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-core, google-api-python-client
build	Install tested Windows dependencies	2026-11-16T02:36:04.7572029Z 
build	Install tested Windows dependencies	2026-11-16T02:36:04.7621545Z Successfully installed altgraph-0.17.5 certifi-2026.10.23 cffi-2.1.1 charset-normalizer-3.5.2 cryptography-50.0.2 google-api-core-2.44.0 google-api-python-client-2.202.0 google-auth-2.62.2 google-auth-httplib2-0.4.4 google-auth-oauthlib-1.5.0 googleapis-common-protos-1.76.0 httplib2-0.32.1 idna-3.20 iniconfig-2.3.1 jaraco-classes-3.4.0 jaraco-context-6.1.2 jaraco-functools-4.6.0 keyring-25.7.0 more-itertools-11.2.1 oauthlib-4.0.1 opentelemetry-api-1.45.2 pefile-2024.8.26 pluggy-1.7.0 proto-plus-1.29.0 protobuf-7.36.2 pyasn1-0.6.5 pyasn1-modules-0.4.2 pycparser-3.12 pygments-2.21.0 pyinstaller-6.22.3 pyinstaller-hooks-contrib-2026.10 pyparsing-3.3.3 pyside6-6.8.3 pyside6-addons-6.8.3 pyside6-essentials-6.8.3 pytest-9.2.0 pywin32-ctypes-0.2.3 requests-2.34.2 requests-oauthlib-2.0.0 setuptools-84.2.1 shiboken6-6.8.3 typing-extensions-4.16.0 tzdata-2026.6 uritemplate-4.2.0 urllib3-2.8.0
build	Install tested Windows dependencies	2026-11-16T02:36:06.0338287Z Obtaining file:///D:/a/Checkpoint/Checkpoint
build	Install tested Windows dependencies	2026-11-16T02:36:06.0358395Z   Checking if build backend supports build_editable: started
build	Install tested Windows dependencies	2026-11-16T02:36:06.3742031Z   Checking if build backend supports build_editable: finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:36:06.3764899Z   Preparing editable metadata (pyproject.toml): started
build	Install tested Windows dependencies	2026-11-16T02:36:06.8822262Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:36:06.8886738Z Building wheels for collected packages: checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:36:06.8909544Z   Building editable for checkpoint-desktop (pyproject.toml): started
build	Install tested Windows dependencies	2026-11-16T02:36:07.3589654Z   Building editable for checkpoint-desktop (pyproject.toml): finished with status 'done'
build	Install tested Windows dependencies	2026-11-16T02:36:07.3606979Z   C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\setuptools\command\editable_wheel.py:354: BuildBackendWarning: Editable installation.
build	Install tested Windows dependencies	2026-11-16T02:36:07.3608294Z   !!
build	Install tested Windows dependencies	2026-11-16T02:36:07.3608597Z   
build	Install tested Windows dependencies	2026-11-16T02:36:07.3609012Z           ********************************************************************************
build	Install tested Windows dependencies	2026-11-16T02:36:07.3609788Z           Please be careful with folders in your working directory with the same
build	Install tested Windows dependencies	2026-11-16T02:36:07.3611024Z           name as your package as they may take precedence during imports.
build	Install tested Windows dependencies	2026-11-16T02:36:07.3611820Z           ********************************************************************************
build	Install tested Windows dependencies	2026-11-16T02:36:07.3612390Z   
build	Install tested Windows dependencies	2026-11-16T02:36:07.3612694Z   !!
build	Install tested Windows dependencies	2026-11-16T02:36:07.3613118Z     with strategy, WheelFile(wheel_path, "w") as wheel_obj:
build	Install tested Windows dependencies	2026-11-16T02:36:07.3641152Z   Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.37-0.editable-py3-none-any.whl size=3269 sha256=ba107bd67ce45167de7db295303ea7e9ec5968ffeba8beccb7f359b9636a644d
build	Install tested Windows dependencies	2026-11-16T02:36:07.3643600Z   Stored in directory: C:\Users\runneradmin\AppData\Local\Temp\pip-ephem-wheel-cache-3qj3j9a0\wheels\a2\38\6e\88ad7ec70fd74394064971fa20d15ccdcdb6f76505932df31d
build	Install tested Windows dependencies	2026-11-16T02:36:07.3670977Z Successfully built checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:36:07.3899646Z Installing collected packages: checkpoint-desktop
build	Install tested Windows dependencies	2026-11-16T02:36:07.4265963Z Successfully installed checkpoint-desktop-0.1.37
build	Install tested Windows dependencies	2026-11-16T02:36:07.8342198Z No broken requirements found.
build	Test on Windows	﻿2026-11-16T02:36:07.9555081Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'
build	Test on Windows	2026-11-16T02:36:07.9555789Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'[0m
build	Test on Windows	2026-11-16T02:36:07.9556419Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
build	Test on Windows	2026-11-16T02:36:07.9556990Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
build	Test on Windows	2026-11-16T02:36:07.9597830Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Test on Windows	2026-11-16T02:36:07.9598188Z env:
build	Test on Windows	2026-11-16T02:36:07.9598373Z   QT_QPA_PLATFORM: offscreen
build	Test on Windows	2026-11-16T02:36:07.9598716Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:36:07.9599173Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Test on Windows	2026-11-16T02:36:07.9600353Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:36:07.9600761Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:36:07.9601388Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-16T02:36:07.9601934Z ##[endgroup]
build	Test on Windows	2026-11-16T02:36:22.1091562Z ........................................................................ [ 10%]
build	Test on Windows	2026-11-16T02:36:32.9078890Z ........................................................................ [ 20%]
build	Test on Windows	2026-11-16T02:36:47.2559831Z ........................................................................ [ 31%]
build	Test on Windows	2026-11-16T02:36:52.1824366Z ........................................................................ [ 41%]
build	Test on Windows	2026-11-16T02:37:17.7278576Z ........................................................................ [ 51%]
build	Test on Windows	2026-11-16T02:38:56.8821146Z ........................................................................ [ 62%]
build	Test on Windows	2026-11-16T02:39:36.6702852Z ........................................................................ [ 72%]
build	Test on Windows	2026-11-16T02:41:29.8729375Z ........................................................................ [ 82%]
build	Test on Windows	2026-11-16T02:46:07.9426047Z ........................................................................ [ 93%]
build	Test on Windows	2026-11-16T02:46:47.2837515Z ...............................................                          [100%]
build	Test on Windows	2026-11-16T02:46:47.2838385Z 695 passed in 638.21s (0:10:38)
build	Build desktop and updater	﻿2026-11-16T02:46:48.1993162Z ##[group]Run ./scripts/build.ps1 -Python (Get-Command python).Source
build	Build desktop and updater	2026-11-16T02:46:48.1993830Z [36;1m./scripts/build.ps1 -Python (Get-Command python).Source[0m
build	Build desktop and updater	2026-11-16T02:46:48.2035395Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Build desktop and updater	2026-11-16T02:46:48.2035810Z env:
build	Build desktop and updater	2026-11-16T02:46:48.2036047Z   QT_QPA_PLATFORM: offscreen
build	Build desktop and updater	2026-11-16T02:46:48.2036413Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:46:48.2036931Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Build desktop and updater	2026-11-16T02:46:48.2037429Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:46:48.2037874Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:46:48.2038418Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:46:48.2038782Z ##[endgroup]
build	Build desktop and updater	2026-11-16T02:46:49.2122442Z 203 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
build	Build desktop and updater	2026-11-16T02:46:49.2125619Z 203 INFO: Python: 3.12.10
build	Build desktop and updater	2026-11-16T02:46:49.2314655Z 235 INFO: Platform: Windows-2022Server-10.0.20348-SP0
build	Build desktop and updater	2026-11-16T02:46:49.2315238Z 235 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:46:49.2320199Z 235 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint.spec
build	Build desktop and updater	2026-11-16T02:46:49.2834223Z 282 INFO: Module search paths (PYTHONPATH):
build	Build desktop and updater	2026-11-16T02:46:49.2835025Z ['D:\\a\\Checkpoint\\Checkpoint',
build	Build desktop and updater	2026-11-16T02:46:49.2835552Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
build	Build desktop and updater	2026-11-16T02:46:49.2836192Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
build	Build desktop and updater	2026-11-16T02:46:49.2836753Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
build	Build desktop and updater	2026-11-16T02:46:49.2837277Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
build	Build desktop and updater	2026-11-16T02:46:49.2837860Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
build	Build desktop and updater	2026-11-16T02:46:49.2838498Z  '__editable__.checkpoint_desktop-0.1.37.finder.__path_hook__',
build	Build desktop and updater	2026-11-16T02:46:49.2839117Z  'D:\\a\\Checkpoint\\Checkpoint']
build	Build desktop and updater	2026-11-16T02:46:49.5165200Z 517 INFO: Appending 'datas' from .spec
build	Build desktop and updater	2026-11-16T02:46:49.5187704Z 517 INFO: checking Analysis
build	Build desktop and updater	2026-11-16T02:46:49.5188637Z 517 INFO: Building Analysis because Analysis-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:46:49.5189543Z 517 INFO: Looking for Python shared library...
build	Build desktop and updater	2026-11-16T02:46:49.5190599Z 517 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
build	Build desktop and updater	2026-11-16T02:46:49.5192085Z 517 INFO: Running Analysis Analysis-00.toc
build	Build desktop and updater	2026-11-16T02:46:49.5192538Z 517 INFO: Target bytecode optimization level: 0
build	Build desktop and updater	2026-11-16T02:46:49.5192991Z 517 INFO: Initializing module dependency graph...
build	Build desktop and updater	2026-11-16T02:46:49.5201253Z 517 INFO: Initializing module graph hook caches...
build	Build desktop and updater	2026-11-16T02:46:49.5359726Z 532 INFO: Analyzing modules for base_library.zip ...
build	Build desktop and updater	2026-11-16T02:46:50.6007708Z 1596 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:50.9523777Z 1955 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:52.1809720Z 3175 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:53.3034441Z 4302 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:53.8239421Z 4818 INFO: Caching module dependency graph...
build	Build desktop and updater	2026-11-16T02:46:53.8627764Z 4865 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_checkpoint.py
build	Build desktop and updater	2026-11-16T02:46:54.0297743Z 5021 INFO: Processing standard module hook 'hook-PySide6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:54.1850881Z 5179 INFO: Processing standard module hook 'hook-shiboken6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:54.3152850Z 5319 INFO: Processing standard module hook 'hook-PySide6.QtNetwork.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:56.4362140Z 7434 INFO: Processing standard module hook 'hook-PySide6.QtCore.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:46:59.4018593Z 10406 INFO: Processing standard module hook 'hook-PySide6.QtWidgets.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:02.1018659Z 13097 INFO: Processing standard module hook 'hook-PySide6.QtGui.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:29.3682247Z 40358 INFO: Processing standard module hook 'hook-sqlite3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:29.6420938Z 40640 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:29.8120106Z 40812 INFO: Processing standard module hook 'hook-keyring.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:30.2718356Z 41265 INFO: Processing pre-safe-import-module hook 'hook-jaraco.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:30.2725843Z 41265 INFO: SetuptoolsInfo: initializing cached setuptools info...
build	Build desktop and updater	2026-11-16T02:47:30.7352914Z 41734 INFO: Setuptools: 'jaraco' appears to be a partial setuptools-vendored copy - extending search paths to ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\jaraco', 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\setuptools\\_vendor\\jaraco']!
build	Build desktop and updater	2026-11-16T02:47:30.7361269Z 41734 INFO: Processing pre-safe-import-module hook 'hook-jaraco.context.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:30.9500495Z 41953 INFO: Processing pre-safe-import-module hook 'hook-backports.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:30.9502769Z 41953 INFO: Setuptools: 'backports' appears to be a full setuptools-vendored copy - creating alias to 'setuptools._vendor.backports'!
build	Build desktop and updater	2026-11-16T02:47:30.9556630Z 41953 INFO: Processing standard module hook 'hook-setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:30.9668169Z 41968 INFO: Processing pre-safe-import-module hook 'hook-distutils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:31.0190236Z 42015 INFO: Processing standard module hook 'hook-sysconfig.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:31.0278121Z 42033 INFO: Processing pre-safe-import-module hook 'hook-jaraco.functools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:31.0379463Z 42033 INFO: Processing pre-safe-import-module hook 'hook-more_itertools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:31.2012895Z 42203 INFO: Processing standard module hook 'hook-_osx_support.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:31.2048601Z 42203 INFO: Processing pre-safe-import-module hook 'hook-typing_extensions.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:31.4691932Z 42469 INFO: Processing standard module hook 'hook-multiprocessing.util.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:31.5531240Z 42547 INFO: Processing standard module hook 'hook-xml.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:31.7862127Z 42782 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:32.1378715Z 43142 INFO: Processing pre-safe-import-module hook 'hook-packaging.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:32.4808271Z 43486 INFO: Processing pre-safe-import-module hook 'hook-jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:32.4810332Z 43486 INFO: Setuptools: 'jaraco.text' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.jaraco.text'!
build	Build desktop and updater	2026-11-16T02:47:32.4926356Z 43495 INFO: Processing standard module hook 'hook-setuptools._vendor.jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:32.4938536Z 43495 INFO: Processing pre-safe-import-module hook 'hook-importlib_resources.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:32.8950271Z 43892 INFO: Processing pre-safe-import-module hook 'hook-tomli.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:32.8952285Z 43892 INFO: Setuptools: 'tomli' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.tomli'!
build	Build desktop and updater	2026-11-16T02:47:33.5023841Z 44503 INFO: Processing pre-safe-import-module hook 'hook-wheel.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:33.5026201Z 44503 INFO: Setuptools: 'wheel' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.wheel'!
build	Build desktop and updater	2026-11-16T02:47:33.6249615Z 44628 INFO: Processing pre-safe-import-module hook 'hook-importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:33.6252272Z 44628 INFO: Setuptools: 'importlib_metadata' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.importlib_metadata'!
build	Build desktop and updater	2026-11-16T02:47:33.6479674Z 44644 INFO: Processing standard module hook 'hook-setuptools._vendor.importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:33.6686090Z 44659 INFO: Processing pre-safe-import-module hook 'hook-zipp.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:33.6687799Z 44659 INFO: Setuptools: 'zipp' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.zipp'!
build	Build desktop and updater	2026-11-16T02:47:33.7149600Z 44706 INFO: Processing standard module hook 'hook-win32ctypes.core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:34.4502555Z 45441 INFO: Processing standard module hook 'hook-pycparser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:34.9059847Z 45911 INFO: Processing standard module hook 'hook-webbrowser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:35.1810758Z 46179 INFO: Processing standard module hook 'hook-cryptography.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:36.2007325Z 47192 INFO: hook-cryptography: cryptography does not seem to be using dynamically linked OpenSSL.
build	Build desktop and updater	2026-11-16T02:47:36.9250328Z 47927 INFO: Processing standard module hook 'hook-urllib3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:37.4113668Z 48411 INFO: Processing standard module hook 'hook-certifi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:37.4586111Z 48458 INFO: Processing standard module hook 'hook-charset_normalizer.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:38.1010232Z 49100 INFO: Processing standard module hook 'hook-google.api_core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:38.1246088Z 49116 INFO: Processing standard module hook 'hook-opentelemetry.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:38.4383924Z 49432 INFO: Processing standard module hook 'hook-httplib2.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:38.7733108Z 49772 INFO: Processing standard module hook 'hook-difflib.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:38.9984077Z 49991 INFO: Processing standard module hook 'hook-googleapiclient.model.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
build	Build desktop and updater	2026-11-16T02:47:39.4851206Z 50476 INFO: Processing standard module hook 'hook-PySide6.QtSvg.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:40.1816018Z 51179 INFO: Processing standard module hook 'hook-xml.etree.cElementTree.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:40.4853272Z 51477 INFO: Processing module hooks (post-graph stage)...
build	Build desktop and updater	2026-11-16T02:47:40.5052646Z 51508 WARNING: Hidden import "pycparser.lextab" not found!
build	Build desktop and updater	2026-11-16T02:47:40.5053813Z 51508 WARNING: Hidden import "pycparser.yacctab" not found!
build	Build desktop and updater	2026-11-16T02:47:40.5311236Z 51523 INFO: Processing pre-safe-import-module hook 'hook-gi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
build	Build desktop and updater	2026-11-16T02:47:40.6788810Z 51680 INFO: Performing binary vs. data reclassification (813 entries)
build	Build desktop and updater	2026-11-16T02:47:40.7495602Z 51742 INFO: Looking for ctypes DLLs
build	Build desktop and updater	2026-11-16T02:47:40.7847476Z 51789 INFO: Analyzing run-time hooks ...
build	Build desktop and updater	2026-11-16T02:47:40.7892107Z 51789 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.7915657Z 51789 INFO: Including run-time hook 'pyi_rth_pkgutil.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.7935380Z 51789 INFO: Including run-time hook 'pyi_rth_multiprocessing.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.7956034Z 51789 INFO: Including run-time hook 'pyi_rth_setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.7967789Z 51789 INFO: Including run-time hook 'pyi_rth_pyside6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.7984679Z 51789 INFO: Processing pre-find-module-path hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path'
build	Build desktop and updater	2026-11-16T02:47:40.7998856Z 51805 INFO: Processing standard module hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:40.8025105Z 51805 INFO: Including run-time hook 'pyi_rth_cryptography_openssl.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:40.8342644Z 51836 INFO: Creating base_library.zip...
build	Build desktop and updater	2026-11-16T02:47:40.8549347Z 51852 INFO: Looking for dynamic libraries
build	Build desktop and updater	2026-11-16T02:47:41.5883535Z 52592 INFO: Extra DLL search directories (AddDllDirectory): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\shiboken6']
build	Build desktop and updater	2026-11-16T02:47:41.5884648Z 52592 INFO: Extra DLL search directories (PATH): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PySide6']
build	Build desktop and updater	2026-11-16T02:47:43.3473232Z 54344 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\warn-Checkpoint.txt
build	Build desktop and updater	2026-11-16T02:47:43.4345962Z 54438 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\xref-Checkpoint.html
build	Build desktop and updater	2026-11-16T02:47:43.4845150Z 54485 INFO: checking PYZ
build	Build desktop and updater	2026-11-16T02:47:43.4845847Z 54485 INFO: Building PYZ because PYZ-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:43.4846622Z 54485 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz
build	Build desktop and updater	2026-11-16T02:47:44.2085536Z 55204 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz completed successfully.
build	Build desktop and updater	2026-11-16T02:47:44.2351653Z 55235 INFO: checking PKG
build	Build desktop and updater	2026-11-16T02:47:44.2352256Z 55235 INFO: Building PKG because PKG-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:44.2352905Z 55235 INFO: Building PKG (CArchive) Checkpoint.pkg
build	Build desktop and updater	2026-11-16T02:47:44.2531723Z 55251 INFO: Building PKG (CArchive) Checkpoint.pkg completed successfully.
build	Build desktop and updater	2026-11-16T02:47:44.2539536Z 55251 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\runw.exe
build	Build desktop and updater	2026-11-16T02:47:44.2540508Z 55251 INFO: checking EXE
build	Build desktop and updater	2026-11-16T02:47:44.2541052Z 55251 INFO: Building EXE because EXE-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:44.2541743Z 55251 INFO: Building EXE from EXE-00.toc
build	Build desktop and updater	2026-11-16T02:47:44.2543350Z 55251 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\Checkpoint.exe
build	Build desktop and updater	2026-11-16T02:47:44.2573998Z 55251 INFO: Copying icon to EXE
build	Build desktop and updater	2026-11-16T02:47:44.2591651Z 55251 INFO: Copying 0 resources to EXE
build	Build desktop and updater	2026-11-16T02:47:44.2592105Z 55251 INFO: Embedding manifest in EXE
build	Build desktop and updater	2026-11-16T02:47:44.2606886Z 55251 INFO: Appending PKG archive to EXE
build	Build desktop and updater	2026-11-16T02:47:44.2649437Z 55266 INFO: Fixing EXE headers
build	Build desktop and updater	2026-11-16T02:47:44.3417743Z 55344 INFO: Building EXE from EXE-00.toc completed successfully.
build	Build desktop and updater	2026-11-16T02:47:44.3513098Z 55344 INFO: checking COLLECT
build	Build desktop and updater	2026-11-16T02:47:44.3513824Z 55344 INFO: Building COLLECT because COLLECT-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:44.3516273Z 55344 INFO: Building COLLECT COLLECT-00.toc
build	Build desktop and updater	2026-11-16T02:47:44.9687562Z 55970 INFO: Building COLLECT COLLECT-00.toc completed successfully.
build	Build desktop and updater	2026-11-16T02:47:44.9877225Z 55985 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\dist
build	Build desktop and updater	2026-11-16T02:47:45.3155908Z 109 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
build	Build desktop and updater	2026-11-16T02:47:45.3160003Z 109 INFO: Python: 3.12.10
build	Build desktop and updater	2026-11-16T02:47:45.3367526Z 125 INFO: Platform: Windows-2022Server-10.0.20348-SP0
build	Build desktop and updater	2026-11-16T02:47:45.3368477Z 125 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Build desktop and updater	2026-11-16T02:47:45.3373382Z 125 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\CheckpointUpdater.spec
build	Build desktop and updater	2026-11-16T02:47:45.3407851Z 140 INFO: Module search paths (PYTHONPATH):
build	Build desktop and updater	2026-11-16T02:47:45.3408552Z ['D:\\a\\Checkpoint\\Checkpoint',
build	Build desktop and updater	2026-11-16T02:47:45.3409276Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
build	Build desktop and updater	2026-11-16T02:47:45.3410185Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
build	Build desktop and updater	2026-11-16T02:47:45.3410967Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
build	Build desktop and updater	2026-11-16T02:47:45.3431598Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
build	Build desktop and updater	2026-11-16T02:47:45.3432472Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
build	Build desktop and updater	2026-11-16T02:47:45.3433348Z  '__editable__.checkpoint_desktop-0.1.37.finder.__path_hook__',
build	Build desktop and updater	2026-11-16T02:47:45.3434028Z  'D:\\a\\Checkpoint\\Checkpoint']
build	Build desktop and updater	2026-11-16T02:47:45.5717318Z 360 INFO: checking Analysis
build	Build desktop and updater	2026-11-16T02:47:45.5718611Z 360 INFO: Building Analysis because Analysis-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:45.5719596Z 360 INFO: Looking for Python shared library...
build	Build desktop and updater	2026-11-16T02:47:45.5720730Z 360 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
build	Build desktop and updater	2026-11-16T02:47:45.5721739Z 360 INFO: Running Analysis Analysis-00.toc
build	Build desktop and updater	2026-11-16T02:47:45.5722339Z 360 INFO: Target bytecode optimization level: 0
build	Build desktop and updater	2026-11-16T02:47:45.5722978Z 360 INFO: Initializing module dependency graph...
build	Build desktop and updater	2026-11-16T02:47:45.5731818Z 360 INFO: Initializing module graph hook caches...
build	Build desktop and updater	2026-11-16T02:47:45.5886512Z 375 INFO: Analyzing modules for base_library.zip ...
build	Build desktop and updater	2026-11-16T02:47:46.4239396Z 1220 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:46.5105691Z 1299 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:47.8362320Z 2629 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:48.0664959Z 2864 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:49.5040878Z 4303 INFO: Caching module dependency graph...
build	Build desktop and updater	2026-11-16T02:47:49.5426602Z 4334 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_updater.py
build	Build desktop and updater	2026-11-16T02:47:49.5656760Z 4350 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:49.6363095Z 4428 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
build	Build desktop and updater	2026-11-16T02:47:49.6463787Z 4443 INFO: Processing module hooks (post-graph stage)...
build	Build desktop and updater	2026-11-16T02:47:49.6522987Z 4443 INFO: Performing binary vs. data reclassification (1 entries)
build	Build desktop and updater	2026-11-16T02:47:49.6533211Z 4443 INFO: Looking for ctypes DLLs
build	Build desktop and updater	2026-11-16T02:47:49.6597656Z 4459 INFO: Analyzing run-time hooks ...
build	Build desktop and updater	2026-11-16T02:47:49.6605334Z 4459 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
build	Build desktop and updater	2026-11-16T02:47:49.6649808Z 4459 INFO: Creating base_library.zip...
build	Build desktop and updater	2026-11-16T02:47:49.6846784Z 4474 INFO: Looking for dynamic libraries
build	Build desktop and updater	2026-11-16T02:47:49.7940057Z 4584 INFO: Extra DLL search directories (AddDllDirectory): []
build	Build desktop and updater	2026-11-16T02:47:49.7940626Z 4584 INFO: Extra DLL search directories (PATH): []
build	Build desktop and updater	2026-11-16T02:47:50.1080386Z 4897 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\warn-CheckpointUpdater.txt
build	Build desktop and updater	2026-11-16T02:47:50.1236627Z 4913 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\xref-CheckpointUpdater.html
build	Build desktop and updater	2026-11-16T02:47:50.1381165Z 4928 INFO: checking PYZ
build	Build desktop and updater	2026-11-16T02:47:50.1381848Z 4928 INFO: Building PYZ because PYZ-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:50.1383421Z 4928 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz
build	Build desktop and updater	2026-11-16T02:47:50.2907095Z 5085 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz completed successfully.
build	Build desktop and updater	2026-11-16T02:47:50.2948587Z 5085 INFO: checking PKG
build	Build desktop and updater	2026-11-16T02:47:50.2949798Z 5085 INFO: Building PKG because PKG-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:50.2951096Z 5085 INFO: Building PKG (CArchive) CheckpointUpdater.pkg
build	Build desktop and updater	2026-11-16T02:47:50.3076234Z 5100 INFO: Building PKG (CArchive) CheckpointUpdater.pkg completed successfully.
build	Build desktop and updater	2026-11-16T02:47:50.3083293Z 5100 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\run.exe
build	Build desktop and updater	2026-11-16T02:47:50.3084287Z 5100 INFO: checking EXE
build	Build desktop and updater	2026-11-16T02:47:50.3084839Z 5100 INFO: Building EXE because EXE-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:50.3085253Z 5100 INFO: Building EXE from EXE-00.toc
build	Build desktop and updater	2026-11-16T02:47:50.3087276Z 5100 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\CheckpointUpdater.exe
build	Build desktop and updater	2026-11-16T02:47:50.3107401Z 5100 INFO: Copying icon to EXE
build	Build desktop and updater	2026-11-16T02:47:50.3125803Z 5100 INFO: Copying 0 resources to EXE
build	Build desktop and updater	2026-11-16T02:47:50.3126264Z 5100 INFO: Embedding manifest in EXE
build	Build desktop and updater	2026-11-16T02:47:50.3140944Z 5100 INFO: Appending PKG archive to EXE
build	Build desktop and updater	2026-11-16T02:47:50.3149828Z 5100 INFO: Fixing EXE headers
build	Build desktop and updater	2026-11-16T02:47:50.3815239Z 5178 INFO: Building EXE from EXE-00.toc completed successfully.
build	Build desktop and updater	2026-11-16T02:47:50.3829278Z 5178 INFO: checking COLLECT
build	Build desktop and updater	2026-11-16T02:47:50.3830599Z 5178 INFO: Building COLLECT because COLLECT-00.toc is non existent
build	Build desktop and updater	2026-11-16T02:47:50.3832820Z 5178 INFO: Building COLLECT COLLECT-00.toc
build	Build desktop and updater	2026-11-16T02:47:50.4183195Z 5210 INFO: Building COLLECT COLLECT-00.toc completed successfully.
build	Build desktop and updater	2026-11-16T02:47:50.4198243Z 5210 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-dist
build	Package and validate extracted executable	﻿2026-11-16T02:47:50.5534342Z ##[group]Run python scripts/package_windows_release.py --test-report .ci-results/pytest.xml
build	Package and validate extracted executable	2026-11-16T02:47:50.5535107Z [36;1mpython scripts/package_windows_release.py --test-report .ci-results/pytest.xml[0m
build	Package and validate extracted executable	2026-11-16T02:47:50.5535690Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Validação do pacote Windows falhou.' }[0m
build	Package and validate extracted executable	2026-11-16T02:47:50.5575110Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Package and validate extracted executable	2026-11-16T02:47:50.5575617Z env:
build	Package and validate extracted executable	2026-11-16T02:47:50.5575809Z   QT_QPA_PLATFORM: offscreen
build	Package and validate extracted executable	2026-11-16T02:47:50.5576126Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Package and validate extracted executable	2026-11-16T02:47:50.5576599Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Package and validate extracted executable	2026-11-16T02:47:50.5577060Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Package and validate extracted executable	2026-11-16T02:47:50.5577463Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Package and validate extracted executable	2026-11-16T02:47:50.5577853Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Package and validate extracted executable	2026-11-16T02:47:50.5578207Z ##[endgroup]
build	Package and validate extracted executable	2026-11-16T02:48:04.4499128Z Checkpoint smoke: 6 pages OK; SQLite integrity=ok
build	Package and validate extracted executable	2026-11-16T02:48:05.6193675Z Cadastro smoke: salvar, auxiliar, renderiza��o e SQLite OK
build	Package and validate extracted executable	2026-11-16T02:48:11.6736203Z Checkpoint 0.1.37 � Windows x64
build	Package and validate extracted executable	2026-11-16T02:48:11.6736811Z Commit: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52
build	Package and validate extracted executable	2026-11-16T02:48:11.6737244Z Python: 3.12.10
build	Package and validate extracted executable	2026-11-16T02:48:11.6737672Z Testes: {'tests': 695, 'failures': 0, 'errors': 0, 'skipped': 0}
build	Package and validate extracted executable	2026-11-16T02:48:11.6738466Z Smoke do fonte: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
build	Package and validate extracted executable	2026-11-16T02:48:11.6739111Z Smoke do ZIP extra�do: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
build	Package and validate extracted executable	2026-11-16T02:48:11.6741186Z Auxiliar isolado do fonte e do ZIP extra�do: resposta e schema verificados.
build	Package and validate extracted executable	2026-11-16T02:48:11.6742347Z Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
build	Package and validate extracted executable	2026-11-16T02:48:11.6743436Z CheckpointUpdater.exe --check: sa�da 0.
build	Package and validate extracted executable	2026-11-16T02:48:11.6744086Z ZIP SHA-256: 54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a
build	Package and validate extracted executable	2026-11-16T02:48:11.6745058Z Steam autenticada e homologa��o Windows 10/11 pessoal n�o est�o cobertas.
build	Render Windows interface review	﻿2026-11-16T02:48:11.7929695Z ##[group]Run python scripts/render_ui_review.py work/ui-review
build	Render Windows interface review	2026-11-16T02:48:11.7930252Z [36;1mpython scripts/render_ui_review.py work/ui-review[0m
build	Render Windows interface review	2026-11-16T02:48:11.7930743Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Capturas da interface falharam.' }[0m
build	Render Windows interface review	2026-11-16T02:48:11.7931248Z [36;1mpython scripts/package_ui_review.py work/ui-review release-assets[0m
build	Render Windows interface review	2026-11-16T02:48:11.7931741Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Revisão visual incompleta.' }[0m
build	Render Windows interface review	2026-11-16T02:48:11.7971768Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Render Windows interface review	2026-11-16T02:48:11.7972125Z env:
build	Render Windows interface review	2026-11-16T02:48:11.7972305Z   QT_QPA_PLATFORM: offscreen
build	Render Windows interface review	2026-11-16T02:48:11.7972638Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Render Windows interface review	2026-11-16T02:48:11.7973112Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Render Windows interface review	2026-11-16T02:48:11.7973594Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Render Windows interface review	2026-11-16T02:48:11.7973997Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Render Windows interface review	2026-11-16T02:48:11.7974658Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Render Windows interface review	2026-11-16T02:48:11.7974978Z ##[endgroup]
build	Render Windows interface review	2026-11-16T02:48:13.7113703Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
build	Render Windows interface review	2026-11-16T02:48:22.5075159Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
build	Render Windows interface review	2026-11-16T02:48:22.7536031Z D:\a\Checkpoint\Checkpoint\work\ui-review
build	Render Windows interface review	2026-11-16T02:48:23.0571759Z Revis�o visual: 61 PNGs e �ndice HTML; bases e logs exclu�dos.
build	Upload verified release files	﻿2026-11-16T02:48:23.1879310Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
build	Upload verified release files	2026-11-16T02:48:23.1879842Z with:
build	Upload verified release files	2026-11-16T02:48:23.1880050Z   name: checkpoint-windows-release
build	Upload verified release files	2026-11-16T02:48:23.1880318Z   path: release-assets/*
build	Upload verified release files	2026-11-16T02:48:23.1880545Z   if-no-files-found: error
build	Upload verified release files	2026-11-16T02:48:23.1880767Z   retention-days: 14
build	Upload verified release files	2026-11-16T02:48:23.1880960Z   compression-level: 6
build	Upload verified release files	2026-11-16T02:48:23.1881155Z   overwrite: false
build	Upload verified release files	2026-11-16T02:48:23.1881347Z   include-hidden-files: false
build	Upload verified release files	2026-11-16T02:48:23.1881564Z env:
build	Upload verified release files	2026-11-16T02:48:23.1881732Z   QT_QPA_PLATFORM: offscreen
build	Upload verified release files	2026-11-16T02:48:23.1882777Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Upload verified release files	2026-11-16T02:48:23.1883233Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Upload verified release files	2026-11-16T02:48:23.1883699Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Upload verified release files	2026-11-16T02:48:23.1884108Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Upload verified release files	2026-11-16T02:48:23.1884501Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Upload verified release files	2026-11-16T02:48:23.1884844Z ##[endgroup]
build	Upload verified release files	2026-11-16T02:48:23.3708665Z (node:3644) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Upload verified release files	2026-11-16T02:48:23.3709466Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Upload verified release files	2026-11-16T02:48:23.3794383Z With the provided path, there will be 8 files uploaded
build	Upload verified release files	2026-11-16T02:48:23.3799447Z Artifact name is valid!
build	Upload verified release files	2026-11-16T02:48:23.3802069Z Root directory input is valid!
build	Upload verified release files	2026-11-16T02:48:23.6034757Z Beginning upload of artifact content to blob storage
build	Upload verified release files	2026-11-16T02:48:23.8840408Z (node:3644) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
build	Upload verified release files	2026-11-16T02:48:24.0889091Z Uploaded bytes 8388608
build	Upload verified release files	2026-11-16T02:48:24.2761626Z Uploaded bytes 16777216
build	Upload verified release files	2026-11-16T02:48:24.5830773Z Uploaded bytes 25165824
build	Upload verified release files	2026-11-16T02:48:24.8757594Z Uploaded bytes 33554432
build	Upload verified release files	2026-11-16T02:48:25.1073861Z Uploaded bytes 41943040
build	Upload verified release files	2026-11-16T02:48:25.4218774Z Uploaded bytes 50331648
build	Upload verified release files	2026-11-16T02:48:25.6555004Z Uploaded bytes 58720256
build	Upload verified release files	2026-11-16T02:48:25.9710710Z Uploaded bytes 67108864
build	Upload verified release files	2026-11-16T02:48:26.2833808Z Uploaded bytes 75497472
build	Upload verified release files	2026-11-16T02:48:26.4997691Z Uploaded bytes 83886080
build	Upload verified release files	2026-11-16T02:48:26.6289084Z Uploaded bytes 87984622
build	Upload verified release files	2026-11-16T02:48:26.6483167Z Finished uploading artifact content to blob storage!
build	Upload verified release files	2026-11-16T02:48:26.6488182Z SHA256 digest of uploaded artifact zip is 3715c13142957635785af4f35133defc3262a4c79cb7311a3d361b0b89980252
build	Upload verified release files	2026-11-16T02:48:26.6490977Z Finalizing artifact upload
build	Upload verified release files	2026-11-16T02:48:26.9758172Z Artifact checkpoint-windows-release.zip successfully finalized. Artifact ID 14193492682
build	Upload verified release files	2026-11-16T02:48:26.9759640Z Artifact checkpoint-windows-release has been successfully uploaded! Final size is 87984622 bytes. Artifact ID is 14193492682
build	Upload verified release files	2026-11-16T02:48:26.9772066Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592/artifacts/14193492682
build	Preserve Windows test report	﻿2026-11-16T02:48:27.0064732Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
build	Preserve Windows test report	2026-11-16T02:48:27.0065285Z with:
build	Preserve Windows test report	2026-11-16T02:48:27.0065548Z   name: checkpoint-windows-test-report
build	Preserve Windows test report	2026-11-16T02:48:27.0065887Z   path: .ci-results/pytest.xml
build	Preserve Windows test report	2026-11-16T02:48:27.0066213Z   if-no-files-found: ignore
build	Preserve Windows test report	2026-11-16T02:48:27.0066485Z   retention-days: 14
build	Preserve Windows test report	2026-11-16T02:48:27.0066733Z   compression-level: 6
build	Preserve Windows test report	2026-11-16T02:48:27.0066982Z   overwrite: false
build	Preserve Windows test report	2026-11-16T02:48:27.0067282Z   include-hidden-files: false
build	Preserve Windows test report	2026-11-16T02:48:27.0067551Z env:
build	Preserve Windows test report	2026-11-16T02:48:27.0067776Z   QT_QPA_PLATFORM: offscreen
build	Preserve Windows test report	2026-11-16T02:48:27.0068132Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:48:27.0068675Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Preserve Windows test report	2026-11-16T02:48:27.0069187Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:48:27.0069643Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:48:27.0070101Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Preserve Windows test report	2026-11-16T02:48:27.0070457Z ##[endgroup]
build	Preserve Windows test report	2026-11-16T02:48:27.2001531Z (node:5368) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Preserve Windows test report	2026-11-16T02:48:27.2017377Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Preserve Windows test report	2026-11-16T02:48:27.2061195Z With the provided path, there will be 1 file uploaded
build	Preserve Windows test report	2026-11-16T02:48:27.2069609Z Artifact name is valid!
build	Preserve Windows test report	2026-11-16T02:48:27.2072914Z Root directory input is valid!
build	Preserve Windows test report	2026-11-16T02:48:27.4390629Z Beginning upload of artifact content to blob storage
build	Preserve Windows test report	2026-11-16T02:48:27.4668912Z (node:5368) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
build	Preserve Windows test report	2026-11-16T02:48:27.5031286Z Uploaded bytes 14188
build	Preserve Windows test report	2026-11-16T02:48:27.5195838Z Finished uploading artifact content to blob storage!
build	Preserve Windows test report	2026-11-16T02:48:27.5197612Z SHA256 digest of uploaded artifact zip is fda533eea7f4328f489e5dbab9b64a7beea995cf29b7dced779bd3ed0dd8ebf5
build	Preserve Windows test report	2026-11-16T02:48:27.5200002Z Finalizing artifact upload
build	Preserve Windows test report	2026-11-16T02:48:27.8357381Z Artifact checkpoint-windows-test-report.zip successfully finalized. Artifact ID 14193672365
build	Preserve Windows test report	2026-11-16T02:48:27.8358476Z Artifact checkpoint-windows-test-report has been successfully uploaded! Final size is 14188 bytes. Artifact ID is 14193672365
build	Preserve Windows test report	2026-11-16T02:48:27.8367060Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43793047592/artifacts/14193672365
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	﻿2026-11-16T02:48:27.8644643Z Post job cleanup.
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:28.0036715Z (node:2104) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:28.0037582Z (Use `node --trace-deprecation ...` to show where the warning was created)
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:28.1259612Z [command]"C:\Program Files\Git\usr\bin\tar.exe" --posix -cf cache.tzst --exclude cache.tzst -P -C D:/a/Checkpoint/Checkpoint --files-from manifest.txt --force-local --use-compress-program "zstd -T0"
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:28.9654394Z (node:2104) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:29.9529118Z Sent 164500545 of 231609409 (71.0%), 156.7 MBs/sec
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:30.1016698Z Sent 231609409 of 231609409 (100.0%), 192.2 MBs/sec
build	Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065	2026-11-16T02:48:30.2305187Z Cache saved with the key: setup-python-Windows-x64-python-3.12.10-pip-eb71efc05b2754f3c8048b82aafb5b6c4b1d694285a4ae18da9e58d103e7bab6
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	﻿2026-11-16T02:48:30.2563330Z Post job cleanup.
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.4410841Z [command]"C:\Program Files\Git\bin\git.exe" version
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.4680640Z git version 2.56.1.windows.1
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.4741700Z Temporarily overriding HOME='D:\a\_temp\97ed0a98-fe96-4b12-ace3-d0933d7cc394' before making global git config changes
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.4742685Z Adding repository directory to the temporary git global config as a safe directory
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.4752915Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.5039966Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.5321880Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:30.9963639Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:31.0249294Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:31.5947664Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
build	Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262	2026-11-16T02:48:31.6228341Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
build	Complete job	﻿2026-11-16T02:48:32.0984014Z Evaluate and set job outputs
build	Complete job	2026-11-16T02:48:32.0991714Z Set output 'version'
build	Complete job	2026-11-16T02:48:32.0993754Z Cleaning up orphan processes
build	Complete job	2026-11-16T02:48:32.1521034Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@11d5960a326750d5838078e36cf38b85af677262, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

```

stderr integral:
```text

```

Código de saída: 0

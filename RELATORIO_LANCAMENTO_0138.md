# Lançamento 0.1.38 — publicado e verificado

## 0.1.38 publicada — correção de abertura

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.38

Tag/código: c4a7e1d221ba52a8580dd73ab884b1964e6ffd32. Windows release 43857996709 concluído com build e publicação aprovados. Windows/Python 3.12.10: 700 passed in 633.27s (0:10:33), zero falhas/erros/skips. Linux/Python 3.12.14: 700 passed in 483.81s (0:08:03), código funcional idêntico. Fonte e executável extraído passaram também por abertura normal com Qt windows, HWND visível/responsivo, captura, fechamento e SQLite, em Windows já elevado.

Dez arquivos publicados baixados e conferidos por tamanho/SHA-256 contra os digests do GitHub. CRC dos dois ZIPs válido. ZIP Windows: 84314842 bytes, SHA-256 15fef170b44dcf6073d50fed3f601f8b1cb265540c5e456113fe2befad0e3702. A 0.1.37/tag/arquivos foram preservados. Fonte do fix usa MSG.hWnd durante criação nativa, evitando chamar winId recursivamente; não muda dados, schema 4, cofre ou A4.

Upload local inicial recusado por autenticação em uploads.github.com; publicação concluída pelo workflow existente com identidade do próprio GitHub, sem alterar o workflow de release. A execução read-only anterior foi preservada como validação, e o publisher repetiu todos os gates. Documentação posterior não move a tag.

Consentimento UAC interativo e uso no PC do dono continuam sujeitos à confirmação; não confundir execução nativa já elevada no runner com consentimento automatizado. As demais limitações anteriores de fontes de preço, A4 e fechamento somente da ROM permanecem. Registros seguintes descrevem a preparação e as falhas de infraestrutura.

O dono autorizou explicitamente publicar a correção após revisar os resultados e receber o pacote validado. A 0.1.37/tag/arquivos permanecem preservados. Candidato funcional validado: ff136584974b55989c10598612235717508ec25a; Windows UI validation 43799707113, 700 testes Windows, build, smokes e abertura normal do fonte e executável extraído aprovados; Linux 700 testes.

Primeira tentativa de publicação pela CLI: GitHub API autenticada, mas upload para uploads.github.com retornou HTTP 401 Bad credentials. A verificação posterior não encontrou release/tag 0.1.38 nem rascunho remanescente. Nenhum pacote parcial é apresentado como publicação. Não foram registrados tokens ou links assinados.

Alternativa: workflow Windows release existente, sem alteração no seu código, usando GITHUB_TOKEN do próprio GitHub. Notas públicas atualizadas para a 0.1.38 após autorização; novo commit só documental/notas, sem mudança funcional desde ff13658. Workflow repetirá testes/build/smokes/abertura nativa e publicará somente após aprovação. Tags e releases anteriores não serão movidas ou sobrescritas.

Resultados e verificação final serão acrescentados após conclusão. A validação de abertura é de Windows já elevado no runner; consentimento UAC real e uso no PC do dono não são homologados por isso.

## Execução de publicação

Windows release 43857996709: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43857996709

SHA c4a7e1d221ba52a8580dd73ab884b1964e6ffd32, branch fix/0.1.38-abertura. Publicação manual autorizada pelo dono; workflow de publicação preservado. Aplicativo/scripts/testes idênticos ao candidato ff13658 anteriormente aprovado. Autenticação do upload será feita pelo GITHUB_TOKEN do próprio job, sem copiar credenciais para este ambiente.

## Log Windows integral

Run 43857996709, job 133267155625. API de logs do GitHub, resposta bem-sucedida.

```text
﻿2026-11-16T11:28:07.4920632Z Current runner version: '2.338.2'
2026-11-16T11:28:07.4955413Z ##[group]Runner Image Provisioner
2026-11-16T11:28:07.4956580Z Hosted Compute Agent
2026-11-16T11:28:07.4957425Z Version: 20261103.629
2026-11-16T11:28:07.4958460Z Commit: 15dbd9ccb5dbf34fae002b6ed1a2670f52df37bc
2026-11-16T11:28:07.4959650Z Build Date: 2026-11-03T17:26:59Z
2026-11-16T11:28:07.4960816Z Worker ID: {34756d17-78a4-45fc-9257-86729beb0334}
2026-11-16T11:28:07.4961965Z Region: centralus
2026-11-16T11:28:07.4962786Z Cloud: Azure
2026-11-16T11:28:07.4963707Z ##[endgroup]
2026-11-16T11:28:07.4965695Z ##[group]Operating System
2026-11-16T11:28:07.4966729Z Microsoft Windows Server 2022
2026-11-16T11:28:07.4967687Z 10.0.20348
2026-11-16T11:28:07.4968413Z Datacenter
2026-11-16T11:28:07.4969175Z ##[endgroup]
2026-11-16T11:28:07.4969989Z ##[group]Runner Image
2026-11-16T11:28:07.4970941Z Image: windows-2022
2026-11-16T11:28:07.4971801Z Version: 20261112.366.7
2026-11-16T11:28:07.4974194Z Included Software: https://github.com/actions/runner-images/blob/win22/20261112.366/images/windows/Windows2022-Readme.md
2026-11-16T11:28:07.4976914Z Image Release: https://github.com/actions/runner-images/releases/tag/win22%2F20261112.366
2026-11-16T11:28:07.4978484Z ##[endgroup]
2026-11-16T11:28:07.4980177Z ##[group]GITHUB_TOKEN Permissions
2026-11-16T11:28:07.4982635Z Contents: read
2026-11-16T11:28:07.4983502Z Metadata: read
2026-11-16T11:28:07.4984290Z ##[endgroup]
2026-11-16T11:28:07.4986839Z Secret source: Actions
2026-11-16T11:28:07.4988194Z Cache mode: write
2026-11-16T11:28:07.4989248Z Prepare workflow directory
2026-11-16T11:28:07.5430981Z Prepare all required actions
2026-11-16T11:28:07.5478522Z Getting action download info
2026-11-16T11:28:07.8324865Z Download action repository 'actions/checkout@11d5960a326750d5838078e36cf38b85af677262' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-11-16T11:28:07.9559202Z Download action repository 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-11-16T11:28:08.1064174Z Download action repository 'actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-11-16T11:28:08.4275997Z Complete job name: build
2026-11-16T11:28:08.5946190Z ##[group]Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262
2026-11-16T11:28:08.5947465Z with:
2026-11-16T11:28:08.5947912Z   persist-credentials: false
2026-11-16T11:28:08.5948433Z   fetch-depth: 0
2026-11-16T11:28:08.5948931Z   repository: pedroalexcarneiro/Checkpoint
2026-11-16T11:28:08.5953155Z   token: ***
2026-11-16T11:28:08.5953593Z   ssh-strict: true
2026-11-16T11:28:08.5954017Z   ssh-user: git
2026-11-16T11:28:08.5954424Z   clean: true
2026-11-16T11:28:08.5954853Z   sparse-checkout-cone-mode: true
2026-11-16T11:28:08.5955380Z   fetch-tags: false
2026-11-16T11:28:08.5955822Z   show-progress: true
2026-11-16T11:28:08.5956255Z   lfs: false
2026-11-16T11:28:08.5956664Z   submodules: false
2026-11-16T11:28:08.5957140Z   set-safe-directory: true
2026-11-16T11:28:08.5957635Z   allow-unsafe-pr-checkout: false
2026-11-16T11:28:08.5958355Z env:
2026-11-16T11:28:08.5958776Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:28:08.5959262Z ##[endgroup]
2026-11-16T11:28:08.7386085Z Syncing repository: pedroalexcarneiro/Checkpoint
2026-11-16T11:28:08.7387937Z ##[group]Getting Git version info
2026-11-16T11:28:08.7388619Z Working directory is 'D:\a\Checkpoint\Checkpoint'
2026-11-16T11:28:08.8303728Z [command]"C:\Program Files\Git\bin\git.exe" version
2026-11-16T11:28:09.1712737Z git version 2.56.1.windows.1
2026-11-16T11:28:09.1755911Z ##[endgroup]
2026-11-16T11:28:09.1773624Z Temporarily overriding HOME='D:\a\_temp\25674f09-03d1-401d-adc7-58b201a03813' before making global git config changes
2026-11-16T11:28:09.1775546Z Adding repository directory to the temporary git global config as a safe directory
2026-11-16T11:28:09.1784421Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
2026-11-16T11:28:09.2385808Z Deleting the contents of 'D:\a\Checkpoint\Checkpoint'
2026-11-16T11:28:09.2390982Z ##[group]Initializing the repository
2026-11-16T11:28:09.2399573Z [command]"C:\Program Files\Git\bin\git.exe" init D:\a\Checkpoint\Checkpoint
2026-11-16T11:28:09.3216096Z Initialized empty Git repository in D:/a/Checkpoint/Checkpoint/.git/
2026-11-16T11:28:09.3247511Z [command]"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/pedroalexcarneiro/Checkpoint
2026-11-16T11:28:09.3781254Z ##[endgroup]
2026-11-16T11:28:09.3782666Z ##[group]Disabling automatic garbage collection
2026-11-16T11:28:09.3788563Z [command]"C:\Program Files\Git\bin\git.exe" config --local gc.auto 0
2026-11-16T11:28:09.4060023Z ##[endgroup]
2026-11-16T11:28:09.4061773Z ##[group]Setting up auth
2026-11-16T11:28:09.4071731Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T11:28:09.4350520Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T11:28:10.7647251Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T11:28:10.7925573Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T11:28:11.2456554Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T11:28:11.2734306Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T11:28:11.7157823Z [command]"C:\Program Files\Git\bin\git.exe" config --local http.https://github.com/.extraheader "AUTHORIZATION: basic ***"
2026-11-16T11:28:11.7457344Z ##[endgroup]
2026-11-16T11:28:11.7457864Z ##[group]Fetching the repository
2026-11-16T11:28:11.7479894Z [command]"C:\Program Files\Git\bin\git.exe" -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
2026-11-16T11:28:13.4666817Z From https://github.com/pedroalexcarneiro/Checkpoint
2026-11-16T11:28:13.4667988Z  * [new branch]      codex/design-fidelity-pt-br -> origin/codex/design-fidelity-pt-br
2026-11-16T11:28:13.4668917Z  * [new branch]      codex/steam-library-import -> origin/codex/steam-library-import
2026-11-16T11:28:13.4669768Z  * [new branch]      fix/0.1.29          -> origin/fix/0.1.29
2026-11-16T11:28:13.4670468Z  * [new branch]      fix/0.1.30          -> origin/fix/0.1.30
2026-11-16T11:28:13.4671147Z  * [new branch]      fix/0.1.32-visual   -> origin/fix/0.1.32-visual
2026-11-16T11:28:13.4671594Z  * [new branch]      fix/0.1.33-drive    -> origin/fix/0.1.33-drive
2026-11-16T11:28:13.4672070Z  * [new branch]      fix/0.1.34-bugs     -> origin/fix/0.1.34-bugs
2026-11-16T11:28:13.4672444Z  * [new branch]      fix/0.1.35-ajustes  -> origin/fix/0.1.35-ajustes
2026-11-16T11:28:13.4672859Z  * [new branch]      fix/0.1.36-ajustes  -> origin/fix/0.1.36-ajustes
2026-11-16T11:28:13.4673369Z  * [new branch]      fix/0.1.37-ajustes  -> origin/fix/0.1.37-ajustes
2026-11-16T11:28:13.4674004Z  * [new branch]      fix/0.1.38-abertura -> origin/fix/0.1.38-abertura
2026-11-16T11:28:13.4674781Z  * [new branch]      fix/rename-redesign-0.1.28 -> origin/fix/rename-redesign-0.1.28
2026-11-16T11:28:13.4675726Z  * [new branch]      main                -> origin/main
2026-11-16T11:28:13.4676399Z  * [new tag]         v0.1.10             -> v0.1.10
2026-11-16T11:28:13.4676912Z  * [new tag]         v0.1.11             -> v0.1.11
2026-11-16T11:28:13.4677384Z  * [new tag]         v0.1.12             -> v0.1.12
2026-11-16T11:28:13.4677841Z  * [new tag]         v0.1.13             -> v0.1.13
2026-11-16T11:28:13.4679425Z  * [new tag]         v0.1.14             -> v0.1.14
2026-11-16T11:28:13.4679916Z  * [new tag]         v0.1.15             -> v0.1.15
2026-11-16T11:28:13.4680392Z  * [new tag]         v0.1.16             -> v0.1.16
2026-11-16T11:28:13.4680946Z  * [new tag]         v0.1.17             -> v0.1.17
2026-11-16T11:28:13.4681448Z  * [new tag]         v0.1.18             -> v0.1.18
2026-11-16T11:28:13.4681923Z  * [new tag]         v0.1.19             -> v0.1.19
2026-11-16T11:28:13.4682378Z  * [new tag]         v0.1.2              -> v0.1.2
2026-11-16T11:28:13.4682848Z  * [new tag]         v0.1.20             -> v0.1.20
2026-11-16T11:28:13.4683307Z  * [new tag]         v0.1.21             -> v0.1.21
2026-11-16T11:28:13.4683756Z  * [new tag]         v0.1.22             -> v0.1.22
2026-11-16T11:28:13.4684231Z  * [new tag]         v0.1.23             -> v0.1.23
2026-11-16T11:28:13.4684693Z  * [new tag]         v0.1.24             -> v0.1.24
2026-11-16T11:28:13.4685158Z  * [new tag]         v0.1.25             -> v0.1.25
2026-11-16T11:28:13.4685617Z  * [new tag]         v0.1.26             -> v0.1.26
2026-11-16T11:28:13.4686112Z  * [new tag]         v0.1.27             -> v0.1.27
2026-11-16T11:28:13.4686589Z  * [new tag]         v0.1.28             -> v0.1.28
2026-11-16T11:28:13.4687088Z  * [new tag]         v0.1.29             -> v0.1.29
2026-11-16T11:28:13.4687553Z  * [new tag]         v0.1.3              -> v0.1.3
2026-11-16T11:28:13.4688025Z  * [new tag]         v0.1.30             -> v0.1.30
2026-11-16T11:28:13.4688538Z  * [new tag]         v0.1.32             -> v0.1.32
2026-11-16T11:28:13.4689095Z  * [new tag]         v0.1.33             -> v0.1.33
2026-11-16T11:28:13.4689880Z  * [new tag]         v0.1.34             -> v0.1.34
2026-11-16T11:28:13.4690397Z  * [new tag]         v0.1.35             -> v0.1.35
2026-11-16T11:28:13.4690840Z  * [new tag]         v0.1.36             -> v0.1.36
2026-11-16T11:28:13.4691299Z  * [new tag]         v0.1.37             -> v0.1.37
2026-11-16T11:28:13.4691801Z  * [new tag]         v0.1.4              -> v0.1.4
2026-11-16T11:28:13.4774170Z  * [new tag]         v0.1.5              -> v0.1.5
2026-11-16T11:28:13.4775865Z  * [new tag]         v0.1.6              -> v0.1.6
2026-11-16T11:28:13.4776461Z  * [new tag]         v0.1.7              -> v0.1.7
2026-11-16T11:28:13.4776966Z  * [new tag]         v0.1.8              -> v0.1.8
2026-11-16T11:28:13.4777472Z  * [new tag]         v0.1.9              -> v0.1.9
2026-11-16T11:28:13.4778961Z [command]"C:\Program Files\Git\bin\git.exe" branch --list --remote origin/fix/0.1.38-abertura
2026-11-16T11:28:13.5129814Z   origin/fix/0.1.38-abertura
2026-11-16T11:28:13.5164702Z [command]"C:\Program Files\Git\bin\git.exe" rev-parse refs/remotes/origin/fix/0.1.38-abertura
2026-11-16T11:28:13.5433340Z c4a7e1d221ba52a8580dd73ab884b1964e6ffd32
2026-11-16T11:28:13.5456249Z ##[endgroup]
2026-11-16T11:28:13.5456792Z ##[group]Determining the checkout info
2026-11-16T11:28:13.5457549Z ##[endgroup]
2026-11-16T11:28:13.5466081Z [command]"C:\Program Files\Git\bin\git.exe" sparse-checkout disable
2026-11-16T11:28:13.5920354Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all extensions.worktreeConfig
2026-11-16T11:28:13.6194606Z ##[group]Checking out the ref
2026-11-16T11:28:13.6202482Z [command]"C:\Program Files\Git\bin\git.exe" checkout --progress --force -B fix/0.1.38-abertura refs/remotes/origin/fix/0.1.38-abertura
2026-11-16T11:28:13.8733459Z Switched to a new branch 'fix/0.1.38-abertura'
2026-11-16T11:28:13.8756182Z branch 'fix/0.1.38-abertura' set up to track 'origin/fix/0.1.38-abertura'.
2026-11-16T11:28:13.8799411Z ##[endgroup]
2026-11-16T11:28:13.9200315Z [command]"C:\Program Files\Git\bin\git.exe" log -1 --format=%H
2026-11-16T11:28:13.9459801Z c4a7e1d221ba52a8580dd73ab884b1964e6ffd32
2026-11-16T11:28:13.9488153Z ##[group]Removing auth
2026-11-16T11:28:13.9495589Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T11:28:13.9769629Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T11:28:14.4083884Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T11:28:14.4346483Z http.https://github.com/.extraheader
2026-11-16T11:28:14.4376833Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
2026-11-16T11:28:14.4708477Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T11:28:14.9559830Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T11:28:14.9839085Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T11:28:15.4349406Z ##[endgroup]
2026-11-16T11:28:15.4715507Z ##[group]Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
2026-11-16T11:28:15.4715951Z with:
2026-11-16T11:28:15.4716135Z   python-version: 3.12
2026-11-16T11:28:15.4716337Z   architecture: x64
2026-11-16T11:28:15.4716525Z   cache: pip
2026-11-16T11:28:15.4716748Z   cache-dependency-path: requirements-tested.txt
2026-11-16T11:28:15.4717036Z   check-latest: false
2026-11-16T11:28:15.4719522Z   token: ***
2026-11-16T11:28:15.4719720Z   update-environment: true
2026-11-16T11:28:15.4719945Z   allow-prereleases: false
2026-11-16T11:28:15.4720153Z   freethreaded: false
2026-11-16T11:28:15.4720333Z env:
2026-11-16T11:28:15.4720500Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:28:15.4720705Z ##[endgroup]
2026-11-16T11:28:15.6209558Z ##[group]Installed versions
2026-11-16T11:28:15.6411697Z (node:6376) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T11:28:15.6412999Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T11:28:15.6413777Z Successfully set up CPython (3.12.10)
2026-11-16T11:28:15.6414494Z ##[endgroup]
2026-11-16T11:28:18.2719851Z Cache hit for: setup-python-Windows-x64-python-3.12.10-pip-eb71efc05b2754f3c8048b82aafb5b6c4b1d694285a4ae18da9e58d103e7bab6
2026-11-16T11:28:18.2835172Z (node:6376) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T11:28:19.4111103Z Received 117440512 of 231609841 (50.7%), 112.0 MBs/sec
2026-11-16T11:28:20.1698677Z Received 231609841 of 231609841 (100.0%), 125.6 MBs/sec
2026-11-16T11:28:20.1703122Z Cache Size: ~221 MB (231609841 B)
2026-11-16T11:28:20.1776907Z [command]"C:\Program Files\Git\usr\bin\tar.exe" -xf D:/a/_temp/c21113d0-e21c-4e48-8c85-61d203ec2cf0/cache.tzst -P -C D:/a/Checkpoint/Checkpoint --force-local --use-compress-program "zstd -d"
2026-11-16T11:28:21.2406176Z Cache restored successfully
2026-11-16T11:28:21.2513240Z Cache restored from key: setup-python-Windows-x64-python-3.12.10-pip-eb71efc05b2754f3c8048b82aafb5b6c4b1d694285a4ae18da9e58d103e7bab6
2026-11-16T11:28:21.2827367Z ##[group]Run $version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'
2026-11-16T11:28:21.2829004Z [36;1m$version = python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; assert tomllib.loads(Path("pyproject.toml").read_text())["project"]["version"] == __version__; print(__version__)'[0m
2026-11-16T11:28:21.2830177Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao ler a versão.' }[0m
2026-11-16T11:28:21.2830648Z [36;1mif ($version -notmatch '^\d+\.\d+\.\d+$') { throw 'Versão inválida.' }[0m
2026-11-16T11:28:21.2831078Z [36;1m"version=$version" >> $env:GITHUB_OUTPUT[0m
2026-11-16T11:28:21.2935770Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:28:21.2936121Z env:
2026-11-16T11:28:21.2936307Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:28:21.2936669Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.2937142Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:28:21.2937596Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.2938007Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.2938433Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.2938743Z ##[endgroup]
2026-11-16T11:28:21.9547117Z ##[group]Run python -m pip install -r requirements-tested.txt
2026-11-16T11:28:21.9547656Z [36;1mpython -m pip install -r requirements-tested.txt[0m
2026-11-16T11:28:21.9548127Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependências.' }[0m
2026-11-16T11:28:21.9548615Z [36;1mpython -m pip install --no-deps --no-build-isolation -e .[0m
2026-11-16T11:28:21.9549056Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar o projeto.' }[0m
2026-11-16T11:28:21.9549418Z [36;1mpython -m pip check[0m
2026-11-16T11:28:21.9549763Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Dependências inconsistentes.' }[0m
2026-11-16T11:28:21.9588163Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:28:21.9588509Z env:
2026-11-16T11:28:21.9588700Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:28:21.9589018Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.9589528Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:28:21.9590014Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.9590410Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.9590812Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:28:21.9591130Z ##[endgroup]
2026-11-16T11:28:24.7142309Z Collecting altgraph==0.17.5 (from -r requirements-tested.txt (line 1))
2026-11-16T11:28:24.7163818Z   Using cached altgraph-0.17.5-py2.py3-none-any.whl.metadata (7.5 kB)
2026-11-16T11:28:24.7455811Z Collecting certifi==2026.10.23 (from -r requirements-tested.txt (line 2))
2026-11-16T11:28:24.7476160Z   Using cached certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
2026-11-16T11:28:24.8736565Z Collecting cffi==2.1.1 (from -r requirements-tested.txt (line 3))
2026-11-16T11:28:24.8758217Z   Using cached cffi-2.1.1-cp312-cp312-win_amd64.whl.metadata (2.6 kB)
2026-11-16T11:28:25.0151534Z Collecting charset-normalizer==3.5.2 (from -r requirements-tested.txt (line 4))
2026-11-16T11:28:25.0174140Z   Using cached charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
2026-11-16T11:28:25.0237389Z Requirement already satisfied: colorama==0.4.6 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 5)) (0.4.6)
2026-11-16T11:28:25.2076986Z Collecting cryptography==50.0.2 (from -r requirements-tested.txt (line 6))
2026-11-16T11:28:25.2099578Z   Using cached cryptography-50.0.2-cp311-abi3-win_amd64.whl.metadata (4.4 kB)
2026-11-16T11:28:25.2494397Z Collecting google-api-core==2.44.0 (from -r requirements-tested.txt (line 7))
2026-11-16T11:28:25.2514173Z   Using cached google_api_core-2.44.0-py3-none-any.whl.metadata (3.2 kB)
2026-11-16T11:28:25.2980907Z Collecting google-api-python-client==2.202.0 (from -r requirements-tested.txt (line 8))
2026-11-16T11:28:25.3000229Z   Using cached google_api_python_client-2.202.0-py3-none-any.whl.metadata (6.9 kB)
2026-11-16T11:28:25.3233898Z Collecting google-auth-httplib2==0.4.4 (from -r requirements-tested.txt (line 9))
2026-11-16T11:28:25.3257185Z   Using cached google_auth_httplib2-0.4.4-py3-none-any.whl.metadata (3.0 kB)
2026-11-16T11:28:25.3549179Z Collecting google-auth-oauthlib==1.5.0 (from -r requirements-tested.txt (line 10))
2026-11-16T11:28:25.3572296Z   Using cached google_auth_oauthlib-1.5.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T11:28:25.3960176Z Collecting google-auth==2.62.2 (from -r requirements-tested.txt (line 11))
2026-11-16T11:28:25.3992608Z   Using cached google_auth-2.62.2-py3-none-any.whl.metadata (6.0 kB)
2026-11-16T11:28:25.4366897Z Collecting googleapis-common-protos==1.76.0 (from -r requirements-tested.txt (line 12))
2026-11-16T11:28:25.4386008Z   Using cached googleapis_common_protos-1.76.0-py3-none-any.whl.metadata (8.5 kB)
2026-11-16T11:28:25.4660679Z Collecting httplib2==0.32.1 (from -r requirements-tested.txt (line 13))
2026-11-16T11:28:25.4685763Z   Using cached httplib2-0.32.1-py3-none-any.whl.metadata (2.2 kB)
2026-11-16T11:28:25.4938582Z Collecting idna==3.20 (from -r requirements-tested.txt (line 14))
2026-11-16T11:28:25.4959159Z   Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
2026-11-16T11:28:25.5205306Z Collecting iniconfig==2.3.1 (from -r requirements-tested.txt (line 15))
2026-11-16T11:28:25.5224878Z   Using cached iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
2026-11-16T11:28:25.5476384Z Collecting jaraco-classes==3.4.0 (from -r requirements-tested.txt (line 16))
2026-11-16T11:28:25.5496093Z   Using cached jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T11:28:25.5743488Z Collecting jaraco-context==6.1.2 (from -r requirements-tested.txt (line 17))
2026-11-16T11:28:25.5765330Z   Using cached jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
2026-11-16T11:28:25.6042931Z Collecting jaraco-functools==4.6.0 (from -r requirements-tested.txt (line 18))
2026-11-16T11:28:25.6065397Z   Using cached jaraco_functools-4.6.0-py3-none-any.whl.metadata (2.9 kB)
2026-11-16T11:28:25.6412590Z Collecting keyring==25.7.0 (from -r requirements-tested.txt (line 19))
2026-11-16T11:28:25.6431548Z   Using cached keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
2026-11-16T11:28:25.6800669Z Collecting more-itertools==11.2.1 (from -r requirements-tested.txt (line 20))
2026-11-16T11:28:25.6821872Z   Using cached more_itertools-11.2.1-py3-none-any.whl.metadata (42 kB)
2026-11-16T11:28:25.7130023Z Collecting oauthlib==4.0.1 (from -r requirements-tested.txt (line 21))
2026-11-16T11:28:25.7166959Z   Using cached oauthlib-4.0.1-py3-none-any.whl.metadata (8.6 kB)
2026-11-16T11:28:25.7474916Z Collecting opentelemetry-api==1.45.2 (from -r requirements-tested.txt (line 22))
2026-11-16T11:28:25.7496500Z   Using cached opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB)
2026-11-16T11:28:25.7527008Z Requirement already satisfied: packaging==26.3 in C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages (from -r requirements-tested.txt (line 23)) (26.3)
2026-11-16T11:28:25.7748184Z Collecting pefile==2024.8.26 (from -r requirements-tested.txt (line 24))
2026-11-16T11:28:25.7767236Z   Using cached pefile-2024.8.26-py3-none-any.whl.metadata (1.4 kB)
2026-11-16T11:28:25.9270487Z Collecting pluggy==1.7.0 (from -r requirements-tested.txt (line 25))
2026-11-16T11:28:25.9289868Z   Using cached pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
2026-11-16T11:28:25.9562148Z Collecting proto-plus==1.29.0 (from -r requirements-tested.txt (line 26))
2026-11-16T11:28:25.9581195Z   Using cached proto_plus-1.29.0-py3-none-any.whl.metadata (2.2 kB)
2026-11-16T11:28:26.1209911Z Collecting protobuf==7.36.2 (from -r requirements-tested.txt (line 27))
2026-11-16T11:28:26.1233472Z   Using cached protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
2026-11-16T11:28:26.1676675Z Collecting pyasn1-modules==0.4.2 (from -r requirements-tested.txt (line 28))
2026-11-16T11:28:26.1698449Z   Using cached pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
2026-11-16T11:28:26.2043801Z Collecting pyasn1==0.6.5 (from -r requirements-tested.txt (line 29))
2026-11-16T11:28:26.2065638Z   Using cached pyasn1-0.6.5-py3-none-any.whl.metadata (8.4 kB)
2026-11-16T11:28:26.2297900Z Collecting pycparser==3.12 (from -r requirements-tested.txt (line 30))
2026-11-16T11:28:26.2318581Z   Using cached pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
2026-11-16T11:28:26.2627328Z Collecting pygments==2.21.0 (from -r requirements-tested.txt (line 31))
2026-11-16T11:28:26.2647072Z   Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
2026-11-16T11:28:26.2938048Z Collecting pyinstaller-hooks-contrib==2026.10 (from -r requirements-tested.txt (line 32))
2026-11-16T11:28:26.2959640Z   Using cached pyinstaller_hooks_contrib-2026.10-py3-none-any.whl.metadata (16 kB)
2026-11-16T11:28:26.3516500Z Collecting pyinstaller==6.22.3 (from -r requirements-tested.txt (line 33))
2026-11-16T11:28:26.3536667Z   Using cached pyinstaller-6.22.3-py3-none-win_amd64.whl.metadata (8.5 kB)
2026-11-16T11:28:26.3865029Z Collecting pyparsing==3.3.3 (from -r requirements-tested.txt (line 34))
2026-11-16T11:28:26.3887196Z   Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
2026-11-16T11:28:26.4237130Z Collecting pyside6-addons==6.8.3 (from -r requirements-tested.txt (line 35))
2026-11-16T11:28:26.4305775Z   Using cached PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.4 kB)
2026-11-16T11:28:26.4734334Z Collecting pyside6-essentials==6.8.3 (from -r requirements-tested.txt (line 36))
2026-11-16T11:28:26.4791552Z   Using cached PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl.metadata (4.1 kB)
2026-11-16T11:28:26.5182365Z Collecting pyside6==6.8.3 (from -r requirements-tested.txt (line 37))
2026-11-16T11:28:26.5201425Z   Using cached PySide6-6.8.3-cp39-abi3-win_amd64.whl.metadata (5.7 kB)
2026-11-16T11:28:26.5631926Z Collecting pytest==9.2.0 (from -r requirements-tested.txt (line 38))
2026-11-16T11:28:26.5690236Z   Using cached pytest-9.2.0-py3-none-any.whl.metadata (7.9 kB)
2026-11-16T11:28:26.6006724Z Collecting pywin32-ctypes==0.2.3 (from -r requirements-tested.txt (line 39))
2026-11-16T11:28:26.6025657Z   Using cached pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
2026-11-16T11:28:26.6297533Z Collecting requests-oauthlib==2.0.0 (from -r requirements-tested.txt (line 40))
2026-11-16T11:28:26.6316439Z   Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
2026-11-16T11:28:26.6651945Z Collecting requests==2.34.2 (from -r requirements-tested.txt (line 41))
2026-11-16T11:28:26.6683099Z   Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-11-16T11:28:26.7544884Z Collecting setuptools==84.2.1 (from -r requirements-tested.txt (line 42))
2026-11-16T11:28:26.7577181Z   Using cached setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
2026-11-16T11:28:26.7950432Z Collecting shiboken6==6.8.3 (from -r requirements-tested.txt (line 43))
2026-11-16T11:28:26.7972645Z   Using cached shiboken6-6.8.3-cp39-abi3-win_amd64.whl.metadata (2.8 kB)
2026-11-16T11:28:26.8324480Z Collecting typing-extensions==4.16.0 (from -r requirements-tested.txt (line 44))
2026-11-16T11:28:26.8343820Z   Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-11-16T11:28:26.8600398Z Collecting tzdata==2026.6 (from -r requirements-tested.txt (line 45))
2026-11-16T11:28:26.8621912Z   Using cached tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
2026-11-16T11:28:26.8863660Z Collecting uritemplate==4.2.0 (from -r requirements-tested.txt (line 46))
2026-11-16T11:28:26.8885159Z   Using cached uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)
2026-11-16T11:28:26.9227070Z Collecting urllib3==2.8.0 (from -r requirements-tested.txt (line 47))
2026-11-16T11:28:26.9246084Z   Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
2026-11-16T11:28:26.9986703Z Using cached altgraph-0.17.5-py2.py3-none-any.whl (21 kB)
2026-11-16T11:28:27.0007278Z Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
2026-11-16T11:28:27.0037314Z Using cached cffi-2.1.1-cp312-cp312-win_amd64.whl (185 kB)
2026-11-16T11:28:27.0054797Z Using cached charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
2026-11-16T11:28:27.0074429Z Using cached cryptography-50.0.2-cp311-abi3-win_amd64.whl (3.8 MB)
2026-11-16T11:28:27.0107178Z Using cached google_api_core-2.44.0-py3-none-any.whl (225 kB)
2026-11-16T11:28:27.0127286Z Using cached google_auth-2.62.2-py3-none-any.whl (270 kB)
2026-11-16T11:28:27.0147786Z Using cached googleapis_common_protos-1.76.0-py3-none-any.whl (307 kB)
2026-11-16T11:28:27.0169388Z Using cached opentelemetry_api-1.45.2-py3-none-any.whl (60 kB)
2026-11-16T11:28:27.0186811Z Using cached proto_plus-1.29.0-py3-none-any.whl (50 kB)
2026-11-16T11:28:27.0204085Z Using cached protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
2026-11-16T11:28:27.0223407Z Using cached requests-2.34.2-py3-none-any.whl (73 kB)
2026-11-16T11:28:27.0243050Z Using cached idna-3.20-py3-none-any.whl (69 kB)
2026-11-16T11:28:27.0260968Z Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
2026-11-16T11:28:27.0291444Z Using cached google_api_python_client-2.202.0-py3-none-any.whl (17.1 MB)
2026-11-16T11:28:27.0374522Z Using cached google_auth_httplib2-0.4.4-py3-none-any.whl (9.5 kB)
2026-11-16T11:28:27.0394275Z Using cached httplib2-0.32.1-py3-none-any.whl (92 kB)
2026-11-16T11:28:27.0411303Z Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB)
2026-11-16T11:28:27.0428749Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2026-11-16T11:28:27.0445796Z Using cached google_auth_oauthlib-1.5.0-py3-none-any.whl (20 kB)
2026-11-16T11:28:27.0465396Z Using cached iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
2026-11-16T11:28:27.0482403Z Using cached jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
2026-11-16T11:28:27.0499412Z Using cached jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
2026-11-16T11:28:27.0530633Z Using cached jaraco_functools-4.6.0-py3-none-any.whl (11 kB)
2026-11-16T11:28:27.0547848Z Using cached keyring-25.7.0-py3-none-any.whl (39 kB)
2026-11-16T11:28:27.0609821Z Using cached more_itertools-11.2.1-py3-none-any.whl (74 kB)
2026-11-16T11:28:27.0628432Z Using cached oauthlib-4.0.1-py3-none-any.whl (161 kB)
2026-11-16T11:28:27.0646158Z Using cached pefile-2024.8.26-py3-none-any.whl (74 kB)
2026-11-16T11:28:27.0665974Z Using cached pluggy-1.7.0-py3-none-any.whl (27 kB)
2026-11-16T11:28:27.0683149Z Using cached pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
2026-11-16T11:28:27.0700777Z Using cached pyasn1-0.6.5-py3-none-any.whl (84 kB)
2026-11-16T11:28:27.0762639Z Using cached pycparser-3.12-py3-none-any.whl (62 kB)
2026-11-16T11:28:27.0782879Z Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
2026-11-16T11:28:27.0807152Z Using cached pyinstaller_hooks_contrib-2026.10-py3-none-any.whl (463 kB)
2026-11-16T11:28:27.0826519Z Using cached pyinstaller-6.22.3-py3-none-win_amd64.whl (1.5 MB)
2026-11-16T11:28:27.0851010Z Using cached PySide6_Addons-6.8.3-cp39-abi3-win_amd64.whl (127.9 MB)
2026-11-16T11:28:27.1396191Z Using cached PySide6_Essentials-6.8.3-cp39-abi3-win_amd64.whl (72.2 MB)
2026-11-16T11:28:27.1798970Z Using cached PySide6-6.8.3-cp39-abi3-win_amd64.whl (561 kB)
2026-11-16T11:28:27.1822232Z Using cached pytest-9.2.0-py3-none-any.whl (411 kB)
2026-11-16T11:28:27.2033007Z Using cached pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
2026-11-16T11:28:27.2051057Z Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
2026-11-16T11:28:27.2091016Z Using cached setuptools-84.2.1-py3-none-any.whl (876 kB)
2026-11-16T11:28:27.2092764Z Using cached shiboken6-6.8.3-cp39-abi3-win_amd64.whl (1.2 MB)
2026-11-16T11:28:27.2117859Z Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-11-16T11:28:27.2135429Z Using cached tzdata-2026.6-py2.py3-none-any.whl (348 kB)
2026-11-16T11:28:27.9219358Z Installing collected packages: altgraph, urllib3, uritemplate, tzdata, typing-extensions, shiboken6, setuptools, pywin32-ctypes, pyparsing, pyinstaller-hooks-contrib, pygments, pycparser, pyasn1, protobuf, pluggy, pefile, oauthlib, more-itertools, jaraco-context, iniconfig, idna, charset-normalizer, certifi, requests, pytest, pyside6-essentials, pyinstaller, pyasn1-modules, proto-plus, opentelemetry-api, jaraco-functools, jaraco-classes, httplib2, googleapis-common-protos, cffi, requests-oauthlib, pyside6-addons, keyring, cryptography, pyside6, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-core, google-api-python-client
2026-11-16T11:29:02.4425820Z 
2026-11-16T11:29:02.4475098Z Successfully installed altgraph-0.17.5 certifi-2026.10.23 cffi-2.1.1 charset-normalizer-3.5.2 cryptography-50.0.2 google-api-core-2.44.0 google-api-python-client-2.202.0 google-auth-2.62.2 google-auth-httplib2-0.4.4 google-auth-oauthlib-1.5.0 googleapis-common-protos-1.76.0 httplib2-0.32.1 idna-3.20 iniconfig-2.3.1 jaraco-classes-3.4.0 jaraco-context-6.1.2 jaraco-functools-4.6.0 keyring-25.7.0 more-itertools-11.2.1 oauthlib-4.0.1 opentelemetry-api-1.45.2 pefile-2024.8.26 pluggy-1.7.0 proto-plus-1.29.0 protobuf-7.36.2 pyasn1-0.6.5 pyasn1-modules-0.4.2 pycparser-3.12 pygments-2.21.0 pyinstaller-6.22.3 pyinstaller-hooks-contrib-2026.10 pyparsing-3.3.3 pyside6-6.8.3 pyside6-addons-6.8.3 pyside6-essentials-6.8.3 pytest-9.2.0 pywin32-ctypes-0.2.3 requests-2.34.2 requests-oauthlib-2.0.0 setuptools-84.2.1 shiboken6-6.8.3 typing-extensions-4.16.0 tzdata-2026.6 uritemplate-4.2.0 urllib3-2.8.0
2026-11-16T11:29:03.6764188Z Obtaining file:///D:/a/Checkpoint/Checkpoint
2026-11-16T11:29:03.6784190Z   Checking if build backend supports build_editable: started
2026-11-16T11:29:04.0133562Z   Checking if build backend supports build_editable: finished with status 'done'
2026-11-16T11:29:04.0156206Z   Preparing editable metadata (pyproject.toml): started
2026-11-16T11:29:04.4046179Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
2026-11-16T11:29:04.4109531Z Building wheels for collected packages: checkpoint-desktop
2026-11-16T11:29:04.4132315Z   Building editable for checkpoint-desktop (pyproject.toml): started
2026-11-16T11:29:04.8712386Z   Building editable for checkpoint-desktop (pyproject.toml): finished with status 'done'
2026-11-16T11:29:04.8729008Z   C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\setuptools\command\editable_wheel.py:354: BuildBackendWarning: Editable installation.
2026-11-16T11:29:04.8729777Z   !!
2026-11-16T11:29:04.8729955Z   
2026-11-16T11:29:04.8730199Z           ********************************************************************************
2026-11-16T11:29:04.8730689Z           Please be careful with folders in your working directory with the same
2026-11-16T11:29:04.8731211Z           name as your package as they may take precedence during imports.
2026-11-16T11:29:04.8731702Z           ********************************************************************************
2026-11-16T11:29:04.8732156Z   
2026-11-16T11:29:04.8732332Z   !!
2026-11-16T11:29:04.8732588Z     with strategy, WheelFile(wheel_path, "w") as wheel_obj:
2026-11-16T11:29:04.8757582Z   Created wheel for checkpoint-desktop: filename=checkpoint_desktop-0.1.38-0.editable-py3-none-any.whl size=3272 sha256=af7c23140e396b0c3e779e3dd43efcf3d59156b0370de794432d8a4a33970761
2026-11-16T11:29:04.8759341Z   Stored in directory: C:\Users\runneradmin\AppData\Local\Temp\pip-ephem-wheel-cache-zuqs1jof\wheels\a2\38\6e\88ad7ec70fd74394064971fa20d15ccdcdb6f76505932df31d
2026-11-16T11:29:04.8786535Z Successfully built checkpoint-desktop
2026-11-16T11:29:04.9013457Z Installing collected packages: checkpoint-desktop
2026-11-16T11:29:04.9348007Z Successfully installed checkpoint-desktop-0.1.38
2026-11-16T11:29:05.3253993Z No broken requirements found.
2026-11-16T11:29:05.4408150Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'
2026-11-16T11:29:05.4408854Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'[0m
2026-11-16T11:29:05.4409547Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
2026-11-16T11:29:05.4410132Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
2026-11-16T11:29:05.4449927Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:29:05.4450274Z env:
2026-11-16T11:29:05.4450465Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:29:05.4450782Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:29:05.4451244Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:29:05.4451689Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:29:05.4452124Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:29:05.4452520Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:29:05.4452833Z ##[endgroup]
2026-11-16T11:29:18.8555700Z ........................................................................ [ 10%]
2026-11-16T11:29:29.5765659Z ........................................................................ [ 20%]
2026-11-16T11:29:43.7651667Z ........................................................................ [ 30%]
2026-11-16T11:29:48.4596677Z ........................................................................ [ 41%]
2026-11-16T11:30:12.8110521Z ........................................................................ [ 51%]
2026-11-16T11:31:50.4048279Z ........................................................................ [ 61%]
2026-11-16T11:32:30.3588939Z ........................................................................ [ 72%]
2026-11-16T11:34:24.1129373Z ........................................................................ [ 82%]
2026-11-16T11:38:28.0584998Z ........................................................................ [ 92%]
2026-11-16T11:39:39.8942409Z ....................................................                     [100%]
2026-11-16T11:39:39.8943380Z 700 passed in 633.27s (0:10:33)
2026-11-16T11:39:40.7933488Z ##[group]Run ./scripts/build.ps1 -Python (Get-Command python).Source
2026-11-16T11:39:40.7934275Z [36;1m./scripts/build.ps1 -Python (Get-Command python).Source[0m
2026-11-16T11:39:40.7975478Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:39:40.7975892Z env:
2026-11-16T11:39:40.7976126Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:39:40.7976496Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:39:40.7977036Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:39:40.7977536Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:39:40.7978013Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:39:40.7978487Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:39:40.7978857Z ##[endgroup]
2026-11-16T11:39:41.8399519Z 234 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
2026-11-16T11:39:41.8402913Z 234 INFO: Python: 3.12.10
2026-11-16T11:39:41.8589135Z 265 INFO: Platform: Windows-2022Server-10.0.20348-SP0
2026-11-16T11:39:41.8589730Z 265 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:39:41.8594790Z 265 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint.spec
2026-11-16T11:39:41.9101179Z 312 INFO: Module search paths (PYTHONPATH):
2026-11-16T11:39:41.9101743Z ['D:\\a\\Checkpoint\\Checkpoint',
2026-11-16T11:39:41.9102281Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
2026-11-16T11:39:41.9102905Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
2026-11-16T11:39:41.9103477Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
2026-11-16T11:39:41.9104012Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
2026-11-16T11:39:41.9104615Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
2026-11-16T11:39:41.9105296Z  '__editable__.checkpoint_desktop-0.1.38.finder.__path_hook__',
2026-11-16T11:39:41.9105840Z  'D:\\a\\Checkpoint\\Checkpoint']
2026-11-16T11:39:42.1382868Z 531 INFO: Appending 'datas' from .spec
2026-11-16T11:39:42.1405924Z 547 INFO: checking Analysis
2026-11-16T11:39:42.1407011Z 547 INFO: Building Analysis because Analysis-00.toc is non existent
2026-11-16T11:39:42.1407845Z 547 INFO: Looking for Python shared library...
2026-11-16T11:39:42.1408756Z 547 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
2026-11-16T11:39:42.1409514Z 547 INFO: Running Analysis Analysis-00.toc
2026-11-16T11:39:42.1410153Z 547 INFO: Target bytecode optimization level: 0
2026-11-16T11:39:42.1410542Z 547 INFO: Initializing module dependency graph...
2026-11-16T11:39:42.1419213Z 547 INFO: Initializing module graph hook caches...
2026-11-16T11:39:42.1579608Z 562 INFO: Analyzing modules for base_library.zip ...
2026-11-16T11:39:43.0140617Z 1407 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:43.1054473Z 1500 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:44.4110125Z 2814 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:44.6105948Z 3017 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:46.1966779Z 4596 INFO: Caching module dependency graph...
2026-11-16T11:39:46.2356446Z 4628 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_checkpoint.py
2026-11-16T11:39:46.4003792Z 4799 INFO: Processing standard module hook 'hook-PySide6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:46.5538590Z 4956 INFO: Processing standard module hook 'hook-shiboken6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:46.6782436Z 5081 INFO: Processing standard module hook 'hook-PySide6.QtNetwork.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:48.8223931Z 7227 INFO: Processing standard module hook 'hook-PySide6.QtCore.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:51.2543381Z 9661 INFO: Processing standard module hook 'hook-PySide6.QtWidgets.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:39:53.6787326Z 12073 INFO: Processing standard module hook 'hook-PySide6.QtGui.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:18.1409328Z 36544 INFO: Processing standard module hook 'hook-sqlite3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:18.4121741Z 36810 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:18.5813371Z 36982 INFO: Processing standard module hook 'hook-keyring.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:19.0297851Z 37436 INFO: Processing pre-safe-import-module hook 'hook-jaraco.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.0304736Z 37436 INFO: SetuptoolsInfo: initializing cached setuptools info...
2026-11-16T11:40:19.4856497Z 37890 INFO: Setuptools: 'jaraco' appears to be a partial setuptools-vendored copy - extending search paths to ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\jaraco', 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\setuptools\\_vendor\\jaraco']!
2026-11-16T11:40:19.4863606Z 37890 INFO: Processing pre-safe-import-module hook 'hook-jaraco.context.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.6967350Z 38093 INFO: Processing pre-safe-import-module hook 'hook-backports.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.6969750Z 38093 INFO: Setuptools: 'backports' appears to be a full setuptools-vendored copy - creating alias to 'setuptools._vendor.backports'!
2026-11-16T11:40:19.7023861Z 38108 INFO: Processing standard module hook 'hook-setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:19.7132942Z 38108 INFO: Processing pre-safe-import-module hook 'hook-distutils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.7645710Z 38171 INFO: Processing standard module hook 'hook-sysconfig.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:19.7736387Z 38171 INFO: Processing pre-safe-import-module hook 'hook-jaraco.functools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.7837022Z 38187 INFO: Processing pre-safe-import-module hook 'hook-more_itertools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:19.9434345Z 38343 INFO: Processing standard module hook 'hook-_osx_support.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:19.9473794Z 38352 INFO: Processing pre-safe-import-module hook 'hook-typing_extensions.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:20.2060783Z 38609 INFO: Processing standard module hook 'hook-multiprocessing.util.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:20.2894375Z 38687 INFO: Processing standard module hook 'hook-xml.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:20.5144792Z 38921 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:20.8536793Z 39249 INFO: Processing pre-safe-import-module hook 'hook-packaging.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:21.1908766Z 39593 INFO: Processing pre-safe-import-module hook 'hook-jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:21.1910647Z 39593 INFO: Setuptools: 'jaraco.text' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.jaraco.text'!
2026-11-16T11:40:21.2024991Z 39609 INFO: Processing standard module hook 'hook-setuptools._vendor.jaraco.text.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:21.2038585Z 39609 INFO: Processing pre-safe-import-module hook 'hook-importlib_resources.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:21.6100659Z 40015 INFO: Processing pre-safe-import-module hook 'hook-tomli.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:21.6102712Z 40015 INFO: Setuptools: 'tomli' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.tomli'!
2026-11-16T11:40:22.2003917Z 40594 INFO: Processing pre-safe-import-module hook 'hook-wheel.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:22.2006256Z 40594 INFO: Setuptools: 'wheel' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.wheel'!
2026-11-16T11:40:22.3180397Z 40718 INFO: Processing pre-safe-import-module hook 'hook-importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:22.3182614Z 40718 INFO: Setuptools: 'importlib_metadata' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.importlib_metadata'!
2026-11-16T11:40:22.3403150Z 40734 INFO: Processing standard module hook 'hook-setuptools._vendor.importlib_metadata.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:22.3603948Z 40765 INFO: Processing pre-safe-import-module hook 'hook-zipp.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:22.3606658Z 40765 INFO: Setuptools: 'zipp' appears to be a setuptools-vendored copy - creating alias to 'setuptools._vendor.zipp'!
2026-11-16T11:40:22.4051685Z 40812 INFO: Processing standard module hook 'hook-win32ctypes.core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:23.1118329Z 41516 INFO: Processing standard module hook 'hook-pycparser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:23.5563564Z 41953 INFO: Processing standard module hook 'hook-webbrowser.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:23.8247259Z 42219 INFO: Processing standard module hook 'hook-cryptography.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:24.7986947Z 43204 INFO: hook-cryptography: cryptography does not seem to be using dynamically linked OpenSSL.
2026-11-16T11:40:25.5061236Z 43908 INFO: Processing standard module hook 'hook-urllib3.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:25.9828036Z 44377 INFO: Processing standard module hook 'hook-certifi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:26.0267900Z 44424 INFO: Processing standard module hook 'hook-charset_normalizer.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:26.6605462Z 45065 INFO: Processing standard module hook 'hook-google.api_core.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:26.6837790Z 45080 INFO: Processing standard module hook 'hook-opentelemetry.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:26.9894388Z 45393 INFO: Processing standard module hook 'hook-httplib2.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:27.3173527Z 45722 INFO: Processing standard module hook 'hook-difflib.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:27.5384392Z 45941 INFO: Processing standard module hook 'hook-googleapiclient.model.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\stdhooks'
2026-11-16T11:40:28.0175516Z 46410 INFO: Processing standard module hook 'hook-PySide6.QtSvg.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:28.6926408Z 47099 INFO: Processing standard module hook 'hook-xml.etree.cElementTree.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:28.9887580Z 47396 INFO: Processing module hooks (post-graph stage)...
2026-11-16T11:40:29.0084414Z 47411 WARNING: Hidden import "pycparser.lextab" not found!
2026-11-16T11:40:29.0086266Z 47411 WARNING: Hidden import "pycparser.yacctab" not found!
2026-11-16T11:40:29.0335268Z 47427 INFO: Processing pre-safe-import-module hook 'hook-gi.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_safe_import_module'
2026-11-16T11:40:29.1773701Z 47583 INFO: Performing binary vs. data reclassification (813 entries)
2026-11-16T11:40:29.2453636Z 47646 INFO: Looking for ctypes DLLs
2026-11-16T11:40:29.2801336Z 47677 INFO: Analyzing run-time hooks ...
2026-11-16T11:40:29.2839679Z 47677 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:29.2863530Z 47693 INFO: Including run-time hook 'pyi_rth_pkgutil.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:29.2882863Z 47693 INFO: Including run-time hook 'pyi_rth_multiprocessing.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:29.2903016Z 47693 INFO: Including run-time hook 'pyi_rth_setuptools.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:29.2914726Z 47693 INFO: Including run-time hook 'pyi_rth_pyside6.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:29.2931254Z 47693 INFO: Processing pre-find-module-path hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path'
2026-11-16T11:40:29.2944475Z 47693 INFO: Processing standard module hook 'hook-_pyi_rth_utils.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:29.2970331Z 47693 INFO: Including run-time hook 'pyi_rth_cryptography_openssl.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\_pyinstaller_hooks_contrib\\rthooks'
2026-11-16T11:40:29.3265669Z 47725 INFO: Creating base_library.zip...
2026-11-16T11:40:29.3460243Z 47741 INFO: Looking for dynamic libraries
2026-11-16T11:40:30.0635827Z 48459 INFO: Extra DLL search directories (AddDllDirectory): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\shiboken6']
2026-11-16T11:40:30.0636882Z 48459 INFO: Extra DLL search directories (PATH): ['C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PySide6']
2026-11-16T11:40:31.7996755Z 50196 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\warn-Checkpoint.txt
2026-11-16T11:40:31.8852618Z 50290 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\xref-Checkpoint.html
2026-11-16T11:40:31.9335443Z 50337 INFO: checking PYZ
2026-11-16T11:40:31.9336178Z 50337 INFO: Building PYZ because PYZ-00.toc is non existent
2026-11-16T11:40:31.9337448Z 50337 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz
2026-11-16T11:40:32.6754798Z 51072 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\PYZ-00.pyz completed successfully.
2026-11-16T11:40:32.7014244Z 51103 INFO: checking PKG
2026-11-16T11:40:32.7015075Z 51103 INFO: Building PKG because PKG-00.toc is non existent
2026-11-16T11:40:32.7015851Z 51103 INFO: Building PKG (CArchive) Checkpoint.pkg
2026-11-16T11:40:32.7190527Z 51119 INFO: Building PKG (CArchive) Checkpoint.pkg completed successfully.
2026-11-16T11:40:32.7197587Z 51119 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\runw.exe
2026-11-16T11:40:32.7198440Z 51119 INFO: checking EXE
2026-11-16T11:40:32.7198983Z 51119 INFO: Building EXE because EXE-00.toc is non existent
2026-11-16T11:40:32.7199538Z 51119 INFO: Building EXE from EXE-00.toc
2026-11-16T11:40:32.7201544Z 51119 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\Checkpoint\Checkpoint.exe
2026-11-16T11:40:32.7232736Z 51119 INFO: Copying icon to EXE
2026-11-16T11:40:32.7249625Z 51119 INFO: Copying 0 resources to EXE
2026-11-16T11:40:32.7250071Z 51119 INFO: Embedding manifest in EXE
2026-11-16T11:40:32.7263794Z 51119 INFO: Appending PKG archive to EXE
2026-11-16T11:40:32.7307088Z 51134 INFO: Fixing EXE headers
2026-11-16T11:40:32.8073523Z 51213 INFO: Building EXE from EXE-00.toc completed successfully.
2026-11-16T11:40:32.8160802Z 51213 INFO: checking COLLECT
2026-11-16T11:40:32.8161477Z 51213 INFO: Building COLLECT because COLLECT-00.toc is non existent
2026-11-16T11:40:32.8163399Z 51213 INFO: Building COLLECT COLLECT-00.toc
2026-11-16T11:40:33.4117103Z 51807 INFO: Building COLLECT COLLECT-00.toc completed successfully.
2026-11-16T11:40:33.4307023Z 51823 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\dist
2026-11-16T11:40:33.7551314Z 109 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.10
2026-11-16T11:40:33.7556112Z 109 INFO: Python: 3.12.10
2026-11-16T11:40:33.7769728Z 140 INFO: Platform: Windows-2022Server-10.0.20348-SP0
2026-11-16T11:40:33.7770631Z 140 INFO: Python environment: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:40:33.7776608Z 140 INFO: wrote D:\a\Checkpoint\Checkpoint\work\pyinstaller\CheckpointUpdater.spec
2026-11-16T11:40:33.7809318Z 140 INFO: Module search paths (PYTHONPATH):
2026-11-16T11:40:33.7809920Z ['D:\\a\\Checkpoint\\Checkpoint',
2026-11-16T11:40:33.7810339Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python312.zip',
2026-11-16T11:40:33.7810817Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\DLLs',
2026-11-16T11:40:33.7811272Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib',
2026-11-16T11:40:33.7811690Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64',
2026-11-16T11:40:33.7812151Z  'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages',
2026-11-16T11:40:33.7812707Z  '__editable__.checkpoint_desktop-0.1.38.finder.__path_hook__',
2026-11-16T11:40:33.7813108Z  'D:\\a\\Checkpoint\\Checkpoint']
2026-11-16T11:40:34.0065321Z 359 INFO: checking Analysis
2026-11-16T11:40:34.0066129Z 359 INFO: Building Analysis because Analysis-00.toc is non existent
2026-11-16T11:40:34.0067078Z 359 INFO: Looking for Python shared library...
2026-11-16T11:40:34.0067923Z 359 INFO: Using Python shared library: C:\hostedtoolcache\windows\Python\3.12.10\x64\python312.dll
2026-11-16T11:40:34.0069203Z 359 INFO: Running Analysis Analysis-00.toc
2026-11-16T11:40:34.0069914Z 359 INFO: Target bytecode optimization level: 0
2026-11-16T11:40:34.0070530Z 359 INFO: Initializing module dependency graph...
2026-11-16T11:40:34.0079841Z 359 INFO: Initializing module graph hook caches...
2026-11-16T11:40:34.0228977Z 375 INFO: Analyzing modules for base_library.zip ...
2026-11-16T11:40:34.8380125Z 1202 INFO: Processing standard module hook 'hook-heapq.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:34.9224500Z 1283 INFO: Processing standard module hook 'hook-encodings.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:36.2140461Z 2564 INFO: Processing standard module hook 'hook-math.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:36.4367932Z 2799 INFO: Processing standard module hook 'hook-pickle.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:37.8387910Z 4191 INFO: Caching module dependency graph...
2026-11-16T11:40:37.8761297Z 4237 INFO: Analyzing D:\a\Checkpoint\Checkpoint\run_updater.py
2026-11-16T11:40:37.8982076Z 4253 INFO: Processing standard module hook 'hook-_ctypes.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:37.9672294Z 4331 INFO: Processing standard module hook 'hook-platform.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks'
2026-11-16T11:40:37.9765475Z 4331 INFO: Processing module hooks (post-graph stage)...
2026-11-16T11:40:37.9822991Z 4347 INFO: Performing binary vs. data reclassification (1 entries)
2026-11-16T11:40:37.9832452Z 4347 INFO: Looking for ctypes DLLs
2026-11-16T11:40:37.9895847Z 4347 INFO: Analyzing run-time hooks ...
2026-11-16T11:40:37.9903378Z 4347 INFO: Including run-time hook 'pyi_rth_inspect.py' from 'C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks'
2026-11-16T11:40:37.9947599Z 4347 INFO: Creating base_library.zip...
2026-11-16T11:40:38.0139151Z 4378 INFO: Looking for dynamic libraries
2026-11-16T11:40:38.1212184Z 4472 INFO: Extra DLL search directories (AddDllDirectory): []
2026-11-16T11:40:38.1212698Z 4472 INFO: Extra DLL search directories (PATH): []
2026-11-16T11:40:38.4232957Z 4786 INFO: Warnings written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\warn-CheckpointUpdater.txt
2026-11-16T11:40:38.4385371Z 4801 INFO: Graph cross-reference written to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\xref-CheckpointUpdater.html
2026-11-16T11:40:38.4527735Z 4817 INFO: checking PYZ
2026-11-16T11:40:38.4528589Z 4817 INFO: Building PYZ because PYZ-00.toc is non existent
2026-11-16T11:40:38.4529479Z 4817 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz
2026-11-16T11:40:38.6042917Z 4957 INFO: Building PYZ (ZlibArchive) D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\PYZ-00.pyz completed successfully.
2026-11-16T11:40:38.6081672Z 4973 INFO: checking PKG
2026-11-16T11:40:38.6082937Z 4973 INFO: Building PKG because PKG-00.toc is non existent
2026-11-16T11:40:38.6083600Z 4973 INFO: Building PKG (CArchive) CheckpointUpdater.pkg
2026-11-16T11:40:38.6202014Z 4973 INFO: Building PKG (CArchive) CheckpointUpdater.pkg completed successfully.
2026-11-16T11:40:38.6209248Z 4973 INFO: Bootloader C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\run.exe
2026-11-16T11:40:38.6210216Z 4973 INFO: checking EXE
2026-11-16T11:40:38.6210854Z 4973 INFO: Building EXE because EXE-00.toc is non existent
2026-11-16T11:40:38.6211724Z 4973 INFO: Building EXE from EXE-00.toc
2026-11-16T11:40:38.6213971Z 4973 INFO: Copying bootloader EXE to D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-build\CheckpointUpdater\CheckpointUpdater.exe
2026-11-16T11:40:38.6233824Z 4973 INFO: Copying icon to EXE
2026-11-16T11:40:38.6255357Z 4989 INFO: Copying 0 resources to EXE
2026-11-16T11:40:38.6255940Z 4989 INFO: Embedding manifest in EXE
2026-11-16T11:40:38.6270785Z 4989 INFO: Appending PKG archive to EXE
2026-11-16T11:40:38.6279489Z 4989 INFO: Fixing EXE headers
2026-11-16T11:40:38.6968187Z 5051 INFO: Building EXE from EXE-00.toc completed successfully.
2026-11-16T11:40:38.6981882Z 5051 INFO: checking COLLECT
2026-11-16T11:40:38.6983208Z 5051 INFO: Building COLLECT because COLLECT-00.toc is non existent
2026-11-16T11:40:38.6985240Z 5051 INFO: Building COLLECT COLLECT-00.toc
2026-11-16T11:40:38.7329683Z 5098 INFO: Building COLLECT COLLECT-00.toc completed successfully.
2026-11-16T11:40:38.7344607Z 5098 INFO: Build complete! The results are available in: D:\a\Checkpoint\Checkpoint\work\pyinstaller\helper-dist
2026-11-16T11:40:38.8613222Z ##[group]Run python scripts/package_windows_release.py --test-report .ci-results/pytest.xml
2026-11-16T11:40:38.8614079Z [36;1mpython scripts/package_windows_release.py --test-report .ci-results/pytest.xml[0m
2026-11-16T11:40:38.8614713Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Validação do pacote Windows falhou.' }[0m
2026-11-16T11:40:38.8653788Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:40:38.8654211Z env:
2026-11-16T11:40:38.8654440Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:40:38.8654806Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:40:38.8655329Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:40:38.8655813Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:40:38.8656250Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:40:38.8656765Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:40:38.8657139Z ##[endgroup]
2026-11-16T11:40:52.6856290Z Checkpoint smoke: 6 pages OK; SQLite integrity=ok
2026-11-16T11:40:53.8099031Z Cadastro smoke: salvar, auxiliar, renderiza��o e SQLite OK
2026-11-16T11:41:01.3575651Z Checkpoint 0.1.38 � Windows x64
2026-11-16T11:41:01.3576399Z Commit: c4a7e1d221ba52a8580dd73ab884b1964e6ffd32
2026-11-16T11:41:01.3577122Z Python: 3.12.10
2026-11-16T11:41:01.3577741Z Testes: {'tests': 700, 'failures': 0, 'errors': 0, 'skipped': 0}
2026-11-16T11:41:01.3578689Z Smoke do fonte: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
2026-11-16T11:41:01.3579633Z Smoke do ZIP extra�do: 6 p�ginas; SQLite �ntegro; biblioteca vazia.
2026-11-16T11:41:01.3581704Z Auxiliar isolado do fonte e do ZIP extra�do: resposta e schema verificados.
2026-11-16T11:41:01.3583249Z Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
2026-11-16T11:41:01.3584392Z CheckpointUpdater.exe --check: sa�da 0.
2026-11-16T11:41:01.3586061Z Inicializa��o normal nativa Windows do fonte e do execut�vel extra�do: HWND vis�vel, resposta, captura, fechamento e SQLite verificados; executor j� elevado, sem automatizar consentimento UAC.
2026-11-16T11:41:01.3588309Z ZIP SHA-256: 15fef170b44dcf6073d50fed3f601f8b1cb265540c5e456113fe2befad0e3702
2026-11-16T11:41:01.3590233Z Steam autenticada e homologa��o Windows 10/11 pessoal n�o est�o cobertas.
2026-11-16T11:41:01.4819503Z ##[group]Run python scripts/render_ui_review.py work/ui-review
2026-11-16T11:41:01.4820151Z [36;1mpython scripts/render_ui_review.py work/ui-review[0m
2026-11-16T11:41:01.4820668Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Capturas da interface falharam.' }[0m
2026-11-16T11:41:01.4821222Z [36;1mpython scripts/package_ui_review.py work/ui-review release-assets[0m
2026-11-16T11:41:01.4821810Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Revisão visual incompleta.' }[0m
2026-11-16T11:41:01.4861410Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
2026-11-16T11:41:01.4861832Z env:
2026-11-16T11:41:01.4862070Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:41:01.4862437Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:01.4863010Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:41:01.4863530Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:01.4864094Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:01.4864554Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:01.4864919Z ##[endgroup]
2026-11-16T11:41:03.3935764Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
2026-11-16T11:41:12.1093248Z WARNING:root:Moldura integrada indispon�vel; controles nativos preservados.
2026-11-16T11:41:12.3502220Z D:\a\Checkpoint\Checkpoint\work\ui-review
2026-11-16T11:41:12.6490951Z Revis�o visual: 61 PNGs e �ndice HTML; bases e logs exclu�dos.
2026-11-16T11:41:12.7804618Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
2026-11-16T11:41:12.7805085Z with:
2026-11-16T11:41:12.7805292Z   name: checkpoint-windows-release
2026-11-16T11:41:12.7805561Z   path: release-assets/*
2026-11-16T11:41:12.7805793Z   if-no-files-found: error
2026-11-16T11:41:12.7806010Z   retention-days: 14
2026-11-16T11:41:12.7806205Z   compression-level: 6
2026-11-16T11:41:12.7806403Z   overwrite: false
2026-11-16T11:41:12.7806603Z   include-hidden-files: false
2026-11-16T11:41:12.7806815Z env:
2026-11-16T11:41:12.7806985Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:41:12.7807286Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:12.7807743Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:41:12.7808243Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:12.7808646Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:12.7809098Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:12.7809412Z ##[endgroup]
2026-11-16T11:41:12.9637987Z (node:3240) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T11:41:12.9638747Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T11:41:12.9731091Z With the provided path, there will be 10 files uploaded
2026-11-16T11:41:12.9736127Z Artifact name is valid!
2026-11-16T11:41:12.9738871Z Root directory input is valid!
2026-11-16T11:41:13.2536264Z Beginning upload of artifact content to blob storage
2026-11-16T11:41:13.5393644Z (node:3240) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T11:41:14.2834901Z Uploaded bytes 8388608
2026-11-16T11:41:14.4748368Z Uploaded bytes 16777216
2026-11-16T11:41:14.5511328Z Uploaded bytes 25165824
2026-11-16T11:41:14.7728997Z Uploaded bytes 33554432
2026-11-16T11:41:14.7981808Z Uploaded bytes 41943040
2026-11-16T11:41:15.0944160Z Uploaded bytes 50331648
2026-11-16T11:41:15.3046764Z Uploaded bytes 58720256
2026-11-16T11:41:15.5169699Z Uploaded bytes 67108864
2026-11-16T11:41:15.8294718Z Uploaded bytes 75497472
2026-11-16T11:41:16.0196927Z Uploaded bytes 83886080
2026-11-16T11:41:16.1267987Z Uploaded bytes 88040845
2026-11-16T11:41:16.1776527Z Finished uploading artifact content to blob storage!
2026-11-16T11:41:16.1781300Z SHA256 digest of uploaded artifact zip is 40af0a210d63e54976f3c90048796551f768ed9c9a368ad4c470827835dc06e3
2026-11-16T11:41:16.1784161Z Finalizing artifact upload
2026-11-16T11:41:16.5400731Z Artifact checkpoint-windows-release.zip successfully finalized. Artifact ID 14223096127
2026-11-16T11:41:16.5402144Z Artifact checkpoint-windows-release has been successfully uploaded! Final size is 88040845 bytes. Artifact ID is 14223096127
2026-11-16T11:41:16.5413148Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43857996709/artifacts/14223096127
2026-11-16T11:41:16.5671424Z ##[group]Run actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
2026-11-16T11:41:16.5672001Z with:
2026-11-16T11:41:16.5672285Z   name: checkpoint-windows-test-report
2026-11-16T11:41:16.5686691Z   path: .ci-results/pytest.xml
2026-11-16T11:41:16.5687110Z   if-no-files-found: ignore
2026-11-16T11:41:16.5687494Z   retention-days: 14
2026-11-16T11:41:16.5687828Z   compression-level: 6
2026-11-16T11:41:16.5688318Z   overwrite: false
2026-11-16T11:41:16.5689003Z   include-hidden-files: false
2026-11-16T11:41:16.5689303Z env:
2026-11-16T11:41:16.5689497Z   QT_QPA_PLATFORM: offscreen
2026-11-16T11:41:16.5689822Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:16.5690305Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
2026-11-16T11:41:16.5690789Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:16.5692014Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:16.5692432Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
2026-11-16T11:41:16.5692748Z ##[endgroup]
2026-11-16T11:41:16.7427896Z (node:1992) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T11:41:16.7428621Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T11:41:16.7478804Z With the provided path, there will be 1 file uploaded
2026-11-16T11:41:16.7483824Z Artifact name is valid!
2026-11-16T11:41:16.7486718Z Root directory input is valid!
2026-11-16T11:41:17.0118979Z Beginning upload of artifact content to blob storage
2026-11-16T11:41:17.0335098Z (node:1992) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-11-16T11:41:17.1855546Z Uploaded bytes 14257
2026-11-16T11:41:17.2310244Z Finished uploading artifact content to blob storage!
2026-11-16T11:41:17.2311937Z SHA256 digest of uploaded artifact zip is 052bee3efd172a2868f14e38b06bbae41caa4310ed324f962ebd938dd76ae91e
2026-11-16T11:41:17.2314283Z Finalizing artifact upload
2026-11-16T11:41:17.6624282Z Artifact checkpoint-windows-test-report.zip successfully finalized. Artifact ID 14222987143
2026-11-16T11:41:17.6625390Z Artifact checkpoint-windows-test-report has been successfully uploaded! Final size is 14257 bytes. Artifact ID is 14222987143
2026-11-16T11:41:17.6633988Z Artifact download URL: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43857996709/artifacts/14222987143
2026-11-16T11:41:17.6970363Z Post job cleanup.
2026-11-16T11:41:17.8290012Z Cache hit occurred on the primary key setup-python-Windows-x64-python-3.12.10-pip-eb71efc05b2754f3c8048b82aafb5b6c4b1d694285a4ae18da9e58d103e7bab6, not saving cache.
2026-11-16T11:41:17.8291406Z (node:5540) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-11-16T11:41:17.8292087Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-11-16T11:41:17.8516478Z Post job cleanup.
2026-11-16T11:41:18.0621836Z [command]"C:\Program Files\Git\bin\git.exe" version
2026-11-16T11:41:18.0885454Z git version 2.56.1.windows.1
2026-11-16T11:41:18.0940114Z Temporarily overriding HOME='D:\a\_temp\6b175a06-028c-4759-94d1-1086b8ac9ae9' before making global git config changes
2026-11-16T11:41:18.0941398Z Adding repository directory to the temporary git global config as a safe directory
2026-11-16T11:41:18.0950911Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\Checkpoint\Checkpoint
2026-11-16T11:41:18.1233192Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
2026-11-16T11:41:18.1510748Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
2026-11-16T11:41:18.5826185Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-11-16T11:41:18.6101804Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
2026-11-16T11:41:19.0514393Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-11-16T11:41:19.0789078Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
2026-11-16T11:41:19.5135078Z Evaluate and set job outputs
2026-11-16T11:41:19.5142343Z Set output 'version'
2026-11-16T11:41:19.5144298Z Cleaning up orphan processes
2026-11-16T11:41:19.5528807Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@11d5960a326750d5838078e36cf38b85af677262, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/


```

## Arquivos publicados verificados

```json
{
  "release_sha": "c4a7e1d221ba52a8580dd73ab884b1964e6ffd32",
  "assets": [
    {
      "file": "Checkpoint-0.1.38-detail-overview.png",
      "bytes": 96121,
      "sha256": "0049d9e10aff3cf759c781d90b736c5b8c571d624d7c1e5f99484757d4333d0e"
    },
    {
      "file": "Checkpoint-0.1.38-home.png",
      "bytes": 84584,
      "sha256": "c61c2a492c2c93e146ab737e5be16e4008d84217e14d0f51103d95cff180542d"
    },
    {
      "file": "Checkpoint-0.1.38-library.png",
      "bytes": 137853,
      "sha256": "19186657670ec2b8e17db3e59a27b682179105354fbceebb093748f32c79f617"
    },
    {
      "file": "Checkpoint-0.1.38-native-startup.json",
      "bytes": 284,
      "sha256": "75a57df76b28f1c826b5d5ede6e0dd18d1c922c9f2395a0e589bd26c9197e48a"
    },
    {
      "file": "Checkpoint-0.1.38-native-startup.png",
      "bytes": 57626,
      "sha256": "1e9a3c229088e110cc3bdb46193e6c5bd842de4f25fc9524806e639c667c8e27"
    },
    {
      "file": "Checkpoint-0.1.38-ui-review.txt",
      "bytes": 560,
      "sha256": "1a8a2f68366a63696c327ef314695e6def2cdf419428fdb2139792a6952f376c"
    },
    {
      "file": "Checkpoint-0.1.38-ui-review.zip",
      "bytes": 3794454,
      "sha256": "9808421736bb72ea4868bb26dd2571cd4fcca311d888fdc5e8bd0b249c7e383b",
      "crc_valid": true
    },
    {
      "file": "Checkpoint-0.1.38-validation.txt",
      "bytes": 884,
      "sha256": "d63335f462dd4f3f506d0cd913f1df22c65885b2eecc77f559f8bac6c9afae32"
    },
    {
      "file": "Checkpoint-0.1.38-windows-x64.zip",
      "bytes": 84314842,
      "sha256": "15fef170b44dcf6073d50fed3f601f8b1cb265540c5e456113fe2befad0e3702",
      "crc_valid": true
    },
    {
      "file": "Checkpoint-0.1.38-windows-x64.zip.sha256",
      "bytes": 101,
      "sha256": "0f2a944339815eba467f1963dcca0bfd55d1f286e6fd29d3f2f903dc0ea5a9fb"
    }
  ],
  "native": {
    "backend": "windows",
    "ordinary_startup": true,
    "already_elevated": true,
    "pid": 2248,
    "hwnd": 721372,
    "client_size": [
      1100,
      740
    ],
    "responsive": true,
    "screenshot": "native-startup.png",
    "exit_code": 0,
    "stdout": "",
    "stderr": ""
  },
  "tests": {
    "tests": 700,
    "failures": 0,
    "errors": 0,
    "skipped": 0
  }
}
```

# Lançamento Checkpoint 0.1.35

Pré-release publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.35

Workflow concluído: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335

Commit do aplicativo e tag v0.1.35: df5ff41e74b36cea4e2abd160e1172f4166bf32a. Autorização explícita do dono para lançamento recebida nesta conversa.

542 testes Windows passaram, sem falhas, erros ou skips. Build, aplicativo/atualizador, smokes do fonte e do ZIP extraído e revisão visual concluídos. O hash publicado pelo GitHub para o ZIP coincide com o arquivo SHA-256 e com validation.txt: c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571.

A validação no runner Windows não é homologação no PC do dono. Permanecem as pendências públicas A4, fechamento apenas da ROM com emulador aberto e captura real de jogos; não foram declaradas resolvidas. Nenhum teste, workflow ou arquivo protegido foi alterado na preparação. tzdata==2026.6 foi adicionado para disponibilizar IANA ZoneInfo nos testes Windows, com reprodução antes/depois sem alterar asserções.

## Validação publicada — conteúdo integral

```text
Checkpoint 0.1.35 · Windows x64
Commit: df5ff41e74b36cea4e2abd160e1172f4166bf32a
Python: 3.12.10
Testes: {'tests': 542, 'failures': 0, 'errors': 0, 'skipped': 0}
Smoke do fonte: 6 páginas; SQLite íntegro; biblioteca vazia.
Smoke do ZIP extraído: 6 páginas; SQLite íntegro; biblioteca vazia.
Auxiliar isolado do fonte e do ZIP extraído: resposta e schema verificados.
Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
CheckpointUpdater.exe --check: saída 0.
ZIP SHA-256: c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571
Steam autenticada e homologação Windows 10/11 pessoal não estão cobertas.
```

## Etapa completa dos testes Windows — log original

```text
build	Test on Windows	﻿2026-11-15T03:09:35.5610194Z ##[group]Run $env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'
build	Test on Windows	2026-11-15T03:09:35.5611023Z [36;1m$env:CHECKPOINT_TEST_ROOT = Join-Path $env:RUNNER_TEMP 'checkpoint-tests'[0m
build	Test on Windows	2026-11-15T03:09:35.5611764Z [36;1mpython -X faulthandler -m pytest tests -q -p no:cacheprovider --junitxml=.ci-results/pytest.xml[0m
build	Test on Windows	2026-11-15T03:09:35.5612448Z [36;1mif ($LASTEXITCODE -ne 0) { throw 'Testes Windows falharam.' }[0m
build	Test on Windows	2026-11-15T03:09:35.5649948Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
build	Test on Windows	2026-11-15T03:09:35.5650232Z env:
build	Test on Windows	2026-11-15T03:09:35.5650395Z   QT_QPA_PLATFORM: offscreen
build	Test on Windows	2026-11-15T03:09:35.5650647Z   pythonLocation: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-15T03:09:35.5651008Z   PKG_CONFIG_PATH: C:\hostedtoolcache\windows\Python\3.12.10\x64/lib/pkgconfig
build	Test on Windows	2026-11-15T03:09:35.5651361Z   Python_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-15T03:09:35.5651674Z   Python2_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-15T03:09:35.5652011Z   Python3_ROOT_DIR: C:\hostedtoolcache\windows\Python\3.12.10\x64
build	Test on Windows	2026-11-15T03:09:35.5652977Z ##[endgroup]
build	Test on Windows	2026-11-15T03:09:47.2931382Z ........................................................................ [ 13%]
build	Test on Windows	2026-11-15T03:09:55.5128131Z ........................................................................ [ 26%]
build	Test on Windows	2026-11-15T03:10:00.1127098Z ........................................................................ [ 39%]
build	Test on Windows	2026-11-15T03:10:16.9466028Z ........................................................................ [ 53%]
build	Test on Windows	2026-11-15T03:10:59.0609386Z ........................................................................ [ 66%]
build	Test on Windows	2026-11-15T03:12:30.0811294Z ........................................................................ [ 79%]
build	Test on Windows	2026-11-15T03:14:24.1919700Z ........................................................................ [ 92%]
build	Test on Windows	2026-11-15T03:15:56.2025703Z ......................................                                   [100%]
build	Test on Windows	2026-11-15T03:15:56.2026222Z 542 passed in 379.76s (0:06:19)
```

## Comandos e saídas integrais da preparação e publicação

PYTHONTZPATH vazio foi usado nas duas execuções do módulo test_dates_0135.py para reproduzir a ausência da base de fusos do sistema. A primeira falhou por falta de tzdata; a segunda passou após instalar a dependência. Todos os resultados foram preservados.

### /workspace/work/venv/bin/python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; from checkpoint.database import MIGRATIONS; assert tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]["version"] == __version__ == "0.1.35"; assert len(MIGRATIONS)==4; print("Versão 0.1.35 consistente; schema 4 preservado.")'

Horário UTC: 2026-11-15T03:05:13.180560+00:00

stdout:
````text
Versão 0.1.35 consistente; schema 4 preservado.
````

stderr:
````text
````

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_updates.py tests/test_visual_0132.py tests/test_save_lifecycle.py -q -p no:cacheprovider

Horário UTC: 2026-11-15T03:05:33.326520+00:00

stdout:
````text
.............................................................            [100%]
61 passed in 19.78s
````

stderr:
````text
````

Código de saída: 0

### /workspace/work/venv/bin/python -m pip index versions tzdata

Horário UTC: 2026-11-15T03:06:25.742162+00:00

stdout:
````text
tzdata (2026.6)
Available versions: 2026.6, 2026.5, 2026.4, 2026.3, 2026.2, 2026.1, 2025.3, 2025.2, 2025.1, 2024.2, 2024.1, 2023.4, 2023.3, 2023.2, 2023.1, 2022.7, 2022.6, 2022.5, 2022.4, 2022.3, 2022.2, 2022.1, 2021.5, 2021.4, 2021.3, 2021.2.post0, 2021.2, 2021.1, 2020.5, 2020.4, 2020.3, 2020.2, 2020.1
````

stderr:
````text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip
````

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py -q -p no:cacheprovider --tb=short

Horário UTC: 2026-11-15T03:06:26.252597+00:00

stdout:
````text
FF                                                                       [100%]
=================================== FAILURES ===================================
________ test_daily_local_preserves_raw_utc[Zelda: A Link to the Past] _________
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/zoneinfo/_common.py:12: in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:46: in wrapper
    return func(anchor)
           ^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:56: in files
    return from_package(resolve(anchor))
                        ^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/functools.py:912: in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:82: in _
    return importlib.import_module(cand)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:
tests/test_dates_0135.py:7: in test_daily_local_preserves_raw_utc
    assert library.stats(display_timezone=ZoneInfo('America/Sao_Paulo'))['daily']=={'2026-11-14':600}
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/zoneinfo/_common.py:24: in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
E   zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key America/Sao_Paulo'
______________ test_daily_local_preserves_raw_utc[Metroid Fusion] ______________
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/zoneinfo/_common.py:12: in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:46: in wrapper
    return func(anchor)
           ^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:56: in files
    return from_package(resolve(anchor))
                        ^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/functools.py:912: in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/resources/_common.py:82: in _
    return importlib.import_module(cand)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:
tests/test_dates_0135.py:7: in test_daily_local_preserves_raw_utc
    assert library.stats(display_timezone=ZoneInfo('America/Sao_Paulo'))['daily']=={'2026-11-14':600}
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/zoneinfo/_common.py:24: in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
E   zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key America/Sao_Paulo'
=========================== short test summary info ============================
FAILED tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Zelda: A Link to the Past]
FAILED tests/test_dates_0135.py::test_daily_local_preserves_raw_utc[Metroid Fusion]
2 failed in 0.07s
````

stderr:
````text
````

Código de saída: 1

### /workspace/work/venv/bin/python -m pip install tzdata==2026.6

Horário UTC: 2026-11-15T03:06:39.808791+00:00

stdout:
````text
Collecting tzdata==2026.6
  Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata
Successfully installed tzdata-2026.6
````

stderr:
````text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip
````

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py -q -p no:cacheprovider --tb=short

Horário UTC: 2026-11-15T03:06:40.166119+00:00

stdout:
````text
..                                                                       [100%]
2 passed in 0.04s
````

stderr:
````text
````

Código de saída: 0

### /workspace/work/venv/bin/python -m pip check

Horário UTC: 2026-11-15T03:06:40.445031+00:00

stdout:
````text
No broken requirements found.
````

stderr:
````text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
````

Código de saída: 0

### git diff --check

Horário UTC: 2026-11-15T03:06:40.474029+00:00

stdout:
````text
````

stderr:
````text
````

Código de saída: 0

### git diff --name-only

Horário UTC: 2026-11-15T03:08:00.603662+00:00

stdout:
````text
.github/release-notes.md
CHANGELOG.md
CONTINUITY.md
PROJECT_STATUS.md
checkpoint/__init__.py
pyproject.toml
requirements-tested.txt
````

stderr:
````text
````

Código de saída: 0

### git ls-remote origin refs/heads/fix/0.1.35-ajustes refs/tags/v0.1.35

Horário UTC: 2026-11-15T03:08:01.047128+00:00

stdout:
````text
f0a5514825b05d0f41aa129cdd5f0e65546a2d7c	refs/heads/fix/0.1.35-ajustes
````

stderr:
````text
````

Código de saída: 0

### git diff --name-only f0a5514825b05d0f41aa129cdd5f0e65546a2d7c -- checkpoint/dialogs.py checkpoint/quick_add.py checkpoint/worker.py checkpoint/enrichment.py checkpoint/game_import.py checkpoint/completion_queue.py tests/test_save_lifecycle.py tests/test_visual_0132.py .github/workflows

Horário UTC: 2026-11-15T03:08:01.079331+00:00

stdout:
````text
````

stderr:
````text
````

Código de saída: 0

### git commit -m 'release: preparar 0.1.35 e dados de fuso para testes Windows'

Horário UTC: 2026-11-15T03:08:07.625568+00:00

stdout:
````text
[fix/0.1.35-ajustes df5ff41] release: preparar 0.1.35 e dados de fuso para testes Windows
 8 files changed, 325 insertions(+), 76 deletions(-)
 create mode 100644 RELATORIO_PREPARACAO_0135.md
````

stderr:
````text
````

Código de saída: 0

### git push origin fix/0.1.35-ajustes

Horário UTC: 2026-11-15T03:08:09.002892+00:00

stdout:
````text
````

stderr:
````text
To https://github.com/pedroalexcarneiro/Checkpoint.git
   f0a5514..df5ff41  fix/0.1.35-ajustes -> fix/0.1.35-ajustes
````

Código de saída: 0

### git ls-remote origin refs/heads/fix/0.1.35-ajustes

Horário UTC: 2026-11-15T03:08:28.271387+00:00

stdout:
````text
df5ff41e74b36cea4e2abd160e1172f4166bf32a	refs/heads/fix/0.1.35-ajustes
````

stderr:
````text
````

Código de saída: 0

### gh workflow run windows-release.yml --repo pedroalexcarneiro/Checkpoint --ref fix/0.1.35-ajustes

Horário UTC: 2026-11-15T03:08:30.343385+00:00

stdout:
````text
````

stderr:
````text
````

Código de saída: 0

### gh run list --repo pedroalexcarneiro/Checkpoint --workflow windows-release.yml --branch fix/0.1.35-ajustes --limit 5 --json databaseId,headSha,event,status,conclusion,url,createdAt

Horário UTC: 2026-11-15T03:08:42.013257+00:00

stdout:
````text
[{"conclusion":"","createdAt":"2026-11-15T03:08:30Z","databaseId":43670989335,"event":"workflow_dispatch","headSha":"df5ff41e74b36cea4e2abd160e1172f4166bf32a","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335"}]
````

stderr:
````text
````

Código de saída: 0

### gh run view 43670989335 --repo pedroalexcarneiro/Checkpoint --json status,conclusion,headSha,jobs,url

Horário UTC: 2026-11-15T03:08:59.611354+00:00

stdout:
````text
{"conclusion":"","headSha":"df5ff41e74b36cea4e2abd160e1172f4166bf32a","jobs":[{"completedAt":"0001-01-01T00:00:00Z","conclusion":"","databaseId":132680757884,"name":"build","startedAt":"2026-11-15T03:08:33Z","status":"in_progress","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"","name":"Install tested Windows dependencies","number":5,"status":"in_progress"},{"conclusion":"","name":"Test on Windows","number":6,"status":"pending"},{"conclusion":"","name":"Build desktop and updater","number":7,"status":"pending"},{"conclusion":"","name":"Package and validate extracted executable","number":8,"status":"pending"},{"conclusion":"","name":"Render Windows interface review","number":9,"status":"pending"},{"conclusion":"","name":"Upload verified release files","number":10,"status":"pending"},{"conclusion":"","name":"Preserve Windows test report","number":11,"status":"pending"},{"conclusion":"","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"pending"},{"conclusion":"","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"pending"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335/job/132680757884"}],"status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335"}
````

stderr:
````text
````

Código de saída: 0

### gh release view v0.1.35 --repo pedroalexcarneiro/Checkpoint --json tagName,isDraft,isPrerelease,url,publishedAt,assets,body

Horário UTC: 2026-11-15T03:18:31.600949+00:00

stdout:
````text
{"assets":[{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662479","contentType":"image/png","createdAt":"2026-11-15T03:17:51Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEP","label":"","name":"Checkpoint-0.1.35-detail-overview.png","size":96516,"state":"uploaded","updatedAt":"2026-11-15T03:17:51Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-detail-overview.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662475","contentType":"image/png","createdAt":"2026-11-15T03:17:51Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEL","label":"","name":"Checkpoint-0.1.35-home.png","size":130578,"state":"uploaded","updatedAt":"2026-11-15T03:17:51Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-home.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662483","contentType":"image/png","createdAt":"2026-11-15T03:17:51Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvET","label":"","name":"Checkpoint-0.1.35-library.png","size":143770,"state":"uploaded","updatedAt":"2026-11-15T03:17:52Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-library.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662476","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-15T03:17:51Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEM","label":"","name":"Checkpoint-0.1.35-ui-review.txt","size":560,"state":"uploaded","updatedAt":"2026-11-15T03:17:51Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-ui-review.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662473","contentType":"application/zip","createdAt":"2026-11-15T03:17:51Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEJ","label":"","name":"Checkpoint-0.1.35-ui-review.zip","size":4219024,"state":"uploaded","updatedAt":"2026-11-15T03:17:52Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-ui-review.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662497","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-15T03:17:52Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEh","label":"","name":"Checkpoint-0.1.35-validation.txt","size":684,"state":"uploaded","updatedAt":"2026-11-15T03:17:52Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-validation.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662501","contentType":"application/zip","createdAt":"2026-11-15T03:17:52Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEl","label":"","name":"Checkpoint-0.1.35-windows-x64.zip","size":84209955,"state":"uploaded","updatedAt":"2026-11-15T03:17:56Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-windows-x64.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/749662500","contentType":"application/octet-stream","createdAt":"2026-11-15T03:17:52Z","downloadCount":0,"id":"RA_kwDOVpnrA84srvEk","label":"","name":"Checkpoint-0.1.35-windows-x64.zip.sha256","size":101,"state":"uploaded","updatedAt":"2026-11-15T03:17:52Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-windows-x64.zip.sha256"}],"body":"# Checkpoint 0.1.35\n\n**PRÉ-RELEASE para Windows x64.**\n\n- Jogar usa a ROM vinculada e o perfil de emulador. Encerrar o processo do emulador finaliza o registro da sessão.\n- Tempo jogado do app e da Steam somado em um total, como 2h15min, sem duplicar snapshots.\n- Desejos com cards de até 360 px, arte quadrada, mais colunas e preço de loja oficial por padrão. Opção de incluir keyshops; ausência de preço com motivo explícito.\n- Status editável na ficha: Backlog, Jogando, Pausado, Concluído e Abandonado.\n- Memórias com orientação inicial, cards alinhados e exclusão com confirmação.\n- Configurações com prévias dos nove temas, tamanho das capas destacado e prévia à direita do slider. Botões e logos de conexão ajustados.\n- Ficha exclusiva de desejos, banners sem recorte, resumo da Wikipédia e mensagens de ausência de descrição.\n- Captura de janela com Ctrl+Shift+S configurável, vinculada ao jogo iniciado pelo Checkpoint. Detecção de executáveis nas bibliotecas Steam por VDF/manifests.\n- Troca de aba por clique completo, calendário no fuso local e remoção de textos de apoio.\n\n## Pendências conhecidas\n\n- Fechar apenas a ROM, deixando o emulador aberto, ainda pode exigir encerrar o registro manualmente na aba Atividade. A detecção automática desse caso continua pendente.\n- Adicionar jogo > ROM do Drive ainda exige escolha e confirmação (A4).\n- A captura real de jogos no Windows ainda não foi validada; o primeiro uso real será no PC do dono. Testes com adaptador controlado não equivalem a essa validação.\n- Emuladores, contas reais das integrações, instalações Steam e DPI/fontes do PC do dono continuam sujeitos à validação de uso real.\n\nSchema 4 preservado. Sem alteração dos arquivos protegidos de cadastro/Drive e lifecycle. O workflow só publica após testes Windows, build e verificação do pacote extraído.\n","isDraft":false,"isPrerelease":true,"publishedAt":"2026-11-15T03:17:56Z","tagName":"v0.1.35","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.35"}
````

stderr:
````text
````

Código de saída: 0

### git ls-remote origin refs/heads/fix/0.1.35-ajustes refs/tags/v0.1.35

Horário UTC: 2026-11-15T03:18:32.168601+00:00

stdout:
````text
df5ff41e74b36cea4e2abd160e1172f4166bf32a	refs/heads/fix/0.1.35-ajustes
df5ff41e74b36cea4e2abd160e1172f4166bf32a	refs/tags/v0.1.35
````

stderr:
````text
````

Código de saída: 0

### gh release download v0.1.35 --repo pedroalexcarneiro/Checkpoint --pattern '*validation.txt' --pattern '*windows-x64.zip.sha256' --dir /workspace/work/release-0135/assets

Horário UTC: 2026-11-15T03:18:33.412392+00:00

stdout:
````text
````

stderr:
````text
````

Código de saída: 0

### gh api repos/pedroalexcarneiro/Checkpoint/releases/assets/749662501 --jq '{name: .name, size: .size, digest: .digest, state: .state, url: .browser_download_url}'

Horário UTC: 2026-11-15T03:18:44.120197+00:00

stdout:
````text
{"digest":"sha256:c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571","name":"Checkpoint-0.1.35-windows-x64.zip","size":84209955,"state":"uploaded","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.35/Checkpoint-0.1.35-windows-x64.zip"}
````

stderr:
````text
````

Código de saída: 0

### gh run view 43670989335 --repo pedroalexcarneiro/Checkpoint --json status,conclusion,headSha,jobs,url

Horário UTC: 2026-11-15T03:18:45.136078+00:00

stdout:
````text
{"conclusion":"success","headSha":"df5ff41e74b36cea4e2abd160e1172f4166bf32a","jobs":[{"completedAt":"2026-11-15T03:17:34Z","conclusion":"success","databaseId":132680757884,"name":"build","startedAt":"2026-11-15T03:08:33Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"success","name":"Test on Windows","number":6,"status":"completed"},{"conclusion":"success","name":"Build desktop and updater","number":7,"status":"completed"},{"conclusion":"success","name":"Package and validate extracted executable","number":8,"status":"completed"},{"conclusion":"success","name":"Render Windows interface review","number":9,"status":"completed"},{"conclusion":"success","name":"Upload verified release files","number":10,"status":"completed"},{"conclusion":"success","name":"Preserve Windows test report","number":11,"status":"completed"},{"conclusion":"success","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"completed"},{"conclusion":"success","name":"Complete job","number":23,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335/job/132680757884"},{"completedAt":"2026-11-15T03:17:59Z","conclusion":"success","databaseId":132682920713,"name":"publish","startedAt":"2026-11-15T03:17:36Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093","number":3,"status":"completed"},{"conclusion":"success","name":"Publish development release","number":4,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":8,"status":"completed"},{"conclusion":"success","name":"Complete job","number":9,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335/job/132682920713"}],"status":"completed","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335"}
````

stderr:
````text
````

Código de saída: 0

### /workspace/work/venv/bin/python -c 'from pathlib import Path; root=Path("/workspace/work/release-0135/assets"); print((root/"Checkpoint-0.1.35-validation.txt").read_text(encoding="utf-8")); print((root/"Checkpoint-0.1.35-windows-x64.zip.sha256").read_text(encoding="utf-8"))'

Horário UTC: 2026-11-15T03:18:45.222627+00:00

stdout:
````text
Checkpoint 0.1.35 · Windows x64
Commit: df5ff41e74b36cea4e2abd160e1172f4166bf32a
Python: 3.12.10
Testes: {'tests': 542, 'failures': 0, 'errors': 0, 'skipped': 0}
Smoke do fonte: 6 páginas; SQLite íntegro; biblioteca vazia.
Smoke do ZIP extraído: 6 páginas; SQLite íntegro; biblioteca vazia.
Auxiliar isolado do fonte e do ZIP extraído: resposta e schema verificados.
Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
CheckpointUpdater.exe --check: saída 0.
ZIP SHA-256: c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571
Steam autenticada e homologação Windows 10/11 pessoal não estão cobertas.

c006662506343dfd5c102e075e3faa13927db7df359177796a7461b18cadc571  Checkpoint-0.1.35-windows-x64.zip

````

stderr:
````text
````

Código de saída: 0

Logs integrais adicionais do workflow: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43670989335. Baixados também para windows-run.stdout.log no diretório local de evidências /workspace/work/release-0135, sem perda de linhas. Consultas periódicas de acompanhamento em monitor.jsonl.

PRÉ-RELEASE 0.1.35 PUBLICADA

# Preparação do lançamento 0.1.35

O dono autorizou: “ok, podemos lancar a versao 1.35”. Versão correspondente à branch e série atual: 0.1.35. Autorização cobre o push de preparação e a execução do workflow Windows release, que cria tag e pré-release somente após testes/build/smokes. Não alterar releases protegidas, não criar PR e não usar force.

Base: f0a5514825b05d0f41aa129cdd5f0e65546a2d7c, branch fix/0.1.35-ajustes, checkout inicialmente limpo e remoto igual. v0.1.35 ausente na consulta inicial. Atualizados pyproject.toml, checkpoint/__init__.py, notas de release e documentação. Schema 4 preservado.

Dependência de portabilidade: a nova prova de fuso usa ZoneInfo. Windows não fornece a base IANA; faltava tzdata nas dependências de teste. Reproduzido em Linux com PYTHONTZPATH vazio (dois jogos), sem alterar asserções. Adicionado tzdata==2026.6 em requirements-tested.txt e repetida a mesma prova sem base do sistema. PYTHONTZPATH vazio aplicou-se às duas execuções do módulo test_dates_0135.py abaixo. Nenhum teste nem workflow foi alterado.

Pendências públicas nas notas: A4 e encerramento interno de ROM; captura real de jogos no Windows e uso no PC do dono permanecem não validados. O runner Windows valida testes, build e pacote extraído, não essa homologação pessoal. Resultado definitivo da publicação deve ser conferido no Actions e nos arquivos validation.txt/SHA-256 anexados à release.

## Comandos de preparação — saídas integrais

### /workspace/work/venv/bin/python -c 'import tomllib; from pathlib import Path; from checkpoint import __version__; from checkpoint.database import MIGRATIONS; assert tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]["version"] == __version__ == "0.1.35"; assert len(MIGRATIONS)==4; print("Versão 0.1.35 consistente; schema 4 preservado.")'

Horário UTC: 2026-11-15T03:05:13.180560+00:00

stdout:
```text
Versão 0.1.35 consistente; schema 4 preservado.
```

stderr:
```text
```

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_updates.py tests/test_visual_0132.py tests/test_save_lifecycle.py -q -p no:cacheprovider

Horário UTC: 2026-11-15T03:05:33.326520+00:00

stdout:
```text
.............................................................            [100%]
61 passed in 19.78s
```

stderr:
```text
```

Código de saída: 0

### /workspace/work/venv/bin/python -m pip index versions tzdata

Horário UTC: 2026-11-15T03:06:25.742162+00:00

stdout:
```text
tzdata (2026.6)
Available versions: 2026.6, 2026.5, 2026.4, 2026.3, 2026.2, 2026.1, 2025.3, 2025.2, 2025.1, 2024.2, 2024.1, 2023.4, 2023.3, 2023.2, 2023.1, 2022.7, 2022.6, 2022.5, 2022.4, 2022.3, 2022.2, 2022.1, 2021.5, 2021.4, 2021.3, 2021.2.post0, 2021.2, 2021.1, 2020.5, 2020.4, 2020.3, 2020.2, 2020.1
```

stderr:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip
```

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py -q -p no:cacheprovider --tb=short

Horário UTC: 2026-11-15T03:06:26.252597+00:00

stdout:
```text
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
```

stderr:
```text
```

Código de saída: 1

### /workspace/work/venv/bin/python -m pip install tzdata==2026.6

Horário UTC: 2026-11-15T03:06:39.808791+00:00

stdout:
```text
Collecting tzdata==2026.6
  Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata
Successfully installed tzdata-2026.6
```

stderr:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.

[notice] A new release of pip is available: 25.0.1 -> 26.3
[notice] To update, run: /workspace/work/venv/bin/python -m pip install --upgrade pip
```

Código de saída: 0

### /workspace/work/venv/bin/python -m pytest tests/test_dates_0135.py -q -p no:cacheprovider --tb=short

Horário UTC: 2026-11-15T03:06:40.166119+00:00

stdout:
```text
..                                                                       [100%]
2 passed in 0.04s
```

stderr:
```text
```

Código de saída: 0

### /workspace/work/venv/bin/python -m pip check

Horário UTC: 2026-11-15T03:06:40.445031+00:00

stdout:
```text
No broken requirements found.
```

stderr:
```text
WARNING: The directory '/home/agent/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
```

Código de saída: 0

### git diff --check

Horário UTC: 2026-11-15T03:06:40.474029+00:00

stdout:
```text
```

stderr:
```text
```

Código de saída: 0

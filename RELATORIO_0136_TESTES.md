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

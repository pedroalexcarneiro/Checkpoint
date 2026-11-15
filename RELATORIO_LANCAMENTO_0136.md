# Lançamento Checkpoint 0.1.36 — em andamento

Autorização explícita do dono recebida nesta conversa para lançar no GitHub. Padrão mantido: pré-release Windows x64, pelo workflow existente Windows release, sem modificar workflows nem tags/releases anteriores.

Base local recebida: 67f4800540fc43be4fe2ee8e8976814c5a677db3 (documentação); código validado: da12842e6de663ee4791a6a4010bc622cfed8222, 612 testes Linux. Checkout inicial limpo; versão declarada 0.1.36, schema 4. Remoto fix/0.1.35-ajustes continua 818ec80a492a29936782ddb3a43eecaf3ef996e3; tag v0.1.36 e branch remota fix/0.1.36-ajustes inexistentes na consulta inicial.

Preparação altera somente documentação/notas públicas. A etapa Windows testa e constrói o commit enviado; validação no runner não comprova captura real, conta autenticada ou homologação no PC do dono. Limitações 02/03/06, A4 e ROM descarregada com emulador vivo preservadas nas notas.

Saídas integrais dos comandos de lançamento serão acrescentadas abaixo. Nenhuma credencial é registrada.

## verificacao-pre-push

UTC: 2026-11-15T17:43:22.875975+00:00

Comando: `["/workspace/work/venv/bin/python", "-c", "import subprocess;from pathlib import Path;import tomllib;from checkpoint import __version__;assert __version__=='0.1.36'==tomllib.loads(Path('pyproject.toml').read_text(encoding='utf-8'))['project']['version'];base='67f4800540fc43be4fe2ee8e8976814c5a677db3';names=subprocess.check_output(['git','diff','--name-only',base],text=True,encoding='utf-8').splitlines();assert not any(n.startswith(('checkpoint/','tests/','scripts/','.github/workflows/')) or n in ('requirements-tested.txt','pyproject.toml') for n in names);[(Path(n).read_text(encoding='utf-8'),None if b'\\r' not in Path(n).read_bytes() else (_ for _ in ()).throw(AssertionError(n))) for n in names];subprocess.run(['git','diff','--check'],check=True);print('Versão/schema confirmados; código/testes/workflows/scripts/dependências inalterados desde entrega validada.');print('Arquivos de preparação:',names)"]`

stdout integral:
```text
Versão/schema confirmados; código/testes/workflows/scripts/dependências inalterados desde entrega validada.
Arquivos de preparação: ['.github/release-notes.md', 'CHANGELOG.md', 'CONTINUITY.md', 'PROJECT_STATUS.md']

```

stderr integral:
```text

```

Código de saída: 0

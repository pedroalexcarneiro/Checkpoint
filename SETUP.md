# Instalação e execução

## Requisitos

Windows 10/11, Python 3.12 de 64 bits. Para desenvolver: Git e dependências de `requirements-tested.txt`. Linux permite testes Qt offscreen, mas não valida o executável Windows.

## Instalar e executar

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-tested.txt
.venv\Scripts\python -m pip install --no-deps --no-build-isolation -e .
.venv\Scripts\python run_checkpoint.py
```

## Build no Windows

```powershell
./scripts/build.ps1 -Python .venv\Scripts\python.exe
```

O build gera Checkpoint e seu auxiliar de atualização. Publicação é uma ação separada; esta revisão não publica releases. Use os scripts de validação somente com pastas de teste novas.

## Dados e recuperação

Padrão: `%LOCALAPPDATA%\Checkpoint`, banco `checkpoint.sqlite`, schema 4. `--data-dir CAMINHO` seleciona outra pasta e não consulta a pasta padrão. Mantenha dados fora da instalação.

A primeira abertura copia o diretório anterior quando o novo ainda não existe, produz um snapshot SQLite pela API de backup e verifica sua integridade. Preserva a origem, preferências, imagens, arquivos e credenciais antigas; credenciais são copiadas apenas entre serviços do cofre. Exportações de segredos não são copiadas para arquivos. Preferências antigas de aparência são normalizadas para Verde quando necessário.

Falhas interrompem a abertura e mostram o caminho original para recuperação. Não apague a pasta antiga nem abra duas versões simultaneamente. Uma pasta nova já existente não é sobrescrita. Backups de saves continuam compatíveis com manifestos anteriores.

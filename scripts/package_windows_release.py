"""Cria ZIP Windows e só o libera após smoke do conteúdo efetivamente extraído."""
import argparse
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import platform
import sqlite3
import subprocess
import sys
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET
import zipfile

from checkpoint import __version__
from checkpoint.database import MIGRATIONS
from checkpoint.update_installer import extract_package
from checkpoint.updates import MAX_DOWNLOAD


def smoke(command, directory):
    subprocess.run([*command, '--smoke-test', '--data-dir', str(directory)],
                   check=True, timeout=90, env={**os.environ, 'QT_QPA_PLATFORM': 'offscreen'})
    screenshot = directory / 'smoke-home.png'
    if not screenshot.is_file() or screenshot.read_bytes()[:8] != b'\x89PNG\r\n\x1a\n':
        raise RuntimeError('Smoke não gerou uma captura PNG válida.')
    with closing(sqlite3.connect((directory / 'checkpoint.sqlite').as_uri() + '?mode=ro', uri=True)) as sql:
        if sql.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise RuntimeError('Integridade SQLite falhou.')
        if sql.execute('PRAGMA user_version').fetchone()[0] != len(MIGRATIONS):
            raise RuntimeError('Schema incorreto no smoke.')
        if sql.execute('SELECT count(*) FROM games').fetchone()[0] != 0:
            raise RuntimeError('Smoke deve começar com biblioteca vazia.')
    request=directory/'worker-request.json'
    response=directory/'worker-response.json'
    request.write_text(json.dumps({'operation':'ping','database':str(directory/'checkpoint.sqlite'),
                                  'response':str(response),'arguments':{}}),encoding='utf-8')
    subprocess.run([*command,'--worker-request',str(request)],check=True,timeout=30)
    if json.loads(response.read_text(encoding='utf-8')) != {'ok':True,'result':{'worker':'ok','schema':len(MIGRATIONS)}}:
        raise RuntimeError('Auxiliar isolado do pacote não respondeu corretamente.')



def save_smoke(command,directory):
    subprocess.run([*command,'--save-smoke-test','--data-dir',str(directory)],
                   check=True,timeout=60,env={**os.environ,'QT_QPA_PLATFORM':'offscreen'})
    if not (directory/'save-smoke.png').is_file():
        raise RuntimeError('Cadastro completo não gerou captura.')
    with closing(sqlite3.connect(directory/'checkpoint.sqlite')) as sql:
        if sql.execute('PRAGMA integrity_check').fetchone()[0]!='ok' or sql.execute('SELECT count(*) FROM games').fetchone()[0]!=1:
            raise RuntimeError('Cadastro completo não preservou a fixture isolada.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-report', type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != 'win32' or platform.machine().lower() not in {'amd64', 'x86_64'}:
        raise RuntimeError('Este pacote deve ser gerado e validado em Windows x64.')
    root = Path(__file__).resolve().parents[1]
    os.chdir(root)
    suites = list(ET.parse(args.test_report).getroot().iter('testsuite'))
    counts = {key: sum(int(suite.get(key, 0)) for suite in suites)
              for key in ('tests', 'failures', 'errors', 'skipped')}
    if counts['tests'] == 0 or counts['failures'] or counts['errors'] or counts['tests'] == counts['skipped']:
        raise RuntimeError('O relatório não comprova execução de testes Windows com sucesso.')
    portable = root / 'dist' / 'Checkpoint'
    for required in ('Checkpoint.exe', '_internal', 'CheckpointUpdater/CheckpointUpdater.exe', 'LEIA-ME.txt'):
        if not (portable / required).exists():
            raise RuntimeError(f'Componente ausente: {required}')
    output = root / 'release-assets'
    output.mkdir(exist_ok=True)
    archive_path = output / f'Checkpoint-{__version__}-windows-x64.zip'
    with zipfile.ZipFile(archive_path, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(portable.rglob('*')):
            if path.is_symlink():
                raise RuntimeError('Links não são permitidos no pacote.')
            if path.is_file():
                archive.write(path, path.relative_to(portable.parent).as_posix())
    with zipfile.ZipFile(archive_path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError('ZIP com CRC inválido.')
    if archive_path.stat().st_size > MAX_DOWNLOAD:
        raise RuntimeError('ZIP excede o limite aceito pelo atualizador.')
    with TemporaryDirectory(prefix='checkpoint-release-') as temporary:
        temporary = Path(temporary).resolve()
        smoke([sys.executable, '-m', 'checkpoint.app'], temporary / 'source-smoke')
        save_smoke([sys.executable, '-m', 'checkpoint.app'], temporary / 'source-save-smoke')
        extracted = extract_package(archive_path, temporary / 'extracted')
        smoke([str(extracted / 'Checkpoint.exe')], temporary / 'portable-smoke')
        save_smoke([str(extracted / 'Checkpoint.exe')], temporary / 'portable-save-smoke')
        subprocess.run([str(extracted / 'CheckpointUpdater' / 'CheckpointUpdater.exe'), '--check'],
                       check=True, timeout=30)
    with archive_path.open('rb') as source:
        digest = hashlib.file_digest(source, 'sha256').hexdigest()
    (output / (archive_path.name + '.sha256')).write_text(f'{digest}  {archive_path.name}\n', encoding='utf-8')
    evidence = [
        f'Checkpoint {__version__} · Windows x64',
        f'Commit: {os.environ.get("GITHUB_SHA", "local")}',
        f'Python: {platform.python_version()}',
        f'Testes: {counts}',
        'Smoke do fonte: 6 páginas; SQLite íntegro; biblioteca vazia.',
        'Smoke do ZIP extraído: 6 páginas; SQLite íntegro; biblioteca vazia.',
        'Auxiliar isolado do fonte e do ZIP extraído: resposta e schema verificados.',
        'Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).',
        'CheckpointUpdater.exe --check: saída 0.',
        f'ZIP SHA-256: {digest}',
        'Steam autenticada e homologação Windows 10/11 pessoal não estão cobertas.',
    ]
    (output / f'Checkpoint-{__version__}-validation.txt').write_text('\n'.join(evidence) + '\n', encoding='utf-8')
    print('\n'.join(evidence))


if __name__ == '__main__':
    main()

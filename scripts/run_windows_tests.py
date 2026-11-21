"""Executa toda a suíte em processos Qt independentes e reúne os resultados JUnit."""
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET


def main():
    root = Path(__file__).resolve().parents[1]
    paths = sorted(set((root / 'tests').rglob('test_*.py')) | set((root / 'tests').rglob('*_test.py')))
    if not paths:
        raise RuntimeError('Nenhum teste encontrado.')

    batches = []
    batch = []
    for path in paths:
        # Este módulo testa encerramento de janelas e processos de propósito.
        # Mantenha o QApplication dos demais testes fora desse ciclo de vida.
        if path.name == 'test_isolated_operations.py':
            if batch:
                batches.append(batch)
                batch = []
            batches.append([path])
        else:
            batch.append(path)
            if len(batch) == 30:
                batches.append(batch)
                batch = []
    if batch:
        batches.append(batch)

    result = ET.Element('testsuites')
    failed = False
    with TemporaryDirectory(prefix='checkpoint-windows-tests-') as temporary:
        for number, batch in enumerate(batches, 1):
            report = Path(temporary) / f'pytest-{number}.xml'
            print(f'Testes Windows — lote {number} ({len(batch)} arquivos)', flush=True)
            command = [sys.executable, '-X', 'faulthandler', '-m', 'pytest', '-q',
                       '-p', 'no:cacheprovider', f'--junitxml={report}',
                       *(str(path.relative_to(root)) for path in batch)]
            process = subprocess.run(command, cwd=root)
            if process.returncode or not report.is_file():
                print(f'Lote {number} terminou com código {process.returncode}.', flush=True)
                failed = True
            if report.is_file():
                result.extend(ET.parse(report).getroot().iter('testsuite'))

    output = root / '.ci-results' / 'pytest.xml'
    output.parent.mkdir(exist_ok=True)
    ET.ElementTree(result).write(output, encoding='utf-8', xml_declaration=True)
    print(f'{sum(int(suite.get("tests", 0)) for suite in result)} testes registrados em {output.name}.')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())

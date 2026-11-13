"""Captura a ficha após busca/seleção/salvamento por cliques, com fonte falsa.

Uso: QT_QPA_PLATFORM=offscreen python scripts/render_search_flow_review.py /tmp/prova-nova
Não reutiliza banco, não consulta cofre/rede, não preenche o cadastro diretamente.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication

from checkpoint.database import Database
from checkpoint.library import Library
from search_flow_support import METROID, save_via_search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    root = args.output.resolve()
    if root.exists():
        raise SystemExit('Use um diretório novo: evidências existentes preservadas.')
    repository = Path(__file__).resolve().parents[1]
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repository, text=True).strip()
    dirty = bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=repository, text=True).strip())
    if dirty:
        raise SystemExit('Registre o código antes de capturar, para identificar o commit exato.')
    root.mkdir(parents=True)
    app = QApplication.instance() or QApplication([])
    app.setStyle('Fusion')
    records = []
    for width, height in [(1280, 800), (1920, 1080)]:
        with TemporaryDirectory(prefix='search-flow-', dir=root) as temporary:
            data = Path(temporary)
            db = Database(data / 'review.sqlite')
            try:
                library = Library(db)
                window, game = save_via_search(app, library, data / 'source', size=(width, height))
                try:
                    for field in ('developer', 'publisher', 'description'):
                        assert game[field] == METROID[field], field
                    assert game['source'] == 'Busca'
                    for kind in ('cover', 'banner'):
                        assert Path(game[kind]).is_file() and not QImage(game[kind]).isNull()
                    name = f'real-flow-{width}x{height}-detail.png'
                    assert window.grab().save(str(root / name))
                    image = QImage(str(root / name))
                    assert (image.width(), image.height()) == (width, height)
                    records.append(dict(file=name, commit=commit, dirty=dirty,
                        width=width, height=height, bytes=(root / name).stat().st_size,
                        sha256=hashlib.sha256((root / name).read_bytes()).hexdigest(),
                        saved={key: game[key] for key in ('title', 'developer', 'publisher', 'description', 'source')},
                        images_on_disk=True))
                finally:
                    window.close()
                    app.processEvents()
            finally:
                db.close()
    (root / 'real-flow-info.json').write_text(json.dumps(dict(
        environment='Linux / Qt offscreen, não Windows',
        flow='Clique Adicionar, digitação, pesquisa real no auxiliar com fonte falsa, clique no resultado, clique Salvar durante detalhes pendentes; espera filas.',
        fixtures='Somente fornecedores e transporte de imagens controlados; nenhum cadastro manual. Imagens identificadas como fonte controlada.',
        captures=records), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for record in records:
        print(record['file'], record['commit'], record['bytes'])


if __name__ == '__main__':
    main()

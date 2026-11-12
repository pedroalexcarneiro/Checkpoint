"""Publica somente PNGs e índice local; nenhuma base, log ou credencial."""
from pathlib import Path
import html
import hashlib
import os
import sys
import zipfile
from gamevault import __version__

source=Path(sys.argv[1]);output=Path(sys.argv[2]);output.mkdir(parents=True,exist_ok=True)
images=sorted(path for path in source.glob('*.png') if not path.stem[0].isdigit())
if len(images)<30:raise SystemExit('Revisão visual incompleta: são esperadas pelo menos 30 capturas.')
page='''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Checkpoint · Revisão da interface</title><style>body{margin:32px;background:#14171b;color:#e8eaed;font:16px system-ui}main{max-width:1440px;margin:auto}p{max-width:900px;color:#b3bdc4;line-height:1.6}nav{display:flex;gap:10px;flex-wrap:wrap;margin:30px 0}a{color:#a1d38e}section{margin:40px 0}img{max-width:100%;border:1px solid #343c43;border-radius:12px}h2{font-size:21px}</style><main><h1>Checkpoint · Interface Windows</h1><p>Capturas do aplicativo real em Qt offscreen no Windows. Jogos, sessões e artes são fixtures locais de teste. Não representam uma biblioteca pessoal, conexão autenticada ou imagens obtidas de provedores. A avaliação estética é distinta dos testes funcionais.</p>'''
page+='<nav>'+''.join(f'<a href="#{html.escape(path.stem)}">{html.escape(path.stem)}</a>' for path in images)+'</nav>'
page+=''.join(f'<section id="{html.escape(path.stem)}"><h2>{html.escape(path.stem)}</h2><img loading="lazy" src="{html.escape(path.name)}" alt="Captura {html.escape(path.stem)}"></section>' for path in images)+'</main></html>'
with zipfile.ZipFile(output/f'Checkpoint-{__version__}-ui-review.zip','w',zipfile.ZIP_DEFLATED) as archive:
    archive.writestr('index.html',page)
    for path in images:archive.write(path,path.name)
for name in ('home','library','detail-overview'):
    (output/f'Checkpoint-{__version__}-{name}.png').write_bytes((source/(name+'.png')).read_bytes())
print(f'Revisão visual: {len(images)} PNGs e índice HTML; bases e logs excluídos.')

review=output/f'Checkpoint-{__version__}-ui-review.zip'
report=[f'Checkpoint {__version__} · Revisão visual',f'Plataforma: {sys.platform}',f'Commit: {os.environ.get("GITHUB_SHA","local")}',f'Capturas Qt: {len(images)}', 'Janelas: 1440x960 e 1000x700; editor, cadastro e diálogos em suas dimensões próprias.', 'Temas: verde, roxo e branco; demais cores disponíveis no seletor.', 'Fixtures isoladas: jogos, sessões, metas e artes. Nenhuma conta autenticada.', 'Conteúdo publicado: capturas PNG e index.html. Base, logs e artes auxiliares excluídos.',f'SHA-256 ui-review.zip: {hashlib.sha256(review.read_bytes()).hexdigest()}']
(output/f'Checkpoint-{__version__}-ui-review.txt').write_text('\n'.join(report)+'\n',encoding='utf-8')

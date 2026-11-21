"""Medição isolada com volume, imagem grande e eventos; nunca abre dados pessoais."""
import argparse
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import time

from PySide6.QtCore import QCoreApplication, QEvent, QTimer
from PySide6.QtGui import QColor, QImage, QPainter, QLinearGradient
from PySide6.QtWidgets import QApplication

from checkpoint.database import Database
from checkpoint.library import Library
from checkpoint.window import MainWindow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--images', type=int, default=96)
    args = parser.parse_args()
    root = args.directory.resolve()
    root.mkdir(parents=True, exist_ok=False)
    app = QApplication.instance() or QApplication([])
    app.setQuitOnLastWindowClosed(False)
    db = Database(root/'benchmark.sqlite')
    library = Library(db)
    library.set_setting('artwork.auto', False)
    library.set_setting('prices.auto', False)
    from checkpoint.credentials import CredentialVault
    CredentialVault.get = lambda *args: None
    games = [library.save_game({'title': name, 'platform': 'PC'})
             for name in ('Volume A — teste isolado', 'Volume B — teste isolado')]
    sources = []
    for width, height in ((1920, 1080), (3840, 2160)):
        image = QImage(width, height, QImage.Format_RGB32)
        painter = QPainter(image)
        gradient = QLinearGradient(0, 0, width, height)
        gradient.setColorAt(0, QColor('#182838'))
        gradient.setColorAt(1, QColor('#8e734e'))
        painter.fillRect(image.rect(), gradient)
        for n in range(160):
            painter.setPen(QColor.fromHsv(n*11 % 360, 170, 210))
            painter.drawLine(n*29 % width, 0, n*59 % width, height)
        painter.end()
        path = root/f'source-{width}.png'
        assert image.save(str(path))
        sources.append(path)
    for n in range(args.images):
        path = root/f'captura-{n:04}.png'
        shutil.copyfile(sources[1 if n % 12 == 0 else 0], path)
        library.add_media(games[n % 2], path, f'Captura sintética {n}')
    for n in range(12):
        library.add_diary(games[n % 2], f'Anotação isolada {n}')
    for n in range(4):
        path = root/f'invalido-{n}.png'
        path.write_bytes(b'not an image')
        library.add_media(games[n % 2], path, 'Mídia inválida de teste')
    for n in range(4):
        path = root/f'video-{n}.mp4'
        path.write_bytes(b'unsupported fixture')
        library.add_media(games[n % 2], path, 'Vídeo inválido de teste')

    window = MainWindow(library)
    window.resize(1920, 1080)
    window.show()
    for _ in range(6): app.processEvents()
    readings = []
    last_tick = time.perf_counter()
    gaps = []
    def tick():
        nonlocal last_tick
        current = time.perf_counter()
        gaps.append(current-last_tick)
        last_tick = current
    pulse = QTimer()
    pulse.setInterval(10)
    pulse.timeout.connect(tick)
    pulse.start()
    for run in range(3):
        if run:
            window.navigate(2)
            for _ in range(4): app.processEvents()
            QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        last_tick = time.perf_counter()
        cpu = time.process_time()
        started = time.perf_counter()
        window.navigate(3)
        navigation = time.perf_counter()-started
        for _ in range(8): app.processEvents()
        readings.append({'run': run, 'navigate_seconds': navigation,
                         'first_events_seconds': time.perf_counter()-started,
                         'cpu_seconds': time.process_time()-cpu,
                         'max_event_gap_seconds': max(gaps, default=0)})
        gaps.clear()
    pulse.stop()
    window.close()
    window.deleteLater()
    QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = {'platform': platform.platform(), 'python': platform.python_version(),
              'qt_platform': os.environ.get('QT_QPA_PLATFORM'), 'fixtures': True,
              'images': args.images, 'large_images': (args.images+11)//12,
              'invalid_images': 4, 'invalid_videos': 4, 'notes': 12,
              'size': [1920, 1080], 'runs': readings,
              'peak_rss_kib_linux': peak}
    db.close()
    (root/'measurements.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__': main()

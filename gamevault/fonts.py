"""Fontes Windows explícitas, inclusive no Qt offscreen do build e dos testes."""
import os
import sys
from pathlib import Path
from PySide6.QtGui import QFont,QFontDatabase,QRawFont


def install_fonts(application):
    if sys.platform=='win32':
        directory=Path(os.environ.get('WINDIR',r'C:\Windows'))/'Fonts'
        for name in ('segoeui.ttf','segoeuib.ttf','seguisb.ttf','segoeuil.ttf'):
            path=directory/name
            if path.is_file():QFontDatabase.addApplicationFont(str(path))
        application.setFont(QFont('Segoe UI',10))


def verify_text_font():
    raw=QRawFont.fromFont(QFont('Segoe UI',12))
    return raw.isValid() and all(raw.glyphIndexesForString('Checkpoint Início Configurações'))

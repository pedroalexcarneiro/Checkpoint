import os
os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
import shutil
from pathlib import Path
from uuid import uuid4
import pytest
from gamevault.database import Database
from gamevault.library import Library

@pytest.fixture
def folder():
    # tempfile cria diretórios sem acesso neste host; mkdir usa ACL herdada.
    path=Path(os.environ.get('GAMEVAULT_TEST_ROOT','.test-data'))/uuid4().hex
    path.mkdir(parents=True)
    yield path
    resolved=path.resolve()
    assert Path(os.environ.get('GAMEVAULT_TEST_ROOT','.test-data')).resolve() in resolved.parents
    shutil.rmtree(resolved)

@pytest.fixture
def library(folder):
    db=Database(folder/'library.sqlite')
    yield Library(db)
    db.close()


@pytest.fixture(scope='session')
def app():
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QFontDatabase
    from gamevault.theme import DARK
    application=QApplication.instance() or QApplication([])
    font=Path('C:/Windows/Fonts/segoeui.ttf')
    if font.exists(): QFontDatabase.addApplicationFont(str(font))
    application.setStyle('Fusion'); application.setStyleSheet(DARK)
    yield application

import os
os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
import shutil
from pathlib import Path
from uuid import uuid4
import pytest
from checkpoint.database import Database
from checkpoint.library import Library

@pytest.fixture
def folder():
    # tempfile cria diretórios sem acesso neste host; mkdir usa ACL herdada.
    path=Path(os.environ.get('CHECKPOINT_TEST_ROOT','.test-data'))/uuid4().hex
    path.mkdir(parents=True)
    yield path
    resolved=path.resolve()
    assert Path(os.environ.get('CHECKPOINT_TEST_ROOT','.test-data')).resolve() in resolved.parents
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
    from checkpoint.theme import DARK
    application=QApplication.instance() or QApplication([])
    font=Path('C:/Windows/Fonts/segoeui.ttf')
    if font.exists(): QFontDatabase.addApplicationFont(str(font))
    application.setStyle('Fusion'); application.setStyleSheet(DARK)
    yield application

@pytest.hookimpl(wrapper=True)
def pytest_runtest_protocol(item, nextitem):
    if not item.nodeid.startswith('tests/test_labels_0137.py::test_not_started_label'):
        return (yield)
    import sys
    filenames = {'test_bugs_0134.py', 'test_labels_0137.py', 'window.py', 'home_view.py',
                 'detail_view.py', 'design_system.py', 'global_hotkey.py',
                 'controller_capture.py', 'library.py', 'transfers.py'}

    def trace(frame, event, arg):
        filename = frame.f_code.co_filename.rsplit('\\', 1)[-1]
        if filename not in filenames:
            return None
        if event == 'line':
            os.write(2, f"{filename}:{frame.f_lineno} {frame.f_code.co_name}\n".encode())
        return trace

    sys.settrace(trace)
    try:
        return (yield)
    finally:
        sys.settrace(None)

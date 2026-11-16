"""O renderizador deve liberar o atalho antes de criar a janela vazia."""
import os
from pathlib import Path
import subprocess
import sys


def test_review_releases_global_shortcut_between_windows(folder):
    code = r'''
import runpy
import sys
from checkpoint.dialog_style import AppMessages as QMessageBox
import checkpoint.global_hotkey as hotkey
from checkpoint.credentials import CredentialVault

class ExclusiveApi:
    active = {}
    registrations = 0
    def register(self, identity, modifiers, key):
        if identity in self.active or (modifiers, key) in self.active.values():
            return False
        self.active[identity] = (modifiers, key)
        self.registrations += 1
        return True
    def unregister(self, identity):
        return self.active.pop(identity, None) is not None

api = ExclusiveApi()
original_init = hotkey.GlobalCaptureHotkey.__init__
def exclusive_init(self, window, callback, sequence, **kwargs):
    original_init(self, window, callback, sequence, api=api)
hotkey.GlobalCaptureHotkey.__init__ = exclusive_init
CredentialVault.get = lambda *args: None
def unexpected_warning(*args):
    raise RuntimeError('Revisão bloqueada por aviso modal: ' + str(args[-1]))
QMessageBox.warning = unexpected_warning
sys.argv = ['scripts/render_ui_review.py', sys.argv[1]]
runpy.run_path(sys.argv[0], run_name='__main__')
assert api.registrations == 2, api.registrations
assert api.active == {}, api.active
'''
    output = folder / 'review'
    result = subprocess.run(
        [sys.executable, '-c', code, str(output)],
        cwd=Path(__file__).resolve().parents[1],
        env={**os.environ, 'QT_QPA_PLATFORM': 'offscreen'},
        capture_output=True, text=True, encoding='utf-8', errors='replace',
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert len(list(output.glob('*.png'))) >= 30
    for name in ('home', 'library', 'empty-home', 'empty-wishlist',
                 'empty-memories', 'empty-statistics'):
        assert (output / (name + '.png')).is_file()

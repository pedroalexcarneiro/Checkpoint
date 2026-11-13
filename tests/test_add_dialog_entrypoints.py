"""O sinal clicked(bool) não pode ser interpretado como arquivo do Drive."""
from PySide6.QtCore import Qt, QTimer
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QPushButton
from checkpoint.dialogs import GameDialog
from checkpoint.window import MainWindow


def test_wishlist_add_keeps_button_signal_separate_from_drive_file(app, library, monkeypatch):
    monkeypatch.setattr('checkpoint.credentials.CredentialVault.get', lambda *args: None)
    library.set_setting('prices.auto', False)
    window = MainWindow(library)
    window.show(); window.navigate(2); app.processEvents()
    opened = []
    def close_dialog():
        dialog = app.activeModalWidget()
        if isinstance(dialog, GameDialog):
            opened.append(dialog)
            dialog.reject()
    try:
        button = next(button for button in window.findChildren(QPushButton)
                      if button.isVisible() and button.text() == 'Adicionar desejo')
        QTimer.singleShot(0, close_dialog)
        QTest.mouseClick(button, Qt.LeftButton); app.processEvents()
        assert len(opened) == 1
        assert opened[0].drive_file_id is None
        assert opened[0].purpose == 'wish'
    finally:
        window.close(); app.processEvents()

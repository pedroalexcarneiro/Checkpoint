"""Redimensionar um modal não deve desfazer a posição escolhida pelo usuário."""
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QDialog
from checkpoint.dialog_style import prepare_dialog
from test_bugs_0134 import ui, sample


def test_resize_and_reopen_preserve_explicit_dialog_position(ui, app):
    window, identity = ui
    dialog = prepare_dialog(QDialog(window))
    dialog.resize(420, 280)
    dialog.show()
    for _ in range(5): app.processEvents()
    try:
        dialog.move(40, 60)
        chosen = QPoint(dialog.pos())
        for width, height in [(460, 310), (430, 290), (500, 340)]:
            dialog.resize(width, height)
            for _ in range(5): app.processEvents()
            assert dialog.pos() == chosen
            assert dialog.width() <= dialog.screen().availableGeometry().width()-32
        dialog.hide()
        dialog.show()
        for _ in range(5): app.processEvents()
        assert dialog.pos() == chosen
    finally:
        dialog.reject()
        dialog.deleteLater()

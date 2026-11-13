from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
from checkpoint.dialogs import GameDialog
from checkpoint.integrations import MetadataResult
from checkpoint.window_style import DialogTitleBar

def test_add_dialog_has_one_internal_close_and_no_local_automation_option(library,app):
    dialog=GameDialog(library=library);dialog.show();app.processEvents();quick=dialog.quick_add
    assert dialog.windowFlags() & Qt.FramelessWindowHint
    assert dialog.findChild(DialogTitleBar) is not None
    assert len([b for b in dialog.findChildren(QPushButton) if b.accessibleName()=='Fechar'])==1
    assert not any(b.text()=='Ajustar detalhes' and b.isVisible() for b in dialog.findChildren(QPushButton))
    assert dialog.complete_on_save.isHidden() and quick.query.isClearButtonEnabled()
    assert not quick.save.isEnabled()
    quick.advanced.setChecked(True);app.processEvents()
    assert quick.platform.width()>=220 and quick.platform.height()>=40
    assert quick.platform.fontMetrics().horizontalAdvance('Todas as plataformas')+40<=quick.platform.width()
    result=MetadataResult('rawg','7','Example',developer='Estúdio')
    dialog.apply_catalog(result);quick.show_result(result)
    assert quick.save.isEnabled() and quick.confirmed.isVisible()
    dialog.reject()

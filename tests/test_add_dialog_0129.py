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


def test_advanced_options_leave_preview_and_actions_in_order(library,app):
    from PySide6.QtWidgets import QScrollArea
    dialog=GameDialog(library=library)
    assert dialog.height()==min(700,dialog.screen().availableGeometry().height())
    dialog.resize(680,600);dialog.show()
    quick=dialog.quick_add
    try:
        quick.state.setText('Resultado selecionado com ficha incompleta. Pesquise manualmente.')
        quick.drive_manage.show();quick.manual.show()
        scroll=dialog.findChild(QScrollArea,'addResultsScroll')
        for expanded in (False,True,False):
            quick.advanced.setChecked(expanded)
            for _ in range(8):app.processEvents()
            assert scroll.geometry().bottom()<quick.state.geometry().top()
            assert quick.drive_manage.y()==quick.manual.y()
            assert quick.drive_manage.geometry().right()<quick.manual.x()
            assert quick.manual.geometry().bottom()<quick.advanced.y()
            assert scroll.geometry().bottom()<quick.advanced.y()
            assert quick.platform.isVisible()==expanded
            assert quick.save.isVisible()
        quick.sources.setCurrentIndex(2);app.processEvents()
        assert scroll.isHidden() and quick.steam_panel.isVisible()
        quick.sources.setCurrentIndex(1);app.processEvents()
        assert scroll.isVisible()
    finally:
        dialog.reject();dialog.deleteLater()

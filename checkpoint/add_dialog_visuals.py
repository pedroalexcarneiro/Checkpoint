"""Apresentação do cadastro. Não executa buscas, validações ou salvamento."""
from PySide6.QtWidgets import QSizePolicy
from .visual_tokens import SPACE,HEIGHT


def style_add_dialog(dialog):
    quick=dialog.quick_add
    dialog.setMinimumSize(680,600);dialog.resize(760,640)
    dialog.layout().setContentsMargins(*([SPACE['lg']]*4));dialog.layout().setSpacing(SPACE['sm'])
    quick.query.setFixedHeight(48)
    quick.sources.setExpanding(True);quick.sources.setDrawBase(False)
    quick.preview.setFixedHeight(148);quick.preview.layout().setContentsMargins(*([SPACE['md']]*4))
    quick.art.setFixedSize(80,112)
    quick.results.setMinimumHeight(200);quick.results.setMaximumHeight(216)
    quick.state.setWordWrap(True)
    for button in (quick.save,quick.cancel):
        button.setMinimumHeight(HEIGHT['button']);button.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)
    quick.save.setProperty('variant','primary');quick.cancel.setProperty('variant','secondary')

    from .catalog_result_visuals import CatalogResultDelegate
    quick.results.setItemDelegate(CatalogResultDelegate(quick,quick.results))
    quick.results.setSpacing(SPACE['xxs']);quick.results.setMouseTracking(True)

    quick.drive_manage.setObjectName('secondary')
    if dialog.catalog_result is None:
        quick.facts.setText('Digite o nome de um jogo e escolha um resultado para continuar.')
    from .catalog_result_visuals import ResultEmptyOverlay
    quick.visual_empty=ResultEmptyOverlay(quick)

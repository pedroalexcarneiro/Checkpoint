"""Apresentação do cadastro. Não executa buscas, validações ou salvamento."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame,QHBoxLayout,QScrollArea,QSizePolicy,QVBoxLayout,QWidget
from .visual_tokens import SPACE,HEIGHT


def style_add_dialog(dialog):
    quick=dialog.quick_add
    dialog.setMinimumSize(680,600);dialog.resize(760,640)
    dialog.layout().setContentsMargins(22,SPACE['lg'],22,SPACE['lg']);dialog.layout().setSpacing(SPACE['sm'])
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
    arrange_results(dialog)
    if dialog.catalog_result is None:
        quick.facts.setText('Digite o nome de um jogo e escolha um resultado para continuar.')
    from .catalog_result_visuals import ResultEmptyOverlay
    quick.visual_empty=ResultEmptyOverlay(quick)


def arrange_results(dialog):
    quick=dialog.quick_add
    outer=dialog.layout()
    action_index=outer.indexOf(quick.drive_manage)
    actions=QHBoxLayout()
    for button in (quick.drive_manage,quick.manual):
        outer.removeWidget(button)
        actions.addWidget(button)
    actions.addStretch()
    outer.insertLayout(action_index,actions)

    first=outer.indexOf(quick.results)
    count=outer.indexOf(quick.other)-first+1
    body=QWidget()
    content=QVBoxLayout(body)
    content.setContentsMargins(0,0,0,0)
    content.setSpacing(SPACE['sm'])
    for _ in range(count):
        item=outer.takeAt(first)
        widget=item.widget()
        visible=not widget.isHidden()
        content.addWidget(widget,0,item.alignment())
        widget.setVisible(visible)
    content.addStretch()
    scroll=QScrollArea()
    scroll.setObjectName('addResultsScroll')
    scroll.setFrameShape(QFrame.NoFrame)
    scroll.setWidgetResizable(True)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.setWidget(body)
    outer.insertWidget(first,scroll,1)

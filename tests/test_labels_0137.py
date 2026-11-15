import pytest
from PySide6.QtWidgets import QComboBox
from test_bugs_0134 import ui, sample


@pytest.mark.parametrize('stored', ['Não iniciado', 'Backlog'])
def test_not_started_label_keeps_legacy_data_on_open(ui, app, stored):
    w, identity = ui
    w.library.save_game({'title': w.library.get(identity)['title'], 'status': stored}, identity)
    w.detail(identity); app.processEvents()
    control = w.detail_page.findChild(QComboBox, 'gameStatus')
    assert [control.itemText(i) for i in range(control.count())] == [
        'Não iniciado', 'Jogando', 'Pausado', 'Concluído', 'Abandonado']
    assert control.currentText() == 'Não iniciado'
    assert w.library.get(identity)['status'] == stored
    assert identity in [g['id'] for g in w.library.owned_games(status='Não iniciado')]
    control.setCurrentText('Jogando')
    assert w.library.get(identity)['status'] == 'Jogando'


def test_period_and_sort_labels_keep_underlying_keys(ui):
    from checkpoint.statistics_periods import PERIODS
    w, _ = ui
    assert PERIODS[:3] == (('Hoje', 'daily'), ('Esta semana', 'weekly'), ('Este mês', 'monthly'))
    assert w.sort.itemText(w.sort.findData('title')) == 'Alfabeticamente'
    assert w.sort.itemText(w.sort.findData('recent')) == 'Adicionados recentemente'

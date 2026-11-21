from datetime import datetime, timedelta, timezone
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QComboBox
from test_bugs_0134 import ui, sample


def settle(app):
    for _ in range(10):
        app.processEvents()


def test_about_and_diary_actions_align_at_the_bottom_right(ui,app):
    window,identity=ui
    window.library.save_game({'title':'Jogo sem descrição','platform':'GBA','source':'Busca'},identity)
    window.resize(1000,700);window.detail(identity);settle(app)
    overview=window.detail_tabs.widget(0)
    buttons={b.text():b for b in overview.findChildren(QPushButton)}
    search,edit=buttons['Pesquisar manualmente'],buttons['Editar ficha']
    assert search.y()==edit.y() and search.geometry().right()<edit.x()
    assert edit.parentWidget().width()-edit.geometry().right()<=26
    for caption in ('Plataforma','Origem · Busca'):
        fact=next(label for label in overview.findChildren(QLabel) if label.text()==caption)
        assert fact.mapTo(overview,QPoint()).y()<edit.mapTo(overview,QPoint()).y()
    window.detail_tabs.setCurrentIndex(2);settle(app)
    diary=window.detail_tabs.currentWidget()
    buttons={b.text():b for b in diary.findChildren(QPushButton)}
    folder,add,save=[buttons[name] for name in ('Abrir pasta de capturas','Adicionar captura ou vídeo','Salvar memória')]
    assert folder.y()==add.y()==save.y()
    assert folder.geometry().right()<add.x() and add.geometry().right()<save.x()
    assert diary.width()-save.geometry().right()<=14


def test_long_file_name_uses_central_width_and_keeps_full_name(ui, app):
    w, identity = ui
    filename = 'The Legend of Zelda - Ocarina of Time (USA) (Revision 1) - versão de teste.z64'
    with w.library.sql:
        w.library.sql.execute(
            'INSERT INTO game_files(game_id,drive_id,original_name,platform) VALUES(?,?,?,?)',
            (identity, 'isolated-0139', filename, 'N64'))
    for width in (1000, 1280, 1920):
        w.resize(width, 800)
        w.detail(identity)
        w.detail_tabs.setCurrentIndex(3)
        settle(app)
        label = w.detail_tabs.currentWidget().findChild(QLabel, 'romFileName')
        assert label is not None
        assert label.toolTip() == filename
        assert not label.wordWrap()
        frame = label.parentWidget().parentWidget()
        button = next(b for b in frame.findChildren(QPushButton) if b.text() == 'Baixar ROM')
        end = label.mapTo(frame, label.rect().topRight()).x()
        start = button.mapTo(frame, QPoint()).x()
        assert end < start
        assert label.width() > 250
    assert w.library.sql.execute('SELECT original_name FROM game_files WHERE game_id=?', (identity,)).fetchone()[0] == filename


def test_completions_use_recorded_timestamp_not_current_status(ui, app):
    from checkpoint.statistics_periods import period_stats
    w, identity = ui
    other = w.library.save_game({'title': 'Hades', 'status': 'Concluído'})
    now = datetime.now(timezone.utc)
    with w.library.sql:
        w.library.sql.execute("UPDATE games SET status='Concluído',completed_at=NULL WHERE id=?", (identity,))
        w.library.sql.execute("UPDATE games SET completed_at=? WHERE id=?", ((now-timedelta(days=1)).isoformat(), other))
    before = [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')]
    assert sum(period_stats(w.library, 'all')['completions'].values()) == 1
    w.navigate(4)
    period = w.pages[4].findChild(QComboBox, 'statisticsPeriod')
    period.setCurrentIndex(period.findData('all'))
    settle(app)
    frame = w.pages[4].findChild(QWidget, 'completionMetrics')
    assert frame is not None
    assert any(label.text() == 'Jogos concluídos' for label in frame.findChildren(QLabel))
    assert frame.findChild(QLabel, 'metricValue').text() == '1'
    assert [tuple(r) for r in w.library.sql.execute('SELECT * FROM games')] == before

"""Consulta assíncrona e importação explícita de jogos Steam."""
from threading import Event
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QAbstractItemView, QDialog, QHBoxLayout, QInputDialog, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,
)

from .credentials import CredentialVault
from .integrations.steam import SteamProvider, steam_id
from .jobs import Job
from .steam_library import import_games, save_achievements


class SteamDialog(QDialog):
    enrichment_progress = Signal(str)
    def __init__(self, library, parent=None):
        super().__init__(parent)
        self.library = library
        self.games, self.links = [], {}
        self.result_account = None
        self.job = None
        self.changed = False
        self.setWindowTitle('Importar biblioteca Steam')
        self.resize(1040, 700)
        layout = QVBoxLayout(self)
        help_text = QLabel('Consulte a conta, marque os jogos e confirme a importação. Horas Steam ficam separadas das sessões locais. Jogos com o mesmo nome só são associados por sua escolha.')
        help_text.setWordWrap(True)
        help_text.hide()
        row = QHBoxLayout()
        row.addWidget(QLabel('SteamID64'))
        self.account = QLineEdit(str(library.setting('steam.account', '')))
        self.account.setPlaceholderText('Identificador numérico de 17 dígitos')
        row.addWidget(self.account, 1)
        self.key_button = QPushButton('Configurar chave Steam')
        self.key_button.clicked.connect(self.configure_key)
        row.addWidget(self.key_button)
        self.fetch_button = QPushButton('Consultar biblioteca')
        self.fetch_button.setObjectName('primary')
        self.fetch_button.clicked.connect(self.fetch)
        row.addWidget(self.fetch_button)
        layout.addLayout(row)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['Importar', 'Jogo Steam', 'Horas Steam', 'Destino no Checkpoint'])
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(1, 300)
        self.table.setAlternatingRowColors(True);self.table.setShowGrid(False);self.table.verticalHeader().hide()
        self.table.itemChanged.connect(self.selection_changed)
        layout.addWidget(self.table, 1)
        actions = QHBoxLayout()
        self.mark_button = QPushButton('Marcar todos')
        self.mark_button.clicked.connect(lambda: self.mark_all(Qt.Checked))
        self.unmark_button = QPushButton('Desmarcar todos')
        self.unmark_button.clicked.connect(lambda: self.mark_all(Qt.Unchecked))
        self.link_button = QPushButton('Associar linha a cadastro existente')
        self.link_button.clicked.connect(self.link_selected)
        self.new_button = QPushButton('Usar novo cadastro na linha')
        self.new_button.clicked.connect(self.unlink_selected)
        for control in (self.mark_button, self.unmark_button, self.link_button, self.new_button):
            actions.addWidget(control)
        layout.addLayout(actions)
        footer = QHBoxLayout()
        self.import_button = QPushButton('Importar jogos marcados')
        self.import_button.setObjectName('primary')
        self.import_button.clicked.connect(self.import_selected)
        self.achievements_button = QPushButton('Atualizar conquistas da linha')
        self.achievements_button.clicked.connect(self.fetch_achievements)
        footer.addWidget(self.import_button)
        footer.addWidget(self.achievements_button)
        layout.addLayout(footer)
        self.state = QLabel('Requer chave Steam Web API e acesso aos detalhes dos jogos da conta. Nenhuma senha Steam é solicitada.')
        self.state.setTextFormat(Qt.PlainText)
        self.state.setWordWrap(True)
        layout.addWidget(self.state)
        self.enrichment_progress.connect(self.state.setText)
        self.enrichment_stop = Event()
        self.stop_button = QPushButton('Parar preenchimento após o jogo atual')
        self.stop_button.clicked.connect(self.enrichment_stop.set)
        self.stop_button.hide()
        layout.addWidget(self.stop_button)
        from .design_system import dialog_heading
        dialog_heading(layout,'Steam','Consulte sua conta e escolha os jogos para importar.','Steam')
        self.account.textChanged.connect(self.invalidate)
        self.selection_changed()

    def controls(self):
        return (self.account, self.key_button, self.fetch_button, self.table,
                self.mark_button, self.unmark_button, self.link_button, self.new_button,
                self.import_button, self.achievements_button)

    def selection_changed(self, *_):
        self.import_button.setEnabled(self.job is None and any(
            self.table.item(index, 0).checkState() == Qt.Checked for index in range(len(self.games))))
        self.achievements_button.setEnabled(self.job is None and bool(self.games))

    def invalidate(self):
        self.games, self.links, self.result_account = [], {}, None
        self.table.setRowCount(0)
        self.selection_changed()

    def configure_key(self):
        value, ok = QInputDialog.getText(self, 'Steam Web API', 'Chave pessoal da API (armazenada no cofre do Windows):', QLineEdit.Password)
        if ok and value.strip():
            try:
                CredentialVault().set('steam', value.strip())
                self.state.setText('Chave salva. Consulte a biblioteca para verificar o acesso.')
            except Exception:
                self.state.setText('Não foi possível salvar a chave no cofre do Windows.')

    def run_job(self, work, success):
        self.job = Job(work, self)
        for control in self.controls():
            control.setEnabled(False)
        def deliver(result):
            try:
                success(result)
            except Exception:
                self.state.setText('Não foi possível salvar o resultado Steam. A transação foi cancelada; consulte novamente.')
        self.job.succeeded.connect(deliver)
        self.job.failed.connect(self.state.setText)
        self.job.finished.connect(self.job_finished)
        self.job.start()

    def job_finished(self):
        self.job.deleteLater()
        self.job = None
        for control in self.controls():
            control.setEnabled(True)
        self.stop_button.hide()
        self.selection_changed()

    def fetch(self):
        try:
            account = steam_id(self.account.text())
        except ValueError as error:
            self.state.setText(str(error))
            return
        self.invalidate()
        self.state.setText('Consultando biblioteca Steam…')
        self.run_job(lambda: (account, SteamProvider(CredentialVault().get('steam')).owned_games(account)), self.show_games)

    def show_games(self, result):
        account, games = result
        self.games, self.result_account = games, account
        self.library.set_setting('steam.account', account)
        self.table.blockSignals(True)
        self.table.setRowCount(len(games))
        for index, game in enumerate(games):
            check = QTableWidgetItem()
            check.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            check.setCheckState(Qt.Unchecked)
            self.table.setItem(index, 0, check)
            self.table.setItem(index, 1, QTableWidgetItem(f'{game.title} · AppID {game.app_id}'))
            self.table.setItem(index, 2, QTableWidgetItem('Não disponível' if game.minutes is None else f'{game.minutes / 60:.1f} h'))
            self.table.setItem(index, 3, QTableWidgetItem(self.destination(game)))
        self.table.blockSignals(False)
        self.state.setText(f'{len(games)} jogos retornados. Marque os desejados; a consulta não importa automaticamente.' if games else 'A Steam retornou uma biblioteca vazia. Nenhum cadastro local foi removido.')
        self.selection_changed()

    def destination(self, game):
        existing = self.library.sql.execute("SELECT g.id,g.title,g.deleted_at FROM games g JOIN external_identifiers e ON g.id=e.game_id WHERE e.provider='steam' AND e.external_id=?", (game.app_id,)).fetchone()
        if existing:
            return ('Na lixeira · restaure antes de importar: ' if existing['deleted_at'] else 'Atualizar horas: ') + existing['title']
        if game.app_id in self.links:
            target = self.library.get(self.links[game.app_id])
            return 'Associar: ' + (target['title'] if target else 'Cadastro indisponível')
        same_title = self.library.sql.execute('SELECT 1 FROM games WHERE deleted_at IS NULL AND title=? COLLATE NOCASE', (game.title,)).fetchone()
        return 'Novo · título já existe; revise a associação' if same_title else 'Novo cadastro'

    def link_selected(self):
        index = self.table.currentRow()
        if index < 0:
            self.state.setText('Selecione uma linha para associar.')
            return
        game = self.games[index]
        if self.library.sql.execute("SELECT 1 FROM external_identifiers WHERE provider='steam' AND external_id=?", (game.app_id,)).fetchone():
            self.state.setText('Este AppID já tem um cadastro associado. Restaure-o na lixeira se necessário.')
            return
        rows = self.library.sql.execute("SELECT g.id,g.title FROM games g WHERE g.deleted_at IS NULL AND NOT EXISTS (SELECT 1 FROM external_identifiers e WHERE e.game_id=g.id AND e.provider='steam') ORDER BY g.title COLLATE NOCASE").fetchall()
        if not rows:
            self.state.setText('Nenhum cadastro sem identidade Steam está disponível.')
            return
        choices = [f"{row['title']} · cadastro {row['id']}" for row in rows]
        choice, ok = QInputDialog.getItem(self, 'Associar jogo Steam', f'Escolha o cadastro que representa {game.title}:', choices, 0, False)
        if ok:
            self.links[game.app_id] = rows[choices.index(choice)]['id']
            self.table.item(index, 3).setText(self.destination(game))

    def unlink_selected(self):
        index = self.table.currentRow()
        if index >= 0:
            game = self.games[index]
            self.links.pop(game.app_id, None)
            self.table.item(index, 3).setText(self.destination(game))
            self.state.setText('AppIDs já importados continuam associados ao cadastro original.')

    def mark_all(self, state):
        self.table.blockSignals(True)
        for index in range(len(self.games)):
            self.table.item(index, 0).setCheckState(state)
        self.table.blockSignals(False)
        self.selection_changed()

    def import_selected(self):
        selected = [game for index, game in enumerate(self.games) if self.table.item(index, 0).checkState() == Qt.Checked]
        if not selected or not self.result_account:
            return
        try:
            from .trash_import import ask_removed,removed_match,detach_removed
            decisions=[]
            for game in selected:
                from .integrations import MetadataResult
                removed=removed_match(self.library,{'title':game.title,'platform':'PC'},result=MetadataResult('steam',game.app_id,game.title))
                if removed:
                    decision=ask_removed(self,removed['title'])
                    if decision=='cancel':return
                    decisions.append((removed['id'],game.app_id,decision))
            selected_ids = {game.app_id for game in selected}
            import_links={key:value for key,value in self.links.items() if key in selected_ids}
            with self.library.sql:
                for identity,app,decision in decisions:
                    if decision=='restore' and app not in import_links:import_links[app]=identity
                    elif decision=='new' and import_links.get(app)==identity:import_links.pop(app)
                    if decision=='restore':self.library.sql.execute('UPDATE games SET deleted_at=NULL WHERE id=?',(identity,))
                    else:detach_removed(self.library,identity)
                created, updated = import_games(self.library, self.result_account, selected, import_links)
        except (ValueError, RuntimeError) as error:
            self.state.setText(str(error))
            return
        except Exception:
            self.state.setText('Não foi possível salvar a importação. A transação foi cancelada.')
            return
        self.changed = True
        for index, game in enumerate(self.games):
            self.table.item(index, 3).setText(self.destination(game))
        summary=f'{created} jogos criados; {updated} atualizados/associados. Dados pessoais e sessões locais foram preservados.'
        ids=[self.library.sql.execute("SELECT game_id FROM external_identifiers WHERE provider='steam' AND external_id=?",(game.app_id,)).fetchone()[0] for game in selected]
        path=self.library.db.path
        self.enrichment_stop.clear();self.stop_button.show()
        def complete():
            from .database import Database
            from .library import Library
            from .worker import run_isolated
            db=Database(path)
            try:
                lib=Library(db);messages=[]
                for index,identity in enumerate(ids):
                    if self.enrichment_stop.is_set():
                        messages.append('Preenchimento interrompido. Jogos importados preservados.');break
                    game=lib.get(identity)
                    title=game['title'] if game else 'Jogo indisponível'
                    self.enrichment_progress.emit(f'{index+1}/{len(ids)} · '+title+' · buscando ficha e imagens…')
                    try:message=run_isolated('enrich',path,game_id=identity)
                    except Exception:message='Não foi possível completar as imagens; jogo importado preservado.'
                    messages.append(title+': '+message)
                return '\n'.join(messages)
            finally:db.close()
        self.state.setText(summary+' Buscando fichas e imagens…')
        self.run_job(complete,lambda message:self.state.setText(summary+'\n'+message))

    def fetch_achievements(self):
        index = self.table.currentRow()
        if index < 0 or not self.result_account:
            self.state.setText('Selecione um jogo já importado desta conta.')
            return
        game, account = self.games[index], self.result_account
        if not self.library.sql.execute('SELECT 1 FROM steam_owned_games WHERE steam_id=? AND app_id=?', (account, game.app_id)).fetchone():
            self.state.setText('Importe este jogo antes de consultar conquistas.')
            return
        self.state.setText('Consultando conquistas do jogo selecionado…')
        def save(rows):
            save_achievements(self.library, account, game.app_id, rows)
            self.changed = True
            unlocked = sum(row.unlocked_at is not None for row in rows)
            self.state.setText(f'Conquistas Steam: {unlocked}/{len(rows)} desbloqueadas. Disponíveis na página do jogo.')
        self.run_job(lambda: SteamProvider(CredentialVault().get('steam')).achievements(account, game.app_id), save)

    def reject(self):
        if self.job:
            self.state.setText('Aguarde a consulta Steam terminar antes de fechar.')
            return
        super().reject()

    def closeEvent(self, event):
        if self.job:
            self.state.setText('Aguarde a consulta Steam terminar antes de fechar.')
            event.ignore()
            return
        super().closeEvent(event)

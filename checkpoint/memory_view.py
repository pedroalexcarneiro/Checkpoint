"""Página persistente de Memórias, abas preguiçosas e cards sob demanda."""
from datetime import datetime, timedelta, timezone
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTabWidget
from .design_system import page_scroll, empty_state
from .home_data import recent_memories
from .memory_artwork import memory_cache
from .visual_tokens import SPACE


def record_key(record):
    return record['kind'], record['id']


class MemoryBrowser(QWidget):
    batch_size = 24

    def __init__(self, window):
        super().__init__()
        self.host = window
        self.cache = memory_cache(window)
        self.records = []
        self.states = []
        self.signature = None
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        filters = QHBoxLayout()
        self.game_filter = QComboBox()
        self.game_filter.setObjectName('memoryGameFilter')
        self.game_filter.setAccessibleName('Jogo das memórias')
        self.period = QComboBox()
        self.period.setObjectName('memoryPeriodFilter')
        self.period.setAccessibleName('Período das memórias')
        for caption, days in [('Todo o período', 0), ('Últimos 7 dias', 7),
                              ('Últimos 30 dias', 30), ('Último ano', 365)]:
            self.period.addItem(caption, days)
        self.order = QComboBox()
        self.order.setObjectName('memoryOrder')
        self.order.setAccessibleName('Ordenação das memórias')
        self.order.addItem('Mais recentes', 'recent')
        self.order.addItem('Mais antigas', 'oldest')
        self.order.addItem('Alfabeticamente', 'title')
        for widget in (self.game_filter, self.period, self.order):
            filters.addWidget(widget)
        filters.addStretch()
        layout.addLayout(filters)
        self.tabs = QTabWidget()
        self.tabs.setObjectName('memoryTabs')
        for caption, kind in [('Tudo', None), ('Diário', 'diary'), ('Capturas e vídeos', 'media')]:
            page = QWidget()
            outer = QVBoxLayout(page)
            outer.setContentsMargins(0, 16, 0, 0)
            inside = page_scroll(outer, reserve_scrollbar=True)
            inside.setContentsMargins(0, 0, SPACE['sm'], SPACE['xs'])
            self.states.append({'kind': kind, 'layout': inside, 'scroll': inside.scroll_area,
                                'grid': None, 'empty': None, 'signature': None, 'limit': self.batch_size})
            index = len(self.states)-1
            inside.scroll_area.verticalScrollBar().valueChanged.connect(
                lambda value, i=index: self.more_if_needed(i, value))
            self.tabs.addTab(page, caption)
        self.tabs.currentChanged.connect(self.populate)
        layout.addWidget(self.tabs)
        for widget, key, default in [(self.period, 'memories.period', 0),
                                     (self.order, 'memories.order', 'recent')]:
            widget.setCurrentIndex(max(0, widget.findData(window.library.setting(key, default))))
        for widget in (self.game_filter, self.period, self.order):
            widget.currentIndexChanged.connect(self.filter_changed)
        self.refresh()

    def refresh(self):
        records = recent_memories(self.host.library)
        index=getattr(self.host,'media_index',None)
        if index and index.missing:
            records=[{**row,'missing':True} if row.get('path') in index.missing else row for row in records]
        signature = tuple(tuple(sorted(row.items())) for row in records)
        if signature == self.signature:
            self.populate(self.tabs.currentIndex())
            return
        self.signature = signature
        self.records = records
        selected = self.game_filter.currentData()
        if selected is None:
            selected = self.host.library.setting('memories.game', None)
        self.game_filter.blockSignals(True)
        self.game_filter.clear()
        self.game_filter.addItem('Todos os jogos', None)
        titles = {row['game_id']: row['title'] for row in records}
        for identity, title in sorted(titles.items(), key=lambda pair: (pair[1].casefold(), pair[0])):
            self.game_filter.addItem(title, identity)
        self.game_filter.setCurrentIndex(max(0, self.game_filter.findData(selected)))
        self.game_filter.blockSignals(False)
        self.populate(self.tabs.currentIndex())

    def filter_changed(self):
        for key, value in [('memories.game', self.game_filter.currentData()),
                           ('memories.period', self.period.currentData()),
                           ('memories.order', self.order.currentData())]:
            self.host.library.set_setting(key, value)
        for state in self.states:
            state['signature'] = None
            state['limit'] = self.batch_size
        self.populate(self.tabs.currentIndex())

    def selected(self, state):
        result = []
        game_id = self.game_filter.currentData()
        days = self.period.currentData() or 0
        cutoff = datetime.now(timezone.utc)-timedelta(days=days)
        from .statistics_periods import instant
        for row in self.records:
            if game_id is not None and row['game_id'] != game_id:
                continue
            if state['kind'] and (row['kind'] == 'diary') != (state['kind'] == 'diary'):
                continue
            if days:
                try:
                    if instant(row['created_at']) < cutoff:
                        continue
                except (TypeError, ValueError):
                    continue
            result.append(row)
        if self.order.currentData() == 'oldest':
            result.reverse()
        elif self.order.currentData() == 'title':
            result.sort(key=lambda row: (row['title'].casefold(), row['game_id']))
        return result

    def populate(self, index):
        if index < 0 or index >= len(self.states):
            return
        from .collection_views import MemoryGrid, memory_card
        state = self.states[index]
        selected = self.selected(state)
        shown = selected[:state['limit']]
        signature = tuple(tuple(sorted(row.items())) for row in shown)
        if state['signature'] == signature:
            return
        state['signature'] = signature
        if not selected:
            if state['grid']:
                state['grid'].hide()
            if state['empty'] is None:
                state['empty'] = empty_state('memories', 'Nenhuma memória',
                    'Abra um jogo, entre na aba Memórias e adicione uma captura ou anotação.',
                    self.host.first_memory, 'Biblioteca')
                state['layout'].addWidget(state['empty'])
            state['empty'].show()
            return
        if state['empty']:
            state['empty'].hide()
        grid = state['grid']
        if grid is None:
            grid = state['grid'] = MemoryGrid(300)
            grid.setObjectName('memoriesGrid')
            state['layout'].addWidget(grid)
            state['layout'].addStretch()
        old = {getattr(card, 'memory_key', None): card for card in grid.cards}
        cards = []
        for record in shown:
            key = record_key(record)
            card = old.pop(key, None)
            if card is not None and card.memory_record != record:
                card.hide()
                card.deleteLater()
                card = None
            if card is None:
                card = memory_card(self.host, record, diary_only=state['kind'] == 'diary',
                                   thumbnail_cache=self.cache)
                card.memory_key = key
                card.memory_record = record.copy()
            cards.append(card)
        for card in old.values():
            card.hide()
            card.deleteLater()
        grid.cards = cards
        grid.reflow()
        grid.show()
        for card in cards:
            card.show()
            # Inserções no topo preservam também a ordem dos filhos acessíveis.
            card.raise_()

    def more_if_needed(self, index, value):
        if index != self.tabs.currentIndex():
            return
        state = self.states[index]
        bar = state['scroll'].verticalScrollBar()
        if not bar.maximum() or value < bar.maximum()-max(200, state['scroll'].height()):
            return
        if state['limit'] < len(self.selected(state)):
            state['limit'] += self.batch_size
            self.populate(index)

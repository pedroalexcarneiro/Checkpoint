"""Configuração GG.deals: entrada temporária e armazenamento exclusivo no cofre."""
from PySide6.QtWidgets import QFrame,QVBoxLayout,QHBoxLayout,QLineEdit
from .ui_components import text,action
from .theme import get_theme

class GgDealsConnection(QFrame):
    def __init__(self,window):
        super().__init__();self.window=window;self.setObjectName('ggdealsConnection')
        body=QVBoxLayout(self);body.setContentsMargins(18,16,18,16);body.setSpacing(10)
        head=QHBoxLayout();head.addWidget(text('GG.deals','cardTitle'));head.addStretch()
        self.dot=text('●');self.dot.setObjectName('ggdealsStateDot');self.dot.setFixedWidth(12);head.addWidget(self.dot)
        self.state=text('','muted');self.state.setObjectName('ggdealsState');head.addWidget(self.state);body.addLayout(head)
        row=QHBoxLayout();self.entry=QLineEdit();self.entry.setObjectName('ggdealsKey');self.entry.setEchoMode(QLineEdit.Password);self.entry.setPlaceholderText('Chave da API — salva somente no cofre');self.entry.setAccessibleName('Chave da API GG.deals');self.entry.setMaxLength(512)
        row.addWidget(self.entry,1);self.save_button=action('Salvar',self.save,True);self.remove_button=action('Remover',self.remove);row.addWidget(self.save_button);row.addWidget(self.remove_button);body.addLayout(row)
        self.notice=text('API oficial · valores em reais; histórico não é preço original.','caption');body.addWidget(self.notice)
        self.entry.textChanged.connect(lambda value:self.save_button.setEnabled(bool(value.strip())))
        self.entry.returnPressed.connect(self.save);self.save_button.setEnabled(False);self.update_state()
    def vault(self):
        from .credentials import CredentialVault
        return getattr(self.window,'ggdeals_vault_factory',CredentialVault)()
    def update_state(self):
        configured=self.window.integration_status('GG.deals').startswith('Credencial salva')
        self.state.setText('Configurado' if configured else 'Não configurado')
        self.dot.setProperty('configured',configured)
        self.dot.setStyleSheet('color: '+(get_theme('green').colors['accent'] if configured else self.window.theme.colors['muted']))
        self.remove_button.setEnabled(configured)
    def save(self):
        value=self.entry.text().strip()
        if not value:self.notice.setText('Cole a chave antes de salvar.');return
        try:
            self.vault().set('ggdeals',value)
        except Exception:
            self.notice.setText('Não foi possível salvar no cofre do Windows. Tente novamente.')
        else:
            from .prices import invalidate_prices
            invalidate_prices(self.window.library)
            self.notice.setText('Chave salva no cofre do Windows.');self.update_state()
        finally:
            self.entry.clear()
    def remove(self):
        try:self.vault().delete('ggdeals')
        except Exception:self.notice.setText('Não foi possível remover a configuração do cofre. Tente novamente.')
        else:
            from .prices import invalidate_prices
            invalidate_prices(self.window.library)
            self.notice.setText('Configuração removida do cofre.');self.update_state()
        finally:self.entry.clear()

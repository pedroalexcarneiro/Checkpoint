import secrets
from PySide6.QtWidgets import QLineEdit,QLabel
from checkpoint.ggdeals_connection import GgDealsConnection
from checkpoint.window import MainWindow

class MemoryVault:
    def __init__(self):self.value=None
    def get(self,name):return self.value
    def set(self,name,value):self.value=value
    def delete(self,name):self.value=None


def test_connection_key_is_masked_transient_and_only_saved_to_vault(library,app,monkeypatch,caplog):
    vault=MemoryVault();window=MainWindow(library);window.ggdeals_vault_factory=lambda:vault
    window.navigate(5);window.settings_tabs.setCurrentIndex(1)
    connection=window.pages[5].findChild(GgDealsConnection)
    assert connection.state.text()=='Não configurado' and not connection.remove_button.isEnabled()
    assert not connection.save_button.isEnabled() and connection.entry.echoMode()==QLineEdit.Password
    value=secrets.token_urlsafe(32);connection.entry.setText(value);connection.save_button.click()
    saved=vault.value==value;assert saved,'A configuração não foi salva no cofre de teste'
    assert connection.entry.text()=='' and connection.state.text()=='Configurado'
    assert connection.dot.property('configured') and connection.remove_button.isEnabled()
    rows=' '.join(str(tuple(row)) for row in library.sql.execute('SELECT * FROM settings'))
    visible=' '.join(label.text() for label in connection.findChildren(QLabel))
    leaked=value in rows or value in visible or value in caplog.text
    assert not leaked,'A configuração vazou para dados, texto ou logs'
    connection.remove_button.click();assert vault.value is None
    assert connection.state.text()=='Não configurado' and not connection.dot.property('configured')
    window.close()


def test_vault_errors_never_echo_input_or_exception(library,app,caplog):
    value=secrets.token_urlsafe(32)
    class Broken(MemoryVault):
        def set(self,name,current):raise RuntimeError(current)
        def delete(self,name):raise RuntimeError(value)
    vault=Broken();window=MainWindow(library);window.ggdeals_vault_factory=lambda:vault
    window.navigate(5);connection=window.pages[5].findChild(GgDealsConnection)
    connection.entry.setText(value);connection.save()
    assert not connection.entry.text()
    connection.remove()
    shown=' '.join(label.text() for label in connection.findChildren(QLabel))+caplog.text
    leaked=value in shown;assert not leaked,'A exceção do cofre expôs uma credencial'
    window.close()


def test_configuration_change_rechecks_prices_without_discarding_cache(library):
    from checkpoint.prices import invalidate_prices,needs_update,snapshot
    from checkpoint.library import now
    identity=library.save_game({'title':'Example'})
    library.set_setting(f'prices.ggdeals.{identity}',{'lowest':5900,'attempted_at':now()})
    assert not needs_update(library,identity)
    invalidate_prices(library)
    assert needs_update(library,identity) and snapshot(library,identity)['lowest']==5900

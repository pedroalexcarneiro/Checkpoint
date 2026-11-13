"""Segredos somente no cofre; a migração de serviço preserva o registro anterior."""
from keyring.errors import PasswordDeleteError
from .data_migration import LEGACY_PRODUCT

SERVICE='Checkpoint'
CREDENTIAL_NAMES=('steam','rawg','steamgriddb','drive-readonly','github-updates')


class CredentialVault:
    def __init__(self,backend=None):
        if backend is None:
            import keyring
            from keyring.backends.Windows import WinVaultKeyring
            keyring.set_keyring(WinVaultKeyring());backend=keyring
            if keyring.get_keyring().priority<=0:raise RuntimeError('Armazenamento seguro de credenciais indisponível.')
        self.keyring=backend
    def get(self,name):return self.keyring.get_password(SERVICE,name)
    def set(self,name,value):self.keyring.set_password(SERVICE,name,value)
    def delete(self,name):
        try:self.keyring.delete_password(SERVICE,name)
        except PasswordDeleteError:pass
    def migrate_legacy(self):
        copied=0
        for name in CREDENTIAL_NAMES:
            if self.keyring.get_password(SERVICE,name) is not None:continue
            value=self.keyring.get_password(LEGACY_PRODUCT,name)
            if value is not None:self.keyring.set_password(SERVICE,name,value);copied+=1
        return copied

"""Segredos no Windows Credential Manager via keyring, nunca em arquivos versionados."""
class CredentialVault:
    def __init__(self):
        import keyring
        from keyring.backends.Windows import WinVaultKeyring
        keyring.set_keyring(WinVaultKeyring())
        self.keyring = keyring
        if keyring.get_keyring().priority <= 0:
            raise RuntimeError('Armazenamento seguro de credenciais indisponível.')
    def get(self,name):
        return self.keyring.get_password('GameVault',name)
    def set(self,name,value):
        self.keyring.set_password('GameVault',name,value)
    def delete(self,name):
        try: self.keyring.delete_password('GameVault',name)
        except self.keyring.errors.PasswordDeleteError: pass

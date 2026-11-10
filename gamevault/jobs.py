"""Trabalhos de rede fora da thread da interface."""
from PySide6.QtCore import QThread,Signal

class Job(QThread):
    succeeded = Signal(object)
    failed = Signal(str)
    def __init__(self,work,parent=None):
        super().__init__(parent); self.work = work
    def run(self):
        try: self.succeeded.emit(self.work())
        except Exception as error:
            # Não propaga URLs, respostas OAuth ou chaves em mensagens genéricas.
            from .integrations import IntegrationError
            message = str(error) if isinstance(error,(IntegrationError,ValueError)) else 'Operação não concluída. Verifique conexão, credenciais e permissões.'
            self.failed.emit(message)

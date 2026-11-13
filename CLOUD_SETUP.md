# Ambiente de desenvolvimento

Use Python 3.12 e instale requirements-tested.txt e o projeto editável sem dependências adicionais. Confirme branch e versão antes de editar; esta revisão está em fix/rename-redesign-0.1.28.

No Linux, use QT_QPA_PLATFORM=offscreen para testes e capturas. Nunca use a pasta real do usuário: selecione diretórios novos com --data-dir e CHECKPOINT_TEST_ROOT. O cofre real não deve ser consultado por testes. Consulte TESTING.md e SETUP.md.

Não copie arquivos de credenciais nem exponha variáveis de ambiente ou configurações de autenticação. Falhas de rede devem ser registradas por categoria, sem URLs privadas ou valores secretos.

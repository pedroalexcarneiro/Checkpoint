Biblioteca Steam e correção de encerramento do formulário.

- Configurações > Steam: consulte a biblioteca com SteamID64 e chave Steam Web API, marque os jogos e confirme a importação.
- Associe jogos a cadastros existentes explicitamente. AppIDs já importados atualizam horas sem duplicar o jogo nem substituir notas, artes ou status.
- Horas por conta e conquistas Steam ficam separadas das sessões e marcos pessoais. Consulte conquistas por jogo no gerenciador Steam.
- Corrigido o encerramento nativo do formulário sem janela pai no Qt.
- Banco atualizado para schema 4 com backup automático antes da migração. Feche versões anteriores e preserve uma cópia de `%LOCALAPPDATA%\GameVault` antes de atualizar. O executável 0.1.13 não abre o banco migrado.

Baixe **Checkpoint-0.1.14-windows-x64.zip**, extraia a pasta Checkpoint completa e abra Checkpoint.exe. Mantenha `_internal` e `CheckpointUpdater`. Não é necessário instalar Python.

O fluxo de publicação exige testes em Windows, smoke do fonte e do executável extraído do ZIP, integridade SQLite, verificação do atualizador auxiliar e SHA-256. Consulte o arquivo de validação anexado para o resultado desta compilação. O pacote não tem assinatura digital; validação autenticada Steam e homologação em Windows 10/11 pessoal permanecem pendentes. O projeto completo continua em desenvolvimento.

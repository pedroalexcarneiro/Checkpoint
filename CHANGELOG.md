# Changelog

## 0.1.2 — Saves por jogo

- Perfis persistentes de saves tradicionais por jogo.
- Backup manual por jogo e backup opcional ao encerrar a sessão, em segundo plano.
- Histórico por jogo e restauração para a pasta original com cópia da versão anterior.
- Validação de estabilidade antes e depois da cópia; bloqueio de execução/fechamento durante operações.
- 28 testes passaram, incluindo sessão encerrada disparando backup real em worker.


## 0.1.1 — Checkpoint

- Novo nome na interface e no executável.
- Removidos slogans e subtítulos promocionais, com estados vazios diretos.
- Preservados banco, cofre e trava legados para compatibilidade com a biblioteca existente.


## 0.1.0 — 2026-11-10

- Projeto criado do zero em Python/PySide6, SQLite transacional e duas migrações versionadas.
- Navegação principal, identidade escura, estados vazios, biblioteca com CRUD, lixeira e filtros.
- Diário, mídia referenciada, conquistas pessoais, wishlist local e estatísticas reais.
- Execução local, perfis de emuladores, argumentos sem shell, sessões e recuperação manual.
- Cliente RAWG, seleção de artes SteamGridDB e cache validado; validação real com chaves pendente.
- Cliente Drive readonly, varredura paginada, cursor incremental, revisão manual e downloads verificados; validação real OAuth pendente.
- Importação DAT Logiqx e busca conservadora de checksum.
- Backup local de saves e restauração com cópia anterior e verificação SHA-256.
- Testes de domínio, segurança de caminhos, persistência, clientes controlados e UI headless.
- Documentação técnica, roadmap e receita de build Windows.

Não inclui ainda sincronização de saves no Drive, preços automáticos, Steam ou RetroAchievements. Ver PROJECT_STATUS.md para evidência final e pendências.

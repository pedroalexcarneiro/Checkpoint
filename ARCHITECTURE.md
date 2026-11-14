# Arquitetura

Python 3.12, PySide6, SQLite schema 4. Pacote `checkpoint`, entrada `checkpoint.app:main`, launcher `run_checkpoint.py`.

- `app.py`: inicialização, diretório de dados, encerramento e smokes isolados.
- `data_migration.py`: sessão de dados com travas, cópia em staging, snapshots SQLite com backup/integridade, compatibilidade de caminhos e preferências. A constante LEGACY_PRODUCT concentra a identificação anterior documentada no CHANGELOG.
- `credentials.py`: cofre Windows, serviço Checkpoint, migração entre serviços sem persistência ou log de valores.
- `database.py`, `library.py`, `game_import.py`: persistência, regras de posse e identidade; schema mantido em 4.
- `window.py`: navegação e coordenação; `home_view.py`, `detail_view.py`, `collection_views.py`, `settings_view.py`, `statistics_view.py`: telas.
- `cover_grid.py`, `ui_components.py`, `design_system.py`, `theme.py`: pintura, componentes, proporções e nove paletas.
- `dialogs.py`, `quick_add.py`, `game_editor.py`: formulário/validação, cadastro rápido e editor. Sobreposição mantida; proposta de simplificação no relatório.
- `jobs.py`, `worker.py`, `completion_queue.py`: enriquecimento e tarefas em segundo plano; falhas preservam o cadastro.
- `integrations/`: provedores e cache de imagens. `saves.py`: backups com restauração compatível com manifestos anteriores.

Tokens nunca pertencem ao SQLite, fixtures em disco ou relatórios. Tests usam pastas próprias e provedores controlados; capturas não equivalem a validação autenticada.

0.1.34 local: rom_link.py concentra candidatos, vínculo único das entradas da interface e conclusão; rom_link_dialog.py mantém os Jobs vivos até finished e oferece nova tentativa; rom_link_worker.py executa o novo protocolo auxiliar, inclusive via --rom-link-request no executável congelado. O worker/enrichment/cadastro protegidos não foram alterados. icons.py renderiza SVGs Lucide locais, empacotados como dados, com licença em THIRD_PARTY_NOTICES.md. Nenhuma mudança de schema.

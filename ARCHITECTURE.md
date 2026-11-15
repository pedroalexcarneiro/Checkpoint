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

## Ajustes locais 0.1.35

playtime.py agrega sessões locais uma vez e maior snapshot Steam por jogo para apresentação, sem criar sessões remotas. prices.selected_quote separa cache bruto de preço exibido e aplica filtro de lojas oficiais/keyshops. library.stats mantém UTC como contrato padrão; a tela solicita calendário local. Nenhuma migração de schema.

game_capture.py localiza janela Windows por PID de sessão iniciada pelo app e grava mídia pelo serviço da biblioteca; testes Linux usam adaptador controlado. A captura real Windows permanece sem validação. steam_installations.py lê bibliotecas VDF e manifests a partir de raízes Steam descobertas no sistema; o editor adiciona detecção sem alterar dialogs.py. settings_previews.py usa as paletas reais e mantém a prévia de tamanho à direita do slider.

ClickTabBar decide seleção no fim de clique, preservando teclado. Fechar processo do emulador encerra sessão; fechar somente a ROM dentro do processo permanece bloqueado, sem inferência por perda de foco. Consultar RELATORIO_0135.md e relatório de testes integral para limites e evidências.

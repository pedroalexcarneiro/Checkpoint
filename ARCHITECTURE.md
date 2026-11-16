# Arquitetura

## Correção de criação da janela 0.1.38

O handler Windows usa MSG.hWnd do callback e não invoca QWidget.winId durante criação/destruição nativa. Esse getter pode recriar a janela quando o Qt ainda não associou o handle. native_startup_check.py valida externamente a abertura normal em Windows já elevado do fonte e do executável extraído, com plugin Qt windows; não acrescenta modo especial ao produto nem automatiza consentimento UAC.

## Serviços locais 0.1.37

home_data.py lê execuções com PID, resumo semanal e memórias existentes; home_components.py compõe carrosséis, ações separadas e metadados de uma linha. library_list.py substitui a tabela por delegate horizontal. playtime.collection_times agrega sessões e snapshots separadamente em consultas limitadas, sem duplicação por join.

artwork_cache.py usa LRU limitada em bytes/entradas e invalidação por arquivo. Biblioteca solicita modo assíncrono: QImageReader e escala em QThreadPool de dois workers; QPixmap/pintura somente na GUI. Até 24 pedidos por cache; artwork_prefetch.py antecipa região visível e linhas vizinhas. Outros consumidores podem usar modo síncrono. Nenhum asset original é regravado.

period_chart.py seleciona barras horárias/semanais, calendário mensal ou mapa compacto; statistics_periods.day_hours reparte instantes reais entre limites locais inclusive DST. avatar_crop.py preserva original e calcula recorte/zoom; profile_dialog.py grava preferências atomicamente.

local_rom.py/local_rom_dialog.py validam arquivo, identidade/plataforma/perfil e confirmação, reutilizando game_files/rom_versions/EmulatorCommand/Launcher. Nenhuma cópia/upload/download para a origem local. rom_link.py endurece somente o vínculo pela ficha; A4 permanece protegido.

window_controls.py/windows_frame.py integram controles e adaptação nativa Windows; elevation.py prepara runas antes dos dados e exige SID original. Esses dois caminhos permanecem parciais sem homologação do pacote Windows. Schema 4, serviços protegidos e cofre preservados.

## Serviços acrescentados na rodada local 0.1.36

`global_hotkey.py` concentra RegisterHotKey/WM_HOTKEY Windows e ciclo de vida; sem dependência adicional. `game_capture.py` valida janela em primeiro plano/PID de sessão vivo e associação única antes/depois da imagem; não altera sessões por foco. Sem associação comprovada de processos-filhos: recusa com motivo.

`statistics_periods.py` calcula limites locais de calendário e recorta durações em instantes UTC, repartindo por meia-noite local/DST. Snapshots Steam não são distribuídos em períodos. SQLite schema 4 inalterado. Contexto de preços e preferências usam settings; dados existentes preservados. Coexistência de posse/Desejos pode ser explícita por collection.unowned=false, preservando semântica legada quando ausente.

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

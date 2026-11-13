# Relatório de correções — Checkpoint 0.1.28

## Base, escopo e preservação

Base confirmada antes das mudanças: `codex/design-fidelity-pt-br`, versão 0.1.27, commit `1f3df2730db2058ae9da074161716a9c0fa4edcc`. Branch de trabalho: `fix/rename-redesign-0.1.28`. A main não foi usada nem alterada. Versão atual consistente em pyproject e módulo: 0.1.28.

Não foram criadas tags ou releases, alterados assets de releases anteriores, usados force push ou acessadas bibliotecas pessoais. Nenhuma credencial real foi lida, criada ou gravada pela tarefa. Os testes de cofre usam valores fictícios somente em memória. Os comandos Git usam a conexão já configurada, sem inspecionar seu material de autenticação.

## Renomeação, arquivo por arquivo

Pacote `checkpoint/`, entrada `checkpoint.app:main`, launcher `run_checkpoint.py`, serviço do cofre Checkpoint, banco `checkpoint.sqlite`, pasta `%LOCALAPPDATA%\Checkpoint`, lock `checkpoint.lock` e scripts de build/validação atualizados. As correspondências literais entre caminhos anteriores e atuais ficam no apêndice histórico do CHANGELOG, para que o nome anterior não permaneça em documentação operacional.

| Arquivo atual | Alteração da renomeação |
| --- | --- |
| `.github/workflows/windows-release.yml` | Referências técnicas ou textuais atualizadas. |
| `.github/workflows/windows-ui-validation.yml` | Referências técnicas ou textuais atualizadas. |
| `AGENTS.md` | Referências técnicas ou textuais atualizadas. |
| `CLOUD_SETUP.md` | Referências técnicas ou textuais atualizadas. |
| `CONTINUITY.md` | Referências técnicas ou textuais atualizadas. |
| `PROJECT_STATUS.md` | Referências técnicas ou textuais atualizadas. |
| `README.md` | Referências técnicas ou textuais atualizadas. |
| `SETUP.md` | Referências técnicas ou textuais atualizadas. |
| `TESTING.md` | Referências técnicas ou textuais atualizadas. |
| `THIRD_PARTY_NOTICES.md` | Referências técnicas ou textuais atualizadas. |
| `checkpoint/.gitkeep` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/__init__.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/activity_heatmap.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/app.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/artwork_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/artwork_progress.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/artwork_render.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/assets/services/google-drive.png` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/assets/services/steam.ico` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/auto_artwork.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/automatic_catalog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/branding.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/catalog_picker.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/collection_views.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/completion_queue.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/cover_grid.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/credentials.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/database.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/description_provenance.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/design_system.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/detail_view.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/dialogs.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/drive_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/emulator_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/enrichment.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/folder_platform_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/fonts.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/game_editor.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/game_import.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/game_saves.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/home_view.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/.gitkeep` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/__init__.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/descriptions.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/drive.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/ggdeals.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/http.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/images.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/metadata.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/network.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/steam.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/integrations/steam_store.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/jobs.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/launcher.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/library.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/locale.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/metadata_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/price_queue.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/price_view.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/prices.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/profile_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/quick_add.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/rom_catalog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/save_profiles.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/save_smoke.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/saves.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/settings_view.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/statistics_view.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/steam_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/steam_library.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/task_status.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/theme.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/trash_import.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/ui_components.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/unified_catalog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/update_installer.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/updates.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/updates_dialog.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/window.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/window_style.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `checkpoint/worker.py` | Caminho renomeado; imports/referências atualizados quando presentes. |
| `evidence/cloud-qt-shutdown.txt` | Referências técnicas ou textuais atualizadas. |
| `evidence/save-modal-crash.txt` | Referências técnicas ou textuais atualizadas. |
| `evidence/validation.txt` | Referências técnicas ou textuais atualizadas. |
| `pyproject.toml` | Referências técnicas ou textuais atualizadas. |
| `run_checkpoint.py` | Launcher renomeado e import atualizado. |
| `run_updater.py` | Referências técnicas ou textuais atualizadas. |
| `scripts/LEIA-ME.txt` | Referências técnicas ou textuais atualizadas. |
| `scripts/build.ps1` | Referências técnicas ou textuais atualizadas. |
| `scripts/create_icon.py` | Referências técnicas ou textuais atualizadas. |
| `scripts/package_ui_review.py` | Referências técnicas ou textuais atualizadas. |
| `scripts/package_windows_release.py` | Referências técnicas ou textuais atualizadas. |
| `scripts/render_ui_review.py` | Referências técnicas ou textuais atualizadas. |
| `tests/conftest.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_auto_artwork.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_catalog.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_complete_layout.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_completion_queue.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_drive.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_drive_auth.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_drive_search.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_enrichment.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_folder_platforms.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_game_import.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_game_saves.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_isolated_operations.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_layout_regressions_025.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_library.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_localized_metadata.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_migrations.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_network.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_profile.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_quick_add.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_save_lifecycle.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_save_profiles.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_saves.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_services.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_steam.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_themes.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_trash_import.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_ui.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_ui_polish.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_ui_redesign.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_updates.py` | Referências técnicas ou textuais atualizadas. |
| `tests/test_wishlist_prices.py` | Referências técnicas ou textuais atualizadas. |

Busca final: `git grep -ni 'game''vault' -- . ':(exclude)CHANGELOG.md'` deve retornar zero ocorrências. As 78 linhas com ocorrências históricas restantes no CHANGELOG têm estes motivos: linha 7, descrição da renomeação nesta versão; linha 396, introdução histórica; linhas 400–471, um caminho anterior por arquivo no apêndice. Cada uma dessas 72 linhas documenta um arquivo renomeado; linhas 472–475 registram os quatro identificadores de compatibilidade (serviço, pasta, banco e trava). Todos esses usos são históricos, sem uso operacional direto. Não são imports, serviços ou instruções atuais. Em `data_migration.py`, `LEGACY_PRODUCT` monta o identificador anterior exclusivamente para compatibilidade; removê-lo impediria localizar os dados e o cofre antigos.

## Migração e segurança de dados

`prepare_data_directory` cria staging, copia arquivos comuns e produz snapshots consistentes dos bancos SQLite com `sqlite3.Connection.backup`, verificando `PRAGMA integrity_check` antes da adoção. Não copia arquivos WAL/SHM manualmente. Renomeia o banco principal no destino e mantém o schema 4. Preserva a pasta original, preferências, notas, sessões, mídia e backups. Caminhos internos passam a apontar para a cópia; caminhos externos não são trocados.

Uma trava transitória serializa o início; as travas antiga e nova permanecem retidas durante a sessão, impedindo abrir a edição anterior ao mesmo tempo. Destino existente não é sobrescrito. Uma pasta nova vazia ao lado de banco antigo gera erro claro em vez de abrir uma biblioteca vazia. Falhas removem somente staging incompleto, mostram o caminho de origem na interface e registram apenas categoria/classe de erro no log.

O cofre copia somente credenciais ausentes no serviço novo, sem apagar ou substituir valores antigos. O marcador de conclusão contém apenas um número, não valores de credencial. No Linux, a migração nativa do cofre não é tentada. Em testes, inclusive os preparados para Windows, o backend é em memória.

Decisão conservadora: exportações reconhecíveis de segredos (`credentials*.json`, `token*.json`, `client_secret*.json`, `.env` e variantes) não são copiadas para outros arquivos; permanecem intocadas na origem. Arquivos comuns com nomes parecidos, como a ROM fictícia usada no teste, continuam copiados. Isso resolve a tensão entre copiar a pasta inteira e não copiar credenciais em arquivos. SQLite secundário de backup é copiado pela API sem reescrever seu conteúdo histórico. Arquivos de saves continuam aceitando manifestos anteriores.

Testes em `tests/test_data_migration.py`: primeira abertura com pasta antiga completa e WAL; abertura sem dados antigos; destino existente; falha de integridade sem publicar cópia; credenciais fictícias sem log/arquivo e sem sobrescrever o serviço novo; preferência antiga normalizada para Verde com outras preferências intactas; concorrência de instâncias; `--data-dir` sem tocar no padrão; banco corrompido e destino vazio; erro de cofre sanitizado; edição antiga aberta; arquivo comum preservado. `tests/test_saves.py` cobre o manifesto anterior.

Não foi validada migração de uma biblioteca pessoal ou cofre real no computador Windows do usuário. Testes são isolados; não se deve confundir cobertura automatizada com essa validação.

## Nove temas

Removido o tema Branco, incluindo paleta, seletor, swatches, revisão de capturas e textos atuais. Temas: Azul, Verde, Amarelo, Vermelho, Preto, Roxo, Rosa, Laranja e Ciano. Verde permanece padrão. A bolinha branca das referências foi removida por decisão do dono.

Arquivos envolvidos: `checkpoint/theme.py`, `checkpoint/profile_dialog.py`, `scripts/render_ui_review.py`, `scripts/package_ui_review.py`, `tests/test_themes.py`, `tests/test_ui_redesign.py`, README, DESIGN, SETUP, TESTING, PROJECT_STATUS, CONTINUITY e notas da revisão. Documentos históricos foram consolidados no CHANGELOG. A chave antiga de preferência permanece apenas na normalização obrigatória de `data_migration.py` e na fixture de migração, sem representar um tema disponível. Cores de tinta em SVG/imagens não são paletas do aplicativo.

## Layout e bugs

- Biblioteca: quatro colunas, capas verticais, título/status alinhados à imagem, borda de seleção, filtros próximos às abas e espaço superior reduzido. Placeholder desenha o título completo, inclusive ARK, sem inventar arte ou usar duas letras.
- Desejos: mesma grade vertical; cards de dimensões iguais e área de logo fixa, proporcional e contida. Cinco jogos exibem “5 jogos”; um exibe “1 jogo”. Reserva de espaço de rolagem evita mudança de largura entre uma e várias linhas. Ofertas, adição e lixeira ficam alinhadas.
- Início: banner com “Continuar jogando”, quatro capas de continuidade e atividade à direita. Havendo ambos os tipos, prioriza uma conquista e uma entrada de diário; não fabrica eventos.
- Ficha: banner/voltar, barra de execução, bolinha de status, tempo, menu, quatro abas, descrição à esquerda, galeria à direita e metadados com ícones. Logo/capa não se duplicam na ficha.
- Cadastro: três fontes, pesquisa com lupa/limpar, prévia com capa pequena, título/plataforma/estúdio e check, link de troca, automação, avançado recolhido e fechar visível. Estados de busca e ausência não se sobrepõem. Botão exige seleção de jogo ou ROM. Busca de dados/imagens ocorre em segundo plano; uma ROM selecionada pode ser salva mesmo sem ficha disponível.
- Desejos usa “Adicionar desejo” e “Salvar desejo”; a ficha mostra “Adicionado à lista de desejos”. O risco de posse foi confirmado no código anterior: salvar reaproveitava a identidade e escrevia a marca de não possuído. Agora a posse anterior é preservada e o aviso indica que o jogo já está na Biblioteca. Testes verificam ausência de marca indevida e preservação de notas.
- Biblioteca vazia oferece adicionar; busca/filtro sem resultado oferece limpar filtros; abas vazias têm mensagem própria e retorno a todos os jogos.
- Conexões: 2×2, quatro serviços, ajuda no canto direito, Avançado recolhido, Gerenciar/Conectar e bolinhas verde/cinza. “Configurado” informa presença de configuração, não autenticação verificada.
- Menu: identidade existente preservada, cinco destinos, separador, Configurações e perfil no rodapé com chevron. Textos e contadores revisados em PT-BR, inclusive importação Steam, conquistas e dia singular no calendário; datas de apresentação e acessibilidade DD/MM/AAAA; datas ISO persistidas continuam ISO.

### Desvios e decisões explícitas

1. Desejos não tinha mockup específico completo: usa a grade da Biblioteca com logo contida, preço, link e ações. Em janelas menores o preço fica abaixo de “Menor preço atual”, preservando leitura. Desvio permitido pelo pedido.
2. “Jogar” somente com executável configurado; sem ele, “Configurar execução” é secundário. ROMs continuam acessíveis em Arquivos. Desvio solicitado.
3. Início substitui “Ver jogo” por “Continuar jogando”. Sem execução configurada, o botão abre a ficha para configuração, sem tentar iniciar algo inexistente. Desvio solicitado, com comportamento conservador.
4. Identidade checkpo//nt e ícone próprio preservados, em vez do controle e do texto em maiúsculas das referências. Exceção do dono.
5. Nove temas e ausência da bolinha branca, por decisão do dono.
6. Solicitar desejo de um jogo já possuído preserva a Biblioteca e informa isso; não o reclassifica silenciosamente.

## Capturas e comparação

Geradas por `scripts/render_ui_review.py`, usando Qt real, dados locais e artes sintéticas identificadas. Não são fotografias do Windows do usuário nem prova de acesso a provedores. São 61 capturas de páginas/estados no pacote de revisão; arquivos auxiliares de arte, SQLite e logs ficam fora dele.

| Tela | Captura versionada | Conferência |
| --- | --- | --- |
| Início | [home.png](evidence/ui-0.1.28/home.png) | Banner, continuidade e atividade em duas colunas. |
| Biblioteca | [library.png](evidence/ui-0.1.28/library.png) | Quatro capas verticais, nome/status e controles. |
| Ficha | [detail-overview.png](evidence/ui-0.1.28/detail-overview.png) | Barra, abas, metadados e galeria. |
| Desejos | [wishlist-prices.png](evidence/ui-0.1.28/wishlist-prices.png) | Cinco jogos, logos contidas e ações alinhadas. |
| Adicionar jogo | [add-selected.png](evidence/ui-0.1.28/add-selected.png) | Seleção/check, automação e avançado. |
| Configurações | [settings-connections.png](evidence/ui-0.1.28/settings-connections.png) | Quatro cards 2×2 e estados não configurados. |
| Conexões configuradas | [settings-connections-configured.png](evidence/ui-0.1.28/settings-connections-configured.png) | Bolinhas verdes e Gerenciar, presença simulada declarada, sem credenciais. |

Revisão completa local: `/workspace/work/checkpoint-0128-entrega`. Pacote sem bancos/logs: `/workspace/work/checkpoint-0128-entrega-artifacts/Checkpoint-0.1.28-ui-review.zip`. Janelas verificadas: 1000×700, 1100×740 e 1920×1080.

Diferenças restantes: artes e conteúdo das capturas são fixtures, portanto personagens/logos dos jogos das referências não aparecem; fontes, métricas, antialiasing, barra nativa e DPI podem diferir no Windows. O diálogo tem altura mínima maior para evitar sobreposição e preservar a prévia. Steam/Drive mantêm assets oficiais existentes; SteamGridDB/RAWG ainda usam monogramas herdados SG/R, e não os logos oficiais específicos da imagem. Tentativas de obter seus favicons encontraram restrição de rede nesta sessão; mantive identificadores existentes em vez de desenhar marcas falsas. Esses pontos impedem declarar igualdade pixel a pixel. A estrutura foi comparada visualmente, mas a aprovação estética pertence ao dono.

## Testes e comandos reais

Comando da suíte em cada etapa: `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests -q -p no:cacheprovider`. Fixtures usam pastas próprias, removidas após os testes. Smokes usam diretórios novos fora do checkout.

| Etapa | Resultado |
| --- | --- |
| Base 0.1.27, antes de alterar | 225 passaram, 168,33 s |
| Renomeação | 225 passaram, 173,51 s |
| Migração | 236 passaram, 170,10 s |
| Nove temas | 236 passaram, 161,46 s |
| Grades e compatibilidade de backups | 241 passaram, 160,64 s |
| Estrutura das telas de referência | 245 passaram, 193,58 s |
| Cadastro, posse e contadores | 249 passaram, 199,31 s |
| Geometria e placeholder, testes focados | 9 passaram, 1,89 s |
| Primeiro fechamento antes da revisão final de contadores | 251 passaram, 228,03 s |
| Após fechamento explícito das conexões de teste | 251 passaram, 281,86 s |
| Contadores Steam/calendário, testes focados | 27 passaram, 4,27 s |
| Fechamento final 0.1.28 — Linux | 252 passaram, 273,37 s |
| Windows CI final | 252 passaram, 174,51 s; build, smokes e capturas aprovados |

Na primeira rodada Windows houve 251 testes aprovados e três erros de limpeza: conexões SQLite abertas pelas verificações não foram fechadas pelo gerenciador de transação. As três leituras de teste passaram a usar `contextlib.closing`; o código de migração já o usava. As 12 verificações de migração passaram localmente após a correção.

Houve falhas intermediárias em expectativas textuais antigas (“Menor preço”, “artes”, “1 imagens”, contagens fracionadas da importação Steam) e na comparação de largura com/sem espaço de rolagem. Foram corrigidas, incluindo reserva estável da rolagem; não se omitiu a execução com falha nem se trataram testes parciais como suíte completa. Execuções intermediárias registraram 1 falha/240 aprovações na grade, 4 falhas/245 aprovações nos textos de artes, 1 falha/250 aprovações no singular de imagem e 1 falha/251 aprovações no texto antigo da importação em lote. A execução final acima passou integralmente.

O fluxo de cadastro em processo separado foi atualizado para selecionar uma fixture, sem acessar catálogo real.

Outros comandos/resultados:

```bash
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --smoke-test --data-dir /workspace/work/checkpoint-0128-ultimo-pages
# Checkpoint smoke: 6 pages OK; SQLite integrity=ok
QT_QPA_PLATFORM=offscreen .venv/bin/python -m checkpoint.app --save-smoke-test --data-dir /workspace/work/checkpoint-0128-ultimo-cadastro
# Cadastro smoke: salvar, auxiliar, renderização e SQLite OK
QT_QPA_PLATFORM=offscreen .venv/bin/python scripts/render_ui_review.py /workspace/work/checkpoint-0128-entrega
QT_QPA_PLATFORM=offscreen .venv/bin/python scripts/package_ui_review.py /workspace/work/checkpoint-0128-entrega /workspace/work/checkpoint-0128-entrega-artifacts
# Revisão visual: 61 PNGs e índice HTML; bases e logs excluídos.
.venv/bin/python -m pip check
# No broken requirements found.
```

Dependência local de build ausente foi instalada e o projeto reinstalado editável; scripts passaram depois disso. A versão do módulo e de pyproject foi conferida como 0.1.28. API pública GitHub respondeu HTTP 200; leitura de v0.1.27 retornou tag correta, release não rascunho e oito assets. Nada foi escrito em releases.

Windows CI concluído com sucesso em Windows Server 2022 x64/Python 3.12.10: **252 testes passaram em 174,51 s**, build concluído, validação de fonte/executável extraído e capturas concluídas. Execução: [Windows UI validation](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43368694510), código validado `124daab`. Artefatos novos: [pacote e revisão Windows](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43368694510/artifacts/14011324126) e [relatório de testes](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43368694510/artifacts/14011329615). Retenção configurada: 14 dias. As sete capturas versionadas neste relatório são as inspecionadas localmente em Linux; as capturas Windows do runner estão no artefato, sem afirmar inspeção no computador pessoal. Workflow de validação separado, com permissão somente de leitura e upload de artefatos novos; o workflow de release não inclui esta branch. Nenhuma publicação foi solicitada.

## Revisão de código e documentação

A busca encontrou `window.metadata` no botão “Pesquisar metadados manualmente” de Conexões > Avançado, e `metadata_dialog.py` é importado por esse método. Portanto ambos foram mantidos; a hipótese de código morto não se confirmou.

`dialogs.py` ainda concentra campos, validação e fontes antigas; `quick_add.py` reorganiza esses campos no cadastro rápido; `game_editor.py` os apresenta em abas para edição. Há sobreposição de composição, preenchimento e sinalização. Proposta futura: extrair um modelo de formulário e um controlador de seleção/enriquecimento compartilhados, mantendo cadastro e edição como apresentações separadas. A fusão não foi executada.

README, LEIA-ME, SETUP, INTEGRATIONS, PROJECT_STATUS, CONTINUITY, DESIGN, ARCHITECTURE, CLOUD_SETUP, TESTING, ROADMAP e notas atuais foram revisados. PROJECT_STATUS agora contém estado atual, pendências e limitações, sem hashes ou IDs de workflow. CHANGELOG reúne versões da 0.1.0 à atual, descrições antes misturadas à instalação e apêndice de caminhos renomeados. Evidence antigo recebeu identificação histórica; contagens e datas históricas não foram apresentadas como resultados novos. Exigências antigas de formato e paleta foram removidas da documentação operacional.

## Não validado e decisão humana pendente

Não foi aberto o programa no Windows do usuário, não foram usados seus dados ou credenciais, nem verificadas contas reais Steam, Drive, SteamGridDB, RAWG ou GG.deals. DPI, múltiplos monitores, renderização final no computador pessoal e satisfação estética exigem conferência humana. A presença de configuração simulada nas capturas não comprova login. Windows CI validou o runner e o executável nele, sem validar o computador pessoal.

Decisão de produto pendente: **o dono deseja futuramente unificar os três componentes de cadastro?** Nesta tarefa foram mantidos, com a sobreposição documentada. As demais decisões conservadoras e diferenças visuais estão explicitadas acima, sem substituir as referências por um layout novo.

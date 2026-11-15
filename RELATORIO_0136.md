# Relatório em andamento — Checkpoint 0.1.36

Base: 818ec80a492a29936782ddb3a43eecaf3ef996e3. Branch local fix/0.1.36-ajustes. Não publicada. Plano: PLANO_0136.md. Resultados atuais: RELATORIO_0136_TESTES.md.

Os três vídeos foram recebidos e quadros selecionados inspecionados. Não houve controle ou teste no Windows do dono. Capturas de referência e vídeos são evidência visual externa, não reprodução executada por este ambiente.

Registro por item e resultados serão acrescentados após testes. A4 e distinção ROM descarregada/emulador vivo permanecem separados, sem alteração dos contratos protegidos.

## 06 — captura global — parcial

Anterior: QShortcut limitado ao Checkpoint e retorno imediato se a janela não estivesse ativa. Vídeo não prova uma captura global executada. Reprodução controlada anterior: 8 testes existentes, captura bloqueada fora de foco conforme contrato antigo.

Implementado: RegisterHotKey/WM_HOTKEY com MOD_NOREPEAT, validação de combinação, substituição com registro novo antes de liberar o anterior, conflito visível sem salvar configuração inválida, liberação no fechamento aceito. Captura seleciona PID da janela em primeiro plano, exige processo de sessão vivo e associação única; não usa a ficha aberta para decidir. Valida HWND/PID/visibilidade antes/depois de obter pixels; erro não grava arquivo. Sem mudança na sessão por foco.

Arquivos/funções: checkpoint/global_hotkey.py (GlobalCaptureHotkey, WindowsHotkeyApi, native_key), game_capture.py (WindowsCapture, capture_game), window.py (inicialização, set_capture_shortcut, closeEvent); testes de captura 0135/0136. Expectativa antiga de app ativo substituída pela autorização explícita do item 06, preservando associação/arquivo e ausência de sessão.

Posterior: 10 testes Linux com adaptadores, dois jogos, troca/conflito/liberação, múltiplos PIDs, sessão encerrada/ambígua, atribuição e um arquivo por acionamento. Saídas integrais no relatório de testes. Referência nativa: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerhotkey.

Limitações: implementação nativa não executada em Windows nem em jogo/emulador real; QScreen.grabWindow pode não fornecer conteúdo de renderizadores exclusivos/DirectX (erro de imagem nula orienta modo janela, imagem preta não é validação positiva). Processos-filhos/launchers não associados são rejeitados, sem alegar suporte. Checkpoint em primeiro plano não é alvo elegível: ativar a janela do jogo. Windows com jogo/emulador/minimizado, conflito com outro app e pixels efetivos permanecem não testados.

## 04 — banner da ficha — parcial (relato Windows ainda não reproduzido)

Anterior: a implementação já usava KeepAspectRatio. Os testes existentes de bordas passaram. Não se comprovou o recorte relatado no Windows a partir do vídeo/faixa do Início. A primeira execução do novo teste falhou por ausência do método de inspeção banner_rect e por erro da fixture (add_wish não existe em Library); corrigida a fixture usando wishlist isolada, sem mudança de contrato ou asserção.

A área da imagem agora é calculada em banner_rect a partir da geometria atual a cada pintura e desenhada diretamente do pixmap original, sem cache escalado anterior. Removido cálculo de proporção sem uso. Fonte: checkpoint/ui_components.py::Hero.banner_rect/paintEvent/resizeEvent; testes/test_banner_resize_0136.py. Dois jogos de fixture (Aurora/Horizonte), duas proporções 1200×250/600×400, posse e Desejos, abrir em 1280×800/1920×1080 e repetir grande/menor/restaurado. Comparação de pixels das bordas superior/inferior e proporção/contain, sem deformação.

Screenshots sintéticas anteriores: antes-ficha-{1,2}-{1280x800,1920x1080}.png em evidencias-0136. Qt offscreen, DPR 1, 96 DPI lógicos; metadados antes-screens.json. Alteração não prova correção da ocorrência Windows. Maximização nativa e DPI do dono não testados; resize offscreen não equivale a homologação Windows.

## 02–03 — preços, identidade e desconto — parciais

Evidência: 2.mp4 01:31 mostra linhas Indisponível e ausência de ID; é quadro do Windows do dono, não reprodução autenticada. Antes: 11 regressões existentes passaram; 6 novos cenários falharam (preço PC aceito para console, desconto ausente, ordenação ausente, ausência sem motivo). Depois: 28 testes pertinentes passaram. Um teste novo tinha perdido a referência do widget pai; corrigida a fixture, preservadas as asserções.

Integração existente: API oficial quando há chave no cofre; fallback HTML público já existente e configurável. Nenhuma fonte nova nem coleta adicional adotada. Documentação primária consultada em 15/11/2026: https://gg.deals/api/prices/ e https://forum.gg.deals/d/2392-changelog-oct-14-2026-new-api-endpoints. API oferece app/sub/bundle Steam e by-slug (desde 14/10/2026). Resposta documentada traz mínimos atuais/históricos, moeda, título e URL; não documenta original individual, loja, plataforma ou edição. Slug não comprova suporte da API a consoles; cobertura do site não foi usada como prova. Sem credencial GG.deals disponível neste ambiente; nenhuma requisição autenticada/conta real ou jogo console com cobertura API foi validado.

Implementado: guardião de plataforma recusa atribuição de PC a Nintendo DS/Switch e outras plataformas ainda sem identidade comprovada; cache e IDs preservados. Não associa por nome e não baixa ROM. Motivo específico, sem preço zero. URLs antigas de comparação não são reutilizadas em consulta sem contexto compatível. Identidade contextual de oferta salva em settings, sem migração de schema ou alteração de registros de jogos/ROMs.

Desconto só é derivado de original maior que atual na mesma oferta individual classificada, BRL, link GG.deals válido, loja identificada e contexto Steam/plataforma coincidente. Original/histórico de agregados ou cache sem contexto não gera percentual. Arredondamento ao inteiro mais próximo, empate para cima; resultado arredondado zero não exibe desconto. O fallback público existente pode trazer essa oferta; API oficial atual não a fornece. Maior desconto ordena a oferta selecionada conforme política oficiais/keyshops; ausentes ao fim, desempate por título/ID estável. Nenhum histórico tratado como original.

Cards e painel da ficha usam Sem preço salvo com causa; retiradas linhas sem dado Indisponível. API e fonte pública mantidas, links/atribuição preservados. Testes: PC Portal 2/Hades II, consoles Zelda Phantom Hourglass/Metroid Dread sem atribuição PC, cache sem proveniência, contextos diferentes, moedas, ordenação/keyshops, original da mesma oferta e arredondamento. Fixtures não comprovam cobertura real.

Arquivos: checkpoint/prices.py (platform_problem, selected_quote, refresh_prices, wishlist_order); price_view.py (source_url, price_summary, comparison); collection_views.py (ordenação); testes/test_price_integrity_0136.py. Expectativa test_price_display_official da ordenação discount substituída pela autorização do item 03; preservados atribuição e fila sem Steam. Demais testes históricos com original agregado continuam recusando desconto, pois não têm oferta/contexto confiáveis.

Bloqueio restante 02: comprovar resposta autenticada por slug para uma edição console e sua plataforma/BRL, antes de criar vínculo editável explícito de provedor/edição. Proposta: validar produto exato em conta disponível no Windows, guardar slug+plataforma+edição+região+proveniência por confirmação; não inferir de título. Nenhuma mudança de schema necessária enquanto persistência de identidade em settings for suficiente.

Bloqueio restante 03: não há original individual na resposta oficial documentada. Proposta de recorte: manter mínimos oficiais sem desconto na API; exibir desconto apenas para ofertas individuais do fallback já habilitado quando comprovadas, ou aguardar contrato detalhado do provedor. Não adotar scraping novo nem outra fonte sem decisão específica. Nenhum suporte universal declarado.

## 07–08 — Estatísticas e períodos — feito no ambiente Linux

Anterior: screenshot antes-tela-4-1280x800.png reproduziu cards equivalentes com alturas desiguais (com/sem subtítulo), sem reproduzir tooltip nativo do dono. Fonte solicitada Segoe UI, DPR 1, 96 DPI lógicos; gravações 1280×720 não comprovam DPI do Windows. Ausência de serviço/filtros novos registrada pela primeira execução (erro de importação, não reprodução de defeito temporal).

Implementado: cards temporais alinhados, altura/linhas equivalentes; nome longo elidido com título íntegro acessível/tooltip, valor separado sem disputar espaço. Período visível com Diário, Semanal, Mensal, Últimos 3/6/12 meses e Todo o período; preferência persistida. Métricas temporais/heatmap/mais jogados/conclusões usam o mesmo recorte local. Coleção atual (status, jogos, gêneros, plataformas, total app + maior snapshot Steam por jogo) separada; nenhum snapshot Steam distribuído pelo calendário. Sem alegação de deduplicação temporal entre app e Steam.

Limites: [início,agora), dia/mês atuais, semana segunda-feira; janelas móveis subtraem meses de calendário preservando hora, dia limitado ao último do mês destino. UTC guardado permanece intacto; limites e meia-noite calculados no fuso local do sistema ou fuso explícito nos testes; duração da sessão reparte instantes até o limite, incluindo DST de 23/25h. Todo o período também exclui instantes futuros. Fuso não fixado no Brasil. Não recria banco/schema. Agregado Steam permanece somente em Tempo total · app + Steam.

Arquivos/funções: checkpoint/statistics_periods.py (period_bounds, period_stats, instant), statistics_view.py (metric, GameNameButton, render_statistics, build_statistics), activity_heatmap.py (set_interval/interval). Cobertura inclui dois jogos, meia-noite, ano, semanas/mês/mês com dia limitado, janela vazia, snapshot Steam alto que não entra no recorte, DST e preservação exata dos registros. 1280×800/1920×1080 com sete filtros, limites dos labels e alinhamento. Expectativa fixa de 365 células em test_wishlist_prices atualizada para os dias do intervalo móvel de calendário; preservados tempos e agrupamento local, conforme item 08.

Capturas da implementação: estatisticas-tela-4-{1280x800,1920x1080}.png; dados isolados (Portal 2/Metroid Fusion), não banco pessoal. Captura 1280×800 enviada no chat para revisão. Fontes reais/renderização Windows e tooltip no PC do dono não testados; sem mudança global de fonte.

## 09 — Mais estatísticas — feito

Antes: dois testes falharam pois gêneros/conclusões estavam escondidos pelo disclosure. Removido o botão e integrado seu conteúdo na página, sem apagar dados. Arquivos: checkpoint/statistics_view.py::render_statistics; tests/test_statistics_visible_0136.py. Dois jogos de fixture, gênero/status preservados; dez testes pertinentes passaram.

Complemento solicitado durante revisão no chat: a primeira captura de Estatísticas tinha sobra excessiva abaixo da legenda. Substituída altura fixa de 252px por HeatmapViewport, que acompanha a altura calculada do gráfico e eventual barra horizontal; ActivityHeatmap emite height_changed. Teste verifica tamanho ajustado nos sete períodos e duas resoluções, sem retirar rolagem da página. Capturas calor-compacto-tela-4-1280x800.png e calor-compacto-tela-4-1920x1080.png enviadas no chat; reduzem a sobra sem reduzir fontes. Não houve reescrita do commit anterior.

## Complemento do item 07 — Mais jogados como lista da Biblioteca

Solicitado no chat após revisão das capturas: logo à esquerda, nome no meio e tempo à direita. Novo commit, sem reescrever anteriores. Duas fixtures antes falharam porque não havia linhas com logo. Implementado em statistics_view.py::render_statistics, usando list_art.list_icon para logo contida igual à Biblioteca; capa contida/ícone neutro quando falta logo. Nome elidido com título completo no tooltip/acessibilidade; tempo em coluna separada, linha clicável pelo nome. Testes/test_statistics_list_0136.py verifica dois jogos, ordem por tempo, colunas sem sobreposição e duas janelas. Filtros temporais preservados.

## 10 — cinco tamanhos de capa — feito no ambiente Linux

Antes: 3.mp4 00:20 e screenshots anteriores mostram slider longo e três exemplos pequenos. As 13 regressões antigas de layout/serviços passavam; mudança de produto solicitada explicitamente, não falha desses testes. Slider removido, cinco escolhas clicáveis 70/90/100/125/150 (faixa 70–150 já suportada), crescimento visual, base comum, verde, foco e teclado com setas/Espaço/Enter. A opção altera a grade e persiste ao reabrir.

Preferências antigas mantidas no SQLite até nova escolha: 87 é representado/aplicado como 90. Empate vai para menor; extremos fora da faixa mapeiam ao extremo; inválido usa 100. Configurações não recriadas nem migração de schema. cover_size continua lendo valor legado original; nearest_cover_choice governa apresentação/aplicação inicial. Compact antigo de 80 é exibido como 70 por empate, sem apagar a preferência.

Arquivos: checkpoint/settings_previews.py (CoverChoice/CoverSizeChoices), settings_view.py (build_settings), card_layout.py (COVER_CHOICES/nearest_cover_choice), window.py (refresh_library). Removida classe antiga de três exemplos. Expectativas de slider em tests/test_cover_preview_0135.py/test_card_layout.py substituídas pela autorização do item 10, mantendo cobertura de largura, base, cor, proporção, ausência de sobreposição, persistência e efeito na grade. 23 testes pertinentes passaram; duas fixtures de jogos, resoluções 1280×800 e 1920×1080, extremos e preferência 87, teclado/foco.

## 11 — centralização óptica Steam — feito no raster Linux, Windows não testado

Investigados container 48×48, pixmap Steam 32px/Drive 36px, margens/cores e centro geométrico versus massa dos pixels claros. O ICO contém pixels opacos nos cantos; cortar pelo canal alfa não melhoraria a marca. Medição no raster exibido encontrou centro claro deslocado à esquerda/abaixo. Ajustada somente apresentação em +2px horizontal e −1px vertical; normalizado DPR do pixmap para 1 antes de compor o canvas lógico. Marca inteira contida e comparação de ocupação com Drive preservada. Nenhum redesenho, iniciais ST ou Lucide para serviço.

Arquivo original checkpoint/assets/services/steam.ico intacto; SHA-256 9f890a9debcdfccc339149a7943be9aff9e4c9203c2fa37d5671a5b2c88503ad. Arquivos/funções: ui_components.py::service_icon; tests/test_service_optical_0136.py. Primeira compensação de 1px ainda falhou na medida de centro; aumentada para 2px sem alterar tolerância do teste. Nove regressões passaram, incluindo dois jogos e ocupação relativa Steam/Drive. Captura revisao-conexoes-1280x800.png enviada no chat. Testes de raster não equivalem à aprovação óptica do dono nem DPI Windows.

Complemento de revisão da lista: dono aprovou o estilo e pediu mais destaque no tempo. Mantido layout; apenas o tempo recebeu 16px, peso 600 e cor principal, alinhado à direita. Nove testes pertinentes passaram. HeatmapViewport passou a habilitar explicitamente rolagem horizontal quando necessária (a classe-base a desativa); sem remover rolagem de página.

## 01 — tempo em Desejos e posse — feito

Antes: dois cenários falharam por tempo 2h15min visível no card. A ficha exclusiva já ocultava tempo; preservado. Removido apenas o rótulo temporal dos cards de Desejos. Sessões, snapshots, notas e metadados não apagados.

Para coexistência Biblioteca/Desejos, collection.unowned=false explícito agora conserva posse mesmo com wishlist, enquanto ausência de flag mantém semântica legada (wishlist é exclusiva). Adicionar aos desejos pelo menu de jogo possuído grava false, sem retirar da Biblioteca; retirar dos desejos conserva posse. Adição pelo diálogo que reutiliza identidade existente permanece no contrato anterior protegido por regressão: informa que já pertence à Biblioteca. Aquisição exclusiva preserva registro e histórico.

Arquivos/funções: collection_views.py::build_wishlist; library.py::is_owned/owned_games; window.py::add_wish/remove_wish; tests/test_wish_time_0136.py. Testados dois jogos/fixtures, desejo exclusivo, aquisição, coexistência e retirada, tempos Biblioteca e comparação integral das sessões antes/depois. 29 regressões pertinentes passaram. Sem migração de schema nem apagamento/reescrita de instantes.

Complemento do item 10 solicitado no chat: margens externas das cinco capas estavam desiguais apesar de colunas iguais. Reproduzido por quatro testes nas duas janelas: diferença de 31,29px entre bordas esquerda/direita. CoverSizeChoices passou a distribuir pelos contornos reais da arte, com seis vãos equivalentes (externos e internos), conservando proporção, base, foco e escolha. 21 testes pertinentes passaram, sem afrouxar a tolerância nova de 1–2px de arredondamento.

## 05 — descrição no Início — feito

Antes: duas comparações de pixels falharam porque a descrição alterava a imagem pintada do Hero. Retirado apenas o bloco de pintura sobreposta em ui_components.py::Hero.paintEvent. Banco, descrição em Sobre o jogo, arte/logo, plataforma/status e Continuar jogando preservados. Nenhum slogan substituto. Quinze testes pertinentes passaram, incluindo dois jogos, persistência da descrição, ação dentro do banner e redimensionamentos/contain.

Composição: imagem continua contida e proporcional na área; letterbox necessário quando proporções diferem não foi tratado como prova de recorte. Não foi introduzido preenchimento que corte a arte para eliminar faixa. A ocorrência da ficha Windows permanece separada no item 04. Capturas posteriores serão registradas no índice final.

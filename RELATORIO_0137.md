# Relatório 0.1.37 — implementação e validação

## Resultado final da publicação

Pré-release publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37

- Tag/código: c526cb4bc5e8721dfdfdf20222c8c1c41562ce52, conferido por ls-remote.
- Workflow 43793047592: build e publish success, nenhuma falha/skip/erro na suíte final Windows.
- Windows/Python 3.12.10: 695 passed in 638.21s (0:10:38).
- Linux/Python 3.12.14: 695 passed in 478.98s (0:07:58), após a correção de limpeza do teste.
- Fonte e executável realmente extraído: smokes de seis páginas, cadastro, auxiliar, SQLite e atualizador aprovados.
- Oito arquivos publicados baixados e conferidos por tamanho e digest GitHub SHA-256; CRC dos dois ZIPs válido.
- ZIP Windows: 84312887 bytes; SHA-256 54a99c68269935918bdac58a810de611569b600a031c953b63c1287e55880e6a.

Primeiro candidato a33f48a foi substituído antes da publicação por correção restrita ao teste; o run interrompido não é apresentado como aprovado. A tag 0.1.36 continua em 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Não houve force, alteração de workflow/asset/protegido, PR ou movimento de tag anterior. Atualizações documentais posteriores não mudam a tag lançada.

Permanecem as limitações de capacidade da fonte console/original individual, uso real com UAC/moldura/captura/launchers/contas/emuladores/DPI/monitores no PC do dono, A4 e fechar só a ROM. Runner Windows/pacote aprovados não homologam esses cenários pessoais. Elevação para outra conta é recusada para preservar dados/cofre. Isso está nas notas públicas; a rodada inteira não é chamada de concluída com pendências importantes.

Detalhamento e etapas anteriores abaixo; saídas Windows completas em RELATORIO_LANCAMENTO_0137.md.

Base: 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1 de fix/0.1.36-ajustes; remoto reconfirmado e checkout inicial limpo. Branch: fix/0.1.37-ajustes. Fase inicial sem autorização de publicação; o dono autorizou posteriormente lançar a versão depois das verificações. Essa autorização nova será executada após o fechamento local e validação Windows, com resultado em RELATORIO_LANCAMENTO_0137.md. Código, tag e assets publicados da 0.1.36 permanecem preservados.

Pedido: documento enviado em 15/11/2026, com imagens A (Início integrado) e B (lista horizontal). Vídeos p1–p4 ausentes neste chat: horários e problemas citados são relatos, não testes diretos. Capturas futuras do app usarão dados sintéticos isolados e serão identificadas. Não confundir Linux/Qt offscreen com Windows real do dono.

Plano e ranking de ofertas: PLANO_0137.md. Registro por item será atualizado com requisito, evidência antes/depois, reprodução, arquivos/funções, commit, testes, resolução/escala, limitações e status. A4 bloqueado; troca automática de ROM descartada; encerramento apenas da ROM permanece limitação conhecida.

## Estado inicial comprovado

- Lista usa QTableWidget com cabeçalhos Logo/Jogo/Plataforma/Status/Gênero/Nota: diverge da imagem B e do item 5.
- Início atual escolhe Jogando/Pausado e pode usar updated_at: não representa necessariamente uma execução. Novo bloco usará play_sessions criadas após Popen bem-sucedido, sem fabricar histórico.
- Grade decodifica cover_pixmap em cada paint e refresh_library reconstrói grade e tabela; medir antes de atribuir o travamento do PC do dono a essas operações.
- Períodos têm rótulos Diário/Semanal/Mensal; item 8 solicita Hoje/Esta semana/Este mês, com semântica preservada.
- Perfil só seleciona imagem e faz recorte central ao apresentar: faltam posicionamento/zoom/recorte editável.
- Schema 4; play_sessions existente fornece início, PID e estado. Não há necessidade identificada de nova tabela para jogos recentes.
- Fonte GG.deals atual: API agregada Steam/BRL, sem original individual/plataforma/edição na resposta documentada. Cobertura de consoles autenticada ainda não comprovada; investigar sem consultar cofre real.

## Item 8 — rótulos e compatibilidade (feito, validação Linux)

Antes: 6 falhas na regressão nova, em dois jogos, mostrando Backlog e Diário/Semanal/Mensal. Depois: 26 testes direcionados aprovados, incluindo contratos protegidos. Ficha, filtros, grade, hero, editor (via STATUSES importado) e composição estatística mostram Não iniciado. Library.clean_game_data continua aceitando Backlog legado; abrir a ficha não regrava; filtro Não iniciado inclui ambos os valores e stats agrega sem perda. Nome: A–Z e Adicionados recentemente mantêm as chaves title/recent e created_at; Desejos usa Nome: A–Z/Menor preço/Maior desconto. Períodos mantêm chaves e limites.

Arquivos/funções: library.py (STATUSES/display_status/clean_game_data/games/stats), detail_view.py (build_detail), cover_grid.py (paint), ui_components.py (Hero/GameTile), statistics_periods.py (PERIODS), statistics_view.py (StatusRing), window.py (build_library), collection_views.py (build_wishlist). Nenhum protegido editado. Testes de status 0135/0136 tiveram somente a expectativa Backlog substituída pelo rótulo explicitamente aprovado Não iniciado; preservadas persistência, cinco opções, tema, foco, menu e ausência de regravação. Nova cobertura testa o valor Backlog efetivamente salvo antes de abrir. Sem migração ou mudança de schema. Windows real não testado. Commit desta unidade identificável pelo título fix: aplicar rótulos aprovados da 0.1.37; SHA será relacionado no índice final.

## Item 4 — dados do Início (feito, serviço Linux)

Novo home_data.py: execution_history/recent_games/ week_summary/wish_offers/recent_memories. Registros recentes exigem PID positivo, estado conhecido e início UTC válido não futuro; ordenação por instante/ID, um card por jogo, independente de status/updated_at. Linhas legadas sem PID não são usadas como prova de lançamento. Histórico detalhado preserva cada sessão. Sem nova persistência/schema.

Resumo semanal reutiliza period_stats: segunda-feira 00h local até agora, tempo recortado, sessões finalizadas com duração positiva que intersectam o período; Jogos iniciados conta jogos distintos cujo início finalizado pertence à semana. Ativas/interrompidas não entram até finalização/revisão. Sessão iniciada antes da semana pode contribuir tempo/sessão sem contar como jogo iniciado nela. Steam agregado não participa. Fuso parametrizável, sem regravar instantes.

Ranking viável: desconto individual confiável primeiro, percentual decrescente; restantes por nome/ID. Mesma selected_quote e política oficial/keyshops de Desejos. Só state=ready e preço positivo/classificado entram; último cache após falha não é anunciado como oferta atual. Sem histórico fabricado. A tabela price_history existe no schema, mas não é alimentada pelo fluxo atual e não comprova edição/plataforma/observações comparáveis; não foi usada como indicador de redução.

Antes: quatro falhas por serviço inexistente. Depois: 22 testes aprovados, incluindo dois pares de jogos, limites de semana, futuros/PID ausente, Steam, cache/console sem cobertura e regressões estatísticas/preços. Imagens anteriores em evidence-0137/antes, 1280×800/1920×1080/1000×700 (fixtures Qt Linux). Captura do Início anterior enviada no chat. UI do novo Início ainda em implementação; não confundir serviço pronto com tela pronta.

## Complemento — ROM local (incorporado, em diagnóstico)

Já existem game_files para caminho/plataforma/estado local e rom_versions.profile_id; EmulatorCommand passa a ROM por argumento sem shell e Launcher acompanha o processo e grava sessão após Popen. Falta seleção local na ficha: link_rom abre exclusivamente RomLinkDialog/Drive. candidates admite substring do título e ausência de plataforma amplia resultados; risco Ocarina of Time versus 3D será tratado sem afirmar associação errada concluída. Plano ampliado sem reiniciar ou descartar commits. Nenhum protegido precisa ser editado no desenho inicial.

## Item 4 — Início integrado e revisão com o dono (feito em Linux, revisão visual em andamento)

Arquivos: home_view.py::build_home, home_components.py::RecentArtwork/RecentGameCard/GameStrip/OfferLogo/SingleLineInfo/MemoryCarousel/show_execution_history/open_memory; home_data.py::recent_games aceita limite opcional. Histórico usa sessões reais com PID; Continuar jogando aciona execução/configuração, arte e ação de ficha só abrem ficha; memória de texto abre leitura sem sobrescrever rascunho. Ver estatísticas escolhe weekly; Ver desejos/Memórias navegam à aba correta. Carrosséis com setas/teclado e limites desabilitados. Sem escrita em sessões/mídias ao navegar.

Complementos do dono durante a implementação, prevalecendo sobre o molde inicial: capa em vez de banner nos recentes; depois três jogos em carrossel horizontal, com área exatamente proporcional à imagem, sem recorte, faixas laterais ou corte de cantos. Base do bloco recente alinhada à base das ofertas. Título Ofertas, linhas consecutivas no topo (centralização vertical rejeitada), logo do jogo na linha (capa rejeitada), nome/contexto no meio e preço à direita sem caixa. Nos recentes: plataforma removida; status/última vez/tempo total em três linhas sem quebra. Data curta local, completa no tooltip. Plataforma mantida em Ofertas por integridade da edição, conforme escopo.

Capturas reais Qt/fixtures Linux enviadas no chat: antes, inicio-v1, inicio-capas-v2, inicio-ofertas-v4, inicio-carrossel-v5, inicio-ofertas-v6, inicio-ofertas-v7 e inicio-v8, em /workspace/work/evidence-0137; script também gera 1920×1080 e 1000×700. Tentativa v2 gerou capas altas e conteúdo distribuído; revisada. V4 tinha dois jogos e área limitada; substituída pelo carrossel de três e proporção exata após pedido do dono. Não alegar aprovação visual pelo simples envio de capturas.

Validação: 33 testes direcionados passaram em 13,09 s, incluindo renderer completo, antes/depois, ações independentes, períodos, favoritos, Desejos, limites dos carrosséis, quatro bordas de capas em dois jogos/resoluções e origem logo sem capa. Falha intermediária da comparação de descrição ocorreu por reflow pendente, com imagens de larguras diferentes; comparação passa após estabilizar eventos Qt, preservada igualdade exata de pixels e texto externo na ficha. Tests home_0129/reference_layout_0128/home_description_0136 adaptados ao requisito explícito: histórico comprovado em vez de status, carrossel/ações fora da arte em vez de hero único. Fixtures agora têm início/PID; preservadas cobertura de descrição/resize/ações/dados. Nenhum protegido alterado. Windows real e aprovação estética final permanecem pendentes.

## Complemento posterior — Ofertas sem imagem (feito em Linux, revisão visual)

Última instrução do dono substitui o pedido anterior de logo: linha só com nome, original riscado, desconto e atual. Removido OfferLogo; plataforma/origem não aparecem nesse resumo, mas validação de identidade/contexto e preferência de lojas continua no serviço. Original/percentual são omitidos se a mesma oferta não os sustentar, sem usar histórico nem 0% fictício. Lista permanece imediatamente abaixo do título Ofertas; sem centralização vertical, sem caixas de preço e sem imagens. Captura real Qt/fixtures inicio-v9 enviada no chat, 1280×800, com demais resoluções geradas pelo script. Nova regressão verifica quatro campos, riscado, percentual, ausência de logo/plataforma e valor preservado. Revisão estética segue aberta; nenhuma nova fonte/autenticação real foi usada.

## Item 5 — Biblioteca em lista (feito em Linux, revisão visual)

Antes: tabela de seis colunas; nova regressão teve 4 falhas por ausência do componente. Depois: LibraryList/ListDelegate em library_list.py pinta cards horizontais de altura uniforme com logo contida, nome elidido quando necessário, tempo XhXXmin e coração. Sem tabela, cabeçalhos, status/plataforma/gênero nas linhas ou tooltips; filtros e abas existentes preservados. Qt AccessibleText informa nome/tempo/favorito; Enter abre e Espaço alterna favorito. Clique no coração é consumido antes da ativação do item e mantém Biblioteca; abrir ficha conserva comportamento anterior.

window.py::build_library/refresh_library/open_selected/toggle_favorite substitui table por game_list. Reutiliza itens quando IDs/ordem não mudam, preserva posição após layout e separa favorito da navegação. Grade/lista continuam usando mesma busca, filtros e ordenação. Favoritos e dados não apagados. Imagem real Qt da lista enviada no chat: inicio-v10/1280x800-list.png, fixtures isoladas; script gera demais resoluções. Arquivos publicados/assets protegidos intactos.

52 testes direcionados aprovados em 6,22 s: lista, clique/teclado de favorito, nome longo, busca/ordenação, logo versus capa, navegação, Desejos e Início. Asserções legadas de QTableWidget/ícone por célula em test_layout_0134/test_ui/test_folder_platforms foram substituídas por cards e pintura real, preservando cobertura de logo verde, ausência de capa vermelha, imagem azul e quantidade de jogos. Testes antigos de home no test_ui_redesign adaptados à execução comprovada e novos blocos; geometria comparada no mesmo sistema de coordenadas. Falha intermediária de edição/indentação e expectativas antigas estão integralmente no registro, corrigidas e repetidas. Sem skip/xfail nem mudanças protegidas. Fluidez do Windows do dono ainda não validada; benchmark de grade é unidade separada.

## Complemento — prévia de banners nas Ofertas (implementado em Linux, revisão visual pendente)

Após pedir apenas nome/preços, o dono propôs um banner por linha. OfferBanner reutiliza arte proporcional sem logo sobreposta e sem recorte; nome/original/desconto/atual ficam abaixo. Sem banner disponível, mantém a linha de dados. Não muda identidade, ranking ou fonte. Prévia inicio-v10 enviada no chat; não presumir aprovação estética. Teste novo verifica as quatro bordas em larguras 300/480/680, banner em vez de capa e repetição de resize. 18 testes de Início/dados passaram; incluídos também na rodada de 52 regressões. Nenhuma informação comercial inventada; valores da imagem são fixtures declaradas.

## Item 6 — grade, cache e atualização (feito em Linux; Windows do dono não homologado)

Medição antes/depois com 500 jogos e 100 PNGs distintos 300×450, janela 1280×800, mesmo benchmark isolado. Antes: inicialização 1,747 s; refresh 0,759–0,788 s; mediana de quadro 27,25 ms; pico RSS 389.916 KiB. Depois final: inicialização 0,151 s; refresh 0,0346–0,0364 s; mediana de quadro 8,08 ms; pico RSS 107.904 KiB. Não é FPS garantido nem reprodução do travamento no PC do dono. Posição preservada antes/depois de refresh em ambas as rodadas.

Mudanças: artwork_cache.py::ArtworkCache mantém LRU de rasters escalados sob demanda (32 MiB grade, 8 MiB lista), invalida por caminho/mtime_ns/tamanho/dimensões e limita imagens; logos têm somente margem transparente removida na apresentação. Nenhum asset original alterado. CoverGrid/CoverDelegate usam cache e arte inteira (sem fill com recorte); ausência de imagem mantém título. CardMetrics e art_rect equilibram margens e vãos, preservando alinhamento da última linha; reserva final de um pixel evita quebra de coluna no QListView. Tentativa intermediária sem essa reserva reduziu colunas indevidamente, falhou no teste e foi corrigida antes da medição final.

playtime.collection_times agrega sessões e MAX Steam separadamente, depois combina por jogo, sem joins multiplicadores. Teste com 100 jogos encontrou 401 consultas antes; agora no máximo 8, valores idênticos (local + maior snapshot). Refresh da lista/grade já reutiliza itens e não decodifica toda a biblioteca na construção. A contagem total de SQL do benchmark subiu de 10 para 15 por trazer os tempos da nova lista, mas não cresce por jogo e o tempo total caiu. Nenhum temporizador de contorno.

91 testes aprovados em 48,34 s: margens/colunas, imagem atualizada, limite de cache, totais, roda com 500 jogos, scroll preservado, lista, fontes, preferências, contratos protegidos e imagens. Saídas integrais e benchmarks em RELATORIO_0137_TESTES.md e /workspace/work/evidence-0137/bench-antes/bench-final; captura biblioteca-v1 enviada no chat. Nenhuma mudança de schema ou dado pessoal.

## Complemento — rótulo Alfabeticamente

A instrução posterior do dono substitui Nome: A–Z por Alfabeticamente na Biblioteca e Desejos; chaves title/name e ordenação permanecem. Combo da Biblioteca ampliado para exibir também Adicionados recentemente sem corte. Teste de rótulos atualizado somente no texto autorizado. Não altera filtros, dados ou precedência de ordenação.

## Item 9 — gráficos por período e remoção de Gêneros (feito em Linux, revisão visual)

Antes: a semana usa a mesma grade anual e ocupa coluna estreita. Novos testes tiveram quatro falhas. Implementado period_chart.PeriodChart: Hoje mostra distribuição horária de sessões locais reais; Esta semana tem sete posições de dias; mês usa calendário com dias e tooltip; períodos maiores usam mapa de calor compacto. Primeira proposta com meses em linhas e 31 colunas foi rejeitada expressamente no chat; substituída antes do commit, capturas estatisticas-v1/v2 documentam a revisão. Não considerar a proposta rejeitada uma aprovação.

Gráficos menores ficam ao lado de Mais jogados quando há largura, com empilhamento na janela menor; históricos extensos mantêm rolagem necessária para não cortar células. Preservadas métricas, valor destacado e lista com logo/nome/tempo; nome sem caixa de botão. Removida seção Gêneros da coleção e sua lista; gêneros no banco/ficha preservados. Teste antigo de disponibilidade dos gêneros foi atualizado para exigir ausência na tela e permanência nos dados, conforme item 9.2; conclusões continuam presentes.

statistics_periods.day_hours reparte sessões finalizadas entre intervalos horários reais do dia local, sem inventar datas Steam, inclui 23/25 horas em transições DST e mantém instantes. Sem mudar semântica de period_stats. 25 regressões finais aprovadas em 3,51 s; antes da revisão, 31 regressões da primeira proposta também passaram, mas isso não validou estética. Capturas reais Qt semana/12m enviadas no chat; script gera dia/mês/12m/todo período em três resoluções. Windows real não homologado.

## Item 14 — foto de perfil editável (feito em Linux)

Antes: escolha de arquivo com recorte central fixo; três formatos de teste falharam por ausência de editor. avatar_crop.AvatarCrop implementa recorte quadrado, arrasto/teclas, zoom 100–400%, limites na imagem, orientação e prévia circular. profile_dialog.ProfileDialog valida formato/tamanho, usa QImageReader com autoTransform, permite escolher/remover/salvar/cancelar. Original em disco nunca alterado; cópia imutável do original e avatar recortado de 256×256 ficam no ImageCache. profile.avatar_original/profile.avatar_crop usam settings existentes; schema 4. Estado/nome/avatar são gravados numa transação; cancelar não altera preferências.

7 testes aprovados em 0,59 s na rodada com orientação/arrasto (além de regressão de tema anterior): paisagem, retrato, pequena, arquivo inválido, zoom/reposicionamento, cancelamento, reabertura, original byte a byte e JPEG com EXIF de rotação 90°. Leitura da imagem aplica orientação sem regravar o arquivo de origem. Captura real Qt de perfil-v1/profile.png enviada no chat com imagem sintética; sem foto pessoal. Seletor nativo/Windows do dono não homologado. scripts/render_0137_review.py seleciona a imagem sintética pelo mesmo select_photo usado pela interface, sem salvar a fixture na biblioteca pessoal.

## Complemento — indicador circular do Zoom (feito em Linux)

Por pedido posterior do dono, profile_dialog.py aplica thumb circular de 14 px ao controle Zoom, usando a cor do tema; faixa, limites, teclado e valor inalterados. Captura real perfil-v2/profile.png enviada no chat. Mudança de estilo reversível verificada por renderização, sem teste que apenas repita CSS.

## Complemento — vincular e executar ROM local (feito em Linux; emuladores reais não homologados)

Já existiam game_files.local_path/available/platform/extension, rom_versions.profile_id, EmulatorCommand e Launcher.start_command. Faltava a seleção local pela ficha. Reutilizados esses serviços e schema 4; nenhuma alteração de banco pessoal, protected file ou A4.

Novos local_rom.py::validate_path/compatible_profiles/identity_problem/bind_local e local_rom_dialog.py::LocalRomDialog/RomSourceDialog. Ficha oferece Escolher ROM local e Vincular ROM do Drive; substituição abre seletor de origem. Seletor de arquivo Qt usa o padrão nativo na plataforma, valida existência/leitura, exibe caminho/plataforma/perfil e só grava ao confirmar. Perfis locais exigem extensão explicitamente declarada, plataforma compatível, executável existente e argumentos com {rom}; nenhum suporte universal a compactados. Ausência oferece configuração. Título divergente sem identidade comprovada exige confirmação; plataforma/edição claramente diferente é bloqueada e oferece outra ficha/cadastro. Nenhuma reidentificação automática ou atribuição de preço cruzada.

bind_local usa transação/serviço atomic existente, só cria/atualiza vínculo e perfil, desvincula índice anterior sem apagar arquivo/versões e preserva metadados, memórias e sessões. Sem Drive/cofre/download/upload, cópia ou renomeação da ROM. Jogar usa o perfil salvo e passa o caminho real ao EmulatorCommand; Launcher monitora o processo. Arquivo ausente oferece localizar novamente sem apagar vínculo/histórico. Extensão de registro legado vazio é derivada do arquivo real em memória, sem migração destrutiva.

Drive pela ficha: rom_link.complete_link rejeita plataforma/edição divergente antes de bind/download e valida plataforma do resultado de catálogo antes de complete_identity. rom_link_dialog mantém o fluxo de acerto, mostra correção para divergência, permite escolher outra ficha/cadastrar e pede confirmação explícita para título não exato. Bind genérico, cadastro protegido e arquivos A4 permaneceram intactos. Removida frase tutorial do diálogo; estado sem candidatos mantém ação concreta.

Reprodução controlada confirmou risco no worker antigo: Ocarina of Time/3D chegava ao download e alterava vínculo antes da rejeição; isso não prova que o dono concluiu a associação na captura original. Agora testes de plataforma preenchida/vazia impedem vínculo, download e alteração de metadados, inclusive quando a GUI não chega a listar o candidato.

49 regressões finais aprovadas em 3,73 s: dois programas CHIP-8 originais de teste (00e01200 e 00e0600170011204), caminhos com espaços/acentos, perfil/compatibilidade/extensão, leitura negada controlada, substituição preservando ambos os originais, cancelamento, clique de confirmação, reabertura, arquivo ausente/relocalização, subprocesso lendo exatamente a ROM escolhida e encerramento finalizando sessão; Drive e contrato protegido também passaram. Os programas são dados próprios/legalmente disponíveis; o executor Python controlado valida seu conteúdo/caminho e sai, não é homologação dos emuladores reais do dono. Falhas intermediárias registradas: registros de teste antigos tinham plataforma PC para ROM de console e extensão de perfil vazia; fixtures corrigidas para plataforma/extensão efetivas, sem afrouxar rejeição nem mudar asserções de sessão. Duas rodadas locais presas em modais inesperados foram interrompidas (exit -15), corrigidas e repetidas; nenhum workflow remoto foi cancelado.

Capturas Qt reais enviadas: rom-local-v1/rom-origem.png, rom-local.png; rom-local-vinculada.png também gerada após gravação real na base isolada. Seletor nativo Windows, jogos/emuladores reais e uso elevado não homologados neste Linux. Fechar apenas a ROM com emulador vivo continua limitação; troca automática descartada, não implementada. Arquivos: local_rom.py/local_rom_dialog.py, window.py (start_game/launch_rom/link_rom/choose_local_rom/link_drive_rom), detail_view.py (Arquivos), rom_link.py/rom_link_dialog.py, script de revisão e testes pertinentes.

Complemento de rótulo aplicado junto à ficha: filtro de plataforma mostra Todas, com chave vazia e filtragem inalteradas, conforme pedido posterior.

## Complemento — texto Carregando prévia sem corte (feito em Linux)

Reproduzido com Pokémon FireRed and LeafGreen+ e Ocarina of Time 3D: QLabel de 70×94 sem quebra cortava a mensagem. Somente QuickAdd.show_result foi alterado, dentro da exceção autorizada: aplica estilo antes de medir a fonte, largura suficiente para Carregando e quebra do placeholder em linhas que cabem na altura. Pixmap continua contido ao chegar. Título, fonte, seleção de ROM, jobs e contratos de persistência/lifecycle intactos; não editados construtor/choose/received ou dialogs.py.

Antes: 2 testes falharam; depois: 18 testes passaram em 1,79 s, incluindo QuickAdd e contrato AST protegido. Captura real Qt do estado de carregamento reproduzido com dados controlados enviada: evidence-0137/previa-carregando/preview.png, diálogo 760×700. Não é consulta autenticada ou homologação da gravação no PC do dono. Sem fonte fictícia publicada nem alteração de dado pessoal.

## Complemento do item 6 — pequenas pausas na rolagem (implementado e validado em Linux)

Após o relato posterior do dono, inspeção confirmou QImageReader.read/escala dentro de ArtworkCache.load, chamado pelos delegates durante paint. O cache existente evitava repetição, mas a primeira apresentação de uma imagem ainda fazia esse trabalho na thread da interface. Isso identifica um gargalo possível; não é reprodução direta do vídeo/PC Windows.

artwork_cache.py agora permite modo assíncrono nos dois modos da Biblioteca: leitura/recorte transparente/escala de QImage em pool limitado a dois workers, conversão para QPixmap somente na GUI, fila de até 24 pedidos por cache, prioridade de pintura e LRU com teto em bytes e entradas. artwork_prefetch.py antecipa a região visível e linhas vizinhas, sem carregar a biblioteca inteira. Sinal de conclusão solicita nova pintura; a posição, os itens, a proporção inteira e os arquivos originais são preservados. Arte anterior só permite banner alternativo depois de a leitura da capa terminar sem imagem válida, evitando troca provisória por outro tipo de arte. Stat dos arquivos locais continua na GUI para invalidar alterações; esta unidade não promete eliminar todo acesso ao sistema de arquivos da pintura.

Regressão nova teve duas falhas antes por ausência da API assíncrona; depois, 77 testes direcionados passaram em 8,08 s e três testes específicos em 0,50 s. Dois jogos/imagens distintos: leitura intencionalmente bloqueada não impede timer/eventos da GUI; proporção e pixels finais exatos; alteração do arquivo invalida cache; fila e memória limitadas; recorte transparente comparado ao raster original pixel a pixel. Testes antigos test_banner_fallback_0134.py e test_layout_0134.py apenas aguardam conclusão real antes da captura, sem alterar nenhuma asserção de pixels ou dimensões. Quatro falhas intermediárias capturaram o placeholder antes da chegada da imagem; sincronização explícita corrigiu isso. Uma invocação citou arquivo de teste inexistente e saiu com código 4; nova execução com nomes existentes passou. Saídas integrais preservadas em RELATORIO_0137_TESTES.md.

O benchmark anterior 27,25→8,08 ms continua sendo da otimização síncrona já registrada, não uma medição deste novo carregamento assíncrono. Ainda falta validar a sensação de rolagem no Windows real e em bibliotecas do dono. Nenhum dado pessoal, protected file, A4 ou asset original foi alterado.

## Complemento de Desejos — filtro e espaço do rodapé (feito em Linux)

wish_platforms.py agrupa plataformas reais em Todas/PC/Switch/PlayStation/Xbox, sem transferir identidade, preço ou sessão entre elas; outras plataformas existentes permanecem acessíveis. collection_views.build_wishlist apresenta combo no estilo atual, mantém Alfabeticamente, persiste seleção e oferece limpar o filtro quando vazio. Filtro visual não comprova cobertura de preços console. Foram 32 regressões aprovadas em 5,61 s, com captura desejos-filtro-v1/wishes-platform-menu.png enviada no chat.

Pedido posterior sobre o vão entre desconto e Ver ofertas: WishGrid.reflow calcula a altura real da seção de preço pelo layout, preserva arte 1:1, teto de 360 px e colunas, e reduz o link do rodapé à mesma altura dos controles de 28 px. Dois testes de espaçamento falharam antes com vão de 51 px e passaram depois com limite de 28 px; 58 regressões passaram em 21,19 s. Valores, origem oficial por padrão, filtro de keyshops, motivos de ausência e dados salvos preservados. Captura desejos-compactos-v1 enviada; revisão final inclui o último ajuste de altura do rodapé.

## Complemento de carregamento — texto final Carregando (feito em Linux)

O dono pediu posteriormente somente Carregando. show_result normaliza o placeholder legado para esse texto dentro da exceção autorizada; nenhuma alteração em choose, dialogs.py, jobs ou A4. Vinte regressões passaram em 1,55 s no grupo de carregamento/filtro/espaçamento/preço/contrato. A primeira imagem previa-carregando/preview.png foi gerada por script auxiliar sem aplicar o tema e não é válida para revisão de estilo; a captura corrigida previa-carregando-v2/preview.png e a nova loading-preview do renderizador do aplicativo substituem essa evidência visual. O branco observado era do script auxiliar, não uma mudança de tema do aplicativo.

## Item 10 — moldura integrada (parcial, Windows real pendente)

window_controls.py compõe faixa de 32 px e botões minimizar/maximizar-restaurar/fechar, com teclado e nomes acessíveis, sem título ou marca adicionais. Fechar chama window.close e preserva closeEvent/guardas existentes. windows_frame.py mantém estilos nativos Windows de borda/resize, caption, menu de sistema, maximização, área útil do monitor e HTMAXBUTTON para Snap; MainWindow delega nativeEvent e aplica a moldura ao mostrar. Falha na API restaura flags e barra nativa, sem impedir uso do aplicativo. Linux usa a composição Qt para revisar layout.

Testes controlados cobrem maximizar/restaurar, acessibilidade/foco, encaminhamento do fechamento e regiões de borda. Grupo inicial de 31 regressões passou em 3,55 s; grupo posterior com UAC/filtros/contratos passou em 66 testes, 7,14 s. Não comprovados no Windows real: moldura/DWM, Snap Layouts, arrasto/double-click do sistema, mudança de monitor/DPI, taskbar/área útil, Alt+F4 e fechamento durante tarefas. Captura Linux não comprova esses comportamentos nativos. Não declarar o item homologado ou liberar pacote por essa evidência.

## Item 11 — UAC na inicialização (parcial, pacote Windows pendente)

elevation.py usa ShellExecuteExW/runas no executável Windows interativo congelado, antes de abrir banco, migrar dados ou acessar cofre. Preserva argumentos com quoting Windows, cwd, caminho de dados absoluto e raiz original; captura SID antes de elevar e exige o mesmo SID no filho. Cancelamento encerra a instância sem repetir prompt ou iniciar sessão. Troca para outra conta administrativa é recusada antes dos dados, evitando biblioteca/cofre de outro usuário. Já elevado na mesma conta não repete UAC. Auxiliares worker/ROM continuam com suas entradas atuais; smokes/rede são modos diagnósticos explícitos, não detecção de testes. Fonte Python de desenvolvimento não força UAC. Não alterados manifesto/build/workflows/atualizador; o executável do pacote inicia pelo mesmo bootstrap.

Seis testes próprios controlados e regressões de migração/updates totalizaram 38 aprovações em 1,22 s; subprocessos confirmam que handoff/cancelamento/SID diferente ocorrem sem preparar o diretório. Essa evidência não valida ShellExecuteExW nem o pacote no Windows. Restam UAC real, usuário padrão que informa credencial de outra conta (agora recusado de propósito), launchers/Steam, processos-filhos, captura elevada, atualização e cofre reais. Não houve acesso às contas do dono nem pedido de token.

## Item 7 — cinco tamanhos (feito por preservação e regressão Linux)

O componente CoverSizeChoices já implementava cinco capas 70/90/100/125/150, proporção vertical, base comum, seleção verde, teclado e conversão segura de preferência antiga. Não foi recriado. Os testes test_cover_preview_0135.py preservam todas as verificações de alinhamento, borda ativa, limites do card, persistência e aplicação à Biblioteca; incluídos no grupo final de 77 aprovações. O renderizador final captura explicitamente 70%/150% em 1280×800, 1920×1080 e 1000×700. Não há slider de tamanho de capa; Zoom do perfil é outro controle.

## Item 12 — capacidade de preços (parcial/bloqueado na expansão)

Documentação primária https://gg.deals/api/prices/ consultada diretamente nesta rodada. Cópia local ggdeals-api-doc.html, SHA-256 1c46c85b1f61b6e52cc055d342f539d2a4d4c21bb110c5117c320465a5a1f544. Além dos endpoints Steam, existe by-slug, documentado em 14/10/2026: /v1/prices/by-slug/ recebe slugs/key/region e retorna título/URL e currentRetail/currentKeyshops/historicalRetail/historicalKeyshops/currency. O contrato observado não comprova plataforma/edição/loja individual/original. Não há chave/autenticação do dono disponível neste ambiente. Não foi feita consulta autenticada console em BRL e não se presume que a cobertura do site existe na API/plano.

Bloqueio concreto: não há mapeamento comprovado que permita transformar cadastro Switch/PlayStation/Xbox em consulta da edição correta, nem original individual na resposta agregada. O aplicativo continua recusando preço PC em console, mostrando hífen e motivo real. A existência de by-slug, isoladamente, não libera associação por título. Sem nova fonte/scraper, sem registro fictício, sem remover aviso para aparentar suporte. Uma proposta futura de provedor exige cobertura/região/edição demonstradas, contrato de identidade e avaliação de manutenção; credenciais devem ser configuradas pelo cofre, nunca enviadas no chat.

Parte preservada/funcional: oficial por padrão, keyshops opcionais, atual e original da mesma oferta quando comprovados, percentual na cor do tema, ordenação por maior desconto, sem usar histórico como original ou inventar 0%. Filtro de plataforma em Desejos é apresentação e não resolve este bloqueio. O Início usa o mesmo selected_quote e exclui estado de falha/identidade divergente/origem não classificada; ordenação viável foi registrada antes da implementação. Cobertura temporal de cache pronto será conferida na revisão final.

## Dados, contratos e limites da entrega local

Schema continua 4, sem migração ou recriação de banco. Preferências novas/alteradas pertencem aos controles escolhidos pelo usuário: wishlist.platform_filter, profile.avatar_original/profile.avatar_crop e as opções de visualização existentes. Backlog legado não é regravado ao abrir. ROM local usa campos existentes game_files/rom_versions; confirmar muda somente vínculo/perfil e não remove original anterior, sessões, memórias ou metadados. Sem base pessoal, credenciais, ROMs, saves ou mídia pessoal nas evidências versionadas.

Protegidos e fluxo A4 intactos. Exceção QuickAdd restrita a show_result, com verificação AST preservada. Até o encerramento da fase inicialmente local não houve push, PR, tag, release, workflow ou alteração de notas públicas. Depois o dono autorizou especificamente lançar a 0.1.37; notas públicas foram então preparadas e o envio/workflow serão registrados no relatório de lançamento. Workflows e autorizações históricas da 0.1.36 não foram alterados ou reutilizados.

## Último complemento — prévia vazia até chegar a capa (feito em Linux)

Depois dos 690 testes integrais aprovados, o dono substituiu Carregando por espaço vazio. Somente QuickAdd.show_result limpa os placeholders de texto da arte; não limpa pixmap já recebido e mantém os 70×94 do espaço original. Nenhuma alteração de choose/received, cadastro, jobs ou fonte. Estado da consulta fora da arte permanece separado.

Teste anterior atualizado especificamente para a nova decisão: duas falhas antes porque ainda aparecia Carregando; depois 54 testes aprovados em 14,07 s, incluindo contratos protegidos. Pokémon FireRed and LeafGreen+ e Ocarina of Time 3D ficam sem texto/pixmap durante a espera; sinal real Qt do job controlado percorre received e coloca duas capas diferentes, com pixels, proporção e limites conferidos. Título e ausência de jobs espúrios preservados. Asserções antigas de cabimento da palavra foram substituídas pela exigência explícita de ausência de texto e chegada da imagem, por instrução do próprio dono.

## Revisão do item 4.3 — validade temporal das Ofertas (feito em Linux)

A revisão final identificou que state=ready sozinho ainda permitia promover cache antigo como oferta atual no Início. home_data.wish_offers agora exige checked_at com fuso, idade de zero até menos de uma hora, BRL explícito e contexto de identidade confirmado pelo selected_quote. Data ausente/inválida/ambígua/futura e cache vencido ficam fora do Início; os valores armazenados e a apresentação de cache na ficha/Desejos não são apagados nem regravados. Usa a janela de cache existente da consulta, sem inventar histórico ou nova fonte.

Cinco casos novos, com Portal 2 e Hades, cobrem ausência, erro, data sem fuso, limite de uma hora e futuro; preço salvo preservado exatamente, consulta com 3.599 segundos aceita. Antes faltava a API de relógio para essa verificação; depois 27 testes de dados/layout/preços passaram em 2,08 s. Fixtures desta rodada agora informam data de consulta recente explicitamente, sem alterar expectativas de valores/ordenação/desconto. Invocação intermediária citou teste inexistente e saiu com código 4; nova execução com nomes existentes passou, saída integral mantida. A suíte integral será repetida porque houve essa mudança funcional posterior aos 690 testes.

## Índice por item na revisão final

Feito significa implementação/regressão Linux, não homologação Windows pessoal. Linhas parciais/bloqueadas não são apresentadas como conclusão integral da rodada.

| Item | Status | Arquivos/funções principais e evidência | Commits da unidade |
| --- | --- | --- | --- |
| 1 Base/diagnóstico | feito | AGENTS/documentos, branch e base 58b0c118 reconfirmadas; plano inicial | 05f3aaf |
| 2 Referências | feito na implementação; revisão estética não presumida | Imagens A/B e correções posteriores; render_0137_review, 3 resoluções | 8a66e32, f543166 |
| 3 Vídeos | parcial | p1–p4 não anexados nesta rodada; achados tratados como relato, sem fingir observação direta | 05f3aaf e este relatório |
| 4 Início | feito em Linux | home_data execution_history/recent_games/week_summary/wish_offers/recent_memories; home_components e home_view; carrosséis/ações e datas reais | 4d38531, 8a66e32, dbbea93, f356e59, 41f3826 |
| 5 Lista | feito em Linux | library_list ListDelegate/LibraryList; window refresh_library/toggle_favorite; logo/nome/tempo/coração e filtros | c2b1773 |
| 6 Grade/rolagem | feito em Linux; PC Windows não homologado | artwork_cache load/_read_image; artwork_prefetch; cover_grid; playtime.collection_times; benchmark 500 jogos e leitura lenta | 2450275, 36a3146 |
| 7 Capas 70–150 | feito por preservação/regressão | settings_previews CoverSizeChoices já existente, testes de base/verde/teclado/persistência e capturas 70/150 | 36a3146, f543166 (validação/capturas) |
| 8 Rótulos/status | feito em Linux | library.display_status/STATUSES, filtros e detalhe; Alfabeticamente/Todas/Não iniciado sem regravar Backlog legado | 7dcd020, 63c7de2, a1505a1 |
| 9 Estatísticas | feito em Linux | period_chart.PeriodChart; statistics_periods.day_hours; statistics_view sem Gêneros da coleção; metadados preservados | 3d7c132 |
| 10 Moldura | parcial | window_controls e windows_frame; MainWindow.nativeEvent/showEvent; Windows real/Snap/monitores/área útil pendentes | e06e4f1 |
| 11 Elevação | parcial | elevation.elevate_startup/WindowsElevationApi e app.main; controles de SID/argumentos/cancelamento; UAC real pendente | 27e304d |
| 12 Preços | parcial; expansão console bloqueada | Fonte oficial inspecionada; sem confirmação autenticada de plataforma/edição/original; integridade atual preservada, sem nova fonte | relatório de capacidade; 41f3826 para validade temporal no Início |
| 13 Desejos | feito em Linux | collection_views.build_wishlist/WishGrid.reflow; wish_platforms; filtro em combo, rodapé compacto, regressões de ficha/favorito/preços | 29f5db5 |
| 14 Avatar | feito em Linux | avatar_crop e profile_dialog select_photo/recorte/zoom/save; original/EXIF/cancelamento/persistência | fc19ac9, 058fa53 |
| 15 Banner/captura | parcial | Banners inteiros e regressões preservados; captura global/elevada com jogos reais não homologada | f356e59, e06e4f1 e regressões da suíte |
| 16 Limites | bloqueado/descartado conforme pedido | A4 intacto; fechar só ROM permanece limitação; troca automática descartada, não implementada | plano e relatório; sem alteração do fluxo protegido |
| 17 Marca/temas/textos | feito em Linux | Assets/nove temas preservados; Steam real/raster original; ordenação e prévia conforme decisões posteriores | 7dcd020, 63c7de2, 2565e57 e regressões |
| 18 Dados/contratos | feito em Linux | Schema 4, game_files/rom_versions existentes, originais/histórico mantidos; contrato AST e protegidos intactos | a1505a1, 2565e57 e auditoria final |
| 19 Validação | parcial | Linux e Windows runner/pacote aprovados, capturas e escalas Qt disponíveis; Windows real/contas/emuladores não homologados; execução registrada no relatório de lançamento | RELATORIO_0137_TESTES e relatório de lançamento |
| 20 Entrega | feito na entrega local e publicação autorizada; limitações mantidas | Documentos/notas/relatórios/índice/patches locais e hashes; publicação só após autorização posterior e gates | f543166 e commit documental final |
| ROM local adicional | feito em Linux; emuladores reais não homologados | local_rom validate_path/compatible_profiles/identity_problem/bind_local; local_rom_dialog; window.start_game/launch_rom e rom_link; dois programas próprios | a1505a1 |
| Prévia vazia adicional | feito em Linux | Somente QuickAdd.show_result; teste com dois jogos e chegada efetiva da capa pelo sinal Qt | d6a373b e c4b0e99 (etapas substituídas), 2565e57 (estado final) |

## Commits completos até o código congelado para a suíte final

Saída de git log --reverse --format='%H %s' 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1..HEAD; o commit documental posterior será incluído no manifesto externo da entrega, evitando referência circular ao próprio relatório.

```text
05f3aaf0487601a3e4b51b69cab47e7b847b6d72 docs: planejar implementação local da 0.1.37
7dcd020dd06f05e8722ad7b654a0ab2837be9531 fix: aplicar rótulos aprovados da 0.1.37
4d38531ec8cc4ed9c9516768a4ea172f6ce274f0 feat: obter dados locais verificáveis para o novo Início
8a66e32eeb97501dc427c7e3d2819a3eb564bbfb feat: integrar Início com carrosséis e Ofertas conforme revisão
dbbea93600d9528d48e0cddc8b36df93ae9ecba1 fix: simplificar Ofertas aos quatro campos pedidos
c2b1773583f98a8c2d909955dc2f82c503391359 feat: substituir tabela da Biblioteca por lista de cards
f356e59cf16cdf046a919520cde14aa4ab7e1d14 feat: apresentar prévia de banners nas linhas de Ofertas
2450275407d336258a368787fc0a1e13e1ce0715 perf: limitar rasters e evitar reconstrução da Biblioteca
63c7de2d8953e24e4f6ce7831cce1439375e0207 fix: nomear ordenação como Alfabeticamente
3d7c132b41ed05e05a53e605d0c2ea1cef0ac085 feat: adaptar gráficos ao período e remover Gêneros da tela
fc19ac9e5cd620ed908221d0994e61094e66fbfa feat: editar recorte posição e zoom da foto de perfil
058fa536a90c75dde1bdf0e7dac49bedb12947a8 style: usar indicador circular no zoom da foto
a1505a175224d1bbe2b02a91adfe732d0e2a8bbe feat: vincular ROM local pela ficha e validar edição antes de executar
d6a373b6cdc7e737d693bfd9299242ce83ff8560 fix: mostrar texto de carregamento da prévia sem corte
36a314687a1ca5542688dcefc06685cca4420c1f perf: carregar arte da biblioteca fora da interface
29f5db5d16467468542d76ed18050cba3af0cb76 fix: filtrar desejos por plataforma e compactar rodape
c4b0e99e1de11e392c073077cf9b431c4c7f4e08 fix: simplificar placeholder para Carregando
e06e4f1adf2b523f66486d8e4a9e592d19441f6b feat: integrar controles e moldura da janela
27e304df2380098847a4b8472e0ffd8e431ece85 feat: preparar elevacao UAC preservando conta e dados
2565e579cd530847a859dcf226a52ade6482abc3 fix: manter previa vazia ate a capa chegar
41f382687c0a566313bf9f923a40c36ae9f8c280 fix: exibir no Inicio somente ofertas com consulta recente
f543166037e545aad99c6aef21bf6ed95fe4bb10 chore: preparar versao local 0.1.37 e revisao visual
```

## Resultado local final

Código congelado f543166037e545aad99c6aef21bf6ed95fe4bb10; versão 0.1.37; schema 4. Linux/Python 3.12.14/PySide6 6.8.3, QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp. Suíte exigida integral: **695 passed in 479.02s (0:07:59)**, código de saída 0, sem skips/xfails introduzidos. A execução anterior teve 690 aprovações antes dos últimos ajustes; não é usada como resultado final. Comando, stdout completo, stderr e exit de ambas estão em RELATORIO_0137_TESTES.md. Não houve mudança de código/testes/scripts durante a suíte final; somente documentação/notas.

Smokes novos/isolados aprovados: seis páginas e SQLite integrity=ok; cadastro, auxiliar, renderização e persistência. Capturas finais reais Qt com arte/valores sintéticos identificados: revisao-codigo-final (DPR 1), final-dpi150 (1,5) e final-dpi200 (2), cada conjunto com 48 screenshots listados no manifesto, em janelas lógicas 1280×800/1920×1080/1000×700. Essas escalas Qt não homologam Windows/DPI/monitores reais. Capas 70/150, controles, Perfil, origem/ROM local e prévia vazia incluídos. As imagens de revisão anteriores permanecem históricas; loading-preview final substitui a palavra Carregando. Não presumida aprovação estética por gerar capturas.

Auditoria por git diff confirmou workflows, assets e arquivos protegidos idênticos à base 58b0c118; o teste AST protegido passou na suíte. Arquivos de texto novos/alterados verificados como UTF-8/LF; nenhuma normalização de protegido. O único arquivo de .github preparado após a autorização de lançamento é release-notes.md, com as notas da 0.1.37. Não houve force ou reescrita de histórico.

Entrega local preparada com documentos, relatórios, capturas e patches completos gerados por git format-patch -1 SHA --stdout e SHA-256 em manifesto externo. Hash do próprio relatório e do commit documental constam no manifesto externo após o commit, evitando referência circular. O lançamento autorizado, seu SHA, execução Windows, testes/build/smokes/arquivos e resultado são registrados em RELATORIO_LANCAMENTO_0137.md; preparar documentação não é afirmar que publicou.

Continuam parciais/bloqueados: preços console/original da API sem prova autenticada; moldura/UAC/captura elevada/launchers/contas/emuladores e uso real no Windows do dono; A4 e fechamento apenas da ROM. Não declarar a rodada inteira concluída com essas pendências. Esta entrega conclui a implementação/verificação local possível e explicita o que não foi homologado.

## SHA-256 dos patches integrais do candidato enviado

Gerados por git format-patch -1 SHA --stdout; cada comando terminou com exit 0 e stderr vazio. Até o SHA enviado a33f48afbb8502a2f128de453451f326e8c988c2. Registros documentais posteriores têm patches e hashes adicionais no manifesto externo final.

```text
bf80f14b70206f2b9dcef119926fc360ee8277454be000fed27380123fb4b27b  01-05f3aaf0487601a3e4b51b69cab47e7b847b6d72.patch
aa2cd1074f827a862ffd32500ca33417ab26463334a2d35ac4b7c18a00c48e50  02-7dcd020dd06f05e8722ad7b654a0ab2837be9531.patch
3118b3525dbbdf0e85556a6c516204cb324e1b7525c57176e607f2ae46199522  03-4d38531ec8cc4ed9c9516768a4ea172f6ce274f0.patch
9a2e99d084c641dd43c87c213015938470898d4cae76a8186274e39e7a60bf34  04-8a66e32eeb97501dc427c7e3d2819a3eb564bbfb.patch
0524b945e0600cd3622cbe58d63dcf68e4d94f1c3529d4408e46797ee4e1b1eb  05-dbbea93600d9528d48e0cddc8b36df93ae9ecba1.patch
c00263504fdaf448a3f61ab01b4b098bfbde1fb2b42348442d78e63092b104bc  06-c2b1773583f98a8c2d909955dc2f82c503391359.patch
c0e513bf00f82f66897b37625a917d22f810c1c9e8a75d9b3645f7f59a927654  07-f356e59cf16cdf046a919520cde14aa4ab7e1d14.patch
c1f2e7a385da85e37222cfa84fff7af4ecf7fbf9a7cdac953b19bc4b0bd51628  08-2450275407d336258a368787fc0a1e13e1ce0715.patch
d538013a763e7d383c115d12c8e713f35a39b1e77537b305151c4828e6b89ec6  09-63c7de2d8953e24e4f6ce7831cce1439375e0207.patch
9f0aed79d0a79b35f0cdcd3a8a3a7b7162084d4a4defe5203ef9ea04a263e9ec  10-3d7c132b41ed05e05a53e605d0c2ea1cef0ac085.patch
fdd30c01984525f27ac321fd51220791c655b513721d67dfc99d4386b796985d  11-fc19ac9e5cd620ed908221d0994e61094e66fbfa.patch
fa735d5774bcc49f5b09d5a7e0f530feaa2d9b419189ed27d9095b90f3af8c34  12-058fa536a90c75dde1bdf0e7dac49bedb12947a8.patch
a7366e1ac2e00106ed99ccfbc124724ce2e1f8254001c71f56f40cf4fa4e60cc  13-a1505a175224d1bbe2b02a91adfe732d0e2a8bbe.patch
24416152f390e88c45d0e90b8efa6ba0a9b0f04dce0de6ff98c3b5ea7bf4e47e  14-d6a373b6cdc7e737d693bfd9299242ce83ff8560.patch
af875536d5d600f4eed55dd05156e14d1664d6831b493a0547be1ba64f3f972f  15-36a314687a1ca5542688dcefc06685cca4420c1f.patch
dae41bfdf77d9333e9597d7b84b02dfe4e8ce959790c3fb1fcd047afe5dce7bc  16-29f5db5d16467468542d76ed18050cba3af0cb76.patch
f2ba883ac3101d454a021661736a7955a4b24c14b74193dcf62ce40c01fd43a4  17-c4b0e99e1de11e392c073077cf9b431c4c7f4e08.patch
efa5a7f7add200ee8065b8a51e6444b0979c1b6fd8e58abc242e1fe3b1f0869e  18-e06e4f1adf2b523f66486d8e4a9e592d19441f6b.patch
0d12ea98494dd1934899b3aa271069cf9ff89449a3b535801b5a2bbb38469776  19-27e304df2380098847a4b8472e0ffd8e431ece85.patch
242edd3a44fe82fbca87442d33604e58adc276939f27ff5424cbe2e03b290d2e  20-2565e579cd530847a859dcf226a52ade6482abc3.patch
84d42d2195b96067e995cfe76009ffd4d235639289d8ed216068ad932c9a8304  21-41f382687c0a566313bf9f923a40c36ae9f8c280.patch
d66501b92ab6f31562e6fbd25981001fb7692036627ef83af0ff0cc7d81fca01  22-f543166037e545aad99c6aef21bf6ed95fe4bb10.patch
8c668e9ff29e3910ec09bbebc354e0e6fbd31acec663424b3e69613c4cc6b925  23-a33f48afbb8502a2f128de453451f326e8c988c2.patch
```

## Complemento de evidência de Aparência

As capturas gerais da aba começam no topo dos nove temas; na janela menor, o controle de tamanho fica abaixo e exige rolagem vertical, conforme permitido. Conjuntos adicionais capas-controle-final, capas-controle-dpi150 e capas-controle-dpi200 mostram o próprio controle visível após ensureWidgetVisible, nas opções 70/150 em 1280×800/1920×1080, com dois jogos isolados. São grabs reais do mesmo aplicativo; nenhum código de produção foi alterado para essas imagens. A evidência adicional evita usar uma captura do topo como prova visual de um controle fora da área visível.

## Correção da validação Windows — limpeza do teste dos controles

Primeiro candidato enviado a33f48a não foi publicado: execução 43790327035 encerrada após bloqueio reproduzido no próprio teste. O spy de close permanecia ativo na limpeza da fixture, deixando o atalho nativo registrado; a próxima janela bloqueava em conflito. Reprodução controlada teve dois erros antes e três aprovações depois. tests/test_window_controls_0137.py usa agora monkeypatch.context apenas na verificação do encaminhamento e depois fecha a janela pelo botão real, exigindo invisibilidade e liberação do atalho. Sem mudança em código do aplicativo ou qualquer asserção anterior. Suíte Linux e execução Windows serão repetidas no novo commit; histórico não reescrito. Logs e contagem/ordem da interrupção no relatório de lançamento.

## Patch adicional da correção de validação

c526cb4bc5e8721dfdfdf20222c8c1c41562ce52 — SHA-256 323f54bdc0dd70000d4b16c2bc6491bcb2b28d9a8f95b17e24a7758654d1d1b2; git format-patch -1 SHA --stdout, exit 0, stderr vazio. Os hashes anteriores cobrem os commits até a33f48a; esse patch completa os 24 commits até a tag c526cb4. O commit documental posterior e o hash final deste relatório ficam no manifesto externo da entrega para evitar referência circular.

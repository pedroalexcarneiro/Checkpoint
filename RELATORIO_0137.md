# Relatório 0.1.37 — em implementação local

Base: 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1 de fix/0.1.36-ajustes; remoto reconfirmado e checkout inicial limpo. Branch: fix/0.1.37-ajustes. Sem autorização para publicação, push, PR, tag, release ou workflow de lançamento. Código, tag e assets publicados da 0.1.36 permanecem preservados.

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

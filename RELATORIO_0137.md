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

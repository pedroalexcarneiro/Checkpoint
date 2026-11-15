# PLANO_0135 — execução autorizada e complementos aprovados

Base confirmada: `fix/0.1.34-bugs` em `af1d3ab56492cba56b541ddb971759d9c15b015b`. Conta conectada: `pedroalexcarneiro`, permissões push/admin confirmadas. Releases v0.1.28, v0.1.33 e v0.1.34 presentes.

Lidos AGENTS.md, RELATORIO_0134_COMPLETA.md, CONTINUITY.md, PROJECT_STATUS.md, ARCHITECTURE.md e ROADMAP.md. A documentação descreve entregas como locais; o remoto verificado é a referência atual. Esta etapa cria somente documentação local; não cria branch de implementação, commit, push, PR, tag ou release.

## Método após aprovação

Reconsultar HEAD remoto e comunicar divergência material. Criar fix/0.1.35-ajustes desse HEAD. Um commit por item, com teste novo falhando antes da correção e passando depois, em pelo menos dois jogos diferentes (Zelda: A Link to the Past e Metroid Fusion, salvo fixtures Steam que exigem dois AppIDs reais distintos). Registrar comandos, stdout, stderr e código integralmente. Arquivos abaixo são candidatos, não autorização para mudar protegidos. Para itens novos, o teste inicial demonstra ausência do comportamento. Sem reprodução nos itens investigativos, não declarar correção.

## 1. Jogar executa a ROM

- Arquivos prováveis: checkpoint/window.py (start_game/launch_rom), launcher.py e detail_view.py.
- Teste antes da correção: Clicar Jogar e Executar versão em Zelda: A Link to the Past e Metroid Fusion, com perfis e ROMs locais controlados; comparar argv e ROM enviada ao processo. Incluir caminhos com espaços e ROM ausente.
- Aceitação: As duas ações usam o mesmo perfil e a ROM vinculada; erro útil quando faltar arquivo, sem sessão fantasma.

## 2. Sessões encerradas e interrompidas

- Arquivos prováveis: checkpoint/launcher.py (poll/finish/interrupt), window.py (poll_sessions/recover_sessions).
- Teste antes da correção: Nos dois jogos, encerrar processo, fechar somente a ROM mantendo emulador, reiniciar app e tentar jogar novamente. Usar subprocessos reais isolados e adaptador de monitoramento controlado.
- Aceitação: Nenhuma sessão ativa fica presa; duração gravada uma vez; interrupções reais aparecem na revisão. Fechar só a ROM exige investigar sinal confiável do emulador; não inferir encerramento apenas pela perda de foco.

## 3. Largura dos cards de Desejos

- Arquivos prováveis: checkpoint/collection_views.py (WishGrid.reflow), card_layout.py.
- Teste antes da correção: Povoar a grade com ambos os jogos repetidos como cadastros distintos; medir em 800, 1280, 1920 e 2560 px.
- Aceitação: Proposta: teto de 360 px por card, mais colunas quando couber e arte 1:1; janela estreita sem overflow. Ver conflito de testes abaixo.

## 4. Tempo único app + Steam

- Arquivos prováveis: checkpoint/detail_view.py, statistics_view.py, collection_views.py, library.py, ui_components.py, activity_heatmap.py.
- Teste antes da correção: Dois jogos com 60+75 min e 0 min; incluir segundos residuais, dados ausentes e múltiplas contas Steam. Conferir ficha, Estatísticas e Desejos.
- Aceitação: Um total em XhXXmin, como 2h15min e 0h00min; truncar segundos só após somar. Não duplicar snapshots de contas nem transformar tempo Steam em sessões locais. Ver conflito explícito abaixo.

## 5. Primeira memória

- Arquivos prováveis: checkpoint/collection_views.py (build_memories), window.py e detail_view.py.
- Teste antes da correção: Em banco vazio de memórias com os dois jogos, clicar Biblioteca, escolher cada jogo e verificar destino; também biblioteca sem jogos.
- Aceitação: Texto explica abrir jogo > Memórias > captura/anotação. Botão conduz à escolha e depois à aba Memórias; biblioteca vazia oferece cadastro.

## 6. Grade de memórias

- Arquivos prováveis: checkpoint/collection_views.py (memory_card/build_memories), design_system.py.
- Teste antes da correção: Misturar anotação e captura dos dois jogos, títulos longos e duas larguras; medir geometria e texto visível.
- Aceitação: Cards alinhados por linha, título do jogo consistente e legível nos dois tipos, imagens proporcionais.

## 7. Apagar memória

- Arquivos prováveis: checkpoint/collection_views.py, window.py, library.py.
- Teste antes da correção: Para cada jogo testar cancelar/confirmar exclusão de anotação e captura; preservar memória do outro jogo e mídia externa original.
- Aceitação: Ação em cada card, confirmação identificando memória; cancelar preserva tudo, confirmar remove só o registro e atualiza a tela. Tratar arquivos gerenciados sem apagar origem importada.

## 8. Controle de status

- Arquivos prováveis: checkpoint/detail_view.py, library.py, home_view.py, statistics_view.py.
- Teste antes da correção: Nos dois jogos clicar e persistir cada um dos cinco estados, reabrir ficha e conferir Início e distribuição da coleção.
- Aceitação: Controle acessível por mouse/teclado com Backlog, Jogando, Pausado, Concluído e Abandonado; mapear legado Não iniciado sem perda; telas refletem mudança imediatamente.

## 9. Configurações proporcionais

- Arquivos prováveis: checkpoint/settings_view.py, design_system.py, window_style.py.
- Teste antes da correção: Abrir configurações com acervos de cada jogo em 1280×800 e 1920×1080; medir ocupação e acesso ao controle de capas.
- Aceitação: Cards aproveitam largura/altura sem vazio excessivo; Tamanho das capas claramente rotulado, valor e destaque; conteúdo acessível em janela estreita.

## 10. Conexões padronizadas

- Arquivos prováveis: checkpoint/settings_view.py, ggdeals_connection.py, window_style.py.
- Teste antes da correção: Duas fixtures de acervo e estados conectado/desconectado/erro; medir botões e verificar navegação por teclado nos temas.
- Aceitação: Quatro conexões 2×2 preservadas, uma ação principal por card, dimensões/estilo comuns, checkboxes tematizadas, rótulo GG.deals curto.

## 11. Dados e backup

- Arquivos prováveis: checkpoint/settings_view.py.
- Teste antes da correção: Nas duas fixtures verificar geometria e cliques com callbacks isolados, sem restaurar dados reais.
- Aceitação: Botões junto ao texto e alinhados à esquerda; Criar backup principal, Restaurar saves e Abrir pasta de dados secundários.

## 12. Ficha exclusiva de Desejos

- Arquivos prováveis: checkpoint/detail_view.py, window.py (detail/acquire_wish), library.py.
- Teste antes da correção: Abrir ambos os jogos só nos desejos; comparar com jogo da biblioteca que também está nos desejos e depois adquirir.
- Aceitação: Exclusivos sem Memórias, Atividade, Arquivos, Galeria ou Configurar execução; exibir Adicionar à biblioteca e Na lista de desejos. Adquirir habilita ficha de biblioteca sem perder metadados.

## 13. Banner sem recorte

- Arquivos prováveis: checkpoint/detail_view.py, collection_views.py (WishLogo), cover_art.py/artwork_render.py.
- Teste antes da correção: Artes dos dois jogos com bordas coloridas e proporções diferentes; renderizar ficha e Desejos em várias larguras.
- Aceitação: Quatro bordas visíveis, proporção original mantida, sem deformação; Desejos conserva área externa 1:1 e contém banner como alternativa.

## 14. Resumo da Wikipédia

- Arquivos prováveis: checkpoint/wiki_text.py (intro), detail_view.py.
- Teste antes da correção: Textos dos dois jogos com parênteses japoneses, aninhados, datas numéricas/por extenso e contexto editorial; comparar banco antes/depois.
- Aceitação: Apresentação remove parênteses e conteúdo, datas e contexto; conserva descrição útil do jogo e texto original no banco. Evitar filtro que elimine descrição por conter a palavra história.

## 15. Sobre o jogo vazio

- Arquivos prováveis: checkpoint/detail_view.py, metadata_state.py, window.py.
- Teste antes da correção: ROMs dos dois jogos sem texto, com artes apenas e com falha de provedor; clicar recuperação.
- Aceitação: Seção sempre visível com motivo honesto e Pesquisar manualmente/Editar ficha; vínculo ROM preservado; sem alterar fluxo protegido de cadastro.

## 16. Preço oficial por padrão

- Arquivos prováveis: checkpoint/prices.py, price_view.py, collection_views.py, integrations/ggdeals_api.py.
- Teste antes da correção: Dois jogos com oferta oficial mais cara que keyshop, só keyshop, nenhuma oferta e cache antigo; alternar opção e conferir ordenação.
- Aceitação: Padrão considera só lojas oficiais; opção persistida inclui keyshops e atualiza preço/ordem. Cache não pode passar preço keyshop por oficial; sem preço oficial, explicar. Sem desconto/preço original nem fonte nova.

## 17. Captura Ctrl+Shift+S

- Arquivos prováveis: Novo serviço checkpoint/game_capture.py; window.py, settings_view.py, launcher.py e persistência de mídia.
- Teste antes da correção: Nos dois jogos iniciados pelo app, mapear PID/janela; testar atalho, conflito, preferência persistida, app sem foco, jogo externo e erro de captura. Qt e adaptador Windows controlados; integração Windows separada.
- Aceitação: Com Checkpoint em primeiro plano, captura janela do jogo iniciado e grava na Memórias correspondente; atalho configurável. Sem jogo elegível, aviso; sem foco, não captura. Com duas sessões, seleção explícita se alvo ambíguo; nunca capturar janela arbitrária. Captura real Windows fica pendente de validação nesse sistema.

## 18. Executáveis nas bibliotecas Steam

- Arquivos prováveis: Novo checkpoint/steam_installations.py; steam_library.py, game_editor.py e integrações pertinentes.
- Teste antes da correção: VDFs UTF-8 e manifests de dois jogos instalados em unidades/bibliotecas diferentes; subpastas, espaços, entradas antigas, múltiplos executáveis e Steam ausente.
- Aceitação: Descobrir raiz Steam no sistema, ler libraryfolders.vdf e manifests e procurar executáveis no installdir correto; não usar caminho fixo nem escolher launcher ambíguo silenciosamente. Outros jogos mantêm Escolher executável; não alterar dialogs.py.

## 19. Investigar troca de aba por arrasto

- Arquivos prováveis: checkpoint/detail_view.py, smooth_scroll.py, design_system.py e window.py conforme evento identificado.
- Teste antes da correção: Com ficha de cada jogo, simular press/move/release sobre conteúdo e barra de abas, roda, touchpad e foco; instrumentar eventos sem dados pessoais.
- Aceitação: Registrar evento e passos que reproduzem antes de corrigir; arrasto não muda aba, clique e tecla continuam funcionando. Sem reprodução, registrar não reproduzido e pedir print/gesto exato, sem correção especulativa.

## 20. Investigar data futura

- Arquivos prováveis: checkpoint/activity_heatmap.py, library.py (now/statistics), statistics_view.py, locale.py e origem dos registros.
- Teste antes da correção: Dois jogos com sessões em 2026-11-15 00:30 UTC (=14/11 21:30 em São Paulo), limites da meia-noite, ISO com offset e legado; separar célula vazia de registro real.
- Aceitação: Provar origem e fuso; agrupar/exibir datas no fuso local do usuário, mantendo instantes do banco. Não fixar America/Sao_Paulo para todo usuário nem apagar/recuar registros genuínos. Corrigir só causa reproduzida.

## Conflitos conhecidos que exigem decisão específica

O item 4 contradiz diretamente `tests/test_time_prices_0134.py::test_app_and_steam_times_are_separate`: exige rótulos separados (1 h local e 3 h Steam). A proposta é substituir, somente com aprovação explícita, essas expectativas pela soma 4h00min e ausência de duplicação, conservando cobertura dos valores originais. A aprovação genérica do plano não será tomada como autorização para editar asserções.

O item 3 pode conflitar com `tests/test_layout_0134.py::test_wishes_fill_columns_with_square_art`, que exige preencher toda a largura. Um teto de card pode deixar sobra. Proposta, sujeita a autorização específica caso o conflito se confirme: preservar arte quadrada e largura mínima onde couber, exigir teto de 360 px e aumento de colunas em vez de preenchimento integral. Nenhuma asserção foi alterada.

Outros conflitos encontrados durante reprodução serão registrados com teste, asserção e razão exata antes de pedir aprovação. Não usar skips, xfails, detecção de ambiente ou contornos.

## Limites obrigatórios

A4 fora de escopo. Não alterar dialogs.py, tests/test_save_lifecycle.py, checkpoint/worker.py, enrichment.py, game_import.py ou completion_queue.py. Em quick_add.py apenas show_result/show_missing_metadata seriam permitidos, mas não há alteração planejada. Teste protegido visual intacto. Não alterar releases protegidas nem publish-0.1.28.yml. Schema 4 preservado; nenhuma migração prevista. Não imprimir credenciais ou dados pessoais. Toda nova leitura textual em código/testes com encoding='utf-8'; arquivos novos/editados em LF. Não normalizar arquivos protegidos incidentalmente.

## Ordem e entrega após aprovação

Ordem sugerida: 1–2; 3–4; 5–8; 9–11; 12–16; 17–18; 19–20. Itens bloqueados ficam registrados, sem contornar contratos, e trabalho independente pode continuar. Antes do push final, relatar qualquer bloqueio que impeça todos os itens ficarem prontos; não publicar branch parcial como entrega completa.

Rodar regressões relevantes e suíte completa com `QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp python -m pytest tests -q -p no:cacheprovider`, em Python 3.12 e dados isolados. Nunca resumir saída de teste no relatório: guardar stdout, stderr e exit code completos, inclusive falhas antes da correção. Nenhum teste executado nesta fase de planejamento.

RELATORIO_0135.md final: item, SHA, arquivos/funções, feito/bloqueado/revertido e motivo; suíte integral; patches completos `git format-patch -1 <sha> --stdout` e SHA-256; limitações Windows. Atualizar continuidade/estado/documentação pertinente. Push único da branch somente quando o conjunto estiver pronto, sem force; sem PR, tag, release ou workflow de publicação. Validação Linux offscreen não comprova Windows, fechamento interno de ROM em emuladores reais, captura Win32, DPI nem contas autenticadas.

## 21. Logo da Steam em Conexões — acrescentado ao fim da fila

- Arquivos prováveis: checkpoint/ui_components.py (service_icon); novo teste de renderização do card. Fonte atual: checkpoint/assets/services/steam.ico, preservada.
- Pré-condição: mostrar a logo atual e seu caminho ao dono; aguardar confirmação antes de qualquer alteração. Imagem exibida no chat e confirmação recebida: “Confirmar e iniciar o item 21”.
- Teste antes/depois: renderizar o card Steam e comparar área ocupada com Google Drive em duas fixtures de jogos distintos; verificar margem, proporção e ausência de recorte.
- Aceitação: logo contida no quadrado de 48 px, com área visual comparável à do Google Drive (arte contida em 36 px), sem substituir o arquivo de marca por Lucide. Não modificar a ordem nem os commits já feitos dos itens 1–20. Se surgir dependência que altere requisito anterior, parar e avisar.

## 22. Logos de serviço fora da padronização Lucide — acrescentado após 21

- Arquivos prováveis: novos testes de contrato e documentação da área de ícones; sem substituir logos existentes.
- Teste antes/depois: bloquear a renderização Lucide no teste e confirmar que Steam, Google Drive, SteamGridDB e RAWG continuam renderizando suas marcas próprias em duas fixtures de jogos distintos.
- Aceitação: logos de serviço não usam Lucide; somente a escala/posição do item 21 é alterada. Se a exclusão já estiver correta na base, registrar teste passando antes e depois como verificação, sem inventar um bug para obter falha. Commit separado com essa cobertura e documentação.

## Complementos aprovados após 21–22 (novos commits, sem reescrever anteriores)

- Correção adicional do item 9: prévias funcionais dos nove temas, ocupação da largura e card de tamanho das capas destacado. Teste de ocupação antes/depois com dois jogos.
- Visual A (Desejos, itens 3/16): Sem preço salvo em destaque e motivo factual abaixo; consulta sem oferta oficial distinguida de consulta não feita e ausência de ID Steam.
- Visual B (Conexões, item 21): logo real steam.ico, sem iniciais ST; prova por pixels do arquivo original.
- Visual C (Ficha, item 8): cinco estados, atual em destaque; Não iniciado é mostrado como Backlog sem regravação automática.
- Elementos de mockup excluídos: números/círculos de anotação, cabeçalho Checkpoint adicional, rodapé Biblioteca pessoal e rótulo Verde duplicado. Seleção por cards de tema funcionais; identidade atual preservada.
- Prévia de capas (item 9): slider à esquerda e três exemplos à direita, mesma linha e base comum; destaque verde acompanha valor, percentual junto ao slider; testes 1280×800/1920×1080 e 70%/150% sem overflow.
- Regra de texto nas sete telas: remover frases de apoio e legendas decorativas; preservar títulos, rótulos, dados, descrições externas, texto do usuário, erros e estados vazios com ação concreta. Registrar lista por tela no relatório final.

## Fechamento local

542 testes passando na suíte completa. Encerramento interno de ROM com emulador aberto permanece bloqueado; nenhum push. Todos os complementos foram acrescentados em novos commits, preservando commits existentes a partir da instrução do dono. Estados vazios mantêm instruções diretas com o destino da ação; teste protegido foi preservado. Relatórios finais: RELATORIO_0135.md e RELATORIO_0135_TESTES.md.

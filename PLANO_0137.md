# Plano 0.1.37 — implementação local

Pedido integral recebido em 15/11/2026; referências: imagem A (Início) e imagem B (Biblioteca em lista), anexadas nesta conversa. Base local/remota reconfirmada: fix/0.1.36-ajustes em 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1; tag v0.1.36 em 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Checkout inicial limpo. Branch nova fix/0.1.37-ajustes. Sem push, PR, tag, release ou workflow de publicação.

## Sequência de unidades e critérios

1. Diagnóstico: código, sessões e esquema; capacidade atual de preços e reprodução da lista/grade/estatísticas. Preservar código publicado e registrar evidências antes de corrigir.
2. Item 8: rótulos Não iniciado, Nome: A–Z, Adicionados recentemente e períodos Hoje/Esta semana/Este mês. Mesmos dados e cálculos; status ausente das linhas da lista.
3. Item 4: serviço de dados do Início a partir de play_sessions válidas, sem criar histórico retroativo. Histórico existente contém início e PID após Popen bem-sucedido; não exige nova tabela. Resumo usa semana segunda-feira 00h local até agora; somente sessões finalizadas com duração comprovada entram em tempo/sessões/jogos, sessões ativas/interrompidas ficam fora até revisão. Documentar essa limitação, sem duração inventada.
4. Item 4: composição do Início com dois jogos recentes, ficha/execução separadas, histórico real, resumo semanal navegável, ofertas atuais e carrossel de memórias reais. Sem execuções: ação Biblioteca; sem jogos: Adicionar jogo. Rolagem vertical e colunas adaptativas.
5. Item 5: substituir tabela por cards horizontais com logo/nome/tempo/favorito; preservar filtros e busca, sem status/plataforma/gênero nas linhas ou tooltips. Teclado e clique do coração independentes da ficha.
6. Item 6: medir grade antes/depois em volume, identificar decodificações/escala no paint, cache limitado e atualizações sem reconstrução desnecessária; preservar posição, margens e proporção inteira. Não extrapolar benchmark Linux para fluidez no PC do dono.
7. Item 7: verificar cinco capas 70/90/100/125/150, verticais, mesma proporção/base, gaps equilibrados, destaque verde e teclado; corrigir apenas divergências reproduzidas.
8. Item 9: gráficos adequados a dia/semana/mês/3/6/12 meses/todo histórico; remover Gêneros da coleção sem apagar dados; preservar métricas/tempos e fuso. Compartilhar imagens de períodos curto e longo.
9. Item 14: editor de avatar com recorte, arrasto, zoom, orientação e prévia, confirmação/cancelamento e persistência, preservando original. Sem migração destrutiva.
10. Item 10: investigar integração de moldura Windows preservando controles nativos, snap, bordas e fechamento protegido; implementar somente dentro da capacidade verificável, registrar validação Windows real ausente. Nunca contornar closeEvent.
11. Item 11: investigar manifesto e bootstrap do pacote Windows; elevação explícita com UAC, preservação de argumentos/diretório/dados/identidade e cancelamento sem laço. Não elevar auxiliares indiscriminadamente. Sem homologação do pacote Windows nesta rodada Linux, marcar parcial/não testado conforme evidência.
12. Itens 12/13/15/17/18: integridade de preços e regressões de Desejos, banner, favorito, logo Steam, captura e contratos. Console e original individual dependem de capacidade/autenticação comprovadas; sem credencial no ambiente, não inventar suporte nem pedir token no chat.
13. Item 20: documentação, notas locais, versão alvo 0.1.37, suíte completa Linux offscreen, smokes isolados, capturas em 1280×800/1920×1080 e DPI disponíveis; commits locais por unidade, patches integrais e hashes quando entregues.

## Ofertas do Início — critério viável antes da implementação

Usar o mesmo selected_quote/discount_percent de Desejos e respeitar prices.include_keyshops. Candidatos somente com preço atual positivo BRL, origem classificada, identidade/plataforma/edição compatíveis. Desconto individual confiável: grupo inicial em percentual decrescente, desempate nome normalizado/ID; sem desconto confiável: grupo de ofertas atuais por nome/ID, sem rótulo de oportunidade ou recorde. Não há série de observações comparáveis persistida que permita comprovar redução em relação à consulta anterior; não criar histórico fictício nem ranking por redução absoluta. Menor histórico não é original. Não ordenar jogos diferentes pelo menor preço para sugerir atratividade. Sem nova fonte ou scraping; diagnóstico da API será registrado no relatório. Histórico e data da consulta ficam na ficha, nunca nos rodapés do Início.

## Limites e preservação

## Complemento incorporado — ROM local pela ficha

Pedido posterior do dono, mantendo a branch e commits existentes, sem publicação. Já existem game_files.local_path/available/extension/platform, rom_versions.profile_id, EmulatorCommand e Launcher.start_command com monitoramento do processo. Reutilizar esses dados/serviços; não recriar banco ou implementar caminho paralelo de sessões. A4 permanece intacto.

Adicionar origem local claramente separada de Drive na ficha Biblioteca, seletor nativo, existência/leitura, plataforma e perfil realmente compatíveis. Prévia de arquivo/plataforma/perfil e confirmação antes de substituir vínculo; cancelar preserva tudo. Vínculo local não chama Drive/download/cofre, nem copia/move/apaga a ROM. Original anterior permanece em disco e no índice. Arquivo ausente permite localizar novamente, mantendo sessões e metadados. Persistir perfil por ID, sem confundir com executável. Incompatibilidade de extensão/plataforma/edição exige correção da seleção ou abertura/cadastro explícito da edição apropriada; nunca reidentificar por semelhança.

Investigar também candidates/bind/complete_link pela ficha: a busca atual admite substring de título e, quando a ficha não tem plataforma, pode listar outra plataforma; isso é risco, não prova de vínculo errado no vídeo. Harden somente esse fluxo não protegido, com confirmação explícita e sem alterar o cadastro A4. Comparar Ocarina of Time versus Ocarina of Time 3D, com arquivos/plataformas visíveis. Não atribuir preço/sessão/metadados de edição divergente.

Validação: dois programas ROM de teste próprios/legalmente disponíveis, subprocesso de execução controlada, caminhos acentuados/com espaços, incompatibilidade, cancelamento, substituição e originais, ausência/leitura, reabertura, fim de processo e regressão Drive. Identificar fixture e não alegar homologação de emulador real. Capturas reais Qt da origem e do vínculo local. Limitação de fechar apenas a ROM e proibição de troca automática mantidas. Registrar arquivos/métodos protegidos caso apareça bloqueio, continuar independentes.

As duas imagens estão disponíveis; p1.mp4–p4.mp4 citados não foram anexados nesta rodada. Achados descritos são relatos do dono, não reprodução do implementador. Testes isolados usam dois jogos quando aplicável. Imagens geradas são grabs reais do Qt com fixtures identificadas, não aprovação visual nem contas autenticadas.

Preservar banco, sessões, arquivos, identidades, originais, cofre, nove temas e assets. Schema inicial 4: preferir dados existentes; justificar antes de acrescentar persistência. Protegidos: tests/test_save_lifecycle.py, worker.py, enrichment.py, game_import.py, completion_queue.py, dialogs.py e contrato test_protected_drive_and_registration_logic_is_unchanged. Não alterar quick_add.py nem A4. Troca automática de ROM foi descartada; fechar apenas a ROM com emulador vivo continua limitação.

Não enfraquecer asserções, criar skips/xfails ou detectar testes em produção. Expectativas incompatíveis com novos requisitos serão substituídas apenas na cobertura pertinente, preservando a intenção e os testes protegidos. Novas leituras UTF-8, arquivos novos/alterados LF, sem normalizar protegidos. Evidências integrais de comandos e resultados em RELATORIO_0137_TESTES.md e arquivos externos de evidência; limitações e SHAs em RELATORIO_0137.md.

## Complemento visual posterior — Início

Após a primeira captura, o dono pediu capa em vez de banner nos cards recentes, aumentando a presença vertical, e a base do bloco esquerdo na mesma altura da base das ofertas à direita. Essa instrução substitui somente a arte desses cards no item 4.1; banners das fichas continuam inteiros e proporcionais. Capas inteiras, sem recorte; ausência de capa permite banner como alternativa. Memórias começam abaixo de ambos os blocos. Mostrar nova captura antes de fechar o layout.

Complemento visual posterior: título do painel passa a Ofertas (substitui Ofertas dos desejos). Conteúdo continua vindo dos desejos, com política/identidade preservadas. Linhas organizadas, uniformes e centralizadas no espaço disponível, imagem/nome/contexto/preço alinhados; preço sem caixa de botão. Não preencher o painel distribuindo título e linhas arbitrariamente.

Complementos visuais posteriores prevalecem: três jogos recentes visíveis em carrossel horizontal com setas/teclado; área de cada capa acompanha exatamente a proporção da imagem, sem limite de altura que crie faixas ou recorte. Não cortar cantos da arte. Ofertas deve ser lista de linhas consecutivas imediatamente abaixo do título, alinhada ao topo, sem centralização vertical dos itens no painel. Bases dos blocos principais continuam alinhadas.

Complemento visual posterior de Ofertas: usar exclusivamente logo do jogo na linha, inteira e proporcional; não usar capa como miniatura. Sem logo, ícone neutro. Preservar nome/contexto/preço e navegação.

Complemento posterior nos cards recentes: remover plataforma; manter status, última vez e tempo total em três linhas separadas, cada informação sem quebra. Data local curta (hoje/ontem/dia e mês, horário), data completa no tooltip/acessibilidade. Esse recorte é dos cards recentes; plataforma permanece nas ofertas para impedir confusão de edição.

Última decisão de Ofertas: remover toda miniatura/logo e contexto visual; linha somente nome, original riscado, percentual na cor do tema e atual. Essa decisão substitui o pedido anterior de logo. Identidade/plataforma/edição e política continuam validadas nos dados; original/percentual só aparecem juntos quando confiáveis na mesma oferta. API sem original individual mantém nome/atual, sem dados inventados.

Nova prévia solicitada para Ofertas: um banner horizontal por oferta, inteiro e proporcional, e faixa de nome/original/desconto/atual abaixo. Sem logo/miniatura adicional; sem banner disponível, manter linha de dados. Captura inicio-v10 enviada no chat para comparação, sem alegar aprovação estética.

Última instrução de rótulo: Alfabeticamente substitui Nome: A–Z na Biblioteca e Desejos, preservando chaves e comparação de títulos.

Complemento de rótulo: filtro de plataforma mostra somente Todas no estado sem filtro, substituindo Plataforma: Todas/Todas as plataformas; dados/opções e filtragem preservados.

Revisão posterior de Estatísticas: grade de meses em linhas e dias 1–31 foi rejeitada pelo dono. Não manter esse desenho nos períodos longos. Usar mapa de calor compacto (semanas em colunas), barras em Hoje/Esta semana e calendário mensal próprio; parear gráficos menores com Mais jogados para evitar painel largo vazio.

Complemento do Perfil: indicador do slider de Zoom circular, substituindo o quadrado; manter faixa, valores, teclado e funcionamento do recorte. Captura perfil-v2 enviada ao dono.

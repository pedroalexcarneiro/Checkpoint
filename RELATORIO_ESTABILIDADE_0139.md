# Checkpoint 0.1.39 — estabilidade e organização em execução

Plano: PLANO_ESTABILIDADE_0139.md. Base 9ecbc95. Nenhuma publicação autorizada.

## Diagnóstico inicial

- Memórias (4/12): build_memories descarta a página e constrói três abas com
  cards de todos os registros. ArtworkButton lê QPixmap original na GUI; cada
  add_card chama reflow de toda a grade. A quantificação ainda será medida.
- Captura (4/9): capture_game adquire QPixmap, codifica PNG, grava e reconstrói
  página de forma síncrona. Backend atual lê pixels visíveis do desktop e exige
  primeiro plano; não serve para prometer janela coberta sem foco.
- Download (5/15): RomLinkDialog aguarda Job de run_link; reject é bloqueado.
  complete_link reúne vínculo, download e metadados. GoogleDriveClient.download
  não publica progresso/cancelamento; DriveScanner.download usa ID como nome
  físico. Isso não comprova a causa da espera de uma hora relatada.
- Sessões (7/8): Launcher só calcula duração no finish; interrupt e recuperação
  não persistem tempo acompanhado. Não há checkpoint periódico. Revisão cancelada
  deixa a sessão interrompida sem marca de dispensa. Histórico deve ser preservado.
- Diálogos (6): DialogPresentation recentraliza em cada Resize usando a tela do
  pai. É candidato concreto a reposicionamento em transição de DPI; ainda requer
  reprodução controlada. Corrupção ao restaurar não foi reproduzida neste ponto.

## Materiais

Vídeos novos inspecionados por sequência de quadros. O de Memórias mantém a
tela anterior durante a espera e repete após Desejos; clique não tem marcação
precisa. O de download mostra aviso para aguardar e reposicionamento do modal.
Não usar essas cenas como prova de acesso ao Windows, autenticação ou causa.
Imagem nova do Início recebida e lida; implementação visual vem após estabilidade.

## Situação

Implementação em curso. Nenhum item declarado concluído; resultados desta rodada
serão adicionados com comandos, stdout/stderr e códigos completos.

## Unidade 1 — Memórias, desempenho e grade (4/12; parte dos filtros de 11)

Reprodução medida com 96 imagens (88 Full HD/8 4K), 12 notas, quatro imagens
inválidas e quatro vídeos inválidos, dois jogos. Vídeos inválidos verificam que
falha de mídia não bloqueia a página; não comprovam reprodução de vídeo válido.
Antes: navegação 4,944/5,029/4,507 s; primeiro processamento de eventos
5,001/5,084/4,573 s, pico do processo 4091020 KiB. Depois: navegação
0,080/0,007/0,007 s; primeiros eventos 0,107/0,026/0,026 s, pico 130132 KiB.
São ensaios Linux/offscreen isolados; não equivalem ao tempo no PC do dono.

Causas confirmadas na reprodução: decodificação QPixmap original na GUI,
reconstrução das três abas e reflow repetido a cada card. MemoryBrowser preserva
página/abas/cards; só monta a aba consultada e incrementa lotes ao rolar.
MemoryArtwork usa ArtworkCache assíncrono compartilhado de 24 MiB, duas threads,
QImageReader redimensionado e QPixmap na GUI. Retorno sem alteração reutiliza os
widgets; novo registro mantém cards anteriores e ordenação acessível. Nenhum
original alterado. Grade usa largura disponível, mais colunas e sobra equilibrada.

Filtros: jogo apenas dentre registros de Memórias, tipo nas abas existentes,
período e ordenação persistidos. Complemento posterior do dono reafirmado:
não mostrar jogos da Biblioteca sem memória. Teste inclui jogo só com captura,
jogo só com diário e jogo vazio; apagar último diário remove opção do seletor.

Regressão final da unidade: 52 passed, exit 0 (saída integral em evidence).
Primeiras tentativas e falhas preservadas. Asserções de pixels/atribuição não
foram reduzidas: helpers de testes e renderizador aguardam a conclusão real das
miniaturas assíncronas, em vez de presumir leitura síncrona após poucos eventos.
Nenhum protegido alterado. Captura de fixture 1280×800 em evidence/estabilidade-0139.

Estado: desempenho/grade implementados e testados localmente; pastas/indexação
(11), processamento de captura (4/9) e validação Windows desta rodada ainda
pendentes. Não há homologação pessoal nem layout declarado aprovado.

## Unidade 2 — Sessões e dispensa (7/8)

Reprodução do Launcher da base e161dd5, relógio controlado: após 15 s ativos,
SQLite ainda contém zero segundos; interrupt também deixa zero/interrompida.
Registro completo em sessoes-base-repro.json. Isso reproduz ausência de tempo
persistido, sem alegar desligamento real do Windows ou medição do PC pessoal.

SessionTracker grava a cada 10 s e força checkpoint no fechamento/consulta de
desligamento/suspensão. Retomada abre novo intervalo sem somar a pausa; calendário
e totais usam somente intervalos comprovados, mantendo uma única sessão. Lacuna
sem amostra superior a 30 s não é presumida jogo: fica registrada em sessions.gap.
Isso não encerra jogo nem detecta troca/fechamento só de ROM. Crash recupera o
último prefixo comprovado uma vez; instante offline não é somado. Precisão em
queda abrupta é limitada ao último checkpoint bem-sucedido (~10 s mais atrasos).

Fechamento normal salva até o encerramento do acompanhamento e não mata o jogo.
WM_QUERYENDSESSION só salva; WM_ENDSESSION confirmado finaliza sem confirmação
ou rede. Cancelar desligamento não encerra sessão. Mensagens de energia tratam
suspensão/hibernação e retomada. Eventos nativos foram implementados, não ensaiados
em Windows nesta rodada. Checkpoint é melhor esforço, não salvamento interno do jogo.

Falhas de escrita preservam amostra para retry. Checkpoint usa espera SQLite
limitada a 25 ms e restaura o timeout anterior, evitando travar GUI sob escritor
concorrente. Encerramento detectado fica congelado durante retry, sem somar tempo
após sair o processo. Metadados inválidos não impedem abrir nem inventam duração.

Revisão: cancelar/X/Escape (resultado não confirmado do diálogo) persiste
sessions.review_dismissed.<id>, sem mudar duração/registro. Aviso no Início ignora
só aquela sessão; ação manual das Configurações inclui dispensadas. Confirmar
continua idempotente. Página atual remove o aviso após revisão.

Esquema 4 preservado: usa duration_seconds/ended_at existentes e preferências
versionadas por sessão, com identidade/início/fim/soma validados; nenhum banco
recriado nem registro legado reidentificado. Sessão antiga sem checkpoint segue
interrompida para revisão. Asserções antigas/protegidos intactos.

Gate direcionado: 41 testes aprovados (duração no stdout integral), exit 0. Testes cobrem
crash/reabertura repetida, duas revisões independentes, revisão manual posterior,
suspensão atravessando dia, desligamento cancelado/confirmado, erro de disco,
lock SQLite real, retry após fim do processo e checkpoint inválido. Relógio e
processo controlados nos casos novos; regressões existentes incluem processo real.
Estado: lógica/integração local implementadas; eventos de energia e desligamento
Windows real ainda não homologados. Código novo não promete gravação após queda
abrupta nem suporte a salvar progresso do jogo.

## Unidade 3 — Posição do diálogo (parte de 6A)

Reprodução Qt real: mover QDialog preparado para 40/60 e redimensionar altera
indevidamente sua posição. Duas reproduções por fixture falharam na base.
DialogPresentation centralizava em todo Resize, sempre pela tela do pai.
Agora centraliza apenas na apresentação inicial e usa a tela atual para limitar
o tamanho, sem mover em Resize. Uma verificação no primeiro Paint limita a
geometria inicial final de QMessageBox/QInputDialog, que o Qt ainda ajusta após
Show. Não há timer nem repintura periódica; mover/reabrir mantém a posição.

Tentativas intermediárias preservadas: uma mensagem inicial excedia a borda da
tela virtual após o ajuste interno do Qt. Gate com teste de geometria anterior
inalterado: 11 passed in 1.05s, exit 0. Protegidos/ImageDialog intactos.

Estado: causa de recentralização corrigida localmente. Transição real entre
monitores/DPI e flicker do vídeo ainda não homologados. Corrupção da janela
principal ao minimizar/restaurar (6B) permanece separada e não reproduzida;
a correção do modal não é apresentada como solução desse outro defeito.

## Unidade 4 — Downloads da ficha e do gerenciador (itens 5 e 15)

O vídeo de 23:31 mostra o aviso que bloqueava o fechamento e a janela voltando
ao centro ao mover. A duração de mais de uma hora foi relatada pelo dono.
O fluxo de download e vínculo na ficha agora abre tarefa em processo separado,
com fila visível em Configurações > Downloads, navegação livre e cancelamento
cooperativo. A etapa em andamento mostra bytes, percentual e previsão quando
o total é informado. Fechar a janela do Checkpoint durante a transferência
oferece voltar ou cancelar e aguardar a interrupção segura.

O arquivo fica como parcial até passar pela verificação disponível. O destino
final preserva nome e extensão reconhecíveis, trata nomes reservados do
Windows e usa numeração quando há colisão. O vínculo anterior persiste até
a confirmação da gravação. Falhas de metadados ficam separadas da disponibilidade
da ROM. A etapa de publicação tem registro para recuperar o destino verificado
se o processo falhar entre a gravação do arquivo e o SQLite. A4 mantém seu
fluxo de cadastro e seus arquivos protegidos.

Gate direcionado: 76 testes aprovados, exit 0. Inclui fila, cancelamento,
arquivos inválidos/colisões, abertura do processo isolado e regressões de
vínculo. Capturas Qt em 1000×700, 1280×800 e 1920×1080 usam dados sintéticos.
O cancelamento é observado entre blocos/retries. Uma chamada HTTP em andamento
pode chegar ao próprio timeout antes de ceder. Parciais são preservados para
diagnóstico; a retomada automática de parciais não foi implementada. Não houve
Drive autenticado nem teste Windows com o ambiente pessoal.

### Acompanhamento na ficha

O complemento pedido com a imagem da ficha mostra o mesmo cartão de progresso
na aba Arquivos, acima dos vínculos existentes. A ficha acompanha a tarefa
após fechar o diálogo e ao reabrir a página. O painel mostra apenas tarefas
associadas ao jogo ou aos arquivos já vinculados à ficha. A fila global segue
em Configurações > Downloads.

A captura progresso-ficha-1280x800.png é da interface Qt com bytes simulados.
O teste de navegação saiu do diálogo a 25%, conferiu a mesma barra na ficha,
abriu outro jogo sem transferências e confirmou o progresso ao retornar.
Gate de vínculo e transferência: 25 testes aprovados em 3,11 s, exit 0.

## Commits locais já preparados

- f0b43c0: plano/base confirmados e diagnóstico inicial.
- e161dd5: Memórias progressivas/filtros/grade/medição.
- 45208e6: checkpoints de tempo e dispensa por sessão.
- 0732989: manter posição dos diálogos ao redimensionar.
- 0b0734e: fila de transferências, progresso e verificação.

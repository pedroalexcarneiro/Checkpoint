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

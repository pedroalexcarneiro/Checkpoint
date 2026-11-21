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

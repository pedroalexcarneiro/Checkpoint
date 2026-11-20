# Checkpoint 0.1.39 — relatório da rodada local

**Em validação; lançamento autorizado posteriormente pelo dono.** Branch fix/0.1.39-polimento.
Plano: PLANO_0139.md. Este relatório distingue reprodução local, relato,
documentação do provedor e homologação Windows. Não é declaração de conclusão.

## Complementos após o fechamento inicial — em validação

O dono relatou captura repetida no HSR, Memórias desatualizada e nomes/legenda
sobrepostos em Estatísticas menor. Também pediu degradê como referência e
aprovou a segunda prévia com “legal, gostei. podemos seguir”. Foram incorporados
C1–C4 ao plano sem reescrever commits anteriores. A suíte de 752 testes abaixo
é histórica; será repetida após esses complementos antes de publicar.

C4: theme.surface_gradients/stylesheet aplica a intensidade da segunda prévia
às superfícies principais. Destaques/paletas persistidos preservados, Preto
monocromático; navegação usa secondary para contraste no topo mais claro.
As prévias são Qt real/Linux, fixtures Portal 2/Hades/Celeste, não dados pessoais.
Validação direcionada: gradient-approved, 44 passed in 17.64s, exit 0.
Capturas finais desse ajuste em /workspace/work/evidence-0139/degrade-aplicado.

C1: havia nomes UUID distintos por captura; não foi confirmado cache de arquivo
reutilizado. O backend anterior usava QScreen.grabWindow(HWND), que pode devolver
uma superfície antiga em jogos acelerados. Agora WindowsCapture valida PID/HWND/
área cliente antes e depois de copiar um novo quadro visível por GDI/BitBlt,
com bitmap/DC próprios por chamada e liberação em finally. Recusa janela fora
da tela, alvo mudado e sessão inelegível; sem fallback de desktop inteiro.
Não foi possível reproduzir/homologar HSR/DirectX do dono neste Linux.

O defeito de atualização foi reproduzido: capture_game_window só reconstruía a
ficha. Agora atualiza Memórias/Início quando visíveis, sem navegar, preservando
o filtro. build_memories ordena empates pelo ID para que o quadro recém-gravado
apareça primeiro mesmo no mesmo segundo. Nenhum original é sobrescrito.
Arquivos/funções: game_capture.WindowsCapture, windows_capture.client_rect/
grab_client, window.capture_game_window, collection_views.build_memories.
capture-refresh-before: 5 failed, 2 passed (duas bibliotecas/jogos); depois,
capture-refresh-after: 17 passed in 1.24s, incluindo regressões anteriores.
capture-native-frames: 9 passed in 1.91s em Linux. O teste de subprocesso usa
janela Qt própria: em Windows executará o backend nativo e exigirá quadros
vermelho/azul distintos; aqui usou Qt offscreen e não validou GDI/HSR.

C2: reproduzidos o padding herdado no botão de nome e a disputa entre resumo
e legenda pintados em regiões sobrepostas. statistics-responsive-before:
3 failed; primeira correção: 16 passed in 2.49s nos testes direcionados.
A primeira captura com o mapa centralizado em painel largo foi rejeitada pelo
dono por excesso de vazio. A nova regressão de ocupação falhou antes: 2 failed,
1 passed. StatisticsColumns limita a largura do painel ao calendário e dá o
restante à lista; em largura insuficiente, empilha e ajusta o limite de célula.
Não há altura igual forçada. Nomes usam padding zero/reticências medidas e
tooltip completo, logos contidas em 112×48, tempos continuam 16px/negrito.
ActivityHeatmap.footer_layout mede os textos e separa as linhas quando preciso;
PeriodChart/HeatmapViewport acompanham a altura real. Capturas em 1000×700,
1280×800 e 1920×1080 em /workspace/work/evidence-0139/estatisticas-compactas.
statistics-compact-after: 16 passed in 2.56s, incluindo dois jogos/títulos longos,
ocupação mínima, ausência de sobreposição, totais e períodos existentes.

C3: o print cru “Conclusões no período / 11/2026 · 1” corresponde ao código
antigo; o card Jogos concluídos já existia no commit ddac441. Nova captura real
mostra o card integrado ao tema e os testes continuam exigindo timestamp real,
sem inferir datas do status nem modificar registros. Nenhuma correção de dados.

## Gates Linux do fechamento inicial

- **752 passed in 577.63s (0:09:37), exit 0**, Python 3.12.14, Qt 6.8.3
  offscreen, CHECKPOINT_TEST_ROOT=/tmp. Código/testes congelados em
  8dd4c24a9aa73d716dc5c2bd7fc9f805e2a44767; depois só documentação/capturas.
- Smokes do fonte: seis páginas/worker/SQLite e cadastro completos, exit 0.
- Verificação: schema 4, main AST de bootstrap igual, oito paletas intactas,
  assets/workflows/protegidos iguais, exceto método autorizado. Novos/modificados
  textuais UTF-8/LF; prefixo CRLF protegido preservado na exceção declarada.
- 27 screenshots reais com manifesto/hashes em evidence/ui-0.1.39; DPR 1,5/2
  adicionais guardados externamente. Sem dados pessoais.
- 20 patches integrais/hashes registrados abaixo; documentação final posterior
  não muda o código testado. Logs completos de 68 comandos nesta etapa em
  RELATORIO_0139_TESTES.md, incluindo falhas e protótipos descartados.
- Windows/build/executável extraído/publicação: próximos gates, sem alegação
  antecipada de sucesso. A expansão de preços console continua bloqueada.

## Estado inicial e evidências

Base normal 0.1.38: 9dd9c93ce7baf0051bbc783323b401d4ba8c7059, checkout limpo.
HEAD remoto normal e variante sem administrador reconfirmados antes da branch.
Variante build/0.1.38-sem-admin em 1252b815 preservada; não é base desta rodada.
Plano inicial local ffbc816. Nenhum push, PR, tag, release ou workflow executado.

Os prints específicos da 0.1.38 descritos no pedido não acompanharam o arquivo
enviado nesta mensagem. Suas descrições são relatos. Screenshots desta rodada
usam Qt real/Linux offscreen, fixtures identificadas e banco isolado; não abrem
a biblioteca do dono e não equivalem a screenshots/homologação Windows.

Evidências externas locais em /workspace/work/evidence-0139. Os arquivos
stdout/stderr/json são integrais. RELATORIO_0139_TESTES.md reunirá essas saídas,
comandos, ambiente e códigos de saída sem usar contagens históricas.

## Exceção de contrato autorizada

Após a proposta concreta PROPOSTA_DIALOGO_PROTEGIDO_0139.md, o dono respondeu
“Autorizar somente ImageDialog.__init__”. A exceção permite apenas apresentação
do visualizador de capturas. Não autoriza mudar GameDialog, métodos de cadastro,
A4 ou os demais arquivos protegidos. Registrar patch exato e preservação dos
demais métodos/bytes ao fechar. Teste de preservação continua intacto.

## Reprodução inicial

- Item 3: home_view.build_home remove explicitamente AlignTop de AdaptiveColumns
  e promove a seção esquerda a Expanding; Ofertas usa banners de largura inteira
  e stretch vertical. RecentGameCard distribui sobra na QVBoxLayout; largura
  mínima de Continuar jogando é zerada. recent_games elimina sessões repetidas
  por jogo. GameStrip mostra sempre até três cards, sem adaptação à largura.
  Capturas antes/1920x1080-home.png e antes/1280x800-home.png.
- Item 4: WishGrid calcula colunas pelo alvo 300 e permite chegar a 360; arte
  ocupa toda a área central quadrada. Reprodução com dois desejos isolados.
- Item 6: memory_card impõe altura mínima 320 para diário e mídia, inclusive
  na aba só Diário. Texto usa alinhamento padrão sem topo explícito.
- Item 7: existe games.completed_at. Library.save_game grava o instante UTC
  da marcação Concluído, inclusive ao cadastrar assim; remarcação substitui o
  instante. Não é histórico completo de todas as conclusões nem data obtida
  do status atual. period_stats usa esse campo e limites temporais locais,
  ignorando registros sem data. Nenhum dado será criado/regravado por layout.
- Item 8: CoverChoice.paintEvent desenha foco tracejado ao redor do botão
  inteiro sempre que hasFocus, inclusive após clique de mouse.
- Itens 9/10: perfis estão em Dados e backup > Avançado; lixeira em disclosure.
  Gestão existente adiciona/edita perfis, não oferece remoção nem padrão global.
- Item 11: LibraryList não reserva gutter entre viewport/lista e scrollbar.
- Item 13: ui_components.action escolhe colors.text para todos os ícones,
  inclusive botão primário cujo texto usa on_accent.
- Item 14: dark_theme cria as mesmas superfícies azuladas para os nove temas;
  Preto só muda o destaque. Defeito do tema aplicado e de sua prévia.
- Item 15: nome em QLabel wordWrap sem política horizontal explícita dentro
  de layout aninhado compete com StatusChip e botão lateral.
- Item 16: Configurar saves aparece no cabeçalho e no ActionCard vazio
  vertical. Na configuração existente, a pasta é reduzida ao basename.
- Item 16.1: GameSaveBackups.create grava ZIP em save_backups/<game_id>;
  restore valida e usa a pasta da configuração. Drive usa drive.readonly;
  os campos drive_id/drive_folder_id no schema não comprovam implementação
  de upload. Nenhuma sincronização nova autorizada.

As regressões iniciais falham antes das correções. A primeira versão do teste
de Lixeira chamou soft_delete inexistente; corrigida a preparação para Library.delete
e repetida antes de qualquer correção. Falha do próprio teste não é evidência do app.

## Integrações — evidência atual

Item 5: GET https://gg.deals/api/prices/ respondeu HTTP 200 em 16/11/2026;
102257 bytes, SHA-256 922fb4560bb1cccc7be1e55b1cb905e823b21f73d0db8a8f05a1069cce1964c1.
Documento original guardado em ggdeals-api-prices.html.
by-steam-app-id, by-steam-sub-id, by-steam-bundle-id e by-slug documentados.
Resposta documentada: title/url/currentRetail/currentKeyshops/historicalRetail/
historicalKeyshops/currency. Slug não comprova plataforma/edição; seletor
do site não é parâmetro de plataforma documentado para a API. Região br existe.
Não há prova autenticada de oferta console correta nesta instalação.
Estado: bloqueado para consulta console real; proposta concreta de dependência
será incluída no diagnóstico. Não remover aviso nem atribuir preço PC a console.

## Resultados por unidade

### Item 3 — Início integrado

Reproduzido e corrigido localmente; revisão visual do dono ainda pendente.
home_data.recent_sessions lê uma entrada por sessão já persistida (IDs
distintos mesmo jogo), sem alterar recent_games para consumidores legados.
home_view.build_home preserva AlignTop; HomeSectionHeader adapta título/ação;
GameStrip adapta quantidade à largura mínima real do botão. Artes inteiras
limitadas a 210 px de altura, cards limitados pela medida do conteúdo, sem
esticar para acompanhar a coluna direita. MainWindow.navigate libera somente
a largura do Início, preservando margens externas 24 px.

HomeOfferRow/OfferThumbnail substituem banners por linhas, miniatura, nome,
origem e preço; plataforma somente quando necessária para distinguir o item.
Originais/descontos mantêm a política da mesma oferta. Pintura usa contorno
arredondado de 12 px na arte real, inclusive quatro cantos; teste verifica
os quatro cantos e centros das quatro bordas, proporção e ausência de sobreposição.
Par de chevrons usa o mesmo SVG original espelhado, sem modificar asset.

home-after: **40 passed in 4.80s**, exit 0, dois jogos parametrizados e
1280×800/1920×1080/1000×700/restauração de largura. Primeira iteração expôs
quatro expectativas antigas de base compartilhada e preenchimento total
da arte: foram substituídas pelo alinhamento superior e área contida,
em obediência ao requisito novo. Verificações dos pixels das quatro bordas,
navegação/limites, status e metadados de linha única preservadas; mais
sessões acrescentadas para exercitar navegação também na janela larga.
Nenhuma asserção de dados/contratos foi enfraquecida.

Capturas proposta-inicio-2/1280x800-home.png e 1920x1080-home.png compartilhadas
no chat, fixtures Linux Qt DPR 1. A primeira proposta encontrou miniatura
sobreposta por política Ignored herdada; Fixed aplicado só à miniatura e
regressão de não sobreposição acrescentada antes da captura posterior.
Essas imagens são redimensionamentos; maximização/restauração Qt serão
registradas separadamente. Não declarar homologação Windows ou aprovação visual.

Complemento posterior do dono: retirada a faixa escura lateral das capas,
causada por preencher de input a área maior que a imagem. Agora essa sobra
usa o fundo do card; imagem inteira continua limitada e arredondada.
home-letterbox-after: **26 passed in 3.85s**, exit 0, incluindo comparação
de pixels entre a sobra da arte e o card, com dois jogos.
scripts/render_0139_review.py acrescenta reprodução autônoma com tela virtual
1920×1080, showMaximized/showNormal e manifesto de dimensões/estado/DPR.

### Item 4 — Desejos compactos

WishGrid.reflow usa alvo de 240 px e teto de 280 px, abaixo do teto anterior
360; não amplia poucos cards para completar janela. Proporção 1:1, mais
colunas, textos/preços/fontes/favoritos e ficha exclusiva preservados.
wishes-after: **20 passed in 4.02s**, exit 0, cobrindo dois jogos, proporção,
colunas, filtros, ordenação/posição, ficha exclusiva, ausência de tempo e
rodapé sem vão excessivo. Screenshots normal/maximizada gerados com dois
e vários desejos pelo renderizador novo; revisão visual ainda pendente.

### Item 6 — Diário

collection_views.memory_card aceita composição de Diário sem altura mínima
de mídia; build_memories aplica somente na aba Diário. Conteúdo alinhado à
esquerda/topo, margens 16 e gaps 12, sem alterar texto. Visualização mista
mantém a altura/grade equivalente de capturas; exclusão exige confirmação e
preserva originais. memories-after: **18 passed in 2.53s**, exit 0, dois jogos,
texto intacto, layout compacto e regressões de exclusão/cancelamento/arquivos.
Screenshots memorias/memorias-diario.png e memorias-mista.png compartilhados
(1280×800, Linux Qt, fixtures). Aprovação visual do dono não presumida.

## Limitações preservadas

### Item 7 — Jogos concluídos

Auditoria descrita em Reprodução inicial: completed_at é última marcação
de conclusão por jogo, não histórico de todas as conclusões. Serviço e
persistência intactos. statistics_view.render_statistics apresenta card
coeso Jogos concluídos com total, filtro atual e rótulo objetivo de significado;
distribuição mensal preservada na dica acessível. Sem data gravada não conta,
mesmo com status Concluído. Nenhum registro apagado/criado/modificado.
completions-after: **15 passed in 3.00s**, exit 0, dois jogos, ausência de
timestamp, limites/DST/períodos, preservação dos campos. Teste antigo foi
atualizado somente no título substituído expressamente pelo pedido.

Sem reconhecimento automático de troca de ROM. Fechar só ROM mantendo o
emulador aberto continua limitação conhecida. UAC, contas, cofre real, hotkey
Windows, emuladores reais, DPI/monitores nativos e executável desta rodada
não homologados no PC do dono. Sem novo schema nem alteração de dados pessoais.

## Complemento item 6 — mesma área de prévia

MemoryGrid alinha cards pelo topo. Na visualização mista, QTextEdit somente leitura ocupa os mesmos 160 px de ArtworkButton, sem mudar o texto; aba Diário permanece compacta. mixed-preview-after: 4 passed in 0.59s; memories-alignment-after: 28 passed in 3.17s. Capturas memorias-preview substituem a proposta anterior.

## Item 8 — foco de capas

CoverChoice distingue foco por teclado de clique; retira contorno externo e desenha foco dentro da capa somente por teclado. Seleção, cinco tamanhos, bases, percentual e persistência preservados. cover-focus-after: 24 passed in 3.34s, exit 0, dois jogos.

## Item 11 — espaço da rolagem

LibraryList reserva viewport de 16 px e barra constante, com handle desabilitado quando não há rolagem. Sem salto horizontal ou sobreposição de favorito. Verificação local corrigiu o próprio teste: QScrollBar.x é relativo ao container; usa-se mapTo(view). local-components-after: 43 passed in 4.41s, incluindo lista, favoritos, pixels e memórias; primeira rodada gutter teve dois falsos negativos do teste, preservados nos logs.

## Item 14 — Preto neutro

Paleta Preto passa a superfícies/contornos cinza-neutros e preview usa a mesma paleta aplicada. Oito outras paletas e nove opções preservadas; sem assets alterados. black-after: 23 passed in 17.54s, contraste de texto e persistência/navegação em todos os temas aprovados.

## Item 13 — ícones primários e rótulos

action usa on_accent no ícone primário e disabled no estado desabilitado, copiando o QIcon antes de acrescentar modo para preservar o cache. ElidedLabel centraliza texto de linha única com dica completa. icon-and-trash-final: 19 passed in 1.86s, incluindo os dois jogos e os pixels dos estados normal/desabilitado. Calibração do próprio teste corrigiu import de QIcon e tolerância de 1 nível RGB no antialias; branco continua reprovado.

## Itens 9/12 — execução, perfis e diálogos básicos

EmulatorProfiles reutiliza IDs/SQL/argumentos existentes na página e no modal; remove somente perfil sem vínculos e após confirmação. Perfil em uso é preservado com motivo e caminho de seleção alternativo. ExecutionProfileDialog filtra plataforma/extensão/capacidade, salva só profile_id e mantém região/revisão; cancelar não escreve nem executa/baixa ROM. MainWindow.configure_execution preserva editor para jogos sem ROM. DialogPresentation é opt-in por diálogo já construído, sem filtro global, sem temporizador de contorno e sem alteração em seletor nativo/UAC. AppMessages/AppInputs constroem modais explícitos em português; aviso de sessão usa Cancelar/Iniciar sessão e padrão Cancelar, com fim manual acessível na Atividade. Setas desabilitadas atenuam somente o ícone. dialogs-navigation-final: 57 passed in 21.03s, incluindo sessões/ROM local/cancelamento/perfis/lifecycle/contrato. Mock targets de quatro testes foram ajustados para a nova fábrica própria; asserções preservadas. Protótipo inicial de observador de ChildPolished foi descartado após reentrância/duas quedas -11; execuções interrompidas e falhas ficam nos logs, não contam como aprovação. A implementação entregue não usa esse observador.

## Itens 9/10 — abas Emuladores e Lixeira

Aparência/Conexões/Downloads/Dados e backup preservam índices; Emuladores e Lixeira acrescentadas, seção ativa sobrevive à restauração. Gestão sai do Avançado; restauração sai do disclosure. trash_view usa card horizontal com logo contida da Biblioteca, nome, data/hora real e Restaurar à direita. Homônimos distinguem plataforma/registro. Data vazia/inválida mostra Data não registrada; data sem hora explicita horário ausente. Não classifica registros ativos sem deleted_at como lixeira, não inventa informação e não oferece exclusão/limpeza nova. icon-and-trash-final: 19 passed in 1.86s; all-new-before-final: 50 passed in 6.05s; restauração individual, integridade, estado anterior e originais preservados.

## Itens 15/16 — Arquivos e saves tradicionais

Nome da ROM ocupa centro expansível com elipse e tooltip integral; situação abaixo e ação à direita, sem modificar original_name. Saves vazio usa linha compacta e única ação; configurado mostra caminho completo acessível, padrões, último backup real e ações existentes. Campo e histórico/serviços de backup não mudam. settings-tabs-after: 32 passed in 19.28s, incluindo nome longo em 1000/1280/1920, dois jogos, saves e registros íntegros. Primeira checagem de nome encontrou erro do próprio teste ao buscar botão dentro do widget de texto; corrigido o ancestral, sem mudar geometria exigida.

## Item 12 — exceção ImageDialog autorizada

Somente ImageDialog.__init__ mudou em dialogs.py: usa FittedImage e apresentação opt-in. Prefixo protegido anterior à classe é byte a byte idêntico. O método novo usa LF; prefixo legado CRLF foi preservado para respeitar a exceção restrita e evitar normalização incidental de protegidos. Nenhuma alteração em GameDialog/QuickAdd/A4/lifecycle. Testes reais do modal verificam redimensionamento, proporção, arquivo original e prefixo protegido; contrato AST segue intacto. Testes novos completos: 50 passed in 6.05s.

## Item 12 — demais diálogos próprios

Apresentação opt-in estendida após validação básica a artes/progresso/catálogo/Drive/pastas/metadados/Steam/perfil/atualizações. Mudanças restritas a imports e preparação visual; funções de negócio preservadas. game_editor/trash_import adotam somente as fábricas próprias nos popups já existentes. Erros de bootstrap usam a mesma fábrica, sem alterar decisões de UAC/cancelamento/retornos ou diretório de dados. dialog-additional-after: 73 passed in 8.63s, incluindo Steam, perfil/avatar, atualizações, catálogo, pastas, artes, lixeira e regressão do fluxo Drive protegido. Windows DWM/DPI/monitores reais continuam não homologados.

## Complementos finais de revisão visual

O dono pediu agrupamento dos botões de Emuladores: Novo perfil junto da lista,
Escolher executável ao lado do campo, Remover/Salvar juntos no rodapé com Salvar
em destaque. Aplicado em EmulatorProfiles; emulator-actions-after: 38 passed
in 3.39s, dois jogos. Pediu também mais espaço entre mensagem e botões no aviso
de sessão; margens de 24/20 e gap vertical de 18 no layout do QMessageBox.
Após ver as duas novas capturas, respondeu “ok, gostei”. Essa resposta aprova
essas composições apresentadas, não constitui autorização de publicação.

A validação adicional de posicionamento detectou crescimento do QMessageBox
após Show com texto traduzido/margens: numa tela virtual menor que a janela
principal, a borda direita podia passar. DialogPresentation passa a ajustar
limites/centro também em Resize, com proteção de reentrância, sem temporizador.
A asserção de contenção da janela foi mantida. O aviso mantém padrão Cancelar.

A fábrica nova de erros de bootstrap exigiu atualizar somente o alvo do stub
QMessageBox no subprocesso de test_elevation_0137 (para AppMessages). Primeiro
run teve dois timeouts dos próprios stubs; startup-final: 20 passed in 3.37s,
com as mesmas asserções de uma única elevação/nenhum dado ou cofre preparado.
Nenhuma decisão de UAC foi alterada e o código de elevação está intacto.

Reprodução final independente na base normal 9dd9c93, usando worktree somente
para teste e os testes já corrigidos: regressions-base-final teve 33 falhas
em 4.12s antes das correções. Isso substitui os falsos negativos das primeiras
versões dos novos testes de coordenadas/imports. A base recebeu somente cópias
de testes, nunca mudanças do produto ou dados pessoais.

## Validação dos últimos complementos e nova autorização

Dialog-layout-final: 62 passed in 7.41s, exit 0: aviso com gap mínimo 16,
contenção/centragem mantidas após layout, UAC sem preparação de dados antes
da decisão, perfis/ROMs e todas as regressões visuais novas. Capturas de
100%, 150% e 200% concluídas em Qt offscreen; escalas sintéticas e manifesto
não homologam DPI/monitores nativos do Windows. Versão declarada 0.1.39,
schema permanece 4. Novos arquivos e linhas modificadas usam UTF-8/LF;
exceção do prefixo protegido CRLF de dialogs.py documentada acima.

O dono autorizou lançamento posterior: “ok, quando finalizar, pode já dar
release no github”. A pendência console havia sido comunicada imediatamente
antes. Envio/testes Windows/publicação passam a ser autorizados após os gates,
sem declarar a expansão multiplataforma como entregue. Relatório específico:
RELATORIO_LANCAMENTO_0139.md. As proibições no registro inicial descrevem
somente a primeira fase e não apagam essa autorização posterior.

## Regressões encontradas na primeira suíte integral atual

A execução full-linux sobre 64d64de não concluiu: quatro falhas observadas e
interrupção controlada (-15, 385,59 s) no teste de fechamento com job ativo,
cujo stub ainda substituía QMessageBox Qt em vez da fábrica própria. O próprio
teste voltou a interceptar AppMessages, mantendo a exigência de aviso/janela
aberta/espera do job. O guard do renderizador contra warning modal também foi
apontado para AppMessages, preservando suas asserções e timeout.

Duas falhas eram requisitos de apresentação substituídos: test_card_layout
exigia largura mínima 280; agora exige faixa 220–280 mantendo fonte/itens/link/
proporção/colunas. test_complete_layout agora inclui texto de QTextEdit somente
leitura junto de QLabel para conferir nota visível e exclusão de nota de jogo
removido; asserções de conteúdo intactas. Ajustes derivados dos itens 4/6 e do
complemento visual expresso do dono, sem relaxar dados ou contratos.

As outras falhas revelaram recriação desnecessária dos cards ainda visíveis
no redimensionamento: referência da arte podia ser invalidada e uma composição
antiga aparecer em consultas de filhos. GameStrip agora reutiliza tiles das
sessões que continuam visíveis, preservando foco; remove corretamente só os
que saem. Arte ausente tem altura conhecida antes do layout. MemoryCarousel
retira da árvore os cartões descartados antes de liberar. Sem alterar sessões.

full-regressions-fixed: 30 passed in 18.95s, exit 0, incluindo quatro falhas
originais, foco/arte após redimensionar, job ativo e ciclo de vida do renderizador.
Uma nova suíte integral será executada no commit corrigido; a tentativa parcial
não é tratada como validação aprovada. Arquivos/saídas originais preservados.

## Compatibilidade final das expectativas visuais aprovadas

A suíte completa sobre 9856afc concluiu: 4 failed, 748 passed in 577.49s,
exit 1. Sem falhas novas de dados/execução; restaram quatro expectativas antigas:
Layout_0134 exigia faixa 280–360 em Desejos (dois jogos em janela larga),
Layout_regressions_025 limitava o cabeçalho do Início a 1392 mesmo após o pedido
expresso de largura útil, e Reference_layout_0128 ainda exigia o título antigo.

Atualizações restritas aos requisitos substituídos: faixa 220–280 e mais colunas
pelo alvo 240 mantendo proporção quadrada; Início exige margem lógica 24–32
em cada lado enquanto demais páginas mantêm limite anterior; título Últimas
sessões preservando Resumo/Memórias e ação correta de Continuar. Não há alteração
no produto neste ajuste, nem relaxamento de asserções de dados ou contratos.
Nova suíte integral será executada com essas expectativas aprovadas pelo escopo.

## Quadro de entrega e rastreabilidade


| Item | Status | Commit(s) | Arquivos e funções | Evidência e limite |
|---|---|---|---|---|
| 3 / 3.1–3.5 | feito em código; revisão específica registrada | c08f268, e60def3, 9856afc | home_view.build_home; home_data.recent_sessions; RecentGameCard/RecentArtwork/GameStrip/HomeOfferRow/HomeSectionHeader; MainWindow.navigate | Capturas antes e depois; sessões repetidas, foco, quatro bordas/cantos, CTA, limites e semana; 40/26/30 testes direcionados nos logs |
| 4 | feito | e8d1675; 8dd4c24 | collection_views.WishGrid.reflow | Alvo 240/teto 280, 1:1, mais colunas; 20 testes direcionados, dois/vários desejos normal/maximizada |
| 5 | bloqueado | 64d64de | DIAGNOSTICO_INTEGRACOES_0139.md; provedores não alterados | HTTP 200/doc hash registrado; sem oferta console autenticada ou contrato de plataforma/edição comprovado |
| 6 | feito; complemento visual aplicado | a367b4d, 192ed37 | collection_views.memory_card/MemoryGrid/build_memories; MemoryCarousel | Diário compacto e grade mista com prévia 160; texto/cancelamento/arquivos preservados; capturas e 18/28/4 testes |
| 7 | feito com significado explícito | ddac441 | statistics_view.render_statistics | Última marcação completed_at existente, não histórico inventado; 15 testes e captura estatisticas-conclusoes |
| 8 | feito | 0aa66ed | settings_previews.CoverChoice | Mouse sem contorno externo, foco do teclado dentro da capa; 24 testes, cinco opções e valores preservados |
| 9 | feito | 1a9630d, da0e847, 92ae641 | EmulatorProfiles/EmulatorDialog; ExecutionProfileDialog; MainWindow.configure_execution | IDs/argumentos/plataformas/vínculos; edição, remoção confirmada/in-use bloqueado, seleção compatível, cancelamento/reabertura; botões aprovados pelo dono |
| 10 | feito | da0e847 | settings_view.build_settings; trash_view.build_trash/deletion_label | Cards com logo/nome/data/Restaurar, homônimos distintos, Data não registrada; restauração individual e integridade |
| 11 | feito | ff00484 | library_list.LibraryList.__init__ | Gutter 16 lógico/barra estável; lista/favorito/teclado/rolagem preservados |
| 12 | feito em ambiente controlado; homologação nativa parcial | 1a9630d, 45a49d8, a563c5e, 92ae641 | dialog_style; construtores opt-in; ImageDialog.__init__ autorizado | Português, padrão/cancelamento/Escape, limites/Resize, FittedImage e abertura; seletores nativos/UAC preservados; 57/73/62 testes nos lotes |
| 13 | feito | 4544f16 | ui_components.action | Ícone primário on_accent e disabled; pixels comparados; logos de serviço intactas |
| 14 | feito | 3fcbfda | theme.THEMES[black]; ThemePreview | Superfícies neutras; oito outras paletas exatamente iguais; 23 testes de tema/contraste, capturas |
| 15 | feito | a187482 | detail_view.build_detail; ui_components.ElidedLabel | Nome ocupa centro, elipse/dica integral, status abaixo e ação à direita; 1000/1280/1920, dois jogos |
| 16 | feito na composição existente | a187482 | detail_view.build_detail | Uma ação no vazio e no configurado, pasta integral/último backup real; sem alterar serviços |
| 16.1 | diagnóstico feito; sincronização remota não implementada | 64d64de | DIAGNOSTICO_INTEGRACOES_0139.md | ZIP local, caminho e restauração documentados; Drive read-only; proposta separada de upload |
| 17–19 | preservados nos testes disponíveis | 9856afc; verification-result.json | Dados, A4, tempo, UAC, favoritos, ROM local, captura, saves/schema/cofre/assets | Bytes/AST verificados; único método protegido excepcional documentado; sem dados pessoais ou nova migração |
| 20 | Linux aprovado; Windows a validar | 8dd4c24 | Suíte integral e smokes | Resultados atuais em RELATORIO_0139_TESTES.md; não reaproveitar falhas/interrupções como aprovação |
| 21 | capturas feitas; limites explícitos | 9856afc | scripts/render_0139_review.py; evidence/ui-0.1.39 | 27 PNGs + manifesto no Git; 20 capturas adicionais em cada DPR 1,5/2 fora do Git. Fixtures Qt/Linux, não Windows do dono |
| 22 | relatórios e notas preparados; lançamento autorizado depois | 64d64de e documentação final | PLANO/RELATORIO/TESTES/NOTAS/DIAGNOSTICO/LANCAMENTO e docs atuais | Revisão por commits/capturas; sem publicar suporte console não comprovado |

## Patches dos commits de implementação e testes

Intervalo fechado: 9dd9c93ce7baf0051bbc783323b401d4ba8c7059..8dd4c24a9aa73d716dc5c2bd7fc9f805e2a44767.
Cada arquivo foi gerado por git format-patch -1 <sha> --stdout. Patches integrais
em /workspace/work/evidence-0139/patches; documentação final e pós-publicação
posteriores ao intervalo continuam no histórico Git, sem reescrever os commits.

| SHA completo | Assunto | SHA-256 do patch |
|---|---|---|
| ffbc816980845456f0b56395c4b0a04af2334431 | docs: registrar escopo local e validacao da 0.1.39 | 922c581e74af031166f3f184bbb0b47362eeaff139f09998fe5e25f6c5f41bfd |
| c08f268761c090ce41bb52ca34839aed46cdf6d2 | fix: compactar Inicio e navegar por sessoes reais | 427cbde3bedd11b845cc2a2459cfc51a44184bfea38cd6cc7a902ae5494bc5dd |
| e60def39bae0fb8df39f771a93f046f33960f5a5 | fix: retirar fundo escuro ao redor das capas recentes | 573560aad319c73e2f6265e31786355ccf973fa2069a0dc20975c3da1def4f51 |
| e8d167543b1fe80009a872e109205ab7f160a59e | fix: reduzir cards de Desejos e ampliar quantidade de colunas | c0413f5cd185ab020b94b6da054df91dd4bb6362a01fbcc22800701762e0ac18 |
| a367b4de3ff8a24aea363f198e1b465f48508ae0 | fix: compactar Diario preservando grade mista de memorias | c6072378492088f15e7232e654a3f49bb8747253ac2a15458774817eaf6f33be |
| ddac44190d1ed6fd0c7f037417df9da3047c4250 | fix: integrar conclusoes registradas ao periodo de estatisticas | 79a985ff70d015910af16581d2d4f4e615bbaac3b41aa7e4cbca7d5b89717ddd |
| 192ed37fc5359989574af3a0257bad41db9abb01 | fix: alinhar previas de Diario e capturas na grade mista | bf32d9d25e04c39e16eb75c2062b2ffe067cb99e43d3521b1e4ff82717216cbc |
| 0aa66ede160c2dc764d238e17db551c7f5a1a37e | fix: manter foco das opcoes dentro da propria capa | e201b97e78477195514ed7c3a0a8c435334f32fb2e934770b861f83b426ce9ab |
| ff004842ce1b5dfead822111c8e4d43035a2d196 | fix: reservar espaco estavel entre lista e barra de rolagem | f857124056d7381013bdecbce51accd5405dc68736e8a96ae40b7532b2857bf6 |
| 3fcbfdae53f2d1a1433efadb21ba0b01cefb5586 | fix: usar superficies neutras no tema Preto | c35e5cf45ccb0e2b240b36731d095afcedda002ab27a1cafd15c5b4764dc0bd6 |
| 4544f16d3818e3bc8e3ed2ee96e2eefbd8dd4ec3 | fix: harmonizar icones primarios e rotulos de linha unica | c2e2c3284359f33ac3adbde9ae9362ac1ac659327cbe4a245e6e36d4451dfe0a |
| 1a9630df8d7d34e29529aabd4a0475d8c010a714 | fix: padronizar dialogos de execucao e preservar perfis vinculados | cdf6d14dcaa206bbd8ddf20f34a5ef2ef667fb9d53701b024261ebc097e6e214 |
| da0e847c3352c803b0b7ede42fc3380f7c1218c9 | fix: expor Emuladores e Lixeira com cards e restauracao individual | 19f8f89f6d93d0a2aec33a515c6b041ce5266fe2271b5e1531cd9869b7eff5b4 |
| a187482d232a628a42badc824fe9cb3fdf5ed442 | fix: organizar nomes de ROM e compactar saves na ficha | a5e6da85fa5312f857477bdecea68a0ffeb5f84a2cc32a41a902c26ad2934789 |
| 45a49d8e510a1586c641ade4327b7ced2abe5b77 | fix: adaptar visualizador de capturas na excecao autorizada | 789ce47e0f01183707b72526294d417f8144f844bdc1aedc23e6aaad950eef9d |
| a563c5ef88ba0591587e4c6f3558777553f2dadc | fix: aplicar apresentacao comum aos demais dialogos do app | 51865a004247bb50d3ff6197ca7a5444300cf2cd4adbf2145c3f191c32e26fc1 |
| 92ae641f775d35954648fda2a62a6823872a43e5 | fix: fechar revisao de botoes e espacamento dos avisos | 4636faa095eb26127146fa4c77803d038acb6bfe5e08ea6f259544b7a09c35bb |
| 64d64de0801aadfddf2f90610a304b4b82921003 | docs: preparar 0.1.39 e registrar limites das integracoes | 3473f653140574de9f76bcc19d51114dc7cce7a229d101008395e64a2adab90a |
| 9856afcfbde9d2b98130d127eb25fd9fb8072540 | fix: preservar cards e foco ao redimensionar carrosseis | d29bfc2e430572f75707c3e9f69837f4ac42f82003008bae1cf52e66b926a318 |
| 8dd4c24a9aa73d716dc5c2bd7fc9f805e2a44767 | test: alinhar contratos visuais aos requisitos aprovados da 0.1.39 | c51d1dc08fee1f7fc361633bbd92cb709db96456fd3d53b82a39fd878a9ff154 |

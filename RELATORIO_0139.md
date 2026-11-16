# Checkpoint 0.1.39 — relatório da rodada local

**Em andamento, sem publicação autorizada.** Branch fix/0.1.39-polimento.
Plano: PLANO_0139.md. Este relatório distingue reprodução local, relato,
documentação do provedor e homologação Windows. Não é declaração de conclusão.

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

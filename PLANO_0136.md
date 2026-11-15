# Plano local — Checkpoint 0.1.36

Autorização: pedido completo de 15/11/2026 e referências enviadas neste chat.
Base reconfirmada por fetch: fix/0.1.35-ajustes, 818ec80a492a29936782ddb3a43eecaf3ef996e3; sem alteração em relação ao HEAD documental informado. Checkout inicial limpo. Branch local: fix/0.1.36-ajustes. Não publicar, fazer push, PR, tag, release, alterar assets ou acionar lançamento.

## Ordem, implementação e aceitação

1. **06 — captura global**: investigar RegisterHotKey/WM_HOTKEY nativos, ciclo de vida e conflito; selecionar janela por sessão/PID e primeiro plano verificado; rejeitar ambiguidades e alvos inválidos. Testar adaptadores com dois jogos, múltiplas sessões, troca/conflito/liberação e gravação única. Windows real e conteúdo DirectX não são demonstrados por Linux.
2. **04 — banner da ficha**: reproduzir geometria/contain, duas proporções, Biblioteca e Desejos, abrir grande e alternar/restaurar. Corrigir apenas defeitos comprovados; preservar imagem inteira. Evidências Linux 1280×800 e 1920×1080, DPR registrado, sem alegar DPI do dono.
3. **02–03 — preços**: consultar documentação atual da API, distinguir suporte do site/API/conta; identidade de plataforma/edição explícita, sem semelhança de nomes. Preservar caches e proveniência. Original/desconto só da mesma oferta, moeda, plataforma e edição. Se incapaz, documentar bloqueio e entregar apenas partes comprovadas. Ordenação estável e motivos específicos; oficiais por padrão, opção keyshops persistida.
4. **07–09 — Estatísticas**: reproduzir métricas equivalentes e nomes/valores longos; filtros locais consistentes; semana começa segunda-feira, períodos móveis de calendário terminam agora, dia limitado ao mês de destino. Intervalos semiabertos, sessões repartidas e recortadas em UTC após conversão dos limites locais, sem mudar dados. Steam agregado só no total geral. Integrar gêneros e conclusões antes de retirar Mais estatísticas.
5. **10 — cinco capas**: 70/90/100/125/150%, faixa atual compatível. Preferências intermediárias mapeadas à mais próxima (empate para menor); fora da faixa nos extremos; preservar preferência antiga até escolha explícita, sem recriar configurações. Mouse/teclado/foco, base comum, persistência e efeito na grade, dois tamanhos de janela.
6. **11–12 — acabamento**: medir área/opacidade/alinhamento Steam/Drive sem editar assets; inspecionar fontes, containers e escala antes de ajustes locais, preservando nove temas, wordmark/cabeçalho, Desejos 360px/1:1/colunas, estados e Memórias, backups.
7. **01 e 05 — apresentação**: remover tempo dos cards/exclusivo de Desejos sem perder histórico/posse; remover descrição do Hero do Início mantendo banco/Sobre/ação/identidade e contain.
8. Regressões pertinentes antes/depois de cada unidade, suíte integral Linux; atualizar documentos, notas não publicadas e relatório com SHAs e limitações reais. Commits locais por item/unidade, sem reescrever os anteriores.

## Evidências e limites

Vídeos recebidos: 1.mp4 (179,221s, Início), 2.mp4 (181,760s, Adicionar desejo) e 3.mp4 (81,152s, Biblioteca/Configurações); todos 1280×720. Quadros selecionados, não controle do PC do dono. 3.mp4 00:20 e 00:34: prévias pequenas/controles Conexões; 2.mp4 01:31: ausência de preço; 02:02: notas curtas não comprovam defeito na grade. Moldes antigos orientam layout, sem números/círculos, cabeçalho extra, rodapé Biblioteca pessoal, Verde duplicado ou ST. Novo requisito de cinco capas substitui slider e três exemplos.

Evidências geradas em /workspace/work/evidencias-0136, fora do versionamento de mídia pessoal. RELATORIO_0136_TESTES.md guarda stdout/stderr integrais, comando, ambiente e exit de cada execução. Não usar resultados da 0.1.35 como testes atuais.

## Contratos e dados

Não alterar arquivos/testes protegidos nem sequência A4; quick_add fora do escopo. ROM fechada com emulador vivo permanece pendência separada. Não abrir base pessoal nem credenciais; SQLite, mídias e ROMs de teste isolados. Novos/alterados UTF-8 e LF. Textos somente títulos, rótulos, erro/estado vazio acionável ou motivo objetivo; descrição externa somente no lugar apropriado. Não remover cobertura ou enfraquecer asserções; expectativas somente nas mudanças explicitamente autorizadas.

## Complementos solicitados durante a execução

- Mais jogados no período: logo à esquerda, nome no meio, tempo à direita com 16px/seminegrito/contraste; estilo da lista aprovado no chat.
- Remover sobra fixa abaixo da legenda do mapa de calor; altura acompanha conteúdo e eventual barra horizontal.
- Cinco capas com vãos iguais entre contornos e margens externas iguais, mantendo base comum.
- Percentual na cor do tema ativo.
- Ausência de preço: instrução posterior substituiu Sem preço salvo pelo hífen literal `-`; manter motivo curto embaixo, sem zero nem silêncio.
- Banner: proporção original fixa; altura do bloco acompanha a largura, imagem inteira em escala uniforme e geometria fracionária, sem faixa lateral. Testar quatro bordas e alternar maximizado/restaurado no ambiente disponível.
- Aprovação específica recebida para atualizar coordenadas do teste da logo Steam de x+8/y+8 para x+10/y+7 e raster explícito em 100%, mantendo igualdade de pixels e arquivo original.
- Complemento posterior aprovado: ficha exclusiva aberta em Desejos mantém esse contexto e volta à lista, sem adquirir o jogo. Retirar Adicionar à biblioteca da ficha; menu coerente com Desejos; manter aquisição somente por ação explícita na lista.

# Checkpoint 0.1.37 — notas da publicação

Pré-release publicada após autorização posterior do dono: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.37. Testes e pacote Windows aprovados; 695 testes Windows e 695 Linux. As limitações abaixo permanecem explícitas.

- Início reúne últimos jogos executados, resumo semanal, Ofertas e memórias recentes. Três capas inteiras em carrossel; ações de ficha e execução separadas.
- Biblioteca em lista usa cards com logo, nome, tempo e favorito. Grade preserva capas inteiras e margens equilibradas; cache e carregamento em segundo plano reduzem trabalho durante a rolagem.
- Estatísticas adapta o gráfico ao período e remove Gêneros da coleção sem apagar os dados.
- Foto de perfil permite recorte, reposicionamento e zoom, com prévia e cancelamento.
- Ficha da Biblioteca permite escolher ROM local, validar plataforma/perfil, confirmar vínculo e executar pelo fluxo acompanhado, sem Drive ou upload. Os arquivos originais e o histórico são preservados.
- Desejos inclui filtro de plataforma e cards compactos. Ordenação usa Alfabeticamente; ausência de preço mantém hífen e motivo real.
- Controles de janela integrados e pedido UAC foram implementados; homologação interativa da moldura e do UAC no PC do dono permanece pendente.

Limitações importantes:

- Consulta de preços console e preço original individual da API oficial GG.deals não foram comprovados. Filtro de plataforma não significa cobertura de consulta pronta. Percentual só aparece com original confiável da mesma oferta.
- DWM/Snap/DPI/monitores, UAC, captura elevada, launchers, contas e emuladores reais não foram homologados no Windows do dono.
- Testes de ROM usam dois programas próprios e executor controlado; não certificam emuladores reais. Fechar só a ROM mantendo o emulador aberto continua limitação; troca automática não foi implementada.
- Adicionar jogo > ROM do Drive permanece sob o contrato A4, sem alteração.

Schema 4 e arquivos/identidades/sessões/assets originais preservados. Resultados efetivos e evidências nos relatórios 0137.

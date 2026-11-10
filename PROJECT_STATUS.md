# Estado do projeto — Checkpoint

Atualizado em 10/11/2026. Versão 0.1.2 de desenvolvimento. **O projeto completo não está concluído.** O ponto de continuidade é este diretório, com código real, documentação e testes.

## Implementado e utilizável localmente

- Python/PySide6, tema escuro editorial, navegação persistente e estados vazios.
- Banco SQLite local com WAL, FKs, transações, duas migrações, trava de instância, logs rotativos e backup consistente.
- Biblioteca: cadastro/edição de campos pessoais, capas/banner/logo por arquivo, filtro de título/plataforma/gênero/status, ordenação, favoritos, categorias em texto, galeria 3:4 e lista.
- Remoção recuperável em lixeira; não apaga ROMs, saves, mídias ou arquivos Drive.
- Página individual com artes, descrição, diário, marcos pessoais, referências de captura/vídeo, sessões e versões de arquivos.
- Diário de texto, timeline de memórias, imagens ampliadas e vídeo no programa padrão.
- Wishlist local com metas BRL, alteração e remoção. Sem preços de demonstração.
- Estatísticas do banco: status, plataformas/gêneros, totais/média, ranking e tempo semanal/mensal por sessões confirmadas, conclusões por mês.
- Executável local direto, perfis de emulador com argumentos JSON, plataforma/extensões, execução de ROM local e registro manual explícito de sessão emulada.
- Recuperação de sessões interrompidas com duração confirmada pelo usuário. Não infere horas após encerramento inesperado.
- Backups locais manuais e pós-sessão de saves por jogo selecionados por padrões, manifesto e SHA-256; restauração com validação e cópia anterior.

## Clientes implementados, ainda sem validação com contas reais

- RAWG: pesquisa, escolha explícita, detalhes e importação com identificador externo.
- SteamGridDB: escolha de jogo e arte, download para cache e confirmação visual; autenticação por chave no cofre.
- Google Drive: OAuth Desktop readonly, raiz por ID, BFS recursivo paginado, metadados/MD5, cursor de alterações, associação manual de versões e download por ID com verificação. ROM instalada permanece no disco. Cliente não tem função de excluir remoto.
- DAT Logiqx: catálogo local e candidatos exatos MD5/tamanho/plataforma. Nomes normalizados não provocam associação automática.

Credenciais necessárias: OAuth Google Cloud Desktop JSON e consentimento; chaves RAWG e SteamGridDB. Nada foi incluído no Git. Windows Credential Manager é o único backend de segredos. A UI não apresenta credencial existente como conexão verificada.

## Validação já executada

- 23 testes automatizados passaram na execução final: domínio, SQLite/migração, saves/ZIP, clientes com respostas controladas, DAT, subprocesso real e UI headless.
- Smoke pelo código fonte abriu as seis páginas e retornou integridade SQLite `ok`.
- Captura headless do início vazio foi inspecionada visualmente; tema/estado vazio legíveis.
- Executável PyInstaller x64 recompilado a partir do código final: smoke headless com saída 0, seis páginas abertas, schema 2, integridade SQLite `ok`, 0 jogos iniciais e log sem erros.
- A pasta portátil completa tem aproximadamente 249 MB antes de compactação. O pacote não depende do Python instalado para esse smoke; a validação foi feita no próprio host Windows do Codex, não em uma máquina limpa.
- Código versionado em repositório Git local próprio, sem remote configurado. Os arquivos ZIP de entrega e checksums ficam em outputs, fora do repositório de fontes.

## Pendências principais

1. Validar integrações reais e scanner em coleção grande; progresso/cancelamento, 410, shared drives, ordem complexa de alterações e retomada de downloads.
2. Saves por jogo/emulador com perfis tradicionais validados, backup automático pós-sessão e sincronização/versionamento/conflitos no Drive. Backup local por jogo já possui disparo opcional ao término do registro de sessão; envio ao Drive continua pendente.
3. Steam: biblioteca, privacidade, horas e conquistas oficiais; RetroAchievements real; IGDB.
4. Preços automáticos regionais, histórico, menor preço, scheduler, limites e alertas. Atualmente só wishlist e meta local.
5. Launchers externos, processos filhos, detecção específica de encerramento de ROM e suspensão/pausa.
6. Editores completos de diário, anexos por entrada, galeria visual, conquistas e progresso estruturados.
7. Entidades normalizadas para plataformas/gêneros/categorias, repositórios dedicados e virtualização/paginação.
8. Assinatura, instalador/atualizador, licenças de terceiros e testes limpos Windows 10/11.

## Problemas/limitações conhecidos

- Nenhum perfil de emulador/save real foi validado. Lista de extensões de save state bloqueadas não é universal; padrões devem selecionar somente saves tradicionais.
- Backup local e alguns cálculos/leitura de listas são síncronos; podem travar a UI temporariamente em coleções grandes. Varredura/rede usa workers.
- Restauração é atômica por arquivo, não por conjunto; versão anterior é preservada para recuperação manual.
- Sessão por processo direto pode terminar cedo quando um launcher abre outro processo. Emuladores usam término manual. Sem detecção de inatividade/standby.
- Artes manuais e mídia são caminhos referenciados; mover o original quebra o vínculo. Artes baixadas são cacheadas.
- Recorte de arte é central sem deformação, sem detecção automática de assunto. Lista de artes não tem miniaturas, mas possui confirmação visual após download.
- Plataformas/gêneros/categorias usam texto; sem gerenciamento dedicado/associações múltiplas normalizadas.
- Estatísticas de calendário usam UTC; evolução de conclusões reflete completed_at da entrada, não um log de todas as transições.
- Conjuntos de ROM com múltiplos arquivos (como CUE/BIN) não são agrupados nem preparados automaticamente. As dependências precisam ser organizadas manualmente; não considerar esse formato validado.
- Drive: sem seletor de pasta visual, sem remoção local pela UI, sem troca de raiz na mesma biblioteca, sem retomada HTTP persistente. Parciais ficam no disco para diagnóstico.
- Backup do banco não inclui mídia, ROMs nem segredos do cofre.
- Pacote não assinado; teste headless não equivale a homologação completa em Windows limpo.

## Próxima tarefa recomendada

Revisar evidências e manter os testes verdes. Depois validar OAuth/RAWG/SteamGridDB em diretório de dados isolado com credenciais autorizadas. A próxima implementação prioritária é o ciclo de saves tradicionais configurado por jogo, com workers, perfis validados e autorização Drive separada de escrita. O ROADMAP.md preserva todo o escopo solicitado.

## Atualização 0.1.1 — Checkpoint

Nome visível e executável alterados para Checkpoint. Removidos slogans da navegação, do início e dos estados vazios. Os dados, a trava de instância e o cofre continuam usando os identificadores internos GameVault para abrir a biblioteca existente sem migração. O pacote Python e a pasta de fontes também permanecem com seus nomes internos. O usuário confirmou que os fluxos locais solicitados no teste anterior funcionaram; isso não valida integrações autenticadas.
Validação 0.1.1: 23 testes passaram. Executável Checkpoint.exe abriu as seis páginas em modo smoke, retornou saída 0 e preservou integralmente um cadastro em biblioteca legada isolada (%LOCALAPPDATA%/GameVault). Integridade SQLite ok. Início sem slogans inspecionado visualmente.

## Continuação — configuração de saves por jogo

Implementado no código: botão Configurar saves deste jogo, persistência de pasta/padrões específicos por jogo e rejeição de padrões abertos, caminhos relativos e formatos conhecidos de save state. 24 testes passaram. Esta alteração ainda não foi empacotada: o ZIP 0.1.1 continua sendo a última distribuição. Próximo trabalho: conectar os perfis ao backup em worker e ao término confirmado de sessões, com histórico por jogo. Backup automático e Drive continuam pendentes.


## Checkpoint 0.1.2 — saves por jogo

Implementados perfis de pasta/padrões por jogo, botão de backup manual na página individual, opção persistente de backup ao encerrar o registro da sessão, histórico por jogo e restauração para a pasta original do perfil. Operações por jogo rodam em worker com conexão SQLite própria; execução do jogo e fechamento do aplicativo são bloqueados durante a operação. A restauração preserva a versão local anterior em ZIP. Alterar o perfil não remove o histórico antigo.

O backup compara o conjunto de arquivos, tamanho, modificação e SHA-256 antes e após a cópia. Arquivos em alteração impedem a publicação do ZIP. O intervalo de estabilidade é de um segundo e não prova que um processo externo nunca mais escreverá: encerre o jogo antes de encerrar o registro. A opção automática começa desativada por jogo. Para executáveis monitorados, dispara ao sair o processo direto; launchers com processos filhos e detecção específica de ROM continuam pendentes. Não há varredura automática de saves nem reconhecimento universal de save states. Escolha padrões explícitos de saves tradicionais.

Configure o diretório de backups em Configurações; depois, na página do jogo, configure a pasta e os padrões (ex.: *.sav). O botão Fazer backup agora usa esse perfil. Ative a opção de backup ao encerrar a sessão se desejar. As versões aparecem abaixo e podem ser restauradas com confirmação. Não há envio ao Drive nesta versão.

Validação: 28 testes passaram (8,51 s), incluindo histórico preservado ao mudar perfil, restauração com cópia anterior, rejeição de backup de outro jogo, saves em alteração e encerramento de sessão disparando backup real em worker pela interface headless. Testes com emuladores reais e saves pessoais continuam pendentes. O backup manual antigo das Configurações continua síncrono; os novos fluxos por jogo usam workers.

Pacote 0.1.2 gerado. O executável passou pelo smoke com saída 0 e preservou a biblioteca legada isolada; SQLite íntegro. Evidência em evidence/checkpoint-012-validation.txt.

# Estado do projeto — Checkpoint

Atualizado em 10/11/2026. Versão 0.1.4 de desenvolvimento. **O projeto completo não está concluído.** O ponto de continuidade é este diretório, com código real, documentação e testes.

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

## Publicação no GitHub

Repositório privado criado e código/documentação/testes/scripts enviados pelo navegador autenticado: https://github.com/pedroalexcarneiro/Checkpoint

Release de desenvolvimento v0.1.2 publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.2
Commit remoto da tag: 474167e06c2d4211d3adb8c3c03f35840971d7ff. Os arquivos Windows, fonte, checksums e informações de build aparecem nos Assets. SHA-256 do ZIP Windows exibido pelo GitHub confere com o arquivo local: 576eb0211ecc628d5c2dcbcfcd2e9a1c6bd65b6837dfaf4e0344fd286714318a.

A publicação foi feita pela interface web, sem instalar GitHub Desktop nem obter tokens. O histórico remoto foi criado pela web e difere do histórico Git local: antes de um futuro push autenticado, reconciliar os históricos em checkout separado, sem force-push. Os marcadores .gitkeep adicionais do remoto apenas criam diretórios para upload. A tag publicada antecede esta anotação local de estado.

O aplicativo ainda não tem atualizador automático. Próxima tarefa para eliminar ZIPs manuais: implementar atualização pelo aplicativo com integridade e rollback; por ser um repositório privado, definir acesso seguro às releases sem embutir credenciais no executável.


## Checkpoint 0.1.3 — atualizações pelo aplicativo

Configurações > Atualizações do Checkpoint permite salvar uma credencial de leitura no Windows Credential Manager, consultar as 100 releases mais recentes do repositório pedroalexcarneiro/Checkpoint, baixar uma versão mais nova e aplicar/reiniciar. O repositório é privado: use um fine-grained personal access token restrito ao repositório Checkpoint, com Contents: Read-only. O login feito no navegador para publicar o código não autentica automaticamente o aplicativo. Nenhuma chave real foi criada, coletada ou incluída no código. A opção de incluir pré-releases vem marcada porque o projeto está em desenvolvimento.

O cliente usa a API oficial do GitHub. O pacote precisa ter SHA-256 fornecido na release e tamanho compatível. O token é enviado somente a api.github.com; o download redirecionado para CDN confiável ocorre sem o token. Erros de acesso/rede são apresentados sem URLs assinadas ou credenciais. Referência: https://docs.github.com/en/rest/releases/assets e https://docs.github.com/en/rest/releases/releases .

O ZIP é extraído em área separada após verificar integridade. São rejeitados caminhos externos, streams alternativos, nomes reservados, links, duplicatas e pacotes acima dos limites de tamanho. O processo auxiliar CheckpointUpdater.exe é copiado para fora da instalação, aguarda o Checkpoint fechar e preserva a instalação anterior numa pasta Checkpoint.previous-<id> ao lado da instalação. Falha de cópia provoca recuperação do nome original; cópias incompletas são preservadas para diagnóstico. O diretório de dados precisa ficar fora da instalação. Não há elevação administrativa, alteração de política PowerShell ou exclusão da biblioteca.

Antes de aplicar, encerre sessões e aguarde backups. A pasta portátil deve se chamar Checkpoint e ter permissão de escrita no seu diretório pai. A primeira adoção do atualizador exige usar o novo pacote 0.1.3, porque o 0.1.2 não contém o auxiliar. Atualizações posteriores poderão ser aplicadas pelos botões do aplicativo após configurar a credencial.

Limitações: não há consulta periódica, cancelamento de downloads, assinatura digital do executável nem detecção automática de falha tardia ao iniciar a nova versão. SHA-256 confirma correspondência ao arquivo da release, não substitui assinatura do fornecedor. Queda de energia entre a renomeação e a cópia pode exigir restaurar manualmente a pasta Checkpoint.previous-<id>. A atualização tem resultados em updates/<id>/install.result.json no diretório de dados; falha antes do reinício pode exigir reabrir a versão anterior manualmente. A origem não é atualizada por esses botões, apenas o pacote Windows empacotado.

Validação de domínio/rede controlada: 39 testes passaram em 5,74 s. Sem credencial de API real, consulta e download privados ainda não foram validados contra a conta GitHub. Testes com respostas controladas não equivalem a validação autenticada. O auxiliar one-dir recompilado foi executado fora da instalação: aguardou o processo de teste, aplicou a troca em uma pasta isolada e preservou a versão anterior. O executável principal retornou saída 0 e preservou a biblioteca legada isolada. O primeiro ensaio one-file falhou ao extrair uma DLL no temporário deste host e foi substituído por one-dir; esse arquivo com falha não integra a entrega.


Estado atual: Checkpoint 0.1.3 validado localmente com 39 testes e smoke dos dois executáveis. Consulta e download reais da API privada ainda dependem de uma credencial de leitura configurada pelo usuário. Publicação GitHub em andamento; a tag 0.1.2 continua disponível.

Publicação 0.1.3 concluída: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.3 . Tag aponta ao commit remoto f929fa206947fe709024f19989783b5960b0891e. Os quatro anexos estão disponíveis; SHA-256 exibido pelo GitHub para o ZIP Windows confere com o local: 80a2a552715e3b276dd98dcaf3d671eec777368021910df8541db9210fb264fe. Código e documentação sincronizados pela interface web antes da criação da tag. Esta anotação local é posterior à tag. Captura da release em outputs/github-checkpoint-013.png. Próximo passo de validação: configurar uma credencial restrita de leitura no aplicativo e testar a API privada; não foi criada credencial nem feito teste autenticado.


## Checkpoint 0.1.4 — correção da consulta de atualizações

Corrigida a leitura da lista de versões: o GitHub pode retornar gzip e o leitor anterior usava o corpo bruto sem descompactar. A falha foi reproduzida com resposta HTTP gzip controlada e na API pública github/docs sem credenciais; a consulta pública passou após usar iter_content com limite de 8 MB descompactados. Isso confirma o defeito do leitor, mas não prova que a mensagem de conexão do usuário tinha exatamente essa causa.

Agora erros de proxy, certificado HTTPS, timeout, conexão e JSON inválido têm mensagens distintas, sem exibir URLs ou segredos. Não foi desativada a validação TLS nem contornada a configuração de proxy. O teste público de rede no ambiente Codex exigiu permissão explícita de rede; sem ela o proxy restrito do ambiente recusava a conexão.

A interface exige salvar uma credencial digitada antes de consultar e informa quando não há credencial no cofre. O campo é limpo ao salvar com sucesso. Nenhum token real do usuário foi lido, copiado ou enviado por esta sessão. Consulta autenticada ao repositório privado continua pendente de validação no aplicativo pelo usuário.

Validação: 46 testes passaram em 5,77 s; incluem regressão com gzip real do urllib3/Requests, mensagens de erros de rede sem vazamento de segredos e bloqueio de consulta com token não salvo. Consulta pública real sem autenticação retornou com sucesso, sem atualizações compatíveis. O 0.1.3 pode precisar de substituição manual caso a consulta antiga impeça baixar esta correção.

Executável 0.1.4 validado após recompilação: smoke com saída 0, biblioteca legada isolada preservada e integridade SQLite ok. Auxiliar de atualização executado fora da instalação, com troca isolada e preservação da versão anterior. Arquivos serão publicados como v0.1.4; o acesso autenticado com a credencial real do usuário não foi testado por esta sessão.

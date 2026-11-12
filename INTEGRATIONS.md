# Integrações

## 0.1.17 — consulta após persistir o cadastro

A identificação automática agora acontece em segundo plano, após salvar, sem abrir
catálogo/carregamento modal obrigatório. Fonte indisponível ou falha do auxiliar
preserva o jogo já cadastrado. Atualização em lote é sequencial e pode parar após
o jogo atual. Nenhuma mudança em OAuth, chaves, escopos ou provedores.

## 0.1.16 — identificação automática e auxiliares

O cadastro tenta Steam (PC), RAWG e SteamGridDB já configurados; compara nome e
plataforma, recusando empates e baixa semelhança. RAWG e SteamGridDB só compartilham
identidades quando retornam o mesmo título. Não há pedido de chave por jogo nem
escopo OAuth novo. Sem correspondência, o cadastro manual continua funcionando.
A preferência global de automação é respeitada; uma tentativa manual em lote pode
ser forçada. Ficha/imagens dependem da disponibilidade nas fontes.

Download Drive e enriquecimento rodam em processos auxiliares, com banco próprio,
sem transportar credenciais na linha de comando ou IPC. Um encerramento abrupto
é reportado sem encerrar a interface; native-crash.log recebe stack nativo do
auxiliar sem variáveis locais. Arquivos parciais ficam preservados, e somente
transferências verificadas são disponibilizadas. Testes usam transporte controlado;
Google Drive autenticado não foi acessado nesta correção.

## 0.1.15 — ficha e imagens no cadastro (desenvolvimento)

Steam inicia preenchimento assíncrono por AppID após importar. Cadastro manual e
ROM abrem identificação no catálogo ao salvar; a opção vem marcada e pode ser
desativada para cadastrar offline. Campos e artes existentes são preservados pelo
preenchimento automático. Status, categoria, nota e observações são pessoais.
Configurações oferece completar a biblioteca já identificada, com progresso e
interrupção após o jogo atual. Editar jogo permite identificar cadastros antigos.

Steam fornece ficha pública e imagens disponíveis sem chave adicional da loja.
RAWG exige chave própria para ficha e imagem de fundo como capa/banner; SteamGridDB
fornece identidade e artes, sem ficha detalhada. Logo/capa vertical dependem da fonte.
Não há associação automática por nome nem alteração de original_name da ROM.
Schema permanece 4; versão 0.1.15 somente no código, sem build Windows/publicação.
A release v0.1.14 existente foi preservada.

Validação Linux desta mudança: suíte completa **146 aprovados em 14,99 s, exit 0**;
52 testes focados passaram anteriormente em 3,10 s. Smoke em diretório novo:
seis páginas, exit 0, SQLite integrity=ok, schema 4, zero jogos.
Probes à loja Steam e CDN foram bloqueados pelo proxy (CONNECT HTTP 403);
contratos testados com respostas controladas, sem validar download real, Windows
ou autenticação. Nenhuma credencial foi lida ou exposta pela sessão.

Rede necessária para Steam: store.steampowered.com,
cdn.akamai.steamstatic.com, shared.akamai.steamstatic.com,
shared.fastly.steamstatic.com e cdn.cloudflare.steamstatic.com.
RAWG/SteamGridDB mantêm seus endpoints e chaves configuradas no cofre Windows.
Falha de consulta preserva o cadastro e permite tentar novamente.

Pesquisa documental em 10/11/2026. Implementação de cliente não equivale a validação de conta real. Nenhuma credencial foi inventada ou incluída no repositório.

## Google Drive — implementado, autenticação real pendente

Ative a Drive API em um projeto Google Cloud, configure a tela de consentimento e crie um OAuth Client do tipo Desktop. Em modo de teste, autorize a conta desejada. Em Configurações > Google Drive, escolha o JSON de cliente e autentique. O aplicativo abre o fluxo no navegador do ambiente de execução; não depende do computador pessoal do usuário. Sem credenciais disponíveis, não foi iniciado fluxo real nesta sessão.

Escopo de ROMs: `https://www.googleapis.com/auth/drive.readonly`. Ele permite examinar uma coleção existente; `drive.file` sozinho não dá acesso geral às pastas já existentes. A publicação pode exigir verificação Google conforme escopos e uso. Tokens ficam no Windows Credential Manager e são renovados pelo cliente oficial.

Cole o ID da pasta principal, faça a varredura inicial e depois use Atualizar alterações. A captura do cursor ocorre antes da varredura, conforme [API de alterações](https://developers.google.com/workspace/drive/api/guides/manage-changes). Paginação e alterações são persistidas localmente. O escopo e o cliente de ROMs não implementam escrita ou exclusão. Upload de backups deverá usar autorização separada e escopo mínimo `drive.file`; ainda não está implementado.

Os arquivos são identificados pelo Drive ID. Nome original, plataforma, caminho, tamanho, modificação e MD5 quando fornecido são preservados. Arquivos compactados não são inspecionados remotamente. Plataforma desconhecida permanece para revisão. DATs Logiqx podem gerar candidatos exatos por MD5 + tamanho + plataforma, mas não criam jogos nem vínculos automaticamente. Não há download para identificação.

Limitações: raiz por ID sem navegador de pastas, sem suporte testado a shared drives/atalhos, sem cancelamento/progresso ou retomada persistente do download, sem tratamento automático de cursor expirado 410. Falha preserva o cursor anterior ou a última página aplicada; repita a operação ou faça nova varredura completa. Downloads incompletos ficam como `.partial` e nunca são marcados disponíveis. O próximo download reinicia em novo parcial, sem substituir uma ROM instalada.

## RAWG — implementado, credencial real pendente

Obtenha uma chave própria em [RAWG API](https://rawg.io/apidocs). Configure a chave pelo campo protegido em Configurações. Pesquisar metadados apresenta resultados para escolha explícita, consulta detalhes e importa título, descrição, lançamento, gêneros e origem. A plataforma pessoal é confirmada no diálogo. O identificador externo impede importação duplicada. Artes são selecionadas separadamente.

Revisar termos, limites e atribuição da RAWG antes de distribuição/uso comercial. Sem chave, a biblioteca manual funciona normalmente. Testes usam respostas controladas, sem alegar acesso real.

## SteamGridDB — implementado, credencial real pendente

Obtenha API key própria, salve em Configurações e use Selecionar artes no jogo. Escolha o jogo correto e o tipo de arte. O aplicativo lista arquivos e baixa o escolhido para pré-visualização; só aplica após confirmação. O filtro de capas prioriza dimensões verticais; a galeria final recorta para 3:4. Não há garantia de que toda arte seja oficial: revisar a imagem e os direitos de uso. [Referência API v2](https://www.steamgriddb.com/api/v2).

## IGDB — avaliado, ainda não implementado

[IGDB](https://api-docs.igdb.com/) utiliza credenciais Twitch e OAuth Client Credentials. Requer client ID/secret e tratamento de expiração. Para uma distribuição desktop pública, não embutir segredo compartilhado no executável: considerar serviço intermediário ou credenciais próprias do usuário. O contrato MetadataProvider já permite acrescentar o cliente.

## Steam — implementado no código 0.1.14; autenticação real pendente

A [Steam Web API](https://partner.steamgames.com/doc/webapi/IPlayerService) é consultada por HTTPS em `api.steampowered.com`: GetOwnedGames v0001 para biblioteca/horas e GetPlayerAchievements v0001 para conquistas por jogo. Operações somente leitura.

1. Obtenha uma chave pessoal em https://steamcommunity.com/dev/apikey conforme requisitos da Steam. Não envie senha, código Steam Guard ou chave no chat.
2. Abra Configurações > Steam > Configurar chave Steam. A chave fica exclusivamente no cofre Windows com nome interno `steam`.
3. Informe o SteamID64 de 17 dígitos. Não é apelido, AppID nem URL personalizada. Esse identificador não secreto pode ficar nas configurações locais.
4. Consulte a biblioteca. O acesso depende de Detalhes dos jogos e regras da API. Resposta indisponível não é tratada como biblioteca vazia; horas ocultas aparecem como não disponíveis.
5. Marque os jogos. Para aproveitar cadastro manual, selecione a linha e use Associar linha a cadastro existente. Sem escolha explícita, nomes iguais continuam cadastros distintos.
6. Importe os marcados. Repetir atualiza o snapshot por AppID/conta sem duplicar o jogo nem substituir título pessoal, notas, artes ou status. Lixeira exige restauração; nenhum jogo local é removido por desaparecer da consulta.
7. Selecione um jogo importado e clique Atualizar conquistas da linha. A consulta é somente desse jogo. Falha preserva o snapshot anterior. Horas, conquistas e datas de consulta aparecem na página do jogo.

Horas de contas diferentes não são somadas e não entram nas estatísticas de sessões locais. Conquistas Steam preservam API name e desbloqueio, separadas dos marcos pessoais. Data desconhecida é distinta de conquista bloqueada.

Não implementa login Steam, execução por URI, artes automáticas, sincronização em segundo plano ou inventário. Use os fluxos existentes para configurar executável e selecionar artes. Testes com transporte controlado não validam conta real; validação Steam autenticada e Windows continua pendente.

## RetroAchievements — avaliado, ainda não implementado

A [API RetroAchievements](https://api-docs.retroachievements.org/v1/get-user-summary.html) requer credencial própria e identificação do usuário. Compatibilidade varia por jogo, hash e emulador; consultar progresso não implementa o sistema de runtime do emulador. Apenas conquistas pessoais funcionam nesta entrega.

## Preços — avaliação e pendências

A [API IsThereAnyDeal](https://docs.isthereanydeal.com/) é a opção inicial a investigar: oferece consulta por país e provedores agregados. É necessário validar credenciais, contrato, lojas efetivamente cobertas no Brasil e moeda retornada. A documentação retornou 403 na leitura direta nesta sessão; não foi implementado um cliente com suposições sobre o payload.

Steam, Epic, Nuuvem e GOG não foram conectadas por endpoints não documentados. Não foi identificada e validada nesta sessão uma API pública apropriada de GG.deals. Não é correto afirmar que todas as lojas têm ou não têm API; a cobertura continuará sendo avaliada por provedor e termos. Nenhum scraping foi implementado.

A lista de desejos e metas BRL são locais. Monitoramento periódico, histórico de preços, promoções, links e notificações ainda não estão disponíveis. O banco possui PriceHistory para essa evolução. Não há valores fictícios ou preços gerados.

## Cofre e logs

Segredos usam exclusivamente o backend Windows Credential Manager. SQLite guarda somente configurações não sensíveis. Não há exportação de tokens, sincronização de segredos ou fallback para texto. As integrações mostram a existência de credencial salva como conexão não verificada, nunca como confirmação de acesso. Erros de jobs omitem respostas OAuth e URLs com chaves.


## Checkpoint 0.1.3 — atualizações pelo aplicativo

Configurações > Atualizações do Checkpoint permite salvar uma credencial de leitura no Windows Credential Manager, consultar as 100 releases mais recentes do repositório pedroalexcarneiro/Checkpoint, baixar uma versão mais nova e aplicar/reiniciar. O repositório é privado: use um fine-grained personal access token restrito ao repositório Checkpoint, com Contents: Read-only. O login feito no navegador para publicar o código não autentica automaticamente o aplicativo. Nenhuma chave real foi criada, coletada ou incluída no código. A opção de incluir pré-releases vem marcada porque o projeto está em desenvolvimento.

O cliente usa a API oficial do GitHub. O pacote precisa ter SHA-256 fornecido na release e tamanho compatível. O token é enviado somente a api.github.com; o download redirecionado para CDN confiável ocorre sem o token. Erros de acesso/rede são apresentados sem URLs assinadas ou credenciais. Referência: https://docs.github.com/en/rest/releases/assets e https://docs.github.com/en/rest/releases/releases .

O ZIP é extraído em área separada após verificar integridade. São rejeitados caminhos externos, streams alternativos, nomes reservados, links, duplicatas e pacotes acima dos limites de tamanho. O processo auxiliar CheckpointUpdater.exe é copiado para fora da instalação, aguarda o Checkpoint fechar e preserva a instalação anterior numa pasta Checkpoint.previous-<id> ao lado da instalação. Falha de cópia provoca recuperação do nome original; cópias incompletas são preservadas para diagnóstico. O diretório de dados precisa ficar fora da instalação. Não há elevação administrativa, alteração de política PowerShell ou exclusão da biblioteca.

Antes de aplicar, encerre sessões e aguarde backups. A pasta portátil deve se chamar Checkpoint e ter permissão de escrita no seu diretório pai. A primeira adoção do atualizador exige usar o novo pacote 0.1.3, porque o 0.1.2 não contém o auxiliar. Atualizações posteriores poderão ser aplicadas pelos botões do aplicativo após configurar a credencial.

Limitações: não há consulta periódica, cancelamento de downloads, assinatura digital do executável nem detecção automática de falha tardia ao iniciar a nova versão. SHA-256 confirma correspondência ao arquivo da release, não substitui assinatura do fornecedor. Queda de energia entre a renomeação e a cópia pode exigir restaurar manualmente a pasta Checkpoint.previous-<id>. A atualização tem resultados em updates/<id>/install.result.json no diretório de dados; falha antes do reinício pode exigir reabrir a versão anterior manualmente. A origem não é atualizada por esses botões, apenas o pacote Windows empacotado.

Validação de domínio/rede controlada: 39 testes passaram em 5,74 s. Sem credencial de API real, consulta e download privados ainda não foram validados contra a conta GitHub. Testes com respostas controladas não equivalem a validação autenticada. O auxiliar one-dir recompilado foi executado fora da instalação: aguardou o processo de teste, aplicou a troca em uma pasta isolada e preservou a versão anterior. O executável principal retornou saída 0 e preservou a biblioteca legada isolada. O primeiro ensaio one-file falhou ao extrair uma DLL no temporário deste host e foi substituído por one-dir; esse arquivo com falha não integra a entrega.


## 0.1.7 — diagnóstico de rede Drive (11/11/2026)

- Classificação segura da cadeia de exceções: proxy, TLS, DNS, timeout, conexão recusada/interrompida e causa não informada. Não imprime mensagens, URLs privadas ou tokens.
- Botão Testar conexão faz GET HTTPS ao endpoint público de token sem código OAuth, JSON ou token; uma resposta HTTP não prova autenticação nem sucesso de POST OAuth.
- Troca inicial do código por token tem timeout de conexão 10 s e leitura 30 s; não repete automaticamente um código de uso único.
- Mantém verificação HTTPS e configurações de proxy do ambiente. Não desativa firewall nem altera certificados.
- 73 testes automatizados passaram. Teste público no ambiente de execução resultou em categoria proxy; o ambiente do aplicativo instalado pode usar configuração diferente. OAuth real segue pendente, sem afirmar correção da causa original.


### Correção confirmada do pacote TLS — 0.1.8
O runtime Python do ambiente modifica SSLContext.__new__ para carregar codex-rejected-cas.pem. O empacotamento anterior omitia esse dado, causando ConnectionError > ProtocolError > FileNotFoundError(errno=2) em ssl.py:440. O build agora inclui o arquivo do próprio runtime, quando presente, em _internal. Não altera a política TLS nem desativa verificação. No executável local, incluir o arquivo mudou a falha reproduzida para resposta HTTPS HTTP 404 do endpoint público de token. Autenticação real com conta do usuário continua pendente. A versão corrige uma causa concreta de falha do transporte; outras restrições de rede podem existir.


## 0.1.10 — pastas personalizadas e capas (11/11/2026)
- Aliases PS1/PSX, PS2, PS3, GameCube/NGC, Wii, N64, NES, Game Boy/Color, Mega Drive, Saturn e Dreamcast.
- Pastas e plataformas: associação por ID de pasta indexada, plataforma livre ou conhecida, herança por subpastas e prioridade da regra mais específica. Salvar/remover reclassifica o ramo existente, sem alterar jogos associados, nomes ou arquivos. Atualize o Drive para descobrir pastas novas; pastas vazias sem regra reconhecível permanecem para revisão. Regras persistem no SQLite; não são credenciais.
- Criar jogo desta ROM exige título confirmado e vincula a versão; outras versões podem ser associadas ao jogo existente. Não cria milhares de jogos nem mescla títulos automaticamente.
- Capa do jogo acessível pela lista Drive após associação; imagem local é validada e copiada ao cache sem chave. Busca SteamGridDB exige chave própria e confirmação do jogo/arte. Lista da biblioteca agora exibe miniaturas; lista Drive mostra capas de jogos associados.
- Scanner não fornece capas nem identifica títulos sozinho. Não houve download ou atribuição automática de artes na coleção real. Não foi necessário alterar credenciais.
- 97 testes passaram antes do ajuste final de atualização da galeria após fechar Drive; testes cobrem herança, regra específica, persistência, renomeação por ID, limites de ramo, validação, criação de jogo sem duplicar arquivo e ícone de capa na tabela.


## 0.1.12 — artes por identidade confirmada (11/11/2026)
Fonte principal: SteamGridDB API v2 (https://www.steamgriddb.com/api/v2), categorias grids/capa, heroes/banner e logos. O provedor fornece artes da comunidade; não há garantia de que todas sejam oficiais. A biblioteca continua recortando capas para 3:4 sem deformar o original.
- Confirmar jogo selecionado persiste o ID do SteamGridDB e obtém capa/banner/logo faltantes; nomes de ROM não são associados automaticamente por suposição. AppID Steam pode ser resolvido pelo provedor e confirmado na interface, sem busca textual. Isso não implementa importação de conta Steam.
- AutoArtwork executa após criar/associar jogo a ROM e após download no gerenciador Drive, se houver identidade confirmada e chave configurada. Sem identidade ou chave, mostra pendência; não desfaz cadastro nem download. Não é preciso baixar a ROM para obter arte.
- Artes existentes preservadas; atualização condicional impede substituir escolha feita durante consulta. Cache validado por imagem e SHA-256; migração 3 adiciona artwork_assets com tipo, ID externo, URL, caminho e data da última arte obtida automaticamente. Esse registro descreve o download, não garante que a arte ainda seja a escolha atual após edição manual.
- Até três alternativas estáticas por tipo, excluindo conteúdo marcado NSFW/humor. Ordem por pontuação do provedor. Consulta automática tem intervalo mínimo de uma hora por jogo; botão Obter artes faltantes permite nova tentativa. Preferência pode desativar automação.
- Banco anterior é copiado consistentemente para backups antes de migrar; migração transacional. Não atualizar banco real com a versão antiga aberta.
- Validação: 111 testes passaram (pytest result 0), com provedores/transferências substituídos em testes. Tela renderizada e inspecionada. Consulta real SteamGridDB e artes reais NÃO validadas: não há chave configurada no cofre desta sessão. Nenhuma arte foi atribuída à coleção real nesta implementação.
- Configurar chave em Configurações > Configurar chave SteamGridDB (não compartilhar chave no chat nem versionar). Em um jogo: Selecionar artes > Pesquisar > selecionar resultado > Confirmar jogo selecionado e obter capa, banner e logo. Para Steam: Identificar pelo AppID Steam > confirmar resultado. Downloads/associações futuros reutilizam o ID salvo.
Referência primária do provedor: https://github.com/SteamGridDB/java-steamgriddb . Os termos do serviço e as licenças dos autores continuam aplicáveis às imagens.


## 0.1.13 — cadastro pelo Drive, títulos e enquadramento (11/11/2026)
- Adicionar jogo contém pesquisa local nas ROMs indexadas (nome/pasta), seleção da versão e preenchimento de nome sugerido, plataforma e origem. Atualizar índice abre o gerenciador diretamente; não é necessário passar por Configurações. O cadastro manual permanece disponível.
- Confirmar título original e completar dados abre escolha explícita no catálogo: SteamGridDB fornece título/identidade/artes com a chave já existente; RAWG fornece ficha detalhada com chave própria. Nome/plataforma vêm do Drive; gênero, descrição, desenvolvedora, publicadora e lançamento somente são preenchidos quando retornados pela fonte escolhida. Não há associação automática por semelhança.
- Salvar usa transação única para jogo, identidade e versão da ROM. Identidade já cadastrada reutiliza o jogo, preservando notas, status e capas; vínculos conflitantes/lixeira exigem revisão. Metadados confirmados podem padronizar o título exibido; original_name nunca é alterado. Artes são obtidas em worker com banco próprio após salvar, sem baixar ROM.
- Criar jogo desta ROM no gerenciador usa o mesmo formulário. Ao confirmar identidade pelo seletor de artes, o título do catálogo também passa a ser usado.
- Galeria e página individual agora mostram capa/banner inteiros, centralizados em quadros fixos, com preenchimento discreto. Não há recorte de logos/texto/personagens nem deformação. Fonte de imagem e cache originais preservados.
- Validação: 120 testes passaram com pytest result 0. Incluem preservação das bordas da arte, título canônico separado do arquivo, preenchimento, troca de ROM limpando metadados antigos, reutilização de versão, rollback sem órfãos e fechamento do progresso/catálogo. Telas renderizadas e inspecionadas em cópia local do banco.
- Busca real SteamGridDB por Zelda - the Minish Cap retornou The Legend of Zelda: The Minish Cap entre as opções. Quatro títulos reais foram padronizados pelos IDs SteamGridDB previamente confirmados, após backup consistente; IDs, original_name, vínculos e integridade do banco verificados. Nenhuma ROM ou arte foi baixada nessa padronização.
- RAWG continua sem validação autenticada nesta sessão; não promete ficha completa usando somente a chave SteamGridDB. Verificar em Windows: novo cadastro pelo Drive, escolha da edição correta, obtenção automática de artes e navegação após salvar.

Validação autenticada adicional 0.1.13, em biblioteca isolada: ID SteamGridDB já confirmado para The Legend of Zelda: The Minish Cap; formulário preenchido com ROM de teste, título do catálogo aplicado, cadastro/identidade/versão salvos e ArtworkProgress concluído. API real retornou e cacheou cover, banner e logo (3 sucessos, zero falhas). Nome original preservado e integrity_check ok. Não adicionou jogo/ROM à coleção real. RAWG real continua pendente.

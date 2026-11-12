# Validação

## 0.1.14 — encerramento Qt corrigido

Reprodução original: test_add_form_drive_search_and_metadata_prefill passava na
asserção e o processo saía com SIGSEGV/139. Conexões dos seletores de arquivo foram
trocadas de lambdas que capturavam o diálogo para método do receptor Qt.

Validação por etapas: teste original exit 0; 16 testes de formulário/UI exit 0;
uma execução completa (necessária para confirmar o shutdown global) terminou com
**136 aprovados em 9,62 s, exit 0**. Smoke: seis páginas, SQLite integrity=ok.
Comando completo, com QT_QPA_PLATFORM=offscreen e XDG_CACHE_HOME=$PWD/.venv/cache:

```sh
.venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

Somente duas regressões novas: destino correto dos quatro botões de arquivo e
subprocesso que abre/fecha formulários sem pai, verificando seu retorno real.
Não foram desabilitadas asserções, encerrado o processo à força nem alteradas
dependências. Para mudanças futuras, executar por impacto; não repetir a suíte
completa sem novo motivo. Detalhes em evidence/cloud-qt-shutdown.txt.

## 0.1.14 — validação focada na nuvem

Com `QT_QPA_PLATFORM=offscreen` e `XDG_CACHE_HOME=$PWD/.venv/cache`, execute:

```sh
.venv/bin/python -m pytest tests/test_steam.py tests/test_migrations.py tests/test_library.py tests/test_ui.py -q -p no:cacheprovider
```

Resultado nesta implementação: 29 aprovados, exit 0. Cobertura nova: privacidade e
respostas inválidas da API, horas ocultas, seleção explícita, associação por AppID,
reimportação, rollback de conflitos/lixeira, contas separadas, conquistas, backup
v3→v4 e fluxo Qt assíncrono com SQLite real. API/cofre substituídos nos testes;
não representam validação Steam autenticada nem Windows.

Reaproveitados os testes existentes de migrações, biblioteca e UI afetados. Não
criados ou repetidos testes de saves, scanner Drive ou temas intactos. A suíte
histórica tinha falha nativa no encerramento do teste de formulário Drive, resolvida
na etapa posterior acima. A execução focada de Steam isoladamente não validava
o encerramento da suíte completa.

## Ambiente efetivamente usado

Windows 10 build 19045 do ambiente Codex (identificado pelo PyInstaller), Python 3.12.14 x64, PySide6 6.8.3, pytest 9.2.0. Não foi necessário usar o computador pessoal do usuário. Versões instaladas estão em requirements-tested.txt.

## Executar testes

```powershell
python -m pytest tests -q -p no:cacheprovider
python -m gamevault.app --smoke-test --data-dir ./dados-smoke
```

A suíte cria bancos e arquivos isolados. Por padrão usa `.test-data` abaixo do diretório atual; `GAMEVAULT_TEST_ROOT` permite escolher uma área temporária. O fixture verifica o destino antes de remover sua própria pasta UUID. Não usa a biblioteca real do usuário nem serviços autenticados.

## Cobertura de comportamento

- CRUD, filtros, busca literal, validação de status/notas e SQL parametrizado.
- Reabertura do SQLite, chaves estrangeiras, migração v1→v2 preservando dados e recusa de esquema futuro.
- Lixeira e restauração, diário e configurações, exclusão de sessões interrompidas das estatísticas.
- Backup SQLite íntegro e fechamento de conexão no Windows.
- Saves tradicionais explicitamente selecionados, exclusão de formatos conhecidos de states, SHA-256, restauração e preservação da versão anterior.
- Rejeição de caminho malicioso dentro de ZIP e padrões totalmente abertos.
- Drive controlado: scanner sem downloads, upsert idempotente, associação de versão, cursor, falha inicial, download com MD5, remoção/missing remota preservando cópia local.
- DAT: hash/plataforma/tamanho exatos, importação idempotente e rejeição de entidades XML.
- Metadados com resposta controlada e lista de resultados para escolha.
- Montagem de argumentos sem shell, subprocesso real Python e monitoramento direto.
- Emulador encerrado sem inferir automaticamente o fim da ROM; sessão manual.
- UI headless: seis páginas, filtros/galeria/lista, detalhes, formulário e renderização.
- Cache: imagem válida, deduplicação, rejeição de conteúdo inválido e URL não autorizada.

O modo smoke verifica as seis áreas e `PRAGMA integrity_check`, e salva uma captura do início vazio. Testes headless validam construção e fluxos exercitados; não substituem uso humano em monitor real.

## Evidência da sessão

Resultado final: **23 testes passaram**, em 1,89 segundos. Smoke do fonte: seis páginas e integridade ok. Smoke do executável recompilado: saída 0, schema 2, integridade ok e biblioteca vazia. Evidência detalhada em PROJECT_STATUS.md. Dois problemas reais de handles Windows foram detectados e corrigidos: conexão SQLite de backup sem close explícito e QImageReader mantendo arquivo temporário aberto. O cache passou a decodificar por buffer de memória.

## Ainda não validado

OAuth real, tokens/revogação do cofre, RAWG/SteamGridDB reais, grandes coleções Drive, mudança de raiz, shared drives, 410, cancelamento, reconexão em cada etapa, cotas reais, download multi-GB e integridade pós-falha de energia. Validar separadamente quando credenciais estiverem disponíveis.

Jogos/emuladores reais, Steam/Epic, processos filhos e sessão de ROM real não foram usados. Não há emulador validado para saves tradicionais nem garantia de reconhecimento universal de save states. Steam, RetroAchievements, preços e backup remoto não são funcionalidades implementadas nesta entrega.

Ainda necessários: instalações limpas Windows 10 e 11, inicialização sem Python, DPI 100/125/150/200%, teclado/leitor de tela, codecs de vídeo, Unicode de caminhos, antivírus, disco cheio, interrupção de restauração, teste de carga e distribuição assinada.


## Checkpoint 0.1.2 — saves por jogo

Implementados perfis de pasta/padrões por jogo, botão de backup manual na página individual, opção persistente de backup ao encerrar o registro da sessão, histórico por jogo e restauração para a pasta original do perfil. Operações por jogo rodam em worker com conexão SQLite própria; execução do jogo e fechamento do aplicativo são bloqueados durante a operação. A restauração preserva a versão local anterior em ZIP. Alterar o perfil não remove o histórico antigo.

O backup compara o conjunto de arquivos, tamanho, modificação e SHA-256 antes e após a cópia. Arquivos em alteração impedem a publicação do ZIP. O intervalo de estabilidade é de um segundo e não prova que um processo externo nunca mais escreverá: encerre o jogo antes de encerrar o registro. A opção automática começa desativada por jogo. Para executáveis monitorados, dispara ao sair o processo direto; launchers com processos filhos e detecção específica de ROM continuam pendentes. Não há varredura automática de saves nem reconhecimento universal de save states. Escolha padrões explícitos de saves tradicionais.

Configure o diretório de backups em Configurações; depois, na página do jogo, configure a pasta e os padrões (ex.: *.sav). O botão Fazer backup agora usa esse perfil. Ative a opção de backup ao encerrar a sessão se desejar. As versões aparecem abaixo e podem ser restauradas com confirmação. Não há envio ao Drive nesta versão.

Validação: 28 testes passaram (8,51 s), incluindo histórico preservado ao mudar perfil, restauração com cópia anterior, rejeição de backup de outro jogo, saves em alteração e encerramento de sessão disparando backup real em worker pela interface headless. Testes com emuladores reais e saves pessoais continuam pendentes. O backup manual antigo das Configurações continua síncrono; os novos fluxos por jogo usam workers.


## Checkpoint 0.1.3 — atualizações pelo aplicativo

Configurações > Atualizações do Checkpoint permite salvar uma credencial de leitura no Windows Credential Manager, consultar as 100 releases mais recentes do repositório pedroalexcarneiro/Checkpoint, baixar uma versão mais nova e aplicar/reiniciar. O repositório é privado: use um fine-grained personal access token restrito ao repositório Checkpoint, com Contents: Read-only. O login feito no navegador para publicar o código não autentica automaticamente o aplicativo. Nenhuma chave real foi criada, coletada ou incluída no código. A opção de incluir pré-releases vem marcada porque o projeto está em desenvolvimento.

O cliente usa a API oficial do GitHub. O pacote precisa ter SHA-256 fornecido na release e tamanho compatível. O token é enviado somente a api.github.com; o download redirecionado para CDN confiável ocorre sem o token. Erros de acesso/rede são apresentados sem URLs assinadas ou credenciais. Referência: https://docs.github.com/en/rest/releases/assets e https://docs.github.com/en/rest/releases/releases .

O ZIP é extraído em área separada após verificar integridade. São rejeitados caminhos externos, streams alternativos, nomes reservados, links, duplicatas e pacotes acima dos limites de tamanho. O processo auxiliar CheckpointUpdater.exe é copiado para fora da instalação, aguarda o Checkpoint fechar e preserva a instalação anterior numa pasta Checkpoint.previous-<id> ao lado da instalação. Falha de cópia provoca recuperação do nome original; cópias incompletas são preservadas para diagnóstico. O diretório de dados precisa ficar fora da instalação. Não há elevação administrativa, alteração de política PowerShell ou exclusão da biblioteca.

Antes de aplicar, encerre sessões e aguarde backups. A pasta portátil deve se chamar Checkpoint e ter permissão de escrita no seu diretório pai. A primeira adoção do atualizador exige usar o novo pacote 0.1.3, porque o 0.1.2 não contém o auxiliar. Atualizações posteriores poderão ser aplicadas pelos botões do aplicativo após configurar a credencial.

Limitações: não há consulta periódica, cancelamento de downloads, assinatura digital do executável nem detecção automática de falha tardia ao iniciar a nova versão. SHA-256 confirma correspondência ao arquivo da release, não substitui assinatura do fornecedor. Queda de energia entre a renomeação e a cópia pode exigir restaurar manualmente a pasta Checkpoint.previous-<id>. A atualização tem resultados em updates/<id>/install.result.json no diretório de dados; falha antes do reinício pode exigir reabrir a versão anterior manualmente. A origem não é atualizada por esses botões, apenas o pacote Windows empacotado.

Validação de domínio/rede controlada: 39 testes passaram em 5,74 s. Sem credencial de API real, consulta e download privados ainda não foram validados contra a conta GitHub. Testes com respostas controladas não equivalem a validação autenticada. O auxiliar one-dir recompilado foi executado fora da instalação: aguardou o processo de teste, aplicou a troca em uma pasta isolada e preservou a versão anterior. O executável principal retornou saída 0 e preservou a biblioteca legada isolada. O primeiro ensaio one-file falhou ao extrair uma DLL no temporário deste host e foi substituído por one-dir; esse arquivo com falha não integra a entrega.


## Checkpoint 0.1.4 — correção da consulta de atualizações

Corrigida a leitura da lista de versões: o GitHub pode retornar gzip e o leitor anterior usava o corpo bruto sem descompactar. A falha foi reproduzida com resposta HTTP gzip controlada e na API pública github/docs sem credenciais; a consulta pública passou após usar iter_content com limite de 8 MB descompactados. Isso confirma o defeito do leitor, mas não prova que a mensagem de conexão do usuário tinha exatamente essa causa.

Agora erros de proxy, certificado HTTPS, timeout, conexão e JSON inválido têm mensagens distintas, sem exibir URLs ou segredos. Não foi desativada a validação TLS nem contornada a configuração de proxy. O teste público de rede no ambiente Codex exigiu permissão explícita de rede; sem ela o proxy restrito do ambiente recusava a conexão.

A interface exige salvar uma credencial digitada antes de consultar e informa quando não há credencial no cofre. O campo é limpo ao salvar com sucesso. Nenhum token real do usuário foi lido, copiado ou enviado por esta sessão. Consulta autenticada ao repositório privado continua pendente de validação no aplicativo pelo usuário.

Validação: 46 testes passaram em 5,77 s; incluem regressão com gzip real do urllib3/Requests, mensagens de erros de rede sem vazamento de segredos e bloqueio de consulta com token não salvo. Consulta pública real sem autenticação retornou com sucesso, sem atualizações compatíveis. O 0.1.3 pode precisar de substituição manual caso a consulta antiga impeça baixar esta correção.


## Checkpoint 0.1.5 — paletas de cores

Adicionadas dez paletas: Azul, Verde, Amarelo, Vermelho, Preto, Branco, Roxo, Rosa, Laranja e Ciano. Nove usam superfícies escuras com acentos dessaturados; Branco é claro, com fundos quentes e texto escuro. A preferência fica em Configurações > Aparência > Tema, é aplicada imediatamente e persiste no SQLite em appearance.theme. Verde continua como padrão para bibliotecas sem preferência; valores antigos/desconhecidos usam esse padrão.

As paletas alteram fundos, painéis, campos, textos, botões, seleção, foco, progresso, navegação, diálogos e cores de capas ausentes. A aplicação também define QPalette para controles do Qt. As artes e capturas originais não são recoloridas. Estados desabilitados recebem tratamento próprio. A moldura externa da janela e diálogos nativos de arquivos podem seguir as preferências do Windows.

Validação: 58 testes passaram em 12,82 s, incluindo contraste mínimo 4,5:1 dos pares de texto normal verificados nas dez paletas, troca imediata, navegação nas seis áreas em cada tema e reabertura do banco preservando a escolha. Isso não é uma auditoria completa de acessibilidade. Foram renderizadas as dez telas iniciais, e a comparação de paletas e o tema Branco foram inspecionados visualmente. Preferências e controles reais de DPI ainda precisam de validação humana no Windows.


## Checkpoint 0.1.6 — diagnóstico OAuth
61 testes passaram, incluindo falha de troca de token, falha de gravação no cofre e inicialização após persistência com dependências substituídas. As mensagens e logs de falha não incluem o segredo de teste. Executável Windows final passou smoke das seis páginas (exit 0) e SQLite integrity_check=ok em diretório isolado. Não valida OAuth real nem resolve a causa original sem nova tentativa do usuário.


## 0.1.7 — diagnóstico de rede Drive (11/11/2026)

- Classificação segura da cadeia de exceções: proxy, TLS, DNS, timeout, conexão recusada/interrompida e causa não informada. Não imprime mensagens, URLs privadas ou tokens.
- Botão Testar conexão faz GET HTTPS ao endpoint público de token sem código OAuth, JSON ou token; uma resposta HTTP não prova autenticação nem sucesso de POST OAuth.
- Troca inicial do código por token tem timeout de conexão 10 s e leitura 30 s; não repete automaticamente um código de uso único.
- Mantém verificação HTTPS e configurações de proxy do ambiente. Não desativa firewall nem altera certificados.
- 73 testes automatizados passaram. Teste público no ambiente de execução resultou em categoria proxy; o ambiente do aplicativo instalado pode usar configuração diferente. OAuth real segue pendente, sem afirmar correção da causa original.


## 0.1.8 — transporte HTTPS (11/11/2026)
- Mensagens incluem cadeia de classes e códigos numéricos de erro, sem texto bruto de exceções ou URLs privadas. Identifica também acesso de rede recusado pelo sistema e encerramento sem resposta HTTP.
- Modo --network-test verifica endpoint público sem tokens e salva network-test.txt em --data-dir para comparar o executável ao Python. Não altera firewall ou certificados.
- Python com acesso de rede autorizado recebeu HTTP 404 do endpoint de token. Isso valida alcance HTTPS, não OAuth nem equivalência com a rede usada pelo usuário.


### Correção confirmada do pacote TLS — 0.1.8
O runtime Python do ambiente modifica SSLContext.__new__ para carregar codex-rejected-cas.pem. O empacotamento anterior omitia esse dado, causando ConnectionError > ProtocolError > FileNotFoundError(errno=2) em ssl.py:440. O build agora inclui o arquivo do próprio runtime, quando presente, em _internal. Não altera a política TLS nem desativa verificação. No executável local, incluir o arquivo mudou a falha reproduzida para resposta HTTPS HTTP 404 do endpoint público de token. Autenticação real com conta do usuário continua pendente. A versão corrige uma causa concreta de falha do transporte; outras restrições de rede podem existir.


## 0.1.9 — reconhecimento de plataformas (11/11/2026)
Aliases explícitos para Nintendo Game Boy Advanced, Super Nintendo (SNES), Switch e variantes comuns, normalizando espaços e separadores. Não usa extensão compartilhada nem correspondência parcial; caminhos com plataformas contraditórias ficam para revisão. Botão Reconhecer plataformas preenche somente campos vazios usando caminhos locais, sem rede, downloads ou alteração de associações.
Validação: 85 testes passaram. Aplicado ao banco real após cópia consistente: 2.102 registros corrigidos; integridade ok; IDs, nomes originais, associações e disponibilidade preservados. Totais: GBA 1.098, SNES 986, DS 24, Switch 18, 3DS 15, PSP 3; três arquivos em Temas permanecem sem plataforma.

Usuário esclareceu que Temas contém temas de emulador, não jogos. A pasta raiz Temas agora é ignorada pelo scanner, incluindo ZIPs. Três registros sem associação/disponibilidade foram retirados do índice local após backup; nenhum arquivo Drive foi alterado. Coleção real: 2.144 ROMs, todas com plataforma identificada.


## 0.1.10 — pastas personalizadas e capas (11/11/2026)
- Aliases PS1/PSX, PS2, PS3, GameCube/NGC, Wii, N64, NES, Game Boy/Color, Mega Drive, Saturn e Dreamcast.
- Pastas e plataformas: associação por ID de pasta indexada, plataforma livre ou conhecida, herança por subpastas e prioridade da regra mais específica. Salvar/remover reclassifica o ramo existente, sem alterar jogos associados, nomes ou arquivos. Atualize o Drive para descobrir pastas novas; pastas vazias sem regra reconhecível permanecem para revisão. Regras persistem no SQLite; não são credenciais.
- Criar jogo desta ROM exige título confirmado e vincula a versão; outras versões podem ser associadas ao jogo existente. Não cria milhares de jogos nem mescla títulos automaticamente.
- Capa do jogo acessível pela lista Drive após associação; imagem local é validada e copiada ao cache sem chave. Busca SteamGridDB exige chave própria e confirmação do jogo/arte. Lista da biblioteca agora exibe miniaturas; lista Drive mostra capas de jogos associados.
- Scanner não fornece capas nem identifica títulos sozinho. Não houve download ou atribuição automática de artes na coleção real. Não foi necessário alterar credenciais.
- 97 testes passaram antes do ajuste final de atualização da galeria após fechar Drive; testes cobrem herança, regra específica, persistência, renomeação por ID, limites de ramo, validação, criação de jogo sem duplicar arquivo e ícone de capa na tabela.


## 0.1.11 — pesquisa no índice Drive (11/11/2026)
Pesquisa local por nome original, título do jogo associado e pasta; ignora caixa e acentos. Filtro de plataforma combinado, contador visível e estado vazio. Consulta caracteres como % e _ literalmente, sem transformar texto em SQL. Preserva a seleção pelo ID enquanto o arquivo permanecer visível; ações operam sobre a lista filtrada. Não consulta APIs nem baixa arquivos. Inclui todas as funções de pastas e capas da 0.1.10, publicada antes deste pedido.


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

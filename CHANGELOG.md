# Changelog

## 0.1.27

- Adicionar jogo restrito a Início e Biblioteca, no topo direito, sem cópia lateral.
- Inclui as correções de layout, Desejos, Steam e perfil da 0.1.26.

## 0.1.26

- Perfil local com foto e apelido, exibidos na lateral, sem conta/login.

- Cadastro global no topo direito, sem duplicata lateral; desejo adicionado separadamente.
- Removidas instruções e frases promocionais de estados vazios e painéis.
- Steam com tabela rolável e tamanho limitado; resumo substitui log por jogo.

- Logos usam o espaço reservado dentro dos cards de Desejos sem distorção.
- Artes faltantes são solicitadas para jogos identificados ao abrir a lista.
- Lista aberta atualiza ao receber a logo; tentativas limitadas por sessão.
- Inclui correções de layout e navegação da 0.1.25.

## 0.1.25

- Corrigidos banners expansivos, tamanho de logos e espaçamento das capas/legendas.
- Cadastro na lateral e busca do Início com resultados ao digitar.
- Estados vazios sem corte, estatísticas adaptativas e memórias sem limite de texto.
- Área principal limitada em telas grandes; dez temas conforme prompt reenviado.
- Revisão visual inclui Full HD, estados vazios e tema claro.

## 0.1.24 — interface e PT-BR — publicada em 13/11/2026

- Cadastro compacto, cabeçalhos e filtros reorganizados; capas ampliadas com título/status alinhados.
- Ícones oficiais Steam/Drive e nove temas escuros; preferência clara antiga usa Verde.
- Wishlist separada da posse, com logos em cards quadrados e ações alinhadas na mesma linha.
- Menor preço em BRL, lojas/keyshops e links de comparação; nenhuma meta de preço na interface.
- Calendário diário de horas, descrições PT quando disponíveis e datas DD/MM/AAAA.
- Informações adicionais da ficha sempre visíveis; GIFs/animações recusados nas artes.
- Dados, arquivos, schema 4 e proteções de processos/QThreads preservados.
- Publicada como pre-release após 216 testes Windows em 94,04 s, sem falhas/erros/skips;
  smokes do fonte/ZIP extraído e atualizador aprovados; 48 capturas Qt com fixtures.
- Workflow 43347929302; tag em 425dd12. Aprovação estética/DPI e contas autenticadas separadas.

## 0.1.19 — composição visual e banners Steam

- Cards próprios e grade responsiva; busca no cabeçalho e controles mais discretos.
- Início com continuidade e atividade lado a lado, hero com cantos e altura adaptável.
- Ficha com barra de ações, descrição e informações compactas; detalhes recolhidos.
- Tipografia, superfícies, ícones das conexões e barra de título Windows revistos.
- Steam prioriza banner panorâmico; corrige header automático antigo por proveniência.
- Escolhas manuais e cache preservados, inclusive ao confirmar arte durante download.
- 177 testes locais passaram; smokes aprovados; rede do CDN Steam bloqueada no Cloud.

## 0.1.18 — identidade e interface

- Identidade intervalo: C// e checkpo//nt, com maior respiro entre símbolo e nome.
- Início pessoal com destaque, continuidade, recentes e atividade da biblioteca.
- Biblioteca com abas rápidas, filtros extras recolhidos e densidade ajustável.
- Ficha com banner/logo, ações no menu e abas; capa preservada só na biblioteca.
- Cadastro por origem e Configurações em quatro seções compactas.
- Dez temas preservados; ícone vetorial em runtime e ICO no executável.
- Rascunho do diário preservado ao atualizar artes. Sem migração de banco.

## 0.1.17 — salvamento sem carregamentos modais encadeados

- Reproduzido SIGSEGV/139 na abertura do carregamento após salvar na 0.1.16.
- Cadastro persistido imediatamente; ficha/imagens seguem em fila em segundo plano.
- Removida a identificação modal de dentro de Salvar e o segundo modal após o cadastro.
- Drive, edição identificada e atualização em lote também usam carregamento sem novo exec.
- 164 testes locais aprovados; regressões de processo completo com imagens, falha do
  auxiliar e Drive. Pacote passa a validar salvar/renderizar no EXE extraído.
- Diagnóstico nativo habilitado na interface sem variáveis locais. Schema permanece 4.

## 0.1.16 — cadastro simples e proteção das operações (desenvolvimento)

- Nome/plataforma no cadastro inicial; opções avançadas e Drive recolhidos.
- Identificação automática com fontes disponíveis, sem catálogo obrigatório.
- Download Drive adiciona o jogo e busca imagens após verificar o arquivo.
- Download e imagens em processos auxiliares; falhas abruptas preservam a interface.
- Proteção de fechamento com workers ativos, slots Qt no receptor e parciais preservados.
- Causa exata do crash Windows relatado ainda não reproduzida; contenção validada
  com interrupções controladas. Smoke do pacote passa a incluir o auxiliar real.

## 0.1.15 — ficha e imagens no cadastro (desenvolvimento)

- Importação Steam completa dados e imagens por AppID, em worker com progresso.
- Cadastro manual/ROM pede identificação no catálogo ao salvar; modo offline mantido.
- Ação para completar fichas e imagens faltantes da biblioteca já identificada.
- Campos pessoais e artes existentes preservados; cancelamento após o jogo atual.
- Provedor público da loja Steam sem chave adicional; RAWG fornece capa/banner.
- 146 testes aprovados e smoke isolado OK em Linux. Rede Steam bloqueada pelo proxy;
  download real e Windows não validados. Sem publicação da 0.1.15; schema permanece 4.

## 0.1.14 — Importação Steam (desenvolvimento)

- Corrigido encerramento nativo do formulário sem pai: seletores de arquivo usam
  método do receptor Qt em vez de lambdas que capturavam o diálogo.
- Duas regressões de seletores/lifecycle; 136 testes completos passaram com exit 0
  após a correção. Smoke de seis páginas com SQLite íntegro reconfirmado.

- Biblioteca via Steam Web API com chave no cofre, SteamID64 e seleção explícita.
- Associação manual e reimportação por AppID preservando dados pessoais.
- Horas por conta e conquistas por jogo separadas das sessões/marcos locais.
- Migração SQLite 4 com backup prévio; conflitos e lixeira cancelam o lote.
- 29 testes focados aprovados; Steam autenticada e build Windows pendentes.
- Nenhum executável Windows ou Release 0.1.14 publicado nesta etapa.

## Continuidade entre dispositivos — 11/11/2026

- Contexto durável em CONTINUITY.md e requisitos em PRODUCT_VISION.md.
- AGENTS.md orienta novos chats e CLOUD_SETUP.md documenta testes isolados na nuvem.
- README atualizado para a versão 0.1.13 e validações reais de Drive/SteamGridDB.
- Preparação não transfere credenciais, biblioteca pessoal nem transcript integral do chat.

## 0.1.5 — Paletas

- Dez temas coesos e discretos, incluindo Branco claro e Preto neutro.
- Seletor em Configurações, aplicação imediata e preferência persistente.
- Controles, diálogos e capas ausentes acompanham o tema escolhido.
- 58 testes passaram, incluindo contraste de texto e persistência.


## 0.1.4 — Consulta de atualizações

- Corrigida resposta gzip da API GitHub.
- Mensagens distintas para proxy, TLS, timeout e conteúdo inválido.
- Consulta exige salvar a credencial digitada antes de continuar.
- 46 testes passaram e consulta pública real foi validada sem token.


## 0.1.3 — Atualizações

- Consulta de releases GitHub privadas com credencial no cofre Windows.
- Download com SHA-256/tamanho, extração validada e auxiliar de instalação.
- Preservação da versão anterior e recuperação em falhas de cópia.
- 39 testes passaram; integração autenticada real continua pendente.


## 0.1.2 — Saves por jogo

- Perfis persistentes de saves tradicionais por jogo.
- Backup manual por jogo e backup opcional ao encerrar a sessão, em segundo plano.
- Histórico por jogo e restauração para a pasta original com cópia da versão anterior.
- Validação de estabilidade antes e depois da cópia; bloqueio de execução/fechamento durante operações.
- 28 testes passaram, incluindo sessão encerrada disparando backup real em worker.


## 0.1.1 — Checkpoint

- Novo nome na interface e no executável.
- Removidos slogans e subtítulos promocionais, com estados vazios diretos.
- Preservados banco, cofre e trava legados para compatibilidade com a biblioteca existente.


## 0.1.0 — 2026-11-10

- Projeto criado do zero em Python/PySide6, SQLite transacional e duas migrações versionadas.
- Navegação principal, identidade escura, estados vazios, biblioteca com CRUD, lixeira e filtros.
- Diário, mídia referenciada, conquistas pessoais, wishlist local e estatísticas reais.
- Execução local, perfis de emuladores, argumentos sem shell, sessões e recuperação manual.
- Cliente RAWG, seleção de artes SteamGridDB e cache validado; validação real com chaves pendente.
- Cliente Drive readonly, varredura paginada, cursor incremental, revisão manual e downloads verificados; validação real OAuth pendente.
- Importação DAT Logiqx e busca conservadora de checksum.
- Backup local de saves e restauração com cópia anterior e verificação SHA-256.
- Testes de domínio, segurança de caminhos, persistência, clientes controlados e UI headless.
- Documentação técnica, roadmap e receita de build Windows.

Não inclui ainda sincronização de saves no Drive, preços automáticos, Steam ou RetroAchievements. Ver PROJECT_STATUS.md para evidência final e pendências.


## Não publicado — diagnóstico Drive
- Erros de autenticação por etapa, sem mensagens contendo segredos.
- Callback do navegador distingue autorização recebida de conexão concluída.
- Suprimidos logs da biblioteca OAuth com códigos e URLs privados.


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

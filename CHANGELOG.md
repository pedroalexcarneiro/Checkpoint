# Changelog

Registros anteriores descrevem o estado de cada versão; não são instruções atuais.

## 0.1.28 — revisão do produto e publicação autorizada

- Renomeação técnica de GameVault para Checkpoint: pacote, launcher, banco, diretório de dados, cofre e scripts.
- Migração por cópia, SQLite consistente com backup/integridade, schema 4 preservado, cofre sem apagar o serviço antigo, travas de instância e recuperação sem perda da origem.
- Nove temas; removido Branco. Preferências antigas compatíveis passam para Verde.
- Biblioteca de quatro colunas e capas verticais; Desejos com logos contidas em áreas fixas; Início, ficha, cadastro e Conexões alinhados às referências.
- Cadastro exige seleção, distingue busca/ausência/seleção, confirma desejos visivelmente e preserva jogos já possuídos. Contadores e estados vazios corrigidos.
- Documentação atual reorganizada; histórico consolidado abaixo. Na etapa de correções não houve publicação; após autorização posterior do dono, a pré-release v0.1.28 foi publicada com o mesmo artefato Windows validado.

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
- Menor preço em BRL, lojas/keyshops e links de comparação; nenhuma meta de preço na interface.
- Calendário diário de horas, descrições PT quando disponíveis e datas DD/MM/AAAA.
- Informações adicionais da ficha sempre visíveis; GIFs/animações recusados nas artes.
- Dados, arquivos, schema 4 e proteções de processos/QThreads preservados.
- Publicada como pre-release após 216 testes Windows em 94,04 s, sem falhas/erros/skips;
  smokes do fonte/ZIP extraído e atualizador aprovados; 48 capturas Qt com fixtures.
- Workflow 43347929302; tag em 425dd12. Aprovação estética/DPI e contas autenticadas separadas.

## 0.1.23 — fontes e revisão Windows verificável

A 0.1.22 foi publicada no commit 39da4e198a2226d82ae90a657c1f1696cb1afa16,
workflow 43278032123 success, 199 testes Windows e smokes aprovados. Ao abrir
O problema não foi detectado pelos testes funcionais. Assets/tag 0.1.22 ficam
preservados. A entrega é substituída por 0.1.23, com registro de Segoe UI antes
da UI e verificação de glifos portugueses que bloqueia capturas sem fonte.
As 37 capturas devem ser abertas e conferidas antes da confirmação final.

## 0.1.22 — revisão completa da interface

A revisão abrange as seis áreas principais, quatro abas da ficha, cadastro,
editor em quatro abas e diálogos de Drive, Steam, imagens, metadados, emuladores,
pastas e atualização. design_system.py concentra superfícies, ícones vetoriais,
estados vazios, grids, colunas adaptativas, previews e amostras de tema.
Tipografia 28/18/14/12 px, bordas discretas, superfícies em gradiente sutil,
componentes compactos e espaçamento comum. Verde padrão aproximado da referência;
os dez temas e preferências persistentes permanecem disponíveis.

Início: descrição no hero, continuidade com tempo local e atividade pessoal;
colunas empilham em janelas estreitas. Biblioteca: grade de quatro colunas em
1000 px, até seis confortável, oito compacta, sem deformar artes. Nome e status
separados da imagem. Cabeçalho de altura estável e filtros sem abas cortadas.
Ficha: banner/logo, favoritos reais, galeria, sessões e marcos em cards, memórias
e arquivos/saves organizados. Favoritar preserva rascunho do diário.
Desejos: capas e metas pessoais com ações reais. Memórias: Tudo/Diário/Capturas
e vídeos, grid com mídia local, sem registros de jogos removidos. Estatísticas:
indicadores, gráfico e legenda com cores, períodos legíveis em PT-BR e plataformas.
Configurações: perfil local, swatches dos dez temas, conexões e pastas compactas,
backups e lixeira recolhida. Nome local usa settings, sem alteração de schema.
Editor opcional: Ficha/Execução/Imagens/Pessoal; contratos de validação e dados
preservados. Diálogos de integração mantêm operações existentes com novo enquadramento.

Reforço de ciclo de vida: busca aguarda Show; diálogo independente não destrói
QThread ativa ao fechar; filtro de eventos tolera destruição do wrapper Python;
consulta de artes inicia após exibição. Temporizadores da janela param ao fechar.
Regressão em subprocesso verifica consulta ativa e encerramento sem abort nativo.

Validação final Linux: 199 testes em 73,65 s, exit 0, sem abort nativo.
Smokes de seis páginas, auxiliar e cadastro com imagem/SQLite passaram com dados
isolados. scripts/render_ui_review.py gera 37 capturas Qt com fixtures, sem conta
ou consulta remota; package_ui_review.py publica PNGs e índice, excluindo bases e
logs. Workflow passa a gerar revisão visual Windows junto da release. Capturas
com fixtures não são prova de integração autenticada nem aprovação estética.
Build Windows 0.1.22 e publicação pendentes neste registro.

## 0.1.21 — busca única e composição visual

Correção da interpretação da marca: wordmark checkpo//nt original centralizado,
sem C// na lateral. Lateral de 198 px, cabeçalho com busca à direita, biblioteca
com abas segmentadas e filtros responsivos (segunda linha em 1000 px), atividade
com ícones e cards compactos. Botão de voltar integrado ao banner da ficha.
Continuar jogando no Início só inicia jogo quando há executável configurado;
nos demais casos Ver jogo abre a ficha. Dez temas e imagens inteiras preservados.

Cadastro novo usa QuickAdd dentro de GameDialog: janela 1040×720, busca única,
resultados e ROMs indexadas à esquerda, prévia da ficha à direita, adicionar sem
formulário técnico. Importação Steam em lote é opcional. Selecionar ROM dispara
consulta na sua plataforma; nenhuma ROM é vinculada por semelhança fraca. Ficha
inequívoca pode ser sugerida; ambiguidades exigem seleção. Correções ficam no
editor opcional ou na ficha depois de salvar. Provedores configurados são
consultados juntos, com agrupamento de resultados compatíveis. O salvamento
continua imediato; conclusão de dados/artes ocorre no auxiliar isolado. Campos
preenchidos e escolhas manuais são preservados. Preferência global de automação
continua respeitada. Provedores autenticados exigem configuração única existente.

Consultas/previews rodam em processos isolados. Respostas antigas não alteram
nova seleção, trabalhos de detalhe são coalescidos, fechamento do diálogo não
destrói QThread ativa. Busca pública Steam sem chave; RAWG/SteamGridDB usados
quando configurados. Falha de busca não impede adicionar pelo nome. Não há
promessa de arte disponível para todo título, nem validação autenticada aqui.

Linux: 192 testes em 39,54 s, zero falhas, Qt offscreen. Smokes de seis páginas,
auxiliar e cadastro com imagem/SQLite aprovados em diretórios isolados. Capturas
reais da interface com fixtures, janelas 1440×980/1000×700 e cadastro 1040×720;
fidelidade estética depende de avaliação do usuário. Consulta pública Steam
bloqueada na nuvem (URLError/OSError); nenhum conteúdo de credencial foi lido
ou exposto. Build Windows/release 0.1.21 pendentes neste registro.

## 0.1.20 — revisão após capturas reais do usuário

Barra lateral com nome centralizado, sem símbolo. Capas sem moldura lateral,
espaços 2:3 para posters Steam e títulos pintados abaixo da arte. Banner define
a proporção do quadro, sem cópia desfocada. Ficha organiza descrição/dados à
esquerda e galeria pessoal à direita. Estatísticas extraídas para módulo próprio,
com indicadores, gráfico temporal e distribuição por status. Rodapé de trabalho
compacto, cancelamento dos pendentes e mensagens transitórias.

Cadastro manual/Drive/Steam oferece restaurar ou adicionar como novo quando há
correspondência removida. Identidades públicas anteriores são arquivadas em
settings ao escolher novo; histórico, notas, arte e registro removido permanecem.
Restaurar depois não rouba identidades já atribuídas ao novo cadastro. A fila
sinaliza correspondências tardias do catálogo para decisão na thread da UI.
Comparação por título é exata e exige a mesma plataforma; ambiguidades não são
associadas automaticamente. Operações de importação usam savepoints aninháveis.

Validação Linux: 185 testes, 33,42 s, exit 0. Comando:
`QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests -q -p no:cacheprovider`.
Smokes via scripts.package_windows_release.smoke/save_smoke: seis páginas,
auxiliar, cadastro com imagem e integridade SQLite aprovados com dados isolados.
Capturas reais com fixtures em 1440×980 e 1000×700, tema escuro/claro; não são
aprovação estética nem testes autenticados. api.github.com respondeu HTTP 200;
v0.1.19 consultada em leitura. Schema 4, dados e releases anteriores preservados.
Build/publicação Windows 0.1.20 pendentes do workflow neste registro.

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

## 0.1.13 — cadastro pelo Drive, títulos e enquadramento (11/11/2026)
- Adicionar jogo contém pesquisa local nas ROMs indexadas (nome/pasta), seleção da versão e preenchimento de nome sugerido, plataforma e origem. Atualizar índice abre o gerenciador diretamente; não é necessário passar por Configurações. O cadastro manual permanece disponível.
- Confirmar título original e completar dados abre escolha explícita no catálogo: SteamGridDB fornece título/identidade/artes com a chave já existente; RAWG fornece ficha detalhada com chave própria. Nome/plataforma vêm do Drive; gênero, descrição, desenvolvedora, publicadora e lançamento somente são preenchidos quando retornados pela fonte escolhida. Não há associação automática por semelhança.
- Salvar usa transação única para jogo, identidade e versão da ROM. Identidade já cadastrada reutiliza o jogo, preservando notas, status e capas; vínculos conflitantes/lixeira exigem revisão. Metadados confirmados podem padronizar o título exibido; original_name nunca é alterado. Artes são obtidas em worker com banco próprio após salvar, sem baixar ROM.
- Criar jogo desta ROM no gerenciador usa o mesmo formulário. Ao confirmar identidade pelo seletor de artes, o título do catálogo também passa a ser usado.
- Galeria e página individual agora mostram capa/banner inteiros, centralizados em quadros fixos, com preenchimento discreto. Não há recorte de logos/texto/personagens nem deformação. Fonte de imagem e cache originais preservados.
- Validação: 120 testes passaram com pytest result 0. Incluem preservação das bordas da arte, título canônico separado do arquivo, preenchimento, troca de ROM limpando metadados antigos, reutilização de versão, rollback sem órfãos e fechamento do progresso/catálogo. Telas renderizadas e inspecionadas em cópia local do banco.
- Busca real SteamGridDB por Zelda - the Minish Cap retornou The Legend of Zelda: The Minish Cap entre as opções. Quatro títulos reais foram padronizados pelos IDs SteamGridDB previamente confirmados, após backup consistente; IDs, original_name, vínculos e integridade do banco verificados. Nenhuma ROM ou arte foi baixada nessa padronização.
- RAWG continua sem validação autenticada nesta sessão; não promete ficha completa usando somente a chave SteamGridDB. Verificar em Windows: novo cadastro pelo Drive, escolha da edição correta, obtenção automática de artes e navegação após salvar.

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

## 0.1.11 — pesquisa no índice Drive (11/11/2026)
Pesquisa local por nome original, título do jogo associado e pasta; ignora caixa e acentos. Filtro de plataforma combinado, contador visível e estado vazio. Consulta caracteres como % e _ literalmente, sem transformar texto em SQL. Preserva a seleção pelo ID enquanto o arquivo permanecer visível; ações operam sobre a lista filtrada. Não consulta APIs nem baixa arquivos. Inclui todas as funções de pastas e capas da 0.1.10, publicada antes deste pedido.

## 0.1.10 — pastas personalizadas e capas (11/11/2026)
- Aliases PS1/PSX, PS2, PS3, GameCube/NGC, Wii, N64, NES, Game Boy/Color, Mega Drive, Saturn e Dreamcast.
- Pastas e plataformas: associação por ID de pasta indexada, plataforma livre ou conhecida, herança por subpastas e prioridade da regra mais específica. Salvar/remover reclassifica o ramo existente, sem alterar jogos associados, nomes ou arquivos. Atualize o Drive para descobrir pastas novas; pastas vazias sem regra reconhecível permanecem para revisão. Regras persistem no SQLite; não são credenciais.
- Criar jogo desta ROM exige título confirmado e vincula a versão; outras versões podem ser associadas ao jogo existente. Não cria milhares de jogos nem mescla títulos automaticamente.
- Capa do jogo acessível pela lista Drive após associação; imagem local é validada e copiada ao cache sem chave. Busca SteamGridDB exige chave própria e confirmação do jogo/arte. Lista da biblioteca agora exibe miniaturas; lista Drive mostra capas de jogos associados.
- Scanner não fornece capas nem identifica títulos sozinho. Não houve download ou atribuição automática de artes na coleção real. Não foi necessário alterar credenciais.
- 97 testes passaram antes do ajuste final de atualização da galeria após fechar Drive; testes cobrem herança, regra específica, persistência, renomeação por ID, limites de ramo, validação, criação de jogo sem duplicar arquivo e ícone de capa na tabela.

## 0.1.9 — reconhecimento de plataformas (11/11/2026)
Aliases explícitos para Nintendo Game Boy Advanced, Super Nintendo (SNES), Switch e variantes comuns, normalizando espaços e separadores. Não usa extensão compartilhada nem correspondência parcial; caminhos com plataformas contraditórias ficam para revisão. Botão Reconhecer plataformas preenche somente campos vazios usando caminhos locais, sem rede, downloads ou alteração de associações.
Validação: 85 testes passaram. Aplicado ao banco real após cópia consistente: 2.102 registros corrigidos; integridade ok; IDs, nomes originais, associações e disponibilidade preservados. Totais: GBA 1.098, SNES 986, DS 24, Switch 18, 3DS 15, PSP 3; três arquivos em Temas permanecem sem plataforma.

Usuário esclareceu que Temas contém temas de emulador, não jogos. A pasta raiz Temas agora é ignorada pelo scanner, incluindo ZIPs. Três registros sem associação/disponibilidade foram retirados do índice local após backup; nenhum arquivo Drive foi alterado. Coleção real: 2.144 ROMs, todas com plataforma identificada.

## 0.1.8 — transporte HTTPS (11/11/2026)
- Mensagens incluem cadeia de classes e códigos numéricos de erro, sem texto bruto de exceções ou URLs privadas. Identifica também acesso de rede recusado pelo sistema e encerramento sem resposta HTTP.
- Modo --network-test verifica endpoint público sem tokens e salva network-test.txt em --data-dir para comparar o executável ao Python. Não altera firewall ou certificados.
- Python com acesso de rede autorizado recebeu HTTP 404 do endpoint de token. Isso valida alcance HTTPS, não OAuth nem equivalência com a rede usada pelo usuário.


### Correção confirmada do pacote TLS — 0.1.8
O runtime Python do ambiente modifica SSLContext.__new__ para carregar codex-rejected-cas.pem. O empacotamento anterior omitia esse dado, causando ConnectionError > ProtocolError > FileNotFoundError(errno=2) em ssl.py:440. O build agora inclui o arquivo do próprio runtime, quando presente, em _internal. Não altera a política TLS nem desativa verificação. No executável local, incluir o arquivo mudou a falha reproduzida para resposta HTTPS HTTP 404 do endpoint público de token. Autenticação real com conta do usuário continua pendente. A versão corrige uma causa concreta de falha do transporte; outras restrições de rede podem existir.

## 0.1.7 — diagnóstico de rede Drive (11/11/2026)

- Classificação segura da cadeia de exceções: proxy, TLS, DNS, timeout, conexão recusada/interrompida e causa não informada. Não imprime mensagens, URLs privadas ou tokens.
- Botão Testar conexão faz GET HTTPS ao endpoint público de token sem código OAuth, JSON ou token; uma resposta HTTP não prova autenticação nem sucesso de POST OAuth.
- Troca inicial do código por token tem timeout de conexão 10 s e leitura 30 s; não repete automaticamente um código de uso único.
- Mantém verificação HTTPS e configurações de proxy do ambiente. Não desativa firewall nem altera certificados.
- 73 testes automatizados passaram. Teste público no ambiente de execução resultou em categoria proxy; o ambiente do aplicativo instalado pode usar configuração diferente. OAuth real segue pendente, sem afirmar correção da causa original.

## 0.1.6 — diagnóstico do Drive

Diagnóstico da autenticação e do transporte, sem registrar credenciais. OAuth real depende da conta e do ambiente Windows.

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

## Continuidade entre dispositivos — 11/11/2026

- Contexto durável em CONTINUITY.md e requisitos em PRODUCT_VISION.md.
- AGENTS.md orienta novos chats e CLOUD_SETUP.md documenta testes isolados na nuvem.
- README atualizado para a versão 0.1.13 e validações reais de Drive/SteamGridDB.
- Preparação não transfere credenciais, biblioteca pessoal nem transcript integral do chat.

## Não publicado — diagnóstico Drive
- Erros de autenticação por etapa, sem mensagens contendo segredos.
- Callback do navegador distingue autorização recebida de conexão concluída.
- Suprimidos logs da biblioteca OAuth com códigos e URLs privados.

## Histórico transferido das instruções de instalação

 — Checkpoint

Nome visível e executável alterados para Checkpoint. Removidos slogans da navegação, do início e dos estados vazios. Os dados, a trava de instância e o cofre continuam usando os identificadores internos Checkpoint para abrir a biblioteca existente sem migração. O pacote Python e a pasta de fontes também permanecem com seus nomes internos. O usuário confirmou que os fluxos locais solicitados no teste anterior funcionaram; isso não valida integrações autenticadas.


## Checkpoint 0.1.3 — saves por jogo

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

## Registro histórico da renomeação técnica

O produto antes chamado GameVault passou a usar Checkpoint em todos os identificadores atuais. Estes caminhos históricos documentam a troca; não são nomes de execução.

| Caminho anterior | Caminho atual |
| --- | --- |
| `gamevault/.gitkeep` | `checkpoint/.gitkeep` |
| `gamevault/__init__.py` | `checkpoint/__init__.py` |
| `gamevault/activity_heatmap.py` | `checkpoint/activity_heatmap.py` |
| `gamevault/app.py` | `checkpoint/app.py` |
| `gamevault/artwork_dialog.py` | `checkpoint/artwork_dialog.py` |
| `gamevault/artwork_progress.py` | `checkpoint/artwork_progress.py` |
| `gamevault/artwork_render.py` | `checkpoint/artwork_render.py` |
| `gamevault/assets/services/google-drive.png` | `checkpoint/assets/services/google-drive.png` |
| `gamevault/assets/services/steam.ico` | `checkpoint/assets/services/steam.ico` |
| `gamevault/auto_artwork.py` | `checkpoint/auto_artwork.py` |
| `gamevault/automatic_catalog.py` | `checkpoint/automatic_catalog.py` |
| `gamevault/branding.py` | `checkpoint/branding.py` |
| `gamevault/catalog_picker.py` | `checkpoint/catalog_picker.py` |
| `gamevault/collection_views.py` | `checkpoint/collection_views.py` |
| `gamevault/completion_queue.py` | `checkpoint/completion_queue.py` |
| `gamevault/cover_grid.py` | `checkpoint/cover_grid.py` |
| `gamevault/credentials.py` | `checkpoint/credentials.py` |
| `gamevault/database.py` | `checkpoint/database.py` |
| `gamevault/description_provenance.py` | `checkpoint/description_provenance.py` |
| `gamevault/design_system.py` | `checkpoint/design_system.py` |
| `gamevault/detail_view.py` | `checkpoint/detail_view.py` |
| `gamevault/dialogs.py` | `checkpoint/dialogs.py` |
| `gamevault/drive_dialog.py` | `checkpoint/drive_dialog.py` |
| `gamevault/emulator_dialog.py` | `checkpoint/emulator_dialog.py` |
| `gamevault/enrichment.py` | `checkpoint/enrichment.py` |
| `gamevault/folder_platform_dialog.py` | `checkpoint/folder_platform_dialog.py` |
| `gamevault/fonts.py` | `checkpoint/fonts.py` |
| `gamevault/game_editor.py` | `checkpoint/game_editor.py` |
| `gamevault/game_import.py` | `checkpoint/game_import.py` |
| `gamevault/game_saves.py` | `checkpoint/game_saves.py` |
| `gamevault/home_view.py` | `checkpoint/home_view.py` |
| `gamevault/integrations/.gitkeep` | `checkpoint/integrations/.gitkeep` |
| `gamevault/integrations/__init__.py` | `checkpoint/integrations/__init__.py` |
| `gamevault/integrations/descriptions.py` | `checkpoint/integrations/descriptions.py` |
| `gamevault/integrations/drive.py` | `checkpoint/integrations/drive.py` |
| `gamevault/integrations/ggdeals.py` | `checkpoint/integrations/ggdeals.py` |
| `gamevault/integrations/http.py` | `checkpoint/integrations/http.py` |
| `gamevault/integrations/images.py` | `checkpoint/integrations/images.py` |
| `gamevault/integrations/metadata.py` | `checkpoint/integrations/metadata.py` |
| `gamevault/integrations/network.py` | `checkpoint/integrations/network.py` |
| `gamevault/integrations/steam.py` | `checkpoint/integrations/steam.py` |
| `gamevault/integrations/steam_store.py` | `checkpoint/integrations/steam_store.py` |
| `gamevault/jobs.py` | `checkpoint/jobs.py` |
| `gamevault/launcher.py` | `checkpoint/launcher.py` |
| `gamevault/library.py` | `checkpoint/library.py` |
| `gamevault/locale.py` | `checkpoint/locale.py` |
| `gamevault/metadata_dialog.py` | `checkpoint/metadata_dialog.py` |
| `gamevault/price_queue.py` | `checkpoint/price_queue.py` |
| `gamevault/price_view.py` | `checkpoint/price_view.py` |
| `gamevault/prices.py` | `checkpoint/prices.py` |
| `gamevault/profile_dialog.py` | `checkpoint/profile_dialog.py` |
| `gamevault/quick_add.py` | `checkpoint/quick_add.py` |
| `gamevault/rom_catalog.py` | `checkpoint/rom_catalog.py` |
| `gamevault/save_profiles.py` | `checkpoint/save_profiles.py` |
| `gamevault/save_smoke.py` | `checkpoint/save_smoke.py` |
| `gamevault/saves.py` | `checkpoint/saves.py` |
| `gamevault/settings_view.py` | `checkpoint/settings_view.py` |
| `gamevault/statistics_view.py` | `checkpoint/statistics_view.py` |
| `gamevault/steam_dialog.py` | `checkpoint/steam_dialog.py` |
| `gamevault/steam_library.py` | `checkpoint/steam_library.py` |
| `gamevault/task_status.py` | `checkpoint/task_status.py` |
| `gamevault/theme.py` | `checkpoint/theme.py` |
| `gamevault/trash_import.py` | `checkpoint/trash_import.py` |
| `gamevault/ui_components.py` | `checkpoint/ui_components.py` |
| `gamevault/unified_catalog.py` | `checkpoint/unified_catalog.py` |
| `gamevault/update_installer.py` | `checkpoint/update_installer.py` |
| `gamevault/updates.py` | `checkpoint/updates.py` |
| `gamevault/updates_dialog.py` | `checkpoint/updates_dialog.py` |
| `gamevault/window.py` | `checkpoint/window.py` |
| `gamevault/window_style.py` | `checkpoint/window_style.py` |
| `gamevault/worker.py` | `checkpoint/worker.py` |
| `run_gamevault.py` | `run_checkpoint.py` |
| Serviço do cofre: `GameVault` | `Checkpoint` |
| `%LOCALAPPDATA%\GameVault` | `%LOCALAPPDATA%\Checkpoint` |
| `gamevault.sqlite` | `checkpoint.sqlite` |
| `gamevault.lock` | `checkpoint.lock` |

# Estado do projeto — Checkpoint

## Publicação confirmada — v0.1.16

Pré-release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.16
Commit: 41208c3217ed3ec007aa267196a6ddc3eedfbf7c; workflow 43215131011 success.
Relatório anexado confirma 158 testes Windows (zero falhas/erros/skips), smoke
fonte/ZIP extraído, auxiliar isolado nos dois formatos e CheckpointUpdater --check.
ZIP: 83.897.718 bytes; SHA-256
b97c5d5a79df5065644fae93380fcf6f1bfc1133046f1b4f4a887e6b4b6fac6f.
Esta confirmação prevalece sobre as pendências de publicação abaixo. O crash
original não foi reproduzido; a contenção foi validada com saídas abruptas
controladas, sem leitura autenticada de uma ROM real nesta sessão.

## 0.1.16 — cadastro simples e operações isoladas

- Formulário novo mostra nome/plataforma; Drive, catálogo manual e ficha completa
  ficam recolhidos. Ao salvar, tenta identificar pelo nome/plataforma e completar
  ficha/imagens sem confirmação obrigatória. Sem resultado confiável, salva offline.
  Empates, plataformas incompatíveis e baixa semelhança não são associados.
- Baixar e adicionar à biblioteca no Drive cria o jogo/vínculo da ROM se necessário
  e inicia a obtenção das imagens depois de concluir/verificar o arquivo.
- Download e enriquecimento executam em auxiliares separados. Saída abrupta do
  auxiliar vira mensagem na janela; o cadastro e os arquivos são preservados.
  Não há mudança de OAuth, cofre, schema (4) ou exclusão remota.
- Respostas do Drive chegam a slots Qt do receptor; fechamento das janelas aguarda
  trabalhos ativos. Arte vertical SteamGridDB precede fallback da imagem RAWG.
- Provedores já configurados são reutilizados; não se pede chave por jogo. Campos
  indisponíveis na fonte permanecem vazios, sem inventar metadados ou logos.

O crash relatado durante ROM/capa no Windows não foi reproduzido nesta nuvem.
Foi validada a contenção: transferência controlada em processo real, interrupção
abrupta do auxiliar de imagens e da transferência; interface viva, download válido
preservado e arquivo parcial não publicado como ROM íntegra. Isso não comprova a
causa exata da queda original nem autenticação Drive real nesta sessão.

Validação Linux: 156 testes em 13,73 s (exit 0), depois 19 testes focados em 3,13 s
após proteção de fechamento/compactação. Últimos testes focados: 22 em 1,65 s, exit 0. Smoke das seis páginas + auxiliar real:
SQLite íntegro/schema 4/biblioteca vazia. Empacotador agora também testa o auxiliar
no executável extraído. Build Windows e publicação 0.1.16 ainda pendentes.

## Publicação confirmada — v0.1.15

Pré-release publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.15
Commit da release: 394e6b6847f723ba6077f75b588b6df9c63ed6aa.
Workflow 43210583534 concluído com sucesso: testes Windows, build do aplicativo e
atualizador, validação do ZIP extraído e publicação. ZIP Windows: 83.883.652 bytes;
SHA-256 afa756039eee0d7dd238c0c388a5dc331a270bd4e9278f264b386f43bb2b1cbe.
Esta confirmação prevalece sobre as notas de preparação abaixo. Acesso real às
fontes de metadados/imagens segue sem validação nesta nuvem (bloqueio do proxy).

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

Versão 0.1.16 de desenvolvimento. **O projeto completo não está concluído.**

## Atualização atual — importação Steam

Publicação Windows em preparação: workflow Actions e empacotador com validação
do executável extraído e SHA-256 foram adicionados. Actionlint e sintaxe Python
verificados localmente; build Windows e publicação só devem ser considerados
concluídos após confirmação da execução. API GitHub bloqueada pela rede vigente;
api.github.com foi acrescentado ao rascunho para permitir acompanhamento.

Correção posterior do Qt na mesma 0.1.14 de desenvolvimento: botões de arquivo do
GameDialog usam método do receptor em vez de lambdas que capturavam o diálogo.
Reprodução original e 16 testes afetados passaram. Uma execução completa confirmou
**136 aprovados em 9,62 s, exit 0**, sem falha nativa após o relatório. Smoke das seis
páginas com SQLite íntegro passou. Duas regressões novas: campo correto de cada
seletor de arquivo e encerramento real de subprocesso com formulários sem pai.
Não houve mudança de dependências, esquema ou funcionalidades Steam nesta correção.

Esta seção prevalece sobre notas históricas abaixo. Schema SQLite: 4. Configurações >
Steam oferece consulta assíncrona, marcação de jogos, associação explícita a cadastro
existente e atualização por AppID. Não associa por título. Importação preserva dados
pessoais; lixeira/conflitos bloqueiam o lote. Horas por conta e conquistas ficam
separadas das sessões e marcos pessoais. Conquistas são consultadas por jogo.

29 testes focados passaram com saída 0: Steam, migrações, biblioteca e UI existente.
API com transporte controlado, sem autenticação real. Smoke Linux 0.1.14 das seis
páginas, SQLite íntegro e diálogo Steam vazio aprovado. O SIGSEGV histórico associado
ao formulário Drive foi resolvido na correção posterior acima. Na etapa Steam não
foram repetidas suítes de saves, scanner Drive ou temas intactos. A execução completa
posterior foi necessária uma vez para verificar o encerramento compartilhado do Qt.

Cofre, API Steam autenticada e build Windows 0.1.14 ainda não validados/publicados.
Migração v3→v4 preserva dados e backup recuperável; executável 0.1.13 não aceita banco
novo. Consulte INTEGRATIONS.md para configuração e limitações.

## Resumo atual para continuidade

Leia `CONTINUITY.md` e `AGENTS.md` antes de retomar. Esta seção e a seção 0.1.13
prevalecem sobre notas históricas abaixo. Schema atual: 3; suíte da release: 120 testes.
OAuth/leitura real Drive e SteamGridDB com três tipos de arte foram validados; RAWG
autenticado, importação Steam, RA, preços automáticos e upload de saves permanecem pendentes.
O cadastro oferece pesquisa Drive, título do catálogo confirmado e artes sem recorte.

Preparação para independência do PC: adicionados `CONTINUITY.md`, `PRODUCT_VISION.md`,
`AGENTS.md` e `CLOUD_SETUP.md`, com requisitos, decisões, limitações e passos de preparação.
GitHub `main` atualizado pelo site autenticado com fonte 0.1.13, integrações, testes,
scripts Windows e documentação; estava em 0.1.5 apesar das Releases mais recentes.
Histórico remoto e tags existentes preservados; biblioteca e credenciais não foram enviadas.
Suíte repetida nesta preparação: 120 testes em 29,33 s, pytest result/exit 0.
Verificação de padrões comuns de segredos: zero ocorrências em 80 arquivos; não é auditoria completa.
Nesta conta, a listagem de ambientes Cloud retornou vazia. Login no Codex web concluído;
conector GitHub aguarda autorização. Nenhum ambiente/chat Cloud foi criado até esta
atualização. Instruções Linux ainda não executadas; preparação não é migração Cloud validada.

## Implementado e utilizável localmente

- Python/PySide6, dez paletas discretas (incluindo Branco claro), navegação persistente e estados vazios.
- Banco SQLite local com WAL, FKs, transações, três migrações, trava de instância, logs rotativos e backup consistente.
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

- 58 testes automatizados passaram na versão 0.1.5: domínio, SQLite/migração, saves/ZIP, clientes controlados, DAT, subprocessos, UI e regressões do atualizador. Consulta pública real à API GitHub passou sem credenciais; acesso privado autenticado ainda aguarda validação do usuário após a correção.
- Smoke pelo código fonte abriu as seis páginas e retornou integridade SQLite `ok`.
- Captura headless do início vazio foi inspecionada visualmente; tema/estado vazio legíveis.
- Executável PyInstaller x64 recompilado a partir do código final: smoke headless com saída 0, seis páginas abertas, schema 2, integridade SQLite `ok`, 0 jogos iniciais e log sem erros.
- A pasta portátil completa tem aproximadamente 249 MB antes de compactação. O pacote não depende do Python instalado para esse smoke; a validação foi feita no próprio host Windows do Codex, não em uma máquina limpa.
- Código versionado em repositório Git local próprio, sem remote configurado. Os arquivos ZIP de entrega e checksums ficam em outputs, fora do repositório de fontes.

## Pendências principais

1. Validar integrações reais e scanner em coleção grande; progresso/cancelamento, 410, shared drives, ordem complexa de alterações e retomada de downloads.
2. Validar perfis tradicionais de emuladores e implementar sincronização/versionamento/conflitos de saves no Drive. Backup local por jogo já possui disparo opcional ao término do registro de sessão; envio ao Drive continua pendente.
3. Steam: biblioteca, privacidade, horas e conquistas oficiais; RetroAchievements real; IGDB.
4. Preços automáticos regionais, histórico, menor preço, scheduler, limites e alertas. Atualmente só wishlist e meta local.
5. Launchers externos, processos filhos, detecção específica de encerramento de ROM e suspensão/pausa.
6. Editores completos de diário, anexos por entrada, galeria visual, conquistas e progresso estruturados.
7. Entidades normalizadas para plataformas/gêneros/categorias, repositórios dedicados e virtualização/paginação.
8. Validar atualizador com API privada real; assinatura, instalador, licenças de terceiros e testes limpos Windows 10/11.

## Problemas/limitações conhecidos

- Nenhum perfil de emulador/save real foi validado. Lista de extensões de save state bloqueadas não é universal; padrões devem selecionar somente saves tradicionais.
- O backup manual antigo das Configurações e alguns cálculos/leitura de listas são síncronos. Backups e restauração por jogo, varredura e rede usam workers.
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

Validar a consulta privada do atualizador 0.1.4 após o usuário salvar a credencial no aplicativo; não acessar o token pelo chat. Depois validar OAuth/RAWG/SteamGridDB em biblioteca isolada. A próxima implementação principal é o backup de saves no Drive com autorização separada, histórico remoto, integridade e conflitos. O ciclo local por jogo com workers já existe e o usuário confirmou backup/restauração. O ROADMAP.md preserva o escopo completo.

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

v0.1.4 publicada e verificada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.4 . Commit remoto 51d41d0fd1b6a00cb5f517091f5cc9d9924f26e7. SHA-256 do ZIP Windows exibido pelo GitHub confere com o arquivo local: 2869711edd9e9ee4a476110093b5c81e6f3aa75530fe658d368840fb35522946. Comprovante em outputs/github-checkpoint-014.png. Próxima validação: usuário salvar a credencial no aplicativo atualizado e repetir a consulta; a mensagem anterior não permite afirmar uma causa única. Esta anotação local é posterior à tag publicada.


## Checkpoint 0.1.5 — paletas de cores

Adicionadas dez paletas: Azul, Verde, Amarelo, Vermelho, Preto, Branco, Roxo, Rosa, Laranja e Ciano. Nove usam superfícies escuras com acentos dessaturados; Branco é claro, com fundos quentes e texto escuro. A preferência fica em Configurações > Aparência > Tema, é aplicada imediatamente e persiste no SQLite em appearance.theme. Verde continua como padrão para bibliotecas sem preferência; valores antigos/desconhecidos usam esse padrão.

As paletas alteram fundos, painéis, campos, textos, botões, seleção, foco, progresso, navegação, diálogos e cores de capas ausentes. A aplicação também define QPalette para controles do Qt. As artes e capturas originais não são recoloridas. Estados desabilitados recebem tratamento próprio. A moldura externa da janela e diálogos nativos de arquivos podem seguir as preferências do Windows.

Validação: 58 testes passaram em 12,82 s, incluindo contraste mínimo 4,5:1 dos pares de texto normal verificados nas dez paletas, troca imediata, navegação nas seis áreas em cada tema e reabertura do banco preservando a escolha. Isso não é uma auditoria completa de acessibilidade. Foram renderizadas as dez telas iniciais, e a comparação de paletas e o tema Branco foram inspecionados visualmente. Preferências e controles reais de DPI ainda precisam de validação humana no Windows.


Executável 0.1.5: smoke com preferência Branco previamente salva carregou a paleta clara e gerou captura com a cor de fundo esperada; saída 0 e preferência preservada. O auxiliar de atualização continuou passando no teste isolado de troca e preservação da versão anterior.

v0.1.5 publicada: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.5 . Commit remoto 48a69c1bd6cd7250ea80a70342c1d7606302f775. Sete Assets disponíveis (pacote Windows, fonte, checksums, informações de build, prévia e arquivos automáticos do GitHub). SHA-256 dos ZIPs exibidos pelo GitHub conferem com os arquivos locais. Pacote Windows: 8c4a3385488e40e5eba293ecedbb7180c57b548e3a1eb563829d4e255f7a22d8. A prévia comparativa está em outputs/Checkpoint-paletas.png e a confirmação da publicação em outputs/github-checkpoint-015.png. Esta anotação local é posterior à tag publicada.


## Diagnóstico de autenticação Drive — 10/11/2026

- Usuário configurou OAuth Desktop e conta de teste, e recebeu callback localhost real; o aplicativo 0.1.5 apresentou erro genérico após autorização. A conexão NÃO está validada.
- Log disponível confirma callback HTTP 200, mas não contém a exceção; causa ainda indeterminada. Não atribuir a pasta vazia, firewall ou cofre sem evidência.
- Código fonte agora distingue leitura de credencial, troca/renovação de token, gravação no cofre e inicialização do cliente; registra somente etapa e classe da exceção. Suprime URLs OAuth no logger da biblioteca e altera mensagem do navegador para não anunciar conexão antes da troca do token.
- Próximo passo: distribuir build com diagnóstico e repetir autenticação; não alterar permissões Google ou recriar JSON sem necessidade. Esta alteração ainda não está no executável 0.1.5 instalado pelo usuário.

Validação do diagnóstico: 61 testes automatizados passaram. OAuth real ainda depende de repetir o teste com esta versão.

Release 0.1.6 publicada em https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.6 como pre-release. Pacote Windows SHA256 286c184ed9e25f50bd6fc969969d7ab9aefff0859fb2a84121f114384a713c31; código fonte desta versão está no asset Checkpoint-0.1.6-source.zip (o tag remoto ainda aponta para o histórico anterior do envio pelo site). Smoke do executável exit 0, schema 2, integrity_check ok. Próximo passo: usuário atualizar e repetir autenticação para identificar a etapa de falha real.


## 0.1.7 — diagnóstico de rede Drive (11/11/2026)

- Classificação segura da cadeia de exceções: proxy, TLS, DNS, timeout, conexão recusada/interrompida e causa não informada. Não imprime mensagens, URLs privadas ou tokens.
- Botão Testar conexão faz GET HTTPS ao endpoint público de token sem código OAuth, JSON ou token; uma resposta HTTP não prova autenticação nem sucesso de POST OAuth.
- Troca inicial do código por token tem timeout de conexão 10 s e leitura 30 s; não repete automaticamente um código de uso único.
- Mantém verificação HTTPS e configurações de proxy do ambiente. Não desativa firewall nem altera certificados.
- 73 testes automatizados passaram. Teste público no ambiente de execução resultou em categoria proxy; o ambiente do aplicativo instalado pode usar configuração diferente. OAuth real segue pendente, sem afirmar correção da causa original.

Executável 0.1.7 final: smoke das seis páginas exit 0; banco isolado com integrity_check ok e schema 2.

Publicada 0.1.7: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.7 . Hash Windows conferido no GitHub: c54983d5287cecf96cfb607f48206a09767a8f61a53cfa10f91c929dff9986c3. Próximo passo: usuário executar Google Drive > Testar conexão na versão 0.1.7 e informar categoria; OAuth ainda não validado. Código completo está no asset source.zip; tag remoto mantém histórico anterior.


## 0.1.8 — transporte HTTPS (11/11/2026)
- Mensagens incluem cadeia de classes e códigos numéricos de erro, sem texto bruto de exceções ou URLs privadas. Identifica também acesso de rede recusado pelo sistema e encerramento sem resposta HTTP.
- Modo --network-test verifica endpoint público sem tokens e salva network-test.txt em --data-dir para comparar o executável ao Python. Não altera firewall ou certificados.
- Python com acesso de rede autorizado recebeu HTTP 404 do endpoint de token. Isso valida alcance HTTPS, não OAuth nem equivalência com a rede usada pelo usuário.


### Correção confirmada do pacote TLS — 0.1.8
O runtime Python do ambiente modifica SSLContext.__new__ para carregar codex-rejected-cas.pem. O empacotamento anterior omitia esse dado, causando ConnectionError > ProtocolError > FileNotFoundError(errno=2) em ssl.py:440. O build agora inclui o arquivo do próprio runtime, quando presente, em _internal. Não altera a política TLS nem desativa verificação. No executável local, incluir o arquivo mudou a falha reproduzida para resposta HTTPS HTTP 404 do endpoint público de token. Autenticação real com conta do usuário continua pendente. A versão corrige uma causa concreta de falha do transporte; outras restrições de rede podem existir.

Validação final 0.1.8: executável recompilado com dado TLS incluído automaticamente respondeu HTTPS HTTP 404 (network-test exit 0); smoke das seis páginas exit 0, schema 2 e integrity_check ok. 75 testes passaram; OAuth real aguarda usuário.

Publicada correção 0.1.8: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.8 . Windows SHA256 c353638a98904eeeceb542219f07f1039bc41b2d6c2fb0df163e45453fd206bc. Próximo passo: usuário atualizar (talvez download manual se o atualizador também falhar por HTTPS), Testar conexão e Autenticar com mesmo JSON. Não foi necessário alterar credenciais nem permissões.


## Validação real do Drive — 11/11/2026

- Usuário confirmou OAuth autenticado na interface 0.1.8 após correção do dado TLS do empacotamento.
- Executada varredura inicial autorizada na raiz fornecida pelo usuário: 2.147 ROMs registradas, zero downloads; integrity_check do banco real retornou ok.
- Criada cópia consistente do SQLite antes da operação na pasta backups dos dados locais.
- Controle Windows localizou a janela, mas captura/input falharam; operação realizada pelo mesmo serviço DriveScanner do código fonte, com token já salvo no cofre e sem ler/exibir seu conteúdo.
- Cursor de alterações e raiz persistidos. A lista da janela já aberta precisa ser recarregada fechando e reabrindo Google Drive.
- Download, associação a jogos e atualização incremental na coleção real seguem sem validação. Nenhum arquivo foi associado automaticamente a um jogo e nenhuma ROM foi baixada.


## 0.1.9 — reconhecimento de plataformas (11/11/2026)
Aliases explícitos para Nintendo Game Boy Advanced, Super Nintendo (SNES), Switch e variantes comuns, normalizando espaços e separadores. Não usa extensão compartilhada nem correspondência parcial; caminhos com plataformas contraditórias ficam para revisão. Botão Reconhecer plataformas preenche somente campos vazios usando caminhos locais, sem rede, downloads ou alteração de associações.
Validação: 85 testes passaram. Aplicado ao banco real após cópia consistente: 2.102 registros corrigidos; integridade ok; IDs, nomes originais, associações e disponibilidade preservados. Totais: GBA 1.098, SNES 986, DS 24, Switch 18, 3DS 15, PSP 3; três arquivos em Temas permanecem sem plataforma.

Usuário esclareceu que Temas contém temas de emulador, não jogos. A pasta raiz Temas agora é ignorada pelo scanner, incluindo ZIPs. Três registros sem associação/disponibilidade foram retirados do índice local após backup; nenhum arquivo Drive foi alterado. Coleção real: 2.144 ROMs, todas com plataforma identificada.

Publicada 0.1.9: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.9 . 86 testes passaram; executável final smoke exit 0; SQLite isolado integrity ok/schema 2; ZIPs íntegros. Banco real: 2.144 ROMs classificadas, Temas removido somente do índice. Atualizar app antes de próximas varreduras; fechar/reabrir Drive para recarregar lista já corrigida.


## 0.1.10 — pastas personalizadas e capas (11/11/2026)
- Aliases PS1/PSX, PS2, PS3, GameCube/NGC, Wii, N64, NES, Game Boy/Color, Mega Drive, Saturn e Dreamcast.
- Pastas e plataformas: associação por ID de pasta indexada, plataforma livre ou conhecida, herança por subpastas e prioridade da regra mais específica. Salvar/remover reclassifica o ramo existente, sem alterar jogos associados, nomes ou arquivos. Atualize o Drive para descobrir pastas novas; pastas vazias sem regra reconhecível permanecem para revisão. Regras persistem no SQLite; não são credenciais.
- Criar jogo desta ROM exige título confirmado e vincula a versão; outras versões podem ser associadas ao jogo existente. Não cria milhares de jogos nem mescla títulos automaticamente.
- Capa do jogo acessível pela lista Drive após associação; imagem local é validada e copiada ao cache sem chave. Busca SteamGridDB exige chave própria e confirmação do jogo/arte. Lista da biblioteca agora exibe miniaturas; lista Drive mostra capas de jogos associados.
- Scanner não fornece capas nem identifica títulos sozinho. Não houve download ou atribuição automática de artes na coleção real. Não foi necessário alterar credenciais.
- 97 testes passaram antes do ajuste final de atualização da galeria após fechar Drive; testes cobrem herança, regra específica, persistência, renomeação por ID, limites de ramo, validação, criação de jogo sem duplicar arquivo e ícone de capa na tabela.


## 0.1.11 — pesquisa no índice Drive (11/11/2026)
Pesquisa local por nome original, título do jogo associado e pasta; ignora caixa e acentos. Filtro de plataforma combinado, contador visível e estado vazio. Consulta caracteres como % e _ literalmente, sem transformar texto em SQL. Preserva a seleção pelo ID enquanto o arquivo permanecer visível; ações operam sobre a lista filtrada. Não consulta APIs nem baixa arquivos. Inclui todas as funções de pastas e capas da 0.1.10, publicada antes deste pedido.

Publicadas 0.1.10 (pastas/capas) e 0.1.11 (pesquisa): https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.11 . Executável 0.1.11 smoke exit 0; schema 2/integrity ok; ZIPs íntegros. Suíte exibiu 98 testes aprovados; teste focado de busca confirmou resultado 0. Busca conferida em leitura da coleção real: 2.144 itens, 27 resultados para pokemon, cerca de 245 ms para inicialização+primeira busca no ambiente. Nenhum dado real foi modificado no teste de busca. Estado de janela Drive e mapeamento renderizados e inspecionados. Próximo passo: usuário atualizar e testar busca, regras personalizadas e criação/associação/capa de jogo. Busca SteamGridDB com credencial real permanece pendente.


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

Publicada 0.1.12: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.12 . Executável final: smoke com banco novo e migração v2→v3 exit 0; integridade ok, capa personalizada preservada e backup v2 verificado. ZIPs íntegros. 111 testes passaram com pytest result 0. Banco real não foi migrado por esta sessão; migração ocorrerá ao atualizar e abrir a nova versão. Próximo passo: configurar chave SteamGridDB no aplicativo e validar consulta/seleção real de um jogo e os três tipos de arte. Nenhuma chave real SteamGridDB disponível; não declarar integração autenticada validada.


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

Publicada 0.1.13: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.13 . Executável final smoke exit 0; SQLite integrity ok/schema 3; ZIPs íntegros. 120 testes passaram com pytest result 0. Fonte completa no asset source.zip; tag remoto ainda aponta ao histórico anterior do upload pelo site. Próximo teste do usuário: Adicionar jogo > pesquisar ROM > Usar ROM selecionada > confirmar título no catálogo > Salvar. Capas/banners preservam imagem completa em quadros uniformes. Quatro títulos reais já padronizados com backup e IDs confirmados. RAWG autenticado permanece pendente.

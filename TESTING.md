# Validação

## Publicação confirmada — v0.1.27

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.27
Fonte da tag: `6fad7bfa278d0cb2897588a7965d545c98fcdacf`.
Workflow Windows release `43357748311`: completed/success.
Windows/Python 3.12.10: **225 testes aprovados em 183,59 s**, zero falhas/erros/skips.
Fonte e ZIP extraído: seis páginas, auxiliar, cadastro com imagem/SQLite e
integridade aprovados; CheckpointUpdater.exe --check retornou 0.
65 capturas Qt Windows geradas. Inspecionadas as páginas principais, conexões,
perfil e lista Steam de 300 jogos; dados/artes dessas capturas são fixtures.
Logos públicas reais também foram conferidas em biblioteca Linux isolada.
Não equivale a autenticação de serviços nem aprovação estética do usuário.

ZIP Windows: 84.082.193 bytes; SHA-256
`8cf3e0c97c81f5962e3380c630fa3135a30c54c57a6766891e2d5bdba7af4768`.
ZIP visual: 4.583.748 bytes; SHA-256
`c3f8c1aafa31bbe7394b9988b6354ba81e1b397f4a3bc6159b7b8a568fb9824f`.
Hash do ZIP visual baixado coincide com o digest GitHub; o hash Windows no
relatório do empacotador coincide com o asset publicado. Tags antigas preservadas.


## 0.1.27 — visibilidade final do cadastro

A primeira execução Windows barrou publicação: o caso de 300 jogos excedeu a
espera de 10 s, com 224 outros testes aprovados. Ajustada somente a tolerância
de espera para 60 s; mantidas as verificações de rolagem, tamanho e resumo.

14 testes focados passaram em 13,79 s após restringir Adicionar jogo a Início
e Biblioteca. Suíte completa anterior de perfil/Steam/Desejos: 225 testes Linux
aprovados em 131,98 s. Windows validará novamente o commit final integralmente.

## 0.1.26 — pedidos adicionais

Regressões para atualização automática da logo na wishlist, não repetição de
consulta na sessão, importação Steam de 300 jogos com tamanho estável e resumo
de uma linha; cadastro global adiciona posse mesmo ao partir de Desejos.
Perfil verifica foto em cache local, original preservado, apelido persistente,
cancelamento, remoção da foto e manutenção ao trocar tema/reabrir janela.
36 testes focados passaram após a implementação do perfil. Suíte Linux completa:
225 aprovados em 131,98 s, exit 0. Pacote Windows aguarda workflow separado.

## 0.1.25 — correções de composição e navegação

Linux: suíte completa com Qt offscreen, 221 testes aprovados em 133,17 s.
Após os ajustes finais de calendário/disclosures, 27 testes focados aprovados
em 47,71 s. Smokes das seis páginas e cadastro com auxiliar, imagem e SQLite
passaram. Capturas reais geradas/inspecionadas em 1000, 1100 e 1920 px, incluindo
artes públicas Steam somente em uma biblioteca isolada, estados vazios e temas.
Não comprova integração autenticada nem validação Windows; resultado Windows
será registrado separadamente após o workflow da nova versão.

## Publicação confirmada — v0.1.24 — 13/11/2026

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.24
Commit da tag: `425dd12ab7571b1bdc236321ef952d3eeff0c2d7`.
Workflow [43347929302](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43347929302)
concluído com sucesso em build e publicação. Pre-release publicada com oito assets.

Windows/Python 3.12.10: **216 testes aprovados em 94,04 s**, zero falhas/erros/skips.
Build do aplicativo e atualizador; smokes das seis páginas, auxiliar isolado,
cadastro com imagem/SQLite e integridade do banco passaram no fonte e no ZIP
extraído. `CheckpointUpdater.exe --check` retornou 0. Revisão automatizada gerou
48 capturas Qt e índice HTML com fixtures isoladas, sem dados pessoais.

ZIP Windows: 84.074.384 bytes; SHA-256
`fe66f68d334689dff5fbcd315d2a9dc249ea5167dda879107f7b303b7ef7290e`.
O digest publicado pelo GitHub coincide com o registrado pelo empacotamento.
ZIP visual: 3.255.466 bytes; SHA-256
`3b3ff0e76c55a20e37e0206501695e681f0253b8bb0019b365aa9519eae37093`.

Esta confirmação substitui a pendência de publicação na preparação abaixo.
A versão publicada é 0.1.24; a fonte da continuidade permanece na branch
`codex/design-fidelity-pt-br`, sem merge em `main` ou alteração de tags antigas.
Não equivale a aprovação estética, inspeção manual de todas as novas capturas,
sessão autenticada ou homologação interativa/DPI Windows 10/11.
Schema 4 e dados pessoais preservados; monitoramento/alertas de preços,
cobertura integral PT-BR e demais itens de ROADMAP continuam pendentes.

## Preparação da publicação 0.1.24 — 13/11/2026

Publicação solicitada para a continuidade implementada em `5d33629` e documentada
em `3f6ae049`, na branch `codex/design-fidelity-pt-br`. Versão do projeto e do
aplicativo atualizadas em conjunto para 0.1.24; notas da release refletem Biblioteca
vertical, wishlist com logos/preços, nove temas escuros, calendário e localização PT-BR.
O workflow Windows release passa a aceitar esta branch e publicará a pre-release
somente após os testes, build, smokes e revisão visual automatizada.

A validação anterior de 216 testes Windows refere-se à fonte `5d33629`.
Os resultados do novo pacote 0.1.24 ainda precisam ser observados no workflow;
esta preparação não declara publicação, aprovação estética ou teste autenticado.
`main`, tags existentes, schema 4 e dados pessoais permanecem preservados.

## Publicação confirmada — v0.1.19

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.19
Commit: 6ab43bfb2cf60a96d48a864af722b3ea7cd5b529; workflow 43259509483 success.
Relatório confirma 177 testes Windows sem falhas/erros/skips; smokes das seis
páginas, auxiliar, cadastro com imagem/SQLite e atualizador do ZIP aprovados.
ZIP Windows: 83.912.188 bytes; SHA-256
353d6c7e40b1571019c1b46503b0f4855741cb688ea815773a94048cf6aec5b1.
A confirmação prevalece sobre as pendências abaixo. A fidelidade visual continua
sendo avaliada pelo usuário. O banner panorâmico não foi baixado do CDN nesta
nuvem: proxy CONNECT 403; contratos/fallback/proteção manual usam testes controlados.

## 0.1.19 — fidelidade visual e banner Steam

O usuário rejeitou a fidelidade visual da 0.1.18; os mockups aprovados continuam
sendo a referência, sem considerar testes funcionais como aprovação estética.
A biblioteca agora usa delegate próprio com cards, título/status alinhados e grade
responsiva; a busca foi para o cabeçalho. Início reorganizado com continuidade e
atividade lado a lado. Hero arredondado, altura proporcional ao banner e arte
principal inteira; ficha com barra de ações e informações secundárias recolhidas.
Tipografia, superfícies, controles e ícones das conexões revistos. Barra de título
nativa solicita o tema escuro no Windows compatível, sem remover controles do SO.

Steam passa a priorizar library_hero.jpg; header da loja é fallback. Cabeçalhos
antigos são substituíveis somente com proveniência Steam, caminho/hash intactos e
identidade correspondente. Abertura da ficha tenta uma vez por sessão, respeitando
a automação. Confirmação manual de arte invalida a proveniência automática.
Alteração manual durante download prevalece; cache antigo permanece preservado.

Validação Linux: 177 testes em 40,09 s, exit 0; após ajustar proporções, 12 focados
em 6,17 s, exit 0. Smokes de páginas, auxiliar e cadastro com imagem/SQLite passaram.
Capturas reais com fixtures isoladas em 1440×980/1000×700; sem dados pessoais.
Probe do hero Steam: CONNECT bloqueado pelo proxy HTTP 403 (curl 56, HTTP 000).
Seleção/fallback/upgrade testados com transporte controlado, não download real.
Schema permanece 4. Build/publicação Windows 0.1.19 dependem do workflow.

## Publicação confirmada — v0.1.18

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.18
Commit: a8c6d413ae87acc839cb145e270a7c3442a4ed78; workflow 43253229490 success.
Relatório confirma 170 testes Windows sem falhas/erros/skips, seis páginas,
auxiliar e cadastro completo com imagem/SQLite no fonte e no EXE extraído,
além de CheckpointUpdater --check. Novo ícone incluído no build Windows.
ZIP: 83.897.043 bytes; SHA-256
b53161b73324e0180043f6e897c49b96a5ac88e093d5a88aeb97edc1a165b924.
Essa confirmação prevalece sobre pendências de publicação abaixo. As fixtures
não comprovam autenticação de contas; dados pessoais não foram acessados.

## 0.1.18 — interface e identidade aprovadas

Implementados Início em feed pessoal, biblioteca limpa com abas/filtros recolhidos,
ficha com banner/logo (sem capa repetida) e abas, cadastro por origem e Configurações
compactas em quatro seções. Identidade C// e checkpo//nt vetorial, com 18 px lógicos
entre símbolo e nome; ícone multirresolução também no executável Windows.
Mantidos os dez temas, dados/arquivos, schema 4 e salvamento em segundo plano.
Configuração de conexão não é apresentada como autenticação confirmada.
Rascunho do diário e aba da ficha são preservados ao atualizar artes.

Validação Linux: 169 testes em 25,14 s, exit 0; após o ajuste de rascunho/rotas,
18 testes focados em 4,78 s, exit 0. Smoke seis páginas, auxiliar e cadastro com
imagem/SQLite aprovados. Prévias reais da interface renderizadas em 1440×980 e
1000×700, com fixtures isoladas, incluindo tema branco. ICO gerado localmente.
Sem acesso a biblioteca pessoal ou credenciais. Build/publicação Windows 0.1.18
pendentes do workflow. Direção visual detalhada em DESIGN.md.

## Publicação confirmada — v0.1.17

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.17
Commit: 1b09d84445f12582d4a2bd3ae21c92bb8c4c563b; workflow 43217720788 success.
Relatório da release confirma 164 testes Windows sem falhas/erros/skips e smoke
completo de salvar, auxiliar, imagem e SQLite no fonte e no EXE extraído do ZIP,
além das seis páginas e CheckpointUpdater --check. Fixtures isoladas, sem contas reais.
ZIP Windows: 83.900.366 bytes; SHA-256
51b10ee94fa3765d5cbe95c4b515b4174fa1f9c569dcbf43406eb1a70fce896a.
Essa confirmação prevalece sobre as pendências de publicação abaixo. A reprodução
Linux do salvamento falhava com 139 antes da alteração e agora encerra com 0.

## 0.1.17 — queda reproduzida no salvamento

Reproduzida no Linux uma falha nativa do fluxo completo 0.1.16: SIGSEGV/exit 139
na abertura de ArtworkProgress.exec após AutomaticLookup.exec dentro de Salvar.
Reproduzida também sem baixar/decodificar imagens. Ao remover o encadeamento modal,
a mesma sequência concluiu cadastro, imagens e encerramento com exit 0.

Salvar agora persiste o cadastro imediatamente. Identificação/ficha/imagens seguem
em fila sequencial em segundo plano, com indicador na barra inferior e opção de
parar após o jogo atual. O formulário não abre outro carregamento modal.
Drive, edição identificada e preenchimento em lote também não abrem esse segundo
loop modal. Mantidos processos auxiliares, preferências e proteção de dados.
Schema permanece 4; nenhuma credencial ou biblioteca pessoal foi lida nesta correção.

Validação local: **164 testes em 20,33 s, exit 0**. Novas regressões executam processos
Qt completos para salvar com PNG/cache/SQLite, falha do auxiliar e criação pelo Drive.
Smoke das seis páginas e smoke completo de cadastro + auxiliar passaram, exit 0.
O empacotador agora exige esse fluxo também no EXE extraído do ZIP. Diagnóstico
nativo também fica habilitado na interface; não registra variáveis locais/segredos.
Evidência: evidence/save-modal-crash.txt. Fontes/transferências são controladas nos
testes; não se trata de validação de conta autenticada ou diagnóstico do Windows
pessoal. Build/publicação 0.1.17 ainda dependem do workflow.

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

## 0.1.15 — preenchimento de ficha e imagens

Validação Linux desta mudança: suíte completa **146 aprovados em 14,99 s, exit 0**;
52 testes focados passaram anteriormente em 3,10 s. Smoke em diretório novo:
seis páginas, exit 0, SQLite integrity=ok, schema 4, zero jogos.
Probes à loja Steam e CDN foram bloqueados pelo proxy (CONNECT HTTP 403);
contratos testados com respostas controladas, sem validar download real, Windows
ou autenticação. Nenhuma credencial foi lida ou exposta pela sessão.

```sh
QT_QPA_PLATFORM=offscreen XDG_CACHE_HOME=/workspace/work/qt-cache .venv/bin/python -m pytest tests -q -p no:cacheprovider
QT_QPA_PLATFORM=offscreen XDG_CACHE_HOME=/workspace/work/qt-cache .venv/bin/python -m gamevault.app --smoke-test --data-dir /workspace/work/checkpoint-0115-smoke-CrnYuU
```

Dez regressões novas cobrem parsing da ficha pública por AppID, identidade errada,
preenchimento de vazios, preservação de dados pessoais e edições concorrentes,
falha de download, catálogo RAWG para ROM, identificação ao salvar e cancelamento.
Testes existentes de importação Steam verificam também o preenchimento assíncrono.

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

## Revisão 0.1.20

185 testes Linux em 33,42 s, sem falhas. Novos casos cobrem restauração,
cadastro novo preservando lixeira, rollback, identidade não roubada, proporção
do banner, indicador compacto e estatísticas derivadas da base. Smokes isolados
de páginas/auxiliar/cadastro aprovados. Windows depende do workflow da release.

Windows 0.1.20 confirmado: workflow 43265226500 success, 185 testes sem
falhas/erros/skips, smokes de fonte e executável extraído aprovados. Relatório
publicado como Checkpoint-0.1.20-validation.txt na release v0.1.20.

## Busca única 0.1.21

192 testes Linux em 39,54 s com Qt offscreen. Casos cobrem busca única,
complementação entre provedores, indisponibilidade parcial, plataforma console,
preenchimento sem etapa avançada, resposta atrasada e preservação da ROM.
Capturas reais com fixtures isoladas; smokes de páginas/auxiliar/cadastro passaram.
Consulta pública Steam nesta nuvem: indisponível (URLError/OSError). Testes de
integração do catálogo usam provedores controlados, não contas autenticadas.

Windows 0.1.21 confirmado: workflow 43272087982 success, 192 testes sem
falhas/erros/skips. Smokes do fonte e do ZIP extraído e atualizador aprovados.
Relatório Checkpoint-0.1.21-validation.txt publicado na release v0.1.21.

## Revisão completa 0.1.22

Novos casos verificam metas e retirada de desejos sem perda de jogos, exclusão
de removidos das memórias, editor em abas preservando valores/imagens, favoritos
preservando rascunhos, header/grade na janela mínima, temas/perfil e encerramento
de diálogo independente com consulta ativa em subprocesso. A rodada final
passou com 199 testes em 73,65 s, exit 0, sem abort nativo. Windows pendente neste registro.
Smokes de páginas, auxiliar e cadastro com imagem/SQLite passaram isoladamente.
37 capturas em scripts/render_ui_review.py cobrem seis páginas, abas, diálogos,
proporções mistas e janelas/temas diferentes. São fixtures, não APIs autenticadas.

A revisão visual 0.1.22 revelou falta de fonte nos PNGs offscreen Windows,
apesar dos 199 testes passarem. A 0.1.23 registra Segoe UI explicitamente e
verifica glifos em português antes de renderizar; capturas exigem inspeção visual.

Windows 0.1.23 confirmado: workflow 43279071033 success, 199 testes sem
falhas/erros/skips e smokes aprovados. Capturas com fonte corrigida produzidas e
PNG de Início/Biblioteca/Aparência inspecionados. ZIP visual possui 37 capturas
e hash conferido; nenhum banco/log foi incluído. Resultado visual continua
aberto a ajustes do usuário, sem confundir sucesso funcional com aprovação estética.

## Continuidade após v0.1.23 — 12/11/2026

Estado final: nove temas escuros (modo claro removido), Biblioteca vertical com
capas ampliadas e legendas alinhadas, wishlist quadrada com logos e ações na mesma
linha, calendário diário, PT-BR/datas e preços públicos BRL. A opção de Biblioteca
quadrada foi descartada pelo usuário; não deve ser reintroduzida por esta revisão.

Validação Linux final: **216 testes aprovados em 93,36 s, exit 0**, sem abort nativo:

```sh
QT_QPA_PLATFORM=offscreen .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider -o faulthandler_timeout=90
```

Smokes executados via `scripts.package_windows_release.smoke` e `save_smoke`, com
`sys.executable -m gamevault.app` e diretórios novos sob `work/`: seis páginas,
integridade/schema SQLite, auxiliar `ping`, assets oficiais presentes e cadastro
com imagem/SQLite aprovados. Nunca abriram a biblioteca pessoal. O wheel foi
construído e inspecionado: contém os módulos e assets necessários, sem base/logs.
Isso não equivale a empacotamento ou homologação Windows.

`scripts/render_ui_review.py work/review-dark-final --art-dir work/reference-art
--prices-file work/prices-for-review.json` gerou 48 capturas Qt, incluindo verde,
roxo/azul, janelas 1100×740 e 1000×700, abas, diálogos, calendário e wishlist.
Dados de jogos/sessões são fixtures; os arquivos opcionais trazem artes/snapshot
públicos para revisão, sem autenticação de conta. O empacotador inclui somente
capturas/índice, sem bases/logs. Inspeção visual Linux não é aprovação estética.

Consultas públicas reais, separadas dos testes com transportes substituídos:
Steam Store retornou descrição PT de Hollow Knight e data ISO 2017-02-24;
MediaWiki retornou descrição PT de The Minish Cap para Game Boy Advance;
GG.deals BR retornou Hollow Knight, mínimo R$ 46,99, lojas oficiais R$ 46,99 e
keyshops R$ 47,46, com 11 ofertas carregadas e links originais. Esses valores são
um snapshot da consulta, não promessa de preço futuro nem validação autenticada.
Nenhum segredo foi lido. SteamGridDB/RAWG autenticados e cofre Windows não foram
validados nesta nuvem.

O novo workflow `Windows UI validation` valida PRs sem publicar releases ou tags.
## Validação Windows desta revisão — 12/11/2026

Fonte validada: `5d33629`; workflow [43326388407](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43326388407), concluído com sucesso.
Windows/Python 3.12.10: **216 testes, zero falhas/erros/skips**, 125,089 s.
Build do aplicativo e atualizador, seis páginas, auxiliar isolado, cadastro com
imagem/SQLite e integridade do banco passaram na origem e no executável extraído.
`CheckpointUpdater.exe --check` retornou 0. Artefato de revisão contém pacote
Windows e 48 capturas Qt com fixtures; Biblioteca, Desejos e Estatísticas foram
inspecionados. Não equivale a aprovação estética, sessão autenticada ou homologação
interativa de DPI em Windows 10/11. Nenhuma release/tag foi publicada.
ZIP Windows SHA-256: `72157494dfbc9d68996b82ad45cf0bb4c3de9961573a8d8addae1ece0f215729`.
ZIP visual SHA-256: `838d68435a16d5aaa74863551cd81ce5d420ad79ca2c1aeb4ec3fdf1ce3b20af`.

# Continuidade do Checkpoint

## Correções após rejeição visual da 0.1.24

Usuário rejeitou a composição da release e reenviou as referências aprovadas.
Banner limitado a 220–300 px, preservando proporção da imagem; colunas do feed
reequilibradas, grade com dimensões limitadas e legendas junto à arte visível.
Atalho Adicionar jogo restaurado na lateral. Busca do Início abre resultados
na Biblioteca ao digitar. Estado vazio reserva espaço para a descrição completa.
Capturas Linux isoladas geradas e inspecionadas; isso não valida Windows/DPI.
Design completo ainda não aprovado. Preservar banco/schema e proteções dos auxiliares.

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

## Decisões finais desta continuidade — 12/11/2026

- Modo claro removido por pedido expresso posterior do usuário. Permanecem nove
  temas escuros e as preferências de cor existentes. Uma preferência legada `white`
  passa para Verde ao abrir; dados da biblioteca não são alterados. Esta decisão
  substitui os registros históricos de dez temas/tema Branco abaixo.

- O usuário descartou o modo quadrado da **Biblioteca** porque não há garantia de
  artes quadradas estáticas para todos os jogos. A Biblioteca mantém o formato
  vertical com área ampliada para o pôster e as imagens inteiras, sem corte/deformação. Não há seletor de formato
  quadrado nem obtenção paralela de artes quadradas nesta entrega.
- **Wishlist:** cards quadrados com logos estáticas, proporção preservada, mesma
  área de apresentação, título de uma linha, preço e ações alinhados. Ver ofertas, + e lixeira
  ficam na mesma linha; logos maiores sem fundo preto próprio. Sem logo,
  usa placeholder discreto e o título normal; não estica texto nem improvisa uma logo.
- **Horas de jogo:** calendário diário no estilo GitHub, com intensidade e tooltip
  de data/duração, últimos 12 meses ou ano escolhido. Usa sessões reais em UTC.
- Retirada a repetição do nome do serviço dos textos de preço. Os botões de ofertas
  continuam abrindo a comparação completa, com links originais preservados.
- Downloads/cadastro de artes recusam GIFs e animações. Os vídeos pessoais em
  Memórias continuam disponíveis; essa regra se refere às artes do jogo.

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

## Continuidade de design e PT-BR — revisão em 12/11/2026

Esta revisão parte de `codex/steam-library-import` em `d23439d`, árvore inicialmente
limpa. Implementação em `codex/design-fidelity-pt-br`, para revisão contra a branch
de desenvolvimento. `main`, tags e releases existentes foram preservadas. A versão
publicada continua v0.1.23. Esta revisão não declara o design aprovado/concluído.
As imagens anexadas pelo usuário continuam sendo a especificação visual; os
registros históricos de “interface completa” abaixo não representam sua aprovação.

- Shell e cabeçalhos compactados; Início mantém continuidade/atividade lado a lado
  em 1000 px; Biblioteca agrupa filtros sem perder lista, ordenação ou favoritos.
  Cadastro passa a diálogo compacto com Pesquisar jogo / ROM do Drive / Steam,
  sugestão em linha e configurações opcionais. Busca/enriquecimento continuam isolados.
- Ícones Steam e Drive são arquivos oficiais, sem redesenho. Incluídos nos dados do
  pacote Python e PyInstaller; origem em THIRD_PARTY_NOTICES.md. O smoke verifica assets.
- Biblioteca vertical com capas inteiras; wishlist em cards quadrados com logos,
  sem texto espremido e com preço/ações em posições comuns. O modo quadrado da
  Biblioteca foi descartado por decisão explícita do usuário, conforme nota acima.
- Steam solicita `brazilian`; datas localizadas da fonte são normalizadas em ISO.
  Ficha/editor/catálogos exibem DD/MM/AAAA; SQLite e contratos permanecem ISO.
  Publicadora, origem, categoria e nota existentes ficam sempre visíveis na ficha.
- ROMs com identidade confirmada podem obter texto PT da Wikipédia quando há artigo
  exato, plataforma compatível e tradução. Desambiguação, remake/ano incompatível e
  ausência de PT não são associados. Fonte/licença ficam visíveis; hash de texto
  protege edições locais. Inglês legado da Steam/RAWG só é substituído com comprovação
  de que ainda coincide com a fonte automática. Sem tradução disponível não há texto
  inventado nem promessa de cobertura integral. Fontes existentes são preservadas.
- Desejos não exibem status de progresso e não contam como coleção possuída nas
  estatísticas/Início/Biblioteca. “Adicionar à biblioteca” confirma aquisição.
  Retirar dos desejos preserva o cadastro como não possuído, recuperável em Dados e
  backup > Desejos removidos. Notas, histórico, status legado, artes e arquivos não
  são apagados. O campo legado de meta de preço é preservado no banco, sem uso na UI.
- Desejos mostra **menor preço atual do GG.deals**, não meta pessoal. A ficha apresenta
  lojas oficiais/keyshops, ofertas carregadas e links originais; botão abre a página
  brasileira com a comparação completa. Usa página pública BR identificada pelo
  redirecionamento oficial de AppID, moeda BRL verificada, cache de uma hora e fila
  espaçada em 6,5 s. Não precisa de chave de API. Falha não vira R$ 0: sinaliza
  indisponibilidade/valor salvo e mantém link e última consulta. Lista local pode ser
  parcial; todas as ofertas ficam acessíveis no GG.deals. Sem AppID/página confirmada,
  oferece pesquisa no site sem presumir uma associação.
- Estatísticas passam a calendário diário com intensidade e distribuição por barras,
  sem pizza; sessões/períodos ausentes recebem zero no intervalo apresentado.
  Totais continuam derivados do SQLite e horas Steam não duplicam sessões locais.

Schema permanece 4. Nenhum banco pessoal, ROM, save, nota, credencial ou log privado
foi lido, copiado ou versionado. Regressões cobrem edição manual, versão de ROM,
origens do cadastro, datas, wishlist/posse, formatos e cache/preços em BRL.
Windows tem workflow de validação de PR separado da publicação de releases.
Resultados efetivos e limitações estão em TESTING.md e evidence/design-ptbr-validation.txt.

## Publicação confirmada — v0.1.23

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.23
Commit: faa60825bcb5fcfa09f443c7926616aba2bb070c; workflow 43279071033 success.
Relatório: 199 testes Windows, zero falhas/erros/skips; seis páginas, auxiliar,
cadastro com imagem/SQLite no fonte e ZIP extraído e atualizador aprovados.
ZIP Windows: 83.984.000 bytes; SHA-256
 a38a093efc96aa55acecad89a2b8a9a5ae498108a491d1fbf656a9a47af2a16e.
Revisão visual: 37 PNGs Qt Windows + index.html; ZIP 2.964.823 bytes; SHA-256
8b702d4eabafdaa53e209f1a3163402b7b9728865728c6866439f63cc9631936.
Hash do ZIP visual conferido em leitura. Início, Biblioteca e Aparência Windows
abertos e inspecionados: textos legíveis, sem quadrados após registro das fontes.
Capturas usam fixtures; não representam contas autenticadas nem dados pessoais.
A publicação substitui as pendências abaixo; releases anteriores foram preservadas.


## 0.1.23 — fontes e revisão Windows verificável

A 0.1.22 foi publicada no commit 39da4e198a2226d82ae90a657c1f1696cb1afa16,
workflow 43278032123 success, 199 testes Windows e smokes aprovados. Ao abrir
os PNGs publicados, foi encontrada fonte ausente no Qt offscreen (quadrados).
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


## Publicação confirmada — v0.1.21

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.21
Commit: e479f87b97dc507b5686f7e0406441a50da56f66; workflow 43272087982 success.
Relatório: 192 testes Windows, zero falhas/erros/skips. Smokes de seis páginas,
auxiliar, cadastro completo com imagem e SQLite no fonte e ZIP extraído aprovados;
CheckpointUpdater.exe --check saiu com 0. ZIP Windows: 83.953.182 bytes; SHA-256
3c5f159048f9ee4584b4679b4559a81260326604b64d1c9669fbbabd55b3852b.
Essa confirmação prevalece sobre as pendências abaixo. A avaliação visual pelo
usuário e testes autenticados continuam distintos da validação automatizada.


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


## Publicação confirmada — v0.1.20

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.20
Commit: d40439f23047a76d6424d2c49b7578f37c9387d6; workflow 43265226500 success.
Relatório confirma 185 testes Windows, zero falhas/erros/skips. Smokes das seis
páginas no fonte e ZIP extraído, auxiliar isolado, cadastro com imagem/SQLite e
CheckpointUpdater.exe --check aprovados. ZIP: 83.927.939 bytes; SHA-256
3a6f83d83bf497dce0d944bb20c63625bcb80f0cc0c9fde0c0bd5dea54386670.
Essa confirmação prevalece sobre as pendências abaixo. Testes isolados não
comprovam integrações autenticadas nem aprovação visual do usuário.


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

Estado de referência: aplicativo 0.1.19 de desenvolvimento, schema SQLite 4.
Este documento transfere o contexto de trabalho; não é uma cópia integral do chat.
Não contém credenciais, dados pessoais da biblioteca ou autorizações para novos acessos.

## Atualização mais recente — encerramento Qt corrigido

Publicação solicitada posteriormente: preparado workflow Windows em
`.github/workflows/windows-release.yml` e empacotador que valida o ZIP extraído,
smoke, SQLite, auxiliar, checksum e limite do atualizador antes da pré-release.
Validadores locais: actionlint 1.7.7 (checksum oficial conferido) e compilação
Python; isso não comprova execução Windows. O acesso à API GitHub foi recusado
pela política atual; api.github.com foi adicionado ao rascunho de rede, ainda
dependente de aplicação. Não declarar Release publicada sem observar o resultado.

- Reproduzida a falha nativa em GameDialog sem janela pai: lambdas conectadas aos
  botões de arquivo capturavam o diálogo até o encerramento do PySide6.
- Substituídas por método do receptor Qt e propriedade que identifica o campo.
  Não mudados PySide6, credenciais, banco, migrações ou comportamento de cadastro.
- Regressões novas somente para os quatro seletores de arquivo e saída real de
  subprocesso que cria/fecha formulários sem pai. Nenhuma asserção antiga removida.
- Teste original passou com exit 0; 16 testes afetados aprovados; uma única execução
  completa confirmou 136 aprovados em 9,62 s, exit 0. Smoke: seis páginas e SQLite ok.
- Para futuras mudanças, voltar à validação por impacto; não repetir suíte completa
  sem alteração ou risco novo. Evidência em evidence/cloud-qt-shutdown.txt.
- Continuação na branch codex/steam-library-import; Steam autenticada e executável
  Windows continuam pendentes. O defeito de encerramento Linux deixou de bloquear.

## Atualização anterior — importação Steam

- Implementado em Configurações > Steam: chave no cofre Windows, SteamID64,
  consulta em worker, seleção explícita, associação manual a cadastro existente,
  importação por AppID e conquistas por jogo sob demanda.
- Horas/conquistas são snapshots por conta, separados das sessões/marcos pessoais.
  Reimportar preserva título pessoal, notas, status e artes. Lixeira e conflitos
  bloqueiam a transação inteira. Não associar automaticamente por nome.
- Migração 4 cria steam_owned_games e steam_achievements, com backup recuperável.
  Executável 0.1.13 não aceita banco migrado; não reabrir com versão antiga.
- 29 testes focados passaram, exit 0: Steam, migrações, biblioteca e UI existente.
  Contratos Steam usam transporte controlado; não são conta autenticada.
  Pedido do usuário: não criar/repetir testes de áreas intactas sem motivo.
- Smoke 0.1.14 aprovado: seis páginas, SQLite íntegro e diálogo Steam vazio.
- A suíte histórica tinha SIGSEGV ao encerrar o teste do formulário Drive;
  resolvido na correção posterior descrita acima.
- Nenhuma chave Steam disponível nesta nuvem. API autenticada, cofre e build
  Windows 0.1.14 não foram validados. Nenhum pacote ou Release foi publicado.
- Domínios partner.steamgames.com e api.steampowered.com salvos no rascunho da rede;
  o acesso ao primeiro foi recusado pela política atual. Rascunho não é aplicação
  de política nem publicação de snapshot.
- Próximo: validar Steam autenticada em dados isolados quando houver acesso
  e seguir prioridades conforme escopo. Encerramento Qt já corrigido acima.

## Objetivo e forma de trabalhar

Construir uma central pessoal de jogos Windows 10/11, funcional e offline: biblioteca
de PC/Steam/outros launchers e emuladores, ROMs no Drive, execução, sessões, estatísticas,
diário, capturas/vídeos, conquistas, desejos/preços e backup de saves tradicionais.
O usuário quer continuar o desenvolvimento de qualquer dispositivo pelo Codex Cloud,
sem manter este computador ligado. O aplicativo continua sendo desktop, não um site.
Não reduzir o produto a protótipo ou anunciar funcionalidades não implementadas.

O usuário prefere ação, testes autônomos e comunicação direta em português brasileiro.
Não quer instalações de ferramentas pessoais para simplesmente enviar mudanças ao GitHub.
O projeto começou do zero; reaproveite seu próprio código existente, não substitua por
um projeto de terceiros. A visão original e prioridades estão em `PRODUCT_VISION.md`.

## Decisões aceitas

- Nome público Checkpoint (antes GameVault). Não renomear pacote/cofre/base legados sem
  migração explícita, pois a biblioteca existente precisa continuar abrindo.
- Python >=3.12, PySide6 6.8.3, SQLite direto com migrações e transações. Sem SQLAlchemy
  por enquanto. Banco local, serviços modulares e APIs por provedores.
- Visual editorial, minimalista, escuro por padrão; sem frases promocionais sob títulos.
  Dez temas discretos: azul, verde, amarelo, vermelho, preto, branco, roxo, rosa, laranja e ciano.
- Capas uniformes em 3:4, imagem inteira centralizada e margens discretas. Banners também
  mostram a arte inteira. Nunca deformar nem cortar logos/textos; cache preserva o original.
- Título exibido deve ser o título original do catálogo confirmado; o nome do arquivo
  ROM deve ser preservado separadamente. Edições/regiões são versões do mesmo jogo,
  sem duplicar automaticamente a biblioteca ou fundir resultados ambíguos.
- Pastas do Drive identificam plataformas, inclusive regras próprias por ID e herança.
  Pasta `Temas` da coleção de referência contém temas de emulador mobile e é ignorada.
- Adicionar jogo deve permitir pesquisar ROMs do índice Drive diretamente, selecionar
  versão, confirmar resultado do catálogo e preencher os campos disponíveis na fonte.
  Não exigir navegar primeiro por Configurações.

## Implementação disponível

- Biblioteca CRUD com exclusão recuperável, busca/filtros, favoritos, lista/galeria,
  categorias e página individual; navegação Início/Biblioteca/Desejos/Memórias/Estatísticas/Configurações.
- SQLite WAL, chaves estrangeiras, migrações até 3, backup antes da migração, configurações,
  logs rotativos e bloqueio de instância. Sem valores demonstrativos na biblioteca.
- Diário textual, mídia referenciada com imagens ampliadas e vídeo no player do sistema,
  conquistas pessoais, desejos com meta BRL e estatísticas de sessões confirmadas.
- Launcher sem shell, executáveis diretos e perfis de argumentos JSON com `{rom}` para
  emuladores. Sessões diretas monitoradas pelo processo; emuladores encerrados manualmente
  no registro, pois processo aberto não prova ROM ativa. Recuperação de sessões interrompidas.
- Backups locais versionados e verificados de saves configurados por jogo, restauração
  preservando versão anterior e opção de backup após sessão. Não há envio desses saves ao Drive.
- Drive OAuth Desktop somente leitura com cofre Windows; scanner BFS paginado, índice de
  arquivos/pastas, cursor de alterações incremental, aliases/regras de plataformas, busca
  local sem acentos, filtro/contador, associação manual e download por ID com tamanho/MD5.
  Scanner não baixa a coleção. Catálogo DAT para revisão por MD5/tamanho/plataforma.
- RAWG implementado para busca e ficha de metadados com chave própria. Seleção explícita.
  SteamGridDB implementado para identidade, título e cover/banner/logo; também resolve
  AppID Steam, o que não é importação de conta Steam.
- Artes automáticas somente após identidade confirmada, preservando artes existentes.
  Cache validado com SHA-256 e proveniência em `artwork_assets`; worker com conexão própria,
  intervalo automático por jogo e tentativa manual. Falha de arte não desfaz cadastro/ROM.
- Cadastro Drive e identidade/versão salvos em transação única; reutiliza identidade existente,
  preserva dados pessoais e rejeita vínculos conflitantes/lixeira sem criar órfãos.
- Atualizador para Releases privadas com token de leitura, opção de prerelease, hash SHA-256,
  staging, helper Windows e rollback de falha de cópia. Sem assinatura nem instalador.

## O que foi efetivamente validado

- Release 0.1.13: 120 testes automatizados aprovados, pytest result 0; smoke do executável
  Windows nas seis páginas exit 0, SQLite schema 3 e integrity_check ok; ZIPs íntegros.
- OAuth real Drive e leitura da coleção foram confirmados. Após excluir somente do índice
  três arquivos de Temas, eram 2.144 ROMs classificadas em seis plataformas. Não há garantia
  de que esses números permaneçam atuais; não usar como dados embutidos do aplicativo.
- Chave SteamGridDB configurada pelo usuário no Windows, API real consultada; fluxo isolado
  de cadastro confirmou título e obteve os três tipos de arte, preservando nome da ROM.
- Quatro títulos da biblioteca pessoal foram padronizados por IDs previamente confirmados,
  após cópia consistente da base. Esses dados pessoais não fazem parte do repositório.
- RAWG autenticado, importação Steam, RetroAchievements, preços e upload de saves ao Drive
  não foram validados/implementados conforme as distinções abaixo. Não confundir testes
  com respostas substituídas e conexão HTTPS com autenticação real.

## Próximas prioridades

1. Consolidar código 0.1.13 e contexto no branch padrão, criar ambiente Cloud e executar
   os testes num checkout limpo. Registrar o que Linux consegue testar e o que exige Windows.
2. Revisar cadastro Drive/catálogo e preenchimento: ficha completa depende da fonte, pois
   SteamGridDB fornece principalmente identidade/artes, não toda a ficha RAWG/IGDB.
3. Implementar importação oficial Steam e tempo/conquistas, respeitando privacidade.
4. Evoluir downloads/scanner para progresso, cancelamento/retomada, coleções grandes,
   Shared Drives e jogos multiarquivo CUE/BIN sem adivinhar associações.
5. Integrar saves tradicionais ao Drive com OAuth separado e escopo de escrita mínimo,
   versionamento, detecção de conflitos e restauração segura. Não ampliar o token somente
   leitura de ROMs silenciosamente.
6. Implementar provedores IGDB/RetroAchievements e preços BRL com acesso permitido,
   agendamento, limites, histórico e alertas. Steam/Epic/GOG/Nuuvem/GG.deals/ITAD devem ser
   avaliados; não existe atualmente monitoramento automático de preços.
7. Melhorar detecção da sessão real de ROM por emulador, edição de memórias/mídia,
   desempenho, DPI, instalação/assinatura e validação limpa em Windows 10/11.

## Arquivos importantes

- `gamevault/app.py`, `window.py`, `dialogs.py`: entrada, navegação e cadastro.
- `database.py`, `library.py`: migrações e operações locais.
- `drive_dialog.py`, `folder_platform_dialog.py`, `integrations/drive.py`, `rom_catalog.py`.
- `game_import.py`, `catalog_picker.py`, `auto_artwork.py`, `artwork_progress.py`,
  `artwork_dialog.py`, `artwork_render.py`, `integrations/metadata.py`.
- `launcher.py`, `game_saves.py`, `save_profiles.py`, `saves.py`, `updates*.py`.
- `scripts/build.ps1`: build Windows PyInstaller e helper do atualizador.
- `tests/`: suíte isolada; `CLOUD_SETUP.md`: instalação/testes sem dados pessoais.

## Limitações e armadilhas conhecidas

- O cofre `CredentialVault` é Windows-only. Não substituir por arquivo em texto claro para
  fazer Linux funcionar. Fluxos sem autenticação e provedores substituídos podem ser testados.
- Diretório legado de dados: `%LOCALAPPDATA%/GameVault`. Banco/configurações/ROMs locais,
  mídias, saves e tokens não são transportados por GitHub ou pelo histórico de chat.
- A atualização 0.1.8 corrigiu dado TLS omitido por um runtime específico do Codex:
  `codex-rejected-cas.pem`, quando existente junto a ssl.py, deve ser incluído pelo build.
  Não desativar validação de certificados para resolver falhas de rede.
- Há diretório temporário antigo inacessível na máquina original. Sempre limitar pytest
  a `tests` e desabilitar cache; nunca incluir diretórios de build/teste no upload.
- Não sobrescrever `QDialog.done` nem o sinal `finished` com handlers de workers.
- Antes desta migração, `main` remoto estava em 0.1.5 e as versões novas só estavam nos
  assets de Releases. A publicação atual deve atualizar os arquivos diretamente no branch.
  Não mover tags antigas nem force-push para tentar unir históricos independentes.
- Linux Cloud não gera um executável Windows validado. Build/testes específicos permanecem
  em Windows; o usuário não deve precisar manter este PC online para desenvolvimento comum.

## Prompt para o novo chat Cloud

Publicação de continuidade em 11/11/2026: os arquivos fonte 0.1.13 foram enviados
diretamente ao `main` pelo site GitHub, preservando o histórico remoto. A suíte local
foi repetida: 120 aprovados, exit 0. Login Codex web concluído; conexão GitHub/ambiente
Cloud ainda precisam ser finalizados e validados. Consulte o resumo atual de status.

Continue o projeto Checkpoint no repositório pedroalexcarneiro/Checkpoint. Leia AGENTS.md,
CONTINUITY.md, PRODUCT_VISION.md e PROJECT_STATUS.md antes de editar. Confira a versão
0.1.13 e execute os testes em ambiente isolado conforme CLOUD_SETUP.md. Preserve as
decisões do usuário e reporte o resultado real. Primeiro valide a continuidade na nuvem;
depois avance na próxima prioridade viável, sem inventar credenciais nem resultados.

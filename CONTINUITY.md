# Continuidade do Checkpoint

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

Estado de referência: aplicativo 0.1.16 de desenvolvimento, schema SQLite 4.
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

# Validação

## Ambiente efetivamente usado

Windows 10 build 19045 do ambiente Codex (identificado pelo PyInstaller), Python 3.12.14 x64, PySide6 6.8.3, pytest 9.2.0. Não foi necessário usar o computador pessoal do usuário. Versões instaladas estão em requirements-tested.txt.

## Executar testes

```powershell
python -m pytest -q -p no:cacheprovider
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

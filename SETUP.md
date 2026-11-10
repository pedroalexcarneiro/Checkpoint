# Instalação e execução

## Requisitos

Windows 10/11 de 64 bits, Python 3.12 de 64 bits. A versão usada nesta entrega é Python 3.12.14 com PySide6 6.8.3. O pacote portátil inclui o runtime Python; o usuário final não precisa instalar Python. Validação em instalações limpas Windows 10/11 ainda é pendente.

## Instalação de desenvolvimento

Na pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m pip install pytest pyinstaller
.\.venv\Scripts\python.exe -m gamevault.app
```

Se o Python do Windows abrir o gerenciador de instalações, use um interpretador 3.12 já instalado explicitamente. Neste ambiente Codex, o interpretador utilizável estava no runtime do Codex. `venv/ensurepip` e `pip` esbarraram em permissões dos temporários; a instalação foi realizada com `uv pip --python` em um venv dentro de `work`. Essa limitação do host não exige alterar o código do produto.

As versões efetivas usadas estão em `requirements-tested.txt`. Para reproduzir esse ambiente, instale esse arquivo antes de instalar o projeto com `--no-deps -e .`. Não copie o venv entre computadores.

## Dados e recuperação

Padrão: `%LOCALAPPDATA%/GameVault`. Inclui `gamevault.sqlite`, WAL, lock e logs rotativos. Artes baixadas ficam em `images`. ROMs, capturas e backups usam diretórios escolhidos pelo usuário. Credenciais são mantidas no Windows Credential Manager (serviço GameVault); não são incluídas no backup do SQLite.

```powershell
python -m gamevault.app --data-dir ./dados-teste
python -m gamevault.app --smoke-test --data-dir ./dados-smoke
```

O modo smoke abre as seis páginas sem exibir janela, verifica integridade SQLite e salva `smoke-home.png`. Utilize sempre uma pasta isolada: abrir a aplicação recupera sessões active como interrupted.

Para restaurar o banco, feche todas as instâncias, preserve o diretório atual inteiro e copie uma cópia SQLite íntegra para `gamevault.sqlite` em uma pasta de dados nova. Não misture arquivos WAL antigos com um banco restaurado. Abra com `--data-dir` para conferir antes de adotá-la. A restauração de banco ainda não possui assistente gráfico.

## Empacotar

```powershell
.\scripts\build.ps1 -Python .\.venv\Scripts\python.exe
```

Saída: `dist/Checkpoint/Checkpoint.exe` e pasta `_internal`. A pasta completa deve acompanhar o executável. O build é one-dir para facilitar diagnóstico e evitar extração temporária a cada início. Build sem assinatura digital; não é um instalador e não possui atualizador automático.

Antes da distribuição pública, revisar licenças Qt/PySide6 LGPLv3, componentes incluídos e APIs utilizadas; incluir os avisos e condições necessários. Não há assinatura ou auditoria legal nesta entrega.

## Uso inicial

1. Adicione um jogo manualmente e escolha sua plataforma/status.
2. Use duplo clique ou Abrir selecionado para a página individual.
3. Configure executável local em Editar, ou um perfil de emulador nas Configurações.
4. Registre memórias, capturas e marcos pessoais no jogo.
5. Configure pastas e credenciais apenas quando quiser usar as integrações.

Vídeos dependem do reprodutor e codecs do Windows. Capturas são referências ao arquivo original: mover o arquivo quebra a referência; não há cópia oculta. ROMs baixadas permanecem no disco; remover um jogo da biblioteca não remove arquivos locais nem remotos.

## Atualização 0.1.3 — Checkpoint

Nome visível e executável alterados para Checkpoint. Removidos slogans da navegação, do início e dos estados vazios. Os dados, a trava de instância e o cofre continuam usando os identificadores internos GameVault para abrir a biblioteca existente sem migração. O pacote Python e a pasta de fontes também permanecem com seus nomes internos. O usuário confirmou que os fluxos locais solicitados no teste anterior funcionaram; isso não valida integrações autenticadas.


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

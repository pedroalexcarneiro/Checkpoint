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

## Atualização 0.1.2 — Checkpoint

Nome visível e executável alterados para Checkpoint. Removidos slogans da navegação, do início e dos estados vazios. Os dados, a trava de instância e o cofre continuam usando os identificadores internos GameVault para abrir a biblioteca existente sem migração. O pacote Python e a pasta de fontes também permanecem com seus nomes internos. O usuário confirmou que os fluxos locais solicitados no teste anterior funcionaram; isso não valida integrações autenticadas.


## Checkpoint 0.1.2 — saves por jogo

Implementados perfis de pasta/padrões por jogo, botão de backup manual na página individual, opção persistente de backup ao encerrar o registro da sessão, histórico por jogo e restauração para a pasta original do perfil. Operações por jogo rodam em worker com conexão SQLite própria; execução do jogo e fechamento do aplicativo são bloqueados durante a operação. A restauração preserva a versão local anterior em ZIP. Alterar o perfil não remove o histórico antigo.

O backup compara o conjunto de arquivos, tamanho, modificação e SHA-256 antes e após a cópia. Arquivos em alteração impedem a publicação do ZIP. O intervalo de estabilidade é de um segundo e não prova que um processo externo nunca mais escreverá: encerre o jogo antes de encerrar o registro. A opção automática começa desativada por jogo. Para executáveis monitorados, dispara ao sair o processo direto; launchers com processos filhos e detecção específica de ROM continuam pendentes. Não há varredura automática de saves nem reconhecimento universal de save states. Escolha padrões explícitos de saves tradicionais.

Configure o diretório de backups em Configurações; depois, na página do jogo, configure a pasta e os padrões (ex.: *.sav). O botão Fazer backup agora usa esse perfil. Ative a opção de backup ao encerrar a sessão se desejar. As versões aparecem abaixo e podem ser restauradas com confirmação. Não há envio ao Drive nesta versão.

Validação: 28 testes passaram (8,51 s), incluindo histórico preservado ao mudar perfil, restauração com cópia anterior, rejeição de backup de outro jogo, saves em alteração e encerramento de sessão disparando backup real em worker pela interface headless. Testes com emuladores reais e saves pessoais continuam pendentes. O backup manual antigo das Configurações continua síncrono; os novos fluxos por jogo usam workers.

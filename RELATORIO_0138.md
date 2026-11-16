# Correção da abertura — 0.1.38 em validação

Relato recebido após publicação da 0.1.37. Vídeo analisado diretamente: Explorer com pacote extraído, prompt de UAC aproximadamente no primeiro segundo e depois ausência da janela durante o restante da gravação. Não se presume, só pelo vídeo, crash exato, consentimento concedido ou perda de dados. Frames e vídeo privados mantidos fora do repositório.

Achado concreto em windows_frame.py: handle consultava self.window.winId durante callbacks de criação, incluindo WM_NCCALCSIZE. Esse getter pode solicitar criação quando o HWND ainda não foi associado pelo Qt, reentrando na criação. As validações antigas usavam Qt offscreen; no Windows elas não cobriam essa sequência de mensagens nativas. Corrigido para usar MSG.hWnd fornecido pelo Windows e rejeitar HWND zero. Não alterados elevação, banco, cofre, migração ou dados pessoais.

Antes: três falhas no teste de mensagens, exigindo que nenhuma mensagem de criação provoque nova criação de HWND. Depois: 14 regressões de moldura/abertura/elevação aprovadas em 1,96 s. Dois HWNDs incluindo valor acima de 32 bits, mensagem sem destinatário e dois jogos em subprocesso com abertura/captura/fechamento. Linux executa backend offscreen e não é declarado validação nativa Windows. Windows executará explicitamente plugin windows, sem skip novo.

scripts/native_startup_check.py acrescenta verificação externa de abertura normal em Windows real já elevado: lança somente um processo próprio com --data-dir novo, procura seu HWND visível por PID/título, exige resposta, captura PNG, fecha com WM_CLOSE e verifica SQLite/exit. Não chama --smoke-test e não automatiza UAC. scripts/package_windows_release.py executará essa verificação no fonte e no executável realmente extraído, preservando os smokes anteriores. Screenshot/registro da abertura nativa serão arquivos da entrega de validação. Aplicativo não detecta testes nem ganha atalho de inicialização que esconda o defeito.

Versão local 0.1.38, schema 4; 0.1.37/tag/releases/artefatos preservados. Ainda pendentes nesta etapa: suíte integral e validação Windows/pacote nativo. Não declarar abertura no PC do dono corrigida só pelos testes controlados. Plano: PLANO_0138.md.

## Validação integral e checkout do runner

Linux no commit 5e77741: 700 passed in 483.81s (0:08:03), exit 0. Windows UI validation 43797801516: 699 passed e uma falha em 642,86 s, sem build. Os cinco testes novos, incluindo duas janelas com Qt windows real em subprocessos, passaram. A falha foi o contrato de preservação: git show c51c245 não encontrava esse objeto porque o checkout do workflow de validação era raso. Nenhuma divergência em arquivo protegido foi apontada; esse run não é apresentado como suíte aprovada.

Correção de infraestrutura restrita a .github/workflows/windows-ui-validation.yml: fetch-depth: 0 no checkout, conforme já usado pelo workflow de release. A asserção protegida e os arquivos protegidos permanecem idênticos; não há fetch ou substituto oculto dentro dos testes. Workflow de publicação intacto. A escolha inicial de workflow sem conferir essa dependência do histórico atrasou o build; novo run repetirá a suíte e verificará o pacote nativo. Nenhuma nova alteração no código do aplicativo nesta etapa.

O primeiro ajuste de checkout (801f31f) inseriu uma segunda chave with no mesmo step. GitHub recusou o dispatch com HTTP 422/YAML duplicado e registrou 43799296217 sem executar testes/build. Corrigido agrupando fetch-depth e persist-credentials no mesmo with. YAML validado com SafeLoader estrito que rejeita duplicidades; persist-credentials permanece false. Erro de edição do implementador, sem publicação/alteração do aplicativo. Histórico mantido, sem amend/force.

# Correção da abertura — 0.1.38 publicada e verificada

## 0.1.38 publicada — correção de abertura

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.38

Tag/código: c4a7e1d221ba52a8580dd73ab884b1964e6ffd32. Windows release 43857996709 concluído com build e publicação aprovados. Windows/Python 3.12.10: 700 passed in 633.27s (0:10:33), zero falhas/erros/skips. Linux/Python 3.12.14: 700 passed in 483.81s (0:08:03), código funcional idêntico. Fonte e executável extraído passaram também por abertura normal com Qt windows, HWND visível/responsivo, captura, fechamento e SQLite, em Windows já elevado.

Dez arquivos publicados baixados e conferidos por tamanho/SHA-256 contra os digests do GitHub. CRC dos dois ZIPs válido. ZIP Windows: 84314842 bytes, SHA-256 15fef170b44dcf6073d50fed3f601f8b1cb265540c5e456113fe2befad0e3702. A 0.1.37/tag/arquivos foram preservados. Fonte do fix usa MSG.hWnd durante criação nativa, evitando chamar winId recursivamente; não muda dados, schema 4, cofre ou A4.

Upload local inicial recusado por autenticação em uploads.github.com; publicação concluída pelo workflow existente com identidade do próprio GitHub, sem alterar o workflow de release. A execução read-only anterior foi preservada como validação, e o publisher repetiu todos os gates. Documentação posterior não move a tag.

Consentimento UAC interativo e uso no PC do dono continuam sujeitos à confirmação; não confundir execução nativa já elevada no runner com consentimento automatizado. As demais limitações anteriores de fontes de preço, A4 e fechamento somente da ROM permanecem. Registros seguintes descrevem a preparação e as falhas de infraestrutura.

## Resultado final

Candidato validado: ff136584974b55989c10598612235717508ec25a. Windows UI validation 43799707113 concluída com sucesso, sem publicação de release/tag. Windows/Python 3.12.10: **700 passed in 673.05s (0:11:13)**, zero falhas/erros/skips. Linux/Python 3.12.14: **700 passed in 483.81s (0:08:03)**. Código/testes idênticos entre a execução Linux 5e77741 e esse candidato; diferenças posteriores foram documentação e checkout do CI.

A abertura normal foi verificada no fonte e no executável realmente extraído: sem --smoke-test, plugin Qt windows, HWND visível, resposta às mensagens, captura, WM_CLOSE, exit 0 e SQLite íntegro. Executor Windows já elevado; não foi automatizado consentimento UAC. Registro do executável: janela 1100×740, ordinary_startup=true, responsive=true, exit_code=0, stdout/stderr vazios. Imagem real Checkpoint-0.1.38-native-startup.png, base de teste vazia. A captura vem do desktop virtual do runner e inclui faixa sem conteúdo à direita; não é homologação visual de outras resoluções nem acesso ao PC do dono.

ZIP Windows: 84316195 bytes, SHA-256 **9f2238c621d0fb5fc9ed22106bee34b938283ef3f8b0cd7e96770a757496cfce**, igual ao checksum gerado pelo build. CRC do pacote e do ZIP de revisão aprovados. Arquivo externo de artefatos do GitHub (14196740155): 88049666 bytes, SHA-256 9f82a60919ca6a8c5b4faa09cae3397f301ddd002bddef64e42ea8f98d465c64, conferido após download. Dez arquivos resultantes com hashes em verified-package.json fora do repositório, sem URL assinada ou vídeo privado.

O download inicial pelo gh recebeu 403 no armazenamento de artefatos. Download pelo conector GitHub concluído e transferido para o workspace; link temporário não persistido no repositório/relatórios. A verificação local confirmou o digest do artefato original, os checksums internos e o registro da inicialização. As saídas Windows completas estão em RELATORIO_0138_TESTES.md.

Tag/arquivos/release 0.1.37 preservados; 0.1.38 ainda não publicada. Patch não muda dados/cofre/migração/A4/assets. Permanece a confirmação do uso no PC do dono, incluindo consentimento UAC real; a aprovação automática do runner não substitui esse teste. Etapas anteriores e falhas de infraestrutura abaixo mantidas como histórico.

Relato recebido após publicação da 0.1.37. Vídeo analisado diretamente: Explorer com pacote extraído, prompt de UAC aproximadamente no primeiro segundo e depois ausência da janela durante o restante da gravação. Não se presume, só pelo vídeo, crash exato, consentimento concedido ou perda de dados. Frames e vídeo privados mantidos fora do repositório.

Achado concreto em windows_frame.py: handle consultava self.window.winId durante callbacks de criação, incluindo WM_NCCALCSIZE. Esse getter pode solicitar criação quando o HWND ainda não foi associado pelo Qt, reentrando na criação. As validações antigas usavam Qt offscreen; no Windows elas não cobriam essa sequência de mensagens nativas. Corrigido para usar MSG.hWnd fornecido pelo Windows e rejeitar HWND zero. Não alterados elevação, banco, cofre, migração ou dados pessoais.

Antes: três falhas no teste de mensagens, exigindo que nenhuma mensagem de criação provoque nova criação de HWND. Depois: 14 regressões de moldura/abertura/elevação aprovadas em 1,96 s. Dois HWNDs incluindo valor acima de 32 bits, mensagem sem destinatário e dois jogos em subprocesso com abertura/captura/fechamento. Linux executa backend offscreen e não é declarado validação nativa Windows. Windows executará explicitamente plugin windows, sem skip novo.

scripts/native_startup_check.py acrescenta verificação externa de abertura normal em Windows real já elevado: lança somente um processo próprio com --data-dir novo, procura seu HWND visível por PID/título, exige resposta, captura PNG, fecha com WM_CLOSE e verifica SQLite/exit. Não chama --smoke-test e não automatiza UAC. scripts/package_windows_release.py executará essa verificação no fonte e no executável realmente extraído, preservando os smokes anteriores. Screenshot/registro da abertura nativa serão arquivos da entrega de validação. Aplicativo não detecta testes nem ganha atalho de inicialização que esconda o defeito.

Versão local 0.1.38, schema 4; 0.1.37/tag/releases/artefatos preservados. Ainda pendentes nesta etapa: suíte integral e validação Windows/pacote nativo. Não declarar abertura no PC do dono corrigida só pelos testes controlados. Plano: PLANO_0138.md.

## Validação integral e checkout do runner

Linux no commit 5e77741: 700 passed in 483.81s (0:08:03), exit 0. Windows UI validation 43797801516: 699 passed e uma falha em 642,86 s, sem build. Os cinco testes novos, incluindo duas janelas com Qt windows real em subprocessos, passaram. A falha foi o contrato de preservação: git show c51c245 não encontrava esse objeto porque o checkout do workflow de validação era raso. Nenhuma divergência em arquivo protegido foi apontada; esse run não é apresentado como suíte aprovada.

Correção de infraestrutura restrita a .github/workflows/windows-ui-validation.yml: fetch-depth: 0 no checkout, conforme já usado pelo workflow de release. A asserção protegida e os arquivos protegidos permanecem idênticos; não há fetch ou substituto oculto dentro dos testes. Workflow de publicação intacto. A escolha inicial de workflow sem conferir essa dependência do histórico atrasou o build; novo run repetirá a suíte e verificará o pacote nativo. Nenhuma nova alteração no código do aplicativo nesta etapa.

O primeiro ajuste de checkout (801f31f) inseriu uma segunda chave with no mesmo step. GitHub recusou o dispatch com HTTP 422/YAML duplicado e registrou 43799296217 sem executar testes/build. Corrigido agrupando fetch-depth e persist-credentials no mesmo with. YAML validado com SafeLoader estrito que rejeita duplicidades; persist-credentials permanece false. Erro de edição do implementador, sem publicação/alteração do aplicativo. Histórico mantido, sem amend/force.

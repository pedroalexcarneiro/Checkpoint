# Lançamento 0.1.37 — em preparação

Autorização posterior do dono: “dps de acabar tu lanca a versao ta”. Essa instrução substitui a restrição de publicação da fase inicial desta rodada. Não reutilizada autorização antiga da 0.1.36.

Plano: terminar verificações locais, enviar fix/0.1.37-ajustes sem force, conferir SHA remoto e disparar Windows release existente nessa branch. O workflow testa no Windows, builda, valida fonte e executável extraído, captura a interface e só então publica a pré-release v0.1.37. Nenhum workflow será modificado; nenhuma tag/release anterior será movida ou substituída. Notas públicas atualizadas para esta versão após a autorização, incluindo limitações.

Código local congelado para a suíte final: f543166037e545aad99c6aef21bf6ed95fe4bb10. Commit posterior de documentação/notas preserva esse código. Resultado e SHA efetivamente enviado serão registrados abaixo. Preparação não equivale a versão publicada.

Pendências explicitadas nas notas: fonte autenticada console/original individual não comprovados; moldura, UAC, captura elevada, emuladores/contas/DPI/monitores reais no PC do dono não homologados; A4 protegido e fechar apenas ROM mantêm seus limites. Runner Windows não certifica uso pessoal real. A rodada não é apresentada como inteiramente concluída com essas pendências.

Comandos registrados com stdout/stderr/código de saída, sem tokens. Testes locais e antes/depois completos em RELATORIO_0137_TESTES.md; detalhes por item em RELATORIO_0137.md.

## push-0137

UTC: 2026-11-16T02:07:53.585557+00:00

Comando: `["git", "push", "origin", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text
remote: 
remote: Create a pull request for 'fix/0.1.37-ajustes' on GitHub by visiting:        
remote:      https://github.com/pedroalexcarneiro/Checkpoint/pull/new/fix/0.1.37-ajustes        
remote: 
To https://github.com/pedroalexcarneiro/Checkpoint.git
 * [new branch]      fix/0.1.37-ajustes -> fix/0.1.37-ajustes

```

Código de saída: 0

## confirmar-remoto-0137

UTC: 2026-11-16T02:08:00.977998+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
a33f48afbb8502a2f128de453451f326e8c988c2	refs/heads/fix/0.1.37-ajustes

```

stderr integral:
```text

```

Código de saída: 0

## actions-antes-dispatch

UTC: 2026-11-16T02:08:17.276178+00:00

Comando: `["gh", "run", "list", "--branch", "fix/0.1.37-ajustes", "--limit", "5", "--json", "databaseId,headSha,status,conclusion,name,event,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
[]

```

stderr integral:
```text

```

Código de saída: 0

## dispatch-release-0137

UTC: 2026-11-16T02:08:26.114508+00:00

Comando: `["gh", "workflow", "run", "windows-release.yml", "--ref", "fix/0.1.37-ajustes"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## localizar-run-0137

UTC: 2026-11-16T02:08:55.346135+00:00

Comando: `["gh", "run", "list", "--branch", "fix/0.1.37-ajustes", "--workflow", "windows-release.yml", "--limit", "3", "--json", "databaseId,headSha,status,conclusion,name,event,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
[{"conclusion":"","databaseId":43790327035,"event":"workflow_dispatch","headSha":"a33f48afbb8502a2f128de453451f326e8c988c2","name":"Windows release","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035"}]

```

stderr integral:
```text

```

Código de saída: 0

## Pré-envio e execução disparada

```text
HEAD local: a33f48afbb8502a2f128de453451f326e8c988c2
git status --porcelain: vazio
ls-remote stdout:

ls-remote stderr:

exit: 0
```

Branch enviada sem force em a33f48afbb8502a2f128de453451f326e8c988c2. ls-remote confirmou o mesmo SHA. Nenhuma execução automática foi criada pelo push; uma única execução manual Windows release foi iniciada após a autorização.

Execução: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035 — workflow_dispatch, SHA a33f48afbb8502a2f128de453451f326e8c988c2. Testes Windows em andamento; nenhuma publicação confirmada neste ponto.

## Primeira execução bloqueada — corrigido o próprio teste

A execução manual 43790327035 foi encerrada pelo implementador depois de reproduzir uma falha na limpeza do teste novo dos controles. Build/publish não foram executados e nenhuma tag/release foi criada. Não era uma execução inesperada do push; o cancelamento desta execução manual evitou aguardar o limite com um modal bloqueado.

Logs Windows: 648 testes completos (93%) e mais 24 pontos, ou seja, 672 completos, sem conclusão da suíte. A ordem de coleta coloca test_window_controls_use_regular_window_close_and_restore[sample0] em 672 e sample1 em 673. O teste substituía window.close por um spy e o mantinha durante a limpeza da fixture; a janela era destruída com o hotkey ainda registrado. A próxima janela podia abrir o modal de conflito e bloquear. Não se trata de 672 aprovações finais nem de falha comprovada do aplicativo em uso real.

Reprodução local com adaptador de atalho exclusivo confirmou dois erros na limpeza, um por jogo. Correção somente em tests/test_window_controls_0137.py: spy limitado a monkeypatch.context; depois o botão fecha realmente a janela e verifica liberação do atalho. Todas as asserções anteriores preservadas; verificações de fechamento/liberação acrescentadas. Depois: três testes aprovados em 0,35 s com o adaptador que antes detectava vazamento. Aplicativo, fontes protegidas, workflows e versão permanecem intactos. Nova execução será de um commit posterior, sem reescrever o candidato anterior.

## andamento-windows-0137

UTC: 2026-11-16T02:17:38.409119+00:00

Comando: `["gh", "run", "view", "43790327035", "--json", "createdAt,updatedAt,headSha,status,conclusion,url"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
{"conclusion":"","createdAt":"2026-11-16T02:08:25Z","headSha":"a33f48afbb8502a2f128de453451f326e8c988c2","status":"in_progress","updatedAt":"2026-11-16T02:08:29Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43790327035"}

```

stderr integral:
```text

```

Código de saída: 0

## encerrar-run-bloqueado

UTC: 2026-11-16T02:25:13.989074+00:00

Comando: `["gh", "run", "cancel", "43790327035"]`

Ambiente: QT_QPA_PLATFORM=; CHECKPOINT_TEST_ROOT=

stdout integral:
```text
✓ Request to cancel workflow 43790327035 submitted.

```

stderr integral:
```text

```

Código de saída: 0

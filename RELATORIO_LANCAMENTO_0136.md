# Lançamento Checkpoint 0.1.36 — em andamento

Autorização explícita do dono recebida nesta conversa para lançar no GitHub. Padrão mantido: pré-release Windows x64, pelo workflow existente Windows release, sem modificar workflows nem tags/releases anteriores.

Base local recebida: 67f4800540fc43be4fe2ee8e8976814c5a677db3 (documentação); código validado: da12842e6de663ee4791a6a4010bc622cfed8222, 612 testes Linux. Checkout inicial limpo; versão declarada 0.1.36, schema 4. Remoto fix/0.1.35-ajustes continua 818ec80a492a29936782ddb3a43eecaf3ef996e3; tag v0.1.36 e branch remota fix/0.1.36-ajustes inexistentes na consulta inicial.

Preparação altera somente documentação/notas públicas. A etapa Windows testa e constrói o commit enviado; validação no runner não comprova captura real, conta autenticada ou homologação no PC do dono. Limitações 02/03/06, A4 e ROM descarregada com emulador vivo preservadas nas notas.

Saídas integrais dos comandos de lançamento serão acrescentadas abaixo. Nenhuma credencial é registrada.

## verificacao-pre-push

UTC: 2026-11-15T17:43:22.875975+00:00

Comando: `["/workspace/work/venv/bin/python", "-c", "import subprocess;from pathlib import Path;import tomllib;from checkpoint import __version__;assert __version__=='0.1.36'==tomllib.loads(Path('pyproject.toml').read_text(encoding='utf-8'))['project']['version'];base='67f4800540fc43be4fe2ee8e8976814c5a677db3';names=subprocess.check_output(['git','diff','--name-only',base],text=True,encoding='utf-8').splitlines();assert not any(n.startswith(('checkpoint/','tests/','scripts/','.github/workflows/')) or n in ('requirements-tested.txt','pyproject.toml') for n in names);[(Path(n).read_text(encoding='utf-8'),None if b'\\r' not in Path(n).read_bytes() else (_ for _ in ()).throw(AssertionError(n))) for n in names];subprocess.run(['git','diff','--check'],check=True);print('Versão/schema confirmados; código/testes/workflows/scripts/dependências inalterados desde entrega validada.');print('Arquivos de preparação:',names)"]`

stdout integral:
```text
Versão/schema confirmados; código/testes/workflows/scripts/dependências inalterados desde entrega validada.
Arquivos de preparação: ['.github/release-notes.md', 'CHANGELOG.md', 'CONTINUITY.md', 'PROJECT_STATUS.md']

```

stderr integral:
```text

```

Código de saída: 0

## push-branch

UTC: 2026-11-15T17:43:56.488033+00:00

Comando: `["git", "push", "origin", "fix/0.1.36-ajustes"]`

stdout integral:
```text

```

stderr integral:
```text
remote: 
remote: Create a pull request for 'fix/0.1.36-ajustes' on GitHub by visiting:        
remote:      https://github.com/pedroalexcarneiro/Checkpoint/pull/new/fix/0.1.36-ajustes        
remote: 
To https://github.com/pedroalexcarneiro/Checkpoint.git
 * [new branch]      fix/0.1.36-ajustes -> fix/0.1.36-ajustes

```

Código de saída: 0

## confirmar-remoto

UTC: 2026-11-15T17:43:56.805484+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.36-ajustes", "refs/tags/v0.1.36"]`

stdout integral:
```text
1a8f24ce24ad273c99f92187311820d42ebc9d1a	refs/heads/fix/0.1.36-ajustes

```

stderr integral:
```text

```

Código de saída: 0

## execucoes-antes

UTC: 2026-11-15T17:44:30.812516+00:00

Comando: `["gh", "run", "list", "--repo", "pedroalexcarneiro/Checkpoint", "--branch", "fix/0.1.36-ajustes", "--limit", "5", "--json", "databaseId,headSha,name,event,status,conclusion,url,createdAt"]`

stdout integral:
```text
[]

```

stderr integral:
```text

```

Código de saída: 0

## acionar-windows-release

UTC: 2026-11-15T17:44:32.989041+00:00

Comando: `["gh", "workflow", "run", "windows-release.yml", "--repo", "pedroalexcarneiro/Checkpoint", "--ref", "fix/0.1.36-ajustes"]`

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## execucoes-apos

UTC: 2026-11-15T17:44:33.930205+00:00

Comando: `["gh", "run", "list", "--repo", "pedroalexcarneiro/Checkpoint", "--workflow", "windows-release.yml", "--branch", "fix/0.1.36-ajustes", "--limit", "5", "--json", "databaseId,headSha,name,event,status,conclusion,url,createdAt"]`

stdout integral:
```text
[]

```

stderr integral:
```text

```

Código de saída: 0

## localizar-execucao

UTC: 2026-11-15T17:45:23.135143+00:00

Comando: `["gh", "run", "list", "--repo", "pedroalexcarneiro/Checkpoint", "--workflow", "windows-release.yml", "--branch", "fix/0.1.36-ajustes", "--limit", "5", "--json", "databaseId,headSha,name,event,status,conclusion,url,createdAt"]`

stdout integral:
```text
[{"conclusion":"","createdAt":"2026-11-15T17:44:32Z","databaseId":43742802876,"event":"workflow_dispatch","headSha":"1a8f24ce24ad273c99f92187311820d42ebc9d1a","name":"Windows release","status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876"}]

```

stderr integral:
```text

```

Código de saída: 0

## estado-inicial

UTC: 2026-11-15T17:45:45.180265+00:00

Comando: `["gh", "run", "view", "43742802876", "--repo", "pedroalexcarneiro/Checkpoint", "--json", "status,conclusion,headSha,jobs,url"]`

stdout integral:
```text
{"conclusion":"","headSha":"1a8f24ce24ad273c99f92187311820d42ebc9d1a","jobs":[{"completedAt":"0001-01-01T00:00:00Z","conclusion":"","databaseId":132899460542,"name":"build","startedAt":"2026-11-15T17:44:36Z","status":"in_progress","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"","name":"Test on Windows","number":6,"status":"in_progress"},{"conclusion":"","name":"Build desktop and updater","number":7,"status":"pending"},{"conclusion":"","name":"Package and validate extracted executable","number":8,"status":"pending"},{"conclusion":"","name":"Render Windows interface review","number":9,"status":"pending"},{"conclusion":"","name":"Upload verified release files","number":10,"status":"pending"},{"conclusion":"","name":"Preserve Windows test report","number":11,"status":"pending"},{"conclusion":"","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"pending"},{"conclusion":"","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"pending"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876/job/132899460542"}],"status":"in_progress","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876"}

```

stderr integral:
```text

```

Código de saída: 0

## Acompanhamento pausado a pedido do dono

Dono pediu deixar o GitHub trabalhando em segundo plano. Workflow 43742802876: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876, commit 1a8f24ce24ad273c99f92187311820d42ebc9d1a, branch fix/0.1.36-ajustes. Execução não cancelada. A publicação é automática somente após sucesso dos testes Windows, build e smokes. Ainda não há comprovação final de publicação neste registro. Ao retomar, conferir conclusão, release v0.1.36, tag, assets e SHA-256 antes de declarar lançado. Saídas e monitor.jsonl em /workspace/work/release-0136.

## regressao-render-antes

UTC: 2026-11-15T19:49:39.784276+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_ui_review_lifecycle_0136.py", "-q", "-p", "no:cacheprovider"]`

stdout integral:
```text
F                                                                        [100%]
=================================== FAILURES ===================================
_____________ test_review_releases_global_shortcut_between_windows _____________

folder = PosixPath('/tmp/7eac6f354bc14f7bb3d7e9c44773623a')

    def test_review_releases_global_shortcut_between_windows(folder):
        code = r'''
    import runpy
    import sys
    from PySide6.QtWidgets import QMessageBox
    import checkpoint.global_hotkey as hotkey
    from checkpoint.credentials import CredentialVault
    
    class ExclusiveApi:
        active = {}
        registrations = 0
        def register(self, identity, modifiers, key):
            if identity in self.active or (modifiers, key) in self.active.values():
                return False
            self.active[identity] = (modifiers, key)
            self.registrations += 1
            return True
        def unregister(self, identity):
            return self.active.pop(identity, None) is not None
    
    api = ExclusiveApi()
    original_init = hotkey.GlobalCaptureHotkey.__init__
    def exclusive_init(self, window, callback, sequence, **kwargs):
        original_init(self, window, callback, sequence, api=api)
    hotkey.GlobalCaptureHotkey.__init__ = exclusive_init
    CredentialVault.get = lambda *args: None
    def unexpected_warning(*args):
        raise RuntimeError('Revisão bloqueada por aviso modal: ' + str(args[-1]))
    QMessageBox.warning = unexpected_warning
    sys.argv = ['scripts/render_ui_review.py', sys.argv[1]]
    runpy.run_path(sys.argv[0], run_name='__main__')
    assert api.registrations == 2, api.registrations
    assert api.active == {}, api.active
    '''
        output = folder / 'review'
        result = subprocess.run(
            [sys.executable, '-c', code, str(output)],
            cwd=Path(__file__).resolve().parents[1],
            env={**os.environ, 'QT_QPA_PLATFORM': 'offscreen'},
            capture_output=True, text=True, encoding='utf-8', errors='replace',
            timeout=90,
        )
>       assert result.returncode == 0, result.stdout + result.stderr
E       AssertionError: Fontconfig error: No writable cache directories
E         This plugin does not support propagateSizeHints()
E         This plugin does not support propagateSizeHints()
E         This plugin does not support propagateSizeHints()
E         ERROR:root:Operação falhou
E         Traceback (most recent call last):
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 142, in guard
E             try: return callback()
E                         ^^^^^^^^^^
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 105, in <lambda>
E             self.guard(lambda:self.capture_shortcut.setKey(configured))
E                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           File "/workspace/work/Checkpoint/checkpoint/global_hotkey.py", line 69, in setKey
E             raise ValueError('Atalho de captura em uso. Escolha outra combinação em Configurações.')
E         ValueError: Atalho de captura em uso. Escolha outra combinação em Configurações.
E         Traceback (most recent call last):
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 142, in guard
E             try: return callback()
E                         ^^^^^^^^^^
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 105, in <lambda>
E             self.guard(lambda:self.capture_shortcut.setKey(configured))
E                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           File "/workspace/work/Checkpoint/checkpoint/global_hotkey.py", line 69, in setKey
E             raise ValueError('Atalho de captura em uso. Escolha outra combinação em Configurações.')
E         ValueError: Atalho de captura em uso. Escolha outra combinação em Configurações.
E         
E         During handling of the above exception, another exception occurred:
E         
E         Traceback (most recent call last):
E           File "<string>", line 30, in <module>
E           File "<frozen runpy>", line 287, in run_path
E           File "<frozen runpy>", line 98, in _run_module_code
E           File "<frozen runpy>", line 88, in _run_code
E           File "scripts/render_ui_review.py", line 174, in <module>
E             if __name__=='__main__':main()
E                                     ^^^^^^
E           File "scripts/render_ui_review.py", line 166, in main
E             empty_window=MainWindow(empty_lib);empty_window.resize(1100,740);empty_window.show()
E                          ^^^^^^^^^^^^^^^^^^^^^
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 105, in __init__
E             self.guard(lambda:self.capture_shortcut.setKey(configured))
E           File "/workspace/work/Checkpoint/checkpoint/window.py", line 145, in guard
E             QMessageBox.warning(self,'Checkpoint',str(error))
E           File "<string>", line 27, in unexpected_warning
E         RuntimeError: Revisão bloqueada por aviso modal: Atalho de captura em uso. Escolha outra combinação em Configurações.
E         
E       assert 1 == 0
E        +  where 1 = CompletedProcess(args=['/workspace/work/venv/bin/python', '-c', "\nimport runpy\nimport sys\nfrom PySide6.QtWidgets im...ntimeError: Revisão bloqueada por aviso modal: Atalho de captura em uso. Escolha outra combinação em Configurações.\n').returncode

tests/test_ui_review_lifecycle_0136.py:50: AssertionError
=========================== short test summary info ============================
FAILED tests/test_ui_review_lifecycle_0136.py::test_review_releases_global_shortcut_between_windows
1 failed in 9.48s

```

stderr integral:
```text

```

Código de saída: 1

## regressao-render-depois

UTC: 2026-11-15T19:50:07.116517+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests/test_ui_review_lifecycle_0136.py", "tests/test_capture_0136.py", "-q", "-p", "no:cacheprovider"]`

stdout integral:
```text
.......                                                                  [100%]
7 passed in 9.84s

```

stderr integral:
```text

```

Código de saída: 0

## primeira-execucao-final

UTC: 2026-11-15T19:50:08.902170+00:00

Comando: `["gh", "run", "view", "43742802876", "--repo", "pedroalexcarneiro/Checkpoint", "--json", "status,conclusion,headSha,jobs,url"]`

stdout integral:
```text
{"conclusion":"cancelled","headSha":"1a8f24ce24ad273c99f92187311820d42ebc9d1a","jobs":[{"completedAt":"2026-11-15T18:14:56Z","conclusion":"cancelled","databaseId":132899460542,"name":"build","startedAt":"2026-11-15T17:44:36Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"success","name":"Test on Windows","number":6,"status":"completed"},{"conclusion":"success","name":"Build desktop and updater","number":7,"status":"completed"},{"conclusion":"success","name":"Package and validate extracted executable","number":8,"status":"completed"},{"conclusion":"cancelled","name":"Render Windows interface review","number":9,"status":"completed"},{"conclusion":"skipped","name":"Upload verified release files","number":10,"status":"completed"},{"conclusion":"success","name":"Preserve Windows test report","number":11,"status":"completed"},{"conclusion":"skipped","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"completed"},{"conclusion":"success","name":"Complete job","number":23,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876/job/132899460542"},{"completedAt":"2026-11-15T18:14:56Z","conclusion":"skipped","databaseId":132908270855,"name":"publish","startedAt":"2026-11-15T18:14:57Z","status":"completed","steps":[],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876/job/132908270855"}],"status":"completed","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43742802876"}

```

stderr integral:
```text

```

Código de saída: 0

## render-local-normal

UTC: 2026-11-15T19:50:55.696770+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/render_ui_review.py", "/workspace/work/release-0136/review-corrigido"]`

stdout integral:
```text
/workspace/work/release-0136/review-corrigido

```

stderr integral:
```text
Fontconfig error: No writable cache directories
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()
This plugin does not support propagateSizeHints()

```

Código de saída: 0

## Diagnóstico e correção da primeira execução

Run 43742802876, commit 1a8f24ce24ad273c99f92187311820d42ebc9d1a. Anotação do GitHub: "The job has exceeded the maximum execution time of 30m0s". Não houve cancelamento manual nem publicação. Testes Windows: **612 passed in 453.60s (0:07:33)**, 0 falhas/erros/skips; build e validação do executável extraído aprovados. Revisão visual bloqueada pelo aviso modal de conflito do atalho, publish ignorado por dependência não concluída.

Log completo recebido pela ferramenta GitHub fetch_workflow_job_logs e preservado como texto UTF-8 em /workspace/work/release-0136/primeiro-job-plugin.log, SHA-256 cd8a2311ac9129725196b90933ce13d098037bf866337ffc59494b9bb441efd5. Caracteres já substituídos na resposta da ferramenta foram preservados; não é uma alegação de log binário original. gh run view --log e gh api actions/jobs/.../logs retornaram conteúdo vazio neste ambiente, motivo do uso da ferramenta GitHub para leitura do log.

Origem: scripts/render_ui_review.py::main ocultava a primeira MainWindow sem encerrá-la e criava a janela de estados vazios. As duas tentavam registrar Ctrl+Shift+S. MainWindow.guard mostrava o erro em QMessageBox.warning e aguardava interação em um runner sem operador. Correção: encerrar a primeira janela e seu banco antes da segunda; recusar continuidade se close() falhar. Aplicativo, atalho real, assets, workflows e gates de publicação permanecem intactos.

Regressão nova tests/test_ui_review_lifecycle_0136.py::test_review_releases_global_shortcut_between_windows executa o script inteiro em subprocesso, com adaptador controlado que recusa registro duplicado e converte aviso modal inesperado em falha imediata. Antes: falha no construtor da segunda MainWindow, mesmo erro de conflito do Windows. Depois: 7 testes direcionados passaram em 9,84 s; duas inscrições sequenciais, nenhum registro restante, pelo menos 30 PNGs e os quatro estados vazios presentes. Os 13 jogos incluem Hollow Knight e Celeste, com artes/sessões sintéticas isoladas; isso não valida contas nem captura de jogos reais.

As saídas integrais antes/depois estão acima. A suíte completa será registrada a seguir. Espaços finais em blocos de stdout/stderr são preservados para manter o registro integral, inclusive os emitidos por git push e pytest; os arquivos de código novos/alterados são UTF-8/LF.

## empacotar-revisao-local

UTC: 2026-11-15T19:51:21.568939+00:00

Comando: `["/workspace/work/venv/bin/python", "scripts/package_ui_review.py", "/workspace/work/release-0136/review-corrigido", "/workspace/work/release-0136/review-assets"]`

stdout integral:
```text
Revisão visual: 61 PNGs e índice HTML; bases e logs excluídos.

```

stderr integral:
```text

```

Código de saída: 0

## primeiro-junit-download

UTC: 2026-11-15T19:54:30.106335+00:00

Comando: `["gh", "run", "download", "43742802876", "--repo", "pedroalexcarneiro/Checkpoint", "--name", "checkpoint-windows-test-report", "--dir", "/workspace/work/release-0136/primeiro-junit"]`

stdout integral:
```text

```

stderr integral:
```text
error downloading checkpoint-windows-test-report: Get "[URL temporária assinada omitida]": Forbidden

```

Código de saída: 1

Artefato JUnit da primeira execução recuperado pela ferramenta GitHub download_workflow_artifact, ID 14174371425; SHA-256 d48521b8fc8ce9aa252712566d93302ead04333b6ed645fd2d5eeff7a7674aa0 conferido com o digest do GitHub. Tentativa gh run download anterior recebeu Forbidden do armazenamento de artefatos; URL temporária assinada omitida do registro por conter credencial transitória.

## suite-linux-correcao-render

UTC: 2026-11-15T19:56:59.484882+00:00

Comando: `["/workspace/work/venv/bin/python", "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider"]`

stdout integral:
```text
........................................................................ [ 11%]
........................................................................ [ 23%]
........................................................................ [ 35%]
........................................................................ [ 46%]
........................................................................ [ 58%]
........................................................................ [ 70%]
........................................................................ [ 82%]
........................................................................ [ 93%]
.....................................                                    [100%]
613 passed in 401.33s (0:06:41)

```

stderr integral:
```text

```

Código de saída: 0

## push-correcao

UTC: 2026-11-15T19:57:20.714528+00:00

Comando: `["git", "push", "origin", "fix/0.1.36-ajustes"]`

stdout integral:
```text

```

stderr integral:
```text
To https://github.com/pedroalexcarneiro/Checkpoint.git
   1a8f24c..4e54fc0  fix/0.1.36-ajustes -> fix/0.1.36-ajustes

```

Código de saída: 0

## confirmar-remoto-correcao

UTC: 2026-11-15T19:57:28.162170+00:00

Comando: `["git", "ls-remote", "origin", "refs/heads/fix/0.1.36-ajustes", "refs/tags/v0.1.36"]`

stdout integral:
```text
4e54fc0b91ca7a4180307874f72f3b32eb3dca87	refs/heads/fix/0.1.36-ajustes

```

stderr integral:
```text

```

Código de saída: 0

## acionar-release-corrigida

UTC: 2026-11-15T19:57:33.744956+00:00

Comando: `["gh", "workflow", "run", "windows-release.yml", "--repo", "pedroalexcarneiro/Checkpoint", "--ref", "fix/0.1.36-ajustes"]`

stdout integral:
```text

```

stderr integral:
```text

```

Código de saída: 0

## Nova execução de lançamento

Correção enviada em 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Saída de git status --porcelain vazia imediatamente após o commit; depois somente este relatório recebeu registros de envio/acompanhamento. HEAD remoto reconfirmado igual ao commit. Sem force push. Tag v0.1.36 inexistente antes do acionamento.

Suíte completa Linux/Python 3.12.14: **613 passed in 401.33s (0:06:41)**, exit 0, QT_QPA_PLATFORM=offscreen e CHECKPOINT_TEST_ROOT=/tmp. Regressão nova aprovada junto com todas as anteriores; nenhuma asserção existente, skip ou xfail alterado. Renderizador normal também concluiu, e package_ui_review gerou 61 PNGs e índice HTML no ZIP, excluindo bancos e logs.

Diff contra 818ec80a492a29936782ddb3a43eecaf3ef996e3 vazio para workflows, checkpoint/assets, tests/test_save_lifecycle.py, checkpoint/worker.py, checkpoint/enrichment.py, checkpoint/game_import.py, checkpoint/completion_queue.py, checkpoint/dialogs.py e checkpoint/quick_add.py. Arquivos novos/alterados de código UTF-8/LF. Patch git format-patch -1 4e54fc0b91ca7a4180307874f72f3b32eb3dca87 --stdout em /workspace/work/release-0136/correcao-render.patch; SHA-256 eb9ba66cf952555e8a13e726f0b6c6e813581890b299a134ec1b4ddaea9b7dee.

Workflow acionado explicitamente no mesmo ref: https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264, criado em 2026-11-15T19:57:33Z, headSha 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. Nenhuma etapa de testes/build/pacote/revisão foi ignorada ou alterada. Confirmação final de publicação ainda pendente nesta seção de acompanhamento.

## conferir-release-anterior

UTC: 2026-11-15T20:05:35.943171+00:00

Comando: `["git", "ls-remote", "origin", "refs/tags/v0.1.35", "refs/tags/v0.1.36"]`

stdout integral:
```text
df5ff41e74b36cea4e2abd160e1172f4166bf32a	refs/tags/v0.1.35

```

stderr integral:
```text

```

Código de saída: 0

## release-publicada

UTC: 2026-11-15T20:10:46.477975+00:00

Comando: `["gh", "release", "view", "v0.1.36", "--repo", "pedroalexcarneiro/Checkpoint", "--json", "url,tagName,name,isPrerelease,isDraft,publishedAt,targetCommitish,assets"]`

stdout integral:
```text
{"assets":[{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207421","contentType":"image/png","createdAt":"2026-11-15T20:10:30Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cY9","label":"","name":"Checkpoint-0.1.36-detail-overview.png","size":96121,"state":"uploaded","updatedAt":"2026-11-15T20:10:30Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-detail-overview.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207418","contentType":"image/png","createdAt":"2026-11-15T20:10:30Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cY6","label":"","name":"Checkpoint-0.1.36-home.png","size":123033,"state":"uploaded","updatedAt":"2026-11-15T20:10:30Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-home.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207420","contentType":"image/png","createdAt":"2026-11-15T20:10:30Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cY8","label":"","name":"Checkpoint-0.1.36-library.png","size":143770,"state":"uploaded","updatedAt":"2026-11-15T20:10:30Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-library.png"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207422","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-15T20:10:30Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cY-","label":"","name":"Checkpoint-0.1.36-ui-review.txt","size":560,"state":"uploaded","updatedAt":"2026-11-15T20:10:30Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-ui-review.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207419","contentType":"application/zip","createdAt":"2026-11-15T20:10:30Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cY7","label":"","name":"Checkpoint-0.1.36-ui-review.zip","size":4095105,"state":"uploaded","updatedAt":"2026-11-15T20:10:31Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-ui-review.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207433","contentType":"text/plain; charset=utf-8","createdAt":"2026-11-15T20:10:31Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cZJ","label":"","name":"Checkpoint-0.1.36-validation.txt","size":684,"state":"uploaded","updatedAt":"2026-11-15T20:10:31Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-validation.txt"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207438","contentType":"application/zip","createdAt":"2026-11-15T20:10:31Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cZO","label":"","name":"Checkpoint-0.1.36-windows-x64.zip","size":84229223,"state":"uploaded","updatedAt":"2026-11-15T20:10:34Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-windows-x64.zip"},{"apiUrl":"https://api.github.com/repos/pedroalexcarneiro/Checkpoint/releases/assets/752207440","contentType":"application/octet-stream","createdAt":"2026-11-15T20:10:31Z","downloadCount":0,"id":"RA_kwDOVpnrA84s1cZQ","label":"","name":"Checkpoint-0.1.36-windows-x64.zip.sha256","size":101,"state":"uploaded","updatedAt":"2026-11-15T20:10:31Z","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/download/v0.1.36/Checkpoint-0.1.36-windows-x64.zip.sha256"}],"isDraft":false,"isPrerelease":true,"name":"Checkpoint 0.1.36 · Interface e PT-BR","publishedAt":"2026-11-15T20:10:34Z","tagName":"v0.1.36","targetCommitish":"main","url":"https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.36"}

```

stderr integral:
```text

```

Código de saída: 0

## tag-publicada

UTC: 2026-11-15T20:10:46.973561+00:00

Comando: `["git", "ls-remote", "origin", "refs/tags/v0.1.36"]`

stdout integral:
```text
4e54fc0b91ca7a4180307874f72f3b32eb3dca87	refs/tags/v0.1.36

```

stderr integral:
```text

```

Código de saída: 0

## conferir-assets-publicados

UTC: 2026-11-15T20:11:08.669157+00:00

Comando: `["/workspace/work/venv/bin/python", "/workspace/work/release-0136/verify_assets.py"]`

stdout integral:
```text
Tag confirmada: 4e54fc0b91ca7a4180307874f72f3b32eb3dca87
0049d9e10aff3cf759c781d90b736c5b8c571d624d7c1e5f99484757d4333d0e 96121 Checkpoint-0.1.36-detail-overview.png
53d654aa4230529f5b8850559c91ea0e65d5a3dfc5a20e1484a1da7bee226548 123033 Checkpoint-0.1.36-home.png
526fe30fb3714e3e19a3eb6e5f3a34121a222971ab883e4bcb39d5392c81ab00 143770 Checkpoint-0.1.36-library.png
66cdff94242415962d84b977c999749fe2b1846f574857ab8bb2afe7cc20ff3f 560 Checkpoint-0.1.36-ui-review.txt
3b11f04efa73dd31d71bc948442e77386464bb93c3e0bdee17001b60fe705825 4095105 Checkpoint-0.1.36-ui-review.zip
b534ada487476d094227522020c61c83f9ffedafc2e5ac069df7c8b8e584bd46 684 Checkpoint-0.1.36-validation.txt
d2fffc594295ec9cd8800300ce4a7535f60ce76211d63454e0544d276cdfb69a 84229223 Checkpoint-0.1.36-windows-x64.zip
b3828c0a8068d72a5a7b3bf3aeaedefd53e5f6884f5efc7ae81bf3905b8ca3b8 101 Checkpoint-0.1.36-windows-x64.zip.sha256

Validação do pacote:
Checkpoint 0.1.36 · Windows x64
Commit: 4e54fc0b91ca7a4180307874f72f3b32eb3dca87
Python: 3.12.10
Testes: {'tests': 613, 'failures': 0, 'errors': 0, 'skipped': 0}
Smoke do fonte: 6 páginas; SQLite íntegro; biblioteca vazia.
Smoke do ZIP extraído: 6 páginas; SQLite íntegro; biblioteca vazia.
Auxiliar isolado do fonte e do ZIP extraído: resposta e schema verificados.
Cadastro completo do fonte e do ZIP: salvar, auxiliar, imagem e SQLite verificados (fixture isolada).
CheckpointUpdater.exe --check: saída 0.
ZIP SHA-256: d2fffc594295ec9cd8800300ce4a7535f60ce76211d63454e0544d276cdfb69a
Steam autenticada e homologação Windows 10/11 pessoal não estão cobertas.

Revisão visual:
Checkpoint 0.1.36 · Revisão visual
Plataforma: win32
Commit: 4e54fc0b91ca7a4180307874f72f3b32eb3dca87
Capturas Qt: 61
Janelas: 1920×1080, 1100×740 e 1000×700; editor, cadastro e diálogos em suas dimensões próprias.
Nove temas escuros, Verde padrão; capturas incluem verde, roxo e azul.
Fixtures isoladas: jogos, sessões, metas e artes. Nenhuma conta autenticada.
Conteúdo publicado: capturas PNG e index.html. Base, logs e artes auxiliares excluídos.
SHA-256 ui-review.zip: 3b11f04efa73dd31d71bc948442e77386464bb93c3e0bdee17001b60fe705825

RELEASE E OITO ARQUIVOS CONFERIDOS

```

stderr integral:
```text

```

Código de saída: 0

## execucao-final

UTC: 2026-11-15T20:11:09.845874+00:00

Comando: `["gh", "run", "view", "43755297264", "--repo", "pedroalexcarneiro/Checkpoint", "--json", "status,conclusion,headSha,jobs,url"]`

stdout integral:
```text
{"conclusion":"success","headSha":"4e54fc0b91ca7a4180307874f72f3b32eb3dca87","jobs":[{"completedAt":"2026-11-15T20:10:22Z","conclusion":"success","databaseId":132937969644,"name":"build","startedAt":"2026-11-15T19:57:36Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":3,"status":"completed"},{"conclusion":"success","name":"Check release version","number":4,"status":"completed"},{"conclusion":"success","name":"Install tested Windows dependencies","number":5,"status":"completed"},{"conclusion":"success","name":"Test on Windows","number":6,"status":"completed"},{"conclusion":"success","name":"Build desktop and updater","number":7,"status":"completed"},{"conclusion":"success","name":"Package and validate extracted executable","number":8,"status":"completed"},{"conclusion":"success","name":"Render Windows interface review","number":9,"status":"completed"},{"conclusion":"success","name":"Upload verified release files","number":10,"status":"completed"},{"conclusion":"success","name":"Preserve Windows test report","number":11,"status":"completed"},{"conclusion":"success","name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","number":21,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":22,"status":"completed"},{"conclusion":"success","name":"Complete job","number":23,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264/job/132937969644"},{"completedAt":"2026-11-15T20:10:36Z","conclusion":"success","databaseId":132941753371,"name":"publish","startedAt":"2026-11-15T20:10:23Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":2,"status":"completed"},{"conclusion":"success","name":"Run actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093","number":3,"status":"completed"},{"conclusion":"success","name":"Publish development release","number":4,"status":"completed"},{"conclusion":"success","name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","number":8,"status":"completed"},{"conclusion":"success","name":"Complete job","number":9,"status":"completed"}],"url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264/job/132941753371"}],"status":"completed","url":"https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/43755297264"}

```

stderr integral:
```text

```

Código de saída: 0

## Resultado final — publicada e conferida

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.36
Publicada em 2026-11-15T20:10:34Z (17h10min34s em America/Sao_Paulo), pré-release, não rascunho. Tag leve v0.1.36 aponta exatamente para 4e54fc0b91ca7a4180307874f72f3b32eb3dca87. O campo targetCommitish da API informa main, mas a referência efetiva da tag foi conferida pela API Git e por git ls-remote: ambos confirmam o commit validado da branch fix/0.1.36-ajustes. main não foi alterada.

Workflow 43755297264: build e publish success. Windows/Python 3.12.10: **613 passed in 582.04s (0:09:42)**, 0 falhas/erros/skips. Build desktop/updater, pacote extraído, cadastro/auxiliar, revisão visual com 61 PNGs e publicação aprovados. Log completo recebido pela ferramenta GitHub e preservado em /workspace/work/release-0136/segundo-job-plugin.log, SHA-256 309f9f8d031a70fed0af0d0323cb770f1ad8f939b40f4b29c7c76536e6d13b49. Eventuais caracteres substituídos pelo transporte da ferramenta foram preservados.

Download real dos oito assets via gh release download v0.1.36 --repo pedroalexcarneiro/Checkpoint --dir /workspace/work/release-0136/assets: stdout vazio, stderr vazio, exit 0. Todos os tamanhos e SHA-256 locais iguais aos digests publicados pelo GitHub. Checksum do ZIP Windows confere com .sha256 e validation.txt; checksum da revisão confere com ui-review.txt. Ambos os ZIPs passaram também na verificação CRC local. Lista completa e hashes na saída conferir-assets-publicados acima e em /workspace/work/release-0136/asset-hashes.json. Nenhum arquivo pessoal publicado.

Limitações preservadas nas notas públicas: cobertura autenticada de consoles e preço original individual da API (02/03), captura real de jogo/processos-filhos/launchers não homologados (06), A4 e encerrar apenas a ROM mantendo o emulador aberto. Runner Windows e fixtures não validam contas ou o PC do dono. Schema 4 inalterado; nenhuma migração pessoal ou acesso à base do dono. Releases/tags anteriores, workflows, assets fonte e arquivos protegidos preservados; sem force push nem PR.

Atualização documental final em CONTINUITY.md, PROJECT_STATUS.md, CHANGELOG.md, ROADMAP.md e neste relatório; posterior ao código publicado. Não move a tag nem exige novo build, pois não altera código/dependências/assets/workflows. Fonte e correção estão no histórico GitHub; os arquivos de release correspondem ao commit da tag, não a este registro posterior.

## Saída da suíte Windows concluída

Trecho integral de stdout da execução pytest (progresso e resultado), extraído do log do job com seus horários UTC:

```text
2026-11-15T19:59:01.6512822Z ........................................................................ [ 11%]
2026-11-15T19:59:10.7364003Z ........................................................................ [ 23%]
2026-11-15T19:59:25.1976935Z ........................................................................ [ 35%]
2026-11-15T19:59:31.2281332Z ........................................................................ [ 46%]
2026-11-15T20:01:19.5628146Z ........................................................................ [ 58%]
2026-11-15T20:01:57.9379133Z ........................................................................ [ 70%]
2026-11-15T20:03:41.9144853Z ........................................................................ [ 82%]
2026-11-15T20:07:57.5205456Z ........................................................................ [ 93%]
2026-11-15T20:08:32.1942935Z .....................................                                    [100%]
2026-11-15T20:08:32.1943566Z 613 passed in 582.04s (0:09:42)
```

LANÇAMENTO 0.1.36 CONCLUÍDO

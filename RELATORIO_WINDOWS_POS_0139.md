# Validação Windows e pacote da revisão pós-0.1.39

Continuidade solicitada pelo dono após o fechamento local: validar no Windows e gerar o ZIP. Nenhuma nova publicação autorizada/executada nesta etapa.

Fonte enviada: `9a658569309ad49d4d138c226e83ef2c2f80849c`, branch `fix/pos-0139-layout`. Checkout limpo antes do envio. Código funcional idêntico ao gate de 808 testes Linux; documentação posterior em 9a65856.

Workflow existente **Windows UI validation**, execução https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/44749088810. Permissão contents:read; gera artifacts, sem job de publicação. Nenhum workflow foi alterado. A versão interna continua 0.1.39; este pacote de revisão será identificado também pelo SHA, sem substituir o ZIP da release publicada.

## Entrega de código

```text
9a658569309ad49d4d138c226e83ef2c2f80849c docs: fechar revisao local com 808 testes e capturas finais
d808f76a36663bd031a230b0a0f3f08a2f3fb6cb feat: completar descontos por oferta e conferir a edicao do produto
f4a7139736c6b164dcdc12522b52f8c3f75eb38e feat: adaptar cores e superficies aos modos claro e escuro
7a7c7d9b9e3c2d470b9306aec465730e65bda15f fix: mostrar jogos unicos e manter memorias no tamanho padrao
```

| Commit | SHA-256 do format-patch |
|---|---|
| 9a658569309ad49d4d138c226e83ef2c2f80849c | e5a116891b9bd15abe3946e21ca656b3e0090ef881a2953c551f32e8ef7853f9 |
| d808f76a36663bd031a230b0a0f3f08a2f3fb6cb | 2e542d1a94fd8993ed5926abde3923e1aa847b271e3a99f71ff3ae0b699e6a9d |
| f4a7139736c6b164dcdc12522b52f8c3f75eb38e | 1aac8dbc778a746dbd653b2bac1ee7ad3fd0b0922456eec8a0ee76a80207ed1e |
| 7a7c7d9b9e3c2d470b9306aec465730e65bda15f | 3a7e246edf5865cba568e1e7a66f05d5ece6e35070d4389329d285afcf97d7ca |

## Envio e execução

### push

```json
{
  "command": [
    "git",
    "push",
    "origin",
    "fix/pos-0139-layout"
  ],
  "started": 1795183110.6015365,
  "exit_code": 0,
  "elapsed": 2.082303285598755
}
```

```sh
git push origin fix/pos-0139-layout
```

stdout:

````text

````

stderr:

````text
remote: 
remote: Create a pull request for 'fix/pos-0139-layout' on GitHub by visiting:        
remote:      https://github.com/pedroalexcarneiro/Checkpoint/pull/new/fix/pos-0139-layout        
remote: 
To https://github.com/pedroalexcarneiro/Checkpoint.git
 * [new branch]      fix/pos-0139-layout -> fix/pos-0139-layout
````
### dispatch

```json
{
  "command": [
    "gh",
    "workflow",
    "run",
    "windows-ui-validation.yml",
    "--repo",
    "pedroalexcarneiro/Checkpoint",
    "--ref",
    "fix/pos-0139-layout"
  ],
  "source_sha": "9a658569309ad49d4d138c226e83ef2c2f80849c",
  "started": 1795183127.0512502,
  "exit_code": 0,
  "elapsed": 1.8861398696899414
}
```

```sh
gh workflow run windows-ui-validation.yml --repo pedroalexcarneiro/Checkpoint --ref fix/pos-0139-layout
```

stdout:

````text

````

stderr:

````text

````

Confirmação remota:

```text
9a658569309ad49d4d138c226e83ef2c2f80849c	refs/heads/fix/pos-0139-layout
```

## Resultado Windows e pacote

Execução **44749088810 concluída com sucesso**, Windows-2022/Python 3.12.10.
JUnit: **808 testes, zero falhas, erros e skips**, em **788,60 s (13min08s)**.
Log e XML em evidence/windows-pos-0139/. Build do desktop e
atualizador aprovado. Fonte e executável extraído passaram nos smokes de seis
páginas, cadastro, auxiliar, SQLite e abertura normal com Qt windows. Runner
já elevado; não comprova consentimento UAC no computador do dono.

Pacote: **84357755 bytes**, SHA-256
`b24b3bac05b3705b368a29a4bc7ae6a88415786c318f1e12a515e51909e0b896`.
CRC do ZIP e sidecar SHA-256 conferidos. Os dois artifacts baixados também
conferem com os digests do GitHub. Download inicial por gh foi recusado pelo
host de armazenamento (HTTP 403); o conector GitHub forneceu os mesmos arquivos,
baixados e verificados com sucesso. Nenhum URL assinado foi versionado.

Artifact completo, disponível até 04/12/2026 (login GitHub necessário):
https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/44749088810/artifacts/14635591757
Dentro dele, o aplicativo está em `Checkpoint-0.1.39-windows-x64.zip`.
Cópia local identificada como `Checkpoint-pos-0.1.39-9a65856-windows-x64.zip`,
com bytes e hash idênticos. Não é nova release/versão publicada.

Tag v0.1.39 continua em 7703d8048884009a5d9e9addb348620d4a788ff0.
Metadados, corpo e dez assets da release publicada comparados antes/depois:
mesmos IDs, tamanhos e digests, sem substituição. Workflows sem alteração;
apenas Windows UI validation executado nesta branch.

Evidências verificadas (SHA-256 de cada arquivo e XML/contagem) em
`evidence/windows-pos-0139/verified-files.json`; log integral baixado em
`evidence/windows-pos-0139/workflow.txt`. Nenhum banco, ROM, save, token ou dado
pessoal incluído. Capturas são de fixtures do runner.


## Limites

Fixtures/runner não homologam HSR, emuladores, contas/cofre ou UAC no PC do dono. API autenticada não validada; consulta console continua sem cobertura confirmada. Protegidos, schema, dados e fluxos A4 preservados.

Espaços finais dentro dos blocos de stdout/stderr de git push foram preservados
para manter a saída integral. Não são alterações de código.

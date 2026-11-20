# Checkpoint 0.1.39 — lançamento publicado e verificado

Autorização posterior explícita do dono: “ok, quando finalizar, pode já dar
release no github”, após comunicação da pendência de consulta console.
Pode enviar o código validado e usar o workflow Windows release existente.
Sem force push, sem reescrever tags/releases/arquivos publicados anteriores,
sem PR ou mudança de workflows. A publicação continua condicionada aos testes.

Branch de trabalho: fix/0.1.39-polimento, da base normal 0.1.38 em
9dd9c93ce7baf0051bbc783323b401d4ba8c7059. Variante sem administrador preservada.
Versão alvo correta: 0.1.39, nunca 1.39. Padrão de pré-release do workflow mantido.

Gates previstos: suíte integral Linux, fonte/smokes/SQLite, inspeção dos
contratos, commit/checkout limpos, envio sem força, suíte integral Windows,
build, fonte e executável extraído abrindo normalmente com Qt windows,
smokes anteriores/worker/cadastro/atualizador, revisão visual e hashes do pacote.
Publisher só executa se o build completo aprovar; nenhuma release declarada
antes de confirmar tag/arquivos e downloads.

Pendências públicas obrigatórias: preços console sem prova autenticada,
saves sem upload Drive e limitação de fechar apenas ROM com emulador vivo.
Runner Windows não equivale a homologar uso/contas/captura/UAC no PC do dono.

Resultados, SHAs, run, assets e SHA-256 serão registrados após as verificações.

## Gate Linux complementar aprovado — código atual

Após os relatos novos e o degradê aprovado: 764 passed in 487.00s (0:08:07),
exit 0, código 03272d021b70c5584b424445d53aa3a18c70ac62. Nenhuma mudança de
asserção antiga nesses complementos. Primeiro ensaio interrompido com erro
de Mock/medição, corrigido no código, com todos os logs preservados.
Qt offscreen/CHECKPOINT_TEST_ROOT=/tmp; smokes e contratos aprovados. Fonte,
testes e scripts congelados; alterações seguintes apenas documentais/capturas.
Envio da branch e workflow Windows serão registrados a seguir, sem antecipar
publicação nem homologação HSR/DirectX/PC do dono.

## Gate Linux inicial — anterior aos complementos

752 passed in 577.63s (0:09:37), exit 0, Linux/Python 3.12.14/Qt offscreen,
CHECKPOINT_TEST_ROOT=/tmp; código/testes em 8dd4c24a9aa73d716dc5c2bd7fc9f805e2a44767.
Primeiras tentativas/falhas integralmente preservadas em RELATORIO_0139_TESTES.md.
Smokes de seis páginas/worker/SQLite/cadastro aprovados. Verificação de bytes,
AST de bootstrap, schema 4, assets, workflows e oito paletas aprovada.
Após esse código só documentação/capturas/notas públicas; o envio levará essa
mesma árvore de aplicação/testes ao workflow Windows release, sem mudar o YAML.

## Envio e início da validação Windows

Fonte enviada: `7703d8048884009a5d9e9addb348620d4a788ff0`. Checkout limpo antes do envio; referências
remotas 0.1.39 ainda ausentes. Nenhum diff de aplicação/scripts/testes em relação
a 03272d0, onde os 764 testes Linux passaram. Push sem força; confirmação remota
do mesmo SHA. Nenhuma execução automática surgiu pelo push.

Workflow existente disparado conforme autorização: [44660106137](https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/44660106137), workflow_dispatch, mesmo SHA.
Nenhum workflow foi alterado. Testes/build/publicação ainda aguardando resultado.

### source-candidate

```json
{
  "sha": "7703d8048884009a5d9e9addb348620d4a788ff0",
  "checks": [
    {
      "command": [
        "git",
        "rev-parse",
        "HEAD"
      ],
      "stdout": "7703d8048884009a5d9e9addb348620d4a788ff0\n",
      "stderr": "",
      "exit_code": 0
    },
    {
      "command": [
        "git",
        "status",
        "--porcelain"
      ],
      "stdout": "",
      "stderr": "",
      "exit_code": 0
    },
    {
      "command": [
        "git",
        "ls-remote",
        "origin",
        "refs/heads/fix/0.1.39-polimento",
        "refs/tags/v0.1.39"
      ],
      "stdout": "",
      "stderr": "",
      "exit_code": 0
    },
    {
      "command": [
        "git",
        "diff",
        "--name-only",
        "03272d021b70c5584b424445d53aa3a18c70ac62",
        "HEAD",
        "--",
        "checkpoint",
        "scripts",
        "tests",
        "pyproject.toml",
        "requirements-tested.txt"
      ],
      "stdout": "",
      "stderr": "",
      "exit_code": 0
    }
  ]
}
```

### push-source

```json
{
  "command": [
    "git",
    "push",
    "origin",
    "fix/0.1.39-polimento"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795141226.9601884,
  "exit_code": 0,
  "elapsed": 2.72184419631958
}
```

stdout integral:

```text

```

stderr integral:

```text
remote: 
remote: Create a pull request for 'fix/0.1.39-polimento' on GitHub by visiting:        
remote:      https://github.com/pedroalexcarneiro/Checkpoint/pull/new/fix/0.1.39-polimento        
remote: 
To https://github.com/pedroalexcarneiro/Checkpoint.git
 * [new branch]      fix/0.1.39-polimento -> fix/0.1.39-polimento
```

### confirm-source-remote

```json
{
  "command": [
    "git",
    "ls-remote",
    "origin",
    "refs/heads/fix/0.1.39-polimento"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795141235.1972308,
  "exit_code": 0,
  "elapsed": 0.24373483657836914
}
```

stdout integral:

```text
7703d8048884009a5d9e9addb348620d4a788ff0	refs/heads/fix/0.1.39-polimento
```

stderr integral:

```text

```

### dispatch-windows

```json
{
  "command": [
    "gh",
    "workflow",
    "run",
    "windows-release.yml",
    "--ref",
    "fix/0.1.39-polimento",
    "--repo",
    "pedroalexcarneiro/Checkpoint"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795141242.184171,
  "exit_code": 0,
  "elapsed": 1.7739243507385254
}
```

stdout integral:

```text

```

stderr integral:

```text

```

## Resultado Windows e publicação confirmada

Workflow https://github.com/pedroalexcarneiro/Checkpoint/actions/runs/44660106137: build e publish concluídos com success. Fonte/tag `7703d8048884009a5d9e9addb348620d4a788ff0`.

Windows/Python 3.12.10: **764 passed in 664.04s (0:11:04)**;
JUnit 764/0 falhas/0 erros/0 skips, artefato 14595283978 conferido por SHA-256.
Linux: **764 passed in 487.00s**, exit 0, mesma árvore de aplicação/testes.
Os dois testes de janela controlada confirmaram quadros vermelho/azul distintos
com Qt windows e GDI nativo. Isso não homologa HSR/DirectX/tela cheia do dono.

O fonte e o executável extraído passaram por abertura normal com HWND visível/
responsivo, captura e fechamento; SQLite íntegro, seis páginas, cadastro completo,
auxiliar/schema e atualizador aprovados. Runner já elevado: consentimento UAC
interativo/conta/cofre/emuladores/contas reais continuam não homologados.

Logs completos dos dois jobs em RELATORIO_0139_TESTES.md. Nenhum workflow foi
alterado, nenhum PR/merge ou force push. A documentação posterior não move a tag.

### Verificação pública dos arquivos

Release: https://github.com/pedroalexcarneiro/Checkpoint/releases/tag/v0.1.39 (prerelease, padrão existente).
Os dez arquivos foram baixados sem autenticação pelo link público e conferidos
por tamanho/SHA-256 contra o digest GitHub; CRC dos dois ZIPs aprovado.
Saída completa do verificador em RELATORIO_0139_TESTES.md (verify-published).

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| Checkpoint-0.1.39-detail-overview.png | 144968 | 5ed57f2c8420906073ea78b71fa3d88f3431b4418d5c3377dd422274a94f9a9e |
| Checkpoint-0.1.39-home.png | 146649 | ad5aefe95e55af40de7030a76a505255d3d6e7130caff18c924af78c7e6c6a24 |
| Checkpoint-0.1.39-library.png | 164658 | 2c1d88122f5216b891dcceb88cd7bfc7ade827f78636e228ed755b7a540c2cae |
| Checkpoint-0.1.39-native-startup.json | 284 | 046e35968f6f8b6f6256c778f48dda71cded9cd484f913e6afc4ce8859115bd2 |
| Checkpoint-0.1.39-native-startup.png | 165601 | afbd6259905b068a17d093a8cdffca39d0c223d630e88abaf889303e4e4d4869 |
| Checkpoint-0.1.39-ui-review.txt | 560 | 901ba4c188aa4c4f0e3bc6acc0d3a50240203f1dd55fcfd17d522a90b2a486c7 |
| Checkpoint-0.1.39-ui-review.zip | 5901996 | ff8f78c7b014bca6d7a28d6812285adfbaf38fb2e6cd5610b174ef524a7a7895 |
| Checkpoint-0.1.39-validation.txt | 884 | 7985a0601ed045a3830c3646de3db2abd981a96be8c66ff5a39a20ee7e617293 |
| Checkpoint-0.1.39-windows-x64.zip | 84345311 | dc6132969de8622e64ab4a36afbc0197c8de527a55cd6ad040813d18ddc9f4a3 |
| Checkpoint-0.1.39-windows-x64.zip.sha256 | 101 | ab0a5f28c57455d496eb799117f54247c5f3236d01514de6c0c8f8d619110a25 |

Tags e arquivos anteriores preservados: v0.1.38 em c4a7e1d221ba52a8580dd73ab884b1964e6ffd32 (10 arquivos), v0.1.37 em c526cb4bc5e8721dfdfdf20222c8c1c41562ce52 (8 arquivos). IDs, nomes, tamanhos e digests iguais ao estado anterior.

### Limites e revisão

HSR real ainda requer confirmação do dono. Console sem prova autenticada de
oferta, saves sem upload Drive e fechar somente ROM permanecem limitações,
sem reidentificação automática nem mudança de A4/contratos protegidos.
Não declarar o projeto inteiro concluído.

Revisão: commits da branch fix/0.1.39-polimento; diff da base 9dd9c93 até a tag
7703d80; PLANO/RELATORIO/TESTES 0139; capturas reais/fixtures em
evidence/ui-0.1.39 e complementos, com manifesto/hashes. Patches completos
dos 26 commits até o candidato enviado estão registrados no relatório principal;
commits documentais posteriores permanecem no Git sem reescrever histórico.

SHA-256 RELATORIO_0139.md: 92cd3930e18c422456e8ca706b758c4377f8b450459bb757b3e99c90d7541972

SHA-256 RELATORIO_0139_TESTES.md: c8f3ca28468714680ccd5d77ef0a7eab08b0c5e0c2ea6a170d3e50c734e0309c

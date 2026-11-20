# Checkpoint 0.1.39 — preparação do lançamento autorizado

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

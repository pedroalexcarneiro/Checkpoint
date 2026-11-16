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

# Checkpoint 0.1.28

- Renomeação técnica para Checkpoint, com migração não destrutiva dos dados e do cofre. A pasta anterior é preservada; o banco continua no schema 4.
- Biblioteca com quatro colunas de capas verticais, Desejos com logos contidas, Início com continuidade e ficha com galeria.
- Cadastro com seleção, dados e imagens em segundo plano; confirmação de desejos e proteção dos jogos já possuídos.
- Nove temas, com Verde como padrão. O tema Branco foi removido.

## Baixar e usar

Baixe **Checkpoint-0.1.28-windows-x64.zip**, extraia a pasta inteira e abra **Checkpoint.exe**. O arquivo `.sha256` permite conferir o pacote.

## Validação e limites

252 testes aprovados em Linux e Windows CI; build, smokes do código-fonte e do executável extraído, SQLite e capturas aprovados. O pacote publicado é o mesmo artefato do CI, sem recompilação.

Código-fonte da revisão: `21ca701`; binário construído em `124daab`. Entre esses commits há somente relatório, documentação e capturas, sem mudanças no código do aplicativo.

A interface ainda apresenta diferenças em relação às referências, documentadas no `RELATORIO_CORRECOES.md`, incluindo monogramas de SteamGridDB/RAWG. DPI, contas reais e o Windows pessoal do usuário não foram homologados. A futura unificação dos componentes de cadastro continua pendente de decisão.

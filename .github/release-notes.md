Ficha e imagens ao adicionar jogos à biblioteca.

- Steam: após importar os jogos selecionados, o Checkpoint busca ficha e imagens pelo AppID, sem chave adicional para a loja.
- ROMs e cadastro manual: ao salvar, confirme o jogo no catálogo. Steam fornece dados de jogos de PC; RAWG cobre outras plataformas com chave própria; SteamGridDB complementa artes com chave própria.
- Configurações > Completar fichas e imagens faltantes da biblioteca permite atualizar cadastros já identificados. Cadastros sem identidade podem ser identificados em Editar jogo.
- Campos e imagens existentes são preservados no preenchimento automático. Categoria, nota, status e observações são pessoais.
- Consultas têm progresso e podem ser interrompidas após o jogo atual. Falhas de rede não desfazem o cadastro. É possível cadastrar offline desmarcando a busca no formulário.
- Ficha e imagens dependem da disponibilidade da fonte; alguns jogos não oferecem logo ou capa vertical. RAWG usa a imagem de fundo como capa/banner, exibida inteira.
- SQLite permanece no schema 4. Nenhuma biblioteca pessoal ou credencial é incluída no pacote.

Baixe **Checkpoint-0.1.15-windows-x64.zip**, extraia a pasta Checkpoint completa e abra Checkpoint.exe. Preserve `_internal` e `CheckpointUpdater`.

A publicação exige a validação Windows do workflow. Consulte o arquivo de validação da compilação; testes com respostas controladas não comprovam acesso autenticado. O projeto completo permanece em desenvolvimento.

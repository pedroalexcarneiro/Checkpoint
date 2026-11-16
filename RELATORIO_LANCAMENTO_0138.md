# Lançamento 0.1.38 — autorizado, em execução

O dono autorizou explicitamente publicar a correção após revisar os resultados e receber o pacote validado. A 0.1.37/tag/arquivos permanecem preservados. Candidato funcional validado: ff136584974b55989c10598612235717508ec25a; Windows UI validation 43799707113, 700 testes Windows, build, smokes e abertura normal do fonte e executável extraído aprovados; Linux 700 testes.

Primeira tentativa de publicação pela CLI: GitHub API autenticada, mas upload para uploads.github.com retornou HTTP 401 Bad credentials. A verificação posterior não encontrou release/tag 0.1.38 nem rascunho remanescente. Nenhum pacote parcial é apresentado como publicação. Não foram registrados tokens ou links assinados.

Alternativa: workflow Windows release existente, sem alteração no seu código, usando GITHUB_TOKEN do próprio GitHub. Notas públicas atualizadas para a 0.1.38 após autorização; novo commit só documental/notas, sem mudança funcional desde ff13658. Workflow repetirá testes/build/smokes/abertura nativa e publicará somente após aprovação. Tags e releases anteriores não serão movidas ou sobrescritas.

Resultados e verificação final serão acrescentados após conclusão. A validação de abertura é de Windows já elevado no runner; consentimento UAC real e uso no PC do dono não são homologados por isso.

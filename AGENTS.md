# Checkpoint — instruções para continuidade

Leia primeiro `CONTINUITY.md`, depois o resumo atual de `PROJECT_STATUS.md`,
`ARCHITECTURE.md`, `ROADMAP.md` e os documentos da área alterada.

- O produto se chama **Checkpoint**. `checkpoint` e o diretório de dados
  `Checkpoint` são identificadores legados necessários à compatibilidade.
- Desenvolva nos arquivos, com funcionalidades reais, estados vazios e erros úteis.
  Não apresente dados fictícios, APIs simuladas ou testes substituídos como validação real.
- Preserve a separação entre interface PySide6, serviços, SQLite e provedores.
  Migrações devem preservar dados e ter testes; nunca recrie o banco do usuário.
- Português brasileiro na interface e comunicação. Sem slogans/subtítulos promocionais.
  Temas discretos e coesos; capas verticais com imagem inteira, sem deformar ou cortar texto; título e status
  alinhados à borda real da imagem.
- Não associe ROM por semelhança fraca. Preserve `original_name`, IDs Drive e versões.
  A escolha explícita no catálogo pode padronizar o título exibido.
- Scanner Drive lê metadados; download somente sob demanda. Não implemente exclusão
  remota. Download local permanece até remoção explícita pelo usuário.
- Backup cobre saves tradicionais configurados, nunca save states. Preserve uma cópia
  anterior antes de restaurar, valide integridade e não publique arquivos em alteração.
- Não versione tokens, JSON OAuth, bancos pessoais, logs privados, ROMs, saves ou mídias.
  Credenciais do Windows não existem automaticamente na nuvem. Não use cofre em texto claro.
- Trabalhe autonomamente dentro do pedido; não solicite testes/comandos no PC do usuário
  quando testes isolados forem possíveis. Não declare validação Windows a partir de Linux.
- Execute `python -m pytest tests -q -p no:cacheprovider`. Qt usa `offscreen` nos testes.
  No Linux, consulte `CLOUD_SETUP.md` para dependências nativas. Integrações usam substitutos
  nos testes; mantenha testes autenticados separados e explicitamente documentados.
- Use `--data-dir` isolado em smoke tests. Nunca abra a base pessoal para testar migrações.
- Atualize `PROJECT_STATUS.md`, `CONTINUITY.md` e documentação pertinente ao entregar.
  Registre limitações e resultados efetivos. O projeto completo ainda não está concluído.
- Publique código fonte em commits do repositório; ZIP em Releases não substitui isso.
  Preserve o histórico remoto, não faça force push e não altere tags de releases existentes.

# Integrações

## Steam

Importação por SteamID64 público e chave Web API pessoal configurada no cofre. Biblioteca privada e restrições da conta podem impedir acesso. O catálogo público da loja pode fornecer ficha e artes sem garantir cobertura de todos os jogos.

## Google Drive

OAuth com acesso de leitura. O índice preserva IDs, nomes originais, plataformas e versões. Downloads são locais e sob demanda; não há exclusão remota. Associações exigem seleção explícita. Credenciais ficam no cofre, nunca no SQLite.

## SteamGridDB e RAWG

Credenciais próprias configuradas em Conexões. SteamGridDB fornece artes da comunidade e identidades; RAWG fornece metadados. A busca selecionada completa dados e imagens disponíveis em segundo plano, preservando escolhas existentes. Uma fonte não garante todos os campos. Artes animadas ou marcadas como impróprias são rejeitadas pelo fluxo automático.

## GG.deals

Consulta pública de preços em reais, com cache e preservação do último valor válido quando a consulta falha. Links de lojas e afiliados são preservados exatamente como fornecidos pela fonte. A prévia lista somente as ofertas extraídas com segurança; a página externa pode conter ofertas adicionais. Indisponível significa que não há preço utilizável, não preço zero. Bloqueios e desafios de acesso podem impedir a consulta.

## Atualizações

Consulta à API GitHub e download de pacote com tamanho e SHA-256 verificados. O repositório é público. Uma credencial opcional de leitura permanece no cofre; não é transferida ao CDN. Aplicação da atualização preserva a instalação anterior. Esta revisão não altera tags ou releases.

## Validação e segurança

Estados configurados indicam presença de configuração, sem afirmar autenticação verificada. Esta tarefa não usou contas reais. Valores secretos nunca aparecem em logs ou testes em disco. Testes do cofre usam backend fictício em memória. O histórico das implementações e limitações anteriores está em CHANGELOG.md.

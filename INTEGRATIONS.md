# Integrações

## Steam

Importação por SteamID64 público e chave Web API pessoal configurada no cofre. Biblioteca privada e restrições da conta podem impedir acesso. O catálogo público da loja pode fornecer ficha e artes sem garantir cobertura de todos os jogos.

## Google Drive

OAuth com acesso de leitura. O índice preserva IDs, nomes originais, plataformas e versões. Downloads são locais e sob demanda; não há exclusão remota. Associações exigem seleção explícita. Credenciais ficam no cofre, nunca no SQLite.

## SteamGridDB e RAWG

Credenciais próprias configuradas em Conexões. SteamGridDB fornece artes da comunidade e identidades; RAWG fornece metadados. A busca selecionada completa dados e imagens disponíveis em segundo plano, preservando escolhas existentes. Uma fonte não garante todos os campos. Artes animadas ou marcadas como impróprias são rejeitadas pelo fluxo automático.

## GG.deals

A [documentação oficial](https://gg.deals/api/prices/) define o endpoint `https://api.gg.deals/v1/prices/by-steam-app-id/`, com `ids`, `key` e `region=br`. A aplicação usa a identidade `steam` em `external_identifiers`; sem ela, não chama a API e mostra “Sem ID da Steam para consulta”.

Com chave salva, o provedor oficial consulta preços e aceita somente BRL. `currentRetail` e `currentKeyshops` são valores atuais; a interface identifica o menor como Loja oficial ou Keyshop. Valores nulos ou zero são indisponíveis. `historicalRetail` e `historicalKeyshops` alimentam somente “Menor histórico”. Não são preço de lista: a API não fornece preço original nem desconto percentual. Descontos só aparecem se a página pública fornecer explicitamente o preço original da mesma oferta.

O [GG.deals informa uso gratuito](https://gg.deals/api/) para projetos pessoais, hobby e open source, com atribuição obrigatória. Desejos e a ficha com preços mostram “Preços: GG.deals”, com link ativo para https://gg.deals/. Links recebidos da fonte não têm afiliados/referrals alterados.

Em Configurações > Conexões, o card GG.deals permite Salvar/Remover a chave exclusivamente no cofre do Windows. O campo é mascarado e limpo após a operação; não mostra a chave armazenada. Há quatro conexões em 2×2 e o quinto card abaixo. Sem chave, o provedor da página pública continua como fallback se a opção em Avançado estiver ativa. Uma chave presente tem prioridade; erro de API preserva o último preço válido, sem fallback silencioso. Alterar configuração permite nova consulta sem apagar o cache.

A documentação limita a API a 100 registros/minuto e 1000/hora. A fila consulta um jogo por vez, com intervalo conservador de 6,5 s e cache de uma hora. HTTP 429, erros de transporte e respostas inválidas recebem mensagens fixas, sem URL autenticada ou corpo de erro. Redirecionamentos autenticados são bloqueados. A consulta real depende da chave e do acesso da instalação Windows; esta revisão usa respostas controladas e não valida conta autenticada.

## Atualizações

Consulta à API GitHub e download de pacote com tamanho e SHA-256 verificados. O repositório é público. Uma credencial opcional de leitura permanece no cofre; não é transferida ao CDN. Aplicação da atualização preserva a instalação anterior. Esta revisão não altera tags ou releases.

## Validação e segurança

Estados configurados indicam presença de configuração, sem afirmar autenticação verificada. Esta tarefa não usou contas reais. Valores secretos nunca aparecem em logs ou testes em disco. Testes do cofre usam backend fictício em memória. O histórico das implementações e limitações anteriores está em CHANGELOG.md.

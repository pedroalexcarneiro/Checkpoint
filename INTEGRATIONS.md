# Integrações

## Steam

Importação por SteamID64 público e chave Web API pessoal configurada no cofre. Biblioteca privada e restrições da conta podem impedir acesso. O catálogo público da loja pode fornecer ficha e artes sem garantir cobertura de todos os jogos.

## Google Drive

OAuth com acesso de leitura. O índice preserva IDs, nomes originais, plataformas e versões. Downloads são locais e sob demanda; não há exclusão remota. Associações exigem seleção explícita. Credenciais ficam no cofre, nunca no SQLite.

## SteamGridDB e RAWG

Credenciais próprias configuradas em Conexões. SteamGridDB fornece artes da comunidade e identidades; RAWG fornece metadados. A busca selecionada completa dados e imagens disponíveis em segundo plano, preservando escolhas existentes. Uma fonte não garante todos os campos. Artes animadas ou marcadas como impróprias são rejeitadas pelo fluxo automático.

## GG.deals

O provedor **Página pública** continua sendo o padrão: consulta HTML BR, mantém links de lojas/afiliados e cache de uma hora, preservando o último preço válido quando há falha. O parser usa o preço original da mesma oferta para calcular desconto; sem original, não inventa percentual. Preço ausente ou zero não é apresentado como oferta utilizável. Bloqueios e mudanças do HTML podem impedir consultas. A página externa pode conter ofertas adicionais.

O contrato PriceProvider retorna preço atual, original, desconto, moeda e lojas. **API oficial GG.deals** é uma implementação separada, desativada sem configuração no cofre. Mesmo com configuração, não realiza chamadas: depende da documentação oficial, a ser fornecida/verificada antes da implementação do transporte. A interface atual continua usando a página pública; não há campo para registrar segredo em arquivo. A decisão sobre a chave depende do dono. Os testes verificam a estrutura com objetos em memória e preços fictícios, não autenticam uma conta nem validam a API real.

## Atualizações

Consulta à API GitHub e download de pacote com tamanho e SHA-256 verificados. O repositório é público. Uma credencial opcional de leitura permanece no cofre; não é transferida ao CDN. Aplicação da atualização preserva a instalação anterior. Esta revisão não altera tags ou releases.

## Validação e segurança

Estados configurados indicam presença de configuração, sem afirmar autenticação verificada. Esta tarefa não usou contas reais. Valores secretos nunca aparecem em logs ou testes em disco. Testes do cofre usam backend fictício em memória. O histórico das implementações e limitações anteriores está em CHANGELOG.md.

# Integrações

## Capacidade e limites da rodada local 0.1.37

Documentação oficial https://gg.deals/api/prices/ inspecionada nesta rodada, cópia SHA-256 1c46c85b1f61b6e52cc055d342f539d2a4d4c21bb110c5117c320465a5a1f544. Endpoint by-slug documentado com key/region, mas resposta não comprova plataforma/edição/loja individual/original. Não há conta/chave autenticada do dono neste ambiente. Consulta console e original individual da API continuam bloqueados, sem novo scraper/fonte. Dropdown PC/Switch/PlayStation/Xbox em Desejos filtra dados existentes e não amplia cobertura de preço. PC não é identidade universal.

ROM local pela ficha funciona offline e usa o arquivo escolhido, sem passar por Drive/cofre/download. Perfis exigem plataforma e extensão explicitamente compatíveis e argumento {rom}; execução reutiliza Launcher/sessões. Drive pela ficha preserva sua origem e rejeita edição/plataforma divergentes antes de vincular/baixar. Cadastro protegido Adicionar jogo > ROM do Drive continua inalterado (A4).

UAC do executável Windows interativo é preparado antes de dados/cofre, com SID original e tratamento de cancelamento. Mudança para outra conta é recusada antes de abrir dados. Captura elevada, launchers, atualizador e cofre reais não foram homologados em Windows nesta rodada.

Decisão posterior do dono na revisão 0.1.36: ausência de preço usa `-` no valor principal, mantendo o motivo curto logo abaixo. Substitui somente o texto Sem preço salvo.

## Revisão de capacidade da fonte — 0.1.36 local

Documentação primária GG.deals consultada em 15/11/2026: https://gg.deals/api/prices/ e changelog oficial de 14/10/2026. Há endpoints por app/sub/bundle Steam e by-slug. O app continua usando app-id para consultas confirmadas de PC; não declara o Steam como identidade universal. Resposta documentada não inclui plataforma/edição, loja individual ou preço original; cobertura do site não comprova cobertura da API. Sem credencial real neste ambiente, console em BRL não foi comprovado. Expansão por slug com vínculo explícito plataforma/edição/proveniência permanece parcial, sem migração especulativa.

Consulta/cache de PC não é mostrado em cadastro de console. Cache com contexto de identidade/edição alterada é preservado e ocultado com motivo. Ofertas oficiais por padrão, keyshops opcionais; desconto deriva somente do original maior da mesma oferta individual BRL e contexto confirmado. Inteiro mais próximo, empate para cima; histórico nunca é original. API agregada não produz desconto. Fallback HTML já existente permanece configurável, sem nova coleta/fonte silenciosa ou substituição de links/referrals.

Captura Windows usa atalho global nativo e exige janela elegível em primeiro plano; Checkpoint pode estar em segundo plano/minimizado. Não há homologação de pixels reais/DirectX, emuladores ou processos-filhos no Windows do dono. Não confundir esses limites com a pendência separada de detectar ROM descarregada com emulador vivo.

## Steam

Importação por SteamID64 público e chave Web API pessoal configurada no cofre. Biblioteca privada e restrições da conta podem impedir acesso. O catálogo público da loja pode fornecer ficha e artes sem garantir cobertura de todos os jogos.

## Google Drive

OAuth com acesso de leitura. O índice preserva IDs, nomes originais, plataformas e versões. Downloads são locais e sob demanda; não há exclusão remota. Associações exigem seleção explícita. Credenciais ficam no cofre, nunca no SQLite.

Na ficha, a seleção de uma ROM é também o pedido explícito de download. A busca respeita título e plataforma, limita a três candidatos e prioriza USA, depois Europe e a revisão mais recente dentro da região. Os vínculos anteriores são desfeitos, sem apagar o índice ou os arquivos locais. O download usa a pasta configurada ou, na primeira solicitação sem pasta, ROMs no diretório de dados. O caminho aparece completo nas Configurações. A pesquisa de dados só aplica uma identidade exata inequívoca; ambiguidades e falhas exigem revisão ou nova tentativa. O fluxo antigo Adicionar jogo > ROM do Drive ainda exige confirmação (A4 bloqueado).

## SteamGridDB e RAWG

Credenciais próprias configuradas em Conexões. SteamGridDB fornece artes da comunidade e identidades; RAWG fornece metadados. A busca selecionada completa dados e imagens disponíveis em segundo plano, preservando escolhas existentes. Uma fonte não garante todos os campos. Artes animadas ou marcadas como impróprias são rejeitadas pelo fluxo automático.

## Wikipédia em português

A fonte de descrição pode ser a Wikipédia em português quando a identificação existente confirma título e plataforma. A busca e a escolha da fonte permanecem inalteradas. Na ficha, só se apresenta o primeiro parágrafo em até três frases, sem datas/anos, números entre parênteses ou trechos de história, versões e listas. O texto armazenado e a proveniência são preservados. Atribuição única do bloco: “Fonte: Wikipédia · CC BY-SA 4.0”, com link para o artigo; nenhum rótulo RAWG/Steam acompanha essa descrição. Metadados e preços continuam com suas respectivas fontes.

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

# Integrações

Pesquisa documental em 10/11/2026. Implementação de cliente não equivale a validação de conta real. Nenhuma credencial foi inventada ou incluída no repositório.

## Google Drive — implementado, autenticação real pendente

Ative a Drive API em um projeto Google Cloud, configure a tela de consentimento e crie um OAuth Client do tipo Desktop. Em modo de teste, autorize a conta desejada. Em Configurações > Google Drive, escolha o JSON de cliente e autentique. O aplicativo abre o fluxo no navegador do ambiente de execução; não depende do computador pessoal do usuário. Sem credenciais disponíveis, não foi iniciado fluxo real nesta sessão.

Escopo de ROMs: `https://www.googleapis.com/auth/drive.readonly`. Ele permite examinar uma coleção existente; `drive.file` sozinho não dá acesso geral às pastas já existentes. A publicação pode exigir verificação Google conforme escopos e uso. Tokens ficam no Windows Credential Manager e são renovados pelo cliente oficial.

Cole o ID da pasta principal, faça a varredura inicial e depois use Atualizar alterações. A captura do cursor ocorre antes da varredura, conforme [API de alterações](https://developers.google.com/workspace/drive/api/guides/manage-changes). Paginação e alterações são persistidas localmente. O escopo e o cliente de ROMs não implementam escrita ou exclusão. Upload de backups deverá usar autorização separada e escopo mínimo `drive.file`; ainda não está implementado.

Os arquivos são identificados pelo Drive ID. Nome original, plataforma, caminho, tamanho, modificação e MD5 quando fornecido são preservados. Arquivos compactados não são inspecionados remotamente. Plataforma desconhecida permanece para revisão. DATs Logiqx podem gerar candidatos exatos por MD5 + tamanho + plataforma, mas não criam jogos nem vínculos automaticamente. Não há download para identificação.

Limitações: raiz por ID sem navegador de pastas, sem suporte testado a shared drives/atalhos, sem cancelamento/progresso ou retomada persistente do download, sem tratamento automático de cursor expirado 410. Falha preserva o cursor anterior ou a última página aplicada; repita a operação ou faça nova varredura completa. Downloads incompletos ficam como `.partial` e nunca são marcados disponíveis. O próximo download reinicia em novo parcial, sem substituir uma ROM instalada.

## RAWG — implementado, credencial real pendente

Obtenha uma chave própria em [RAWG API](https://rawg.io/apidocs). Configure a chave pelo campo protegido em Configurações. Pesquisar metadados apresenta resultados para escolha explícita, consulta detalhes e importa título, descrição, lançamento, gêneros e origem. A plataforma pessoal é confirmada no diálogo. O identificador externo impede importação duplicada. Artes são selecionadas separadamente.

Revisar termos, limites e atribuição da RAWG antes de distribuição/uso comercial. Sem chave, a biblioteca manual funciona normalmente. Testes usam respostas controladas, sem alegar acesso real.

## SteamGridDB — implementado, credencial real pendente

Obtenha API key própria, salve em Configurações e use Selecionar artes no jogo. Escolha o jogo correto e o tipo de arte. O aplicativo lista arquivos e baixa o escolhido para pré-visualização; só aplica após confirmação. O filtro de capas prioriza dimensões verticais; a galeria final recorta para 3:4. Não há garantia de que toda arte seja oficial: revisar a imagem e os direitos de uso. [Referência API v2](https://www.steamgriddb.com/api/v2).

## IGDB — avaliado, ainda não implementado

[IGDB](https://api-docs.igdb.com/) utiliza credenciais Twitch e OAuth Client Credentials. Requer client ID/secret e tratamento de expiração. Para uma distribuição desktop pública, não embutir segredo compartilhado no executável: considerar serviço intermediário ou credenciais próprias do usuário. O contrato MetadataProvider já permite acrescentar o cliente.

## Steam — avaliado, ainda não implementado

A [Steam Web API](https://partner.steamgames.com/doc/webapi/IPlayerService) oferece jogos/horas quando a privacidade da conta permite. Perfil, jogos privados e conquistas variam por visibilidade e suporte. Serão necessários API key e SteamID. Horas remotas devem ficar separadas das sessões locais para evitar dupla contagem; importação da biblioteca deve preservar Steam AppID e pedir confirmação em conflitos. Não há integração Steam funcional nesta versão.

## RetroAchievements — avaliado, ainda não implementado

A [API RetroAchievements](https://api-docs.retroachievements.org/v1/get-user-summary.html) requer credencial própria e identificação do usuário. Compatibilidade varia por jogo, hash e emulador; consultar progresso não implementa o sistema de runtime do emulador. Apenas conquistas pessoais funcionam nesta entrega.

## Preços — avaliação e pendências

A [API IsThereAnyDeal](https://docs.isthereanydeal.com/) é a opção inicial a investigar: oferece consulta por país e provedores agregados. É necessário validar credenciais, contrato, lojas efetivamente cobertas no Brasil e moeda retornada. A documentação retornou 403 na leitura direta nesta sessão; não foi implementado um cliente com suposições sobre o payload.

Steam, Epic, Nuuvem e GOG não foram conectadas por endpoints não documentados. Não foi identificada e validada nesta sessão uma API pública apropriada de GG.deals. Não é correto afirmar que todas as lojas têm ou não têm API; a cobertura continuará sendo avaliada por provedor e termos. Nenhum scraping foi implementado.

A lista de desejos e metas BRL são locais. Monitoramento periódico, histórico de preços, promoções, links e notificações ainda não estão disponíveis. O banco possui PriceHistory para essa evolução. Não há valores fictícios ou preços gerados.

## Cofre e logs

Segredos usam exclusivamente o backend Windows Credential Manager. SQLite guarda somente configurações não sensíveis. Não há exportação de tokens, sincronização de segredos ou fallback para texto. As integrações mostram a existência de credencial salva como conexão não verificada, nunca como confirmação de acesso. Erros de jobs omitem respostas OAuth e URLs com chaves.

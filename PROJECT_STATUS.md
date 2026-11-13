# Estado atual — Checkpoint 0.1.29

## Funciona

- Biblioteca com capas verticais, tamanho de 70% a 150%, colunas responsivas e migração da densidade anterior.
- Início restrito a jogos Jogando/Pausado, destaque recente, atividade pessoal e estado vazio.
- Rolagem animada por pixel, com barras finas na cor do tema, em Biblioteca, Desejos, Memórias e Estatísticas.
- Desejos com área de arte 1:1, logo contida, alternativa de capa/título, preços atuais/históricos e atribuição, ordenação por nome ou menor preço e posição de rolagem preservada.
- Busca com origem correta e salvamento aguardando a ficha selecionada; diálogo com fechamento único e nomes de ROM limpos.
- Nove temas, Verde padrão; identidade checkpo//nt e ícone próprio; quatro Conexões em 2×2 e GG.deals abaixo, com indicadores de configuração.
- Migração não destrutiva de dados/cofre, schema 4, saves, diário, lixeira, Steam e Drive preservados.
- Diálogos aninhados aguardam seus jobs antes de concluir; regressões exercitam o fluxo com faulthandler.

## Pendente

Configuração da chave pelo dono no cofre e validação autenticada da API GG.deals. Decisão sobre futura fonte de preço original para percentual, sem usar histórico. Remoção pelo dono da pré-release anterior publicada por engano. Futura decisão sobre unificar os três componentes de cadastro; a fusão não foi executada.

## Limitações

API oficial implementada e validada com respostas controladas; sem validação de conta real. O fallback público depende de HTML e pode ser bloqueado. A API retorna histórico, não preço original/desconto. As imagens e a ficha dependem da cobertura dos provedores. Testes e capturas desta revisão são Qt offscreen em Linux, com dados isolados; não validam Windows real, DPI ou contas autenticadas.

Resultados por etapa, diferenças visuais e caminhos das capturas estão em RELATORIO_CORRECOES.md. Histórico em CHANGELOG.md. Não houve build, tag nem publicação de release nesta revisão.

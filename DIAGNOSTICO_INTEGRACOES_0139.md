# Checkpoint 0.1.39 — preços por plataforma e saves no Drive

Rodada local, sem publicação. Diagnóstico por inspeção do código e documentação
oficial obtida em 16/11/2026. Não houve consulta autenticada com a conta do dono.
Nenhum token, banco pessoal, save ou ROM real foi acessado.

## Item 5 — consulta console: bloqueado

### Caminho usado hoje

- prices.refresh_prices / PriceQueue selecionam o provedor já autorizado.
- GgDealsApiProvider em integrations/ggdeals_api.py chama
  https://api.gg.deals/v1/prices/by-steam-app-id/ com ids/key/region=br.
- Identidade vem de external_identifiers.provider=steam, com contexto de
  plataforma/edição verificado antes de exibir cache. Console não herda PC.
- Sem chave, o fallback público existente só é usado se habilitado; não houve
  nova fonte, novo scraper, consulta de console por nome ou remoção do aviso.
- selected_quote mantém lojas oficiais por padrão e keyshops conforme opção
  persistida; preço ausente é hífen com motivo. Desconto/original exigem oferta
  individual da mesma identidade, não menor histórico. Tudo isso foi preservado.

### Prova atual do provedor

GET https://gg.deals/api/prices/ retornou HTTP 200, 102257 bytes.
SHA-256: 922fb4560bb1cccc7be1e55b1cb905e823b21f73d0db8a8f05a1069cce1964c1.
HTML bruto e metadados em /workspace/work/evidence-0139/ggdeals-api-prices.html
e ggdeals-documentation.json.

Endpoints documentados: by-steam-app-id, by-steam-sub-id, by-steam-bundle-id,
by-slug. By-slug usa slugs/key/region; região br consta da lista. A resposta
documentada tem title/url/prices e currentRetail/currentKeyshops/
historicalRetail/historicalKeyshops/currency. Não há campo de plataforma/edição
ou parâmetro documentado de filtro de console nessa operação.
O menu PC/Xbox/PlayStation/Switch pertence à navegação do site; sua presença
no HTML não comprova capacidade da API nem direito/plano de acesso.

A instalação aqui é Linux; CredentialVault padrão exige WinVaultKeyring.
O cofre Windows do dono não está disponível e não foi exportado/solicitado.
Os testes do provedor usam respostas controladas e não comprovam oferta real.

### Dependência concreta para implementar com segurança

1. Confirmar com documentação/contrato do provedor se by-slug atende um jogo
   específico de Switch em BRL no plano da chave configurada no Windows.
   Exigir correspondência verificável slug ↔ plataforma ↔ edição ↔ região,
   inclusive distinção de edições PC e console. Não inferir pelo título.
2. Obter uma resposta autenticada **sem registrar a chave**, com URL canônica,
   identidade confirmada, BRL e classificação retail/keyshop. Usar o cofre da
   instalação para consulta; não colar credencial no chat nem em relatórios.
3. Se confirmado: ampliar o provedor existente para identidade GG.deals explícita,
   guardar contexto/proveniência em estrutura já suportada somente após definir
   o contrato, e testar Switch mais outra plataforma com oferta real e casos
   sem oferta/ambíguos/região incorreta/cache de outra edição.
4. Se não houver cobertura: propor fonte e condições de uso/API/plano, custo,
   manutenção e autenticação para autorização separada. Não adotar coleta
   silenciosa ou aproveitar preços PC como se fossem console.

Bloqueios distintos: identificação/capacidade não documentadas; plano real não
verificado; ambiente sem cofre do dono. Não há oferta real console validada.
Não existe base para declarar este item feito ou a rodada inteira concluída.

## Item 16.1 — saves: diagnóstico concluído, upload não implementado

### O que funciona

1. Na ficha, Arquivos > Saves tradicionais > Configurar saves escolhe uma pasta
   **local** e padrões específicos (por exemplo *.sav). Não inclui save states.
2. Configurações > Downloads > Backups de saves define o destino local.
3. Fazer backup agora usa MainWindow.game_backup e GameSaveBackups.create.
   O ZIP é criado por SaveBackupService em
   **<pasta de backups>/<id do jogo>/<arquivo ZIP>**, com manifesto e SHA-256,
   e registrado em save_backups.configuration_id/path/sha256/manifest_json.
4. Backup ao encerrar a sessão usa o mesmo serviço local, se a opção do jogo
   estiver ativa. Fechar só a ROM mantendo o processo vivo não é detectado.
5. Restaurar no histórico valida a versão/manifesto/hash, restaura na pasta
   correspondente à configuração e preserva uma cópia anterior antes de
   substituir arquivos. Nenhuma restauração sobre saves reais foi executada.
6. A ação geral Criar backup em Dados e backup também trabalha com pastas locais;
   o fluxo geral de restauração pede destino e preserva a cópia anterior.

### O que não existe

Não há upload/sincronização de saves na integração atual do Drive.
DriveClient autentica somente drive.readonly, índice e downloads de ROM.
Os campos save_configurations.drive_folder_id e save_backups.drive_id no
schema 4 não têm produtor de upload nesse caminho; sua existência não é
implementação do recurso. Conectar o Drive de ROMs não envia os backups.
Escolher uma pasta já sincronizada por um cliente externo só grava localmente:
a sincronização seria desse cliente, não uma confirmação oferecida pelo Checkpoint.

### Proposta separada, não executada

- Acrescentar serviço independente de envio **explícito** de ZIP já validado,
  sem alterar escopo/credencial read-only, índice, download ou cadastro A4.
- Nova autorização OAuth com drive.file e credencial própria no cofre para
  backups criados pelo app; pasta/destino e conta mostrados antes de confirmar.
- Upload versionado com tamanho/hash/manifesto e verificação de conclusão;
  falha mantém ZIP local e estado objetivo, sem alegar sincronização.
- Restauração baixa para staging, valida integridade/identidade e pede
  confirmação, preservando o backup anterior e bloqueando jogo/saves em uso.
- Sem apagar backups remotos, saves originais ou versões locais automaticamente.
- Testes isolados, cancelamento/rede indisponível/repetição/ZIP inválido/conta
  errada; homologação autenticada separada no Windows antes de declarar suporte.

Esta proposta exige autorização posterior; nenhuma sincronização nova foi
implementada nesta rodada. Dados e serviços existentes foram preservados.

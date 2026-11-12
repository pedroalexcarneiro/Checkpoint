# Arquitetura

## Interface 0.1.18

branding.py desenha a identidade e o ícone; ui_components.py fornece hero, cards e
abas; home_view.py, detail_view.py e settings_view.py constroem as novas páginas.
window.py continua coordenando navegação/serviços. Os fluxos de persistência e a
fila de enriquecimento não foram substituídos. Consulte DESIGN.md.

## Decisões

Python 3.12 + PySide6 Widgets para aplicativo desktop nativo. SQLite via biblioteca padrão, com transações, chaves estrangeiras, WAL e timeout de bloqueio. SQLAlchemy não é necessário para a primeira implementação: o módulo de persistência e os serviços isolam SQL da navegação. A futura adoção de ORM não exige substituir o banco.

Direção visual: superfícies carvão, verde discreto, Segoe UI, tipografia editorial, navegação lateral persistente e cards verticais com recorte central proporcional. O recorte atual é central; detecção de assunto e ajuste manual do ponto focal ainda estão no roadmap. Nenhuma capa física é removida automaticamente. O usuário escolhe a arte.

## Camadas

Atualização 0.1.14: `integrations/steam.py` lê a Steam Web API; `steam_library.py`
aplica importação transacional e snapshots; `steam_dialog.py` consulta em QThread e
salva na thread proprietária do SQLite. Migração 4 cria tabelas por conta/AppID.
Horas/conquistas remotas não alteram sessões ou marcos pessoais. Backup pré-migração
usa o caminho já existente. As notas de versões anteriores abaixo são históricas.

- `app.py`: diretório de dados, log rotativo, trava de instância, ciclo de vida e modo smoke.
- `database.py`: migrações numeradas transacionais, PRAGMA user_version, backup pela API SQLite.
- `library.py`: cadastro, busca parametrizada, lixeira, configurações, memórias, mídia e cálculos estatísticos.
- `launcher.py`: argumentos sem shell, validação local, sessões e recuperação manual.
- `saves.py`: arquivos ZIP versionados, manifesto SHA-256, restauração com cópia anterior.
- `rom_catalog.py`: catálogo Logiqx DAT e candidatos exatos de MD5/tamanho/plataforma.
- `integrations/`: contratos, HTTP, RAWG, SteamGridDB, Drive e cache de imagens.
- `credentials.py`: Windows Credential Manager via backend WinVault explícito. Sem fallback em texto.
- `jobs.py`: trabalhos de rede em QThread; conexões SQLite pertencem à thread que as criou.
- `window.py`, `dialogs.py` e diálogos específicos: apresentação e interação.

A camada de interface ainda contém consultas de leitura e algumas operações simples de escrita. Extrair repositórios específicos de diário, mídia, conquistas, perfis e saves é uma melhoria planejada antes de expandir essas áreas. Não se considera esta separação totalmente finalizada.

## Banco e relacionamentos

Games é a identidade da entrada pessoal. GameFiles representa os arquivos físicos ou remotos; ROMVersions acrescenta região, revisão e perfil a um arquivo. Vários arquivos podem apontar para um único jogo. Identificadores externos são únicos por provedor. Jogos removidos recebem deleted_at; memórias, mídias e arquivos não são apagados.

PlaySessions distingue active, interrupted e finished. Somente finished entra nas estatísticas. Uma interrupção jamais vira automaticamente uma sessão de muitas horas. O usuário informa a duração efetiva na recuperação.

Há tabelas para emuladores/perfis, conquistas, diário, mídia, wishlist, histórico de preços, saves e integrações. Algumas tabelas estão preparadas para futuras funcionalidades; sua existência não significa que o fluxo completo esteja implementado. Plataforma, gênero e categoria usam texto nesta versão; normalização com entidades/tabelas associativas é futura migração.

Migração 1: esquema principal. Migração 2: catálogo de ROMs e índices de checksums. Versões desconhecidas mais novas são recusadas. A migração roda dentro de BEGIN IMMEDIATE e COMMIT; falhas provocam rollback. Atualização v1→v2, recusa de esquema futuro e rollback integral de DDL com falha têm testes automatizados. Backup automático pré-migração ainda está pendente.

## Rede e Drive

Timeout e tentativas limitadas nas chamadas HTTP. Erros de rede não transportam URLs com segredos para a UI. Trabalhos de rede não bloqueiam a interface. Operações locais grandes de backup e leitura de biblioteca ainda são síncronas e deverão ser movidas para workers antes de uso com coleções muito grandes.

Drive: cursor anterior à varredura inicial, paginação de 1000 registros, BFS de pastas e coleta somente de metadados. Atualizações usam changes.list, com aplicação e avanço de cursor na mesma transação por página. Pastas alteradas são reexaminadas. Downloads usam ID, arquivo parcial, tamanho e MD5 quando disponível. A troca de raiz é bloqueada na mesma biblioteca nesta versão. HTTP 410 exige nova varredura manual. Drives compartilhados não foram implementados.

## Saves

A configuração é explícita por pasta/padrão; extensão isolada não garante que um arquivo seja save tradicional. Alguns formatos comuns de save state são rejeitados, mas a lista não é universal. O usuário deve selecionar somente saves tradicionais. Nenhum perfil de emulador foi validado. Backup local manual funciona; automação por jogo e upload ao Drive ainda não estão implementados.

Restauração valida SHA-256 do ZIP e dos arquivos, rejeita caminhos externos e preserva versões existentes em outro ZIP. Substituição é atômica por arquivo; a restauração completa de vários arquivos não é uma transação do sistema de arquivos. A cópia anterior possibilita recuperação manual em caso de interrupção.

## Segurança

SQL parametrizado e ordenação por allowlist. Sem execução por shell. Credenciais fora do banco e do Git. O escopo Drive de ROMs é somente leitura. Não há API de exclusão remota nem exclusão local automática de ROMs. Backup do banco usa conexão separada explicitamente fechada. Limite de tamanho/resolução e verificação de decodificação no cache de imagens.

Faltam assinatura de executável, atualização automática, auditoria de dependências e revisão de segurança para distribuição pública. Não há telemetria.


## 0.1.12 — artes por identidade confirmada (11/11/2026)
Fonte principal: SteamGridDB API v2 (https://www.steamgriddb.com/api/v2), categorias grids/capa, heroes/banner e logos. O provedor fornece artes da comunidade; não há garantia de que todas sejam oficiais. A biblioteca continua recortando capas para 3:4 sem deformar o original.
- Confirmar jogo selecionado persiste o ID do SteamGridDB e obtém capa/banner/logo faltantes; nomes de ROM não são associados automaticamente por suposição. AppID Steam pode ser resolvido pelo provedor e confirmado na interface, sem busca textual. Isso não implementa importação de conta Steam.
- AutoArtwork executa após criar/associar jogo a ROM e após download no gerenciador Drive, se houver identidade confirmada e chave configurada. Sem identidade ou chave, mostra pendência; não desfaz cadastro nem download. Não é preciso baixar a ROM para obter arte.
- Artes existentes preservadas; atualização condicional impede substituir escolha feita durante consulta. Cache validado por imagem e SHA-256; migração 3 adiciona artwork_assets com tipo, ID externo, URL, caminho e data da última arte obtida automaticamente. Esse registro descreve o download, não garante que a arte ainda seja a escolha atual após edição manual.
- Até três alternativas estáticas por tipo, excluindo conteúdo marcado NSFW/humor. Ordem por pontuação do provedor. Consulta automática tem intervalo mínimo de uma hora por jogo; botão Obter artes faltantes permite nova tentativa. Preferência pode desativar automação.
- Banco anterior é copiado consistentemente para backups antes de migrar; migração transacional. Não atualizar banco real com a versão antiga aberta.
- Validação: 111 testes passaram (pytest result 0), com provedores/transferências substituídos em testes. Tela renderizada e inspecionada. Consulta real SteamGridDB e artes reais NÃO validadas: não há chave configurada no cofre desta sessão. Nenhuma arte foi atribuída à coleção real nesta implementação.
- Configurar chave em Configurações > Configurar chave SteamGridDB (não compartilhar chave no chat nem versionar). Em um jogo: Selecionar artes > Pesquisar > selecionar resultado > Confirmar jogo selecionado e obter capa, banner e logo. Para Steam: Identificar pelo AppID Steam > confirmar resultado. Downloads/associações futuros reutilizam o ID salvo.
Referência primária do provedor: https://github.com/SteamGridDB/java-steamgriddb . Os termos do serviço e as licenças dos autores continuam aplicáveis às imagens.

## Busca única 0.1.21

quick_add.py coordena UI, debounce e prévia dentro de GameDialog, preservando o
contrato do cadastro e o editor existente. unified_catalog.py agrega provedores,
filtra plataforma e reúne resultados compatíveis. worker.py executa busca e
prévia isoladas, sem serializar credenciais. Jobs de busca/detalhes são limitados
e respostas verificam geração. A fila completa também identidades confirmadas
RAWG/SteamGridDB, sem exigir nova seleção de provedor no cadastro.

Busca interativa consulta provedores em paralelo, com timeout de 8 s e uma
tentativa por requisição. Previews usam timeout de 8 s por imagem. Integrações
em segundo plano preservam os timeouts/retries anteriores por padrão.

## Sistema de interface 0.1.22

design_system.py fornece composição responsiva e componentes comuns;
collection_views.py apresenta desejos e memórias; game_editor.py reorganiza os
campos existentes em quatro abas sem alterar o contrato de GameDialog.data().
A persistência, a identificação de ROMs e os provedores não foram substituídos.
Capturas de revisão são produzidas por scripts/render_ui_review.py em base nova;
o empacotamento visual só aceita PNGs de capturas e índice HTML, nunca a base.

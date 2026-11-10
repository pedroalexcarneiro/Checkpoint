# Arquitetura

## Decisões

Python 3.12 + PySide6 Widgets para aplicativo desktop nativo. SQLite via biblioteca padrão, com transações, chaves estrangeiras, WAL e timeout de bloqueio. SQLAlchemy não é necessário para a primeira implementação: o módulo de persistência e os serviços isolam SQL da navegação. A futura adoção de ORM não exige substituir o banco.

Direção visual: superfícies carvão, verde discreto, Segoe UI, tipografia editorial, navegação lateral persistente e cards verticais com recorte central proporcional. O recorte atual é central; detecção de assunto e ajuste manual do ponto focal ainda estão no roadmap. Nenhuma capa física é removida automaticamente. O usuário escolhe a arte.

## Camadas

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

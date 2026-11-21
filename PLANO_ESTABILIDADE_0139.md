# Checkpoint 0.1.39 — estabilidade e organização (21/11/2026)

Base confirmada: 9ecbc9505071573e1ce53540d853d4d8d5a981b5, versão 0.1.39
em checkpoint/__init__.py e pyproject.toml. Checkout recebido limpo; HEAD remoto
fix/pos-0139-layout igual. Branch local fix/0139-estabilidade-organizacao.
Sem push, PR, tag, release, publicação, troca de assets ou workflow publicador.
Os 808 testes anteriores são históricos; novos gates serão registrados nesta rodada.

Pedido integral recebido em Texto colado.txt (21/11); imagem escolhida do Início
é referência de composição, preservando conteúdo e tema reais. Vídeos recebidos:
23.31.42.01 (8,799 s, download) e 23.47.30.02 (16,567 s, Memórias), ambos
1920×1080/60 fps. Inspeção por quadros confirma espera e diálogo bloqueante;
não prova duração de uma hora nem causa do defeito no Windows do dono.

## Ordem e unidades locais

1. Medir abertura/reabertura de Memórias, leitura, cards, relayout, captura e
   gravação com volume representativo e responsividade observável.
2. Memórias progressivas, cache limitado, atualização incremental e grade útil
   (itens 4/12). Preservar anotações/filtros e toda imagem original.
3. Sessões: dispensa persistente por sessão, checkpoints, recuperação idempotente,
   desligamento e suspensão com tratamento explícito (7/8).
4. Downloads na ficha/aba Downloads: tarefa independente, progresso, cancelamento,
   parcial/validação e nomes físicos reconhecíveis sem sobrescrever (5/15).
   A4 não muda nem é contornado.
5. Diálogo/estado de janela: reproduzir recentralização; corrigir apresentação
   localizada, preservar Snap/arrasto e documentar limites de monitores reais (6).
6. Captura por janela sem foco: alvo inequívoco, sem desktop/oclusor como fallback,
   sem alvo minimizado; aquisição/codificação desacopladas da GUI (4/9).
7. Extensões/plataformas, com catálogo e compatibilidade compartilhados e correção
   explícita de registros antigos (16/17). Não alterar cadastro protegido.
8. Pastas de mídia por identidade, inventário, indexação estável/segura e filtros
   (11), sem reorganização destrutiva de originais existentes.
9. Listas lógicas persistidas e ROM local com movimentação explicitamente escolhida
   (13/14), preservando arquivos/saves em falhas e fronteiras de volumes.
10. Investigar controle, updates/DLCs e descontos (10/18/19), implementar somente
    capacidade comprovada; registrar propostas/bloqueios específicos e seguir
    itens independentes. Não inventar desconto nem suporte console.
11. Início conforme imagem, banner do último início real, até dez jogos distintos
    anteriores, Continuar, banners pequenos em Ofertas e memórias em largura total
    (20). Capturas reais em 1280×800/1920×1080/menor e revisão com o dono.
12. Regressões significativas, suíte integral, smoke isolado, evidências completas
    e commits locais. Não confundir fixtures/Linux/runner com PC pessoal.

## Contratos

Preservar worker, enrichment, game_import, completion_queue, dialogs, quick_add,
tests/test_save_lifecycle.py e teste protegido visual/A4. A exceção histórica
ImageDialog.__init__ não autoriza nova mudança. Se um item exigir alteração
protegida: proposta concreta, autorização específica e continuidade independente.
Sem troca automática de ROM nem inferência por foco/timeout de ROM descarregada.

Persistência: inspecionar esquema 4 e reaproveitar campos/preferências quando
adequado. Migração nova somente se necessária e com preservação/backup/testes;
nenhum banco pessoal será aberto. UTF-8/LF nos textos novos.

## Registro por item

RELATORIO_ESTABILIDADE_0139.md acompanha requisito, relato/visual/reprodução,
causa comprovada ou hipótese, funções, commit, testes/evidências e estado
feito/parcial/bloqueado/não testado. Saídas integrais externas em
/workspace/work/evidence-0139-estabilidade; seleção não privada será versionada.

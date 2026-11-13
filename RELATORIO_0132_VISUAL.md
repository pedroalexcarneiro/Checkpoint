# Relatório visual — Checkpoint 0.1.32

## Base, escopo e preservação

Branch `fix/0.1.32-visual`, criada em `c51c2456f8479f208d73a1281eb0dfada8ee7213`. Versão 0.1.32 em pyproject.toml e checkpoint/__init__.py; schema 4 preservado. Nenhuma tag, release ou PR. Push autorizado somente desta branch, sem force.

`fix/0.1.30` permanece em `7cd211844a7e12052a18cf156743da0d2a81f0db` e `fix/0.1.29` em `572cb3c50f8257d95f973887baed57f52ac15f90`. Não se criou nem consultou credencial real para validação.

## Componentes e arquivos

- `visual_tokens.py`: escalas 4/8/12/16/24/32, sete tamanhos tipográficos e dois pesos; raio 12 nos cards e 8 nos botões.
- `theme.py`: nove paletas com os mesmos papéis de fundo, superfície, card, bordas, texto, destaque e estados; estilos comuns de botões primário/secundário/fantasma; reaplicar tema idêntico evita repolir todas as janelas.
- `design_system.py`, `ui_components.py`: CardSurface, ActionCard, StatusChip, SectionHeader, estado vazio com ícone/título/descrição/ação e grade responsiva.
- `cover_art.py`, `cover_grid.py`, `card_layout.py`: pintura compartilhada, título alternativo completo e capas sem distorção, métricas e intervalos iguais entre grades. Biblioteca vertical; Desejos mantém área quadrada para logo contida conforme AGENTS.md e decisão anterior.
- `home_view.py`: hero, continuidade e cards de atividade obtidos da biblioteca; estados de coleção vazia e sem jogos em andamento.
- `window.py`: cabeçalho com espaço proporcional e estado vazio da Biblioteca junto aos filtros; nenhuma alteração em salvamento.
- `collection_views.py`, `price_view.py`: arte uniforme, nome, preço principal, loja, histórico e desconto em níveis separados. Não se calcula desconto com preço histórico.
- `detail_view.py`: barra de ações de 64 px, banner menor na ficha pobre, descrição/metadados e galeria lado a lado, estados orientados; altura das abas calculada pela página ativa elimina espaço artificial.
- `settings_view.py`: abas compactas, conexões em 2×2 e estados verdes/cinzas; Downloads e Dados com cards de ação.
- `add_dialog_visuals.py`, `catalog_result_visuals.py`, `dialogs.py`: somente gancho visual no construtor; tamanho, superfícies e delegate dos resultados, arte local quando já existe, plataforma e estado. Nenhuma busca de arte ou job adicional para a lista Drive.
- `scripts/render_ui_review.py`, `scripts/visual_review.py`: matriz reproduzível, fixtures explicitamente declarados e manifesto com commit/hashes.

Telas cobertas: Início, Biblioteca, Desejos, Ficha (quatro abas), Configurações (quatro abas), Adicionar jogo e ROM do Drive, incluindo estados vazios e ficha incompleta. Estatísticas e a página Memórias recebem os tokens globais; não houve redesenho estrutural dessas duas páginas fora do escopo.

## Preservação do cadastro

O teste estrutural compara todos os métodos de QuickAdd e os métodos funcionais de GameDialog com a base (AST). Compara byte a byte os testes/suporte Drive e os módulos de importação, enriquecimento, worker e fila de conclusão. Nenhum desses caminhos foi reescrito. Não se adicionou skip/xfail. As expectativas visuais antigas sobre altura do hero/cabeçalho, largura do diálogo e ausência de descrição foram atualizadas; as verificações de seleção, ausência de jobs/rede e persistência permanecem.

## Validação real executada

Ambiente: Python 3.12, PySide6 6.8.3, Linux Qt offscreen, dados isolados em /tmp. Sem dependências adicionais instaladas nesta etapa.

Comando completo:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

A primeira rodada completa do redesenho terminou com **340 passando e 3 falhando em 1092,86 s**. Falhas: desigualdade de colunas entre grades, teste antigo que proibia descrição no estado vazio e largura antiga do diálogo. Foram corrigidas as métricas e atualizadas as duas expectativas visuais. A rodada focada posterior terminou com **57 passando em 45,72 s**; o novo teste de reaplicação de tema passou separadamente.

Foram também detectados e corrigidos durante desenvolvimento erro do enum Antialiasing no delegate e problemas de descarte de widgets nos novos fixtures visuais; execuções com abort/segfault não foram tratadas como aprovação. A limpeza dos novos fixtures usa deleteLater/DeferredDelete; testes Drive/lifecycle permaneceram intactos.

Suíte integral final: **344 passed in 429.70s (0:07:09)**, exit 0; sem falhas/erros e sem novos skips ou xfails. Qt offscreen, CHECKPOINT_TEST_ROOT=/tmp, Python 3.12.

Novos contratos: contraste de texto primário/secundário/mudo e botão em todas as nove paletas (>=4,5:1); limites horizontais reais em 1280 px nos temas Verde e Rosa; estado vazio com título/explicação/ação; dimensões e pintura comuns dos cards; preservação de cadastro/Drive; altura e alinhamento da ficha; não reaplicar stylesheet idêntico. A base histórica 0.1.30 documenta 303 testes; nesta tarefa o diagnóstico integral acima foi feito após as etapas visuais, não se apresenta aquela execução histórica como rodada nova.

Os menores contrastes medidos (incluindo texto mudo em seleção) vão de **5,11:1 a 5,66:1**; os botões de destaque vão de **7,71:1 a 11,27:1**. Os testes usam os mesmos tokens da UI. A leitura não cobre texto desenhado sobre qualquer imagem arbitrária fora do gradiente do hero.

## Capturas e comparação

72 PNGs, 18 estados × dois temas × duas resoluções, gerados pelo script pedido. Commit do código capturado: `a329fe24f32a11cc258a090de414714f8541bd22`, árvore limpa no início da geração. O commit posterior da entrega contém documentação/evidências; não altera a UI capturada. Manifesto: `evidence/ui-0.1.32/visual-manifest.json`, com tamanho, SHA-256, resolução, tema e commit de cada imagem.

Artes geométricas, jogos, preços, sessões, índice Drive e estados de conexão são fixtures visuais locais. Não são credenciais nem consultas reais; não provam o fluxo de cadastro. Diálogos são grabs reais do Qt compostos sobre o grab da janela, sem retoque ou captura de desktop. Arquivos de banco/cache usados pelo render ficam em /tmp e não integram a entrega.

| Captura | Mudança e limite em relação à referência |
| --- | --- |
| `evidence/ui-0.1.32/visual-inicio-verde-1280x800.png` | Hero com chamada, capas de continuidade e atividade do banco; a arte geométrica local não reproduz a arte comercial da referência. |
| `evidence/ui-0.1.32/visual-biblioteca-verde-1280x800.png` | Capas verticais uniformes, filtros compactos e seleção na arte; a densidade é responsiva e não fixa quatro colunas em toda resolução. |
| `evidence/ui-0.1.32/visual-desejos-verde-1280x800.png` | Arte contida, preço dominante, loja e desconto separados; logos ausentes usam título e os preços são exemplos controlados. |
| `evidence/ui-0.1.32/visual-ficha-verde-1280x800.png` | Barra compacta e informações alinhadas com a galeria; arte, descrição e metadados são fixtures. |
| `evidence/ui-0.1.32/visual-ficha-atividade-verde-1280x800.png` | Sessões e marcos em superfícies próprias; o volume de eventos depende do histórico real. |
| `evidence/ui-0.1.32/visual-ficha-memorias-verde-1280x800.png` | Editor e registros visuais com espaçamento comum; as imagens são locais de teste. |
| `evidence/ui-0.1.32/visual-ficha-arquivos-verde-1280x800.png` | Arquivos sem associação oferecem ação e explicação; o fixture não tem ROM nem save real. |
| `evidence/ui-0.1.32/visual-config-aparencia-verde-1280x800.png` | Nove temas e ajuste de capas em superfície única; a área livre cresce em telas grandes sem conteúdo artificial. |
| `evidence/ui-0.1.32/visual-config-conexoes-verde-1280x800.png` | Abas proporcionais e quatro conexões em 2×2 com estado; logos SGDB/RAWG são monogramas e conexões são simuladas. |
| `evidence/ui-0.1.32/visual-config-downloads-verde-1280x800.png` | Pastas em cards de ação alinhados; não há caminhos pessoais no fixture. |
| `evidence/ui-0.1.32/visual-config-dados-verde-1280x800.png` | Backup e saves em dois cards com ações claras; não foi homologado backup em Windows nesta tarefa. |
| `evidence/ui-0.1.32/visual-adicionar-verde-1280x800.png` | Busca e seleção com capa, destaque e ações hierarquizadas; a captura usa resultado controlado e não comprova consulta externa. |
| `evidence/ui-0.1.32/visual-rom-drive-verde-1280x800.png` | Linhas viraram cards com plataforma, vínculo e arte local disponível; ROM não vinculada usa ícone; não buscamos arte nova nem alteramos o fluxo. |
| `evidence/ui-0.1.32/visual-inicio-vazio-verde-1280x800.png` | Estado com ícone, explicação e ação de cadastro; não inventa jogos para preencher o painel. |
| `evidence/ui-0.1.32/visual-biblioteca-vazia-verde-1280x800.png` | Estado acionável junto aos filtros; não exibe capas sem jogos. |
| `evidence/ui-0.1.32/visual-desejos-vazio-verde-1280x800.png` | Convite com título, explicação e ação; não inventa ofertas. |
| `evidence/ui-0.1.32/visual-inicio-sem-andamento-verde-1280x800.png` | Escolha do próximo jogo e prévia da coleção real; sem jogo em andamento não força um hero fictício. |
| `evidence/ui-0.1.32/visual-ficha-incompleta-verde-1280x800.png` | Banner menor, orientação de edição e galeria com ação; não inventa descrição nem metadados ausentes. |
| `evidence/ui-0.1.32/visual-inicio-verde-1920x1080.png` | Hero com chamada, capas de continuidade e atividade do banco; a arte geométrica local não reproduz a arte comercial da referência. |
| `evidence/ui-0.1.32/visual-biblioteca-verde-1920x1080.png` | Capas verticais uniformes, filtros compactos e seleção na arte; a densidade é responsiva e não fixa quatro colunas em toda resolução. |
| `evidence/ui-0.1.32/visual-desejos-verde-1920x1080.png` | Arte contida, preço dominante, loja e desconto separados; logos ausentes usam título e os preços são exemplos controlados. |
| `evidence/ui-0.1.32/visual-ficha-verde-1920x1080.png` | Barra compacta e informações alinhadas com a galeria; arte, descrição e metadados são fixtures. |
| `evidence/ui-0.1.32/visual-ficha-atividade-verde-1920x1080.png` | Sessões e marcos em superfícies próprias; o volume de eventos depende do histórico real. |
| `evidence/ui-0.1.32/visual-ficha-memorias-verde-1920x1080.png` | Editor e registros visuais com espaçamento comum; as imagens são locais de teste. |
| `evidence/ui-0.1.32/visual-ficha-arquivos-verde-1920x1080.png` | Arquivos sem associação oferecem ação e explicação; o fixture não tem ROM nem save real. |
| `evidence/ui-0.1.32/visual-config-aparencia-verde-1920x1080.png` | Nove temas e ajuste de capas em superfície única; a área livre cresce em telas grandes sem conteúdo artificial. |
| `evidence/ui-0.1.32/visual-config-conexoes-verde-1920x1080.png` | Abas proporcionais e quatro conexões em 2×2 com estado; logos SGDB/RAWG são monogramas e conexões são simuladas. |
| `evidence/ui-0.1.32/visual-config-downloads-verde-1920x1080.png` | Pastas em cards de ação alinhados; não há caminhos pessoais no fixture. |
| `evidence/ui-0.1.32/visual-config-dados-verde-1920x1080.png` | Backup e saves em dois cards com ações claras; não foi homologado backup em Windows nesta tarefa. |
| `evidence/ui-0.1.32/visual-adicionar-verde-1920x1080.png` | Busca e seleção com capa, destaque e ações hierarquizadas; a captura usa resultado controlado e não comprova consulta externa. |
| `evidence/ui-0.1.32/visual-rom-drive-verde-1920x1080.png` | Linhas viraram cards com plataforma, vínculo e arte local disponível; ROM não vinculada usa ícone; não buscamos arte nova nem alteramos o fluxo. |
| `evidence/ui-0.1.32/visual-inicio-vazio-verde-1920x1080.png` | Estado com ícone, explicação e ação de cadastro; não inventa jogos para preencher o painel. |
| `evidence/ui-0.1.32/visual-biblioteca-vazia-verde-1920x1080.png` | Estado acionável junto aos filtros; não exibe capas sem jogos. |
| `evidence/ui-0.1.32/visual-desejos-vazio-verde-1920x1080.png` | Convite com título, explicação e ação; não inventa ofertas. |
| `evidence/ui-0.1.32/visual-inicio-sem-andamento-verde-1920x1080.png` | Escolha do próximo jogo e prévia da coleção real; sem jogo em andamento não força um hero fictício. |
| `evidence/ui-0.1.32/visual-ficha-incompleta-verde-1920x1080.png` | Banner menor, orientação de edição e galeria com ação; não inventa descrição nem metadados ausentes. |
| `evidence/ui-0.1.32/visual-inicio-rosa-1280x800.png` | Hero com chamada, capas de continuidade e atividade do banco; a arte geométrica local não reproduz a arte comercial da referência. |
| `evidence/ui-0.1.32/visual-biblioteca-rosa-1280x800.png` | Capas verticais uniformes, filtros compactos e seleção na arte; a densidade é responsiva e não fixa quatro colunas em toda resolução. |
| `evidence/ui-0.1.32/visual-desejos-rosa-1280x800.png` | Arte contida, preço dominante, loja e desconto separados; logos ausentes usam título e os preços são exemplos controlados. |
| `evidence/ui-0.1.32/visual-ficha-rosa-1280x800.png` | Barra compacta e informações alinhadas com a galeria; arte, descrição e metadados são fixtures. |
| `evidence/ui-0.1.32/visual-ficha-atividade-rosa-1280x800.png` | Sessões e marcos em superfícies próprias; o volume de eventos depende do histórico real. |
| `evidence/ui-0.1.32/visual-ficha-memorias-rosa-1280x800.png` | Editor e registros visuais com espaçamento comum; as imagens são locais de teste. |
| `evidence/ui-0.1.32/visual-ficha-arquivos-rosa-1280x800.png` | Arquivos sem associação oferecem ação e explicação; o fixture não tem ROM nem save real. |
| `evidence/ui-0.1.32/visual-config-aparencia-rosa-1280x800.png` | Nove temas e ajuste de capas em superfície única; a área livre cresce em telas grandes sem conteúdo artificial. |
| `evidence/ui-0.1.32/visual-config-conexoes-rosa-1280x800.png` | Abas proporcionais e quatro conexões em 2×2 com estado; logos SGDB/RAWG são monogramas e conexões são simuladas. |
| `evidence/ui-0.1.32/visual-config-downloads-rosa-1280x800.png` | Pastas em cards de ação alinhados; não há caminhos pessoais no fixture. |
| `evidence/ui-0.1.32/visual-config-dados-rosa-1280x800.png` | Backup e saves em dois cards com ações claras; não foi homologado backup em Windows nesta tarefa. |
| `evidence/ui-0.1.32/visual-adicionar-rosa-1280x800.png` | Busca e seleção com capa, destaque e ações hierarquizadas; a captura usa resultado controlado e não comprova consulta externa. |
| `evidence/ui-0.1.32/visual-rom-drive-rosa-1280x800.png` | Linhas viraram cards com plataforma, vínculo e arte local disponível; ROM não vinculada usa ícone; não buscamos arte nova nem alteramos o fluxo. |
| `evidence/ui-0.1.32/visual-inicio-vazio-rosa-1280x800.png` | Estado com ícone, explicação e ação de cadastro; não inventa jogos para preencher o painel. |
| `evidence/ui-0.1.32/visual-biblioteca-vazia-rosa-1280x800.png` | Estado acionável junto aos filtros; não exibe capas sem jogos. |
| `evidence/ui-0.1.32/visual-desejos-vazio-rosa-1280x800.png` | Convite com título, explicação e ação; não inventa ofertas. |
| `evidence/ui-0.1.32/visual-inicio-sem-andamento-rosa-1280x800.png` | Escolha do próximo jogo e prévia da coleção real; sem jogo em andamento não força um hero fictício. |
| `evidence/ui-0.1.32/visual-ficha-incompleta-rosa-1280x800.png` | Banner menor, orientação de edição e galeria com ação; não inventa descrição nem metadados ausentes. |
| `evidence/ui-0.1.32/visual-inicio-rosa-1920x1080.png` | Hero com chamada, capas de continuidade e atividade do banco; a arte geométrica local não reproduz a arte comercial da referência. |
| `evidence/ui-0.1.32/visual-biblioteca-rosa-1920x1080.png` | Capas verticais uniformes, filtros compactos e seleção na arte; a densidade é responsiva e não fixa quatro colunas em toda resolução. |
| `evidence/ui-0.1.32/visual-desejos-rosa-1920x1080.png` | Arte contida, preço dominante, loja e desconto separados; logos ausentes usam título e os preços são exemplos controlados. |
| `evidence/ui-0.1.32/visual-ficha-rosa-1920x1080.png` | Barra compacta e informações alinhadas com a galeria; arte, descrição e metadados são fixtures. |
| `evidence/ui-0.1.32/visual-ficha-atividade-rosa-1920x1080.png` | Sessões e marcos em superfícies próprias; o volume de eventos depende do histórico real. |
| `evidence/ui-0.1.32/visual-ficha-memorias-rosa-1920x1080.png` | Editor e registros visuais com espaçamento comum; as imagens são locais de teste. |
| `evidence/ui-0.1.32/visual-ficha-arquivos-rosa-1920x1080.png` | Arquivos sem associação oferecem ação e explicação; o fixture não tem ROM nem save real. |
| `evidence/ui-0.1.32/visual-config-aparencia-rosa-1920x1080.png` | Nove temas e ajuste de capas em superfície única; a área livre cresce em telas grandes sem conteúdo artificial. |
| `evidence/ui-0.1.32/visual-config-conexoes-rosa-1920x1080.png` | Abas proporcionais e quatro conexões em 2×2 com estado; logos SGDB/RAWG são monogramas e conexões são simuladas. |
| `evidence/ui-0.1.32/visual-config-downloads-rosa-1920x1080.png` | Pastas em cards de ação alinhados; não há caminhos pessoais no fixture. |
| `evidence/ui-0.1.32/visual-config-dados-rosa-1920x1080.png` | Backup e saves em dois cards com ações claras; não foi homologado backup em Windows nesta tarefa. |
| `evidence/ui-0.1.32/visual-adicionar-rosa-1920x1080.png` | Busca e seleção com capa, destaque e ações hierarquizadas; a captura usa resultado controlado e não comprova consulta externa. |
| `evidence/ui-0.1.32/visual-rom-drive-rosa-1920x1080.png` | Linhas viraram cards com plataforma, vínculo e arte local disponível; ROM não vinculada usa ícone; não buscamos arte nova nem alteramos o fluxo. |
| `evidence/ui-0.1.32/visual-inicio-vazio-rosa-1920x1080.png` | Estado com ícone, explicação e ação de cadastro; não inventa jogos para preencher o painel. |
| `evidence/ui-0.1.32/visual-biblioteca-vazia-rosa-1920x1080.png` | Estado acionável junto aos filtros; não exibe capas sem jogos. |
| `evidence/ui-0.1.32/visual-desejos-vazio-rosa-1920x1080.png` | Convite com título, explicação e ação; não inventa ofertas. |
| `evidence/ui-0.1.32/visual-inicio-sem-andamento-rosa-1920x1080.png` | Escolha do próximo jogo e prévia da coleção real; sem jogo em andamento não força um hero fictício. |
| `evidence/ui-0.1.32/visual-ficha-incompleta-rosa-1920x1080.png` | Banner menor, orientação de edição e galeria com ação; não inventa descrição nem metadados ausentes. |

## Diferenças restantes e decisões conservadoras

A composição segue as referências, mas não é uma reprodução pixel a pixel: fontes/medidas são responsivas, a arte comercial não está presente nos fixtures e a densidade da Biblioteca respeita o controle existente, em vez de impor quatro colunas em qualquer largura. Fichas sem executável mantêm Configurar execução secundário; a ação Jogar aparece quando configurada. Sem andamento, o Início orienta a escolher um jogo; sem arte na ROM, mostra ícone em vez de acionar rede. Mantiveram-se as nove cores e o wordmark/ícone atuais, sem tema Branco.

Não se inventaram atividades, jogos, preços ou metadados no produto para preencher espaços. Settings tem respiro livre quando seu conteúdo é curto; não foram acrescentados blocos decorativos para ocupar a janela. Não se fundiram os três componentes de cadastro, não se mudou o fluxo validado e não se alteraram provedores.

Não validado: Windows real, renderização nativa/antialiasing de fontes no Windows, DPI/escala e tamanho de texto personalizados, teclado/leitor de tela em Windows, contas Steam/Drive/SGDB/RAWG e fontes reais de arte/preço. A aprovação estética final do dono continua necessária; as capturas permitem avaliar as limitações sem declarar equivalência perfeita.

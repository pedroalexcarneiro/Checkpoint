# Relatório local — Checkpoint 0.1.36: preparação parcial

Código final validado: `da12842e6de663ee4791a6a4010bc622cfed8222`. Branch local `fix/0.1.36-ajustes`; base `818ec80a492a29936782ddb3a43eecaf3ef996e3`. Versão alvo 0.1.36, schema 4. **Sem push, PR, tag, release ou workflow. A rodada não está pronta para lançamento.**

Suíte integral Linux/Python 3.12.14: **612 passed in 428.94s (0:07:08)**, exit 0, sem falhas/erros/skips. O código de produção permaneceu inalterado durante essa execução. Smokes do wheel correspondente instalado isoladamente e verificação byte a byte de fonte/assets também fazem parte da entrega. Isso não valida o pacote Windows nem o PC do dono.

Situação: nove itens feitos no ambiente disponível; 02, 03 e 06 parciais pelos limites concretos abaixo. A4 e detectar apenas a ROM fechada com emulador vivo seguem pendências separadas, sem alteração de contrato. Não há suporte universal de console, original inventado ou associação presumida de processo-filho.

Decisões posteriores do dono prevalecem: preço ausente usa `-` com motivo; percentual usa a cor do tema; ficha exclusiva permanece em Desejos e não tem Adicionar à biblioteca; coração marcado fica preenchido e persistido; status segue o recorte visual, sem anotação 2; banner ocupa bloco proporcional à arte inteira em cada largura.

## Situação por item e SHAs

Todos os estados feito abaixo referem-se ao Linux/offscreen e aos contratos/dados isolados testados; homologação Windows permanece não testada. Arquivos, funções, reproduções, evidências e limitações detalhadas constam nas seções de cada item.

| Item | Status | SHAs de implementação/correção | Resultado e limite |
| --- | --- | --- | --- |
| 01 | feito | `e019050fba6f211d7d8ddb0e13b1d4e82646978c`<br>`432afcf9fe64028d3af0878e9e3277943ec3e511`<br>`d3ecbb2f77e87c08b4f7faa4cbab110f284c316c` | Cards sem tempo; posse/histórico preservados; ficha fica em Desejos sem aquisição. |
| 02 | parcial | `0b5dda51693840a47b65f7a6a0a6ba7a963ef8fc`<br>`015fe0388ec78bd8e64e180bceb8e74b0d61c5b2`<br>`03f8ef3f0689ee50b0f91ec0aea66370c804baf9` | Guarda de plataforma/edição/cache entregue; cobertura autenticada console e vínculo por slug não comprovados. |
| 03 | parcial | `0b5dda51693840a47b65f7a6a0a6ba7a963ef8fc`<br>`c6714f96619276e9ac937f920f8c1ebb0bde09e0`<br>`03f8ef3f0689ee50b0f91ec0aea66370c804baf9`<br>`7015fef4a8480c5f912c829514cf919e042b9693` | Desconto/ordenação/origem da mesma oferta, cor do tema e ausência com hífen; API oficial não traz original individual. |
| 04 | feito | `9ebb264db2a6bc05cc855d94cb1387286ae4cab9`<br>`4da67d5eb00d48884813697068c47153b561a8ec` | Proporção original governa altura; geometria fracionária, quatro bordas e estados Qt testados; Windows real pendente. |
| 05 | feito | `fa755f370a0d9bca82e1d899acaec0f19f5abe2f`<br>`4da67d5eb00d48884813697068c47153b561a8ec` | Sem descrição sobre o Início; cadastro/Sobre e arte inteira preservados. |
| 06 | parcial | `bf4b682cc72c388de1c9486b3cee2fc7294870a7` | Hotkey nativa, conflito/liberação e alvo por PID implementados; filhos não associados recusados; pixels/atalho reais Windows não homologados. |
| 07 | feito | `799d49d844734d13707bd51a339dcb2664d9e381`<br>`e9ad0dd37e7a4ef094af9c7f8b372ff6db060bd0`<br>`9919f4de4c08c929ee249349a5272d02f7f64336`<br>`ef2fb4ce83e8b2366f3536fa371d756c48006201` | Métricas alinhadas, nomes/valores separados, mapa sem sobra fixa e lista com logo/nome/tempo destacado. |
| 08 | feito | `799d49d844734d13707bd51a339dcb2664d9e381` | Sete períodos locais; limites de calendário/DST; Steam agregado fora de recortes temporais. |
| 09 | feito | `ef2fb4ce83e8b2366f3536fa371d756c48006201` | Mais estatísticas removido; gêneros e conclusões integrados sem apagar registros. |
| 10 | feito | `5cb36d5396c22057b7a6454ed74ffdb47344894b`<br>`9dd88167bd0ba3e3bdbe3d89a666fc255c5abbe2` | Cinco capas, base e vãos iguais, teclado/foco/persistência; valores legados preservados até escolha. |
| 11 | feito | `e149d11beb84bffc6ed6d59a154477a8a95450b6`<br>`4da67d5eb00d48884813697068c47153b561a8ec` | Centro óptico e raster explícito/DPI; ICO original inteiro e inalterado; Windows não homologado. |
| 12 | feito | `c1d4ef872fedb4ae2505df2f068fc2f66a6852fc`<br>`d3ecbb2f77e87c08b4f7faa4cbab110f284c316c`<br>`affecc6569d2446ea70c279beddfc4716a4ea72e`<br>`da12842e6de663ee4791a6a4010bc622cfed8222` | Revisão visual, títulos acessíveis, contexto Desejos, coração preenchido e controle de status conforme referência. |

## Como revisar e o que falta

No pacote de entrega, abrir REVISAO_VISUAL_0136.html para comparar PNGs integrais de 1280×800/1920×1080. São dados de teste e arte pública Steam, nunca a base pessoal do dono nem capturas por hotkey real. Os vídeos recebidos/quadros pessoais ficaram fora do repositório e do pacote. Fonte resolvida no Linux: OpenAI Sans, solicitada Segoe UI, 96 DPI lógicos/DPR 1; escalas de geometria/raster 150% e 200% documentadas separadamente.

Para prontidão Windows: testar hotkey/registro/liberação e conteúdo de jogo/emulador, app minimizado, processos/launchers compatíveis, restauração/maximização/DPI e pacote Windows correspondente. Código de captura só admite processo raiz de sessão e alvo em primeiro plano verificado; não foi executado em jogo real. Filhos/launchers sem associação comprovada permanecem recusados.

Para os preços: comprovar resposta autenticada por slug da edição/plataforma console em BRL e seu vínculo explícito antes de ampliar suporte. A API oficial documentada só oferece mínimos agregados, sem original/loja individual; desconto depende de oferta individual contextual confiável do fallback já existente. Nenhuma nova coleta/fonte foi adotada. Não usar preço PC para Nintendo DS nem inferir edição por título. Sem chave real disponível no ambiente.

Dados: sem migração de schema, recriação de banco ou limpeza. Sessões/instantes/ROMs/IDs/arquivos/proveniência preservados; flags de posse e contexto de cache usam settings. Percentuais legados ficam armazenados até escolha; apresentação usa valor mais próximo (empate menor). Favoritar não adquire jogo. Os arquivos protegidos, todos os assets e workflows foram comparados byte a byte com a base.

## Execução integral final

Comando: `QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp python -m pytest tests -q -p no:cacheprovider` (Python usado: /workspace/work/venv/bin/python).

stdout integral:
```text
........................................................................ [ 11%]
........................................................................ [ 23%]
........................................................................ [ 35%]
........................................................................ [ 47%]
........................................................................ [ 58%]
........................................................................ [ 70%]
........................................................................ [ 82%]
........................................................................ [ 94%]
....................................                                     [100%]
612 passed in 428.94s (0:07:08)
```

stderr integral:
```text
```

Código de saída: 0. Histórico integral de cada teste/comando, inclusive reproduções vermelhas e execução substituída/interrompida, em RELATORIO_0136_TESTES.md; bytes originais em raw-tests no pacote. Resultados 598/600/604/608 anteriores são intermediários e não substituem esta execução final de 612.

## Commits locais da entrega

```text
da12842 style(detail): agrupar status conforme referência sem anotação de mockup
affecc6 fix(favorites): mostrar coração marcado e preservar estado ao reabrir
d3ecbb2 fix(wishes): manter ficha em Desejos e retirar aquisição da ficha exclusiva
7015fef style(prices): mostrar hífen sem preço e preservar motivo da ausência
432afcf fix(library): preservar semântica de posse com preferência legada nula
03f8ef3 fix(prices): manter loja e desconto na mesma oferta em preços empatados
77b5765 chore: preparar versão local 0.1.36 e documentar limites da rodada
015fe03 fix(prices): recusar cache de uma identidade ou edição anterior
4da67d5 fix(ui): encaixar banner na proporção original e estabilizar raster em DPI alto
c6714f9 style(prices): usar destaque do tema no percentual de desconto
c1d4ef8 fix(ui): manter títulos longos de memórias acessíveis e ações alinhadas
fa755f3 fix(home): retirar descrição sobreposta preservando cadastro e ficha
9dd8816 fix(settings): igualar margens e espaços entre as cinco capas
e019050 fix(wishes): ocultar tempo sem perder histórico nem posse da biblioteca
9919f4d style(stats): destacar tempo na lista de mais jogados
e149d11 fix(ui): compensar centro óptico da marca Steam sem alterar asset
5cb36d5 feat(settings): escolher tamanho das capas em cinco exemplos clicáveis
e9ad0dd fix(stats): mostrar mais jogados com logo nome e tempo em colunas
ef2fb4c fix(stats): integrar dados extras e ajustar altura do mapa de calor
799d49d feat(stats): filtrar períodos locais e alinhar métricas sem distribuir Steam
0b5dda5 fix(prices): validar contexto de ofertas e apresentar descontos comprovados
9ebb264 fix(ui): recalcular área contida do banner na geometria atual
bf4b682 fix(capture): registrar atalho global e identificar sessão pelo primeiro plano
```

## Patches completos e SHA-256

Cada arquivo foi produzido por `git format-patch -1 <sha> --stdout`; conteúdo completo no diretório patches. A documentação final posterior a este relatório tem seu patch/SHA no manifesto externo, evitando autorreferência do hash deste próprio documento. Não há publicação desses commits.

| Arquivo | SHA-256 |
| --- | --- |
| patches/01-bf4b682cc72c388de1c9486b3cee2fc7294870a7.patch | `7db062410dbbd2e256bfbeded878f0e7dc6c00cce3d2d9ec6522c4f2575cc73a` |
| patches/02-9ebb264db2a6bc05cc855d94cb1387286ae4cab9.patch | `acebbf30d1c8b32833fb40e44e4ea00b53f624665395b7c7d66cdddae81a8355` |
| patches/03-0b5dda51693840a47b65f7a6a0a6ba7a963ef8fc.patch | `0e359850552891f0e82bb3a33246cdc3377978773b30865a7aa71726c35c3486` |
| patches/04-799d49d844734d13707bd51a339dcb2664d9e381.patch | `7713e7a7474d4c48e8f9877784cd913b87d905063c127e84c7754c8d205a4900` |
| patches/05-ef2fb4ce83e8b2366f3536fa371d756c48006201.patch | `08abad5fc8eaa29e84d73ef598f392dcc6d78e4416853c727e00525f399b088d` |
| patches/06-e9ad0dd37e7a4ef094af9c7f8b372ff6db060bd0.patch | `8dd9c3bec67a9489ba07966f92137063339e205aea9106434e43b12c721a7814` |
| patches/07-5cb36d5396c22057b7a6454ed74ffdb47344894b.patch | `309c1ecb7defdfd4b75e6caffd9756bf09d37caa82242543dcea95145111a112` |
| patches/08-e149d11beb84bffc6ed6d59a154477a8a95450b6.patch | `ebe857eeaa515a2ced8b9b98ef8abaab19536708af3a3a605b4370964ba799e5` |
| patches/09-9919f4de4c08c929ee249349a5272d02f7f64336.patch | `2e6c40c8bd744086d5a90f087cc0920074940c745b20978e6bc3ee03cf1c18a8` |
| patches/10-e019050fba6f211d7d8ddb0e13b1d4e82646978c.patch | `9b88c8eaee7d64c28a14c9d66621e246a9f742e4e1f4964a5dfdd69c733cf283` |
| patches/11-9dd88167bd0ba3e3bdbe3d89a666fc255c5abbe2.patch | `50843e950a92072a1c5ec05ae58270c54298ce44c89cb41ebd6380c8fe533c54` |
| patches/12-fa755f370a0d9bca82e1d899acaec0f19f5abe2f.patch | `7e6dd0dc389e0b158928c8b36ca4652d9afbaca3d4abe04eaec936bcf26f8096` |
| patches/13-c1d4ef872fedb4ae2505df2f068fc2f66a6852fc.patch | `57b7db58206c7de05732593686c2c791ba3302ccb33e65e0aaa6e5d9bddcd058` |
| patches/14-c6714f96619276e9ac937f920f8c1ebb0bde09e0.patch | `8c5dadbcd51b0f5c4d3c2598c7952f1b33c3f1b6854a0bdff2f60367f28f04c1` |
| patches/15-4da67d5eb00d48884813697068c47153b561a8ec.patch | `6bb51258d7db16a8ba4565161d8a00110033a2c59e8e2cd30df341d6d862cc96` |
| patches/16-015fe0388ec78bd8e64e180bceb8e74b0d61c5b2.patch | `1fadc95d67a252edde7cb627be4a8feec13302b3d3adc798656168322bb30982` |
| patches/17-77b57657ed36b5eedbf78de01b7c3f01a6394434.patch | `3cb0be08681f59e6efa30bc96edd22b986f04f17b681ecf2df4904dcbc331e96` |
| patches/18-03f8ef3f0689ee50b0f91ec0aea66370c804baf9.patch | `fd30e1d372e33eefc3cecf0d8bee23a8a054ae61f8f6f74e65a87eee60993d03` |
| patches/19-432afcf9fe64028d3af0878e9e3277943ec3e511.patch | `dccbed4a64ebc48eaa1f3909d94403e23a4edfda637affcf087acf6a4d682632` |
| patches/20-7015fef4a8480c5f912c829514cf919e042b9693.patch | `dd5ca752a3c32097a68dd3e627afd7fb34e87db2a43bc682a842a97ddd96a441` |
| patches/21-d3ecbb2f77e87c08b4f7faa4cbab110f284c316c.patch | `2cbcb4b187f977ce3a3c6bbd4b637f1b5ac1937a07a8af1d2cb3f85e3fddc1a2` |
| patches/22-affecc6569d2446ea70c279beddfc4716a4ea72e.patch | `5bbae3fa6a589c8b21ee08f7e87b8a9a98b3db04b72a00070e27059829b24c08` |
| patches/23-da12842e6de663ee4791a6a4010bc622cfed8222.patch | `066caf1a44ce9f838a67b6fca01d114d6573e8db4ed580347ad52b0800aa2452` |

## Histórico detalhado de implementação e revisão

Os registros seguintes são cronológicos; decisões posteriores e a situação consolidada acima prevalecem.

# Relatório em andamento — Checkpoint 0.1.36

Base: 818ec80a492a29936782ddb3a43eecaf3ef996e3. Branch local fix/0.1.36-ajustes. Não publicada. Plano: PLANO_0136.md. Resultados atuais: RELATORIO_0136_TESTES.md.

Os três vídeos foram recebidos e quadros selecionados inspecionados. Não houve controle ou teste no Windows do dono. Capturas de referência e vídeos são evidência visual externa, não reprodução executada por este ambiente.

Registro por item e resultados serão acrescentados após testes. A4 e distinção ROM descarregada/emulador vivo permanecem separados, sem alteração dos contratos protegidos.

## 06 — captura global — parcial

Anterior: QShortcut limitado ao Checkpoint e retorno imediato se a janela não estivesse ativa. Vídeo não prova uma captura global executada. Reprodução controlada anterior: 8 testes existentes, captura bloqueada fora de foco conforme contrato antigo.

Implementado: RegisterHotKey/WM_HOTKEY com MOD_NOREPEAT, validação de combinação, substituição com registro novo antes de liberar o anterior, conflito visível sem salvar configuração inválida, liberação no fechamento aceito. Captura seleciona PID da janela em primeiro plano, exige processo de sessão vivo e associação única; não usa a ficha aberta para decidir. Valida HWND/PID/visibilidade antes/depois de obter pixels; erro não grava arquivo. Sem mudança na sessão por foco.

Arquivos/funções: checkpoint/global_hotkey.py (GlobalCaptureHotkey, WindowsHotkeyApi, native_key), game_capture.py (WindowsCapture, capture_game), window.py (inicialização, set_capture_shortcut, closeEvent); testes de captura 0135/0136. Expectativa antiga de app ativo substituída pela autorização explícita do item 06, preservando associação/arquivo e ausência de sessão.

Posterior: 10 testes Linux com adaptadores, dois jogos, troca/conflito/liberação, múltiplos PIDs, sessão encerrada/ambígua, atribuição e um arquivo por acionamento. Saídas integrais no relatório de testes. Referência nativa: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerhotkey.

Limitações: implementação nativa não executada em Windows nem em jogo/emulador real; QScreen.grabWindow pode não fornecer conteúdo de renderizadores exclusivos/DirectX (erro de imagem nula orienta modo janela, imagem preta não é validação positiva). Processos-filhos/launchers não associados são rejeitados, sem alegar suporte. Checkpoint em primeiro plano não é alvo elegível: ativar a janela do jogo. Windows com jogo/emulador/minimizado, conflito com outro app e pixels efetivos permanecem não testados.

## 04 — banner da ficha — parcial (relato Windows ainda não reproduzido)

Anterior: a implementação já usava KeepAspectRatio. Os testes existentes de bordas passaram. Não se comprovou o recorte relatado no Windows a partir do vídeo/faixa do Início. A primeira execução do novo teste falhou por ausência do método de inspeção banner_rect e por erro da fixture (add_wish não existe em Library); corrigida a fixture usando wishlist isolada, sem mudança de contrato ou asserção.

A área da imagem agora é calculada em banner_rect a partir da geometria atual a cada pintura e desenhada diretamente do pixmap original, sem cache escalado anterior. Removido cálculo de proporção sem uso. Fonte: checkpoint/ui_components.py::Hero.banner_rect/paintEvent/resizeEvent; testes/test_banner_resize_0136.py. Dois jogos de fixture (Aurora/Horizonte), duas proporções 1200×250/600×400, posse e Desejos, abrir em 1280×800/1920×1080 e repetir grande/menor/restaurado. Comparação de pixels das bordas superior/inferior e proporção/contain, sem deformação.

Screenshots sintéticas anteriores: antes-ficha-{1,2}-{1280x800,1920x1080}.png em evidencias-0136. Qt offscreen, DPR 1, 96 DPI lógicos; metadados antes-screens.json. Alteração não prova correção da ocorrência Windows. Maximização nativa e DPI do dono não testados; resize offscreen não equivale a homologação Windows.

## 02–03 — preços, identidade e desconto — parciais

Evidência: 2.mp4 01:31 mostra linhas Indisponível e ausência de ID; é quadro do Windows do dono, não reprodução autenticada. Antes: 11 regressões existentes passaram; 6 novos cenários falharam (preço PC aceito para console, desconto ausente, ordenação ausente, ausência sem motivo). Depois: 28 testes pertinentes passaram. Um teste novo tinha perdido a referência do widget pai; corrigida a fixture, preservadas as asserções.

Integração existente: API oficial quando há chave no cofre; fallback HTML público já existente e configurável. Nenhuma fonte nova nem coleta adicional adotada. Documentação primária consultada em 15/11/2026: https://gg.deals/api/prices/ e https://forum.gg.deals/d/2392-changelog-oct-14-2026-new-api-endpoints. API oferece app/sub/bundle Steam e by-slug (desde 14/10/2026). Resposta documentada traz mínimos atuais/históricos, moeda, título e URL; não documenta original individual, loja, plataforma ou edição. Slug não comprova suporte da API a consoles; cobertura do site não foi usada como prova. Sem credencial GG.deals disponível neste ambiente; nenhuma requisição autenticada/conta real ou jogo console com cobertura API foi validado.

Implementado: guardião de plataforma recusa atribuição de PC a Nintendo DS/Switch e outras plataformas ainda sem identidade comprovada; cache e IDs preservados. Não associa por nome e não baixa ROM. Motivo específico, sem preço zero. URLs antigas de comparação não são reutilizadas em consulta sem contexto compatível. Identidade contextual de oferta salva em settings, sem migração de schema ou alteração de registros de jogos/ROMs.

Desconto só é derivado de original maior que atual na mesma oferta individual classificada, BRL, link GG.deals válido, loja identificada e contexto Steam/plataforma coincidente. Original/histórico de agregados ou cache sem contexto não gera percentual. Arredondamento ao inteiro mais próximo, empate para cima; resultado arredondado zero não exibe desconto. O fallback público existente pode trazer essa oferta; API oficial atual não a fornece. Maior desconto ordena a oferta selecionada conforme política oficiais/keyshops; ausentes ao fim, desempate por título/ID estável. Nenhum histórico tratado como original.

Cards e painel da ficha usam Sem preço salvo com causa; retiradas linhas sem dado Indisponível. API e fonte pública mantidas, links/atribuição preservados. Testes: PC Portal 2/Hades II, consoles Zelda Phantom Hourglass/Metroid Dread sem atribuição PC, cache sem proveniência, contextos diferentes, moedas, ordenação/keyshops, original da mesma oferta e arredondamento. Fixtures não comprovam cobertura real.

Arquivos: checkpoint/prices.py (platform_problem, selected_quote, refresh_prices, wishlist_order); price_view.py (source_url, price_summary, comparison); collection_views.py (ordenação); testes/test_price_integrity_0136.py. Expectativa test_price_display_official da ordenação discount substituída pela autorização do item 03; preservados atribuição e fila sem Steam. Demais testes históricos com original agregado continuam recusando desconto, pois não têm oferta/contexto confiáveis.

Bloqueio restante 02: comprovar resposta autenticada por slug para uma edição console e sua plataforma/BRL, antes de criar vínculo editável explícito de provedor/edição. Proposta: validar produto exato em conta disponível no Windows, guardar slug+plataforma+edição+região+proveniência por confirmação; não inferir de título. Nenhuma mudança de schema necessária enquanto persistência de identidade em settings for suficiente.

Bloqueio restante 03: não há original individual na resposta oficial documentada. Proposta de recorte: manter mínimos oficiais sem desconto na API; exibir desconto apenas para ofertas individuais do fallback já habilitado quando comprovadas, ou aguardar contrato detalhado do provedor. Não adotar scraping novo nem outra fonte sem decisão específica. Nenhum suporte universal declarado.

## 07–08 — Estatísticas e períodos — feito no ambiente Linux

Anterior: screenshot antes-tela-4-1280x800.png reproduziu cards equivalentes com alturas desiguais (com/sem subtítulo), sem reproduzir tooltip nativo do dono. Fonte solicitada Segoe UI, DPR 1, 96 DPI lógicos; gravações 1280×720 não comprovam DPI do Windows. Ausência de serviço/filtros novos registrada pela primeira execução (erro de importação, não reprodução de defeito temporal).

Implementado: cards temporais alinhados, altura/linhas equivalentes; nome longo elidido com título íntegro acessível/tooltip, valor separado sem disputar espaço. Período visível com Diário, Semanal, Mensal, Últimos 3/6/12 meses e Todo o período; preferência persistida. Métricas temporais/heatmap/mais jogados/conclusões usam o mesmo recorte local. Coleção atual (status, jogos, gêneros, plataformas, total app + maior snapshot Steam por jogo) separada; nenhum snapshot Steam distribuído pelo calendário. Sem alegação de deduplicação temporal entre app e Steam.

Limites: [início,agora), dia/mês atuais, semana segunda-feira; janelas móveis subtraem meses de calendário preservando hora, dia limitado ao último do mês destino. UTC guardado permanece intacto; limites e meia-noite calculados no fuso local do sistema ou fuso explícito nos testes; duração da sessão reparte instantes até o limite, incluindo DST de 23/25h. Todo o período também exclui instantes futuros. Fuso não fixado no Brasil. Não recria banco/schema. Agregado Steam permanece somente em Tempo total · app + Steam.

Arquivos/funções: checkpoint/statistics_periods.py (period_bounds, period_stats, instant), statistics_view.py (metric, GameNameButton, render_statistics, build_statistics), activity_heatmap.py (set_interval/interval). Cobertura inclui dois jogos, meia-noite, ano, semanas/mês/mês com dia limitado, janela vazia, snapshot Steam alto que não entra no recorte, DST e preservação exata dos registros. 1280×800/1920×1080 com sete filtros, limites dos labels e alinhamento. Expectativa fixa de 365 células em test_wishlist_prices atualizada para os dias do intervalo móvel de calendário; preservados tempos e agrupamento local, conforme item 08.

Capturas da implementação: estatisticas-tela-4-{1280x800,1920x1080}.png; dados isolados (Portal 2/Metroid Fusion), não banco pessoal. Captura 1280×800 enviada no chat para revisão. Fontes reais/renderização Windows e tooltip no PC do dono não testados; sem mudança global de fonte.

## 09 — Mais estatísticas — feito

Antes: dois testes falharam pois gêneros/conclusões estavam escondidos pelo disclosure. Removido o botão e integrado seu conteúdo na página, sem apagar dados. Arquivos: checkpoint/statistics_view.py::render_statistics; tests/test_statistics_visible_0136.py. Dois jogos de fixture, gênero/status preservados; dez testes pertinentes passaram.

Complemento solicitado durante revisão no chat: a primeira captura de Estatísticas tinha sobra excessiva abaixo da legenda. Substituída altura fixa de 252px por HeatmapViewport, que acompanha a altura calculada do gráfico e eventual barra horizontal; ActivityHeatmap emite height_changed. Teste verifica tamanho ajustado nos sete períodos e duas resoluções, sem retirar rolagem da página. Capturas calor-compacto-tela-4-1280x800.png e calor-compacto-tela-4-1920x1080.png enviadas no chat; reduzem a sobra sem reduzir fontes. Não houve reescrita do commit anterior.

## Complemento do item 07 — Mais jogados como lista da Biblioteca

Solicitado no chat após revisão das capturas: logo à esquerda, nome no meio e tempo à direita. Novo commit, sem reescrever anteriores. Duas fixtures antes falharam porque não havia linhas com logo. Implementado em statistics_view.py::render_statistics, usando list_art.list_icon para logo contida igual à Biblioteca; capa contida/ícone neutro quando falta logo. Nome elidido com título completo no tooltip/acessibilidade; tempo em coluna separada, linha clicável pelo nome. Testes/test_statistics_list_0136.py verifica dois jogos, ordem por tempo, colunas sem sobreposição e duas janelas. Filtros temporais preservados.

## 10 — cinco tamanhos de capa — feito no ambiente Linux

Antes: 3.mp4 00:20 e screenshots anteriores mostram slider longo e três exemplos pequenos. As 13 regressões antigas de layout/serviços passavam; mudança de produto solicitada explicitamente, não falha desses testes. Slider removido, cinco escolhas clicáveis 70/90/100/125/150 (faixa 70–150 já suportada), crescimento visual, base comum, verde, foco e teclado com setas/Espaço/Enter. A opção altera a grade e persiste ao reabrir.

Preferências antigas mantidas no SQLite até nova escolha: 87 é representado/aplicado como 90. Empate vai para menor; extremos fora da faixa mapeiam ao extremo; inválido usa 100. Configurações não recriadas nem migração de schema. cover_size continua lendo valor legado original; nearest_cover_choice governa apresentação/aplicação inicial. Compact antigo de 80 é exibido como 70 por empate, sem apagar a preferência.

Arquivos: checkpoint/settings_previews.py (CoverChoice/CoverSizeChoices), settings_view.py (build_settings), card_layout.py (COVER_CHOICES/nearest_cover_choice), window.py (refresh_library). Removida classe antiga de três exemplos. Expectativas de slider em tests/test_cover_preview_0135.py/test_card_layout.py substituídas pela autorização do item 10, mantendo cobertura de largura, base, cor, proporção, ausência de sobreposição, persistência e efeito na grade. 23 testes pertinentes passaram; duas fixtures de jogos, resoluções 1280×800 e 1920×1080, extremos e preferência 87, teclado/foco.

## 11 — centralização óptica Steam — feito no raster Linux, Windows não testado

Investigados container 48×48, pixmap Steam 32px/Drive 36px, margens/cores e centro geométrico versus massa dos pixels claros. O ICO contém pixels opacos nos cantos; cortar pelo canal alfa não melhoraria a marca. Medição no raster exibido encontrou centro claro deslocado à esquerda/abaixo. Ajustada somente apresentação em +2px horizontal e −1px vertical; normalizado DPR do pixmap para 1 antes de compor o canvas lógico. Marca inteira contida e comparação de ocupação com Drive preservada. Nenhum redesenho, iniciais ST ou Lucide para serviço.

Arquivo original checkpoint/assets/services/steam.ico intacto; SHA-256 9f890a9debcdfccc339149a7943be9aff9e4c9203c2fa37d5671a5b2c88503ad. Arquivos/funções: ui_components.py::service_icon; tests/test_service_optical_0136.py. Primeira compensação de 1px ainda falhou na medida de centro; aumentada para 2px sem alterar tolerância do teste. Nove regressões passaram, incluindo dois jogos e ocupação relativa Steam/Drive. Captura revisao-conexoes-1280x800.png enviada no chat. Testes de raster não equivalem à aprovação óptica do dono nem DPI Windows.

Complemento de revisão da lista: dono aprovou o estilo e pediu mais destaque no tempo. Mantido layout; apenas o tempo recebeu 16px, peso 600 e cor principal, alinhado à direita. Nove testes pertinentes passaram. HeatmapViewport passou a habilitar explicitamente rolagem horizontal quando necessária (a classe-base a desativa); sem remover rolagem de página.

## 01 — tempo em Desejos e posse — feito

Antes: dois cenários falharam por tempo 2h15min visível no card. A ficha exclusiva já ocultava tempo; preservado. Removido apenas o rótulo temporal dos cards de Desejos. Sessões, snapshots, notas e metadados não apagados.

Para coexistência Biblioteca/Desejos, collection.unowned=false explícito agora conserva posse mesmo com wishlist, enquanto ausência de flag mantém semântica legada (wishlist é exclusiva). Adicionar aos desejos pelo menu de jogo possuído grava false, sem retirar da Biblioteca; retirar dos desejos conserva posse. Adição pelo diálogo que reutiliza identidade existente permanece no contrato anterior protegido por regressão: informa que já pertence à Biblioteca. Aquisição exclusiva preserva registro e histórico.

Arquivos/funções: collection_views.py::build_wishlist; library.py::is_owned/owned_games; window.py::add_wish/remove_wish; tests/test_wish_time_0136.py. Testados dois jogos/fixtures, desejo exclusivo, aquisição, coexistência e retirada, tempos Biblioteca e comparação integral das sessões antes/depois. 29 regressões pertinentes passaram. Sem migração de schema nem apagamento/reescrita de instantes.

Complemento do item 10 solicitado no chat: margens externas das cinco capas estavam desiguais apesar de colunas iguais. Reproduzido por quatro testes nas duas janelas: diferença de 31,29px entre bordas esquerda/direita. CoverSizeChoices passou a distribuir pelos contornos reais da arte, com seis vãos equivalentes (externos e internos), conservando proporção, base, foco e escolha. 21 testes pertinentes passaram, sem afrouxar a tolerância nova de 1–2px de arredondamento.

## 05 — descrição no Início — feito

Antes: duas comparações de pixels falharam porque a descrição alterava a imagem pintada do Hero. Retirado apenas o bloco de pintura sobreposta em ui_components.py::Hero.paintEvent. Banco, descrição em Sobre o jogo, arte/logo, plataforma/status e Continuar jogando preservados. Nenhum slogan substituto. Quinze testes pertinentes passaram, incluindo dois jogos, persistência da descrição, ação dentro do banner e redimensionamentos/contain.

Composição: imagem continua contida e proporcional na área; letterbox necessário quando proporções diferem não foi tratado como prova de recorte. Não foi introduzido preenchimento que corte a arte para eliminar faixa. A ocorrência da ficha Windows permanece separada no item 04. Capturas posteriores serão registradas no índice final.

## 12 — revisão transversal — feito no ambiente Linux; homologação Windows pendente

Medidas verificadas: sidebar 198px; corpo 14px, títulos de seção 20px e página 30px, botões principais de 40px; Conexões mantém mínimo 120×36 e ícones 48×48. Fonte solicitada Segoe UI; Linux pode resolver fonte substituta, por isso a aparência não prova métrica Windows. Não aplicado aumento global baseado no vídeo reduzido. Preservados cabeçalho/wordmark e limite contratual de cabeçalho 1392px; Configurações usa largura disponível. Desejos mantém máximo 360px, área 1:1 e mais colunas na janela larga.

Inspeção de Memórias encontrou título sem alternativa íntegra quando longo. Criado ElidedAction, com título elidido, tooltip/acessibilidade completos e largura flexível, mantendo ação de abrir jogo e excluir no card. A primeira fixture inspecionava a grade de uma aba oculta (geometria não calculada); corrigida para grade visível. Reexecutada também sobre cópia limpa do commit anterior: dois testes falharam por falta de tooltip/título acessível; posterior passou sem relaxar a asserção. Não foi apresentado o espaço de nota curta como bug de alinhamento.

Arquivos: ui_components.py::ElidedAction, collection_views.py::memory_card; tests/test_visual_audit_0136.py. Trinta e duas regressões pertinentes passaram: dois jogos, janelas 1280×800/1920×1080, títulos longos/ação dentro do card, colunas/arte/largura Desejos, nove temas, exclusões de mockup, status e backup/memórias. Confirmação de exclusão e arquivos originais mantidos. Complementos de Estatísticas, cinco capas e Steam documentados nos respectivos itens.

Elementos de mockup não implementados: números/círculos; cabeçalho extra Checkpoint; rodapé Biblioteca pessoal; Verde duplicado; ST; dados fictícios do molde. Sem frases decorativas ou tutorial novo. Textos externos/usuário e motivos objetivos mantidos. Nenhum arquivo protegido ou contrato A4 alterado.

Complemento do item 03 solicitado no chat: percentual de desconto na cor de destaque do tema, mantendo original riscado e atual destacado. Implementado via seletor priceDiscount em theme.py e price_view.py, sem cor fixa que fique obsoleta ao trocar tema. Onze regressões pertinentes passaram, incluindo troca pelos nove temas e preservação do percentual calculado. Captura anterior ajuste-revisao-desejos-1280x800.png registra porcentagem ainda neutra; captura final registra o destaque. Todos os preços/tempos das imagens são fixtures, não preços consultados em conta real.

## Revisão decisiva do banner (itens 04–05, referência do dono no chat)

A captura enviada pelo dono mostrou a quebra visual à direita. A composição anterior não atendia ao encaixe exigido. Antes, a altura era limitada a 200/240–300/360px independentemente da proporção original; conter a imagem nesse bloco deixava faixas laterais. Quatro novos testes reproduziram a diferença entre altura do bloco e proporção do arquivo.

Corrigido: a proporção intrínseca fica fixa; heightForWidth calcula a altura correspondente à largura atual, sem limite arbitrário para banners presentes. banner_target usa geometria fracionária e escala uniforme da imagem original inteira; banner_rect fornece apenas os limites inteiros de inspeção. Arredondamento de até um pixel de altura não deforma a arte nem gera a antiga faixa lateral. Não há cache de escala anterior. Fallback sem banner mantém layout próprio.

Primeira tentativa inteira ainda deixava até 2px ao refazer contain; teste falhou e foi corrigido com geometria fracionária, mantendo a tolerância. Testes de proporção exata, quatro bordas coloridas preservadas, duas artes/jogos, larguras 750/1026/1388/1700 e retorno, Biblioteca/Desejos e showMaximized/showNormal no Qt offscreen: 29 passaram. Duas expectativas antigas de teto de altura em test_ui_polish foram substituídas pelo requisito posterior explícito de proporção/encaixe; preservados teste de pixels, limite da área e ausência de recorte. Alteração nova, sem reescrever commits anteriores.

Capturas banner-proporcional-revisao-inicio-1280x800.png, banner-proporcional-revisao-ficha-biblioteca-1280x800.png e banner-proporcional-revisao-inicio-1920x1080.png enviadas no chat; PNGs da ficha nas duas janelas disponíveis. Portal 2/Hades com arte pública Steam 1920×620; tempos/cadastro isolados. O defeito de composição foi reproduzido/corrigido no Linux. Maximização Qt offscreen não comprova comportamento do gerenciador de janelas/DPI no Windows do dono. Status atualizado do item 04: feito no ambiente disponível, Windows não testado.

Complemento 11/DPI: primeiro teste a 150% encontrou diferença na variante do ICO escolhida implicitamente por QIcon. Fixada seleção explícita em DPR 1 antes da composição, conservando imagem inteira e SHA do asset. Quinze testes passaram em 150% e quinze em 200%. A primeira suíte integral anterior ao ajuste decisivo do banner terminou com 588 passed/2 failed em 398,91s; únicas falhas: coordenadas antigas do teste da logo. Dono autorizou explicitamente atualizar x+8/y+8 para x+10/y+7 e o raster em 100%, mantendo igualdade exata dos pixels e contagem >15. Nenhuma asserção de integridade removida. A suíte será reexecutada após as últimas correções.

Complemento 12: desativado desenho da base nativa do ClickTabBar, que produzia linha clara acima das abas na captura Fusion. Mantidos seleção por clique completo e teclado, regressões do item 18 da 0.1.35 preservadas.

Complemento de integridade dos itens 02–03: revisão encontrou que um cache com contexto de uma identidade Steam antiga ainda podia mostrar preço após trocar a edição. Dois testes reproduziram. selected_quote agora recusa a apresentação desse cache com motivo Identidade alterada; valor/proveniência permanecem armazenados. source_url usa a identidade atual em vez do link da edição antiga. 27 regressões pertinentes passaram; nenhum preço/ID original apagado. Não amplia suporte de consoles nem associa por nome.

Revisão final de integridade do item 03: ofertas empatadas reproduziram mistura de loja de keyshop com rótulo oficial e original de uma segunda loja. A seleção agora fixa uma única oferta, e loja/original/desconto acompanham essa mesma entrada; não busca original de outra oferta empatada. 28 regressões pertinentes passaram, incluindo recusa do percentual quando a oferta selecionada não tem original.

Revisão final do item 01: preferência legada collection.unowned=null foi reproduzida com divergência entre is_owned e owned_games. Corrigido o fallback para a semântica legada da wishlist quando a flag é nula; false/true explícitos continuam definindo posse. Teste conserva os valores salvos e verifica concordância; sem migração ou limpeza de dados.

## Última decisão de apresentação — ausência de preço com hífen

Pedido posterior do dono substitui o texto principal Sem preço salvo pelo hífen literal `-`, em cards e no painel da ficha. Motivo curto específico permanece embaixo (pendente, sem ID, sem oferta oficial, falha, plataforma/edição não confirmada ou cache sem origem). Não transforma ausência em zero e não altera preços guardados. Arquivo: price_view.py::price_summary. Expectativas em test_visual_complements_0135/test_price_integrity_0136 atualizadas somente nesse texto por autorização direta no chat; causas, ausência de Indisponível e preservação de valores mantidas. Cinco testes falharam antes e 22 pertinentes passaram depois. Captura hifen-revisao-desejos-1280x800.png enviada no chat. Esta decisão prevalece sobre a redação anterior dos itens 02–03 neste histórico.

Pacote técnico wheel 0.1.36 construído localmente e instalado isoladamente; smokes de seis páginas/integridade SQLite e cadastro/auxiliar/renderização passaram no Linux. Não é pacote Windows homologado nem instalador para o dono. Não houve publicação.

Metadados de renderização: fonte solicitada Segoe UI, resolvida OpenAI Sans neste Linux, corpo 14px; DPR 1, DPI lógico 96; tela virtual 800×800. Janelas Qt capturadas em 1280×800 e 1920×1080 lógicos, mesmo quando maiores que essa tela virtual. Escalas de geometria/raster 150%/200% testadas separadamente; não declarar que o desktop Windows ou seu DPI foram reproduzidos.

Verificação remota somente leitura: fix/0.1.35-ajustes continua 818ec80a492a29936782ddb3a43eecaf3ef996e3 e v0.1.35 continua df5ff41e74b36cea4e2abd160e1172f4166bf32a. Nenhuma ref remota fix/0.1.36-ajustes retornada. Sem push/PR/tag/release/workflow. Contratos/assets/workflows comparados byte a byte com a base; UTF-8/LF e diff --check passaram nos arquivos alterados.

## Complemento posterior — ficha continua em Desejos, sem aquisição na ficha

Dono observou que abrir um desejo marcava Biblioteca na lateral. Quatro testes reproduziram a troca indevida de contexto em dois jogos, com/sem banner. build_detail agora conserva Desejos como origem quando aberto pela lista ou quando é desejo exclusivo; ambos os botões de voltar (banner e cabeçalho sem arte) retornam aos desejos. Abrir a ficha preserva integralmente jogo, wishlist e posse. Quando o usuário executa uma aquisição explícita na lista, acquire_wish passa ao contexto Biblioteca.

Após pergunta específica, o dono respondeu Retirar o botão da ficha. Removido Adicionar à biblioteca somente da ficha exclusiva de Desejos. Menu dessa ficha oferece Retirar dos desejos, sem Remover da biblioteca nem ação duplicada de adicionar aos desejos. Aquisição pela lista permanece ação explícita para quando tiver o jogo; abrir/ver detalhes nunca a executa.

Arquivos/funções: checkpoint/detail_view.py::build_detail; window.py::acquire_wish; tests/test_wish_navigation_0136.py. Teste test_detail_0135 foi atualizado apenas da presença para ausência do botão, por aprovação direta, mantendo aba única, ausência de Galeria/Configurar execução e quatro abas depois da aquisição. Sessões/metadados/IDs não apagados. 69 regressões pertinentes passaram, incluindo o contrato protegido test_visual_0132 sem qualquer alteração nele. Esta decisão posterior substitui a exigência anterior de manter o botão na ficha.

Validação intermediária concluída com 600 passed em 408,20s, antes de consolidar esse último complemento; não é homologação do novo contexto da ficha. Uma execução substituída pelo pedido do hífen foi interrompida e teve stdout/stderr/código −15 preservados. A validação integral final terá como base o último commit de código, sem mudanças de produção durante a execução.

## Complemento posterior — coração de favorito

Relato do dono: botão de coração parece não funcionar. Reproduzido em dois jogos, Biblioteca e Desejos: o clique já gravava favorite=1 no SQLite, mas o coração permanecia sempre contornado e não indicava estado marcado. Quatro testes falharam na ausência desse feedback, depois de confirmar a gravação.

Correção: botão checkable carrega o estado persistido; marcado fica preenchido na cor do tema, desmarcado volta ao contorno. Tooltip/acessibilidade Marcar/Retirar preservados. Ícone Lucide recebe preenchimento somente na renderização; arquivo SVG original não é editado/substituído e nenhuma marca de serviço é alterada. Sem mensagens decorativas novas.

Arquivos/funções: detail_view.py::build_detail, design_system.py::IconButton.paintEvent, icons.py::lucide_icon (parâmetro filled opcional). Tests/test_favorite_0136.py valida marcar/desmarcar, pixels do centro, reabrir ficha, leitura por outra conexão SQLite e filtro Favoritos positivo/negativo, preservação de notas/descrição/wishlist/posse (favoritar desejo não o adquire). 23 regressões pertinentes passaram, incluindo navegação de Desejos e ícones. Capturas específicas de marcado/desmarcado acompanham a revisão.

## Complemento posterior — controle de status conforme referência

Dono enviou recorte do controle Jogando e pediu o mesmo estilo, ignorando a anotação 2. Antes, ponto e dropdown eram widgets separados com aparência neutra; dois testes reproduziram a falta de agrupamento. Criado StatusControl, QComboBox funcional com ponto real interno, fundo suave, borda/texto/seta no destaque do tema e foco visível; sem número/círculo de anotação. Espaçamento da barra reduzido localmente para manter o conjunto utilizável em janela menor, sem diminuir fonte.

Backlog, Jogando, Pausado, Concluído e Abandonado mantidos; Não iniciado continua só mapeado visualmente para Backlog até escolha explícita. Menu nativo mantém estado atual em negrito; clique no ponto e teclado abrem/selecionam/salvam corretamente. Nenhuma asserção antiga alterada, inclusive a presença do ponto (agora filho real do controle, visível).

Arquivos/funções: checkpoint/status_control.py::StatusControl; detail_view.py::build_detail. Tests/test_status_pill_0136.py cobre dois jogos, duas janelas, contorno na cor do tema, agrupamento/limites, textos sem corte, ausência da anotação e mouse/teclado; regressões antigas de status/legado preservadas. 22 testes pertinentes passaram e 16 na bateria com seleção real por mouse/teclado. Captura status-final-revisao-ficha-biblioteca-1280x800.png enviada no chat. Execução integral intermediária: 608 passed em 409,72s, anterior à consolidação deste controle; a suíte final será repetida no commit com o componente.

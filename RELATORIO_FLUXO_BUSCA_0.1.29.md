# Prova do fluxo de busca — Checkpoint 0.1.29

## Base e isolamento

Branch `fix/0.1.29`, recebida limpa em `a46bff43a146be5c1aa89951361cb0041e401be9`.
Código do aplicativo inalterado nesta tarefa: `git diff a46bff4 -- checkpoint/` vazio.
Commit dos testes, automação e renderizador: `d64d6a0cdf0d6c0dd665c33f75028b664eb0a47e`.
Não houve build, push, tag, release ou PR. Nenhuma leitura de cofre real; o método de
consulta é substituído por retorno vazio. Fontes são falsas/controladas e o transporte
usa PNGs locais explicitamente rotulados, sem banco de cadastro pré-preenchido.
Qt offscreen em Linux, Python 3.12.14 / PySide6 6.8.3; não valida Windows ou APIs reais.

## 1. Mesmo teste nos dois commits

`tests/test_add_from_search_flow.py::test_search_selection_persists_text_source_and_images`
abre a janela principal, clica em Adicionar, digita Metroid, pesquisa, escolhe um dos
resultados por clique e clica em Adicionar à biblioteca. Não chama diretamente
`apply_catalog`, `show_result`, `validate` ou `save_import`: todos são executados pelo
caminho normal da interface. Usa os Jobs, subprocessos auxiliares, execute_request,
catálogo, cache de imagens, fila de conclusão e SQLite reais. Somente provedores,
transporte de imagens e acesso ao cofre são substituídos nas fronteiras externas.

O teste determinístico salva durante a consulta dos detalhes selecionados. Um marcador
libera a resposta depois do clique; não há sleep na thread da interface. A fonte textual
fica indisponível no enriquecimento posterior, mas a fonte de artes continua disponível.
Isso impede o enriquecimento de reparar e esconder a perda da resposta selecionada.
O segundo teste salva depois de a ficha carregar, cobrindo também esse caminho.
A referência forte ao diálogo no driver é mantida em ambos os commits; não se altera
o ciclo de vida do aplicativo. As filas são drenadas antes das asserções/fechamento.

A cópia da base foi criada fora do checkout com `git archive 8d39c18 | tar -x -C
/tmp/checkpoint-search-proof-base`; somente os novos arquivos de teste e suporte foram
acrescentados à cópia. Seus hashes são idênticos aos da branch atual:

- teste: `181c4e08c9ce0b36ea42e6e10b3ddb37e87a2d52d312a63b86b6ea379d6a4c8c`
- suporte: `559e3dcb4dfa25c332d53ac28f504b732c32816cf6417e4b1a609e74f554129a`

Comando na cópia da base (a partir desse diretório):

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 /workspace/Checkpoint/.venv/bin/python -X faulthandler -m pytest tests/test_add_from_search_flow.py::test_search_selection_persists_text_source_and_images -q -p no:cacheprovider
```

Saída completa, exit 1; imagens conferidas antes da asserção textual:

```text
F                                                                        [100%]
=================================== FAILURES ===================================
____________ test_search_selection_persists_text_source_and_images _____________

app = <PySide6.QtWidgets.QApplication(0x3d0a3b90) at 0x7f3d4c0a5c00>
library = <checkpoint.library.Library object at 0x7f3d4c06fec0>
folder = PosixPath('/tmp/92a0cda6a25c4032a46388b0113c9206')

    def test_search_selection_persists_text_source_and_images(app, library, folder):
        window, game = save_via_search(app, library, folder / 'search-source')
        try:
            # Confira primeiro as imagens: o caso antigo salvava artes, mas perdia texto.
            assert Path(game['cover']).is_file()
            assert Path(game['banner']).is_file()
>           assert game['developer'] == METROID['developer']
E           AssertionError: assert '' == 'MercurySteam'
E
E             - MercurySteam

tests/test_add_from_search_flow.py:12: AssertionError
=========================== short test summary info ============================
FAILED tests/test_add_from_search_flow.py::test_search_selection_persists_text_source_and_images
1 failed in 1.97s
```

Comando na branch atual:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests/test_add_from_search_flow.py -q -p no:cacheprovider
```

Saída completa, exit 0:

```text
..                                                                       [100%]
2 passed in 3.59s
```

## 2. Correção do app

Não foi necessária correção nova em checkpoint/. A correção já presente em a46bff4
aguarda os Jobs do diálogo antes de concluir, aplica os detalhes selecionados e conserva
os textos e a origem Busca ao persistir. O fluxo antigo encerrava o diálogo antes da
resposta dos detalhes e descartava essa resposta, deixando o resumo sem texto salvo;
a origem Manual também não era substituída. Isso é demonstrado para o cenário controlado,
não é diagnóstico de toda possível falha de provedor no Windows.

## 3. Origem de Playdead

Há duas origens distintas no teste anterior: a resposta HTTP controlada do teste de
parser Steam contém developers/publishers Playdead; e provider_result() retorna um
MetadataResult com Playdead. Nos testes de preservação por falha de download e resposta
de identidade errada, save_import recebia diretamente esse último fixture. Portanto,
essas asserções não provavam a busca. Agora ambos iniciam por add_inside_through_search,
que usa o mesmo percurso por cliques com fonte Steam controlada de INSIDE; verifica
Playdead e origem Busca no registro salvo. O teste de falha de imagens mantém o transporte
indisponível e a asserção de capa vazia. Os demais testes unitários de preenchimento,
concorrência e parser mantêm fixtures explícitos para seus respectivos escopos;
não são apresentados como prova do cadastro por busca.

Diff completo de tests/test_enrichment.py:

```diff
diff --git a/tests/test_enrichment.py b/tests/test_enrichment.py
index 1310448..304292c 100644
--- a/tests/test_enrichment.py
+++ b/tests/test_enrichment.py
@@ -64,8 +64,21 @@ def test_unknown_game_never_searches_by_name(library):
     provider.search.assert_not_called()


-def test_download_failure_keeps_metadata_and_game(library, folder):
-    identity = save_import(library, {'title': 'INSIDE'}, result=provider_result())
+def add_inside_through_search(app, library, folder, *, images_unavailable=False):
+    from scripts.search_flow_support import INSIDE, save_via_search
+    window, game = save_via_search(app, library, folder / 'inside-search',
+                                  {**INSIDE, 'images_unavailable': images_unavailable})
+    try:
+        assert game['developer'] == 'Playdead'
+        assert game['source'] == 'Busca'
+        return game['id']
+    finally:
+        window.close()
+        app.processEvents()
+
+
+def test_download_failure_keeps_metadata_and_game(library, folder, app):
+    identity = add_inside_through_search(app, library, folder, images_unavailable=True)
     provider = Mock(); provider.details.return_value = provider_result()
     cache = Mock(); cache.download.side_effect = IntegrationError('Unavailable')
     assert 'Algumas informações ou imagens não puderam ser obtidas.' in complete_game(library, identity, steam_provider=provider, cache=cache)
@@ -88,8 +101,8 @@ def test_concurrent_edit_during_download_is_preserved(library, folder):
     assert library.sql.execute("SELECT count(*) FROM artwork_assets WHERE kind='cover'").fetchone()[0] == 0


-def test_wrong_identity_response_never_applied(library, folder):
-    identity = save_import(library, {'title': 'INSIDE'}, result=provider_result())
+def test_wrong_identity_response_never_applied(library, folder, app):
+    identity = add_inside_through_search(app, library, folder)
     provider = Mock(); provider.details.return_value = MetadataResult('steam', '999', 'Other', developer='Wrong')
     complete_game(library, identity, steam_provider=provider, cache=Cache(folder))
     assert library.get(identity)['developer'] == 'Playdead'
```

## 4. Capturas do fluxo por cliques

Geradas a partir da árvore limpa do commit
`d64d6a0cdf0d6c0dd665c33f75028b664eb0a47e`, sem preenchimento manual do cadastro:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python scripts/render_search_flow_review.py /tmp/checkpoint-029-real-flow-review
```

- `evidence/ui-0.1.29/real-flow-1280x800-detail.png` — 84.256 bytes, 1280×800.
- `evidence/ui-0.1.29/real-flow-1920x1080-detail.png` — 95.719 bytes, 1920×1080.
- `evidence/ui-0.1.29/real-flow-info.json` — commit, árvore limpa, dimensões,
  SHA-256 dos PNGs, campos lidos do banco e confirmação de imagens no disco.

As duas capturas foram inspecionadas: descrição, MercurySteam, Publicadora · Nintendo e
Origem · Busca aparecem após o salvamento; o banner diz FONTE CONTROLADA. A capa é
verificada no disco, não inserida artificialmente na ficha. Não foram semeadas sessões,
conquistas ou galeria. Os bancos/cache de teste temporários foram removidos; só PNGs e
manifesto foram copiados para evidence. A barra de ações continua visualmente alta,
sobretudo em 1920×1080: esta tarefa não altera o layout para embelezar a prova.
A mensagem de enriquecimento posterior indisponível também foi preservada na captura.

## 5. Inventário das 16 capturas anteriores

`review-info.json` antigo não contém hash ou estado da árvore na geração. Logo não é
possível certificar retrospectivamente que cada PNG foi gerado de um commit limpo
atual: estar versionado em a46bff4 não comprova isso. O histórico abaixo informa apenas
o último commit que alterou cada arquivo. O renderizador antigo usa Library.save_game
com desenvolvedora/editora/descrição/artes semeadas manualmente; o diálogo usa
apply_catalog/show_result diretamente, sem busca/salvamento. Preços e estados de conexão
também são controlados. Nenhuma dessas 16 imagens serve como prova do fluxo corrigido.

Prefixo dos caminhos: `evidence/ui-0.1.29/`. “Manter visual” significa conservar como
revisão de layout com rótulo de fixture e descartar como evidência de busca/persistência.

| Arquivo | Última alteração no Git | Geração do commit atual comprovada? | Cadastro/preview manual? | Recomendação |
|---|---|---|---|---|
| 1280x800-add.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1280x800-appearance.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1280x800-detail.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1280x800-home.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1280x800-library.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1280x800-settings.png | a46bff4 | Não comprovada | Sim | Manter visual |
| 1280x800-wish-prices.png | a46bff4 | Não comprovada | Sim | Manter visual |
| 1280x800-wishlist.png | a46bff4 | Não comprovada | Sim | Manter visual |
| 1920x1080-add.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1920x1080-appearance.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1920x1080-detail.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1920x1080-home.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1920x1080-library.png | f0be1b9 | Não comprovada | Sim | Manter visual |
| 1920x1080-settings.png | a46bff4 | Não comprovada | Sim | Manter visual |
| 1920x1080-wish-prices.png | a46bff4 | Não comprovada | Sim | Manter visual |
| 1920x1080-wishlist.png | a46bff4 | Não comprovada | Sim | Manter visual |

## 6. Suíte e entrega

Comando integral no mesmo código de d64d6a0 (somente documentação/evidências
foram acrescentadas depois):

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

Saída completa, exit 0:

```text
........................................................................ [ 24%]
........................................................................ [ 48%]
........................................................................ [ 72%]
........................................................................ [ 97%]
........                                                                 [100%]
296 passed in 387.99s (0:06:27)
```

Resultado: 296 passando, 0 falhas, 0 erros; eram 294 antes dos dois novos casos.
Os dois testes de enriquecimento por INSIDE agora percorrem busca/seleção reais
com fonte controlada e mantêm suas asserções anteriores. Não se removeu asserção
nem se introduziu skip/xfail. A cópia temporária da base foi removida após os testes.
A entrega contém dois commits locais: automação/testes/renderizador, depois
relatório/documentação/PNGs/manifesto. O commit final pode ser obtido por
`git rev-parse fix/0.1.29`; não é inserido no próprio relatório para evitar referência
circular ao hash do arquivo que o contém.
O teste de lifecycle/SIGSEGV não foi alterado; não há skip/xfail novo.
Não foram instaladas dependências nesta tarefa. A versão e o schema permanecem 0.1.29 e 4.

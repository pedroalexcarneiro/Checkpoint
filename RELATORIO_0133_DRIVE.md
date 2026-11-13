# Correção Drive — Checkpoint 0.1.33

Base: `4bdb4ef` da `fix/0.1.32-visual`. Branch isolada `fix/0.1.33-drive`. Sem tag, release, PR ou force push. As branches anteriores e o schema 4 foram preservados. Versão declarada atualizada para 0.1.33.

## Alterações por arquivo

- `checkpoint/integrations/drive.py`: artigos The/A/An são movidos antes do título principal; separadores de subtítulo tornam-se dois-pontos; tags reconhecidas de região/revisão/língua são removidas; inferência também cobre Mega Drive/Master System/Game Gear. Extensões empilhadas e `# GBA` continuam preservando plataforma e separando o nome original do título de pesquisa.
- `checkpoint/quick_add.py`: reutiliza a mesma consulta, lista, delegate e callback de escolha já existentes. Após escolher a ROM, candidatos continuam visíveis mesmo após sugestão exata/detalhes; outra escolha percorre `choose` e busca os detalhes normalmente. A lista recebe check do delegate. Oculta o link redundante de outra escolha e permite altura mínima de 700 px para acomodar a lista, sem sobrepor ações. Sem candidatos, oculta a lista e mantém aviso, pesquisa manual e atualização do índice; salvar depende de clique explícito e preserva o vínculo.
- `checkpoint/catalog_result_visuals.py`: o estado de índice vazio não é mostrado sobre o catálogo de uma ROM já selecionada.
- `checkpoint/detail_view.py`, `checkpoint/ui_components.py`: ficha incompleta usa cabeçalho com título limpo; não desenha o título grande no banner. Sem banner/logo, a área vazia é ocultada. Aviso e pesquisa manual da ficha continuam preservados.
- `checkpoint/__init__.py`, `pyproject.toml`: versão 0.1.33.
- `tests/test_drive_0133.py`: dez nomes reais/exemplos de catálogos DS/GBA/NES/GB/GBC/SNES/Mega Drive e Game & Watch, teste adicional de artigos A/An/The, fluxo por cliques e persistência com fonte que responde apenas à consulta normalizada, e ausência de resultados com aviso/ações antes de salvar explicitamente. Dados são controlados na fronteira do worker; widgets, Job, seleção, validação, MainWindow e SQLite são reais. Não preenche o formulário diretamente.

Os exemplos obrigatórios foram cobertos, inclusive Yu-Gi-Oh! com hífen oficial preservado e Zelda (Game & Watch) com o descritor mantido. Decisão conservadora: não remover todos os parênteses indiscriminadamente, pois descritores legítimos como (Game & Watch) e (The Return) fazem parte do título; removem-se marcações de metadados reconhecidas. Não se associa imagem do arquivo/pasta Drive nem se adiciona provedor: origem de texto permanece Busca e vínculo fica em game_files.

Documentação atualizada: README.md, PROJECT_STATUS.md, CONTINUITY.md e CHANGELOG.md distinguem o código 0.1.33 sem release da pré-release anterior.

## Expectativas existentes alteradas — justificativa explícita

1. `tests/test_rom_titles_0129.py`: `Pokemon - Platinum` passou a `Pokemon: Platinum`, pois a regra solicitada agora converte o separador de subtítulo. Extensão, região e plataforma continuam testadas. A mudança acompanha a nova regra funcional; não remove a verificação nem tolera ausência de resultado.
2. `tests/test_visual_0132.py`: o teste que congelava integralmente QuickAdd contra c51c245 agora excetua somente `show_result` e `show_missing_metadata`, os dois métodos que este pedido exige mudar. Todos os demais métodos, os caminhos de validação/persistência e as comparações byte a byte de testes/suporte Drive, worker/enriquecimento/fila continuam exigidos.

`tests/test_save_lifecycle.py` não foi alterado. Nenhum skip/xfail novo, alteração de timeout ou remoção de asserção de lifecycle. Nenhum teste do Drive anterior foi alterado. A primeira rodada integral de diagnóstico foi interrompida após identificar a expectativa antiga do subtítulo, antes de repetir a suíte final. Não é apresentada como aprovação.

## Prova antes/depois

Comando, nas duas revisões:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp .venv/bin/python -m pytest tests/test_drive_0133.py::test_drive_normalized_search_click_flow -q -p no:cacheprovider
```

Na base 4bdb4ef, somente o teste novo estava adicionado; código do aplicativo intacto. Saída completa:

```text
F                                                                        [100%]
=================================== FAILURES ===================================
___________________ test_drive_normalized_search_click_flow ____________________

app = <PySide6.QtWidgets.QApplication(0x1f538ec0) at 0x7f84005e9500>
library = <checkpoint.library.Library object at 0x7f84005468d0>
folder = PosixPath('/tmp/6f84db4e650d412d95133a2a31ed7e1e')

>   def test_drive_normalized_search_click_flow(app,library,folder):drive_flow(app,library,folder,capture=True)
                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_drive_0133.py:91:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
tests/test_drive_0133.py:76: in drive_flow
    if errors:raise errors[0]
              ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def tick():
        try:
            assert time.monotonic()<deadline,'Fluxo não concluiu'
            d=app.activeModalWidget()
            if not d or not hasattr(d,'quick_add'):return
            q=d.quick_add;state['dialog']=d
            if 'stage' not in state:
                QTest.mouseClick(q.sources,Qt.LeftButton,pos=q.sources.tabRect(1).center());QTest.keyClicks(q.query,'Spirit');state['stage']='rom'
            elif state['stage']=='rom' and q.results.count():
                QTest.mouseClick(q.results.viewport(),Qt.LeftButton,pos=q.results.visualItemRect(q.results.item(0)).center());state['stage']='catalog'
            elif state['stage']=='catalog' and seen and not q.jobs:
>               assert seen==[expected],f'Pesquisa enviada: {seen!r}; esperada: {expected!r}'
E               AssertionError: Pesquisa enviada: ['Legend of Zelda, The - Spirit Tracks']; esperada: 'The Legend of Zelda: Spirit Tracks'
E               assert ['Legend of Z...pirit Tracks'] == ['The Legend ...pirit Tracks']
E
E                 At index 0 diff: 'Legend of Zelda, The - Spirit Tracks' != 'The Legend of Zelda: Spirit Tracks'
E                 Use -v to get more diff

tests/test_drive_0133.py:55: AssertionError
=========================== short test summary info ============================
FAILED tests/test_drive_0133.py::test_drive_normalized_search_click_flow - As...
1 failed in 0.55s
```

Mesmo teste, sem mudança para fazê-lo passar, depois da correção:

```text
.                                                                        [100%]
1 passed in 0.49s
```

Os testes focados originais Drive + novos passaram: 18 em 6,81 s. Nova rodada de normalização/fluxo: 19 em 1,01 s, incluindo artigos A/An e expectativas do parser.

## Suíte completa

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

**357 passed in 474.59s (0:07:54)**, exit 0, sem falhas/erros/skips/xfails na execução final. Linux Qt offscreen, dados em /tmp.

## Capturas reais da UI com fonte controlada

Código de geração: `1fabaefdf50780b6f88d45109ae84a6d8e17f5bb`. Capturas obtidas por grab do diálogo durante o fluxo automatizado, sem preenchimento manual de ficha, sem conta/credencial real, com catálogo falso explicitamente controlado. Não são consultas RAWG/Steam reais. As PNGs não incluem tokens nem chaves. Manifesto com hash/tamanho/commit: `evidence/ui-0.1.33/manifest.json`.

- `evidence/ui-0.1.33/drive-resultados.png`: dois candidatos e check verde, título normalizado, plataforma e fonte; ações sem sobreposição.
- `evidence/ui-0.1.33/drive-sem-resultado.png`: lista oculta, aviso explícito e ações Pesquisar manualmente/Atualizar índice do Drive; ROM identificada continua vinculada.

## Limitações

Validação em Linux Qt offscreen e diretórios temporários /tmp. Não validado em Windows real, DPI/fontes do usuário, contas e autorização reais do Drive, consultas reais RAWG/Steam/SGDB, transporte/autenticidade de artes externas ou disponibilidade desses catálogos. Não houve mudança de credenciais, cofre, protocolo OAuth ou indicador de conexão das Configurações: isso não faz parte desta correção. A lista usa arte local quando disponível, sem inventar capas.

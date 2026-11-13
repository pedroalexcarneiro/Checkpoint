# Correção 0.1.30 — cadastro de ROM do Drive

## Base, escopo e decisões

Branch fix/0.1.30 criada do commit 90dec8e168d822698e176e5c93dd98951e01ab09.
O prefixo 90dec8e8 fornecido no pedido não resolve: foi usado o 90dec8e também
citado pelo dono no item de teste e confirmado na entrega anterior.
A branch fix/0.1.29 permanece em 572cb3c50f8257d95f973887baed57f52ac15f90,
sem alterações. A tag/release v0.1.29 continua no código 90dec8e.
Nesta tarefa não se cria tag, release ou PR; push somente da fix/0.1.30, sem force.
Versão declarada 0.1.30; schema continua 4, sem migração destrutiva.

Decisão conservadora: quando não há texto identificado, a origem de dados é
Não identificada; Google Drive identifica somente o arquivo vinculado. A origem
vira Busca quando texto do catálogo é aplicado. Cadastros antigos com origem
personalizada e edições pessoais não são sobrescritos silenciosamente.

## Diagnóstico e correção

A seleção da ROM já passava por normalize_rom_name, que retira extensão,
marcador de plataforma e região do exemplo. O teste confere que RAWG recebe
somente Pokemon Emerald, mantendo Pokemon Emerald [USA] # GBA.zip no índice.
Não foi preciso alterar essa função.

Havia dois defeitos demonstrados: (1) ao selecionar uma ficha, a origem Google
Drive não era corrigida; (2) o botão Adicionar ficava habilitado durante a
pesquisa inicial, permitindo concluir sem os detalhes e ignorar a resposta por
finishing. Sem resultado ou fonte indisponível não havia aviso persistente.

Agora a ROM selecionada dispara a mesma busca do catálogo, sem misturar a ROM
novamente nos resultados de fichas. Salvar aguarda pesquisa e detalhes, e uma
escolha ambígua continua exigindo seleção explícita. Falhas permitem salvar a
ROM identificada como incompleta, com aviso e ação de pesquisa manual, sem
iniciar um enriquecimento sem identidade que esconda o resultado da busca.
Na ficha, o aviso é calculado dos campos efetivos e do vínculo Drive, portanto
permanece ao reabrir. O botão abre a pesquisa para o mesmo arquivo/jogo e não
cria duplicata. Alterar o nome de pesquisa mantém o vínculo e a plataforma.

Textos vêm de RAWG/Steam. Para ROMs vinculadas ao Drive, o enriquecimento não
persiste imagens RAWG/Steam; artes automáticas vêm do SteamGridDB. Não se busca
arte no arquivo ou na pasta do Drive e não se baixa a ROM ao cadastrá-la.

## Arquivo por arquivo

- scripts/drive_search_flow_support.py: fornecedor RAWG/SteamGridDB controlado,
  transporte local de imagens e índice fictício de ROMs; automação por cliques.
- tests/test_drive_search_flow.py: quatro casos (seleção explícita; salvar durante
  pesquisa; sem resultado; fonte indisponível). Confere textos/data/origem,
  três artes reais no disco com provider SteamGridDB e vínculo/nome original.
- checkpoint/quick_add.py: estados Drive/catálogo, bloqueio de salvar durante
  consultas, resultados sem repetir a ROM, mensagens e pesquisa manual.
- checkpoint/dialogs.py: origem Não identificada/Busca e validação de consulta
  inicial pendente. Mantém a espera de Jobs e não altera o teste de lifecycle.
- checkpoint/game_import.py: textos de catálogo mudam a origem para Busca,
  inclusive em cadastro existente e complete_identity, mantendo a transação.
- checkpoint/enrichment.py: origem atualizada ao preencher texto confirmado;
  imagens automáticas de ROM somente da fonte SteamGridDB.
- checkpoint/window.py: recuperação manual usa o cadastro existente; sem dados
  não inicia enriquecimento sem identidade e informa o resultado na barra.
- checkpoint/detail_view.py: aviso persistente e botão Pesquisar manualmente.
- tests/test_drive_metadata_policy.py: comprova por cliques a recuperação do
  mesmo jogo sem duplicata; confere que RAWG preenche texto mas não salva arte.
- tests/test_quick_add.py: atualiza somente a expectativa de origem sem texto,
  de Google Drive para Não identificada. As demais asserções são preservadas.
- checkpoint/__init__.py e pyproject.toml: versão 0.1.30.
- README.md, CHANGELOG.md, CONTINUITY.md e PROJECT_STATUS.md: estado e regras atuais.
- RELATORIO_0130_DRIVE.md: resultados, diff, decisões e limitações desta tarefa.

## Prova sem modificar o teste para passar

O teste e o suporte foram criados antes de alterar o app e copiados idênticos
para uma exportação git archive 90dec8e em /tmp/checkpoint-0130-base.
Commit de reprodução: 941738d. Commit da correção: afa9ae9.
Hashes preservados depois da correção:

- tests/test_drive_search_flow.py: 33c4c6681308aa51d24ddf7ec05d67eb12cd3005cec64fd70577a970adc0f059
- scripts/drive_search_flow_support.py: efe071911ba1712b5e83d08d2ad9d9ea83faac7b67a796851d8d77bde572ac13

Não há preenchimento direto do formulário nem chamadas diretas a apply_catalog,
show_result, validate ou save_import no teste do fluxo. O driver abre Adicionar,
clica na aba ROM do Drive, digita, escolhe a ROM e, quando necessário, a ficha,
e clica em Adicionar. Jobs, subprocessos, catálogo, cache, filas e SQLite reais.
Somente fornecedores externos/transporte de imagens e consulta ao cofre são
controlados; nunca se consulta o cofre real. A fonte textual fica indisponível
no enriquecimento posterior para não reparar e esconder a perda na seleção.

### Saída completa na base 90dec8e

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 /workspace/Checkpoint/.venv/bin/python -X faulthandler -m pytest tests/test_drive_search_flow.py -q -p no:cacheprovider
```

Executado na cópia da base, exit 1:

```text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_______________ test_drive_search_saves_metadata_and_link[False] _______________

app = <PySide6.QtWidgets.QApplication(0x131c1730) at 0x7ff3d71de040>
library = <checkpoint.library.Library object at 0x7ff3d7222120>
folder = PosixPath('/tmp/d2e214e3a81948bfa81eca6511563667')
save_during_search = False

    @pytest.mark.parametrize('save_during_search', [False, True])
    def test_drive_search_saves_metadata_and_link(app, library, folder, save_during_search):
        window, game, file_id, source = save_via_drive(app, library, folder / 'drive-source',
                                                     save_during_search=save_during_search)
        try:
            assert game['developer'] == EMERALD['developer']
            assert game['description'] == EMERALD['description']
            assert game['publisher'] == EMERALD['publisher']
            assert game['release_date'] == EMERALD['release_date']
>           assert game['source'] == 'Busca'
E           AssertionError: assert 'Google Drive' == 'Busca'
E
E             - Busca
E             + Google Drive

tests/test_drive_search_flow.py:18: AssertionError
_______________ test_drive_search_saves_metadata_and_link[True] ________________

app = <PySide6.QtWidgets.QApplication(0x131c1730) at 0x7ff3d71de040>
library = <checkpoint.library.Library object at 0x7ff3dcfa0b30>
folder = PosixPath('/tmp/34553a6fb1824e3694a4a43e1b86b0bf')
save_during_search = True

    @pytest.mark.parametrize('save_during_search', [False, True])
    def test_drive_search_saves_metadata_and_link(app, library, folder, save_during_search):
        window, game, file_id, source = save_via_drive(app, library, folder / 'drive-source',
                                                     save_during_search=save_during_search)
        try:
>           assert game['developer'] == EMERALD['developer']
E           AssertionError: assert '' == 'Game Freak'
E
E             - Game Freak

tests/test_drive_search_flow.py:14: AssertionError
_ test_drive_without_metadata_explains_and_offers_manual_search[sem-resultado] _

app = <PySide6.QtWidgets.QApplication(0x131c1730) at 0x7ff3d71de040>
library = <checkpoint.library.Library object at 0x7ff3d6ddac90>
folder = PosixPath('/tmp/65f3473aa0b74ca0ab55edb315d1c700'), failure = False

    @pytest.mark.parametrize('failure', [False, True], ids=['sem-resultado', 'fonte-indisponivel'])
    def test_drive_without_metadata_explains_and_offers_manual_search(app, library, folder, failure):
        window, game, file_id, _ = save_via_drive(app, library, folder / 'missing-source',
                                                 no_results=not failure, search_failure=failure)
        try:
            assert not game['developer'] and not game['description'] and not game['publisher']
            assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?', (file_id,)).fetchone()[0] == game['id']
>           assert any(label.isVisible() and label.text() == 'Não encontramos dados para este jogo. Pesquise manualmente.'
                       for label in window.detail_page.findChildren(QLabel))
E                      assert False
E                       +  where False = any(<generator object test_drive_without_metadata_explains_and_offers_manual_search.<locals>.<genexpr> at 0x7ff3d6c2a8e0>)

tests/test_drive_search_flow.py:41: AssertionError
_ test_drive_without_metadata_explains_and_offers_manual_search[fonte-indisponivel] _

app = <PySide6.QtWidgets.QApplication(0x131c1730) at 0x7ff3d71de040>
library = <checkpoint.library.Library object at 0x7ff3dd199af0>
folder = PosixPath('/tmp/f687060476384c77a90d54e16b24ddf8'), failure = True

    @pytest.mark.parametrize('failure', [False, True], ids=['sem-resultado', 'fonte-indisponivel'])
    def test_drive_without_metadata_explains_and_offers_manual_search(app, library, folder, failure):
        window, game, file_id, _ = save_via_drive(app, library, folder / 'missing-source',
                                                 no_results=not failure, search_failure=failure)
        try:
            assert not game['developer'] and not game['description'] and not game['publisher']
            assert library.sql.execute('SELECT game_id FROM game_files WHERE id=?', (file_id,)).fetchone()[0] == game['id']
>           assert any(label.isVisible() and label.text() == 'Não encontramos dados para este jogo. Pesquise manualmente.'
                       for label in window.detail_page.findChildren(QLabel))
E                      assert False
E                       +  where False = any(<generator object test_drive_without_metadata_explains_and_offers_manual_search.<locals>.<genexpr> at 0x7ff3d458c380>)

tests/test_drive_search_flow.py:41: AssertionError
=========================== short test summary info ============================
FAILED tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[False]
FAILED tests/test_drive_search_flow.py::test_drive_search_saves_metadata_and_link[True]
FAILED tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[sem-resultado]
FAILED tests/test_drive_search_flow.py::test_drive_without_metadata_explains_and_offers_manual_search[fonte-indisponivel]
4 failed in 6.45s
```

### Saída após correção na fix/0.1.30

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests/test_drive_search_flow.py -q -p no:cacheprovider
```

Exit 0:

```text
....                                                                     [100%]
4 passed in 6.50s
```

Uma tentativa intermediária ainda falhou em salvar durante a consulta (1 falha,
3 passaram, 20,61 s). A aplicação foi ajustada também para aguardar os detalhes;
o teste e seu suporte não foram alterados para obter aprovação.

## Diff completo da correção do app

```diff
diff --git a/checkpoint/detail_view.py b/checkpoint/detail_view.py
index 5150dc0..f60e6c4 100644
--- a/checkpoint/detail_view.py
+++ b/checkpoint/detail_view.py
@@ -44,6 +44,10 @@ def build_detail(window,game):
     notice=getattr(window,'detail_notice',None)
     if notice and notice[0]==game_id:
         banner=text(notice[1]);banner.setObjectName('wishNotice');banner.setAccessibleName(notice[1]);banner.setStyleSheet('padding: 10px; border: 1px solid '+window.theme.colors['accent']+'; border-radius: 7px;');layout.addWidget(banner)
+    if any(file['drive_id'] for file in files) and not all(game[field] for field in ('description','developer','publisher')):
+        warning=text('Não encontramos dados para este jogo. Pesquise manualmente.')
+        warning.setObjectName('metadataNotice');layout.addWidget(warning)
+        layout.addWidget(action('Pesquisar manualmente',lambda:window.search_game_data(game_id)),0,Qt.AlignLeft)
     tabs=CurrentPageTabs();tabs.setObjectName('detailTabs');window.detail_tabs=tabs
     layouts=[]
     for name in ('Visão geral','Atividade','Memórias','Arquivos'):
diff --git a/checkpoint/dialogs.py b/checkpoint/dialogs.py
index a414739..a844e08 100644
--- a/checkpoint/dialogs.py
+++ b/checkpoint/dialogs.py
@@ -153,7 +153,7 @@ class GameDialog(QDialog):
             else:widget.clear()
         self.fields['title'].setText(normalize_rom_name(file['original_name']))
         self.fields['platform'].setText(file['platform'] or rom_identity(file['original_name'])[1])
-        self.fields['source'].setText('Google Drive')
+        self.fields['source'].setText('Não identificada')
         if file['game_id']:
             existing=self.library.get(file['game_id'])
             if existing:
@@ -179,7 +179,8 @@ class GameDialog(QDialog):
     def apply_catalog(self,result):
         if hasattr(self,'quick_add'):self.quick_add.suspend=True
         self.catalog_result=result
-        if self.drive_file_id is None:self.fields['source'].setText('Busca')
+        if self.drive_file_id is None or any((result.description,result.developer,result.publisher)):
+            self.fields['source'].setText('Busca')
         values={'title':result.title,'description':result.description,'genre':', '.join(result.genres),'developer':result.developer,'publisher':result.publisher,'release_date':result.release_date}
         for key,value in values.items():
             if value:
@@ -209,6 +210,9 @@ class GameDialog(QDialog):
         return result

     def validate(self):
+        quick=getattr(self,'quick_add',None)
+        if quick and self.drive_file_id is not None and self.catalog_result is None and quick.jobs and not quick.metadata_unavailable:
+            self.error.setText('Aguarde a pesquisa da ficha antes de adicionar.');return
         if hasattr(self,'quick_add') and self.catalog_result is None and self.drive_file_id is None:
             self.error.setText('Selecione um jogo ou uma ROM antes de adicionar.');return
         if not self.fields['title'].text().strip():
diff --git a/checkpoint/enrichment.py b/checkpoint/enrichment.py
index 67b4694..bd911ae 100644
--- a/checkpoint/enrichment.py
+++ b/checkpoint/enrichment.py
@@ -53,6 +53,7 @@ def complete_game(library, game_id, steam_provider=None, rawg_provider=None, cac
                 art_provider=SteamGridDbProvider(CredentialVault().get('steamgriddb'))
             sources.append(('steamgriddb',art_provider))
         except Exception:pass
+    drive_rom=library.sql.execute('SELECT 1 FROM game_files WHERE game_id=? AND drive_id IS NOT NULL',(game_id,)).fetchone() is not None
     fields_saved = images_saved = failures = 0
     for source, provider in sources:
         try:
@@ -80,6 +81,7 @@ def complete_game(library, game_id, steam_provider=None, rawg_provider=None, cac
                       'release_date': result.release_date}
             # Identidade e campo são conferidos no UPDATE para preservar edições concorrentes.
             with library.sql:
+                saved_text=0
                 for field, value in values.items():
                     if value:
                         cursor = library.sql.execute(
@@ -88,8 +90,12 @@ def complete_game(library, game_id, steam_provider=None, rawg_provider=None, cac
                             "WHERE game_id=games.id AND provider=? AND external_id=?)",
                             (value, now(), game_id, expected_description if field=='description' else '', source, result.external_id))
                         fields_saved += cursor.rowcount
+                        if field in ('description','developer','publisher'):saved_text+=cursor.rowcount
+                if saved_text and source in ('rawg','steam'):
+                    library.sql.execute("UPDATE games SET source='Busca' WHERE id=? AND source IN ('','Manual','Google Drive','Não identificada')",(game_id,))
                 record(library,game_id,result)
-            for kind, url in result.images.items():
+            # O arquivo/pasta do Drive não é fonte de arte; ROMs usam SteamGridDB.
+            for kind, url in (result.images.items() if not drive_rom or source=='steamgriddb' else []):
                 if kind not in ('cover', 'banner', 'logo'):
                     continue
                 current = library.get(game_id)
diff --git a/checkpoint/game_import.py b/checkpoint/game_import.py
index 1aeb851..ea60b96 100644
--- a/checkpoint/game_import.py
+++ b/checkpoint/game_import.py
@@ -32,6 +32,8 @@ def complete_identity(library,game_id,result):
         for field,value in values.items():
             if value:library.sql.execute(f"UPDATE games SET {field}=?,updated_at=? WHERE id=? AND {field}='' AND deleted_at IS NULL",(value,now(),game_id))

+        if any((result.description,result.developer,result.publisher)):
+            library.sql.execute("UPDATE games SET source='Busca' WHERE id=? AND source IN ('','Manual','Google Drive','Não identificada')",(game_id,))
         from .description_provenance import record
         record(library,game_id,result)

@@ -42,7 +44,7 @@ def save_import(library,data,file_id=None,result=None):
         values={'description':result.description,'developer':result.developer,'publisher':result.publisher,'genre':', '.join(result.genres),'release_date':result.release_date}
         for field,value in values.items():
             if value and not clean.get(field):clean[field]=value
-        if clean.get('source') in (None,'','Manual'):clean['source']='Busca'
+        if any((result.description,result.developer,result.publisher)) and clean.get('source') in (None,'','Manual','Google Drive','Não identificada'):clean['source']='Busca'
     file=library.sql.execute('SELECT * FROM game_files WHERE id=?',(file_id,)).fetchone() if file_id is not None else None
     if file_id is not None and file is None: raise ValueError('A ROM selecionada não está mais no índice.')
     existing=None
@@ -76,6 +78,8 @@ def save_import(library,data,file_id=None,result=None):
                 values={key:value for key,value in values.items() if value and not library.get(game_id)[key]}
                 if values:library.sql.execute(f'UPDATE games SET {",".join(key+"=?" for key in values)},updated_at=? WHERE id=?',[*values.values(),now(),game_id])
         if result:
+            if any((result.description,result.developer,result.publisher)):
+                library.sql.execute("UPDATE games SET source='Busca' WHERE id=? AND source IN ('','Manual','Google Drive','Não identificada')",(game_id,))
             from .description_provenance import record
             record(library,game_id,result)
         if file:
diff --git a/checkpoint/quick_add.py b/checkpoint/quick_add.py
index d356fc1..10ca20c 100644
--- a/checkpoint/quick_add.py
+++ b/checkpoint/quick_add.py
@@ -16,7 +16,7 @@ class QuickAdd(QObject):
     def __init__(self,dialog,outer,allow_steam):
         super().__init__(dialog);self.dialog=dialog;self.library=dialog.library
         self.generation=0;self.jobs=[];self.finishing=False;self.suspend=False;self.closed=False;self.pending_show_lookup=False;self.pending_search=False;self.pending_details=None
-        self.candidates=[];self.local=[];self.owner=dialog
+        self.candidates=[];self.local=[];self.drive_catalog=False;self.metadata_unavailable=False;self.owner=dialog
         while self.owner.parentWidget() is not None:self.owner=self.owner.parentWidget()
         while outer.count():
             item=outer.takeAt(0)
@@ -56,6 +56,7 @@ class QuickAdd(QObject):
         status=QHBoxLayout();status.addWidget(self.busy);status.addWidget(self.state,1);outer.addLayout(status)
         self.steam_panel=dialog.steam_panel;self.steam_panel.setParent(dialog);outer.addWidget(self.steam_panel);self.steam_panel.hide()
         self.drive_manage=action('Atualizar índice do Drive',self.manage_drive);self.drive_manage.setObjectName('quiet');outer.addWidget(self.drive_manage,0,Qt.AlignLeft);self.drive_manage.hide()
+        self.manual=action('Pesquisar manualmente',self.manual_search);self.manual.hide();outer.addWidget(self.manual,0,Qt.AlignLeft)
         advanced=QWidget();advanced_row=QVBoxLayout(advanced);advanced_row.setContentsMargins(0,0,0,0);advanced_row.setSpacing(10)
         self.platform=QComboBox();self.platform.setMinimumSize(220,40);self.platform.setSizeAdjustPolicy(QComboBox.AdjustToContents);self.platform.addItem('Todas as plataformas','')
         for name in sorted({row['platform'] for row in self.library.sql.execute('SELECT DISTINCT platform FROM game_files') if row['platform']}|{'PC','Nintendo Switch','Nintendo DS','Game Boy Advance','Super Nintendo','PlayStation','PlayStation 2'}):self.platform.addItem(name,name)
@@ -90,7 +91,7 @@ class QuickAdd(QObject):
     @Slot(int)
     def source_changed(self,index):
         self.timer.stop();self.generation+=1;self.pending_search=False;self.pending_details=None
-        self.dialog.drive_file_id=None;self.dialog.catalog_result=None
+        self.dialog.drive_file_id=None;self.dialog.catalog_result=None;self.drive_catalog=False;self.metadata_unavailable=False;self.manual.hide()
         self.query.setVisible(index!=2);self.preview.setVisible(index==0);self.results.setVisible(index==1)
         self.steam_panel.setVisible(index==2);self.drive_manage.setVisible(index==1)
         self.advanced.setVisible(index!=2);self.automation.setVisible(index!=2);self.save.setVisible(index!=2);self.save.setEnabled(False);self.other.hide();self.confirmed.hide()
@@ -117,14 +118,19 @@ class QuickAdd(QObject):
     def changed(self,value):
         if self.suspend:return
         self.dialog.error.clear();self.save.setEnabled(False)
-        self.generation+=1;self.dialog.catalog_result=None;self.dialog.drive_file_id=None
+        self.generation+=1;self.dialog.catalog_result=None
+        preserve_rom=self.drive_catalog and self.dialog.drive_file_id is not None and self.sources.currentIndex()==1
+        if not preserve_rom:self.dialog.drive_file_id=None
+        self.metadata_unavailable=False;self.manual.hide()
         for key in ('description','genre','developer','publisher','release_date','cover','banner','logo','executable'):
             self.dialog.fields[key].clear()
-        self.dialog.fields['source'].setText('Manual');self.dialog.fields['platform'].setText(self.platform.currentData() or '')
+        self.dialog.fields['source'].setText('Não identificada' if preserve_rom else 'Manual')
+        if not preserve_rom:self.dialog.fields['platform'].setText(self.platform.currentData() or '')
         self.title.setText(value.strip() or 'Nenhum jogo selecionado');self.art.clear();self.art.setText('Prévia');self.facts.clear()
-        self.association.clear();self.association.hide();self.description.clear();self.results.clear();self.candidates=[];self.confirmed.hide();self.other.hide();self.preview.hide()
+        if not preserve_rom:self.association.clear();self.association.hide()
+        self.description.clear();self.results.clear();self.candidates=[];self.confirmed.hide();self.other.hide();self.preview.hide()
         self.local_results()
-        if len(value.strip())>=2 and self.sources.currentIndex()==0:self.state.setText('Buscando…');self.timer.start()
+        if len(value.strip())>=2 and (self.sources.currentIndex()==0 or preserve_rom):self.state.setText('Buscando…');self.timer.start()
         elif self.sources.currentIndex()==1:
             self.save.setEnabled(False);self.results.show()
             self.state.setText(count_text(len(self.local),'ROM','ROMs') if self.local else 'Nenhuma ROM encontrada')
@@ -142,7 +148,7 @@ class QuickAdd(QObject):
         rows=self.library.sql.execute('SELECT * FROM game_files WHERE drive_id IS NOT NULL ORDER BY original_name')
         self.local=[dict(row) for row in rows if query and query in normalized(normalize_rom_name(row['original_name'])) and (not platform or platform==row['platform'])][:40]
         self.results.blockSignals(True);self.results.clear()
-        if self.sources.currentIndex()==0:self.local=[]
+        if self.sources.currentIndex()==0 or self.dialog.drive_file_id is not None:self.local=[]
         for row in self.local:
             item=QListWidgetItem(row['original_name']+'\nDisponível no Drive · '+(row['platform'] or 'Plataforma não definida'))
             item.setSizeHint(QSize(0,60));item.setToolTip(row['original_name']);self.results.addItem(item)
@@ -157,6 +163,7 @@ class QuickAdd(QObject):
         if not self.dialog.isVisible():self.pending_show_lookup=True;return
         if any(job.property('operation')=='catalog_search' for job in self.jobs):self.pending_search=True;return
         self.pending_search=False;self.preview.hide();self.results.hide();self.state.setText('Buscando…')
+        if self.dialog.drive_file_id is not None:self.save.setEnabled(False)
         self.run('catalog_search',title=self.query.text().strip(),platform=self.dialog.fields['platform'].text())

     def run(self,operation,**arguments):
@@ -182,9 +189,9 @@ class QuickAdd(QObject):
             self.state.setText('' if self.candidates or self.local else 'Nenhum resultado')
             if not self.candidates and not self.local:
                 if self.dialog.drive_file_id is not None:
-                    self.preview.show();self.save.setEnabled(True);self.state.setText('ROM selecionada. Ficha indisponível; você pode adicionar e ajustar depois.')
+                    self.show_missing_metadata()
                 else:self.preview.hide();self.results.hide();self.facts.clear();self.save.setEnabled(False)
-            if payload.get('unavailable'):self.state.setText(self.state.text()+' Parte dos catálogos está indisponível.')
+            if payload.get('unavailable') and not self.metadata_unavailable:self.state.setText(self.state.text()+' Parte dos catálogos está indisponível.')
             # Nunca seleciona uma ROM automaticamente. Uma ficha inequívoca pode ser sugerida.
             match=best_match(self.query.text(),self.dialog.fields['platform'].text(),self.candidates)
             if self.dialog.drive_file_id is not None and match and normalized(match.title)!=normalized(self.query.text()):match=None
@@ -196,10 +203,14 @@ class QuickAdd(QObject):
             path=payload.get('preview',{}).get('cover')
             if path:self.art.setPixmap(QPixmap(path).scaled(self.art.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
             self.state.clear()
+            if self.dialog.drive_file_id is not None and not all((result.description,result.developer,result.publisher)):
+                self.show_missing_metadata()

     @Slot(str)
     def failed(self,message):
-        if not self.closed and self.sender().property('generation')==self.generation:self.state.setText('Consulta indisponível')
+        if not self.closed and self.sender().property('generation')==self.generation:
+            if self.dialog.drive_file_id is not None:self.show_missing_metadata()
+            else:self.state.setText('Consulta indisponível')

     @Slot()
     def job_finished(self):
@@ -222,9 +233,11 @@ class QuickAdd(QObject):
         self.dialog.apply_catalog(result)
         if not self.dialog.fields['platform'].text() and result.platforms:self.dialog.fields['platform'].setText('PC' if 'PC' in result.platforms else result.platforms[0])
         self.show_result(result);self.state.setText('Carregando ficha…')
+        if self.dialog.drive_file_id is not None:self.save.setEnabled(False)
         self.run('catalog_details',provider=result.provider,identity=result.external_id,platform=self.dialog.fields['platform'].text())

     def show_result(self,result):
+        self.metadata_unavailable=False;self.manual.hide()
         self.save.setEnabled(not self.finishing);self.preview.show();self.results.hide();self.other.setVisible(bool(self.candidates));self.confirmed.show()
         self.title.setText(result.title)
         details=[self.dialog.fields['platform'].text() or ' / '.join(result.platforms[:3]),result.developer,result.release_date[:4]]
@@ -233,7 +246,18 @@ class QuickAdd(QObject):
     def drive_loaded(self,file):
         self.art.clear();self.art.setText('Prévia')
         self.generation+=1;self.title.setText(self.query.text());self.facts.setText(file['platform'] or 'Plataforma não definida');self.description.clear()
-        self.save.setEnabled(True);self.association.setText('ROM selecionada · '+file['original_name']);self.association.show();self.preview.show();self.results.hide();self.state.setText('ROM selecionada. Buscando a ficha para esta plataforma…');self.lookup()
+        self.drive_catalog=True;self.metadata_unavailable=False;self.manual.hide();self.save.setEnabled(False)
+        self.association.setText('ROM selecionada · '+file['original_name']);self.association.show();self.preview.show();self.results.hide();self.state.setText('ROM selecionada. Buscando a ficha para esta plataforma…');self.lookup()
+
+    def show_missing_metadata(self):
+        self.metadata_unavailable=True;self.preview.show();self.save.setEnabled(not self.finishing)
+        self.state.setText('Não encontramos dados para este jogo. Pesquise manualmente.')
+        self.manual.show()
+
+    def manual_search(self):
+        # Pesquisar novamente não remove nem troca o vínculo da ROM selecionada.
+        self.drive_catalog=True;self.query.setPlaceholderText('Pesquisar dados do jogo…')
+        self.query.setFocus();self.query.selectAll();self.lookup()

     def use_name(self):
         self.timer.stop();self.generation+=1;self.state.clear();self.dialog.validate()
diff --git a/checkpoint/window.py b/checkpoint/window.py
index b4df9bd..2dbe15e 100644
--- a/checkpoint/window.py
+++ b/checkpoint/window.py
@@ -280,10 +280,16 @@ class MainWindow(QMainWindow):
             row = self.table.currentRow(); item = self.table.item(row,0) if row>=0 else None
         if item: self.detail(item.data(Qt.UserRole))

-    def add_game(self):
+    def search_game_data(self,game_id):
+        file=self.library.sql.execute('SELECT * FROM game_files WHERE game_id=? AND drive_id IS NOT NULL ORDER BY id LIMIT 1',(game_id,)).fetchone()
+        if file:self.add_game(drive_file=dict(file))
+
+    def add_game(self,drive_file=None):
         wish=self.current_page==2
         owned_before={game['id'] for game in self.library.owned_games()}
         dialog = GameDialog(self,library=self.library,purpose='wish' if wish else 'library')
+        if drive_file is not None:
+            dialog.source_tabs.setCurrentIndex(1);dialog.load_drive_file(drive_file)
         result=dialog.exec()
         if dialog.steam_requested:
             QTimer.singleShot(0,self.steam);return
@@ -301,7 +307,9 @@ class MainWindow(QMainWindow):
                 self.detail_notice=(game_id,message) if wish else None
                 self.refresh_library();self.detail(game_id)
                 self.statusBar().showMessage(message)
-                if dialog.complete_on_save.isChecked():
+                if dialog.drive_file_id is not None and dialog.catalog_result is None:
+                    self.statusBar().showMessage('Não encontramos dados para este jogo. Pesquise manualmente.')
+                elif dialog.complete_on_save.isChecked():
                     self.completion_queue.submit([game_id])
             self.guard(save)

```

## Suíte completa

Comando no código final da correção, incluindo a versão 0.1.30:

```bash
QT_QPA_PLATFORM=offscreen CHECKPOINT_TEST_ROOT=/tmp PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

Saída completa, exit 0:

```text
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
..............                                                           [100%]
302 passed in 500.23s (0:08:20)
```

302 passaram, 0 falhas e 0 erros, em 500,23 s. A base tinha 296 testes;
os quatro casos de fluxo Drive e dois de política/recuperação somam seis novos.
Nenhum skip/xfail foi acrescentado, nenhuma asserção foi removida e a suíte
inclui o teste original de lifecycle. A queda nativa parcial não se reproduziu
nessa execução completa, sem atribuir a ela uma causa/correção não demonstrada.

## Rodadas relacionadas e queda nativa observada

Comando parcial: pytest tests/test_quick_add.py tests/test_game_import.py
tests/test_add_from_search_flow.py tests/test_enrichment.py tests/test_save_lifecycle.py
-q -p no:cacheprovider, no mesmo ambiente offscreen/isolado, com -X faulthandler.

Uma rodada na branch terminou com SIGSEGV no GC do pytest após executar os 40 casos;
ela NÃO foi contabilizada como teste aprovado. A mesma seleção na base passou
(40 em 29,65 s); a repetição na branch passou (40 em 28,15 s). Isso não demonstra
uma correção da queda nativa isolada; não se introduziu workaround, skip, xfail,
sleep de encerramento nem remoção de asserção para escondê-la. Nenhum arquivo de
test_save_lifecycle foi alterado. Registro completo da rodada que caiu:

```text
........................................                                 [100%]Fatal Python error: Segmentation fault

Current thread 0x00007fb78b8a8740 (most recent call first):
  Garbage-collecting
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/unraisableexception.py", line 29 in gc_collect_harder
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/unraisableexception.py", line 168 in pytest_unconfigure
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 1377 in _ensure_unconfigure
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/main.py", line 375 in wrap_session
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/main.py", line 380 in pytest_cmdline_main
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_execution.py", line 147 in _multicall
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_manager.py", line 183 in _hookexec
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pluggy/_caller.py", line 197 in __call__
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 262 in _main
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/_pytest/config/__init__.py", line 286 in _console_main
  File "/workspace/Checkpoint/.venv/lib/python3.12/site-packages/pytest/__main__.py", line 9 in <module>
  File "<frozen runpy>", line 88 in _run_code
  File "<frozen runpy>", line 198 in _run_module_as_main

Extension modules: shiboken6.Shiboken, PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets, PySide6.QtTest (total: 5)
```

Os dois testes adicionais de política/recuperação manual passaram em 3,56 s.
A suíte integral inclui todos os casos, sem exclusão do lifecycle.

## Não validado e limites

Python 3.12 / PySide6 6.8.3, Qt offscreen no Linux, pastas isoladas em /tmp.
Não foram validados Windows real, DPI, contas/fornecedores reais, cofre Windows
ou downloads reais de ROM. Os PNGs usados como fontes são locais e explícitos;
não se apresentam testes com provedores controlados como integração autenticada.
Nenhuma dependência foi instalada. Não foram geradas capturas de revisão novas.
A ocorrência nativa isolada no GC permanece registrada como limitação de estabilidade,
sem alegação de causa resolvida. Dados antigos, releases e schema foram preservados.

# Checkpoint pós-0.1.39 — comandos e saídas integrais

Registros atuais desta rodada. Tentativas com erro/interrupção são preservadas e não contam como aprovação.
Qt offscreen/Linux e fixtures isoladas não homologam Windows do dono. Este arquivo registra o gate Linux. Validação Windows/pacote executada posteriormente e aprovada: 808 testes; RELATORIO_WINDOWS_POS_0139.md. Nenhuma nova publicação.
Os blocos abaixo contêm stdout/stderr completos dos arquivos de evidência, sem o corte usado nas prévias do chat.

| Registro | Exit | Duração (s) |
|---|---:|---:|
| targeted | 0 | 24.729 |
| memory-layout-final | 0 | 2.572 |
| full-linux | -15 | 326.485 |
| carousel-visible-before | 0 | 1.215 |
| visual-contrast-before | 1 | 0.409 |
| final-targeted | 0 | 25.232 |
| full-linux-final | 0 | 558.383 |
| offer-details-before | 1 | 0.814 |
| offer-details-after | 0 | 7.193 |
| offer-details-ui | 0 | 5.196 |
| offer-details-final | 0 | 16.585 |
| offer-identity-final | 0 | 11.867 |
| prices-complete | 0 | 17.886 |
| prices-approved-final | 0 | 18.364 |
| full-with-prices | 0 | 549.499 |
| smoke-final | 0 | 0.946 |

## targeted

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_post_0139_layout.py",
    "tests/test_post_0139_themes.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "tests/test_themes.py",
    "tests/test_time_prices_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795143602.4026537,
  "exit_code": 0,
  "elapsed": 24.728832483291626
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_post_0139_layout.py tests/test_post_0139_themes.py tests/test_home_data_0137.py tests/test_home_layout_0137.py tests/test_home_polish_0139.py tests/test_polish_0139.py tests/test_themes.py tests/test_time_prices_0134.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 f097a06dd2f4d82f5d35934297ac1b272c9c4c83c92de7a03e166531fc82abed:

````text
........................................................................ [ 76%]
......................                                                   [100%]
94 passed in 24.38s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## memory-layout-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_post_0139_layout.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795143718.963256,
  "exit_code": 0,
  "elapsed": 2.5717318058013916
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_post_0139_layout.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 42079c95febf6f0f6a0c04562fa71cbb805a5eb2f165d799e820fac67971844d:

````text
..................                                                       [100%]
18 passed in 2.26s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-linux

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795143767.193706,
  "exit_code": -15,
  "elapsed": 326.4853484630585
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 789 bytes; SHA-256 1fbac486ec8972468b339f4a9febf7e720cc671f0a2fba43de5c81b56e63a6ce:

````text
........................................................................ [  9%]
........................................................................ [ 18%]
........................................................................ [ 27%]
........................................................................ [ 36%]
........................................................................ [ 45%]
........................................................................ [ 54%]
........................................................................ [ 64%]
........................................................................ [ 73%]
........................................................................ [ 82%]
...........................................................FF.....F..
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## carousel-visible-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_post_0139_layout.py::test_memory_cards_stay_visible_and_separate_after_resizing",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144094.690692,
  "exit_code": 0,
  "elapsed": 1.2151236534118652
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_post_0139_layout.py::test_memory_cards_stay_visible_and_separate_after_resizing -q -p no:cacheprovider
```

stdout integral — 98 bytes; SHA-256 b834d154d8fc19fda76f00fad8fc11f1864ec2cdb75b2d532f7ca2baa05191a8:

````text
..                                                                       [100%]
2 passed in 0.97s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## visual-contrast-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144120.9568894,
  "exit_code": 1,
  "elapsed": 0.4086019992828369
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast -q -p no:cacheprovider
```

stdout integral — 3171 bytes; SHA-256 9d2f3d6ab1544f9ecc25d729bc7e0e5678ae4d07916b865480ced1bf2821b9c7:

````text
.FF.....F                                                                [100%]
=================================== FAILURES ===================================
_____________ test_semantic_tokens_and_normal_text_contrast[green] _____________

key = 'green'

    @pytest.mark.parametrize('key',list(THEMES))
    def test_semantic_tokens_and_normal_text_contrast(key):
        colors=THEMES[key].colors
        for token in ('background','surface','elevated','card','border_subtle','text','secondary','muted','accent','success','alert'):
            assert token in colors
        for foreground in ('text','secondary','muted'):
            for surface in ('background','surface','elevated','card','selected'):
>               assert contrast(colors[foreground],colors[surface])>=4.5,(key,foreground,surface)
E               AssertionError: ('green', 'muted', 'selected')
E               assert 4.205280598799117 >= 4.5
E                +  where 4.205280598799117 = contrast('#a4b4c6', '#3b4f37')

tests/test_visual_0132.py:14: AssertionError
____________ test_semantic_tokens_and_normal_text_contrast[yellow] _____________

key = 'yellow'

    @pytest.mark.parametrize('key',list(THEMES))
    def test_semantic_tokens_and_normal_text_contrast(key):
        colors=THEMES[key].colors
        for token in ('background','surface','elevated','card','border_subtle','text','secondary','muted','accent','success','alert'):
            assert token in colors
        for foreground in ('text','secondary','muted'):
            for surface in ('background','surface','elevated','card','selected'):
>               assert contrast(colors[foreground],colors[surface])>=4.5,(key,foreground,surface)
E               AssertionError: ('yellow', 'muted', 'selected')
E               assert 4.318484836878344 >= 4.5
E                +  where 4.318484836878344 = contrast('#a4b4c6', '#4d4837')

tests/test_visual_0132.py:14: AssertionError
_____________ test_semantic_tokens_and_normal_text_contrast[cyan] ______________

key = 'cyan'

    @pytest.mark.parametrize('key',list(THEMES))
    def test_semantic_tokens_and_normal_text_contrast(key):
        colors=THEMES[key].colors
        for token in ('background','surface','elevated','card','border_subtle','text','secondary','muted','accent','success','alert'):
            assert token in colors
        for foreground in ('text','secondary','muted'):
            for surface in ('background','surface','elevated','card','selected'):
>               assert contrast(colors[foreground],colors[surface])>=4.5,(key,foreground,surface)
E               AssertionError: ('cyan', 'muted', 'selected')
E               assert 4.218089252827984 >= 4.5
E                +  where 4.218089252827984 = contrast('#a4b4c6', '#334e52')

tests/test_visual_0132.py:14: AssertionError
=========================== short test summary info ============================
FAILED tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[green]
FAILED tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[yellow]
FAILED tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast[cyan]
3 failed, 6 passed in 0.17s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## final-targeted

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_post_0139_layout.py",
    "tests/test_post_0139_themes.py",
    "tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast",
    "tests/test_home_layout_0137.py",
    "tests/test_home_polish_0139.py",
    "tests/test_polish_0139.py",
    "tests/test_themes.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144146.9844663,
  "exit_code": 0,
  "elapsed": 25.231687307357788
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_post_0139_layout.py tests/test_post_0139_themes.py tests/test_visual_0132.py::test_semantic_tokens_and_normal_text_contrast tests/test_home_layout_0137.py tests/test_home_polish_0139.py tests/test_polish_0139.py tests/test_themes.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 e309eb4d2190267fd4dbbb17ebeaee33dc8ee7bc1fe88a8225704c6f4205af5b:

````text
........................................................................ [ 78%]
....................                                                     [100%]
92 passed in 24.75s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-linux-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144240.1628454,
  "exit_code": 0,
  "elapsed": 558.3833186626434
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 912 bytes; SHA-256 595282b71062282a4268ecd064d07edcad4619ee6472550bddc786860d4aa56c:

````text
........................................................................ [  9%]
........................................................................ [ 18%]
........................................................................ [ 27%]
........................................................................ [ 36%]
........................................................................ [ 45%]
........................................................................ [ 54%]
........................................................................ [ 63%]
........................................................................ [ 73%]
........................................................................ [ 82%]
........................................................................ [ 91%]
.....................................................................    [100%]
789 passed in 556.71s (0:09:16)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## offer-details-before

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144813.1648335,
  "exit_code": 1,
  "elapsed": 0.8143863677978516
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py -q -p no:cacheprovider
```

stdout integral — 12662 bytes; SHA-256 540c29d7ed9b4d425e726cac03b185c9fc52b3c0a38c8b386609c2319b9baaf8:

````text
FFFFFFFFF.FF                                                             [100%]
=================================== FAILURES ===================================
_ test_optional_details_confirm_same_offer_without_changing_api_history[Portal 2] _

library = <checkpoint.library.Library object at 0x7f95f377b440>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f377b4d0>
title = 'Portal 2'

    @pytest.mark.parametrize('title',['Portal 2','Hades'])
    def test_optional_details_confirm_same_offer_without_changing_api_history(library,monkeypatch,title):
        identity,api,public,calls,errors=configured(library,monkeypatch,title)
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert value['lowest']==6000 and value['discount']==40 and value['original']==10000
E       assert (6000 == 6000 and None == 40)

tests/test_offer_details_pos_0139.py:42: AssertionError
_ test_optional_details_confirm_same_offer_without_changing_api_history[Hades] _

library = <checkpoint.library.Library object at 0x7f95f32324b0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f3231490>
title = 'Hades'

    @pytest.mark.parametrize('title',['Portal 2','Hades'])
    def test_optional_details_confirm_same_offer_without_changing_api_history(library,monkeypatch,title):
        identity,api,public,calls,errors=configured(library,monkeypatch,title)
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert value['lowest']==6000 and value['discount']==40 and value['original']==10000
E       assert (6000 == 6000 and None == 40)

tests/test_offer_details_pos_0139.py:42: AssertionError
_______ test_public_mismatch_or_failure_never_invents_discount[edition] ________

library = <checkpoint.library.Library object at 0x7f95f32325a0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f3232630>
case = 'edition'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
_______ test_public_mismatch_or_failure_never_invents_discount[currency] _______

library = <checkpoint.library.Library object at 0x7f95f3232060>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f32335f0>
case = 'currency'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
________ test_public_mismatch_or_failure_never_invents_discount[price] _________

library = <checkpoint.library.Library object at 0x7f95f32328a0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f329cda0>
case = 'price'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
_______ test_public_mismatch_or_failure_never_invents_discount[original] _______

library = <checkpoint.library.Library object at 0x7f95f329d010>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f329ce30>
case = 'original'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
________ test_public_mismatch_or_failure_never_invents_discount[store] _________

library = <checkpoint.library.Library object at 0x7f95f329ccb0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f329d370>
case = 'store'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
_________ test_public_mismatch_or_failure_never_invents_discount[link] _________

library = <checkpoint.library.Library object at 0x7f95f329d6a0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f329e060>
case = 'link'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
_____ test_public_mismatch_or_failure_never_invents_discount[unavailable] ______

library = <checkpoint.library.Library object at 0x7f95f329cbc0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f95f329ecc0>
case = 'unavailable'

    @pytest.mark.parametrize('case',['edition','currency','price','original','store','link','unavailable'])
    def test_public_mismatch_or_failure_never_invents_discount(library,monkeypatch,case):
        identity,api,public,calls,errors=configured(library,monkeypatch,'Portal 2')
        if case=='edition':public['url']='https://gg.deals/br/game/other-edition/'
        elif case=='currency':public['currency']='USD'
        elif case=='price':public['retail']=5900
        elif case=='original':public['offers'][0]['original']=6000
        elif case=='store':public['offers'][0]['kind']='keyshop'
        elif case=='link':public['offers'][0]['url']='https://other.example/redirect/'
        else:errors['public']=True
        refresh_prices(library,identity)
        value=selected_quote(library,identity)
>       assert len(calls)==1
E       assert 0 == 1
E        +  where 0 = len([])

tests/test_offer_details_pos_0139.py:63: AssertionError
_ test_details_option_is_explicit_and_rechecks_without_discarding_cache[sample0] _

ui = (<checkpoint.window.MainWindow(0x2bafdce0) at 0x7f95f32f9540>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6fd2b0) at 0x7f95f328a240>

    def test_details_option_is_explicit_and_rechecks_without_discarding_cache(ui,app):
        window,identity=ui;window.navigate(5)
        control=window.pages[5].findChild(QCheckBox,'ggdealsOfferDetails')
>       assert control is not None and not control.isChecked()
E       assert (None is not None)

tests/test_offer_details_pos_0139.py:82: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
_ test_details_option_is_explicit_and_rechecks_without_discarding_cache[sample1] _

ui = (<checkpoint.window.MainWindow(0x2bc88740) at 0x7f95f32f93c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x2b6fd2b0) at 0x7f95f328a240>

    def test_details_option_is_explicit_and_rechecks_without_discarding_cache(ui,app):
        window,identity=ui;window.navigate(5)
        control=window.pages[5].findChild(QCheckBox,'ggdealsOfferDetails')
>       assert control is not None and not control.isChecked()
E       assert (None is not None)

tests/test_offer_details_pos_0139.py:82: AssertionError
=========================== short test summary info ============================
FAILED tests/test_offer_details_pos_0139.py::test_optional_details_confirm_same_offer_without_changing_api_history[Portal 2]
FAILED tests/test_offer_details_pos_0139.py::test_optional_details_confirm_same_offer_without_changing_api_history[Hades]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[edition]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[currency]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[price]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[original]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[store]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[link]
FAILED tests/test_offer_details_pos_0139.py::test_public_mismatch_or_failure_never_invents_discount[unavailable]
FAILED tests/test_offer_details_pos_0139.py::test_details_option_is_explicit_and_rechecks_without_discarding_cache[sample0]
FAILED tests/test_offer_details_pos_0139.py::test_details_option_is_explicit_and_rechecks_without_discarding_cache[sample1]
11 failed, 1 passed in 0.56s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## offer-details-after

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_api.py",
    "tests/test_ggdeals_connection.py",
    "tests/test_price_integrity_0136.py",
    "tests/test_price_display_official.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144843.7431722,
  "exit_code": 0,
  "elapsed": 7.192703008651733
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_api.py tests/test_ggdeals_connection.py tests/test_price_integrity_0136.py tests/test_price_display_official.py tests/test_home_data_0137.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 5003be43f3db5a709f1d432ee3828f0db49b197ecc2ef4ac5570f975bc9140af:

````text
.....................................................................    [100%]
69 passed in 6.84s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## offer-details-ui

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_connection.py",
    "tests/test_price_integrity_0136.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795144933.0855074,
  "exit_code": 0,
  "elapsed": 5.195675373077393
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_connection.py tests/test_price_integrity_0136.py -q -p no:cacheprovider
```

stdout integral — 99 bytes; SHA-256 f585c28ad62a6f97b4ac3d3f52ed60b450ba707725d4b80b9566714356eb2e17:

````text
............................                                             [100%]
28 passed in 4.84s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## offer-details-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_api.py",
    "tests/test_ggdeals_connection.py",
    "tests/test_prices_0129.py",
    "tests/test_price_integrity_0136.py",
    "tests/test_price_display_official.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795145183.9130359,
  "exit_code": 0,
  "elapsed": 16.585113525390625
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_api.py tests/test_ggdeals_connection.py tests/test_prices_0129.py tests/test_price_integrity_0136.py tests/test_price_display_official.py tests/test_home_data_0137.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 02b604a98685d53ed4043b11dec241f82f8124cb3ce10aef1d70ede3a1b65a88:

````text
........................................................................ [ 93%]
.....                                                                    [100%]
77 passed in 16.19s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## offer-identity-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_api.py",
    "tests/test_prices_0129.py",
    "tests/test_price_integrity_0136.py",
    "tests/test_price_display_official.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795145329.0689898,
  "exit_code": 0,
  "elapsed": 11.867133617401123
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_api.py tests/test_prices_0129.py tests/test_price_integrity_0136.py tests/test_price_display_official.py tests/test_home_data_0137.py tests/test_home_layout_0137.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 346cdf58d55097b52a0cd8cc38b07470ebf645d84473b63ad870a3a77e929c80:

````text
........................................................................ [ 96%]
...                                                                      [100%]
75 passed in 11.48s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## prices-complete

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_api.py",
    "tests/test_ggdeals_connection.py",
    "tests/test_prices_0129.py",
    "tests/test_price_integrity_0136.py",
    "tests/test_price_display_official.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "tests/test_time_prices_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795145374.9616635,
  "exit_code": 0,
  "elapsed": 17.88570809364319
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_api.py tests/test_ggdeals_connection.py tests/test_prices_0129.py tests/test_price_integrity_0136.py tests/test_price_display_official.py tests/test_home_data_0137.py tests/test_home_layout_0137.py tests/test_time_prices_0134.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 a16339675a1fa2daaeae12a7c703a3e6b4776dad76f9683de9ef084b1ce92dc6:

````text
........................................................................ [ 87%]
..........                                                               [100%]
82 passed in 17.46s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## prices-approved-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "pytest",
    "tests/test_offer_details_pos_0139.py",
    "tests/test_ggdeals_api.py",
    "tests/test_ggdeals_connection.py",
    "tests/test_prices_0129.py",
    "tests/test_price_integrity_0136.py",
    "tests/test_price_display_official.py",
    "tests/test_home_data_0137.py",
    "tests/test_home_layout_0137.py",
    "tests/test_time_prices_0134.py",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795145524.1404042,
  "exit_code": 0,
  "elapsed": 18.36379361152649
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m pytest tests/test_offer_details_pos_0139.py tests/test_ggdeals_api.py tests/test_ggdeals_connection.py tests/test_prices_0129.py tests/test_price_integrity_0136.py tests/test_price_display_official.py tests/test_home_data_0137.py tests/test_home_layout_0137.py tests/test_time_prices_0134.py -q -p no:cacheprovider
```

stdout integral — 180 bytes; SHA-256 2891476baeab7d4c75099c12c511de9798ea3a9e6c7f51356d8ac6374dd63dc7:

````text
........................................................................ [ 86%]
...........                                                              [100%]
83 passed in 17.99s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## full-with-prices

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-X",
    "faulthandler",
    "-m",
    "pytest",
    "tests",
    "-q",
    "-p",
    "no:cacheprovider"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795145667.55057,
  "exit_code": 0,
  "elapsed": 549.4990062713623
}
```

Comando:

```sh
/workspace/work/venv/bin/python -X faulthandler -m pytest tests -q -p no:cacheprovider
```

stdout integral — 992 bytes; SHA-256 64d45cf08fc5cd116d72b12045f8a90e65586c70ec5953ee0c3ca5c0b4c675ad:

````text
........................................................................ [  8%]
........................................................................ [ 17%]
........................................................................ [ 26%]
........................................................................ [ 35%]
........................................................................ [ 44%]
........................................................................ [ 53%]
........................................................................ [ 62%]
........................................................................ [ 71%]
........................................................................ [ 80%]
........................................................................ [ 89%]
........................................................................ [ 98%]
................                                                         [100%]
808 passed in 547.90s (0:09:07)
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

## smoke-final

```json
{
  "command": [
    "/workspace/work/venv/bin/python",
    "-m",
    "checkpoint.app",
    "--smoke-test",
    "--data-dir",
    "/workspace/work/evidence-pos-0139/smoke-final-data"
  ],
  "cwd": "/workspace/work/Checkpoint",
  "environment": {
    "QT_QPA_PLATFORM": "offscreen",
    "CHECKPOINT_TEST_ROOT": "/tmp",
    "PYTHONDONTWRITEBYTECODE": "1"
  },
  "platform": "Linux-6.18.57-x86_64-with-glibc2.41",
  "started": 1795182140.990984,
  "exit_code": 0,
  "elapsed": 0.9458372592926025
}
```

Comando:

```sh
/workspace/work/venv/bin/python -m checkpoint.app --smoke-test --data-dir /workspace/work/evidence-pos-0139/smoke-final-data
```

stdout integral — 50 bytes; SHA-256 21079070cb6b0ffbec368584ab7b5ce39d68facddbbe2c030e21bb38c87e71c5:

````text
Checkpoint smoke: 6 pages OK; SQLite integrity=ok
````

stderr integral — 48 bytes; SHA-256 e0a46db3e7d086b6ed55477f9c8cc5ec4dbe4b6ef804e1372e9a4a6dc5a6b01a:

````text
Fontconfig error: No writable cache directories
````

## Reprodução inicial e registros auxiliares

Saídas preservadas antes do coletor de metadados. Horários e comandos exatos
não foram registrados nestes arquivos; não são reconstruídos. As falhas de
fixture e a base anterior não contam como gate do código final.

### layout-base

stdout integral — 6277 bytes; SHA-256 283c1028a21c7b801c4e3f01285701021657774c58b64ed4a367eb700027d80d:

````text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
____ test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample0] _____

ui = (<checkpoint.window.MainWindow(0x394e9f30) at 0x7f6bb47ee480>, 1)
app = <PySide6.QtWidgets.QApplication(0x392363f0) at 0x7f6bb4914c00>

    def test_home_shows_each_game_once_and_keeps_sessions_and_totals(ui, app):
        window, first=ui
        second=window.library.save_game({'title':'Outro jogo','platform':'PC'})
        now=datetime.now(timezone.utc)
        with window.library.sql:
            for n, identity in enumerate((first,first,second,first,second)):
                window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid,duration_seconds) VALUES(?,?,'finished',?,600)",(identity,(now-timedelta(hours=n+1)).isoformat(),100+n))
        before=[tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]
        window.navigate(0);settle(app)
        strip=window.pages[0].findChild(GameStrip)
>       assert [g['id'] for g in strip.games]==[first,second]
E       assert [1, 1, 2, 1, 2] == [1, 2]
E         
E         At index 1 diff: 1 != 2
E         Left contains 3 more items, first extra item: 2
E         Use -v to get more diff

tests/test_post_0139_layout.py:24: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample1] _____

ui = (<checkpoint.window.MainWindow(0x3922f0a0) at 0x7f6bb47e1800>, 1)
app = <PySide6.QtWidgets.QApplication(0x392363f0) at 0x7f6bb4914c00>

    def test_home_shows_each_game_once_and_keeps_sessions_and_totals(ui, app):
        window, first=ui
        second=window.library.save_game({'title':'Outro jogo','platform':'PC'})
        now=datetime.now(timezone.utc)
        with window.library.sql:
            for n, identity in enumerate((first,first,second,first,second)):
                window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid,duration_seconds) VALUES(?,?,'finished',?,600)",(identity,(now-timedelta(hours=n+1)).isoformat(),100+n))
        before=[tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]
        window.navigate(0);settle(app)
        strip=window.pages[0].findChild(GameStrip)
>       assert [g['id'] for g in strip.games]==[first,second]
E       assert [1, 1, 2, 1, 2] == [1, 2]
E         
E         At index 1 diff: 1 != 2
E         Left contains 3 more items, first extra item: 2
E         Use -v to get more diff

tests/test_post_0139_layout.py:24: AssertionError
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0] ___

ui = (<checkpoint.window.MainWindow(0x397439b0) at 0x7f6bba6323c0>, 1)
app = <PySide6.QtWidgets.QApplication(0x392363f0) at 0x7f6bb4914c00>
folder = PosixPath('/tmp/d3f1b752565a417089ee03aa94cf46a1')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
        for n in range(2):
            copy=folder/f'captura-{n}.png';assert image.save(str(copy))
            window.library.add_media(identity,copy,'Imagem de teste')
        for size in ((1280,800),(1920,1080)):
            window.resize(*size);window.navigate(0);settle(app)
            carousel=window.pages[0].findChild(MemoryCarousel)
            frames=carousel.findChildren(QWidget,'homeMemoryCard')
>           assert len(frames)==2 and all(f.width()<=300 for f in frames)
E           assert (2 == 2 and False)
E            +  where 2 = len([<checkpoint.design_system.CardSurface(0x3988a1b0, name="homeMemoryCard") at 0x7f6bb425bc40>, <checkpoint.design_system.CardSurface(0x39ca8f50, name="homeMemoryCard") at 0x7f6bb425bbc0>])
E            +  and   False = all(<generator object test_memories_keep_standard_width_and_no_synthetic_dark_padding.<locals>.<genexpr> at 0x7f6bb4296740>)

tests/test_post_0139_layout.py:41: AssertionError
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1] ___

ui = (<checkpoint.window.MainWindow(0x39c4d020) at 0x7f6bb45efc40>, 1)
app = <PySide6.QtWidgets.QApplication(0x392363f0) at 0x7f6bb4914c00>
folder = PosixPath('/tmp/454ad32b084e417ebb22640598235f93')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
        for n in range(2):
            copy=folder/f'captura-{n}.png';assert image.save(str(copy))
            window.library.add_media(identity,copy,'Imagem de teste')
        for size in ((1280,800),(1920,1080)):
            window.resize(*size);window.navigate(0);settle(app)
            carousel=window.pages[0].findChild(MemoryCarousel)
            frames=carousel.findChildren(QWidget,'homeMemoryCard')
>           assert len(frames)==2 and all(f.width()<=300 for f in frames)
E           assert (2 == 2 and False)
E            +  where 2 = len([<checkpoint.design_system.CardSurface(0x39880880, name="homeMemoryCard") at 0x7f6bb42e2900>, <checkpoint.design_system.CardSurface(0x39dc9a50, name="homeMemoryCard") at 0x7f6bb42e0480>])
E            +  and   False = all(<generator object test_memories_keep_standard_width_and_no_synthetic_dark_padding.<locals>.<genexpr> at 0x7f6bb433c2b0>)

tests/test_post_0139_layout.py:41: AssertionError
=========================== short test summary info ============================
FAILED tests/test_post_0139_layout.py::test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample0]
FAILED tests/test_post_0139_layout.py::test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample1]
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0]
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1]
4 failed in 0.67s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

### checkpoint-pos-before

stdout integral — 6675 bytes; SHA-256 7d99c77a8bae6275f36b5f72572c6b2f0bb774ae1e410f902fe8029e8340c0c8:

````text
FFFF                                                                     [100%]
=================================== FAILURES ===================================
____ test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample0] _____

ui = (<checkpoint.window.MainWindow(0x281af5a0) at 0x7ff2c9cfbfc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x280f6f90) at 0x7ff2c9c6ae80>

    def test_home_shows_each_game_once_and_keeps_sessions_and_totals(ui, app):
        window, first=ui
        second=window.library.save_game({'title':'Outro jogo','platform':'PC'})
        now=datetime.now(timezone.utc)
        with window.library.sql:
            for n, identity in enumerate((first,first,second,first,second)):
                window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid,duration_seconds) VALUES(?,?,'finished',?,600)",(identity,(now-timedelta(hours=n+1)).isoformat(),100+n))
        before=[tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]
        window.navigate(0);settle(app)
        strip=window.pages[0].findChild(GameStrip)
>       assert [g['id'] for g in strip.games]==[first,second]
E       assert [1, 1, 2, 1, 2] == [1, 2]
E         
E         At index 1 diff: 1 != 2
E         Left contains 3 more items, first extra item: 2
E         Use -v to get more diff

tests/test_post_0139_layout.py:24: AssertionError
---------------------------- Captured stderr setup -----------------------------
Fontconfig error: No writable cache directories
____ test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample1] _____

ui = (<checkpoint.window.MainWindow(0x28322820) at 0x7ff2c9cdaf80>, 1)
app = <PySide6.QtWidgets.QApplication(0x280f6f90) at 0x7ff2c9c6ae80>

    def test_home_shows_each_game_once_and_keeps_sessions_and_totals(ui, app):
        window, first=ui
        second=window.library.save_game({'title':'Outro jogo','platform':'PC'})
        now=datetime.now(timezone.utc)
        with window.library.sql:
            for n, identity in enumerate((first,first,second,first,second)):
                window.library.sql.execute("INSERT INTO play_sessions(game_id,started_at,state,pid,duration_seconds) VALUES(?,?,'finished',?,600)",(identity,(now-timedelta(hours=n+1)).isoformat(),100+n))
        before=[tuple(r) for r in window.library.sql.execute('SELECT * FROM play_sessions')]
        window.navigate(0);settle(app)
        strip=window.pages[0].findChild(GameStrip)
>       assert [g['id'] for g in strip.games]==[first,second]
E       assert [1, 1, 2, 1, 2] == [1, 2]
E         
E         At index 1 diff: 1 != 2
E         Left contains 3 more items, first extra item: 2
E         Use -v to get more diff

tests/test_post_0139_layout.py:24: AssertionError
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0] ___

ui = (<checkpoint.window.MainWindow(0x28878f30) at 0x7ff2c83d8fc0>, 1)
app = <PySide6.QtWidgets.QApplication(0x280f6f90) at 0x7ff2c9c6ae80>
folder = PosixPath('/tmp/f14c157ae2d04191b3452d53d59feb84')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
>       for _ in range(2):window.library.add_media(identity,path,'Imagem de teste')
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_post_0139_layout.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <checkpoint.library.Library object at 0x7ff2c9c769f0>, game_id = 1
path = PosixPath('/tmp/f14c157ae2d04191b3452d53d59feb84/captura.png')
caption = 'Imagem de teste'

    def add_media(self, game_id, path, caption=''):
        path = Path(path).resolve(strict=True)
        extension = path.suffix.lower()
        if extension not in {'.png','.jpg','.jpeg','.webp','.mp4','.mkv','.avi','.mov'}:
            raise ValueError('Formato de mídia não suportado.')
        with self.sql:
>           self.sql.execute('INSERT INTO media_files(game_id,path,caption,created_at,kind) VALUES(?,?,?,?,?)',
                             (game_id,str(path),caption,now(),'image' if extension in {'.png','.jpg','.jpeg','.webp'} else 'video'))
E           sqlite3.IntegrityError: UNIQUE constraint failed: media_files.path

checkpoint/library.py:121: IntegrityError
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1] ___

ui = (<checkpoint.window.MainWindow(0x288aca00) at 0x7ff2c9873d00>, 1)
app = <PySide6.QtWidgets.QApplication(0x280f6f90) at 0x7ff2c9c6ae80>
folder = PosixPath('/tmp/c48d4654559d4608b2a4e9177059b47e')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
>       for _ in range(2):window.library.add_media(identity,path,'Imagem de teste')
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_post_0139_layout.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <checkpoint.library.Library object at 0x7ff2cfaf85c0>, game_id = 1
path = PosixPath('/tmp/c48d4654559d4608b2a4e9177059b47e/captura.png')
caption = 'Imagem de teste'

    def add_media(self, game_id, path, caption=''):
        path = Path(path).resolve(strict=True)
        extension = path.suffix.lower()
        if extension not in {'.png','.jpg','.jpeg','.webp','.mp4','.mkv','.avi','.mov'}:
            raise ValueError('Formato de mídia não suportado.')
        with self.sql:
>           self.sql.execute('INSERT INTO media_files(game_id,path,caption,created_at,kind) VALUES(?,?,?,?,?)',
                             (game_id,str(path),caption,now(),'image' if extension in {'.png','.jpg','.jpeg','.webp'} else 'video'))
E           sqlite3.IntegrityError: UNIQUE constraint failed: media_files.path

checkpoint/library.py:121: IntegrityError
=========================== short test summary info ============================
FAILED tests/test_post_0139_layout.py::test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample0]
FAILED tests/test_post_0139_layout.py::test_home_shows_each_game_once_and_keeps_sessions_and_totals[sample1]
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0]
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1]
4 failed in 0.80s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

### checkpoint-pos-after

stdout integral — 6409 bytes; SHA-256 f2eee4c4f3269ba1263a49ae04c2b91912f18b978c90bef3818bdc7845d0485c:

````text
..FF....FF.......................................                        [100%]
=================================== FAILURES ===================================
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0] ___

ui = (<checkpoint.window.MainWindow(0x7d64e50) at 0x7f599d0bf240>, 1)
app = <PySide6.QtWidgets.QApplication(0x7a9b140) at 0x7f59972b14c0>
folder = PosixPath('/tmp/b46800b4f4ce4c93b0fdeeafae0bbd2c')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
>       for _ in range(2):window.library.add_media(identity,path,'Imagem de teste')
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_post_0139_layout.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <checkpoint.library.Library object at 0x7f599d2187a0>, game_id = 1
path = PosixPath('/tmp/b46800b4f4ce4c93b0fdeeafae0bbd2c/captura.png')
caption = 'Imagem de teste'

    def add_media(self, game_id, path, caption=''):
        path = Path(path).resolve(strict=True)
        extension = path.suffix.lower()
        if extension not in {'.png','.jpg','.jpeg','.webp','.mp4','.mkv','.avi','.mov'}:
            raise ValueError('Formato de mídia não suportado.')
        with self.sql:
>           self.sql.execute('INSERT INTO media_files(game_id,path,caption,created_at,kind) VALUES(?,?,?,?,?)',
                             (game_id,str(path),caption,now(),'image' if extension in {'.png','.jpg','.jpeg','.webp'} else 'video'))
E           sqlite3.IntegrityError: UNIQUE constraint failed: media_files.path

checkpoint/library.py:121: IntegrityError
___ test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1] ___

ui = (<checkpoint.window.MainWindow(0x7d434c0) at 0x7f5996c71ac0>, 1)
app = <PySide6.QtWidgets.QApplication(0x7a9b140) at 0x7f59972b14c0>
folder = PosixPath('/tmp/2d65dbc85973422a82ac290ea58a98b4')

    def test_memories_keep_standard_width_and_no_synthetic_dark_padding(ui, app, folder):
        window, identity=ui
        path=folder/'captura.png'
        image=QImage(300,200,QImage.Format_RGB32);image.fill(QColor('#eac040'));assert image.save(str(path))
>       for _ in range(2):window.library.add_media(identity,path,'Imagem de teste')
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_post_0139_layout.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <checkpoint.library.Library object at 0x7f5996ea5eb0>, game_id = 1
path = PosixPath('/tmp/2d65dbc85973422a82ac290ea58a98b4/captura.png')
caption = 'Imagem de teste'

    def add_media(self, game_id, path, caption=''):
        path = Path(path).resolve(strict=True)
        extension = path.suffix.lower()
        if extension not in {'.png','.jpg','.jpeg','.webp','.mp4','.mkv','.avi','.mov'}:
            raise ValueError('Formato de mídia não suportado.')
        with self.sql:
>           self.sql.execute('INSERT INTO media_files(game_id,path,caption,created_at,kind) VALUES(?,?,?,?,?)',
                             (game_id,str(path),caption,now(),'image' if extension in {'.png','.jpg','.jpeg','.webp'} else 'video'))
E           sqlite3.IntegrityError: UNIQUE constraint failed: media_files.path

checkpoint/library.py:121: IntegrityError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0] _____

ui = (<checkpoint.window.MainWindow(0x7d56cb0) at 0x7f5996c38440>, 1)
app = <PySide6.QtWidgets.QApplication(0x7a9b140) at 0x7f59972b14c0>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
        before = [tile.session_id for tile in strip.tiles]
>       assert strip.next.isEnabled() and not strip.previous.isEnabled()
E       assert (False)
E        +  where False = <built-in method isEnabled of IconButton object at 0x7f5996c39540>()
E        +    where <built-in method isEnabled of IconButton object at 0x7f5996c39540> = <checkpoint.design_system.IconButton(0x80bae20, name="iconButton") at 0x7f5996c39540>.isEnabled
E        +      where <checkpoint.design_system.IconButton(0x80bae20, name="iconButton") at 0x7f5996c39540> = <checkpoint.home_components.GameStrip(0x7fb5b20, name="recentGames") at 0x7f5996c3af80>.next

tests/test_home_polish_0139.py:71: AssertionError
____ test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1] _____

ui = (<checkpoint.window.MainWindow(0x804b5e0) at 0x7f5996e9bb80>, 1)
app = <PySide6.QtWidgets.QApplication(0x7a9b140) at 0x7f59972b14c0>

    def test_session_carousel_mouse_and_keyboard_show_other_sessions(ui, app):
        w, identity = ui
        sessions(w, identity)
        w.resize(1280, 800)
        w.navigate(0)
        settle(app)
        strip = w.pages[0].findChild(GameStrip)
        before = [tile.session_id for tile in strip.tiles]
>       assert strip.next.isEnabled() and not strip.previous.isEnabled()
E       assert (False)
E        +  where False = <built-in method isEnabled of IconButton object at 0x7f59947d1540>()
E        +    where <built-in method isEnabled of IconButton object at 0x7f59947d1540> = <checkpoint.design_system.IconButton(0x7e49c40, name="iconButton") at 0x7f59947d1540>.isEnabled
E        +      where <checkpoint.design_system.IconButton(0x7e49c40, name="iconButton") at 0x7f59947d1540> = <checkpoint.home_components.GameStrip(0x7e49820, name="recentGames") at 0x7f5996bb3c40>.next

tests/test_home_polish_0139.py:71: AssertionError
=========================== short test summary info ============================
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample0]
FAILED tests/test_post_0139_layout.py::test_memories_keep_standard_width_and_no_synthetic_dark_padding[sample1]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample0]
FAILED tests/test_home_polish_0139.py::test_session_carousel_mouse_and_keyboard_show_other_sessions[sample1]
4 failed, 45 passed in 4.68s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

### checkpoint-pos-after2

stdout integral — 99 bytes; SHA-256 ac4b4f06894b989e36a35554f2cc8bfeda73fe0e18a199bffbc768ba91a32d26:

````text
.................................................                        [100%]
49 passed in 4.87s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

### checkpoint-pos-themes

stdout integral — 100 bytes; SHA-256 d7dbdefa8953fa8464007e589107ba29818bfdb9364cc1c92a80ed2f1691c2db:

````text
..................................                                       [100%]
34 passed in 18.45s
````

stderr integral — 0 bytes; SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:

````text

````

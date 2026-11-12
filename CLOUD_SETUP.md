# Desenvolvimento independente deste computador

O desenvolvimento 0.1.15 está na branch `codex/steam-library-import` de
`pedroalexcarneiro/Checkpoint`, ainda não incorporado à `main`. Use o checkout
existente ou essa branch ao retomar esta implementação; não use somente o ZIP de
uma release anterior. Confira `pyproject.toml` (0.1.15)
e a presença de `AGENTS.md`, `CONTINUITY.md` e `gamevault/game_import.py`.

O ambiente Linux foi preparado e validado nesta nuvem. Na 0.1.14, 29 testes focados
de Steam, migrações, biblioteca e UI passaram com exit 0; smoke atualizado abriu
seis páginas com SQLite íntegro. A falha nativa de encerramento Qt foi corrigida
posteriormente, com 16 testes afetados e uma execução completa: 136 aprovados,
exit 0, sem crash após o relatório. O smoke das seis páginas foi reconfirmado.
API Steam autenticada e Windows permanecem pendentes. Consulte TESTING.md para
validar por impacto e evitar repetir suítes de áreas intactas sem necessidade.
Use venv com `--copies` no Linux: os testes de launcher comparam caminhos resolvidos.

## Preparar um ambiente Linux Codex Cloud

Escolha Cloud, conecte o repositório privado e prepare Python 3.12. Em uma imagem
Debian/Ubuntu com permissão para instalar pacotes, as dependências Qt típicas são:

```sh
sudo apt-get update
sudo apt-get install -y libegl1 libopengl0 libgl1 libglib2.0-0 libxkbcommon0 libdbus-1-3 libfontconfig1 fonts-dejavu-core
python3.12 -m venv --copies .venv
.venv/bin/python -m pip install -e . pytest
QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest tests -q -p no:cacheprovider
QT_QPA_PLATFORM=offscreen .venv/bin/python -m gamevault.app --smoke-test --data-dir .cloud-smoke
```

Os comandos Linux são instruções de preparação, não uma afirmação de execução neste
host Windows. Ajuste nomes de pacotes conforme a imagem e registre o relatório real.
Não instale `requirements-tested.txt` indiscriminadamente no Linux: é um inventário
do ambiente Windows, incluindo dependências específicas desse sistema.

Os testes não exigem a conta pessoal, ROMs ou chaves reais. O cofre de credenciais usa
Windows Credential Manager; autenticação real pelo app e build do executável precisam
de Windows. Não contorne essa diferença salvando tokens em arquivos versionados.

## Abrir e continuar na nuvem

1. No Codex web/desktop, escolha `Work in > Cloud` e crie/selecione um ambiente.
2. Selecione `pedroalexcarneiro/Checkpoint`; a conexão GitHub precisa ter acesso a ele.
3. Peça para ler `AGENTS.md`, `CONTINUITY.md`, `PRODUCT_VISION.md` e validar a suíte.
4. Revise o relatório e publique o ambiente reutilizável. Continue no mesmo chat Cloud
   pelo web/mobile/desktop com a mesma conta e espaço de trabalho.
5. Mantenha alterações em commits/PRs do repositório e atualize a continuidade.

Referência oficial: https://learn.chatgpt.com/docs/environments/cloud-environments .
As opções podem variar pela conta; conexão GitHub e autenticação podem exigir ação do usuário.
Chat local não vira automaticamente um chat Cloud e o transcript integral não é importado.

## O que permanece separado

O aplicativo Windows, a biblioteca SQLite do usuário, artes pessoais, ROMs, saves,
diretórios locais e credenciais do cofre não são enviados ao GitHub. Migrar desenvolvimento
não significa sincronizar a biblioteca pessoal nem liberar acesso público ao repositório.
Os testes Windows 10/11 e a distribuição continuam no fluxo descrito em SETUP.md.

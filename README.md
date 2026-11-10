# Checkpoint

Biblioteca pessoal de jogos para Windows, desenvolvida do zero em Python 3.12, PySide6 e SQLite. Versão **0.1.4 de desenvolvimento**, com dados locais e interface em português. Não é ainda a implementação completa da visão do produto.

Já oferece biblioteca manual persistente, galeria 3:4 e lista, pesquisa e filtros, favoritos, edição, lixeira recuperável, páginas de jogos, diário, mídia referenciada, conquistas pessoais, estatísticas de sessões confirmadas, metas de compra e backup/restauração local de saves explicitamente selecionados.

Há fluxos de integração implementados para pesquisa RAWG, seleção de artes SteamGridDB e ROMs no Google Drive. Eles exigem credenciais próprias e **não foram validados com contas reais**. O scanner não baixa ROMs; downloads acontecem apenas por solicitação. Nenhuma função remove arquivos no Drive.

## Executar

No ambiente de desenvolvimento, instale o projeto conforme SETUP.md e execute:

```powershell
python -m gamevault.app
```

O pacote portátil, quando gerado, fica em `dist/Checkpoint/Checkpoint.exe`. A pasta inteira `dist/Checkpoint` é necessária; não mova apenas o executável. Dados ficam em `%LOCALAPPDATA%/GameVault`, separados do programa. Para testar sem tocar na biblioteca principal:

```powershell
python -m gamevault.app --data-dir ./dados-isolados
```

## Documentação

- [Estado e limitações](PROJECT_STATUS.md)
- [Instalação e build](SETUP.md)
- [Arquitetura](ARCHITECTURE.md)
- [Plano de evolução](ROADMAP.md)
- [Integrações e credenciais](INTEGRATIONS.md)
- [Testes](TESTING.md)
- [Alterações](CHANGELOG.md)

O primeiro início é vazio. Dados de testes ficam em diretórios isolados e não são incluídos na biblioteca distribuída. Vídeos abrem no reprodutor padrão do Windows; imagens possuem visualização ampliada no aplicativo.

![Início vazio do GameVault](preview.png)

## Atualização 0.1.4 — Checkpoint

Nome visível e executável alterados para Checkpoint. Removidos slogans da navegação, do início e dos estados vazios. Os dados, a trava de instância e o cofre continuam usando os identificadores internos GameVault para abrir a biblioteca existente sem migração. O pacote Python e a pasta de fontes também permanecem com seus nomes internos. O usuário confirmou que os fluxos locais solicitados no teste anterior funcionaram; isso não valida integrações autenticadas.

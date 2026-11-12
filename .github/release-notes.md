Cadastro simples e proteção durante downloads/imagens.

- Para adicionar um jogo, digite o nome e salve. O Checkpoint tenta buscar ficha e imagens automaticamente nas fontes disponíveis, sem exigir confirmação de catálogo. Sem correspondência confiável, o cadastro é salvo mesmo assim.
- Nome e plataforma aparecem primeiro; Drive e ficha avançada ficam recolhidos. A edição manual continua disponível para corrigir imagens ou identificação.
- No Drive, **Baixar e adicionar à biblioteca** cria o cadastro/vínculo e inicia a busca das imagens após verificar o arquivo.
- Downloads e imagens executam em auxiliares separados. Se um auxiliar encerrar abruptamente, a interface permanece aberta e informa a falha. Downloads válidos e parciais são preservados.
- Preferências de automação, campos pessoais e artes existentes são respeitados. Não há novos escopos OAuth nem chaves exigidas por jogo. SQLite permanece no schema 4.

Baixe **Checkpoint-0.1.16-windows-x64.zip**, extraia a pasta completa e abra Checkpoint.exe. Preserve `_internal` e `CheckpointUpdater`.

A queda Windows relatada durante ROM/capa não foi reproduzida no Linux. A contenção foi testada com processos interrompidos deliberadamente; isso não comprova a causa exata do incidente. Consulte o arquivo de validação para os testes Windows e smoke do executável/auxiliar desta compilação. Downloads Drive autenticados e acesso real às imagens não são comprovados pelos testes com transporte controlado.

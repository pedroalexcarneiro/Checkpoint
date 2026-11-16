# Checkpoint 0.1.38 — correção de abertura

- Corrige uma falha na criação da janela do Windows: o tratamento de mensagens podia pedir ao Qt que criasse novamente a janela antes de terminar a criação original.
- Usa o identificador da janela entregue pelo Windows e mantém os controles integrados.
- Acrescenta validação da abertura normal do fonte e do executável extraído, com janela nativa visível/responsiva, captura, fechamento e integridade do banco.
- Mantém schema 4, biblioteca, sessões, arquivos, perfis e cofre; a correção funcional não altera os serviços de dados.

Validação: 700 testes Windows e 700 Linux aprovados; build, smokes, abertura normal do fonte/executável extraído, captura, fechamento e SQLite aprovados. ZIP conferido por checksum e CRC. Os testes de abertura normal são executados em Windows já elevado; não automatizam consentimento UAC nem homologam contas/emuladores/jogos no PC do dono. As limitações anteriores de fontes de preço, A4 e fechar somente a ROM permanecem.

A versão 0.1.37 e seus arquivos publicados são preservados. Resultados e evidências em RELATORIO_0138.md.

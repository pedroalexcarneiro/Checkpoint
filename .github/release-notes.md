Checkpoint 0.1.27 — revisão de interface, Desejos, Steam e perfil local.

- Logos dos Desejos ocupam a área de apresentação dentro do card, preservando proporção e transparência.
- Logos faltantes de identidades confirmadas entram na fila automática ao abrir Desejos; a tela atualiza quando a imagem chega, sem precisar sair e voltar. Consultas limitadas a uma tentativa por jogo na sessão e respeitando a preferência de automação.
- Adicionar jogo fica no canto superior direito somente em Início e Biblioteca. A duplicata da lateral foi removida. Adicionar desejo é separado dentro da lista.
- Removidas frases instrutivas/promocionais de estados vazios, painéis e diálogos.
- Importação Steam tem lista com rolagem, janela limitada e resultado compacto. O relatório por jogo que expandia o diálogo foi removido.
- A regressão de importação usa 300 jogos e verifica rolagem, tamanho da janela e resumo sem log por jogo.
- Perfil local em janela própria: escolher/remover foto e alterar apelido. O nick e a foto aparecem na lateral, sem login nem campos de conta.

- Início e ficha com banner de altura limitada, logo legível e imagem sem deformação ou corte; feed e atividade em colunas equilibradas.
- Biblioteca com dimensões limitadas, quatro colunas na janela de 1000 px, legendas junto à arte e foco alinhado à imagem. Originais preservados.
- Adicionar jogo sempre direcionado à Biblioteca.
- Busca do Início abre os resultados da Biblioteca ao digitar.
- Estados vazios compactos, sem instruções redundantes; memórias sem limite que corte o texto.
- Estatísticas com cards adaptativos e calendário dimensionado à largura disponível.
- Nove temas disponíveis, com Verde como padrão; preferências persistentes.
- Área principal com largura máxima para evitar expansão desproporcional em telas grandes. Cadastro, editor, conexões e demais diálogos mantêm seus fluxos existentes.

Baixe **Checkpoint-0.1.27-windows-x64.zip**, extraia a pasta completa e abra **Checkpoint.exe**. Mantenha `_internal` e `CheckpointUpdater`.

O ZIP de revisão visual contém capturas reais Qt geradas no Windows: seis páginas, ficha, cadastro, editor, integrações, estados vazios, formatos diferentes, telas de 1000/1100/1920 px e quatro temas. Jogos e sessões são fixtures isoladas, sem acesso à biblioteca pessoal ou contas autenticadas.

Consulte **Checkpoint-0.1.27-validation.txt** para os testes Windows e os smokes do fonte, executável extraído, SQLite, auxiliar e atualizador. Avaliação visual e validação de integrações autenticadas são distintas desses testes.

Banco/schema 4, notas, histórico, credenciais, imagens e arquivos pessoais preservados. Tags e releases anteriores não foram alteradas.

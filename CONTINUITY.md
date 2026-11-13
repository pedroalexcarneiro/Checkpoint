# Continuidade do Checkpoint

Trabalho atual: versão 0.1.29, branch `fix/0.1.29`, iniciada no commit `8d39c18` da base solicitada. Não usar a main defasada nem alterar as branches codex existentes.

Leia PROJECT_STATUS.md, RELATORIO_CORRECOES.md e ARCHITECTURE.md. Referências visuais e decisões do dono prevalecem: wordmark checkpo//nt e ícone próprio; Biblioteca vertical com tamanho ajustável e seis colunas no padrão largo; Desejos com arte 1:1; Início de andamento; ficha com galeria; Conexões 2×2. São nove temas, Verde padrão.

Não volte a permitir que um GameDialog conclua enquanto seus jobs de busca estão ativos, inclusive sob DriveDialog. Ao salvar durante a consulta de detalhes selecionados, aguarde a resposta no loop Qt e preserve desenvolvedora, editora e descrição. Não use skip/xfail para quedas nativas.

Valide com QT_QPA_PLATFORM=offscreen, CHECKPOINT_TEST_ROOT em /tmp e --data-dir novo nos smokes. O schema permanece 4; a migração copia e preserva a origem. Nunca consultar cofre real em testes.

Não criar tags nem publicar releases nesta tarefa. A pré-release v0.1.28 publicada por engano deve ser removida pelo dono; não alterá-la. A API oficial GG.deals aguarda documentação e chave própria no cofre. Não implementar endpoints por suposição. Não fundir os componentes de cadastro sem decisão posterior do dono.

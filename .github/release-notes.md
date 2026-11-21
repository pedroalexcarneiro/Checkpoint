# Checkpoint 0.1.40 · Estabilidade e interface

- Memórias abre e navega com carregamento progressivo. A grade mantém as fotos inteiras, com espaço até a barra de rolagem. Os filtros mostram apenas jogos com memórias.
- Últimas sessões e Memórias recentes deslizam lateralmente no Início. O destaque usa a arte do último jogo iniciado e as ofertas mostram capas verticais.
- Tamanho das capas usa a cor do tema ativo na seleção. O diálogo Adicionar jogo abre em formato vertical, com prévia e resultados roláveis.
- Downloads de ROM mostram progresso na ficha e na fila. Arquivos novos preservam nomes reconhecíveis, sujeitos à verificação e tratamento de colisão.
- Sessões preservam tempo acompanhado por checkpoints. Finalizar solicita o fechamento da janela do jogo.
- Captura Windows por janela, gravação em segundo plano e suporte ao botão Captura do Switch Pro via SDL3. Os avisos de rotina aparecem no canto da janela.
- Desejos ganha filtros responsivos e complemento opcional de desconto em BRL para ofertas com identidade confirmada.

## Validação e limites

- O workflow executa a suíte Windows, monta e verifica o aplicativo e o atualizador, testa o pacote extraído e produz capturas isoladas.
- Os nomes físicos de ROMs que já existiam são preservados. A recuperação desses nomes será tratada separadamente.
- A cobertura de preços para consoles, captura WGC em jogos reais, o desligamento no Windows físico e as integrações autenticadas ainda dependem de homologação própria.
- Backups de saves tradicionais são locais. O fluxo de ROMs no Drive permanece de leitura e o cadastro protegido A4 mantém seu contrato.

Consulte o relatório de continuidade no código-fonte para o histórico, as preferências de interface e as próximas etapas.

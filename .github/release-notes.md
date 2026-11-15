# Checkpoint 0.1.35

**PRÉ-RELEASE para Windows x64.**

- Jogar usa a ROM vinculada e o perfil de emulador. Encerrar o processo do emulador finaliza o registro da sessão.
- Tempo jogado do app e da Steam somado em um total, como 2h15min, sem duplicar snapshots.
- Desejos com cards de até 360 px, arte quadrada, mais colunas e preço de loja oficial por padrão. Opção de incluir keyshops; ausência de preço com motivo explícito.
- Status editável na ficha: Backlog, Jogando, Pausado, Concluído e Abandonado.
- Memórias com orientação inicial, cards alinhados e exclusão com confirmação.
- Configurações com prévias dos nove temas, tamanho das capas destacado e prévia à direita do slider. Botões e logos de conexão ajustados.
- Ficha exclusiva de desejos, banners sem recorte, resumo da Wikipédia e mensagens de ausência de descrição.
- Captura de janela com Ctrl+Shift+S configurável, vinculada ao jogo iniciado pelo Checkpoint. Detecção de executáveis nas bibliotecas Steam por VDF/manifests.
- Troca de aba por clique completo, calendário no fuso local e remoção de textos de apoio.

## Pendências conhecidas

- Fechar apenas a ROM, deixando o emulador aberto, ainda pode exigir encerrar o registro manualmente na aba Atividade. A detecção automática desse caso continua pendente.
- Adicionar jogo > ROM do Drive ainda exige escolha e confirmação (A4).
- A captura real de jogos no Windows ainda não foi validada; o primeiro uso real será no PC do dono. Testes com adaptador controlado não equivalem a essa validação.
- Emuladores, contas reais das integrações, instalações Steam e DPI/fontes do PC do dono continuam sujeitos à validação de uso real.

Schema 4 preservado. Sem alteração dos arquivos protegidos de cadastro/Drive e lifecycle. O workflow só publica após testes Windows, build e verificação do pacote extraído.

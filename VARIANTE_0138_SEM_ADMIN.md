# 0.1.38 — variante sem elevação, somente ZIP

Pedido: pacote separado para abrir com privilégios do usuário, sem pedir administrador; sem tag/release. Base 9dd9c93, checkout inicial limpo; branch build/0.1.38-sem-admin. A release normal e sua tag permanecem intactas.

app.main aceita request_elevation=True por padrão; entrada separada run_checkpoint_user.py chama False. O aplicativo usa o diretório/cofre do usuário atual. Não altera a configuração UAC do Windows nem solicita privilégios do sistema. Programas externos que exigem administrador continuam sujeitos às permissões normais.

Build -NoElevation seleciona a entrada separada. O empacotamento confere entrada efetivamente congelada e manifesto asInvoker, checksum/CRC, smokes de abertura/cadastro/auxiliar e janela nativa do .exe extraído. O runner Windows é elevado; isso não será descrito como homologação interativa de conta padrão ou do PC da empresa. Testes específicos simulam inicialização congelada e exigem zero chamadas de elevação antes dos dados, com diretório padrão e personalizado.

Workflow de validação somente nesta branch é dedicado ao build rápido da variante: testes direcionados de bootstrap/abertura, empacotamento e artefato. Permissões contents:read; sem job de publicação, release ou tag. Não enfraquece asserções existentes nem modifica protegidos/A4. Resultado final e hash serão registrados após o build.

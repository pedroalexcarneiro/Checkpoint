# 0.1.38 — variante sem elevação, somente ZIP

Pedido: pacote separado para abrir com privilégios do usuário, sem pedir administrador; sem tag/release. Base 9dd9c93, checkout inicial limpo; branch build/0.1.38-sem-admin. A release normal e sua tag permanecem intactas.

app.main aceita request_elevation=True por padrão; entrada separada run_checkpoint_user.py chama False. O aplicativo usa o diretório/cofre do usuário atual. Não altera a configuração UAC do Windows nem solicita privilégios do sistema. Programas externos que exigem administrador continuam sujeitos às permissões normais.

Build -NoElevation seleciona a entrada separada. O empacotamento confere entrada efetivamente congelada e manifesto asInvoker, checksum/CRC, smokes de abertura/cadastro/auxiliar e janela nativa do .exe extraído. O runner Windows é elevado; isso não será descrito como homologação interativa de conta padrão ou do PC da empresa. Testes específicos simulam inicialização congelada e exigem zero chamadas de elevação antes dos dados, com diretório padrão e personalizado.

Workflow de validação somente nesta branch é dedicado ao build rápido da variante: testes direcionados de bootstrap/abertura, empacotamento e artefato. Permissões contents:read; sem job de publicação, release ou tag. Não enfraquece asserções existentes nem modifica protegidos/A4. Resultado final e hash serão registrados após o build.

## Resultado

Build somente de artefato 43865947628 aprovado no commit 07baf7884a3d5fb563722e3397e1f3ae2bfb75b3. 13 testes direcionados aprovados no Linux (2,40 s) e Windows (3,33 s); sem alteração de asserções existentes. Executável congelado contém entrada run_checkpoint_user e manifesto asInvoker, ambos conferidos diretamente no PE/arquivo PyInstaller. ZIP extraído passou smokes de abertura/cadastro/auxiliar e abertura nativa, resposta e fechamento, exit 0. Runner elevado; não equivale a teste interativo de conta padrão/PC da empresa.

Arquivo Checkpoint-0.1.38-sem-admin-windows-x64.zip, SHA-256 3eb96f30341f07cd126c05a7d367172a81372ea54065c7dd6b3089ed0247625a. Download do artefato conferido com digest GitHub 65688c7af1b8a99e4f48e66f4f0427d20e21cd7624e9558e8332b00272159e64; checksum interno e CRC do ZIP aprovados. Sem tag ou release nova e sem modificação dos arquivos da release normal. ZIP entregue diretamente pelo workspace.

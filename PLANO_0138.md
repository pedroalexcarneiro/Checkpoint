# 0.1.38 — correção de abertura

Base: fix/0.1.37-ajustes, 929f69361aa70e416de57faa72a9fc61257ef866, remoto reconfirmado; checkout inicial limpo. Tag publicada v0.1.37 em c526cb4 preservada. Branch isolada fix/0.1.38-abertura. Pedido: aplicativo não abre; vídeo de 25,9 s mostra solicitação UAC e ausência da janela depois. O vídeo não é anexado ao repositório e não prova sozinho qual etapa falhou.

1. Reproduzir o uso indevido de winId durante mensagem de criação; testar HWND normal/64 bits/ausente. Inspecionar bootstrap de elevação sem presumir causa UAC.
2. Corrigir windows_frame.handle para usar o HWND da própria mensagem, evitando recriar a janela ao receber mensagens de criação. Não tocar banco, dados, cofre, A4, assets ou arquivos protegidos.
3. Acrescentar teste em subprocesso com Qt windows no Windows e offscreen no Linux; dois jogos, criação/visibilidade/captura/fechamento, timeout e faulthandler. Registrar exatamente o backend executado.
4. Acrescentar à validação do pacote abertura normal do fonte e do executável extraído com Qt windows e executor já elevado. Sem --smoke-test, sem automatizar consentimento UAC, HWND visível/responsivo, screenshot, fechamento e SQLite. Não declarar que isso homologa consentimento UAC no PC do dono.
5. Executar suíte completa Linux e workflow Windows UI validation, sem publicar automaticamente nem substituir tag/arquivos 0.1.37. O primeiro run revelou checkout raso incompatível com o contrato que lê c51c245; ajustar somente fetch-depth: 0 no workflow de validação, mantendo o workflow de publicação intacto. Não modificar ou contornar a asserção protegida. Registrar resultados antes de decidir a entrega da correção.

Preservar asserções existentes, LF/UTF-8, schema 4, identidade/metadata/sessões/ROMs e originais. Nenhuma limpeza de dados pessoais para contornar abertura.

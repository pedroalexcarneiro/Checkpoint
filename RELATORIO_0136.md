# Relatório em andamento — Checkpoint 0.1.36

Base: 818ec80a492a29936782ddb3a43eecaf3ef996e3. Branch local fix/0.1.36-ajustes. Não publicada. Plano: PLANO_0136.md. Resultados atuais: RELATORIO_0136_TESTES.md.

Os três vídeos foram recebidos e quadros selecionados inspecionados. Não houve controle ou teste no Windows do dono. Capturas de referência e vídeos são evidência visual externa, não reprodução executada por este ambiente.

Registro por item e resultados serão acrescentados após testes. A4 e distinção ROM descarregada/emulador vivo permanecem separados, sem alteração dos contratos protegidos.

## 06 — captura global — parcial

Anterior: QShortcut limitado ao Checkpoint e retorno imediato se a janela não estivesse ativa. Vídeo não prova uma captura global executada. Reprodução controlada anterior: 8 testes existentes, captura bloqueada fora de foco conforme contrato antigo.

Implementado: RegisterHotKey/WM_HOTKEY com MOD_NOREPEAT, validação de combinação, substituição com registro novo antes de liberar o anterior, conflito visível sem salvar configuração inválida, liberação no fechamento aceito. Captura seleciona PID da janela em primeiro plano, exige processo de sessão vivo e associação única; não usa a ficha aberta para decidir. Valida HWND/PID/visibilidade antes/depois de obter pixels; erro não grava arquivo. Sem mudança na sessão por foco.

Arquivos/funções: checkpoint/global_hotkey.py (GlobalCaptureHotkey, WindowsHotkeyApi, native_key), game_capture.py (WindowsCapture, capture_game), window.py (inicialização, set_capture_shortcut, closeEvent); testes de captura 0135/0136. Expectativa antiga de app ativo substituída pela autorização explícita do item 06, preservando associação/arquivo e ausência de sessão.

Posterior: 10 testes Linux com adaptadores, dois jogos, troca/conflito/liberação, múltiplos PIDs, sessão encerrada/ambígua, atribuição e um arquivo por acionamento. Saídas integrais no relatório de testes. Referência nativa: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerhotkey.

Limitações: implementação nativa não executada em Windows nem em jogo/emulador real; QScreen.grabWindow pode não fornecer conteúdo de renderizadores exclusivos/DirectX (erro de imagem nula orienta modo janela, imagem preta não é validação positiva). Processos-filhos/launchers não associados são rejeitados, sem alegar suporte. Checkpoint em primeiro plano não é alvo elegível: ativar a janela do jogo. Windows com jogo/emulador/minimizado, conflito com outro app e pixels efetivos permanecem não testados.

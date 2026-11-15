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

## 04 — banner da ficha — parcial (relato Windows ainda não reproduzido)

Anterior: a implementação já usava KeepAspectRatio. Os testes existentes de bordas passaram. Não se comprovou o recorte relatado no Windows a partir do vídeo/faixa do Início. A primeira execução do novo teste falhou por ausência do método de inspeção banner_rect e por erro da fixture (add_wish não existe em Library); corrigida a fixture usando wishlist isolada, sem mudança de contrato ou asserção.

A área da imagem agora é calculada em banner_rect a partir da geometria atual a cada pintura e desenhada diretamente do pixmap original, sem cache escalado anterior. Removido cálculo de proporção sem uso. Fonte: checkpoint/ui_components.py::Hero.banner_rect/paintEvent/resizeEvent; testes/test_banner_resize_0136.py. Dois jogos de fixture (Aurora/Horizonte), duas proporções 1200×250/600×400, posse e Desejos, abrir em 1280×800/1920×1080 e repetir grande/menor/restaurado. Comparação de pixels das bordas superior/inferior e proporção/contain, sem deformação.

Screenshots sintéticas anteriores: antes-ficha-{1,2}-{1280x800,1920x1080}.png em evidencias-0136. Qt offscreen, DPR 1, 96 DPI lógicos; metadados antes-screens.json. Alteração não prova correção da ocorrência Windows. Maximização nativa e DPI do dono não testados; resize offscreen não equivale a homologação Windows.

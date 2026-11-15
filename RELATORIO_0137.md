# Relatório 0.1.37 — em implementação local

Base: 58b0c118c534dbdbc3bc080db4a95e7ecd1554d1 de fix/0.1.36-ajustes; remoto reconfirmado e checkout inicial limpo. Branch: fix/0.1.37-ajustes. Sem autorização para publicação, push, PR, tag, release ou workflow de lançamento. Código, tag e assets publicados da 0.1.36 permanecem preservados.

Pedido: documento enviado em 15/11/2026, com imagens A (Início integrado) e B (lista horizontal). Vídeos p1–p4 ausentes neste chat: horários e problemas citados são relatos, não testes diretos. Capturas futuras do app usarão dados sintéticos isolados e serão identificadas. Não confundir Linux/Qt offscreen com Windows real do dono.

Plano e ranking de ofertas: PLANO_0137.md. Registro por item será atualizado com requisito, evidência antes/depois, reprodução, arquivos/funções, commit, testes, resolução/escala, limitações e status. A4 bloqueado; troca automática de ROM descartada; encerramento apenas da ROM permanece limitação conhecida.

## Estado inicial comprovado

- Lista usa QTableWidget com cabeçalhos Logo/Jogo/Plataforma/Status/Gênero/Nota: diverge da imagem B e do item 5.
- Início atual escolhe Jogando/Pausado e pode usar updated_at: não representa necessariamente uma execução. Novo bloco usará play_sessions criadas após Popen bem-sucedido, sem fabricar histórico.
- Grade decodifica cover_pixmap em cada paint e refresh_library reconstrói grade e tabela; medir antes de atribuir o travamento do PC do dono a essas operações.
- Períodos têm rótulos Diário/Semanal/Mensal; item 8 solicita Hoje/Esta semana/Este mês, com semântica preservada.
- Perfil só seleciona imagem e faz recorte central ao apresentar: faltam posicionamento/zoom/recorte editável.
- Schema 4; play_sessions existente fornece início, PID e estado. Não há necessidade identificada de nova tabela para jogos recentes.
- Fonte GG.deals atual: API agregada Steam/BRL, sem original individual/plataforma/edição na resposta documentada. Cobertura de consoles autenticada ainda não comprovada; investigar sem consultar cofre real.

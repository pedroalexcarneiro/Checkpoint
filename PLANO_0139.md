# Checkpoint 0.1.39 — plano local de correções

## Autorização posterior de lançamento

Após revisar botões/aviso e ser informado da pendência console, o dono instruiu:
“ok, quando finalizar, pode já dar release no github”. Isso autoriza enviar o
código validado, executar o workflow Windows release existente e publicar a
0.1.39 se os gates passarem. Não autoriza force push nem reescrever tags/releases
anteriores ou alegar suporte console não comprovado. A restrição abaixo descreve
a fase inicial; os demais contratos permanecem.


## Autorização e base

Pedido integral recebido em 16/11/2026: correções da 0.1.38 e polimento,
sem push, PR, tag, release, publicação, troca de assets ou workflow de lançamento.
Commits locais por unidade coerente, sem reescrever histórico. Prioridade:
preservar o aplicativo, dados e contratos. Alvo 0.1.39, nunca v1.39.

Checkout inicial limpo: build/0.1.38-sem-admin em
1252b81574b0653bd90cfea0ab1786b4e04c3411. Variante preservada.
Base normal remota reconfirmada: fix/0.1.38-abertura em
9dd9c93ce7baf0051bbc783323b401d4ba8c7059; tag v0.1.38 em
c4a7e1d221ba52a8580dd73ab884b1964e6ffd32. Nova branch **local**:
fix/0.1.39-polimento, criada da base normal, preservando UAC normal.

Lidos AGENTS, CONTINUITY, PROJECT_STATUS, ARCHITECTURE, DESIGN, TESTING,
INTEGRATIONS, ROADMAP, CHANGELOG e plano/relatórios recentes.
Os prints específicos da 0.1.38 mencionados no pedido não foram anexados
nesta mensagem: seus defeitos são relatos, até reprodução independente.
Referências anteriores no chat continuam disponíveis, sujeitas ao pedido novo.

## Etapa A — base e evidências

1. Guardar checkout/HEAD remoto/ambiente. Executar suíte inicial congelada.
2. Capturar app real com banco isolado antes das alterações: 1280×800,
   1920×1080 e 1000×700. Inspecionar geometrias, estilos e serviços envolvidos.
3. Criar regressões de comportamento/geometria que falhem na base; pelo
   menos dois jogos onde aplicável. Não mudar asserções sem relação com
   requisito substituído. Não usar skip/xfail nem contornar contrato.

## Etapa B — correções locais, em commits próprios

4. Item 3: Início alinhado pelo topo, altura por conteúdo, sessões reais
   (mesmo jogo pode repetir), botão integral, arte inteira/arredondada,
   carrossel responsivo e acionável, par de setas consistente; cabeçalho
   semanal adaptável; ofertas compactas com classificação e identidade.
5. Item 4: Desejos compactos, arte 1:1, mais colunas, largura limitada pelo
   conteúdo disponível sem esticar poucos cards; preservar ficha exclusiva.
6. Item 6: Diário compacto e alinhado, tipografia consistente; grade mista
   consistente com capturas. Preservar texto e exclusão/cancelamento.
7. Item 7: auditar completed_at, significado e filtro antes de integrar
   Jogos concluídos às métricas. Não criar persistência nem inferir data de status.
8. Item 8: retirar foco externo pontilhado; mouse mostra seleção na capa
   e percentual, teclado mantém foco discreto na própria arte. Cinco tamanhos.
9. Item 11: reservar 12–16 px lógicos entre lista da Biblioteca e barra,
   com espaço estável e sem sobrepor favorito ou criar rolagem horizontal.
10. Item 13: ícone de adicionar usa primeiro plano correto em cada estado
    do botão; preservar logos de serviços.
11. Item 14: auditar paleta/preview Preto; corrigir só esse tema para
    superfícies neutras, verificar contraste e demais oito paletas intactas.
12. Itens 15/16: Arquivos com nome ocupando centro e ação à direita,
    acesso ao nome integral; saves vazio/configurado compactos, ação única,
    pasta/backup reais. Não modificar identidade, serviços ou originais.

## Etapa C — navegação

13. Item 9: aba Emuladores reutiliza gestão existente e seus IDs/argumentos,
    edição/adição/remoção explícita, aviso de executável ausente. Perfil em uso
    deve ser tratado sem apagar ROMs/saves. Acesso pela ficha preservado.
14. Item 10: aba Lixeira, quantidade, identificação/ID/plataforma, restauração
    individual; testar registros homônimos em banco isolado. Sem exclusão nova.

## Etapa D — diálogos

15. Item 12: inventário de diálogos próprios e contratos; componente comum
    opt-in de apresentação, títulos Windows/tema, português, centralização,
    área disponível, foco/Escape/padrão e cancelamento. Testar progressivamente.
    Seletores nativos e UAC ficam sob controle do sistema. Arquivos protegidos
    não serão alterados nem terão comportamento contornado por monkeypatch
    ou interceptação global. Preparar proposta específica se houver bloqueio.

## Etapa E — integrações

16. Item 5: rever documentação oficial GG.deals e caminhos reais da API,
    identidade/plataforma/edição/região/moeda/proveniência. Implementar apenas
    capacidade comprovada nas integrações autorizadas. Sem fonte ou scraping
    novo silencioso; sem credencial real/cobertura comprovada, marcar bloqueio
    e apresentar dependência concreta, nunca chamar filtro de suporte console.
17. Item 16.1: rastrear configuração/backup/restauração e destino real dos
    saves. Explicar o fluxo disponível e ausência/presença de upload Drive.
    Não implementar sincronização nova; proposta separada se faltar.

## Fechamento revisável

18. Regressões de itens 17–19: lista/favorito/status/ROM local/identidade,
    sessões/tempo/UAC/hotkey/banners/dados/cofre/schema 4/A4 e protegidos.
19. Capturas reais intermediárias e posteriores das telas afetadas, normal,
    menor, maximizada/restaurada e DPI disponíveis; vazias/preenchidas e
    títulos longos. Dados sempre isolados e identificados como fixtures.
20. Suíte integral final com stdout, stderr, comando, ambiente e exit sem
    truncar os arquivos de evidência; smokes de páginas/cadastro/SQLite.
    Windows real, DPI/monitores nativos e contas sem ambiente disponível
    serão marcados não testados. Sem push nem workflow para obter Windows.
21. RELATORIO_0139.md, RELATORIO_0139_TESTES.md, NOTAS_0139.md e docs atuais:
    requisitos/evidências/reprodução/causa/arquivos/funções/SHAs/resultados/
    limitações/status. Entrega revisável, sem declarar prontidão integral
    enquanto existirem bloqueios importantes. Publicação exige nova autorização.

## Contratos preservados

Complemento visual do dono durante execução: Início aproveita a largura útil
após a lateral com margens 24–32 px, sem teto central de 1440 nem ampliação
de cards/imagens para ocupar sobra. Mais sessões visíveis conforme largura;
artes e cards menores. Ofertas em linhas compactas com miniatura, imagem com
os quatro cantos arredondados como a Biblioteca, conteúdo/proporção preservados.
Capturas normal e ampliada exigidas antes de aprovação visual.

A4 ROM → candidatos → escolha → confirmação; tests/test_save_lifecycle.py,
checkpoint/worker.py, enrichment.py, game_import.py, completion_queue.py e
dialogs.py; quick_add.py somente exceções históricas explicitamente concedidas.
Não alterar teste de preservação. Sem reconhecimento automático de troca de
ROM. Fechar apenas ROM com emulador vivo permanece limitação conhecida.
Novos/modificados UTF-8/LF; nenhuma normalização incidental de protegidos.

Evidências integrais locais: /workspace/work/evidence-0139 (sem dados pessoais).

## Complementos posteriores à revisão inicial

- C1 — Captura: investigar quadros repetidos no HSR, obter novo quadro da área
  cliente elegível e publicar imediatamente em Memórias/Início/ficha conforme
  a tela visível. Preservar filtros, originais e associação à sessão; testar
  duas janelas controladas e rejeitar mudança de alvo. Windows/DirectX real
  do dono não é homologado por adaptador Linux ou janela Qt no runner.
- C2 — Estatísticas em janela menor: distribuir painéis conforme espaço útil,
  corrigir espaço de nomes e separar resumo/legenda do mapa sem sobreposição;
  verificar 1000×700, 1280×800, 1920×1080 e retorno ao tamanho normal.
- C3 — Conclusões: mostrar o card Jogos concluídos já implementado no item 7,
  em vez do texto cru da versão antiga, preservando completed_at e os filtros.
- C4 — Degradê aprovado: após duas prévias reais do Início, o dono respondeu
  “legal, gostei. podemos seguir” à segunda. Aplicar essa intensidade às
  superfícies, preservar destaque dos nove temas e Preto neutro. Não copiar
  marca/textos/indicadores do sistema usado como referência.

Acrescentar commits, sem alterar os já feitos. Repetir a suíte integral após
os complementos; os 752 testes anteriores não validam o novo código. A
autorização de release permanece condicionada aos gates finais.

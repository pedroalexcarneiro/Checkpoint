# Roadmap de execução

O escopo completo solicitado permanece como objetivo. As fases abaixo indicam entregas incrementais, sem declarar o produto final concluído.

## Fase 1 — Fundação (implementada, refinamentos pendentes)

- [x] Projeto modular, SQLite com duas migrações, configurações, logs e trava de instância.
- [x] Seis áreas de navegação, estados vazios, tema escuro.
- [x] CRUD manual, recuperação de removidos, galeria/lista, pesquisa, filtros, favoritos e ordenação.
- [x] Cadastro de campos pessoais, artes, categoria e página individual.
- [ ] Migração para plataformas/gêneros/categorias normalizados, gerenciamento dedicado de categorias.
- [ ] Paginação/virtualização para dezenas de milhares de jogos, acessibilidade e alta DPI.

## Fase 2 — Metadados e arte (parcial)

- [x] Contrato de provedores, RAWG com escolha manual de resultado e importação de detalhes.
- [x] SteamGridDB com seleção de jogo, tipo de arte e confirmação visual.
- [x] Cache local por SHA-256, validação de imagem, recorte 3:4 sem deformar.
- [ ] Testes reais autenticados, atribuição exigida pelos provedores, condições de uso antes de distribuir.
- [ ] IGDB, Steam metadata, foco do recorte, previews em miniatura, cache das capas manuais e cache HTTP.

## Fase 3 — Drive e ROMs (parcial)

- [x] OAuth de desktop com token no cofre Windows, raiz por ID, scan BFS paginado e metadados locais.
- [x] Cursor de alterações e atualização incremental; versões e associação manual a um único jogo.
- [x] Download por ID com parcial e verificação, persistência local até decisão do usuário.
- [x] Normalização de nomes, catálogo DAT e candidatos exatos por MD5/tamanho/plataforma.
- [ ] Validação real, seletor visual de pastas, progresso/cancelamento, mudanças concorrentes complexas, 410 e drives compartilhados.
- [ ] Retomada HTTP persistente, CRC32/SHA-1 de arquivos locais sob demanda, catálogos externos e ranking de sugestões.
- [ ] Região/tradução/hack/revisão editáveis e remoção local explícita segura.

## Fase 4 — Launcher e sessões (parcial)

- [x] Executável local, perfis com lista de argumentos, plataforma e extensões.
- [x] ROM local por versão, validação de caminhos, sem shell.
- [x] Sessões do processo direto, emuladores com término manual explícito, recuperação de interrupções.
- [ ] Steam/Epic/outros launchers, URIs permitidas, processos filhos, pausa/suspensão, integrações específicas por emulador.
- [ ] Steam Web API: biblioteca, perfil, horas remotas e conquistas, com deduplicação e origem separada.

## Fase 5 — Experiência pessoal (parcial)

- [x] Diário, mídia referenciada, ampliação de imagens, vídeo no reprodutor padrão, marcos pessoais.
- [x] Totais, status, plataformas, gêneros, ranking, horas semanais/mensais, médias e conclusões por mês.
- [ ] Editor completo de diário/mídia/marcos, anexos por registro, progresso estruturado e galeria visual.
- [ ] Gráficos temporais completos, fuso local configurável e histórico de transições de status.
- [ ] Steam e RetroAchievements reais, reprodução de vídeo integrada quando suportada.

## Fase 6 — Saves (parcial)

- [x] Backup local manual específico, ZIP versionado, manifesto, integridade e restauração com cópia anterior.
- [ ] Perfis tradicionais efetivamente validados por emulador/jogo.
- [x] Configuração persistente por jogo, verificação de estabilidade e backup opcional ao fim do registro de sessão (0.1.2).
- [ ] Google Drive com escopo separado drive.file, upload/download versionado, conflitos e restauração remota.
- [ ] Recuperação transacional de restauração interrompida e política de retenção explícita.

## Fase 7 — Desejos e preços (inicial)

- [x] Lista local, meta em centavos BRL, alteração e remoção.
- [ ] Provedor IsThereAnyDeal após contrato/credencial e confirmação de cobertura BRL.
- [ ] Histórico real, menor preço observado, links, promoções, alertas e scheduler com rate limiting.
- [ ] Avaliar Steam, Epic, Nuuvem, GOG e GG.deals apenas com acesso autorizado/confiável; sem scraping presumido.

## Fase 8 — Finalização (em andamento)

- [x] Suíte automatizada e modo smoke, documentação e receita PyInstaller.
- [ ] Instalação limpa Windows 10/11, certificados, assinatura, licenças de terceiros e instalador.
- [ ] Testes de carga, falhas de disco/rede, múltiplos monitores, DPI, Unicode e processos reais.
- [ ] Atualização segura, migrações com backup automático e distribuição pública.

Próxima prioridade: validar credenciais em biblioteca isolada; robustecer scanner e sessões; implementar automação e Drive para saves; conectar preços com fonte regional validada. Não iniciar novas fontes antes de estabilizar os fluxos existentes.

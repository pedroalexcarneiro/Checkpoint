# Visão e escopo do produto

Este arquivo preserva os requisitos originais e as decisões posteriores relevantes.
Itens abaixo são objetivos, não uma declaração de implementação. Consulte
CONTINUITY.md e PROJECT_STATUS.md para o estado real.

## Produto e arquitetura

Checkpoint é uma biblioteca pessoal offline para Windows 10/11, reunindo PC, Steam,
Epic, outros launchers, independentes, emuladores e ROMs do Google Drive. Deve organizar,
executar, acompanhar e registrar a trajetória do jogador. Python/PySide6/SQLite,
integrações por APIs e arquitetura modular, configurações persistentes, logs, migrações,
tratamento de falhas e credenciais protegidas. Distribuição Windows por PyInstaller.

## Interface e biblioteca

Navegação: Início, Minha biblioteca, Lista de desejos, Capturas e memórias, Estatísticas,
Configurações. Início com destaque, recentes, em andamento, continuar jogando, atividades,
resumo e desejos; estados vazios quando faltam dados. Sem números fictícios.
Galeria e lista com busca por título, filtros por plataforma/gênero/status, ordenação,
favoritos, categorias, CRUD e detalhes. Status: não iniciado, backlog, jogando, pausado,
concluído e abandonado. Ficha: nome, descrição, desenvolvedora, publicadora, lançamento,
plataforma, gênero, capa/banner/logo, status, nota, favorito, notas, origem e IDs externos.
Visual editorial limpo, paletas discretas, tipografia/espaçamento consistentes, transições
suaves quando úteis. Sem slogans. Capas 3:4 com arte inteira; banners horizontais e logos
transparentes quando disponíveis, imagens sem moldura física/branco de embalagem.

## Metadados e artes

Provedores substituíveis IGDB, SteamGridDB, RAWG e Steam. Buscar, exibir resultados,
exigir escolha quando ambíguo, importar ficha e selecionar cover/banner/logo. Persistir
identidades e cache local. Credenciais próprias documentadas, nunca chaves inventadas.
ROMs de emuladores também devem poder ter ficha/artes pelo jogo confirmado. Nome original
da ROM preservado; título da biblioteca pode vir do catálogo. Adicionar jogo permite
pesquisar o índice Drive e preencher a ficha, sem precisar ir às Configurações.

## Drive e identificação de ROMs

OAuth, escolher pasta raiz, scanner recursivo eficiente somente de metadados, plataforma
pela hierarquia e regras configuráveis; suportar pastas novas/nomes comuns de consoles.
Persistir nome original, extensão, tamanho, pasta, ID, modificação, plataforma, MD5 quando
disponível. Atualizar incrementalmente pela API Changes. Identificar por nome normalizado,
plataforma, catálogos/DATs e CRC32/SHA1/MD5 conforme disponibilidade. Não baixar só para
identificar; baixa confiança vai à revisão. Regiões/traduções/hacks/revisões/formatos são
arquivos distintos vinculáveis ao mesmo jogo. Usuário escolhe versão; sem duplicação fraca.
Download sob demanda por ID, destino configurável, integridade e disponibilidade local.
Arquivo permanece até remoção explícita local; nunca excluir original ou backups do Drive.

## Launcher e sessões

PC e launchers externos, ROMs e emuladores. Perfis: nome, executável, argumentos próprios,
plataformas, extensões e ajustes específicos. Validar caminhos/disponibilidade antes de
executar, oferecer download quando remoto. Registrar início/término/duração por jogo;
não contar tempo ocioso do emulador como ROM ativa. Integrações por processo/emulador
quando possíveis e recuperação de sessões interrompidas. Steam oficial: jogos, perfil,
tempo e conquistas quando a privacidade da conta permitir, com limitações documentadas.

## Experiência pessoal e estatísticas

Diário por jogo: data, texto, impressões, progresso, momentos, notas e mídias associadas,
consultável em linha do tempo. Galerias de imagens/vídeos importados, legendas, descrições,
datas e vínculo ao jogo, ampliador/player quando suportado, sem duplicação desnecessária.
Conquistas Steam/RetroAchievements quando acessíveis e marcos pessoais manuais.
Estatísticas reais: total/status, horas, mais jogados, plataforma/gênero, tempo semanal
e mensal, média das sessões e evolução dos concluídos. Gráficos claros e consistentes.

## Saves tradicionais

Somente saves tradicionais, nunca save states. Configuração de caminhos/padrões por jogo
e emulador, backup manual e automático após sessão/estabilidade, cópias no Drive organizadas
por plataforma/jogo, versões, conflitos, verificação e restauração preservando cópia anterior.
Não supor diretórios/formatos universais; documentar perfis efetivamente validados.

## Desejos, preços e configurações

Desejos com alvo BRL, preço atual/mínimo, histórico, promoções, loja/link e alertas.
Avaliar Steam/Epic/Nuuvem/GOG/GG.deals/IsThereAnyDeal por APIs ou acesso permitido.
Atualização periódica com limites; documentar fontes indisponíveis, não fazer scraping
que viole termos. Configurações centralizam APIs, Google Drive, Steam, RA, diretórios,
emuladores, aparência, notificações, backups e frequência de preços. Integrações exibem
estado real: não configurada, aguardando autenticação, conectada ou erro.

## Método, segurança e entrega

Fases: fundação; metadados/visual; Drive/ROMs; launcher/tempo/Steam; experiências;
saves; preços/desejos; testes/otimização/documentação/Windows. Pode reorganizar por
dependências sem eliminar requisitos. Não parar na primeira tela, não criar botões vazios,
não declarar teste autenticado a partir de mocks, não esconder limitações ou TODOs críticos.
Preservar dados e originais, downloads interrompidos, HTTPS e segredos. Manter README,
ARCHITECTURE, ROADMAP, CHANGELOG, SETUP, INTEGRATIONS, TESTING e PROJECT_STATUS atualizados.
Continuar a partir dos arquivos mesmo se a conversa mudar de dispositivo ou ambiente.

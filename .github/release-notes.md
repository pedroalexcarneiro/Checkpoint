# Checkpoint 0.1.39 — correções e polimento

Correções da 0.1.38 e polimento da interface.

- Início usa a largura disponível com margens curtas, Últimas sessões reais
  (incluindo sessões distintas do mesmo jogo), cards menores, capas inteiras
  arredondadas, navegação responsiva e setas equivalentes.
- Resumo semanal adaptável e Ofertas em linhas com miniaturas arredondadas,
  identificação, origem e preço conforme a política de lojas.
- Desejos mais compactos e com mais colunas; ficha exclusiva e favoritos preservados.
- Diário compacto na aba própria; na visualização mista, nota e captura têm
  áreas de prévia equivalentes, texto íntegro e leitura acessível.
- Jogos concluídos integrado ao filtro de Estatísticas, usando a última data
  de marcação já gravada, sem inventar histórico ou criar datas pelo status.
- Foco do teclado dentro das capas de Aparência; tema Preto com superfícies neutras.
- Abas Emuladores e Lixeira: perfis existentes reutilizados e restauração
  individual em cards com logo, nome e data real ou Data não registrada.
- Seleção de perfil pela ficha, gerenciamento com botões agrupados e aviso
  explícito para perfil em uso; remover configuração preserva arquivos.
- Diálogos próprios com tema, botões em português, espaçamento e limites da tela;
  seletores nativos e UAC mantêm o comportamento do sistema.
- Lista da Biblioteca com espaço estável para rolagem; ícones primários na cor
  do texto; nomes longos de ROM e saves tradicionais com composição compacta.

## Pendências e limites

- Consulta real de preços de Switch/PlayStation/Xbox não foi comprovada na API
  atual. Filtro de plataforma não significa suporte console pronto.
- Backups de saves são locais; não existe upload/sincronização implementado
  para o Drive. A integração de ROMs usa acesso de leitura.
- Fechar apenas a ROM com o emulador aberto continua exigindo encerramento
  manual do registro quando necessário; não há reconhecimento de troca de ROM.
- A4, dados, schema 4, identidades, cofre, originais e histórico preservados.
- Testes em runner não homologam contas, emuladores, captura, consentimento UAC
  ou uso no PC do dono. Resultados efetivos acompanham o relatório de lançamento.

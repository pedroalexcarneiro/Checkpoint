# Revisão local após a 0.1.39

Base d57dc56, preservando tag/release 0.1.39. Branch local fix/pos-0139-layout.
Sem autorização de publicação desta revisão; sem push, workflow, tag ou release.

1. Início: um card por ID de jogo, pela sessão mais recente. Histórico completo,
   tempos, sessões e jogos homônimos permanecem intactos.
2. Memórias no Início: largura padrão, quantidade responsiva e carrossel;
   não esticar poucos cards para preencher a linha.
3. Memórias geral: teto de largura por card e prévias sem preenchimento escuro
   artificial; imagem inteira, sem remover faixas pertencentes ao arquivo.
   Nota e captura continuam com áreas equivalentes na grade mista.
4. Desconto: rastrear do provedor até a ficha/Desejos. Usar apenas preço original
   e atual da mesma oferta oficial/contexto; histórico não é preço original.
   Registrar bloqueio se a fonte não informar dados suficientes.
5. Ofertas: comparar miniatura de capa e banner inteiro, em linhas compactas.
   Mostrar comparação real antes de adotar o banner como padrão.
6. Aparência: referência apenas de cores de interface do HTML enviado, sem dados
   de negócio/gráficos/scripts. Fundo acompanha o destaque escolhido; claro e
   escuro independentes da cor. Contraste legível, saturação moderada e Preto
   neutro. Capturas reais para revisão.

Regressões antes/depois, com dois jogos, UTF-8/LF, dados isolados. Nenhum contrato
A4/protegido é alterado. Atualizar documentação e suíte completa ao fechar o código.

Fechamento local: itens implementados; capa mantida após comparação com banner.
Complemento GG.deals aprovado, opcional e desligado por padrão. Gate do código
d808f76: 808 testes Linux aprovados em 547,90 s; smoke seis páginas/SQLite ok.
Capturas e relatórios registrados. Sem publicação; Windows/pacote, conta real,
consulta console e aprovação visual final continuam separados desta validação.

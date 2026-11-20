# Percentual ausente na consulta por API — proposta revisável

Situação: price_summary/comparison já exibem percentuais confirmados. A consulta
oficial atual preenche preço atual/histórico e não original da oferta. Histórico
não é preço de tabela: calcular um desconto a partir dele produziria dado errado.
O coletor público existente já lê price-old por oferta, mas a opção atual promete
usar a página pública quando não houver chave; não significa completar toda API.

Proposta, ainda não implementada nem ativada:

- Controle explícito em Conexões: completar detalhes da oferta pela página pública
  do GG.deals. Desligado inicialmente, independente do fallback sem chave.
- Reutilizar GgDealsProvider existente; nenhuma fonte, conta ou serviço novo.
  Consulta adicional pelo mesmo Steam AppID/contexto, uma vez por atualização
  do cache, apenas para as plataformas realmente suportadas.
- Novo price_enrichment.py compõe API + detalhes públicos, ligado por
  prices.default_provider quando a opção estiver ativa. Não alterar cofre.
- Exigir identidade/canônico correspondentes, BRL, classificação de loja,
  preço atual coincidente e original maior que o atual na mesma oferta. Lojas
  oficiais continuam padrão; keyshops seguem opção separada.
- Divergência de edição, preço ou origem: não preencher desconto. Bloqueio da
  página/falha de rede: preservar preço/histórico da API, sem número inventado.
- Não usar preço da Steam como original de outra loja, histórico como original,
  percentual agregado de outra edição ou preço PC em console.
- Testar dois jogos, origem oficial/keyshop, oferta divergente, falha do público,
  cache/reinício, identidade alterada e ausência de original.

Arquivos previstos: novo serviço price_enrichment.py, seleção de provedor em
prices.py, controle em ggdeals_connection.py e regressões isoladas. Nenhum arquivo
A4/protegido é necessário. A ativação desta consulta adicional fica para escolha
explícita do dono; não contornar a semântica do fallback existente.

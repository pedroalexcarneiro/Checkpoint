Correção do salvamento e da tela branca de carregamento.

- Reproduzida uma queda nativa no fluxo 0.1.16 ao abrir o carregamento seguinte após salvar. Removido o encadeamento dessas janelas modais.
- Salvar agora grava o jogo imediatamente; a busca de ficha/imagens continua em segundo plano, com indicador na barra inferior e opção de parar após o jogo atual.
- Cadastro pelo Drive, edição identificada e preenchimento em lote seguem o mesmo princípio. Falha de consulta preserva o cadastro.
- Mantidos dados pessoais, imagens existentes, arquivos parciais e schema SQLite 4. Nenhuma credencial nova é exigida.
- Testes de processo completo verificam salvar/renderizar imagens, falha do auxiliar e cadastro Drive. O pacote Windows também precisa passar pelo cadastro completo no executável extraído, com fixture isolada.

Baixe **Checkpoint-0.1.17-windows-x64.zip**, extraia a pasta completa e abra Checkpoint.exe. Preserve `_internal` e `CheckpointUpdater`.

Consulte o arquivo de validação para os resultados Windows desta compilação. As fixtures não comprovam autenticação de conta nem diagnóstico de todas as possíveis falhas no computador do usuário.

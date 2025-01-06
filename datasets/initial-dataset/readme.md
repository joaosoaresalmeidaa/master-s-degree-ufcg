# Initial Dataset - Code Review Analysis with LLaMA-2 13B

Este _dataset_ representa a fase inicial do nosso processo de análise de revisões de código, contendo 19.149 comentários coletados através de uma busca sistemática por palavras-chave relacionadas a _code smells_ em projetos de código aberto.

## Estrutura dos Arquivos

O _dataset_ está dividido em múltiplos arquivos CSV representando diferentes etapas da coleta:


## Processo de Coleta

Os comentários foram coletados usando um conjunto específico de palavras-chave relacionadas a _code smells_, incluindo termos como:
- "smell", "smelly"
- "technical debt"
- "anti-pattern"
- [lista completa disponível na dissertação]

## Estatísticas da Coleta

- Total de comentários: 19.149
- Total de Pull Requests: 6.365

## Próximos Passos

Este dataset inicial passa por um processo de refinamento (disponível em `refined-dataset/`) onde:
1. Os comentários são analisados manualmente para confirmar relevância
2. Falsos positivos são removidos
3. O contexto de cada comentário é verificado

## Uso

Este _dataset_ serve como ponto de partida para análise de discussões sobre _code smells_ em projetos de código aberto, sendo posteriormente refinado para análises mais específicas.

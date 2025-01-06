# Refined Dataset - Code Review Analysis with LLaMA-2 13B

Este dataset representa a segunda fase do nosso processo de análise de revisões de código, contendo 3.023 comentários focados em _code smells_. É o resultado de um processo de refinamento sistemático do _dataset_ inicial - contido na pasta _initial-dataset_ - de 19.149 comentários.

## Processo de Refinamento

O _dataset_ foi criado através de um processo de duas etapas:

1. **Filtragem por Palavras-chave**
   - Aplicação sistemática de palavras-chave relacionadas a _code smells_
   - Palavras-chave baseadas em literatura estabelecida ([Fowler 1997](link), [Zhang et al. 2011](link))

2. **Análise Manual**
   - Validação de relevância por múltiplos pesquisadores
   - Remoção de falsos positivos da filtragem automática
   - Verificação do contexto de cada comentário

## Estrutura do Dataset

O dataset contém o seguinte arquivo:
- `dataset_final.csv`: Metadados do PR + discussões sobre os trechos de modificação do PR, resultando em 3023 comentários

### Campos do Dataset

- `comment_id`: Identificador único do comentário
- `pull_request_url`: URL do Pull Request original
- `diff_hunk`: Trecho de código relacionado ao comentário
- `response_llama`: Revisão gerada pelo LLaMA-2 13B
- `user_id`: Identificador do usuário no github
- `user_login`: Nome da conta do usuário
- `created_at`: Data em que o PR foi criado
- `path`: Caminho do arquivo modificado
- `cleaned_diff_hunk`: Trecho de código modificado com ruído removido(#%@-+)
- `content`: Comentário do revisor humano sobre o trecho de código modificado
- `reason`: Categorização do comentário do humano e do modelo com breve discussão sobre o que é abordado em ambos comentários
- `similarity_percentage`: Percentual de similaridade entre os dois comentários(humano/modelo)
- `code`: Código qualitativo que aborda sobre o contexto das discussões

## Informações adicionais

- Total de comentários: 3.023
- Total de Pull Requests: 2.688

## Citação

```bibtex
[Inserir citação quando publicado]

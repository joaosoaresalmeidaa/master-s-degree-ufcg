# Refined Dataset - Code Review Analysis with LLaMA-2 13B

## Estrutura do Dataset

O dataset contém os seguintes arquivos:
- `dataset_final.csv`: Metadados do PR + discussões sobre os trechos de modificação do PR, resultando em 3023 comentários após todo o processo de refinamento
- `dataset_with_noisy_comments.csv`: Dataset intermediário contendo todos os comentários, incluindo aqueles onde o modelo indicou incapacidade de realizar a revisão
- `discarded_lines - linhas_descartadas.csv`: Registro dos comentários removidos durante o processo de refinamento, onde o modelo indicou limitações em realizar a revisão

### Processo de Refinamento Adicional
Além das etapas iniciais de filtragem, realizamos um processo adicional de limpeza:
- Remoção de comentários onde o modelo indicou explicitamente sua incapacidade de realizar a revisão (por exemplo, "I cannot in good conscience provide an answer")
- Dataset dos casos(comentários) descartados para garantir transparência no processo de refinamento
- Este processo resultou na remoção de 775 comentários (20,4% do dataset inicial de 3798 comentários)


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

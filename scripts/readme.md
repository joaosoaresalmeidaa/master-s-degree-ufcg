# Scripts - Code Review Analysis with LLaMA-2 13B

Este diretório contém todos os scripts e notebooks utilizados para coleta, processamento e análise dos dados da pesquisa.

## Scripts e Notebooks

### Coleta de Dados
- `top_repositories.py`: Script para identificar repositórios do GitHub com maior volume de comentários em PRs
- `sniff-main.zip`: Script de mineração dos repositórios selecionados através da API do GitHub

### Processamento e Limpeza
- `counter_prs.py`: Script para contabilizar o número de Pull Requests em cada dataset
- `clean_data.ipynb`: Notebook para limpeza e pré-processamento dos dados coletados
- `frases_indesejadas.txt`: Lista de frases que indicam limitação do modelo em realizar revisões
- `remove_lines_with_unwanted_phrases.py`: Script para remoção automatizada de comentários contendo frases indesejadas

### Análise dos Dados
- `contagem_tags.ipynb`: Notebook para análise quantitativa das tags/códigos atribuídos às revisões
- `llama_2_review.ipynb`: Notebook para processamento das revisões realizadas pelo modelo LLaMA-2 13B
- `analisys_similarity.ipynb`: Notebook para cálculo e análise de similaridade entre revisões humanas e do modelo

## Fluxo de Execução

1. Coleta inicial com `top_repositories.py` e scripts em `sniff-main.zip`
2. Processamento dos dados brutos com `clean_data.ipynb`
3. Remoção de comentários irrelevantes usando `remove_lines_with_unwanted_phrases.py`
4. Geração de revisões com `llama_2_review.ipynb`
5. Análise de similaridade através de `analisys_similarity.ipynb`
6. Análise quantitativa final com `contagem_tags.ipynb`

## Requisitos

- Python 3.8+
- Jupyter Notebook
- Bibliotecas Python listadas em `requirements.txt`
- Acesso à API do LLaMA-2 13B

## Observações

- Os scripts devem ser executados na ordem especificada no fluxo
- Alguns notebooks requerem arquivos intermediários gerados por scripts anteriores
- Certifique-se de configurar corretamente as credenciais de API quando necessário
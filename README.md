# Investigando como LLaMA-2 13B revisa código-fonte com ênfase em smell

Este repositório contém os dados e _scripts_ utilizados na dissertação de mestrado que investiga como o modelo LLaMA-2 13B realiza revisões de código focadas em _smells_. A pesquisa analisa 3.023 comentários de revisão de código extraídos de projetos de código aberto (Neovim, Keycloak e gRPC).

## Estrutura do Repositório
```
├── datasets/                 # Conjuntos de dados em diferentes estágios
│   ├── initial-dataset/     # Dataset inicial (19.149 comentários)
│   ├── raw-data/            # Dados brutos coletados
│   └── refined-dataset/     # Dataset refinado (3.023 comentários)
│
├── scripts/                 # Scripts de coleta, processamento e análise
│   ├── analisys_similarity.ipynb            # Análise de similaridade
│   ├── clean_data.ipynb                     # Limpeza de dados
│   ├── contagem_tags.ipynb                  # Contagem de tags
│   ├── counter_prs.py                       # Contagem de PRs
│   ├── frases_indesejadas.txt              # Lista de frases para filtro
│   ├── llama_2_review.ipynb                # Execução do LLaMA-2
│   ├── remove_lines_with_unwanted_phrases.py # Remoção de frases indesejadas
│   ├── sniff-main.zip                      # Scripts de mineração
│   └── top_repositories.py                 # Seleção de repositórios
```
## Conjuntos de Dados

- **Dataset Inicial**: 19.149 comentários coletados dos projetos
- **Dataset Refinado**: 3.023 comentários após filtragem e análise manual
- **Raw Data**: Dados brutos da coleta inicial

Cada diretório de _dataset_ possui seu próprio README.md com documentação detalhada.

## Scripts

O diretório `scripts/` contém todos os _notebooks_ e _scripts_ utilizados para:
- Coleta e mineração de dados
- Processamento e limpeza
- Execução das revisões com LLaMA-2
- Análise de similaridade
- Processamento dos resultados

Consulte o README.md na pasta `scripts/` para detalhes sobre cada arquivo.

## Como Utilizar

1. Clone o repositório
2. Configure o ambiente Python com as dependências necessárias:
```bash
pip install -r requirements.txt 
```
3. Consulte os READMEs específicos em cada diretório para instruções detalhadas

## Contato

- João Arthur Brunet Monteiro - joao.arthur@computacao.ufcg.edu.br
- João Victor Soares de Almeida - joaovictorsoares@copin.ufcg.edu.br

## Institucional

Pesquisa desenvolvida como parte de dissertação de mestrado no Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Universidade Federal de Campina Grande (UFCG).

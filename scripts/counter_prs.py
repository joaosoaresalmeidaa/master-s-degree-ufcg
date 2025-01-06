import pandas as pd
import glob

"""
Script responsável por realizar contagem de PRs a partir da coluna pull_request_url
"""
def count_lines_and_prs(directory):
    # Inicializando contadores
    total_lines = 0
    total_unique_prs = set()

    # Iterando por todos os arquivos CSV no diretório fornecido
    for file in glob.glob(f"{directory}/*.csv"):
        print(f"Processando: {file}")
        
        # Carregar o CSV
        try:
            df = pd.read_csv(file)

            # Contar o número de linhas do arquivo
            total_lines += len(df)

            # Coletar PRs únicos
            if 'pull_request_url' in df.columns:
                unique_prs = df['pull_request_url'].unique()
                total_unique_prs.update(unique_prs)
            else:
                print(f"Aviso: 'pull_request_url' não encontrado em {file}")

        except Exception as e:
            print(f"Erro ao processar {file}: {e}")

    # Exibindo resultados finais
    print(f"Total de linhas: {total_lines}")
    print(f"Total de PRs únicos: {len(total_unique_prs)}")

# Caminho para o diretório contendo os arquivos CSV
directory = "./path/to/csvs"  # Substitua pelo caminho correto
count_lines_and_prs(directory)

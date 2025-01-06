import csv

# Carregar as frases indesejadas
with open('/Users/joaosoaresalmeida/Downloads/analise/frases_indesejadas.txt', 'r') as file:
    frases_indesejadas = [line.strip() for line in file.readlines()]

# Filtrar o arquivo CSV
with open('/Users/joaosoaresalmeida/Downloads/analise/dataset_v4.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    filtered_rows = []
    for row in reader:
        if len(row) >= 12:  # Verificar se a linha tem pelo menos 12 colunas
            response_llama = row[12]  # A coluna 12 na indexação do Python é 11
            if not any(frase in response_llama for frase in frases_indesejadas):
                filtered_rows.append(row)

# Escrever o resultado em um novo arquivo CSV
with open('/Users/joaosoaresalmeida/Downloads/analise/dataset_filtered.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)
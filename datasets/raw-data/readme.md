# Datasets de metadados sobre discussões em Pull Requests

Este repositório contém os _datasets_ gerados em setembro de 2023, relacionados às discussões em **Pull Requests (PRs)** com as maiores médias de comentários do GitHub.

## Conteúdo

Os arquivos particionados contêm os metadados das discussões, organizados em um único arquivo compactado dividido em partes. Para descompactar, siga as instruções abaixo.

## Instruções para Recompor e Descompactar

1. Reúna todas as partes na mesma pasta:
   - `part_001.zip`
   - `part_002.zip`
   - `part_003.zip`
   - `part_004.zip`

2. Execute o seguinte comando para combinar as partes em um único arquivo compactado:

   ```bash
   cat part_001.zip part_002.zip part_003.zip part_004.zip > raw-review-comments-data.zip
   ```

3. Descompacte o arquivo unido:

   ```bash
   unzip raw-review-comments-data.zip
   ```

## Observação

Caso tenha dúvidas ou problemas ao manipular os arquivos, entre em contato ou abra uma issue no repositório para suporte.

# Resumo Módulo 3 - Pandas

## Aula 1
- Introdução ao pandas e conceitos

# Aula 2
- Series
    - pd.Series(lista)
    - pd.Series(vetor)
    - pd.Series(vetor, index= [0, 1, 2, 3])
- #Series cria um index automaticamente caso nao seja argumentado
- Se criado a partir de dicionarios, é transformado em index o campo chave
    - pd.Series({"chave": valor})

- DataFrames
    - pd.DataFrame(serie / dicionario, index= [0, 1, 2], columns= [colum, colum])
    - Precisa ser passado um index
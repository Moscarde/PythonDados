# Resumo Módulo 3 - Pandas

## Aula 1
- Introdução ao pandas e conceitos

## Aula 2
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

## Aula 3
- Indices e manipulações
- Passando uma coluna para o indice
    - df = df.set_index('coluna')
- Resetando index
    - df = df.reset_index()
- Setando um novo index
    - df.index = ['a', "b", "c"]

- Datas
    - range de datas
    - pd.date_range('1/4/2000', periods= 4) #4 dias sequenciais
    - pd.date_range(start= '1/1/2000', end= '31/12/2000', freq = 'M') #ultimos dias dos meses
    - Definindo index como datas
    - filtro por index de datas
    - cotacao_weg[cotacao_weg.index > '2000-02-25']
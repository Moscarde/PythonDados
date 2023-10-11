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

## Aula 4
- Colunas
- Trocando nome das colunas
    - df.columns = ["coluna1", "coluna3", "coluna3"]
- Filtros por coluna
    - df.coluna
    - df['coluna']
- Filtro por colunas
    - df[["coluna1", "coluna1"]]
    - df[lista_colunas]
- Filtros retornam series com valores e index
- Boa prática é setar a data como index antes de extrair as colunas
- Filtros com condicoes
    - df[df[coluna] > 20]
    - df[(df[coluna] > 20) & (df[coluna] < 30)]
    - & e / ou |

## Aula 5
- loc
    - df.loc['WEGE']
        - retorna uma ou mais linhas correspondentes com valores de todas as colunas
    - df.loc['WEGE', 'preco']
        - retorna uma ou mais linhas correspondentes com valores de todas as colunas
    - também pode ser inserido range de datas
    - df.loc['2014-01-05': '2014-01-07']
- at
    - funcionamento similar ao loc
    - prioriza valores unicos
    - nao usa range de valores
- iloc
    - df.iloc[:3, :]
        - filtra com indices numericos pela ordem das colunas e linhas
        - retorna um ou mais itens
- iat
    - df.iat[1, 4]
        - retorna um item unico na posição especifica

- Atualização de dados
    - loc pode alterar multiplos dados 
    - at altera valores unicos

## Aula 6
- operações entre series e dataframes
    - serie_cotacoes * serie_euro
- criando nova coluna no df com calculo de outras colunas
    - df['p_l'] = df['cotacao'] / df['lucro_por_acao']
- puxando resultados de colunas
    - sum, mean, std, min, max
    - cumsum

## Aula 7
- ordenacao
    - sort_index()
        - ascending = False
- axis = 1 ~> muda o eixo do método
- ordenação por coluna
    - sort_values(by = '' ou [''])
- rank
    - empresas['ranking_padrao'] = empresas['preco_sobre_lucro'].rank()
    - (method = 'max' , 'min', 'dense')

## Aula 8
- lendo arquivos excel - xlsx
- retorna o diretorio atual
    - os.getcwd()
- muda o diretorio de trabalho para o argumentado
    - os.chdir()
- lendo arquivos excel
    - pd.read_excel()
- parametros para tratamento / leitura
    - skiprows= 6 ~~> pula uma quantidade de linhas 
    - index_col= 'Data' ~~> usa uma coluna como index
    - na_values='nd' ~~> define o valor para Na's
    - decimal = ',' ~~> define a seraracao decimal
- removendo valores ausentes
    - df.dropna()
- exportando dados para xlsx
    -df.to_excel('')

## Aula 9
- lendo arquivos csv
    - pd.read_csv()
- parametros
    - sep = ';' ~~> define o separador
    - encoding = 'ISO-8859-1' ~~> define o encoding
- exportando dados para csv
    - df.to_csv('', sep = ';')
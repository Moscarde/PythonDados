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

## Aula 10
- teoria
- biblioteca pandas data reader
- dados mercado financeiro
    - AlphaVantage - dados intraday
    - The Investors Exchange - dados de ações, ETFs e fundos
    - Moscow, Quandl, Tiingo, Yahoo Finance - dados de ações, ETFs e fundos
- dados especificos de financas
    - Fama-French Data - Dados sobre factor investing
    - NASDAQ - Todos os simbolos negociados
    - Naver Finance - dados mercado coreano
    - Stooq.com - Dados de indices
- dados economia
    - Federal Reserve Economic Data (FRED) - Dados da economia americana
    - Bank of Canada - ... canadense
    - Econdb - Economia mundial
    - Organisation for Economic Co-operation and Development (OECD) - Indicadores economicos
    - World Bank - Indicadores economicos
- dados gerais
    - Enigma - Dados genericos como todos os recalls de comida dos eua
    - Eurostat - Dados genericos da ue
    - Thrift Saving Plan(TSP) - dados do fundo de pensao eua

## Aula 11
- yahoofince / yfinance as yf
- buscar dados de acao
    - yf.download(tickers = acao ou [])
- parametros
    - start= '2010-01-01' ~~> inicio
    - end= datetime.now() ~~> fim
    - interval = '1wk' ~~> intervalo
- primeiros resultados
    - df.head(10)

## Aula 12
- puxando dados do Fred com o pandas_datareader
    - pdr.get_data_fred('codigo', inicio, final)
- plotagem de graficos
    - df.plot()

## Aula 13
- puxando dados do world database
    - from pandas_datareader import wb
- puxando indicadores direto da biblioteca
    - wb.get_indicators()
    - wb.search('gdp.*capita.*const')
- wb.download()
    - indicator='NY.GDP.PCAP.KD',
    - country = ['MX', 'BRA'], ~~> codigo paises ISO 3166
    - start=2000,
    - end= 2023
- groupby('col')
- .droplevel(level= 0)

## Aula 14
- puxando dados de factor investing

## Aula 15 Python + MySQL
- Rever aula

## Aula 16
- Tratando dados na
    - df.dropna()
- Parametros
    - how= 'all' ~~> remove apenas linhas em que todos os valores são na
    - subset=['empresa', 'cotacao'] ~~> remove somente as linhas as colunas predefinidas são NA
- Preenchendo dados na
    - df.fillna(0)
    - method='ffill' ~~> preenche com o dado anterior
    - limit= 2 ~~> limite de sequencia de preenchimento

## Aula 17
- Filtrar valores unicos de uma coluna
    - Serie.unique() ~> retorna um array com valores unicos
    - usado para criação de loops
    - porem groupby atende melhor 
- removendo itens duplicados
    - .drop_duplicates(subset='coluna')
    - remove na ordem de index
    - caso precise filtrar a remoção, deve reordenar o index antes
    
## Aula 18
- Mudando o tipo de dado de uma coluna
    - coluna.astype(ind / str)
    - pd.to_datetime(coluna['data'], formnat= '%d/%m/%Y') ~~> str para data
- Trocando valores
    - coluna.replace(incial, final) ~~> inicial pode ser []
    - coluna.str.replace() ~~> para substituir valores fracionados de strings precisa usar o metodo str

## Aula 19
- Operacoes com valores de colunas
    - map(lambda)
    
## Aula 20
- Fatiando / seccionando dados
    - pd.cut(divisoes, serie)
    - pd.value_counts(valores_fatiados) ~~> conta quantos valores se repetem em cada divisao
    - pd.get_dummies(valores_fatiados) ~~> transformar a amostra em variaveis dummys
        - dtype= int

## Aula 21
- Meltando tabelas
    - Transformando tabelas largas em tabelas compridas
    - Processo para usar o groupby
- Formula
    - reset_index() ~> Garantindo que data seja uma coluna, para salvar os valores
    - pd.melt(df, param)
    ou
    - df.melt(param)
        - id_vars = 'Date'
        - var_name = 'Empresa'
        - value_name = 'Price'
- Usando o groupby ou filtrando busca
    - df.groupby('empresa')['price'].mean()

    - df[df['empresa'] == 'WEGE3.SA]
- Revertendo com pivot_table
    - pd.pivot_table(df, param)
    ou
    - df.pivot_table(param)
        - index = 'Date'
        - collumns = 'Empresa'
    - df.droplevel(level = 0, axis = 1)

## Aula 22
- Juntando DFs
- Concat, Merge, Join
- Concat junta dfs sem levar em consideração nenhuma chave ou coluna, apenas agrupa / empilha
- Merge precisa selecionar por qual chave vai combinar valores e a forma de agrupar
- Join - Entra dados de uma df em outro atual, baseado ou nao no index
- pd.concat([dfs])
    - ignore_index= True #ignora o index, mais usado quando valores nao sao baseado em datas e os index são mais aleatorios
- pd.merge(df1, df2, how, left_on, right_on)
    - how = left, right, inner, outer
- df1.join(df2)

- deletando uma coluna de um df
    - df.drop('col', axis=1)


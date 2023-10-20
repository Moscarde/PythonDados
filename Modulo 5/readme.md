# Resumo Módulo 5 - MatPlotLib

## Aula 1
- Matplotlib
- Plotagem com OO
    - fig, ax = plt.subplots()
    - ax.plot(df.index, df['x'])
    - ax.plot(df.index, df['y'])
- Plotagem com pyplot
    - plt.plot(df)


## Aula 2 - pyplot
- plt.plot(x, y)
- df.plot()
    - x = valores para eixo x
    - y = valores para eixo y
- grafico em linha
- grafico em barra
    - .plot(kind = bar)
    - df_anual.plot.bar(stacked = False)
        - stacked = visualização de barra empilhada
    - df.plot.barh()
        - horizontal
- grafico em área
    - df.plot.area()
- histograma - frequencia
    - df.plot.hist(bins= 100)
- boxsplot
    - df.plot.box()
- grafico de dispersao
    - df.plot.scatter(x = '', y = '', c = '', cmap = 'viridis' )
        - x, y = eixos
        - c = cor dos pontos (data)
    
## Aula 3 - figuras e eixos - OO
- fig, ax = plt.subplots()
    - (Matriz)
    - figsize = ()
    - sharey / sharex ~> compartilha y ou x no mosaico
    - plt.subplots(2, 2, figsize = 20, 15)
        - ax[0, 0].plot()
- ax.plot(Series / array / df)
    - ax.plot(np.random.random(10))
    - ax.plot(cotacao.index, cotacao.values)
    - ax.grid(True)

## Aula 4 - 5 label nos eixos e titulos
- set_xlabel('label', params)
- set_ylabel('label', params)
- set_title('title', params)
    - color =''
    - labelpad =15
    - fontsize =12
    - fontweight = 'bold'

## Aula 6 - Manipulação de eixos - Escalas
- set_xlim(valor minimo, valor maximo)
- set_ylim(valor minimo, valor maximo)
- set_yscale('log')
    - escala em log permite visualizar melhor as quedas e subidas expondenciais quando se tem um grafico muito comprido e achatado

## Aula 7 - Legendas
- ax.legend(loc = 0)
    - locations 
    - 0 = best
    - 1 = upper right
    - 2 = upper left
    - ...
    - 10 = center
- ⚠ precisa passar uma string em label =  no param do ax.plot()

## Aula 8 - Personalizar o eixo dos graficos
- formatando eixo
    - valor em reais
        - ax.yaxis.set_major_formatter('R${x:1.2f}')
    - exibição da data
        - ax.xaxis.set_major_formatter(mdate.DateFormatter('%b-%Y'))
    - exibição em porcentagem
        - ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))

- eixo em determinada frequencia
    - ax.xaxis.set_major_locator()
        - mdate.YearLocator(5) ~> apenas em eixos de datas

- quando eixo é numérico
    - redefinir frequencia ou nomes
        - ax.xaxis.set_ticks([0, 2000, 4000], ['Inicio', 'Meio', 'Fim'])

## Aula 9 -  Estilização e cores
- cor da linha / barra
    - ax.plot(x, y, color = 'CODE')
- cor do fundo
    - ax.set_facecolor('CODE')
- style
    - plt.style.use('ggplot')
    - plt.style.use('cyberpunk')
        - precisa instalar e importar

## Aula 10 - Grafico em barras
- ax.bar(x, y, label, width, align)
    - dfs que usam mesmo index acabam se batendo no grafico
        - numero_de_trimestres = 4
        - posicao_barras = np.arange(numero_de_trimestres)([0, 1, 2, 3])
        - largura_barras = 0.3
        - bar1 = ax.bar(posicao_barras, df_lucros.Weg.values, label = 'Weg', width=largura_barras)
        - ax.bar_label(bar1)

- buscando serie ipca e igp-m
- ax.axhline(y = 0, color = 'black')

## Aula 11 - Histograma, Dispersão, Boxplot
- formatter
    - mtick.PercentFormatter(1, decimals = 0)
- ax.hist(series.values, bins = 120)
    - bins = <>

- graficos de dispersão
    - ax.scatter(series1, series2, c = array.like, cmap = 'cool')
        - plt.colorbar(color)
    - barra continua, barra_discreta

- ax.boxplot(x = retornos_mensais)

## Aula 12 - Seaborn
- ++ Outra forma de plotar graficos em grid
- import seaborn as sns
- Linha
    - sns.lineplot(data=)
- Histograma
    - sns.histplot(data= , bins 150)
- Regressao linear
    - sns.regplot(x=, y= , line_kws={"color": ""})
- Boxplot
    - sns.boxplot()

## Aula 13 - Annotations
- Insere anotações com flechas em determinadas datas
    - ax.annotate(
        Texto,
        xy= (data, cotacoes.asof(data) + 2800), #posicao seta
        xytext = (data, cotacoes.asof(data) + 9000), #posicao texto
        arrowprops = dict(facecolor = 'black', headwidth = 4, width = 2, headlength = 4),
        horizontalalignment = 'right', verticalalignment = 'top')

## Aula 14 - Animações
- Funcao animate(i)
    - data fracionada + plot
        data = janela_cor_weg.iloc[:int(i+1)]
        weg = ax.plot(data.index, data.values, color = '#00FFFF',   label = "WEGE3")
    
- ani = FuncAnimation(fig, animate, frames = range(0, len(cotacoes)), interval= 10, repeat = False)

## Aula 15 - Seaborn - Mapa de calor
- para exemplificar foi calculado o valor anualizado de retornos janelas moveis de 1 ano para periodos de 1, 3, 5, 10 anos
- foi criado um df com as tabelas em periodos e linhas em acoes
- ax = sns.heatmap(tabela_janelas_moveis, annot=True, cmap= 'Blues', fmt= 'g')
- plt.yticks(rotation = 0)
- colocar % no texto
    - for t in ax.texts:
        -t.set_text(t.get_text() + '%')

## Aula 16 - Mapa de calor mensal com quantstats qs
- cotacoes.resample('M').last().pct_change().dropna()
- qs.extend_pandas()
- df.plot_monthly_heatmap()
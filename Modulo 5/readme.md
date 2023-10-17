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

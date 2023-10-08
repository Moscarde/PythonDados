# Resumo Módulo 3

## Aula 1 - 2
- NumPy
- Vetores a partir de lista
    - np.array(lista)
- Arranjo sequencial
    - np.arange(min, max, espç)
- Arrays de 0 ou 1s
    - np.zeros(qtd)
    - np.ones(qtd)
- Matrizes
    - np.matrix(lista)
- Lista x Array
- Vetores aleatorios
    - np.random.rand(3, 2)
        - Numero aleatorios independente da ling
    - np.random.randint(low = , high = , size =)
        - Numero aleat inteiro
    - np.random.uniform(low = , high = , size =)
        - numero aleatorio podendo ser negativo(colocar no campo lower)

    
## Aula 3
- Metodos x Atributos
    - obj.atributo
    - obj.metodo()
<!-- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html -->

## Aula 4
- Selecionando posiçoes
    -array[0]
    -array[-1]
- Filtrando os dados
    -array[array > 19]

## [Aula 5](Aula 5.ipynb)
- Concatenando arrays
    - np.concatenate([array1, array2, ...])
- Splitando arrays
    - array1, array2 = np.split(array_maior, [pos])
- Inserindo dados em arrays
    - np.append(array, elem)
    - np.insert(array, pos, elem)
- Deletando elem
    - np.delete(array, pos)
- Reshape
    - np.reshape(3, 3) #3x3
- Operações dentro de arrays
    - array[condição] = elem
- Ordenação
    - np.sort(array) #crescente
    - -np.sort(-array) #decrescente
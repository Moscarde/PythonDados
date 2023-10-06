# Resumo Módulo 2

## Aula 2

- Introdução a variaveis
- Declaração, exibição e cálculos

## Aula 3

- Comentários

## Aula 4

- Objetos e seus tipos
- Conversões
- String variável

## Aula 5

- Inputs
- Calculos com inputs

## Aula 6 - 7

- Operadores Matemáticos
- Ordem de precedência

## Aula 8 - 9

- Modulos e bibliotecas
- Random

## Aula 10 - 11

- Colecoes
- Tuplas
- Listas
- Manipulalção de listas
    - Insersão '.append'
    - Selecionar elemento '[]'
    - Selecionar varios elemento '[:3]'
    - Alterar elemento '[1] = 'test''
    - Inserindo elemento na pos escolhida '.insert(pos, elem)'
    - Removendo elemento '.remove(elem)' || del list[pos]
    - Verificando se um elemento está na lista 'elem in list' ~> True / False
    - Junção de lista
    - Ordenação de lista 'sorted(lista, reverse=True)'
    - Tamanho da lista 'len(lista)'
    - Extraindo valores 'max() min() sum()'

## Aula 12

- Sets
    - .set()
    - .add()
    - .update([1, 2, 3])
    - .discard(elem)
- Operações entre sets
    - .union()
    - .intersection()
    - .difference()

## Aula 13

- Dicionários {chave:valor, chave:valor} dict({})
- Adicionar itens 
    - .update({})
    -['chave'] = valor
- Remover itens
    - .pop('chave')

## Aula 14

- Regex
- Manipulação de strings
    - .startswith()
    - .endswith()
- Filtro por Regex
    - import re
    - expressao = re.compile(padrao)
    - expressao.findall(texto)
- Validacao com regex
    - re.fullmatch(expressao, texto)

## Aula 15 - 16

- Condicionais
- if, elif, else
- and or

## Aula 17 - 18

- Loops
- loop com lista
    - for i in list:
- loop com range
    - for i in range(0, 3):
- loop com enumerate - lista
    - for indice, item in list:

- While

## Aula 19 - 20

- Funçoes
- Retornos
- Função Lambda
- Map
    - Aplica uma funcao a todos os itens da lista e retorna
- Lambda como argumento no map
    - list(map(lambda x: x * 0.2, lista))

## Aula 21

- Try
- Except
- Else
- Finaly

## Aula 22

- List Comprehensions
- Filter
    - Passa um lambda com condicional
    - Caso retorne True, é adicionado a lista
- Map
    - Passa uma ação para ser executado em todos

## Aula 23

- datetime
    - timedelta
    - date
    - datetime
- conversão str ~> date
    - datetime.strptime(str, 'formatacao')
- timedelta
- relativedelta
- timezones
    - pytz

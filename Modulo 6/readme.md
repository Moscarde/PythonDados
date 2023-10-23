# Módulo 6 - OO

- Classe

  - Instancia <-> Classe
  - Classe.atributo **de instancia**
  - Classe.função / metodo **de instancia**()
  - Classe.função / metodo **contrutor**()
  - Clase.funcao / metodo **estatico**()
    - metodo sem argumento / sem interação com a classe
  - atributo "de classe" "global" ~> usado como base para calculos de metodos

- Getter / Setter

  - Tratamento de dados

- Variaveis publicas e privadas

  - var = ... **publica**
  - \_var = ... **restrita**
  - \_\_var = ... **privada**

  - mesma logica tambem pode ser aplicada a funcoes

## Aula 8 - 9 - Associacoes - Agregação 
- atributo de uma classe sendo instancia de outra classe
- executando metodos de outra classe
- classes  existem de forma independente

## Aula 10 - Composicao
- uma classe é dona de outra classe
- é criado um objeto dentro de um metodo de uma classe
- Empresa <~ Enderecos

## Snippets

```
    int(self.cnpj.replace('.', '').replace('/', '').replace('-',''))
    int(''.join(numero for numero in self.cnpj if numero.isdigit()))
```

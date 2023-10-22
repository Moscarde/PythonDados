from icecream import ic


class Empresa:
    ano_atual = 2023
     
    def __init__(self, nome, ticker, data_de_fundacao, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.ticker = ticker
        self.data_de_fundacao = data_de_fundacao


    def tempo_existencia(self):
    #precisa passar o self por ser um método de instancia, só é possivel executar com os atributos dela
        self.anos_existencia = self.ano_atual - self.data_de_fundacao
        print(f"A empresa existe há {self.anos_existencia} anos")
        return(self.anos_existencia)
    
    def cnpj_int(self):
        return int(''.join(numero for numero in self.cnpj if numero.isdigit()))


if __name__ == "__main__":
    weg = Empresa(nome="WEG", ticker="WEGE3", data_de_fundacao = 1998, cnpj = '84.429.695/0001-11')
    ic(weg.nome)
    ic(weg.tempo_existencia())
    ic(weg.cnpj_int())

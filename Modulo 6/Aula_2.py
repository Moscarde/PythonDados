from icecream import ic


class Empresa:
    def __init__(self, nome, ticker, data_de_fundacao, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.ticker = ticker
        self.data_de_fundacao = data_de_fundacao


class Carro:
    def __init__(self, cor, direcao):
        self.cor = cor
        self.direcao = direcao


weg = Empresa(nome="WEG", ticker="WEGE3", data_de_fundacao = 1998, cnpj = 10293014012943)
carro_gabriel = Carro(cor="Prata", direcao="Manual")

if __name__ == "__main__":
    ic(weg.nome)
    ic(carro_gabriel.cor)
    ic(Carro)

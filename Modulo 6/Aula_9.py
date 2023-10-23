from icecream import ic


class Carteira_investimentos:
    def __init__(self, nome_pessoa):
        self.proprietario = nome_pessoa
        self.carteira = []

    def adicionar_acao(self, acao):
        if type(acao) == list:
            for i in acao:
                self.carteira.append(i)
        else:
            self.carteira.append(acao)

    def listar_acoes(self):
        for acao in self.carteira:
            print(acao.ticker, acao.nome_empresa)


class Acoes:
    def __init__(self, ticker, nome_empresa):
        self.ticker = ticker
        self.nome_empresa = nome_empresa


# criando carteira
carteira = Carteira_investimentos("Gabriel")

# criando acoes
weg = Acoes('WEGE3', 'Weg')
petro = Acoes('PETR3', 'Petrobras')

carteira.adicionar_acao([weg, petro])

carteira.listar_acoes()

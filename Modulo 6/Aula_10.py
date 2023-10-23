from icecream import ic

class Empresa:

    def __init__(self, nome_empresa, ticker):
        self.nome = nome_empresa
        self.ticker = ticker
        self.enderecos = [] #uma empresa pode ter diversos enderecos

    def adicionar_endereco(self, cidade, estado, pais):
        self.enderecos.append(Enderecos(cidade, estado, pais))

    def listar_enderecos(self):
        for i in self.enderecos:
            print(f'{i.cidade} - {i.estado} - {i.pais}')

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Enderecos:

    def __init__(self, cidade, estado, pais):
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __del__(self):
        print(f'{self.cidade} foi apagado')


vale = Empresa('Vale', 'VALE3')
vale.adicionar_endereco('rio', 'rj', 'Brasil')
vale.listar_enderecos()

print('-' * 20)
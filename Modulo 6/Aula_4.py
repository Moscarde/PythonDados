from icecream import ic


class Empresa:
    # atributo de classe
    ano_atual = 2023
     
    # construtor
    def __init__(self, nome, ticker, data_de_fundacao, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.ticker = ticker
        self.data_de_fundacao = data_de_fundacao

    #metodo de instancia
    def tempo_existencia(self):
        #precisa passar o self por ser um método de instancia, só é possivel executar com os atributos dela
        self.anos_existencia = self.ano_atual - self.data_de_fundacao
        print(f"A empresa existe há {self.anos_existencia} anos")
        return(self.anos_existencia)
    
    #metodo de instancia
    def cnpj_int(self):
        # return int(''.join(numero for numero in self.cnpj if numero.isdigit()))
        return int(self.cnpj.replace('.', '').replace('/', '').replace('-',''))

    @classmethod
    def criando_empresa_por_tempo_de_existencia(cls, anos_existencia, nome, ticker, cnpj):
        #utilizando o atributo de classe ano_atual
        data_de_fundacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, data_de_fundacao, cnpj)

    @classmethod
    def criando_empresa_com_codigo_completo(cls, nome, ticker, codigo_ticker, data_de_fundacao, cnpj):
        ticker = ticker + str(codigo_ticker)
        return cls(nome, ticker, data_de_fundacao, cnpj)



if __name__ == "__main__":
    weg = Empresa(nome="WEG", ticker="WEGE3", data_de_fundacao = 1998, cnpj = '84.429.695/0001-11')
    ic(weg.nome)
    ic(weg.tempo_existencia())
    ic(weg.cnpj_int())

    petro = Empresa.criando_empresa_com_codigo_completo('Petrobras', 'PETR', 4, 1990, 1244123124)
    ic(petro.ticker)

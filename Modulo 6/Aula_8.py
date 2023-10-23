from icecream import ic

class Cotacoes_empresa:
    def __init__(self):

        self.cotacoes = [20, 20.30, 21, 22],
        self.bd = Banco_de_dados('1234', 'Gabriel')

    def soma_cotacoes(self):
        return print(sum(self.cotacoes))

    def colocar_cotacoes_na_base_de_dados(self):
        self.bd.iniciar_conexao()
        colocar_dados = (self.bd.conexao, self.cotacoes)
        print('Dados no banco')
        

        

class Banco_de_dados:

    def __init__(self, senha, user):
        self.senha = senha
        self.user = user

    def iniciar_conexao(self):
        self.conexao = self.user + self.senha
        print('conexão iniciada')


teste_cotacoes = Cotacoes_empresa()

teste_cotacoes.colocar_cotacoes_na_base_de_dados()
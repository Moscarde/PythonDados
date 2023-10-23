from icecream import ic

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_de_futebol(self):
        print(f'{self.nome} fala sobre futebol')

class Investidor(Pessoa):
    
    def investindo(self):
        print(f'{self.nome} Está comprando acoes')

class Jogador(Pessoa):
    
    def jogando(self):
        print(f'{self.nome} está jogando')


Ronaldinho = Jogador('Ronaldo', 'Nazario')
Ronaldinho.jogando()
Gabriel = Investidor('Gabriel', 'Moscard')
Gabriel.investindo()
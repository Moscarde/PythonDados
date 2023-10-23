import wget
from icecream import ic


class Cvm:
    def __init__(self):
        self.site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"
        self._site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"
        self.__site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"

    def pegando_itr(self, ano_arquivo):
        url = self.__site + f'itr_cia_aberta_{ano_arquivo}.zip'
        wget.download(url)



baixando_dados = Cvm()
#baixando_dados.site = 'meca' #erro
#baixando_dados._site = 'meca' #erro
baixando_dados.__site = 'meca' #sem erro


baixando_dados.pegando_itr(2022)
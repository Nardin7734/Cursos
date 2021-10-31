import requests


class BuscaEndereco:

    def __init__(self, cep):
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!')

    def __str__(self):
        return self.formata_cep()

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def pesquisa_cep(self):
        url ='https://viacep.com.br/ws/{}/json/'.format(self.cep)
        requisicao = requests.get(url)
        dados = requisicao.json()
        return {
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        }


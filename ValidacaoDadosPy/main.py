from datetime import datetime, timedelta
from datas_br import DatasBr

from acesso_cep import BuscaEndereco

cep = '95901560'

obj = BuscaEndereco(cep)

print(obj.pesquisa_cep())
import re
from validate_docbr import CPF


def cpf_e_valido(cpf):
    cpf_instance = CPF()
    return cpf_instance.validate(cpf)


def nome_e_valido(nome):
    return nome.isalpha()


def rg_e_valido(rg):
    return len(rg) == 9


def celular_e_valido(celular):
    """Valida celular no formato XX XXXXX-XXXX"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

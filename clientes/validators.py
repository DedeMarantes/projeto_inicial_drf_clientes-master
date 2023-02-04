import re

from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
        return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}' # regex celular ex: 11 98456-6698
    resposta = re.findall(model, celular)
    return resposta
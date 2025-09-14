# app/validators.py
import re

def is_cpf_valid(cpf: str) -> bool:
    """
    Valida um CPF brasileiro. Retorna True se for válido, False caso contrário.
    """
    # 1. Garante que o input é uma string
    cpf = str(cpf)

    # 2. Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)

    # 3. Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # 4. Verifica se todos os dígitos são iguais (ex: 111.111.111-11), o que é inválido
    if cpf == cpf[0] * 11:
        return False

    # 5. Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    
    if resto != int(cpf[9]):
        return False

    # 6. Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    
    if resto != int(cpf[10]):
        return False

    # Se passou por todas as verificações, o CPF é válido
    return True


def is_cnpj_valid(cnpj: str) -> bool:
    """
    Valida um CNPJ brasileiro.
    """
    cnpj = str(cnpj)
    cnpj = re.sub(r'[^0-9]', '', cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 5
    for i in range(12):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso < 2:
            peso = 9
    
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    if digito1 != int(cnpj[12]):
        return False

    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 6
    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso < 2:
            peso = 9

    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if digito2 != int(cnpj[13]):
        return False

    return True
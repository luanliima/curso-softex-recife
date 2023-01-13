from logging import exception


def calcular_imc (peso, altura):

    if (peso < 0) or (altura < 0):
        raise exception("valores preenchidos incorretamente")

    imc = (peso) / (altura * ltura)

    return imc   
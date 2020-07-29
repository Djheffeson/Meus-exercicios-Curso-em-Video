def metade(valor=0):
    return valor / 2


def dobro(valor=0):
    return valor * 2


def aumentar(valor=0, porcentagem=0):
    aumento = (valor / 100) * porcentagem
    return valor + aumento


def diminuir(valor=0, porcentagem=0):
    corte = (valor / 100) * porcentagem
    return valor - corte


def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')

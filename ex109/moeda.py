def metade(valor=0.0, formatar=''):
    res = valor / 2
    if formatar != '':
        return moeda(res, formatar)
    else:
        return res


def dobro(valor=0.0, formatar=''):
    res = valor * 2
    if formatar != '':
        return moeda(res, formatar)
    else:
        return res * 2


def aumentar(valor=0.0, porcentagem=0, formatar=''):
    aumento = (valor / 100) * porcentagem
    res = aumento + valor
    if formatar != '':
        return moeda(res, formatar)
    else:
        return res


def diminuir(valor=0.0, porcentagem=0, formatar=''):
    corte = (valor / 100) * porcentagem
    res = valor - corte
    if formatar != '':
        return moeda(res, formatar)
    else:
        return res


def moeda(valor=0.0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')

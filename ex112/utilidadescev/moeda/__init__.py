def resumo(valor, aumento=0, diminuicao=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, "R$")}')
    print(f'Metade do preço: \t{metade(valor, "R$")}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, "R$")}')
    print(f'{diminuicao}% de redução: \t{diminuir(valor, diminuicao, "R$")}')

    print('-' * 30)


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

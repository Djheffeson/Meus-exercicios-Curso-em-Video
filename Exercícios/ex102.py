def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: 0 número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: 0 valor do fatorial de um número n.
    """
    print('-'*30)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end=' ')
            if c == 1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    print(f)


# Programa Principal

fatorial(5, show=True)
help(fatorial)

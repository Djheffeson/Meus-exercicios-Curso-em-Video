def leia_dinheiro(entrada):
    while True:
        valor = input(entrada).replace(',', '.').strip()
        valor = verificar(valor)
        if type(valor) == float:
            return valor


def verificar(valor):
    check = valor
    if '.' in check:
        check = check.replace('.', '')

    if check.isnumeric():
        valor = float(valor)

    if type(valor) != float:
        print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
    else:
        return valor

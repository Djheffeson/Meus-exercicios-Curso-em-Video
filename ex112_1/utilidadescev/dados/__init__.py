def leia_dinheiro(entrada):
    valido = False
    while not valido:
        valor = input(entrada).replace(',', '.').strip()
        try:
            return float(valor)
        except:
            print(f'\033[0;31m"{valor}" Não é um preço válido.\033[m')

def visualizar():
    print('–' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('–' * 40)
    arquivo = open('cadastrados.txt', 'r')
    lista = arquivo.readlines()
    nomes = list()
    idades = list()
    pessoas = list()
    arquivo.close()
    for i, v in enumerate(lista):
        if i % 2 == 0:
            nomes.append(v)
        else:
            idades.append(v)

    for i, v in enumerate(nomes):
        pessoas.append([nomes[i].strip(), idades[i].strip()])

    for c in pessoas:
        space = 30 - len(c[0])
        print(f'{c[0]}{" "*space}{c[1]:>} anos')

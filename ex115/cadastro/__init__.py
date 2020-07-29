def cadastrar():
    print('–' * 40)
    print('NOVO CADASTRO'.center(40))
    print('–' * 40)

    nome = str(input('Nome: ')).strip().lower().title()
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[0;31mDigite um número inteiro válido!\033[m')
        else:
            break

    arquivo = open('cadastrados.txt', 'a')
    arquivo.write(f'{nome}\n')
    arquivo.write(f'{idade}\n')
    arquivo.close()

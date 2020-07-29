def leiaint(num):
    print('-'*30)
    num = input('Digite um número: ')
    while not num.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        num = input('Digite um número: ')
    return num


# Programa Principal

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

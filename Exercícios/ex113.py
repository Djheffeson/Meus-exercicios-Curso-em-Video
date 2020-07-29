def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro: Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.')
            num = 0
            break
        else:
            break
    return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro: Digite um número inteiro válido. \033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.')
            num = 0
            break
        else:
            break
    return num


# Programa principal
numint = leiaInt('Digite um inteiro: ')
numfloat = leiaFloat('Digite um real: ')

print(f'O valor inteiro digitado foi {numint} e o real foi {numfloat:.2f}')

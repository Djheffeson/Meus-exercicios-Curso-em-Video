from time import sleep

c = ('\033[m',  # Sem cor
     '\033[0;30;41m',  # vermelho
     '\033[0;30;44m',  # Azul
     '\033[0;30;42m',  # Verde
     '\033[7;30m',  # Branco
     )


def ajuda(lib):
    título(f"Acessando o manual de comando '{lib}'", 2)
    sleep(1)
    print(c[4])
    help(lib)
    print(c[0], end='')
    sleep(1)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)
    print(c[0], end='')


# Programa principal
while True:
    título('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO!', 1)

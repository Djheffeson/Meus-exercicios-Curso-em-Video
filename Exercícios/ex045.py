from time import sleep
from random import randint
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
if jogador == 0 or jogador == 1 or jogador == 2:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)
    if computador == 0: #O computador jogou Pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
    elif computador == 1: #O computador jogou Papel
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
    elif computador == 2: #O computador jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
else:
    print('\033[31mJOGADA INVÁLIDA!')

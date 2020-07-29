from random import randint
from time import sleep
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
computador = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
if jogador == 0 and computador == 1:
    print('-='*11)
    print('Computador jogou Papel\nJogador jogou Pedra')
    print('-='*11)
    print('COMPUTADOR VENCE')
elif jogador == 0 and computador == 2:
    print('-=' * 11)
    print('Computador jogou Tesoura\nJogador jogou Pedra')
    print('-='*11)
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 0:
    print('-=' * 11)
    print('Computador jogou Pedra\nJogador jogou Papel')
    print('-=' * 11)
    print('COMPUTADOR VENCE')
elif jogador == 1 and computador == 2:
    print('-=' * 11)
    print('Computador jogou Tesoura\nJogador jogou Papel')
    print('-=' * 11)
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 0:
    print('-=' * 11)
    print('Computador jogou Pedra\nJogador jogou Tesoura')
    print('-=' * 11)
    print('JOGADOR VENCE')
elif jogador == 2 and computador == 1:
    print('-=' * 11)
    print('Computador jogou Papel\nJogador jogou Tesoura')
    print('-=' * 11)
    print('JOGADOR VENCE')
elif jogador == computador:
    print('EMPATE')